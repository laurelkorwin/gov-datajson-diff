# Change History for nasa.json (Part 167)

### Changes from 31606f9 to dd2190f (Part 156/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_POD_orbits_gps_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_POD_orbits_gps_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1645925,166 +1645904,189 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2761716853-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "solid earth",
+                "tectonics",
+                "gravity/gravitational field",
+                "earth science",
+                "geodetics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_daily_POD_orbits_gps_001",
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
+            "temporal": "2023-10-01T00:00:00Z/2024-11-18T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS daily accumulated real-time POD orbits (60-second sampling, 24-hour files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-AMPG-N-NDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Amateur Observation Network contains 2170 entries of photographic materials. The data files (which are kept at JPL) consist of five types as follows: contact prints, negatives, prints, slides, and transparencies through 1988 February 16.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ampg-n-ndr-halley-v1.0_xqnv-wbf8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-AMPG-N-NDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ampg-n-ndr-halley-v1.0_xqnv-wbf8",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Amateur Observation Network contains 2170 entries of photographic materials. The data files (which are kept at JPL) consist of five types as follows: contact prints, negatives, prints, slides, and transparencies through 1988 February 16.",
-            "title": "IHW COMET HALLEY NON_DIGITAL PHOTOGRAPHIC MATERIAL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY NON_DIGITAL PHOTOGRAPHIC MATERIAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHGAM-4FA1A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Australian Bureau of Meteorology. 2019-09-18. GHRSST Level 4 GAMSSA Global Foundation Sea Surface Temperature Analysis. Version 1.0. GHRSST L4 Australian Global Multi-Sensor SST Analysis (GAMSSA), daily, 1/4 degree resolution. Australian Bureau of Meteorology, Melbourne, Australia. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHGAM-4FA1A. http://www.bom.gov.au/australia/charts/bulletins/apob77.pdf.",
-            "issued": "2019-08-23",
-            "temporal": "2008-07-23T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-23",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C2036881735-POCLOUD",
-            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) Level 4 sea surface temperature analysis, produced daily on an operational basis at the Australian Bureau of Meteorology (BoM) using optimal interpolation (OI) on a global 0.25 degree grid. This Global Australian Multi-Sensor SST Analysis (GAMSSA) v1.0 system blends satellite SST observations from passive infrared and passive microwave radiometers with in situ data from ships, drifting buoys and moorings from the Global Telecommunications System (GTS). SST observations that have experienced recent surface wind speeds less than 6 m/s during the day or less than 2 m/s during night are rejected from the analysis.  The processing results in daily foundation SST estimates that are largely free of nocturnal cooling and diurnal warming effects.  Sea ice concentrations are supplied by the NOAA/NCEP 12.7 km sea ice analysis.  In the absence of observations, the analysis relaxes to the Reynolds and Smith (1994) Monthly 1 degree SST climatology for 1961 - 1990.",
-            "release-place": "Australian Bureau of Meteorology, Melbourne, Australia",
-            "series-name": "GHRSST Level 4 GAMSSA Global Foundation Sea Surface Temperature Analysis",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Australian Bureau of Meteorology",
-            "title": "GHRSST Level 4 GAMSSA_28km Global Foundation Sea Surface Temperature Analysis v1.0 dataset (GDS2)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GAMSSA_28km-ABOM-L4-GLOB-v01.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) Level 4 sea surface temperature analysis, produced daily on an operational basis at the Australian Bureau of Meteorology (BoM) using optimal interpolation (OI) on a global 0.25 degree grid. This Global Australian Multi-Sensor SST Analysis (GAMSSA) v1.0 system blends satellite SST observations from passive infrared and passive microwave radiometers with in situ data from ships, drifting buoys and moorings from the Global Telecommunications System (GTS). SST observations that have experienced recent surface wind speeds less than 6 m/s during the day or less than 2 m/s during night are rejected from the analysis.  The processing results in daily foundation SST estimates that are largely free of nocturnal cooling and diurnal warming effects.  Sea ice concentrations are supplied by the NOAA/NCEP 12.7 km sea ice analysis.  In the absence of observations, the analysis relaxes to the Reynolds and Smith (1994) Monthly 1 degree SST climatology for 1961 - 1990.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHGAM-4FA1A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHGAM-4FA1A",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GAMSSA_28km-ABOM-L4-GLOB-v01.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GAMSSA_28km-ABOM-L4-GLOB-v01.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.ghrsst.org",
-                    "description": "GHRSST Project",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project",
+                    "downloadURL": "http://www.ghrsst.org",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036881735-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036881735-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036881735-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036881735-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GAMSSA_28km-ABOM-L4-GLOB-v01.jpg",
+            "identifier": "C2036881735-POCLOUD",
+            "issued": "2019-08-23",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHGAM-4FA1A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Australian Bureau of Meteorology, Melbourne, Australia",
+            "series-name": "GHRSST Level 4 GAMSSA Global Foundation Sea Surface Temperature Analysis",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2008-07-23T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 4 GAMSSA_28km Global Foundation Sea Surface Temperature Analysis v1.0 dataset (GDS2)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-RIVKIN-THREE-MICRON-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is a collection of 3-micron spectra of 33 asteroids and Phobos and Deimos obtained by Andy Rivkin and collaborators. Nearly all these data have been published.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-rivkin-three-micron-v3.0_xqxk-vp8t",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "129 antigone",
                 "55 pandora",
@@ -1646124,310 +1646126,288 @@
                 "369 aeria",
                 "77 frigga"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-RIVKIN-THREE-MICRON-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-rivkin-three-micron-v3.0_xqxk-vp8t",
-            "description": "This data set is a collection of 3-micron spectra of 33 asteroids and Phobos and Deimos obtained by Andy Rivkin and collaborators. Nearly all these data have been published.",
-            "title": "RIVKIN THREE MICRON ASTEROID DATA V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "RIVKIN THREE MICRON ASTEROID DATA V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCICA-2-CVP-RAW-V2.0",
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
+            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during the commissioning phase. Data of the solar wind was\nobtained, as well as some data with very high background levels.\nData set version 2 replaces a previously delivered data set.\nImportant changes are the ordering of the energy levels which now\ngo from low to high and that the quality flag in the labels is\nupdated.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcica-2-cvp-raw-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCICA-2-CVP-RAW-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcica-2-cvp-raw-v2.0",
-            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during the commissioning phase. Data of the solar wind was\nobtained, as well as some data with very high background levels.\nData set version 2 replaces a previously delivered data set.\nImportant changes are the ordering of the energy levels which now\ngo from low to high and that the quality flag in the labels is\nupdated.",
-            "title": "ROSETTA-ORBITER CHECK RPCICA 2 CVP UNCALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RPCICA 2 CVP UNCALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/419",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Matthews, E.G. 1999. Global Vegetation Types, 1971-1982 (Matthews). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/419",
-            "issued": "2023-11-21",
-            "temporal": "1971-01-01T00:00:00Z/1982-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
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
-            "identifier": "C2808090466-ORNL_CLOUD",
             "description": "A global digital data base of vegetation was compiled at 1 degree latitude by 1 degree longitude resolution, drawing on approximately 100 published sources.  Vegetation data from varied sources were consistently recorded using the hierarchical UNESCO classification system.  The raw data base distinguishes about 180 vegetation types that have been collapsed to 32.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Global Vegetation Types, 1971-1982 (Matthews)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/419_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F419",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F419",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/MatthewsVegetation/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/MatthewsVegetation/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/matthews_global_veg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/matthews_global_veg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/419",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/419",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/MatthewsVegetation/comp/matthews_global_veg.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/MatthewsVegetation/comp/matthews_global_veg.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/MatthewsVegetation/comp/readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/MatthewsVegetation/comp/readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/MatthewsVegetation/comp/veg1x1.help",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/MatthewsVegetation/comp/veg1x1.help",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/419_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/419_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=419",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=419",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/419_1_fit.png",
+            "identifier": "C2808090466-ORNL_CLOUD",
+            "issued": "2023-11-21",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/419",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1971-01-01T00:00:00Z/1982-01-01T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Vegetation Types, 1971-1982 (Matthews)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0712-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-16T21:23:00.000 to 2015-04-17T08:00:28.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0712-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0712-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0712-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-16T21:23:00.000 to 2015-04-17T08:00:28.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0712 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0712 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/skbg-kf16",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Circum-Arctic Map of Permafrost and Ground-Ice Conditions, Version 2. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/skbg-kf16.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "keyword": [
-                "frozen ground",
-                "earth science",
-                "cryosphere",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "J. Heginbottom",
                 "hasEmail": "mailto:heginbottom@gsc.emr.ca"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206814-NSIDCV0",
             "description": "The Circum-Arctic permafrost and ground ice map is available via ftp in ESRI Shapefile format and Equal-Area Scalable Earth Grid (EASE-Grid) format. See the Format section for an explanation of the files provided via FTP.\n\nThe circumpolar permafrost and ground ice data contribute to a unified international data set that depicts the distribution and properties of permafrost and ground ice in the Northern Hemisphere (20\u00b0N to 90\u00b0N). The re-gridded data set shows discontinuous, sporadic, or isolated permafrost boundaries. Permafrost extent is estimated in percent area (90-100 percent, 50-90 percent, 10-50 percent, <10 percent, and no permafrost). Relative abundance of ground ice in the upper 20 m is estimated in percent volume (>20 percent, 10-20 percent, <10 percent, and 0 percent). The data set also contains the location of subsea and relict permafrost. the gridded data are gridded at 12.5 km, 25 km, and 0.5 degree resolution. The shapefiles were derived from the original 1:10,000,000 paper map (Brown et al. 1997)\n\nPermafrost, or permanently frozen ground, is ground (soil, sediment, or rock) that remains at or below 0\u00b0C for at least two years (Permafrost Subcommittee, 1988). It occurs both on land and beneath offshore arctic continental shelves, and underlies about 22 percent of the Earth's land surface.\n\nFor more information on the creation of the original map, see Heginbottom et al. (1993). The original paper map also includes information on the relative abundance of ice wedges, massive ice bodies and Pingos, ranges of permafrost temperature and thickness (Brown et al. 1997).",
-            "title": "Circum-Arctic Map of Permafrost and Ground-Ice Conditions, Version 2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fskbg-kf16",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fskbg-kf16",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD318_or.html?major_version=2",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD318_or.html?major_version=2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/skbg-kf16",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/skbg-kf16",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/skbg-kf16",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/skbg-kf16",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206814-NSIDCV0",
+            "issued": "2019-09-20",
+            "keyword": [
+                "frozen ground",
+                "earth science",
+                "cryosphere",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.7265/skbg-kf16",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 28.0 180.0 90.0",
+            "temporal": "1970-01-01T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Circum-Arctic Map of Permafrost and Ground-Ice Conditions, Version 2"
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
-                "data",
-                "sharad",
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
-            "identifier": "NASA-435",
             "description": "SHARAD",
-            "title": "PDS MRO SHARAD Radargram Release 1",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1646435,23 +1646415,52 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-435",
+            "issued": "2018-06-25",
+            "keyword": [
+                "data",
+                "sharad",
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
+            "title": "PDS MRO SHARAD Radargram Release 1"
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
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_upper_xc_0.9_cm_0.115.dat",
+                    "mediaType": "application/dat"
+                }
             ],
+            "identifier": "NASA-851__10",
+            "issued": "2018-06-25",
             "keyword": [
                 "turbulence",
                 "tangential",
@@ -1646463,270 +1646472,237 @@
                 "airfoil",
                 "validation"
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
-            "identifier": "NASA-851__10",
-            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_upper_xc_0.9_cm_0.115.dat",
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
-            "landingPage": "https://doi.org/10.7927/H4542KJV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rosenzweig, C., P. Neofotis, M. Vicarelii, and X. Xing. 2008-12-31. IPCC Fourth Assessment Report (AR4) Observed Climate Change Impacts Database. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4542KJV. https://doi.org/10.7927/H4542KJV.",
-            "issued": "2008-12-31",
-            "temporal": "1970-01-01T00:00:00Z/2014-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4N29TWJ",
-                "https://doi.org/10.7927/H4RV0KMH",
-                "https://doi.org/10.7927/H4HD7SKJ",
-                "https://doi.org/10.7927/H41C1TT4",
-                "https://doi.org/10.7927/H4WM1BB7",
-                "https://doi.org/10.7927/H4XG9P2R",
-                "https://doi.org/10.7927/H4FT8J0X"
-            ],
-            "keyword": [
-                "earth science",
-                "human dimensions",
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
-            "identifier": "C179002027-SEDAC",
-            "description": "The Intergovernmental Panel on Climate Change (IPCC) Fourth Assessment Report (AR4) Observed Climate Change Impacts Database contains observed responses to climate change across a wide range of systems as well as regions. These data were taken from the Intergovernmental Panel on Climate Change Fourth Assessment Report and Rosenzweig et al. (2008). It consists of responses in the the physical, terrestrial biological systems and marine-ecosystems. The observations that were selected include data that demonstrate a statistically significant trend in change in either direction in systems related to temperature or other climate change variable, and the is for at least 20 years between 1970 and 2004, although study periods may extend earlier or later. For each observation, the data series is described in terms of system, region, longitude and latitude, dates and duration, statistical significance, type of impact, and whether or not land use was identified as a driving factor. System changes are taken from ~80 studies (of which ~75 are new since the IPCC Third Assessment Report) containing more than 29,500 data series. Observations in the database are characterized as a \"change consistent with warming\" or a \"change not consistent with warming\", based on information from the underlying studies.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Rosenzweig, C., P. Neofotis, M. Vicarelii, and X. Xing",
-            "title": "IPCC Fourth Assessment Report (AR4) Observed Climate Change Impacts Database",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-ar5-observed-climate-impacts-v2-01/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Intergovernmental Panel on Climate Change (IPCC) Fourth Assessment Report (AR4) Observed Climate Change Impacts Database contains observed responses to climate change across a wide range of systems as well as regions. These data were taken from the Intergovernmental Panel on Climate Change Fourth Assessment Report and Rosenzweig et al. (2008). It consists of responses in the the physical, terrestrial biological systems and marine-ecosystems. The observations that were selected include data that demonstrate a statistically significant trend in change in either direction in systems related to temperature or other climate change variable, and the is for at least 20 years between 1970 and 2004, although study periods may extend earlier or later. For each observation, the data series is described in terms of system, region, longitude and latitude, dates and duration, statistical significance, type of impact, and whether or not land use was identified as a driving factor. System changes are taken from ~80 studies (of which ~75 are new since the IPCC Third Assessment Report) containing more than 29,500 data series. Observations in the database are characterized as a \"change consistent with warming\" or a \"change not consistent with warming\", based on information from the underlying studies.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4542KJV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4542KJV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-ar5-observed-climate-impacts-v2-01/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-ar5-observed-climate-impacts-v2-01/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-ar4-observed-climate-impacts/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-ar4-observed-climate-impacts/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/ipcc-ar4-observed-climate-impacts/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/ipcc-ar4-observed-climate-impacts/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-ar4-observed-climate-impacts/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-ar4-observed-climate-impacts/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-ar4-observed-climate-impacts",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-ar4-observed-climate-impacts",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-ar5-observed-climate-impacts-v2-01/sedac-logo.jpg",
+            "identifier": "C179002027-SEDAC",
+            "issued": "2008-12-31",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "environmental impacts"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4542KJV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4N29TWJ",
+                "https://doi.org/10.7927/H4RV0KMH",
+                "https://doi.org/10.7927/H4HD7SKJ",
+                "https://doi.org/10.7927/H41C1TT4",
+                "https://doi.org/10.7927/H4WM1BB7",
+                "https://doi.org/10.7927/H4XG9P2R",
+                "https://doi.org/10.7927/H4FT8J0X"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-01-01T00:00:00Z/2014-12-31T00:00:00Z",
             "theme": [
                 "IPCC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IPCC Fourth Assessment Report (AR4) Observed Climate Change Impacts Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1243-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-08T06:54:45.000 to 2015-12-08T11:37:49.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1243-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1243-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1243-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-08T06:54:45.000 to 2015-12-08T11:37:49.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1243 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1243 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP02MOD_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2021-12-31. VIIRS/NPP Moderate Resolution Bands L1B 6-Min Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VNP02MOD_NRT.002. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt.",
-            "issued": "2021-12-15",
-            "temporal": "2021-12-15T00:00:00Z/2024-09-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "spectral/engineering",
-                "infrared wavelengths"
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
-            "identifier": "C2185497928-LANCEMODIS",
-            "description": "The VIIRS/NPP Moderate Resolution Bands L1B 6-Min Swath 750m Near Real Time (NRT) product, short-name VNP02MOD_NRT is among the VIIRS Level 1 and Level 2 swath products that are generated from the processing of 6 minutes of VIIRS data acquired during the S-NPP satellite overpass. The VIIRS sensor has 16 moderate-resolution channels (M-bands) that have 16 detectors (16 rows of pixels per scan), that span the wavelengths from 0.412 micrometer to 12.1 micrometer. The VNP02MOD product is comprised of 16 bands that are sensitive to visible, near-infrared (NIR), and thermal wavelengths.\r\n\r\nThe spatial resolution of the instrument at viewing nadir is approximately 750 m for the Moderate-resolution and Day/Night Bands, and 375m for the Imagery bands.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/NPP Moderate Resolution Bands L1B 6-Min Swath 750 m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/NPP Moderate Resolution Bands L1B 6-Min Swath 750m Near Real Time (NRT) product, short-name VNP02MOD_NRT is among the VIIRS Level 1 and Level 2 swath products that are generated from the processing of 6 minutes of VIIRS data acquired during the S-NPP satellite overpass. The VIIRS sensor has 16 moderate-resolution channels (M-bands) that have 16 detectors (16 rows of pixels per scan), that span the wavelengths from 0.412 micrometer to 12.1 micrometer. The VNP02MOD product is comprised of 16 bands that are sensitive to visible, near-infrared (NIR), and thermal wavelengths.\r\n\r\nThe spatial resolution of the instrument at viewing nadir is approximately 750 m for the Moderate-resolution and Day/Night Bands, and 375m for the Imagery bands.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP02MOD_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP02MOD_NRT.002",
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
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP02MOD_NRT",
-                    "description": "Direct access to the download site and directory hosting the VNP02MOD_NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the VNP02MOD_NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP02MOD_NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2185497928-LANCEMODIS",
+            "issued": "2021-12-15",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP02MOD_NRT.002",
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
+            "title": "VIIRS/NPP Moderate Resolution Bands L1B 6-Min Swath 750 m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-04-08",
-            "temporal": "2021-04-08T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "station",
-                "international",
-                "topo",
-                "location",
-                "space",
-                "coords",
-                "ephemeris",
-                "iss",
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
-            "identifier": "nasa-iss-data_2021-04-08",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-04-08",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1646849,99 +1646825,97 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-04-08",
+            "issued": "2021-04-08",
+            "keyword": [
+                "station",
+                "international",
+                "topo",
+                "location",
+                "space",
+                "coords",
+                "ephemeris",
+                "iss",
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
+            "temporal": "2021-04-08T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-04-08"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROLIS-2-FSS-V1.0",
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
+            "description": "This archive contains raw images from the ROLIS instrument onboard ROSETTA Lander, acquired during the FSS phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the ROLIS experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-rolis-2-fss-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROLIS-2-FSS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-rolis-2-fss-v1.0",
-            "description": "This archive contains raw images from the ROLIS instrument onboard ROSETTA Lander, acquired during the FSS phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the ROLIS experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P ROLIS 2 FSS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P ROLIS 2 FSS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TSIS/TIM/DATA307",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Greg Kopp. 2023-11-07. TSIS_TSI_L3_06HR. Version 04. TSIS TIM Level 3 Total Solar Irradiance 6-Hour Means V04. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/TSIS/TIM/DATA307. https://disc.gsfc.nasa.gov/datacollection/TSIS_TSI_L3_06HR_04.html. Digital Science Data.",
-            "issued": "2023-11-03",
-            "temporal": "2018-01-11T00:00:00Z/2023-11-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-03",
-            "references": [
-                "https://doi.org/10.1007/s11207-005-7446-4",
-                "https://doi.org/10.1007/s11207-005-7447-3"
-            ],
-            "keyword": [
-                "sun-earth interactions",
-                "solar activity",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GREG KOPP",
                 "hasEmail": "mailto:Greg.Kopp@lasp.colorado.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2797642655-GES_DISC",
-            "description": "Version 04 is the current release of this data product, and supercedes all previous versions.\n\nThe TSIS TIM Level 3 Total Solar Irradiance (TSI) 6-Hour Means data product (TSIS_TSI_L3_06HR) uses measurements from the Total Irradiance Monitor (TIM) instrument over the entire spectrum, and averages them over a 6-hour period. TSIS-1 was launched on December 15, 2017 and mounted on the International Space Station (ISS) on December 30, 2017. TIM instrument has long-term repeatability with estimated uncertainties less than 0.014 W/m^2/yr (10 ppm/yr). Accuracy is currently reported as 0.48 W/m^2 (350 ppm), but expected to decrease as calibrations are refined and incorporated. Irradiances are reported at a mean solar distance of 1 AU and zero relative line-of-sight velocity with respect to the Sun.\n\nAll of the data from this product are arranged into a single file in a tabular ASCII text format which can be easily read into a spreadsheet application. New data are appended to the file on a daily basis. The columns contain the date, Julian day, minimum wavelength, maximum wavelength, instrument mode, data version number, irradiance value, irradiance uncertainty, and data quality. The rows are arranged with data at each wavelength over the full TIM wavelength range, repeating for each day for the length of the mission.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TSIS_TSI_L3_06HR",
             "creator": "Greg Kopp",
-            "title": "TSIS TIM Level 3 Total Solar Irradiance 6-Hour Means V04 (TSIS_TSI_L3_06HR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/images/TSIS_TSI_L3_06HR_04.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 04 is the current release of this data product, and supercedes all previous versions.\n\nThe TSIS TIM Level 3 Total Solar Irradiance (TSI) 6-Hour Means data product (TSIS_TSI_L3_06HR) uses measurements from the Total Irradiance Monitor (TIM) instrument over the entire spectrum, and averages them over a 6-hour period. TSIS-1 was launched on December 15, 2017 and mounted on the International Space Station (ISS) on December 30, 2017. TIM instrument has long-term repeatability with estimated uncertainties less than 0.014 W/m^2/yr (10 ppm/yr). Accuracy is currently reported as 0.48 W/m^2 (350 ppm), but expected to decrease as calibrations are refined and incorporated. Irradiances are reported at a mean solar distance of 1 AU and zero relative line-of-sight velocity with respect to the Sun.\n\nAll of the data from this product are arranged into a single file in a tabular ASCII text format which can be easily read into a spreadsheet application. New data are appended to the file on a daily basis. The columns contain the date, Julian day, minimum wavelength, maximum wavelength, instrument mode, data version number, irradiance value, irradiance uncertainty, and data quality. The rows are arranged with data at each wavelength over the full TIM wavelength range, repeating for each day for the length of the mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTSIS%2FTIM%2FDATA307",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTSIS%2FTIM%2FDATA307",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1646951,181 +1646925,221 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TSIS_TSI_L3_06HR_04.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TSIS_TSI_L3_06HR_04.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TSIS_Level3/TSIS_TSI_L3_06HR.04/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TSIS_Level3/TSIS_TSI_L3_06HR.04/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TSIS_TSI_L3_06HR_04",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TSIS_TSI_L3_06HR_04",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TSIS_Level3/TSIS_TSI_L3_06HR.04/doc/README.TSIS.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TSIS_Level3/TSIS_TSI_L3_06HR.04/doc/README.TSIS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/159520RevA_TSIS_Data_User_Guide.pdf",
-                    "description": "TSIS-1 Science Data Products Guide",
                     "@type": "dcat:Distribution",
+                    "description": "TSIS-1 Science Data Products Guide",
+                    "downloadURL": "http://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/159520RevA_TSIS_Data_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/TSIS_TIM_V04_Release_Notes_20200528.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "http://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/TSIS_TIM_V04_Release_Notes_20200528.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/tsis/instruments/tim-total-irradiance-monitor/",
-                    "description": "TIM Instrument Information",
                     "@type": "dcat:Distribution",
+                    "description": "TIM Instrument Information",
+                    "downloadURL": "http://lasp.colorado.edu/home/tsis/instruments/tim-total-irradiance-monitor/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/TSIS_Algorithm_Theoretical_Basis_Document_151430RevA.pdf",
-                    "description": "TSIS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "TSIS ATBD",
+                    "downloadURL": "http://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/TSIS_Algorithm_Theoretical_Basis_Document_151430RevA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/2020-ATBD-TIM-update.pdf",
-                    "description": "TSIS ATBD TSI post-launch update",
                     "@type": "dcat:Distribution",
+                    "description": "TSIS ATBD TSI post-launch update",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/2020-ATBD-TIM-update.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/tsis/reference/publications/",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "http://lasp.colorado.edu/home/tsis/reference/publications/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/tsis/",
-                    "description": "TSIS Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "TSIS Project Home Page.",
+                    "downloadURL": "http://lasp.colorado.edu/home/tsis/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/data/tsis/file_readers/read_lasp_ascii_file.pro",
-                    "description": "IDL-based read software.",
                     "@type": "dcat:Distribution",
+                    "description": "IDL-based read software.",
+                    "downloadURL": "http://lasp.colorado.edu/data/tsis/file_readers/read_lasp_ascii_file.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/images/TSIS_TSI_L3_06HR_04.png",
+            "identifier": "C2797642655-GES_DISC",
+            "issued": "2023-11-03",
+            "keyword": [
+                "sun-earth interactions",
+                "solar activity",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TSIS/TIM/DATA307",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1007/s11207-005-7446-4",
+                "https://doi.org/10.1007/s11207-005-7447-3"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TSIS_TSI_L3_06HR",
+            "temporal": "2018-01-11T00:00:00Z/2023-11-13T00:00:00Z",
             "theme": [
                 "TSIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TSIS TIM Level 3 Total Solar Irradiance 6-Hour Means V04 (TSIS_TSI_L3_06HR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-4-RDR-TARGETED-V1.0",
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
-                "mars reconnaissance orbiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This volume contains the CRISM Targeted Empirical Record (TER) archive, a collection of multiband image cubes derived from targeted (gimbaled) observations of Mars' surface acquired by the Compact Reconnaissance Imaging Spectrometer for Mars (CRISM) instrument on the Mars Reconnaissance Orbiter (MRO) spacecraft. Post-processing attempts to represent the spectrum the instrument would have measured looking at the surface of Mars at a standard illumination geometry, in the absence of atmospheric gases, with aerosol scattering normalized to that at the geometry within the observation that is closest to nadir, in the absence of instrument artifacts. A series of value added products represent spatial variability in signatures of minerals of interest. The data are still in sensor space, allowing map projection using terrain models of the Martian surface that are of better accuracy or spatial resolution than was used to generate the companion Map-projected Targeted Reduced Data Record (MTR) archive.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-4-rdr-targeted-v1.0_xrms-rd4c",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-4-RDR-TARGETED-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-4-rdr-targeted-v1.0_xrms-rd4c",
-            "description": "This volume contains the CRISM Targeted Empirical Record (TER) archive, a collection of multiband image cubes derived from targeted (gimbaled) observations of Mars' surface acquired by the Compact Reconnaissance Imaging Spectrometer for Mars (CRISM) instrument on the Mars Reconnaissance Orbiter (MRO) spacecraft. Post-processing attempts to represent the spectrum the instrument would have measured looking at the surface of Mars at a standard illumination geometry, in the absence of atmospheric gases, with aerosol scattering normalized to that at the geometry within the observation that is closest to nadir, in the absence of instrument artifacts. A series of value added products represent spatial variability in signatures of minerals of interest. The data are still in sensor space, allowing map projection using terrain models of the Martian surface that are of better accuracy or spatial resolution than was used to generate the companion Map-projected Targeted Reduced Data Record (MTR) archive.",
-            "title": "MRO CRISM TARGETED EMPIRICAL RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MRO CRISM TARGETED EMPIRICAL RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1328-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-10T17:09:10.000 to 2016-01-11T00:51:17.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1328-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1328-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1328-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-10T17:09:10.000 to 2016-01-11T00:51:17.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1328 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1328 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition13/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "Press kit for ISS mission Expedition 13 from 03/2006-09/2006. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Press Kit PDF",
+                    "downloadURL": "http://www.nasa.gov/pdf/146654main_Expedition_13_Press_Kit.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "ISS 13 Press Kit"
+                }
+            ],
+            "identifier": "OCIO-Fitara-25",
             "issued": "2006-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "press kit",
                 "mission",
@@ -1647137,269 +1647151,233 @@
                 "2006",
                 "13"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition13/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:037"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "JSC"
             },
-            "identifier": "OCIO-Fitara-25",
-            "description": "Press kit for ISS mission Expedition 13 from 03/2006-09/2006. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
-            "title": "ISS Expedition 13 Press Kit",
-            "programCode": [
-                "026:037"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/146654main_Expedition_13_Press_Kit.pdf",
-                    "description": "Press Kit PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "ISS 13 Press Kit"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ISS Expedition 13 Press Kit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFTAB-2-RDR-CROMMELIN-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irftab-2-rdr-crommelin-v1.0_xrqw-ebqv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFTAB-2-RDR-CROMMELIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irftab-2-rdr-crommelin-v1.0_xrqw-ebqv",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET IRFTAB EDITED REDUCED DATA RECORD CROMMELIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET IRFTAB EDITED REDUCED DATA RECORD CROMMELIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEaSUREs/LSTE/GEOLST4KHR.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Kerry Cawse-Nicholson. GEOLST4KHR.002. Geostationary Earth Orbit Land Surface Temperature Hourly North and South America 4 km V002. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC. https://doi.org/10.5067/MEaSUREs/LSTE/GEOLST4KHR.002. https://doi.org/10.5067/MEaSUREs/LSTE/GEOLST4KHR.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-11-17",
-            "temporal": "2000-04-01T00:00:00Z/2024-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-12",
-            "keyword": [
-                "land surface",
-                "surface thermal properties",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kerry Cawse-Nicholson",
                 "hasEmail": "mailto:kerry-anne.cawse-nicholson@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2167682875-LPDAAC_ECS",
-            "description": "The NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) GEOLST4KHR version 2 swath product provides per-pixel Land Surface Temperature (LST) with a spatial resolution of 4,000 meters (m). The product is produced daily in hourly increments using data acquired from Geostationary Operational Environmental Satellite (GOES) 8 and 10 through 17 satellites for the years 2000 through 2023. The GEOLST4KHR product provides LST values for both North and South America. The GEOLST4KHR data product utilizes the Modern-Era Retrospective analysis for Research and Applications Version 2 / Radiative Transfer for TIROS Operational Vertical Sounder (MERRA-2/RTTOV) Single-Channel Emissivity-Combined ASTER and MODIS Emissivity over Land (CAMEL) algorithm.\n\nThe GEOLST4KHR product provides layers for cloud mask, latitude, longitude, land surface temperature, and land surface temperature error. A low-resolution browse is also available showing land surface temperature as an RGB (red, green, blue) image in JPEG format.",
-            "series-name": "GEOLST4KHR.002",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Kerry Cawse-Nicholson",
-            "title": "Geostationary Earth Orbit Land Surface Temperature Hourly North and South America 4 km V002",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.11.25/GEOLST4KHR_201612291600_002_20210714015139.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) GEOLST4KHR version 2 swath product provides per-pixel Land Surface Temperature (LST) with a spatial resolution of 4,000 meters (m). The product is produced daily in hourly increments using data acquired from Geostationary Operational Environmental Satellite (GOES) 8 and 10 through 17 satellites for the years 2000 through 2023. The GEOLST4KHR product provides LST values for both North and South America. The GEOLST4KHR data product utilizes the Modern-Era Retrospective analysis for Research and Applications Version 2 / Radiative Transfer for TIROS Operational Vertical Sounder (MERRA-2/RTTOV) Single-Channel Emissivity-Combined ASTER and MODIS Emissivity over Land (CAMEL) algorithm.\n\nThe GEOLST4KHR product provides layers for cloud mask, latitude, longitude, land surface temperature, and land surface temperature error. A low-resolution browse is also available showing land surface temperature as an RGB (red, green, blue) image in JPEG format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEaSUREs%2FLSTE%2FGEOLST4KHR.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEaSUREs%2FLSTE%2FGEOLST4KHR.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MEaSUREs/LSTE/GEOLST4KHR.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MEaSUREs/LSTE/GEOLST4KHR.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MEASURES/GEOLST4KHR.002/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MEASURES/GEOLST4KHR.002/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2167682875-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2167682875-LPDAAC_ECS",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1317/GEOLST_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1317/GEOLST_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.11.25/GEOLST4KHR_201612291600_002_20210714015139.1.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.11.25/GEOLST4KHR_201612291600_002_20210714015139.1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1316/GEOLST_UserGuide_V2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1316/GEOLST_UserGuide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://git.earthdata.nasa.gov/projects/LPDUR/repos/lstegeo-swath2grid/browse",
-                    "description": "GEOLST4KHR Swath to Grid Conversion Python Script",
                     "@type": "dcat:Distribution",
+                    "description": "GEOLST4KHR Swath to Grid Conversion Python Script",
+                    "downloadURL": "https://git.earthdata.nasa.gov/projects/LPDUR/repos/lstegeo-swath2grid/browse",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/GEOLST/GEOLST4KHR.002/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/GEOLST/GEOLST4KHR.002/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.11.25/GEOLST4KHR_201612291600_002_20210714015139.1.jpg",
+            "identifier": "C2167682875-LPDAAC_ECS",
+            "issued": "2021-11-17",
+            "keyword": [
+                "land surface",
+                "surface thermal properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEaSUREs/LSTE/GEOLST4KHR.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "series-name": "GEOLST4KHR.002",
             "spatial": "-180.0 -20.9590268 3.4957049 71.8922429",
+            "temporal": "2000-04-01T00:00:00Z/2024-01-01T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geostationary Earth Orbit Land Surface Temperature Hourly North and South America 4 km V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V5.0",
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
+            "description": "This data set is intended to include all groundbased asteroid radar detections. These entries were collected by Steven J. Ostro (1989) [OSTRO1989] and selected data have been provided as collected from the published literature. A null value (e.g., '9.99') in any particular column indicates that the corresponding datum was not available in the published paper. For example, for monostatic radar observations, circular polarization ratio cannot be derived, so the value in this column is '9.99'. In some cases, the data provided in the paper are too complex to be presented in the table, as in the case of a time-series of values.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v5.0_xrsg-hy4j",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V5.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v5.0_xrsg-hy4j",
-            "description": "This data set is intended to include all groundbased asteroid radar detections. These entries were collected by Steven J. Ostro (1989) [OSTRO1989] and selected data have been provided as collected from the published literature. A null value (e.g., '9.99') in any particular column indicates that the corresponding datum was not available in the published paper. For example, for monostatic radar observations, circular polarization ratio cannot be derived, so the value in this column is '9.99'. In some cases, the data provided in the paper are too complex to be presented in the table, as in the case of a time-series of values.",
-            "title": "ASTEROID RADAR V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID RADAR V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA314",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gille, John and Gray, Lesley J.. 2013-08-19. HIR3SCOL. Version 007. HIRDLS/Aura Level 3 Daily Gridded 1 x 1 deg Stratospheric Columns of NO2 V007. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/HIRDLS/DATA314. https://disc.gsfc.nasa.gov/datacollection/HIR3SCOL_007.html. Digital Science Data.",
-            "issued": "2013-05-06",
-            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-06",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
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
-            "identifier": "C1251101014-GES_DISC",
-            "description": "HIR3SCOL is the EOS High Resolution Dynamics Limb Sounder (HIRDLS/Aura) level 3 daily gridded 1 x 1 deg. stratospheric columns of NO2 (nitrogen dioxide) data product. The data are gridded at 1 x 1 degree resolution from +80 to -64 degrees latitude. The stratospheric column is computed from data at 57 to 1.0 hPa. The product consists of one file spanning the entire ~3 year HIRDLS mission from January 22, 2005 through March 17, 2008. Users of the HIR3SCOL data product should read the Version 7 HIRDLS Data Description and Quality document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF5. The data file contains one grid object with data fields, attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HIR3SCOL",
             "creator": "Gille, John and Gray, Lesley J.",
-            "title": "HIRDLS/Aura Level 3 Daily Gridded 1 x 1 deg Stratospheric Columns of NO2 V007 (HIR3SCOL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HIR3SCOL_007.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "HIR3SCOL is the EOS High Resolution Dynamics Limb Sounder (HIRDLS/Aura) level 3 daily gridded 1 x 1 deg. stratospheric columns of NO2 (nitrogen dioxide) data product. The data are gridded at 1 x 1 degree resolution from +80 to -64 degrees latitude. The stratospheric column is computed from data at 57 to 1.0 hPa. The product consists of one file spanning the entire ~3 year HIRDLS mission from January 22, 2005 through March 17, 2008. Users of the HIR3SCOL data product should read the Version 7 HIRDLS Data Description and Quality document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF5. The data file contains one grid object with data fields, attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA314",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA314",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1647409,134 +1647387,132 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HIR3SCOL_007.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HIR3SCOL_007.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/HIR3SCOL.007/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/HIR3SCOL.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/HIR3SCOL.007/HIRDLS-Aura_L3SCOL_v07-00-20-c01_2005d022-2008d077.he5.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/HIR3SCOL.007/HIRDLS-Aura_L3SCOL_v07-00-20-c01_2005d022-2008d077.he5.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HIR3SCOL_007",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HIR3SCOL_007",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HIR3SCOL_007.png",
+            "identifier": "C1251101014-GES_DISC",
+            "issued": "2013-05-06",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA314",
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
+            "series-name": "HIR3SCOL",
             "spatial": "-180.0 -64.0 180.0 80.0",
+            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HIRDLS/Aura Level 3 Daily Gridded 1 x 1 deg Stratospheric Columns of NO2 V007 (HIR3SCOL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/782/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
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
-            "identifier": "DASHLINK_782",
             "description": "Model-based prognostics approaches employ do- main knowledge about a system, its components, and how they fail through the use of physics-based models. Compo- nent wear is driven by several different degradation phenom- ena, each resulting in their own damage progression path, overlapping to contribute to the overall degradation of the component. We develop a model-based prognostics method- ology using particle filters, in which the problem of charac- terizing multiple damage progression paths is cast as a joint state-parameter estimation problem. The estimate is repre- sented as a probability distribution, allowing the prediction of end of life and remaining useful life within a probabilistic framework that supports uncertainty management. We also develop a novel variance control mechanism that maintains an uncertainty bound around the hidden parameters to limit the amount of estimation uncertainty and, consequently, reduce prediction uncertainty. We construct a detailed physics-based model of a centrifugal pump, to which we apply our model- based prognostics algorithms. We illustrate the operation of the prognostic solution with a number of simulation-based experiments and demonstrate the performance of the chosen approach when multiple damage mechanisms are active.",
-            "title": "Multiple Damage Progression Paths in Model-based Prognostics",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_IEEEAerospace_pump_paths.pdf",
-                    "description": "2011_IEEEAerospace_pump_paths.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2011_IEEEAerospace_pump_paths.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_IEEEAerospace_pump_paths.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2011_IEEEAerospace_pump_paths.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_782",
+            "issued": "2013-06-19",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/782/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Multiple Damage Progression Paths in Model-based Prognostics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-04-27",
-            "temporal": "2021-04-27T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "international",
-                "space",
-                "station",
-                "coords",
-                "topo",
-                "trajectory",
-                "coordinates",
-                "iss",
-                "ephemeris",
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
-            "identifier": "nasa-iss-data_2021-04-27",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-04-27",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1647659,693 +1647635,731 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-04-27",
+            "issued": "2021-04-27",
+            "keyword": [
+                "international",
+                "space",
+                "station",
+                "coords",
+                "topo",
+                "trajectory",
+                "coordinates",
+                "iss",
+                "ephemeris",
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
+            "temporal": "2021-04-27T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-04-27"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Y9ZBXLR9NGCM",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSRIce03 Photomosaics, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/Y9ZBXLR9NGCM.",
-            "issued": "2003-03-07",
-            "temporal": "2003-03-07T00:00:00Z/2003-03-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-03-11",
-            "keyword": [
-                "oceans",
-                "sea ice",
-                "cryosphere",
-                "earth science",
-                "snow/ice",
-                "terrestrial hydrosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Sturm",
                 "hasEmail": "mailto:msturm@crrel.usace.army.mil"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386205142-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set contains photographic mosaics of sea ice in the Barrow, Alaska USA area as part of the joint in situ and aircraft AMSRIce03.",
-            "title": "AMSRIce03 Photomosaics, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY9ZBXLR9NGCM",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY9ZBXLR9NGCM",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/photo_mosaics/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/photo_mosaics/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/photo_mosaics/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/photo_mosaics/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/photo_mosaics/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/photo_mosaics/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/photo_mosaics/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/photo_mosaics/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Y9ZBXLR9NGCM",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/Y9ZBXLR9NGCM",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Y9ZBXLR9NGCM",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/Y9ZBXLR9NGCM",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205142-NSIDCV0",
+            "issued": "2003-03-07",
+            "keyword": [
+                "oceans",
+                "sea ice",
+                "cryosphere",
+                "earth science",
+                "snow/ice",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Y9ZBXLR9NGCM",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-03-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-156.4 71.18 -156.15 71.28",
+            "temporal": "2003-03-07T00:00:00Z/2003-03-11T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSRIce03 Photomosaics, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/SNOWTUBE/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lundquist, Jessica D., William Ryan Currier and Bill  Baccus.2018. GPM Ground Validation Snow Depth Monitoring System OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/SNOWTUBE/DATA101",
-            "issued": "2018-05-01",
-            "temporal": "2014-09-05T00:00:00Z/2016-07-26T08:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-25",
-            "keyword": [
-                "cryospheric indicators",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "climate indicators",
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
-            "identifier": "C1979732987-GHRC_DAAC",
             "description": "The GPM Ground Validation Snow Depth Monitoring System OLYMPEX dataset consists of snow depth, temperature, and relative humidity measurements which were collected using snow depth poles, time lapse cameras, temperature/relative humidity sensors, and manual snow surveys.  This dataset was collected during the GPM Ground Validation Olympic Mountain Experiment (OLYMPEX) held on the Olympic Peninsula in the Pacific Northwest of the United States. The analyzed data files are available in netCDF-3 data format.  The dataset includes the individual camera photos of snow poles taken hourly during the field campaign, provided as JPG images.  There are up to 3 cameras/poles per study site location.  In addition, a Microsoft Excel data file contains results of a manual snow survey taken on the specific days of the Airborne Snow Observatory OLYMPEX overflights.  In total, measurements contained in this dataset extend from September 5, 2014 through August 20, 2016, but the primary field campaign data were collected during the fall 2015 to spring 2016 time period.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "GPM Ground Validation Snow Depth Monitoring System OLYMPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/snow_depth_monitoring/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FSNOWTUBE%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FSNOWTUBE%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsnowolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsnowolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://digital.lib.washington.edu/researchworks/handle/1773/38604",
-                    "description": "An independent evaluation of frozen precipitation from the WRF model and PRISM in the Olympic Mountains for WY 2015 and 2016",
                     "@type": "dcat:Distribution",
+                    "description": "An independent evaluation of frozen precipitation from the WRF model and PRISM in the Olympic Mountains for WY 2015 and 2016",
+                    "downloadURL": "https://digital.lib.washington.edu/researchworks/handle/1773/38604",
+                    "mediaType": "text/html",
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
-                    "description": "University of Washington OLYMPEX project web site",
                     "@type": "dcat:Distribution",
+                    "description": "University of Washington OLYMPEX project web site",
+                    "downloadURL": "http://olympex.atmos.washington.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/snow_depth_monitoring/doc/gpmsnowolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/snow_depth_monitoring/doc/gpmsnowolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JHM-D-17-0026.1",
-                    "description": "Independent Evaluation of Frozen Precipitation from WRF and PRISM in the Olympic Mountains",
                     "@type": "dcat:Distribution",
+                    "description": "Independent Evaluation of Frozen Precipitation from WRF and PRISM in the Olympic Mountains",
+                    "downloadURL": "https://doi.org/10.1175/JHM-D-17-0026.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2008WR006979",
-                    "description": "Evergreen trees as inexpensive radiation shields for temperature sensors",
                     "@type": "dcat:Distribution",
+                    "description": "Evergreen trees as inexpensive radiation shields for temperature sensors",
+                    "downloadURL": "https://doi.org/10.1029/2008WR006979",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/snow_depth_monitoring/browse/",
-                    "description": "Browse images illustrate the nature and coverage of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Browse images illustrate the nature and coverage of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/snow_depth_monitoring/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/snow_depth_monitoring/browse/",
+            "identifier": "C1979732987-GHRC_DAAC",
+            "issued": "2018-05-01",
+            "keyword": [
+                "cryospheric indicators",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "climate indicators",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/SNOWTUBE/DATA101",
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
             "spatial": "-123.707 47.5008 -123.033 47.8224",
+            "temporal": "2014-09-05T00:00:00Z/2016-07-26T08:00:00Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Snow Depth Monitoring System OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0418-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-09T15:52:16.000 to 2014-11-09T21:50:49.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0418-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0418-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0418-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-09T15:52:16.000 to 2014-11-09T21:50:49.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0418 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0418 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3286-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-13T12:11:47.000 to 2012-05-13T15:39:44.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3286-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3286-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3286-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-13T12:11:47.000 to 2012-05-13T15:39:44.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3286 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3286 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0546-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-22T23:21:30.000 to 2015-01-23T09:34:09.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0546-v1.0_xsa3-geqb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0546-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0546-v1.0_xsa3-geqb",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-22T23:21:30.000 to 2015-01-23T09:34:09.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0546 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0546 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-MAG-3-RDR-EARTH1-HIGHRES-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Galileo Orbiter Magnetometer (MAG) calibrated high-resolution data from the Earth-1 flyby in spacecraft, GSE, and GSM coordinates. These data cover the interval 1990-11-05 to 1990-12-31.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-mag-3-rdr-earth1-highres-v1.0_xsbm-h3uz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-MAG-3-RDR-EARTH1-HIGHRES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-mag-3-rdr-earth1-highres-v1.0_xsbm-h3uz",
-            "description": "Galileo Orbiter Magnetometer (MAG) calibrated high-resolution data from the Earth-1 flyby in spacecraft, GSE, and GSM coordinates. These data cover the interval 1990-11-05 to 1990-12-31.",
-            "title": "GALILEO ORBITER EARTH MAG RDR EARTH1 HIGHRES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO ORBITER EARTH MAG RDR EARTH1 HIGHRES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC3-MTP021-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT 3 MTP021 phase, which occurred from 2015-09-23 to 2015-10-21 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc3-mtp021-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC3-MTP021-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc3-mtp021-v2.0",
-            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT 3 MTP021 phase, which occurred from 2015-09-23 to 2015-10-21 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 3 MTP021 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 3 MTP021 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-ESC3-V1.0",
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
+            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the comet escort 3 phase (ESC3). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jul 2015 and 21 Oct 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-esc3-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-ESC3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-esc3-v1.0",
-            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the comet escort 3 phase (ESC3). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jul 2015 and 21 Oct 2015.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 5 ESC3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 5 ESC3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA310",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRX3ST8. Version 006. AIRS/Aqua L3 8-day Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA310. https://disc.gsfc.nasa.gov/datacollection/AIRX3ST8_006.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2016-10-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-10-01",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.5194/acp-14-399-2014"
-            ],
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "atmospheric water vapor",
-                "surface radiative properties",
-                "air quality",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "clouds",
-                "surface thermal properties",
-                "land surface",
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere",
-                "altitude"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1238517323-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The AIRS Level 3 8-Day Gridded Retrieval Product contains standard retrieval means, standard deviations and input counts. Each file covers an 8-day period, or one-half of the Aqua orbit repeat cycle. The mean values are simply the arithmetic means of the daily products, weighted by the number of input counts for each day in that grid box. The geophysical parameters have been averaged and binned into 1 x 1 deg grid cells, from -180.0 to +180.0 deg longitude and from -90.0 to +90.0 deg latitude. For each grid map of 4-byte floating-point mean values there is a corresponding 4-byte floating-point map of standard deviation and a 2-byte integer grid map of counts. The counts map provides the user with the number of points per bin that were included in the mean and can be used to generate custom multi-day maps from the daily gridded products. The thermodynamic parameters are: Skin Temperature (land and sea surface), Air Temperature at the surface, Profiles of Air Temperature and Water Vapor, Tropopause Characteristics, Column Precipitable Water, Cloud Amount/Frequency, Cloud Height, Cloud Top Pressure, Cloud Top Temperature, Reflectance, Emissivity, Surface Pressure, Cloud Vertical Distribution. The trace gases parameters are: Total Amounts and Vertical Profiles of Carbon Monoxide, Methane, and Ozone. The actual names of the variables in the data files should be inferred from the Processing File Description document.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRX3ST8",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 multiday standard physical retrieval product (Without HSB)\".",
-            "title": "AIRS/Aqua L3 8-day Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3ST8) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3ST8_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA310",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA310",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3ST8_006.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 multiday standard physical retrieval product (Without HSB)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 multiday standard physical retrieval product (Without HSB)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3ST8_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3ST8_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3ST8_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3ST8.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3ST8.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3ST8.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3ST8.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3ST8+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3ST8+006",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/V6_Released_Processing_Files_Description.pdf",
-                    "description": "AIRS Version 6 Processing Files Description Document.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Version 6 Processing Files Description Document.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/V6_Released_Processing_Files_Description.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 multiday standard physical retrieval product (Without HSB)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3ST8_006.png",
+            "identifier": "C1238517323-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "atmospheric water vapor",
+                "surface radiative properties",
+                "air quality",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "clouds",
+                "surface thermal properties",
+                "land surface",
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA310",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-10-01",
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
+            "series-name": "AIRX3ST8",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2016-10-01T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 8-day Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3ST8) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IGQNPB6183ZX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L3 Radar Global Daily 3 km EASE-Grid Soil Moisture V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/IGQNPB6183ZX.",
-            "issued": "2015-04-13",
-            "temporal": "2015-04-13T00:00:00Z/2015-07-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-07",
-            "keyword": [
-                "land surface",
-                "radar",
-                "soils",
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
-            "identifier": "C2872766452-NSIDC_CPRD",
             "description": "This Level-3 (L3) soil moisture product provides a composite of daily estimates of global land surface conditions retrieved by the Soil Moisture Active Passive (SMAP) radar as well as a variety of ancillary data sources. SMAP L-band soil moisture data are resampled to an Earth-fixed, global, cylindrical 3 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0).",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP L3 Radar Global Daily 3 km EASE-Grid Soil Moisture V003",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-191,-75,144,79&l=SMAP_L3_Active_Soil_Moisture,SMAP_L3_Active_Sigma0_XPOL_QA(disabled=3),SMAP_L3_Active_Sigma0_VV_QA(disabled=3),SMAP_L3_Active_Sigma0_HH_QA(disabled=3),SMAP_L3_Active_Sigma0_XPOL_RFI(disabled=3),SMAP_L3_Active_Sigma0_VV_RFI(disabled=3),SMAP_L3_Active_Sigma0_HH_RFI(disabled=3),SMAP_L3_Active_Sigma0_XPOL,SMAP_L3_Active_Sigma0_VV,SMAP_L3_Active_Sigma0_HH,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-13",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIGQNPB6183ZX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIGQNPB6183ZX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL3SMA+V003",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL3SMA+V003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2872766452-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2872766452-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-191%2C-75%2C144%2C79&l=SMAP_L3_Active_Soil_Moisture%2CSMAP_L3_Active_Sigma0_XPOL_QA%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_VV_QA%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_HH_QA%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_XPOL_RFI%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_VV_RFI%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_HH_RFI%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_XPOL%2CSMAP_L3_Active_Sigma0_VV%2CSMAP_L3_Active_Sigma0_HH%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-13",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-191%2C-75%2C144%2C79&l=SMAP_L3_Active_Soil_Moisture%2CSMAP_L3_Active_Sigma0_XPOL_QA%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_VV_QA%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_HH_QA%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_XPOL_RFI%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_VV_RFI%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_HH_RFI%28disabled%3D3%29%2CSMAP_L3_Active_Sigma0_XPOL%2CSMAP_L3_Active_Sigma0_VV%2CSMAP_L3_Active_Sigma0_HH%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-13",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IGQNPB6183ZX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/IGQNPB6183ZX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IGQNPB6183ZX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/IGQNPB6183ZX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-191,-75,144,79&l=SMAP_L3_Active_Soil_Moisture,SMAP_L3_Active_Sigma0_XPOL_QA(disabled=3),SMAP_L3_Active_Sigma0_VV_QA(disabled=3),SMAP_L3_Active_Sigma0_HH_QA(disabled=3),SMAP_L3_Active_Sigma0_XPOL_RFI(disabled=3),SMAP_L3_Active_Sigma0_VV_RFI(disabled=3),SMAP_L3_Active_Sigma0_HH_RFI(disabled=3),SMAP_L3_Active_Sigma0_XPOL,SMAP_L3_Active_Sigma0_VV,SMAP_L3_Active_Sigma0_HH,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-13",
+            "identifier": "C2872766452-NSIDC_CPRD",
+            "issued": "2015-04-13",
+            "keyword": [
+                "land surface",
+                "radar",
+                "soils",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/IGQNPB6183ZX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-07-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -85.044 180.0 85.044",
+            "temporal": "2015-04-13T00:00:00Z/2015-07-07T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP L3 Radar Global Daily 3 km EASE-Grid Soil Moisture V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xshw-2nyf",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The Rodent Research-3 (RR-3) mission was sponsored by the pharmaceutical company Eli Lilly and Co. and the Center for the Advancement of Science in Space to study the effectiveness of a potential countermeasure for the loss of muscle and bone mass that occurs during spaceflight. Twenty BALB/c 18-weeks old female mice (ten controls and ten treated) were flown to the ISS and housed in the Rodent Habitat for 39-42 days. Twenty mice of similar age sex and strain were used for ground controls housed in identical hardware and matching ISS environmental conditions. Basal controls were housed in standard vivarium cages. Spaceflight ground controls and basal groups had blood collected then were euthanized had one hind limb removed and finally whole carcasses were stored at -80 C until dissection. All mice in this data set received only the control/sham injection. Spatially resolved transcriptional profiles were generated from hearts from three flight and three ground control animals as follows. Hearts were cryosectioned longitudinally onto an array of capture probes that bind RNA fixed stained and visualized. Heart sections were then permeabilized to release RNA onto the capture probes and cDNA synthesized on the chip so that its spatial arrangement is encoded within a set of molecular barcodes. cDNA was then released and sequenced. Four to five levels of each heart was analyzed in this manner to allow a 3D reconstruction of the transcriptome.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-270",
+                    "mediaType": "text/html",
+                    "title": "Spatially resolved transcriptional analysis of hearts from mice flown on the RR-3 mission"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-270_xshw-2nyf",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample collection",
                 "nucleic acid extraction",
@@ -1648356,335 +1648370,297 @@
                 "library construction",
                 "cryosection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xshw-2nyf",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-270_xshw-2nyf",
-            "description": "The Rodent Research-3 (RR-3) mission was sponsored by the pharmaceutical company Eli Lilly and Co. and the Center for the Advancement of Science in Space to study the effectiveness of a potential countermeasure for the loss of muscle and bone mass that occurs during spaceflight. Twenty BALB/c 18-weeks old female mice (ten controls and ten treated) were flown to the ISS and housed in the Rodent Habitat for 39-42 days. Twenty mice of similar age sex and strain were used for ground controls housed in identical hardware and matching ISS environmental conditions. Basal controls were housed in standard vivarium cages. Spaceflight ground controls and basal groups had blood collected then were euthanized had one hind limb removed and finally whole carcasses were stored at -80 C until dissection. All mice in this data set received only the control/sham injection. Spatially resolved transcriptional profiles were generated from hearts from three flight and three ground control animals as follows. Hearts were cryosectioned longitudinally onto an array of capture probes that bind RNA fixed stained and visualized. Heart sections were then permeabilized to release RNA onto the capture probes and cDNA synthesized on the chip so that its spatial arrangement is encoded within a set of molecular barcodes. cDNA was then released and sequenced. Four to five levels of each heart was analyzed in this manner to allow a 3D reconstruction of the transcriptome.",
-            "title": "Spatially resolved transcriptional analysis of hearts from mice flown on the RR-3 mission",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-270",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Spatially resolved transcriptional analysis of hearts from mice flown on the RR-3 mission"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Spatially resolved transcriptional analysis of hearts from mice flown on the RR-3 mission"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1694",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "French, N.H.F., J.A. Graham, L.L. Bourgeau-Chavez, S. Grelick, and E. Whitman. 2020. ABoVE: Burn Severity of Soil Organic Matter, Northwest Territories, Canada, 2014-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1694",
-            "issued": "2020-02-17",
-            "temporal": "2014-05-01T00:00:00Z/2015-10-01T23:59:59Z",
             "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "vegetation",
-                "earth science",
-                "biosphere",
-                "ecological dynamics",
-                "human dimensions",
-                "land surface",
-                "natural hazards",
-                "soils"
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "French, N.H.F., J.A. Graham, L.L. Bourgeau-Chavez, S. Grelick, and E. Whitman. 2020. ABoVE: Burn Severity of Soil Organic Matter, Northwest Territories, Canada, 2014-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1694",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2143402644-ORNL_CLOUD",
             "description": "This dataset provides maps at 30-m resolution of landscape surface burn severity (surface litter and soil organic layers) from the 2014-2015 fires in the Northwest Territories and Northern Alberta, Canada. The maps were derived from Landsat 8 Operational Land Imager/Thermal Infrared Sensor (OLI/TIRS) imagery and two separate multiple linear regression models trained with field data; one for the Plains and a second for the Shield ecoregion. Field observations were used to estimate area burned in each of five severity classes (unburned, singed, light, moderate, severely burned) in six stratified randomly selected plots of 10 x 10-m in size across a 1-ha site. Using this five class scale a burn severity index (BSI) for each 1-ha site was calculated using multiple weighted and averaged field parameters. Pre- and post-fire phenologically paired Landsat 8 images were used to model the five discrete severity classes using midpoints as breaks.",
-            "graphic-preview-description": "Study area included sites burned in 2014 and 2015 in the southeastern portion of the Northwest Territories and northern Alberta of Canada. The study area includes all 2014 and 2015 fires within a radius of approximately 300 km from Great Slave Lake.",
-            "title": "ABoVE: Burn Severity of Soil Organic Matter, Northwest Territories, Canada, 2014-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/NWT_Burn_Severity_Maps_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1694",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1694",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/NWT_Burn_Severity_Maps/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/NWT_Burn_Severity_Maps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/NWT_Burn_Severity_Maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/NWT_Burn_Severity_Maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1694",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1694",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/NWT_Burn_Severity_Maps/comp/NWT_Burn_Severity_Maps.pdf",
-                    "description": "ABoVE: Burn Severity of Soil Organic Matter, Northwest Territories, Canada, 2014-2015: NWT_Burn_Severity_Maps.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Burn Severity of Soil Organic Matter, Northwest Territories, Canada, 2014-2015: NWT_Burn_Severity_Maps.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/NWT_Burn_Severity_Maps/comp/NWT_Burn_Severity_Maps.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/NWT_Burn_Severity_Maps/comp/severity_training.csv",
-                    "description": "ABoVE: Burn Severity of Soil Organic Matter, Northwest Territories, Canada, 2014-2015: severity_training.csv",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Burn Severity of Soil Organic Matter, Northwest Territories, Canada, 2014-2015: severity_training.csv",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/NWT_Burn_Severity_Maps/comp/severity_training.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/NWT_Burn_Severity_Maps_Fig1.png",
-                    "description": "Study area included sites burned in 2014 and 2015 in the southeastern portion of the Northwest Territories and northern Alberta of Canada. The study area includes all 2014 and 2015 fires within a radius of approximately 300 km from Great Slave Lake.",
                     "@type": "dcat:Distribution",
+                    "description": "Study area included sites burned in 2014 and 2015 in the southeastern portion of the Northwest Territories and northern Alberta of Canada. The study area includes all 2014 and 2015 fires within a radius of approximately 300 km from Great Slave Lake.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/NWT_Burn_Severity_Maps_Fig1.png",
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
+            "graphic-preview-description": "Study area included sites burned in 2014 and 2015 in the southeastern portion of the Northwest Territories and northern Alberta of Canada. The study area includes all 2014 and 2015 fires within a radius of approximately 300 km from Great Slave Lake.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/NWT_Burn_Severity_Maps_Fig1.png",
+            "identifier": "C2143402644-ORNL_CLOUD",
+            "issued": "2020-02-17",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "biosphere",
+                "ecological dynamics",
+                "human dimensions",
+                "land surface",
+                "natural hazards",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1694",
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
             "spatial": "-124.03 58.29 -108.83 65.55",
+            "temporal": "2014-05-01T00:00:00Z/2015-10-01T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Burn Severity of Soil Organic Matter, Northwest Territories, Canada, 2014-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI1B1_L1.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 1B1 Radiance Data;See ProductionDateTime for Published Date.",
-            "issued": "2003-03-24",
-            "temporal": "1999-12-18T00:00:00Z/2023-11-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-13",
-            "keyword": [
-                "spectral/engineering",
-                "visible wavelengths",
-                "earth science"
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
-            "identifier": "C179031454-LARC",
             "description": "This is the Level 1B1 Product containing the DNs radiometrically-scaled to radiances with no geometric resampling",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 1B1 Radiance Data V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI1B1_L1.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI1B1_L1.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/misr/quality_summaries/L1_Products.pdf",
-                    "description": "The product quality assessment may be downloaded directly from this link",
                     "@type": "dcat:Distribution",
+                    "description": "The product quality assessment may be downloaded directly from this link",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/misr/quality_summaries/L1_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C179031454-LARC",
+            "issued": "2003-03-24",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI1B1_L1.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1999-12-18T00:00:00Z/2023-11-06T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 1B1 Radiance Data V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSOH-N-NDR-CROMMELIN-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rsoh-n-ndr-crommelin-v1.0_xsq5-ztey",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSOH-N-NDR-CROMMELIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rsoh-n-ndr-crommelin-v1.0_xsq5-ztey",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET RSOH NO-DATA DATA RECORD CROMMELIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET RSOH NO-DATA DATA RECORD CROMMELIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/AMSR2/GCOMW1/GPROFCLIM/3A-MONTH/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFGCOMW1AMSR2_CLIM. Version 07. GPM AMSR-2 on GCOM-W1 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/AMSR2/GCOMW1/GPROFCLIM/3A-MONTH/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGCOMW1AMSR2_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2012-07-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric water vapor",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264135524-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07. \n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3GPROFGCOMW1AMSR2_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM AMSR-2 on GCOM-W1 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2_CLIM) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from GPM AMSR-2 on GCOM-W1 GPROF (25 km x 25 km) (GPM_3GPROFGCOMW1AMSR2_CLIM)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSR2%2FGCOMW1%2FGPROFCLIM%2F3A-MONTH%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSR2%2FGCOMW1%2FGPROFCLIM%2F3A-MONTH%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_CLIM_07.png",
-                    "description": "Surface Precipitation from GPM AMSR-2 on GCOM-W1 GPROF (25 km x 25 km) (GPM_3GPROFGCOMW1AMSR2_CLIM)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from GPM AMSR-2 on GCOM-W1 GPROF (25 km x 25 km) (GPM_3GPROFGCOMW1AMSR2_CLIM)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGCOMW1AMSR2_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGCOMW1AMSR2_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFGCOMW1AMSR2_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFGCOMW1AMSR2_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFGCOMW1AMSR2_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFGCOMW1AMSR2_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFGCOMW1AMSR2_CLIM_07.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFGCOMW1AMSR2_CLIM_07.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFGCOMW1AMSR2_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFGCOMW1AMSR2_CLIM_07",
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
@@ -1648694,160 +1648670,162 @@
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
+            "graphic-preview-description": "Surface Precipitation from GPM AMSR-2 on GCOM-W1 GPROF (25 km x 25 km) (GPM_3GPROFGCOMW1AMSR2_CLIM)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_CLIM_07.png",
+            "identifier": "C2264135524-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric water vapor",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/AMSR2/GCOMW1/GPROFCLIM/3A-MONTH/07",
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
+            "series-name": "GPM_3GPROFGCOMW1AMSR2_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-07-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM AMSR-2 on GCOM-W1 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-E%2FJ%2FSS-WAV-3-CDR-BSTFULL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Juno Waves calibrated burst waveform full resolution data set includes all high rate science electric field waveforms from 50Hz up to 45.25 MHz and magnetic field waveforms from 50Hz to 20kHz with sample rates that depend on the receiver used to obtain the waveforms.  This is the complete waveform data set containing all high rate binning mode data and record mode data received from Waves from launch until the end of mission including initial checkout, the Earth flyby, the Jupiter orbits and cruise. Data are acquired from the Waves Low Frequency Receiver (LFR) and High Frequency Receiver (HFR) and are typically losslessly compressed on  board.  These data are presented in binary SERIES objects.  This data  set comprises highest temporal resolution data obtained by Waves (or all other Juno instruments, for that matter).  Pre-rendered spectrograms generated from these data are included as well to provide the user with a quick view of the content of the data.  This data set should be among the last used of any in the Waves archive as it provides highly detailed information on very short isolated intervals in time.  The Waves full resolution survey data provide context for these data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-e-j-ss-wav-3-cdr-bstfull-v1.0_xsva-fn2n",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-E%2FJ%2FSS-WAV-3-CDR-BSTFULL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-e-j-ss-wav-3-cdr-bstfull-v1.0_xsva-fn2n",
-            "description": "The Juno Waves calibrated burst waveform full resolution data set includes all high rate science electric field waveforms from 50Hz up to 45.25 MHz and magnetic field waveforms from 50Hz to 20kHz with sample rates that depend on the receiver used to obtain the waveforms.  This is the complete waveform data set containing all high rate binning mode data and record mode data received from Waves from launch until the end of mission including initial checkout, the Earth flyby, the Jupiter orbits and cruise. Data are acquired from the Waves Low Frequency Receiver (LFR) and High Frequency Receiver (HFR) and are typically losslessly compressed on  board.  These data are presented in binary SERIES objects.  This data  set comprises highest temporal resolution data obtained by Waves (or all other Juno instruments, for that matter).  Pre-rendered spectrograms generated from these data are included as well to provide the user with a quick view of the content of the data.  This data set should be among the last used of any in the Waves archive as it provides highly detailed information on very short isolated intervals in time.  The Waves full resolution survey data provide context for these data.",
-            "title": "JUNO E/J/S/SS WAVES CALIBRATED BURST FULL RESOLUTION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "JUNO E/J/S/SS WAVES CALIBRATED BURST FULL RESOLUTION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S%2FJ%2FE%2FV-SPICE-6-V1.0",
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
+            "description": "This data set includes the complete set of Cassini SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-j-e-v-spice-6-v1.0_xswh-jp87",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S%2FJ%2FE%2FV-SPICE-6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-j-e-v-spice-6-v1.0_xswh-jp87",
-            "description": "This data set includes the complete set of Cassini SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
-            "title": "CASSINI SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/M9MTZJNBG0GF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2020-08-10. OCO2_L2_Diagnostic. Version 10r. OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information, Retrospective Processing V10r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/M9MTZJNBG0GF. https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Diagnostic_10r.html. Digital Science Data.",
-            "issued": "2020-08-01",
-            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-08-10",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C1685783941-GES_DISC",
-            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nIn early 2021, the OCO Team identified an issue with OCO-2 level 2 products processed since January 28, 2020. The Ancillary Geometric Product (AGAP) file, a static file used in OCO-2 Geolocation processing, was inadvertently replaced with an obsolete version. This AGAP file included a ~300 m pointing error. As a result, all OCO-2 Level 2, version 10r, data files for the period January 28 - December 31, 2020, were corrected and replaced. The replacement process was completed by the end of June, 2021. The significance of this error has been described in Kiel et al. (2019; doi:10.5194/amt-12-2241-2019).\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection encompass various data fields used for diagnostic and pre-processing, including aerosol optical depth, albedo, absorption coefficients, fluorescence, XCO2 uncertainties, averaging kernel, surface type, etc.\n\nThis is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_Diagnostic",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information, Retrospective Processing V10r (OCO2_L2_Diagnostic) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Dia_10r__02242021.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nIn early 2021, the OCO Team identified an issue with OCO-2 level 2 products processed since January 28, 2020. The Ancillary Geometric Product (AGAP) file, a static file used in OCO-2 Geolocation processing, was inadvertently replaced with an obsolete version. This AGAP file included a ~300 m pointing error. As a result, all OCO-2 Level 2, version 10r, data files for the period January 28 - December 31, 2020, were corrected and replaced. The replacement process was completed by the end of June, 2021. The significance of this error has been described in Kiel et al. (2019; doi:10.5194/amt-12-2241-2019).\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection encompass various data fields used for diagnostic and pre-processing, including aerosol optical depth, albedo, absorption coefficients, fluorescence, XCO2 uncertainties, averaging kernel, surface type, etc.\n\nThis is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FM9MTZJNBG0GF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FM9MTZJNBG0GF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1648857,493 +1648835,527 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Diagnostic_10r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Diagnostic_10r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Diagnostic.10r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Diagnostic.10r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_Diagnostic",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_Diagnostic",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Diagnostic.10r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Diagnostic.10r/contents.html",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Diagnostic.V7.pdf",
-                    "description": "Software Interface Specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software Interface Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Diagnostic.V7.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Dia_10r__02242021.png",
+            "identifier": "C1685783941-GES_DISC",
+            "issued": "2020-08-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/M9MTZJNBG0GF",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-08-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2_L2_Diagnostic",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information, Retrospective Processing V10r (OCO2_L2_Diagnostic) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/339/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CAROL WIESEMAN",
+                "hasEmail": "mailto:carol.d.wieseman@nasa.gov"
+            },
+            "description": "not available",
+            "identifier": "DASHLINK_339",
             "issued": "2011-04-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "dashlink",
                 "nasa",
                 "ames"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CAROL WIESEMAN",
-                "hasEmail": "mailto:carol.d.wieseman@nasa.gov"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/339/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_339",
-            "description": "not available",
-            "title": "Benchmark Supercritical Wing",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Benchmark Supercritical Wing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1104-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-16T10:18:20.000 to 2015-10-16T17:25:38.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1104-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1104-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1104-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-16T10:18:20.000 to 2015-10-16T17:25:38.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1104 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1104 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0283-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-09T20:57:30.000 to 2014-09-10T00:42:35.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0283-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0283-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0283-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-09T20:57:30.000 to 2014-09-10T00:42:35.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0283 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0283 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-EXT2-67PCHURYUMOV-M29-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-ext2-67pchuryumov-m29-v3.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-EXT2-67PCHURYUMOV-M29-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-ext2-67pchuryumov-m29-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 3 EXT2-MTP029 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 3 EXT2-MTP029 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2COLN_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "issued": "2014-08-20",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-10-28",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry/carbon and hydrocarbon compounds",
-                "air quality",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "identifier": "C1000000340-LARC",
             "description": "Atmospheric vertical profile estimates and associated errors including the mapping matrix to relate the reduced-size retrieval vectors, covariances, and averaging kernels back to the TES forward model pressure grid.",
-            "title": "TES/Aura L2 Carbon Monoxide Lite Nadir V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2COLN_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2COLN_L2.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C1000000340-LARC",
+            "issued": "2014-08-20",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry/carbon and hydrocarbon compounds",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2COLN_L2.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-10-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L2 Carbon Monoxide Lite Nadir V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1250",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Beldini, T.P., and K. McNabb. 2014. LBA-ECO ND-08 Soil Respiration, Soil Fractions, Carbon and Nitrogen, Para, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1250",
-            "issued": "2023-10-03",
-            "temporal": "2001-07-01T00:00:00Z/2003-03-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
-            "keyword": [
-                "earth science",
-                "land surface",
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
-            "identifier": "C2781620134-ORNL_CLOUD",
             "description": "This data set provides (1) carbon (C) and nitrogen (N) concentration measurements of two soil aggregate fractions (250-2000 micon, small macro-aggregates (SMAG)), and (53-250 micron (micro-aggregates (mico)) and (2) in situ soil respiration measurements (January-March 2003) on sand and clay soils from a Eucalyptus plantation and an adjacent primary forest. The soils for fractionation were sampled in July 2001 from 0-20 cm and 30-50 cm depths. The research site was on the property of Jari Celulose, Monte Dourado, Para, Brazil. There are two files with this data set in comma-delimited (.csv) format.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-08 Soil Respiration, Soil Fractions, Carbon and Nitrogen, Para, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1250",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1250",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/grab_bag/ND08_Soil_Respiration/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/grab_bag/ND08_Soil_Respiration/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND08_Soil_Respiration.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND08_Soil_Respiration.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1250",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1250",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/grab_bag/ND08_Soil_Respiration/comp/ND08_Soil_Respiration.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/grab_bag/ND08_Soil_Respiration/comp/ND08_Soil_Respiration.pdf",
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
+            "identifier": "C2781620134-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1250",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-0.86 -52.55",
+            "temporal": "2001-07-01T00:00:00Z/2003-03-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-08 Soil Respiration, Soil Fractions, Carbon and Nitrogen, Para, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1786",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Jiang, C., and K. Guan. 2020. MODIS-based GPP, PAR, fC4, and SANIRv estimates from SLOPE for CONUS, 2000-2019. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1786",
-            "issued": "2021-11-13",
-            "temporal": "2000-01-01T00:00:00Z/2020-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
-                "biosphere",
-                "earth science",
-                "infrared wavelengths",
-                "vegetation",
-                "surface radiative properties",
-                "spectral/engineering",
-                "soils",
-                "ngda",
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
-            "identifier": "C2266194621-ORNL_CLOUD",
             "description": "This dataset contains estimated gross primary productivity (GPP), photosynthetically active radiation (PAR), soil adjusted near infrared reflectance of vegetation (SANIRv), the fraction of C4 crops in vegetation  (fC4), and their uncertainties for the conterminous United States (CONUS) from 2000 to 2019. The daily estimates are SatelLite Only Photosynthesis Estimation (SLOPE) products at 250-m resolution. There are three distinct features of the GPP estimation algorithm: (1) SLOPE couples machine learning models with MODIS atmosphere and land products to accurately estimate PAR, (2) SLOPE couples gap-filling and filtering algorithms with surface reflectance acquired by both Terra and Aqua MODIS satellites to derive a soil-adjusted NIRv (SANIRv) dataset, and (3) SLOPE couples a temporal pattern recognition approach with a long-term Crop Data Layer (CDL) product to predict dynamic C4 crop fraction. PAR, SANIRv and C4 fraction are used to drive a parsimonious model with only two parameters to estimate GPP, along with a quantitative uncertainty, on a per-pixel and daily basis. The slope GPP product has an R2 = 0.84 and a root-mean-square error (RMSE) of 1.65 gC m-2 d-1.",
-            "graphic-preview-description": "Spatial distribution of (a) GPP (gC m2/d) and (b) GPP uncertainty (gC m2/d) across the CONUS at 250-m resolution for 10 July 2020 (image source: Jiang et al. 2021).",
-            "title": "MODIS-based GPP, PAR, fC4, and SANIRv estimates from SLOPE for CONUS, 2000-2019",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/SLOPE_GPP_CONUS_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1786",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1786",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/SLOPE_GPP_CONUS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/SLOPE_GPP_CONUS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SLOPE_GPP_CONUS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SLOPE_GPP_CONUS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1786",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1786",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SLOPE_GPP_CONUS/comp/read_check.zip",
-                    "description": "MODIS-based GPP, PAR, fC4, and SANIRv estimates from SLOPE for CONUS, 2000-2019: read_check.zip",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-based GPP, PAR, fC4, and SANIRv estimates from SLOPE for CONUS, 2000-2019: read_check.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SLOPE_GPP_CONUS/comp/read_check.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SLOPE_GPP_CONUS/comp/SLOPE_GPP_CONUS.pdf",
-                    "description": "MODIS-based GPP, PAR, fC4, and SANIRv estimates from SLOPE for CONUS, 2000-2019: SLOPE_GPP_CONUS.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-based GPP, PAR, fC4, and SANIRv estimates from SLOPE for CONUS, 2000-2019: SLOPE_GPP_CONUS.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SLOPE_GPP_CONUS/comp/SLOPE_GPP_CONUS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SLOPE_GPP_CONUS_Fig1.png",
-                    "description": "Spatial distribution of (a) GPP (gC m2/d) and (b) GPP uncertainty (gC m2/d) across the CONUS at 250-m resolution for 10 July 2020 (image source: Jiang et al. 2021).",
                     "@type": "dcat:Distribution",
+                    "description": "Spatial distribution of (a) GPP (gC m2/d) and (b) GPP uncertainty (gC m2/d) across the CONUS at 250-m resolution for 10 July 2020 (image source: Jiang et al. 2021).",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SLOPE_GPP_CONUS_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Spatial distribution of (a) GPP (gC m2/d) and (b) GPP uncertainty (gC m2/d) across the CONUS at 250-m resolution for 10 July 2020 (image source: Jiang et al. 2021).",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/SLOPE_GPP_CONUS_Fig1.png",
+            "identifier": "C2266194621-ORNL_CLOUD",
+            "issued": "2021-11-13",
+            "keyword": [
+                "land surface",
+                "biosphere",
+                "earth science",
+                "infrared wavelengths",
+                "vegetation",
+                "surface radiative properties",
+                "spectral/engineering",
+                "soils",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1786",
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
             "spatial": "-155.57 19.99 -52.22 50.01",
+            "temporal": "2000-01-01T00:00:00Z/2020-01-01T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS-based GPP, PAR, fC4, and SANIRv estimates from SLOPE for CONUS, 2000-2019"
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
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/Lutetia_craters_linearfeatures.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-172",
             "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "gaspra",
                 "itokawa",
@@ -1649360,42 +1649372,44 @@
                 "eros",
                 "ida"
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
-            "identifier": "OCIO-Fitara-172",
-            "description": "These images display asteriods documented and approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Asteroids: Lutetia Features",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/Lutetia_craters_linearfeatures.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Asteroids: Lutetia Features"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xt8w-vdtd",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Here we present a whole-genome survey of the murine transcriptomic response to physiologically-relevant radiation doses 2 and 8 Gy. There are 18 distinct biological samples here. Mice were exposed to ionizing radiation (Cesium-138 source) and whole blood was collected by cardiac puncture 6 hours post treatment. Doses were 0 (7 samples) 2 (5 samples) and 8 (6 samples) gy.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-156",
+                    "mediaType": "text/html",
+                    "title": "Identifying radiation exposure biomarkers from mouse blood transcriptome"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-156_xt8w-vdtd",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "specified_biomaterial_action",
                 "p-gse33172-8",
@@ -1649416,47 +1649430,35 @@
                 "p-gse33172-5",
                 "p-gse33172-4"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xt8w-vdtd",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-156_xt8w-vdtd",
-            "description": "Here we present a whole-genome survey of the murine transcriptomic response to physiologically-relevant radiation doses 2 and 8 Gy. There are 18 distinct biological samples here. Mice were exposed to ionizing radiation (Cesium-138 source) and whole blood was collected by cardiac puncture 6 hours post treatment. Doses were 0 (7 samples) 2 (5 samples) and 8 (6 samples) gy.",
-            "title": "Identifying radiation exposure biomarkers from mouse blood transcriptome",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-156",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Identifying radiation exposure biomarkers from mouse blood transcriptome"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Identifying radiation exposure biomarkers from mouse blood transcriptome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-DBP-3-RDR-24COLOR-V2.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset is comprised of asteroid flux data measured in 26 filters using the McCord dual beam photometer, and covering the range 0.32 - 1.08 microns for 285 numbered asteroids, as published in Chapman & Gaffey (1979b) and McFadden, et al. (1984).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-dbp-3-rdr-24color-v2.1_xt99-8r33",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "1075 helina",
                 "support archives",
@@ -1649743,301 +1649745,313 @@
                 "32 pomona",
                 "326 tamara"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-DBP-3-RDR-24COLOR-V2.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-dbp-3-rdr-24color-v2.1_xt99-8r33",
-            "description": "This dataset is comprised of asteroid flux data measured in 26 filters using the McCord dual beam photometer, and covering the range 0.32 - 1.08 microns for 285 numbered asteroids, as published in Chapman & Gaffey (1979b) and McFadden, et al. (1984).",
-            "title": "24-COLOR ASTEROID SURVEY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "24-COLOR ASTEROID SURVEY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-ESC2-MTP015-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 15 period of the ESCORT 2 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-esc2-mtp015-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-ESC2-MTP015-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-esc2-mtp015-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 15 period of the ESCORT 2 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 ESCORT 2\n    MTP015 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 5 ESCORT 2\n    MTP015 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC2-67PCHURYUMOV-M17-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-06-02 to 2015-06-30.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc2-67pchuryumov-m17-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC2-67PCHURYUMOV-M17-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc2-67pchuryumov-m17-v1.0",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-06-02 to 2015-06-30.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 3 RDR MTP 017 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 3 RDR MTP 017 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0618-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-02T22:17:55.000 to 2015-03-03T09:44:27.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0618-v1.0_xtdd-df6j",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0618-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0618-v1.0_xtdd-df6j",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-02T22:17:55.000 to 2015-03-03T09:44:27.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0618 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0618 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-3/RADIOMETER/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gasiewski, Albin J.2001. CAMEX-3 POLARIMETRIC SCANNING RADIOMETER (PSR) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-3/RADIOMETER/DATA101",
-            "issued": "2001-05-11",
-            "temporal": "1998-08-06T00:00:00Z/1998-09-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-18",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "microwave"
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
-            "identifier": "C1979111637-GHRC_DAAC",
             "description": "The Polarimetric Scanning Radiometer (PSR) is a versatile airborne microwave imaging radiometer developed by the Georgia Institute of Technology and the NOAA Environmental Technology Laboratory for the purpose of obtaining polarimetric microwave emission imagery of the Earth's oceans, land, ice, clouds, and precipitation.",
-            "graphic-preview-description": "N/A",
-            "title": "CAMEX-3 POLARIMETRIC SCANNING RADIOMETER (PSR) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/dc8psr/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FRADIOMETER%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FRADIOMETER%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=dc8psr",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=dc8psr",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/dc8psr/browse/1998_0813_187h_front.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/dc8psr/browse/1998_0813_187h_front.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex3/dc8psr/dc8psr_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex3/dc8psr/dc8psr_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/dc8psr/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/dc8psr/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/dc8psr/browse/",
+            "identifier": "C1979111637-GHRC_DAAC",
+            "issued": "2001-05-11",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-3/RADIOMETER/DATA101",
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
             "spatial": "-105.0 10.0 -50.0 50.0",
+            "temporal": "1998-08-06T00:00:00Z/1998-09-23T00:00:00Z",
             "theme": [
                 "CAMEX-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-3 POLARIMETRIC SCANNING RADIOMETER (PSR) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2801723593-LAADS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "National Aeronautics and Space Administration (NASA),. 2023-11-01. Enhanced MODIS Airborne Simulator (eMAS) L2 Cloud Data. Version 1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Level 1 and Atmosphere Archive and Distribution System (LAADS).",
-            "issued": "2013-08-01",
-            "temporal": "2013-08-01T00:00:00Z/2016-09-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-27",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "infrared wavelengths",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EMAS SCIENCE TEAM",
                 "hasEmail": "mailto:roseanne.dominguez@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/LAADS"
-            },
-            "identifier": "C2801723593-LAADS",
-            "description": "The Enhanced Moderate Resolution Imaging Spectroradiometer (MODIS) Airborne Simulator (eMAS)instrument is maintained and operated by the Airborne Sensor Facility at NASA Ames Research Center in Mountain View, California, under the oversight of the EOS Project Science Office at NASA Goddard. The eMAS instrument is now a 38-channel instrument, sensing in the range from 0.445 to 13.844 um.\r\n\r\nThe Enhanced MODIS Airborne Simulator (eMAS) L2 Cloud Data product (eMASL2CLD) consists of cloud optical and physical parameters. These parameters are derived using remotely sensed infrared and near infrared solar reflected radiances. Multispectral images of the reflectance and brightness temperature at 10 wavelengths between 0.66 and 13.98nm were used to derive the probability of clear sky (or cloud), cloud thermodynamic phase, and the optical thickness and effective radius of liquid water and ice clouds. The eMASL2CLD product files are stored in Hierarchical Data Format (HDF-EOS). All gridded cloud parameters are stored as Scientific Data Sets (SDS) within the file.\r\n\r\n\r\n\r\nFor more information and for a list of MAS campaign flights  visit ladsweb at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/mas/\r\n\r\nor, visit the eMAS Homepage at:\r\n\r\nhttps://asapdata.arc.nasa.gov/emas/",
-            "release-place": "Greenbelt, MD, USA",
             "creator": "National Aeronautics and Space Administration (NASA),",
-            "title": "Enhanced MODIS Airborne Simulator (eMAS) L2 Cloud Data",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Enhanced Moderate Resolution Imaging Spectroradiometer (MODIS) Airborne Simulator (eMAS)instrument is maintained and operated by the Airborne Sensor Facility at NASA Ames Research Center in Mountain View, California, under the oversight of the EOS Project Science Office at NASA Goddard. The eMAS instrument is now a 38-channel instrument, sensing in the range from 0.445 to 13.844 um.\r\n\r\nThe Enhanced MODIS Airborne Simulator (eMAS) L2 Cloud Data product (eMASL2CLD) consists of cloud optical and physical parameters. These parameters are derived using remotely sensed infrared and near infrared solar reflected radiances. Multispectral images of the reflectance and brightness temperature at 10 wavelengths between 0.66 and 13.98nm were used to derive the probability of clear sky (or cloud), cloud thermodynamic phase, and the optical thickness and effective radius of liquid water and ice clouds. The eMASL2CLD product files are stored in Hierarchical Data Format (HDF-EOS). All gridded cloud parameters are stored as Scientific Data Sets (SDS) within the file.\r\n\r\n\r\n\r\nFor more information and for a list of MAS campaign flights  visit ladsweb at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/mas/\r\n\r\nor, visit the eMAS Homepage at:\r\n\r\nhttps://asapdata.arc.nasa.gov/emas/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/440/eMASL2CLD/",
-                    "description": "Direct access to eMAS data from LAADS.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to eMAS data from LAADS.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/440/eMASL2CLD/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asapdata.arc.nasa.gov/",
-                    "description": "The Airborne Sensor Facility (ASF) at NASA Ames Research Center.",
                     "@type": "dcat:Distribution",
+                    "description": "The Airborne Sensor Facility (ASF) at NASA Ames Research Center.",
+                    "downloadURL": "https://asapdata.arc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "identifier": "C2801723593-LAADS",
+            "issued": "2013-08-01",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "infrared wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2801723593-LAADS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-09-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/LAADS"
+            },
+            "release-place": "Greenbelt, MD, USA",
             "spatial": "-180.0 -35.0 180.0 80.0",
+            "temporal": "2013-08-01T00:00:00Z/2016-09-28T00:00:00Z",
             "theme": [
                 "MAS_eMAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Enhanced MODIS Airborne Simulator (eMAS) L2 Cloud Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xtnr-hbnt",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Space radiations and microgravity both could cause DNA damage in cells but the effects of microgravity on DNA damage response to space radiations are still controversial. A mRNA microarray and microRNA microarray in dauer larvae of Caenorhabditis elegans (C. elegans) that endured space xef xac x82ight environment and space radiations environment during 16.5-day Shenzhou-8 space mission were performed. In our study wild type dys-1 mutant and ced-1 mutant strains of C.elegans endured four conditions during shenzhou-8 spaceflight mission including spaceflight static condition(ss) spaceflight 1-g centrifugal condition(sc) ground control condition(gc) and no-transport control. Limited to the quantity of worm samples we performed technical-repeat test but not sample-repeat test.Accordingly 12 mRNA microarrays were performed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-167",
+                    "mediaType": "text/html",
+                    "title": "Synergistic effects of microgravity and space radiation (Nimblegen)"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-167_xtnr-hbnt",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample collection",
                 "absorbed radiation dose",
@@ -1650048,306 +1650062,303 @@
                 "labeling",
                 "data collection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xtnr-hbnt",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-167_xtnr-hbnt",
-            "description": "Space radiations and microgravity both could cause DNA damage in cells but the effects of microgravity on DNA damage response to space radiations are still controversial. A mRNA microarray and microRNA microarray in dauer larvae of Caenorhabditis elegans (C. elegans) that endured space xef xac x82ight environment and space radiations environment during 16.5-day Shenzhou-8 space mission were performed. In our study wild type dys-1 mutant and ced-1 mutant strains of C.elegans endured four conditions during shenzhou-8 spaceflight mission including spaceflight static condition(ss) spaceflight 1-g centrifugal condition(sc) ground control condition(gc) and no-transport control. Limited to the quantity of worm samples we performed technical-repeat test but not sample-repeat test.Accordingly 12 mRNA microarrays were performed.",
-            "title": "Synergistic effects of microgravity and space radiation (Nimblegen)",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-167",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Synergistic effects of microgravity and space radiation (Nimblegen)"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Synergistic effects of microgravity and space radiation (Nimblegen)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-PEPSSI-3-KEM1-V1.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-pepssi-3-kem1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-PEPSSI-3-KEM1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-pepssi-3-kem1-v1.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
-            "title": "NEW HORIZONS\n      PEPSSI KEM1\n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      PEPSSI KEM1\n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M03-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m03-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M03-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m03-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP003 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP003 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR10-H%2FL%2FV-NAC%2FWAC-2-EDR-V1.0",
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
+            "description": "This series of fifteen CDs was produced by JPL's Science Digital Data Preservation Task (SDDPT) by migrating the original Mariner Ten image EDRs from old, deteriorating",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr10-h-l-v-nac-wac-2-edr-v1.0_xtrb-k46i",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pds"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR10-H%2FL%2FV-NAC%2FWAC-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr10-h-l-v-nac-wac-2-edr-v1.0_xtrb-k46i",
-            "description": "This series of fifteen CDs was produced by JPL's Science Digital Data Preservation Task (SDDPT) by migrating the original Mariner Ten image EDRs from old, deteriorating",
-            "title": "MARINER 10 IMAGING ARCHIVE EXPERIMENT DATA RECORD",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARINER 10 IMAGING ARCHIVE EXPERIMENT DATA RECORD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/245",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schuepp, P.H., and S.O. Ogunjemiyo. 1999. BOREAS AFM-13 Aircraft Flux Analyses. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/245",
-            "issued": "2023-11-22",
-            "temporal": "1994-01-01T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-17",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere",
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
-            "identifier": "C2813393915-ORNL_CLOUD",
             "description": "Not technically a data set, this is a report of the cross-comparison of data collected by various flux aircraft. Reports of these analyses are available as TIF and ASCII files.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS AFM-13 Aircraft Flux Analyses",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F245",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F245",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/afm13afr/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/afm13afr/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM13.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM13.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/245",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/245",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/AFM13.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/AFM13.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/AFM13.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/AFM13.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/AFM13.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/AFM13.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/afm13afr.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm13afr/comp/afm13afr.def",
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
+            "identifier": "C2813393915-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/245",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-111.0 49.0 -89.0 60.0",
+            "temporal": "1994-01-01T00:00:00Z/1996-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS AFM-13 Aircraft Flux Analyses"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-CAL-SSI-6-V1.0",
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
-                "non science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-cal-ssi-6-v1.0_xtv8-jsuc",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo",
+                "non science"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-CAL-SSI-6-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-cal-ssi-6-v1.0_xtv8-jsuc",
-            "description": "not applicable",
-            "title": "GALILEO SOLID STATE IMAGING CALIBRATION FILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO SOLID STATE IMAGING CALIBRATION FILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xtxe-vuny",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kim Tolbert",
+                "hasEmail": "mailto:kim.tolbert@nasa.gov"
+            },
+            "description": "Time-dependent detector response matrices for each GBM detector covering the duration of every GBM flare.  Needed in the spectral analysis software to relate observed count-rate spectra to model photon spectra. Suitable for analyzing CPEC and CTIME data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://hesperia.gsfc.nasa.gov/fermi/gbm/rsp/",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "NASA-0000246",
             "issued": "2018-06-25",
-            "temporal": "2008-08-12/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "solar",
                 "gbm",
@@ -1650357,252 +1650368,220 @@
                 "telescope",
                 "nai"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kim Tolbert",
-                "hasEmail": "mailto:kim.tolbert@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xtxe-vuny",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000246",
-            "description": "Time-dependent detector response matrices for each GBM detector covering the duration of every GBM flare.  Needed in the spectral analysis software to relate observed count-rate spectra to model photon spectra. Suitable for analyzing CPEC and CTIME data.",
-            "title": "GBM Response Matrix FITS Files",
-            "programCode": [
-                "026:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://hesperia.gsfc.nasa.gov/fermi/gbm/rsp/",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-12/2014-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "GBM Response Matrix FITS Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/809/",
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
-            "identifier": "DASHLINK_809",
             "description": "Prognostics, which deals with predicting remaining useful life of components, subsystems, and systems, is a key tech- nology for systems health management that leads to improved safety and reliability with reduced costs. The prognostics problem is often approached from a component-centric view. However, in most cases, it is not specifically component life- times that are important, but, rather, the lifetimes of the sys- tems in which these components reside. The system-level prognostics problem can be quite difficult due to the increased scale and scope of the prognostics problem and the rela- tive lack of scalability and efficiency of typical prognostics approaches. In order to address these issues, we develop a distributed solution to the system-level prognostics prob- lem, based on the concept of structural model decomposi- tion. The system model is decomposed into independent submodels. Independent local prognostics subproblems are then formed based on these local submodels, resulting in a scalable, efficient, and flexible distributed approach to the system-level prognostics problem. We provide a formulation of the system-level prognostics problem and demonstrate the approach on a four-wheeled rover simulation testbed. The re- sults show that the system-level prognostics problem can be accurately and efficiently solved in a distributed fashion.",
-            "title": "A Distributed Approach to System-Level Prognostics",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/5-DaigleEtAl-PHM2012SystemLevel.pdf",
-                    "description": "5-DaigleEtAl-PHM2012SystemLevel.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "5-DaigleEtAl-PHM2012SystemLevel.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/5-DaigleEtAl-PHM2012SystemLevel.pdf",
+                    "mediaType": "application/pdf",
                     "title": "5-DaigleEtAl-PHM2012SystemLevel.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_809",
+            "issued": "2013-07-29",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/809/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Distributed Approach to System-Level Prognostics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOC-NA%2FWA-2-DSDP-L0-V1.0",
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
+            "description": "This data set contains portions of the MOC Decompressed Standard Data Product (DSDP) Archive, a collection of decompressed images from the Mars Orbiter Camera on the Mars Global Surveyor spacecraft. Images are stored with PDS labels, but are otherwise unprocessed and uncalibrated.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-moc-na-wa-2-dsdp-l0-v1.0_xtzh-czam",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOC-NA%2FWA-2-DSDP-L0-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-moc-na-wa-2-dsdp-l0-v1.0_xtzh-czam",
-            "description": "This data set contains portions of the MOC Decompressed Standard Data Product (DSDP) Archive, a collection of decompressed images from the Mars Orbiter Camera on the Mars Global Surveyor spacecraft. Images are stored with PDS labels, but are otherwise unprocessed and uncalibrated.",
-            "title": "MOC DSDP ARCHIVE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MOC DSDP ARCHIVE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-SPICE-6-V1.0",
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
+            "description": "This data set includes the MSL SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contain geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide rover and planetary ephemerides, instrument mounting alignments, rover orientation, and data needed for relevant time conversions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-spice-6-v1.0_xu3i-ufb5",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-SPICE-6-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-spice-6-v1.0_xu3i-ufb5",
-            "description": "This data set includes the MSL SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contain geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide rover and planetary ephemerides, instrument mounting alignments, rover orientation, and data needed for relevant time conversions.",
-            "title": "MSL SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.lpw.calibrated&version=5.7",
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
-                "mars atmosphere and volatile evolution mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains fully calibrated, science quality data produced by the LPW  instrument. The data include spacecraft potential, electric field waveforms  and wave power. The data have been provided by the LPW team in CDF files.",
+            "identifier": "urn:nasa:pds:maven.lpw.calibrated_xu3w-ijtb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars atmosphere and volatile evolution mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.lpw.calibrated&version=5.7",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:maven.lpw.calibrated_xu3w-ijtb",
-            "description": "This bundle contains fully calibrated, science quality data produced by the LPW  instrument. The data include spacecraft potential, electric field waveforms  and wave power. The data have been provided by the LPW team in CDF files.",
-            "title": "MAVEN LPW Calibrated Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAVEN LPW Calibrated Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV-3%2F4-EPOXI-HARTLEY2-V1.0",
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
+            "description": "This dataset contains calibrated clear-filter images of comet 103/P Hartley 2 acquired by the High Resolution Visible CCD (HRIV) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Four color-filter sets (350-950 nm) were acquired during the hour about closest approach.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-3-4-epoxi-hartley2-v1.0_xu4e-jfbr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "epoxi",
+                "103p/hartley 2 (1986 e2)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV-3%2F4-EPOXI-HARTLEY2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-3-4-epoxi-hartley2-v1.0_xu4e-jfbr",
-            "description": "This dataset contains calibrated clear-filter images of comet 103/P Hartley 2 acquired by the High Resolution Visible CCD (HRIV) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Four color-filter sets (350-950 nm) were acquired during the hour about closest approach.",
-            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRIV CALIBRATED IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRIV CALIBRATED IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://curator.jsc.nasa.gov/lunar/catalogs/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://curator.jsc.nasa.gov/lunar/catalogs/apollo14catalog.cfm"
-            ],
-            "keyword": [
-                "catalog",
-                "lunar",
-                "apollo",
-                "sample"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carlton Allen",
                 "hasEmail": "mailto:carlton.c.allen@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-879",
             "description": "Apollo 16 Special Samples by F. Horz et al.",
-            "title": "Apollo 16 Special Samples",
-            "programCode": [
-                "026:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1650610,93 +1650589,89 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-879",
+            "issued": "2018-06-25",
+            "keyword": [
+                "catalog",
+                "lunar",
+                "apollo",
+                "sample"
+            ],
+            "landingPage": "http://curator.jsc.nasa.gov/lunar/catalogs/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://curator.jsc.nasa.gov/lunar/catalogs/apollo14catalog.cfm"
+            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Apollo 16 Special Samples"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PPR-2-EDR-IDA-V1.0",
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
+            "description": "This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Ida asteroid encounter observations in October 1993.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ppr-2-edr-ida-v1.0_xu7c-zg3z",
+            "issued": "2021-05-21",
+            "keyword": [
+                "ida",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PPR-2-EDR-IDA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ppr-2-edr-ida-v1.0_xu7c-zg3z",
-            "description": "This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Ida asteroid encounter observations in October 1993.",
-            "title": "GLL PPR IDA ENCOUNTER EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GLL PPR IDA ENCOUNTER EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/MINDS/DATA214",
             "citation": "Lok N. Lamsal, Nickolay A. Krotkov, Sergey V. Marchenko, Joanna Joiner, Luke Oman, Alexander Vasilkov, Bradford Fisher, Wenhan Qin, Eun-Su Yang, Zachary Fasnacht, Sungyeon Choi, Peter Leonard, and David Haffner. 2022-04-15. OMI_MINDS_NO2G. Version 1.1. OMI/Aura NO2 Tropospheric, Stratospheric & Total Columns MINDS Daily L2 Global Gridded 0.25 degree x 0.25 degree. NASA Goddard Space Flight Center. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/MINDS/DATA214. https://disc.gsfc.nasa.gov/datacollection/OMI_MINDS_NO2G_1.1.html. Digital Science Data.",
-            "issued": "2021-11-09",
-            "temporal": "2004-10-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-04",
-            "references": [
-                "https://doi.org/10.5194/amt-14-455-2021"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lok Lamsal, PH. D",
                 "hasEmail": "mailto:lok.lamsal@nasa.gov"
             },
+            "creator": "Lok N. Lamsal, Nickolay A. Krotkov, Sergey V. Marchenko, Joanna Joiner, Luke Oman, Alexander Vasilkov, Bradford Fisher, Wenhan Qin, Eun-Su Yang, Zachary Fasnacht, Sungyeon Choi, Peter Leonard, and David Haffner",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2232479983-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "As part of the NASA's Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, this project entitled \u201cMulti-Decadal Nitrogen Dioxide and Derived Products from Satellites (MINDS)\u201d will develop consistent long-term global trend-quality data records spanning the last two decades, over which remarkable changes in nitrogen oxides (NOx) emissions have occurred. The objective of the project Is to adapt Ozone Monitoring Instrument (OMI) operational algorithms to other satellite instruments and create consistent multi-satellite L2 and L3 nitrogen dioxide (NO2) columns and value-added L4 surface NO2 concentrations and NOx emissions data products, systematically accounting for instrumental differences. The instruments include Global Ozone Monitoring Experiment (GOME, 1996-2011), SCanning Imaging Absorption spectroMeter for Atmospheric CHartographY (SCIAMACHY, 2002-2012), OMI (2004-present), GOME-2 (2007-present), and TROPOspheric Monitoring Instrument (TROPOMI, 2018-present). The quality assured L2-L4 products will be made available to the scientific community via the NASA GES DISC website in Climate and Forecast (CF)-compliant Hierarchical Data Format (HDF5) and netCDF formats.",
-            "release-place": "NASA Goddard Space Flight Center",
-            "series-name": "OMI_MINDS_NO2G",
-            "creator": "Lok N. Lamsal, Nickolay A. Krotkov, Sergey V. Marchenko, Joanna Joiner, Luke Oman, Alexander Vasilkov, Bradford Fisher, Wenhan Qin, Eun-Su Yang, Zachary Fasnacht, Sungyeon Choi, Peter Leonard, and David Haffner",
-            "title": "OMI/Aura NO2 Tropospheric, Stratospheric & Total Columns MINDS Daily L2 Global Gridded 0.25 degree x 0.25 degree V1.1 (OMI_MINDS_NO2G) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMI_MINDS_NO2G_1.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FMINDS%2FDATA214",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FMINDS%2FDATA214",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1650706,792 +1650681,831 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMI_MINDS_NO2G_1.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMI_MINDS_NO2G_1.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/esds/competitive-programs/measures/minds",
-                    "description": "NASA ESDS MEaSUREs MINDS Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA ESDS MEaSUREs MINDS Home Page",
+                    "downloadURL": "https://earthdata.nasa.gov/esds/competitive-programs/measures/minds",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gsfc.nasa.gov/",
-                    "description": "EOS Aura Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "EOS Aura Project Home Page",
+                    "downloadURL": "https://aura.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/MINDS/OMI_MINDS_NO2G.1.1/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/MINDS/OMI_MINDS_NO2G.1.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMI_MINDS_NO2G_1.1",
-                    "description": "Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMI_MINDS_NO2G_1.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/MINDS/OMI_MINDS_NO2G.1.1/",
-                    "description": "OPeNDAP Service",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP Service",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/MINDS/OMI_MINDS_NO2G.1.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/MINDS/OMI_MINDS_NO2.1.1/doc/README.MEaSUREs_MINDS_NO2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/MINDS/OMI_MINDS_NO2.1.1/doc/README.MEaSUREs_MINDS_NO2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMI_MINDS_NO2G_1.1.png",
+            "identifier": "C2232479983-GES_DISC",
+            "issued": "2021-11-09",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/MINDS/DATA214",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-14-455-2021"
+            ],
+            "release-place": "NASA Goddard Space Flight Center",
+            "series-name": "OMI_MINDS_NO2G",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura NO2 Tropospheric, Stratospheric & Total Columns MINDS Daily L2 Global Gridded 0.25 degree x 0.25 degree V1.1 (OMI_MINDS_NO2G) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACTIVATE-FLEXPART_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-03-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/ACTIVATE-FLEXPART_1.",
-            "issued": "2020-02-15",
-            "temporal": "2020-02-14T00:00:00Z/2022-06-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-18",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bo Zhang",
                 "hasEmail": "mailto:bo.zhang@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2647129204-LARC_ASDC",
             "description": "ACTIVATE-FLEXPART is the FLEXible PARTicle dispersion model back-trajectories ending at the HU-25 Falcon locations. \r\nACTIVATE was a 5-year NASA Earth-Venture Sub-Orbital (EVS-3) field campaign. Marine boundary layer clouds play a critical role in Earth\u2019s energy balance and water cycle. These clouds cover more than 45% of the ocean surface and exert a net cooling effect. The Aerosol Cloud meTeorology Interactions oVer the western Atlantic Experiment (ACTIVATE) project was a five-year project that provides important globally-relevant data about changes in marine boundary layer cloud systems, atmospheric aerosols and multiple feedbacks that warm or cool the climate. ACTIVATE studied the atmosphere over the western North Atlantic and sampled its broad range of aerosol, cloud and meteorological conditions using two aircraft, the UC-12 King Air and HU-25 Falcon. The UC-12 King Air was primarily used for remote sensing measurements while the HU-25 Falcon will contain a comprehensive instrument payload for detailed in-situ measurements of aerosol, cloud properties, and atmospheric state. A few trace gas measurements were also onboard the HU-25 Falcon for the measurements of pollution traces, which will contribute to airmass classification analysis. A total of 150 coordinated flights over the western North Atlantic occurred through 6 deployments from 2020-2022. The ACTIVATE science observing strategy intensively targets the shallow cumulus cloud regime and aims to collect sufficient statistics over a broad range of aerosol and weather conditions which enables robust characterization of aerosol-cloud-meteorology interactions. This strategy was implemented by two nominal flight patterns: Statistical Survey and Process Study. The statistical survey pattern involves close coordination between the remote sensing and in-situ aircraft to conduct near coincident sampling at and below cloud base as well as above and within cloud top. The process study pattern involves extensive vertical profiling to characterize the target cloud and surrounding aerosol and meteorological conditions.",
-            "title": "ACTIVATE FLEXible PARTicle (FLEXPART) Dispersion Model Back-trajectories",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FACTIVATE-FLEXPART_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FACTIVATE-FLEXPART_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "ASDC Data Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data Citation Policy",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/nasa-embarks-on-us-cross-country-expeditions",
-                    "description": "Nasa.gov Feature \u201cNASA Embarks on Five U.S. Expeditions Targeting Air, Land, and Sea\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "Nasa.gov Feature \u201cNASA Embarks on Five U.S. Expeditions Targeting Air, Land, and Sea\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/nasa-embarks-on-us-cross-country-expeditions",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/probing-the-hazy-mysteries-of-marine-clouds",
-                    "description": "Nasa.gov Feature \u201cProbing the Hazy Mysteries of Marine Clouds\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "Nasa.gov Feature \u201cProbing the Hazy Mysteries of Marine Clouds\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/probing-the-hazy-mysteries-of-marine-clouds",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/activate-makes-a-careful-return-to-flight",
-                    "description": "Nasa.gov Feature \u201cACTIVATE Makes a Careful Return to Flight\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "Nasa.gov Feature \u201cACTIVATE Makes a Careful Return to Flight\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/activate-makes-a-careful-return-to-flight",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/advancing-aerosol-cloud-meteorology-knowledge-through-activate",
-                    "description": "ASDC Microarticle \u201cAdvancing Aerosol-Cloud-Meteorology Knowledge through ACTIVATE\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Microarticle \u201cAdvancing Aerosol-Cloud-Meteorology Knowledge through ACTIVATE\u201d",
+                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/advancing-aerosol-cloud-meteorology-knowledge-through-activate",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://storymaps.arcgis.com/stories/851338f794274388bd5f3280eda55612",
-                    "description": "Armin Sorooshian Researcher Profile",
                     "@type": "dcat:Distribution",
+                    "description": "Armin Sorooshian Researcher Profile",
+                    "downloadURL": "https://storymaps.arcgis.com/stories/851338f794274388bd5f3280eda55612",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://creativecommons.org/publicdomain/zero/1.0/",
-                    "description": "Creative Commons License for ACTIVATE",
                     "@type": "dcat:Distribution",
+                    "description": "Creative Commons License for ACTIVATE",
+                    "downloadURL": "https://creativecommons.org/publicdomain/zero/1.0/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2647129204-LARC_ASDC",
-                    "description": "Earthdata Search for ACTIVATE-FLEXPART_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ACTIVATE-FLEXPART_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2647129204-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACTIVATE-FLEXPART_1",
-                    "description": "DOI for ACTIVATE-FLEXPART_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for ACTIVATE-FLEXPART_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACTIVATE-FLEXPART_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://essd.copernicus.org/articles/15/3419/2023/",
-                    "description": "Spatially coordinated airborne data and complementary products for aerosol, gas, cloud, and meteorological studies: the NASA ACTIVATE dataset",
                     "@type": "dcat:Distribution",
+                    "description": "Spatially coordinated airborne data and complementary products for aerosol, gas, cloud, and meteorological studies: the NASA ACTIVATE dataset",
+                    "downloadURL": "https://essd.copernicus.org/articles/15/3419/2023/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://storymaps.arcgis.com/stories/afb08663731c4e19897e74e19efd2cf6",
-                    "description": "ACTIVATE StoryMap",
                     "@type": "dcat:Distribution",
+                    "description": "ACTIVATE StoryMap",
+                    "downloadURL": "https://storymaps.arcgis.com/stories/afb08663731c4e19897e74e19efd2cf6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACTIVATE/FLEXPART_1/",
-                    "description": "ASDC Direct Data Download for ACTIVATE-FLEXPART_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ACTIVATE-FLEXPART_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACTIVATE/FLEXPART_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2647129204-LARC_ASDC",
+            "issued": "2020-02-15",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACTIVATE-FLEXPART_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-06-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>0.0 -180.0 0.0 180.0 90.0 180.0 90.0 -180.0 0.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2020-02-14T00:00:00Z/2022-06-30T00:00:00Z",
             "theme": [
                 "ACTIVATE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACTIVATE FLEXible PARTicle (FLEXPART) Dispersion Model Back-trajectories"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0968-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-17T21:32:20.000 to 2015-08-18T03:40:09.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0968-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0968-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0968-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-17T21:32:20.000 to 2015-08-18T03:40:09.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0968 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0968 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/Missouri_Reservoirs_RSWQ/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/Missouri_Reservoirs_RSWQ/DATA001.",
-            "issued": "2023-05-01",
-            "temporal": "2023-05-01T00:00:01Z/2023-10-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
-            "keyword": [
-                "salinity/density",
-                "earth science",
-                "ocean chemistry",
-                "ocean optics",
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
-            "identifier": "C2785397264-OB_DAAC",
             "description": "The dataset comprises in-situ hyperspectral data acquired using the on-water approach (aka skylight-blocked approach), using a combination of a downwelling irradiance sensor and an upwelling radiance sensor. These sensors are specifically TriOS RAMSES hyperspectral radiometers, each associated with two calibration files. The data collection was conducted across different reservoirs in the state of Missouri USA. This NASA-funded project directly addresses how Earth-observing satellite data can better inform critical links between the biogeochemical and optical properties of inland waters. It achieves this by using satellite imagery and in-situ measurements from two long-running water quality monitoring programs in the state of Missouri that annually record more than one thousand measurements of nitrogen, phosphorus, chlorophyll-a, Secchi depth, particulate organic and inorganic matter, and cyanotoxins across 100 reservoirs.",
-            "title": "Retrospective analysis of anthropogenic change in Midwest reservoirs: Integrating earth observing data with statewide reservoir monitoring programs",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMissouri_Reservoirs_RSWQ%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMissouri_Reservoirs_RSWQ%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Missouri_Reservoirs_RSWQ/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Missouri_Reservoirs_RSWQ/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2785397264-OB_DAAC",
+            "issued": "2023-05-01",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/Missouri_Reservoirs_RSWQ/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-05-01T00:00:01Z/2023-10-23T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Retrospective analysis of anthropogenic change in Midwest reservoirs: Integrating earth observing data with statewide reservoir monitoring programs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0529-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-31T00:38:20.000 to 2014-12-31T03:41:26.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0529-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0529-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0529-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-31T00:38:20.000 to 2014-12-31T03:41:26.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0529 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0529 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-3-RDR-ELS-EXT1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains calibrated Mars Express ASPERA-3 Electron Spectrometer (ELS) data for the first mission extension (January 1, 2006 - September 30, 2007). These data are provided in units of Differential Number Flux (DNF): cnts/(cm**2-sr-sec-eV)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-3-rdr-els-ext1-v1.0_xubf-7bpb",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-3-RDR-ELS-EXT1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-3-rdr-els-ext1-v1.0_xubf-7bpb",
-            "description": "This data set contains calibrated Mars Express ASPERA-3 Electron Spectrometer (ELS) data for the first mission extension (January 1, 2006 - September 30, 2007). These data are provided in units of Differential Number Flux (DNF): cnts/(cm**2-sr-sec-eV)",
-            "title": "MARS EXPRESS ASPERA-3 CAL RDR ELECTRON SPECTROMTR EXT1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARS EXPRESS ASPERA-3 CAL RDR ELECTRON SPECTROMTR EXT1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/568",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kittel, T.G.F., N.A. Rosenbloom, C. Kaufman, J.A. Royle, C. Daly, H.H. Fisher, W.P. Gibson, S. Aulenbach, D.N. Yates, R. McKeown, D.S. Schimel, and  VEMAP 2 Participants. 2000. VEMAP 2: U.S. Monthly Climate, 1895-1993, Version 2 . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/568",
-            "issued": "2024-04-22",
-            "temporal": "1895-01-01T00:00:00Z/1993-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-23",
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric temperature"
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
-            "identifier": "C2946946128-ORNL_CLOUD",
             "description": "An integrated input data set for ecosystem and vegetation modeling for the conterminous United States. The data set is a ~100 year gridded monthly time series of climate that includes realistic interannual variability.",
-            "graphic-preview-description": "Browse Image",
-            "title": "VEMAP 2: U.S. Monthly Climate, 1895-1993, Version 2",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/567_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F568",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F568",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-2_TCLIMATE_monthly/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-2_TCLIMATE_monthly/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/Vemap-2_MonthlyClimate.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/Vemap-2_MonthlyClimate.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/568",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/568",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/x-netcdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/geog3.nc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/geog3.nc",
+                    "mediaType": "application/x-netcdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/gridpt2record.c",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/gridpt2record.c",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/grid_mask",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/grid_mask",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/is92a.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/is92a.dat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/is92a.readme",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/is92a.readme",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/ncREADday7.c",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/ncREADday7.c",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/ncREADmon6.c",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/ncREADmon6.c",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/Phase_2_User_Guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/Phase_2_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/README.Tclimate3",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/README.Tclimate3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/record2gridpt.c",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/record2gridpt.c",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/Vemap-2_MonthlyClimate.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_monthly/comp/Vemap-2_MonthlyClimate.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/567_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/567_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/568/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/568/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/567_1_fit.png",
+            "identifier": "C2946946128-ORNL_CLOUD",
+            "issued": "2024-04-22",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/568",
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
+            "title": "VEMAP 2: U.S. Monthly Climate, 1895-1993, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-J-IRIS-5-NS-ATMOS-PARAMS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-j-iris-5-ns-atmos-params-v1.0_xuds-397m",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "voyager",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-J-IRIS-5-NS-ATMOS-PARAMS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-j-iris-5-ns-atmos-params-v1.0_xuds-397m",
-            "description": "The data set contains Jovian atmospheric parameters derived from spectra obtained with the Voyager infrared interferometer spectrometer (IRIS). The data set is ordered by time as measured by the Flight Data System Count (FDSC). This represents the data frame number modulo 60. Also included in the data set are information on pointing and associated geometry of the measurements and brightness temperatures obtained from measured radiances at selected wavenumbers.",
-            "title": "VOYAGER 1&2 JUPITER IRIS DERIVED NORTH/SOUTH PARAMETERS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 1&2 JUPITER IRIS DERIVED NORTH/SOUTH PARAMETERS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/NAV/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yang Martin, Melissa .2017. GPM Ground Validation Navigation Data DC-8 OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/NAV/DATA301",
-            "issued": "2017-11-09",
-            "temporal": "2015-11-05T17:20:48Z/2015-12-19T21:53:05Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-18",
-            "keyword": [
-                "platform characteristics",
-                "spectral/engineering",
-                "atmosphere",
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
-            "identifier": "C1979637324-GHRC_DAAC",
             "description": "The GPM Ground Validation NASA DC-8 Navigation Data OLYMPEX dataset supplies navigation data collected by the NASA DC-8 aircraft for flights that occurred during November 5, 2015 through December 19, 2015 for the Olympic Mountains Experiment (OLYMPEX) GPM Ground Validation field campaign. This navigation dataset consists of multiple altitude, pressure, temperature, airspeed, and ground speed measurements in ASCII-IWG1 and XML data formats.",
-            "title": "GPM Ground Validation Navigation Data DC-8 OLYMPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FNAV%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FNAV%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmnavdc8olyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmnavdc8olyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "description": "University of Washington OLYMPEX project web site",
                     "@type": "dcat:Distribution",
+                    "description": "University of Washington OLYMPEX project web site",
+                    "downloadURL": "http://olympex.atmos.washington.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/armstrong/news/FactSheets/FS-050-DFRC.html",
-                    "description": "NASA Armstrong Fact Sheet: DC-8 Airborne Science Laboratory",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Armstrong Fact Sheet: DC-8 Airborne Science Laboratory",
+                    "downloadURL": "https://www.nasa.gov/centers/armstrong/news/FactSheets/FS-050-DFRC.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NAV_DC8/doc/gpmnavdc8olyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NAV_DC8/doc/gpmnavdc8olyx_dataset.pdf",
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
+            "identifier": "C1979637324-GHRC_DAAC",
+            "issued": "2017-11-09",
+            "keyword": [
+                "platform characteristics",
+                "spectral/engineering",
+                "atmosphere",
+                "atmospheric winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/NAV/DATA301",
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
             "spatial": "-129.061 30.3686 -117.797 49.3344",
+            "temporal": "2015-11-05T17:20:48Z/2015-12-19T21:53:05Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Navigation Data DC-8 OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR14-V1.0",
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
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR14) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 23, August 12, and September 1 2012, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr14-v1.0_xuju-cxpw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR14-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr14-v1.0_xuju-cxpw",
-            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR14) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 23, August 12, and September 1 2012, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SAGR14 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SAGR14 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494549-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-14",
-            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "atmosphere",
-                "oceans",
-                "ocean optics",
-                "earth science",
-                "aerosols"
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
-            "identifier": "C2340494549-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-20 VIIRS Global Binned Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA20/VIIRS/L3B/RRS/2022",
-                    "description": "VIIRS-NOAA-20 L3B Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-20 L3B Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA20/VIIRS/L3B/RRS/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2340494549-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "atmosphere",
+                "oceans",
+                "ocean optics",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494549-OB_DAAC.html",
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
+            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-20 VIIRS Global Binned Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xunx-hnnk",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Ionizing radiations are categorized by linear energy transfer (LET) into low-LET and high-LET. High-LET is considered to have a higher relative biological effectiveness (RBE) than low-LET radiations. However the details of the effects have not been clearly determined. The aim of this study was to characterize the difference between high-LET and low LET radiations. The global effects of the three types of high-LET radiations (fast neutron heavy ion (C) and thermal neutron) were compared with the low-LET radiation (gamma ray) using yeast DNA microarrays. Highly induced genes by the three types of high-LET radiations were those genes related to oxidative stress. Oxidative stress was one of the common factors associated with the four types of radiations. Oxidative stress induced by high-LET radiations may be more serious than that induced by gamma rays. Additionally genes related to protein synthesis and the ubiquitin and proteasome system were detected. This suggests that more protein damages can be induced by high-LET radiation that denatures the proteins in yeast cells. The genes specifically altered by each type of high-LET radiation were also studied. Overall design: This series contains 4 kinds of irradiation-induced gene expression profiles. Triplicates hybridization was done in each irradiation exposure and each array have high and low power scanned data respectively. All biological samples were collected independently.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-97",
+                    "mediaType": "text/html",
+                    "title": "Gene-expression profiling of Saccharomyces cerevisiae irradiated by high-LET radiations"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-97_xunx-hnnk",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "growth and treatment protocol",
                 "radiation ionzing",
@@ -1651502,74 +1651516,35 @@
                 "nucleic acid hybridization",
                 "rna extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xunx-hnnk",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-97_xunx-hnnk",
-            "description": "Ionizing radiations are categorized by linear energy transfer (LET) into low-LET and high-LET. High-LET is considered to have a higher relative biological effectiveness (RBE) than low-LET radiations. However the details of the effects have not been clearly determined. The aim of this study was to characterize the difference between high-LET and low LET radiations. The global effects of the three types of high-LET radiations (fast neutron heavy ion (C) and thermal neutron) were compared with the low-LET radiation (gamma ray) using yeast DNA microarrays. Highly induced genes by the three types of high-LET radiations were those genes related to oxidative stress. Oxidative stress was one of the common factors associated with the four types of radiations. Oxidative stress induced by high-LET radiations may be more serious than that induced by gamma rays. Additionally genes related to protein synthesis and the ubiquitin and proteasome system were detected. This suggests that more protein damages can be induced by high-LET radiation that denatures the proteins in yeast cells. The genes specifically altered by each type of high-LET radiation were also studied. Overall design: This series contains 4 kinds of irradiation-induced gene expression profiles. Triplicates hybridization was done in each irradiation exposure and each array have high and low power scanned data respectively. All biological samples were collected independently.",
-            "title": "Gene-expression profiling of Saccharomyces cerevisiae irradiated by high-LET radiations",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-97",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Gene-expression profiling of Saccharomyces cerevisiae irradiated by high-LET radiations"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Gene-expression profiling of Saccharomyces cerevisiae irradiated by high-LET radiations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282248315-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2011-07-01. TRMM_1A01. TRMM Attitude and VIRS Packets and Header Record L1A V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_1A01_7.html.",
-            "issued": "1997-12-20",
-            "temporal": "1997-12-20T00:00:00Z/2014-03-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-03-21",
-            "keyword": [
-                "infrared wavelengths",
-                "sensor characteristics",
-                "spectral/engineering",
-                "visible wavelengths",
-                "earth science",
-                "platform characteristics"
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
-            "identifier": "C1282248315-GES_DISC",
-            "description": "The Level-1A Product file, \"1A01\", is a concatenation of Header record, Spacecraft Attitude packets, VIRS Housekeeping Data packets, VIRS Science Data packets, QACs, and an MDUL.\nAs such, it is reversible to Level 0. The header record contains information pertaining to orbit times, orbit number, times of the first scan, and number of scans, among other things. The Level 0 data contain the actual channel data expressed as \"sensor counts\". A Level 1A file contains data for a single orbit and has a file size of about 31 MB (uncompressed).  There are 16 files of VIRS 1A01 data produced per day.\n\nThe Visible and Infrared Scanner (VIRS) is a five-channel visible/infrared radiometer, which builds on the heritage of theAdvanced Very High Resolution Radiometer (AVHRR) instrument flown aboard the NOAA series of Polar-Orbiting Operational EnvironmentalSatellites (POES). The VIRS detects radiation at 1 visible, 2 near infrared and 2 thermal infrared wavelengths, allowing determination of cloud coverage, cloud top height and temperature, and precipitation indices. The central wavelengths for the VIRS channels are 0.63, 1.60,3.75, 10.8, and 12.0 microns. All channels are in operation during the daytime, but only channels 3, 4 and 5 operate during the nighttime.\n\nSpatial coverage is between 38 degrees North and 38 degrees South owing to the 35 degree inclination of the TRMM satellite. This orbit provides extensive coverage in the tropics and allows each location to be covered at a different local time each day, enabling the analysis of the diurnal cycle of precipitation.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_1A01",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Attitude and VIRS Packets and Header Record L1A V7 (TRMM_1A01) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_1A01_7.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Level-1A Product file, \"1A01\", is a concatenation of Header record, Spacecraft Attitude packets, VIRS Housekeeping Data packets, VIRS Science Data packets, QACs, and an MDUL.\nAs such, it is reversible to Level 0. The header record contains information pertaining to orbit times, orbit number, times of the first scan, and number of scans, among other things. The Level 0 data contain the actual channel data expressed as \"sensor counts\". A Level 1A file contains data for a single orbit and has a file size of about 31 MB (uncompressed).  There are 16 files of VIRS 1A01 data produced per day.\n\nThe Visible and Infrared Scanner (VIRS) is a five-channel visible/infrared radiometer, which builds on the heritage of theAdvanced Very High Resolution Radiometer (AVHRR) instrument flown aboard the NOAA series of Polar-Orbiting Operational EnvironmentalSatellites (POES). The VIRS detects radiation at 1 visible, 2 near infrared and 2 thermal infrared wavelengths, allowing determination of cloud coverage, cloud top height and temperature, and precipitation indices. The central wavelengths for the VIRS channels are 0.63, 1.60,3.75, 10.8, and 12.0 microns. All channels are in operation during the daytime, but only channels 3, 4 and 5 operate during the nighttime.\n\nSpatial coverage is between 38 degrees North and 38 degrees South owing to the 35 degree inclination of the TRMM satellite. This orbit provides extensive coverage in the tropics and allows each location to be covered at a different local time each day, enabling the analysis of the diurnal cycle of precipitation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1651578,80 +1651553,119 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_1A01_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_1A01_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1A/TRMM_1A01.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1A/TRMM_1A01.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_1A01",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_1A01",
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
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1A/TRMM_1A01/doc/README.TRMM_V7.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1A/TRMM_1A01/doc/README.TRMM_V7.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_1A01_7.png",
+            "identifier": "C1282248315-GES_DISC",
+            "issued": "1997-12-20",
+            "keyword": [
+                "infrared wavelengths",
+                "sensor characteristics",
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science",
+                "platform characteristics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282248315-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-03-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "TRMM_1A01",
             "spatial": "-180.0 -38.0 180.0 38.0",
+            "temporal": "1997-12-20T00:00:00Z/2014-03-21T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Attitude and VIRS Packets and Header Record L1A V7 (TRMM_1A01) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xuqe-zc2f",
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
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-104",
+                    "mediaType": "text/html",
+                    "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse soleus muscle transcriptomic and epigenomic data"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-104_xuqe-zc2f",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "dna library construction",
                 "animal and tissue sampling",
@@ -1651662,165 +1651676,127 @@
                 "sample collection",
                 "library construction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xuqe-zc2f",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-104_xuqe-zc2f",
-            "description": "NASA  s Rodent Research (RR) project is playing a critical role in advancing biomedical research on the physiological effects of space environments. Due to the limited resources for conducting biological experiments aboard the International Space Station (ISS) it is imperative to use crew time efficiently while maximizing high-quality science return. NASA  s GeneLab project has as its primary objectives to 1) further increase the value of these experiments using a multi-omics systems biology-based approach and 2) disseminate these data without restrictions to the scientific community. The current investigation assessed viability of RNA DNA and protein extracted from archived RR-1 tissue samples for epigenomic transcriptomic and proteomic assays. During the first RR spaceflight experiment a variety of tissue types were harvested from subjects snap-frozen or RNAlater-preserved and then stored at least a year at -80C after return to Earth. They were then prioritized for this investigation based on likelihood of significant scientific value for spaceflight research. All tissues were made available to GeneLab through the bio-specimen sharing program managed by the Ames Life Science Data Archive and included mouse adrenal glands quadriceps gastrocnemius tibialis anterior extensor digitorum longus soleus eye and kidney. We report here protocols for and results of these tissue extractions and thus the feasibility and value of these kinds of omics analyses. In addition to providing additional opportunities for investigation of spaceflight effects on the mouse transcriptome and proteome in new kinds of tissues our results may also be of value to program managers for the prioritization of ISS crew time for rodent research activities.",
-            "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse soleus muscle transcriptomic and epigenomic data",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-104",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse soleus muscle transcriptomic and epigenomic data"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse soleus muscle transcriptomic and epigenomic data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-5-EXT1-V2.0",
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
+            "description": "This data set contains CODMAC level 5 science data acquired by the DFMS and RTOF ROSINA sensors between 2016-01-13 and 2016-04-05 during the Extension phase 1 of the Rosetta mission at the comet 67P/CG. V2.0: Some minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-5-ext1-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-5-EXT1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-5-ext1-v2.0",
-            "description": "This data set contains CODMAC level 5 science data acquired by the DFMS and RTOF ROSINA sensors between 2016-01-13 and 2016-04-05 during the Extension phase 1 of the Rosetta mission at the comet 67P/CG. V2.0: Some minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 5\n                                      EXT1 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 5\n                                      EXT1 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F08/GPROFCLIM/2A/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_2AGPROFF08SSMI_CLIM. Version 07. GPM SSM/I on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SSMI/F08/GPROFCLIM/2A/07. https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFF08SSMI_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "1987-07-09T00:00:00Z/1991-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "precipitation",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264133957-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 7 is the current version of the data set. Older versions will no longer be available and have been superseded by the current version.\n\nThe 'CLIM'  products differ from their 'regular' counterparts (without the 'CLIM' in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the 'CLIM' output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n\nThe 2AGPROF (Goddard Profiling) algorithm retrieves consistent precipitation and related science fields from the following GMI and partner passive microwave sensors:\n+ TMI (TRMM)\n+ GMI, (GPM)\n+ SSMI (DMSP F11, F13, F14, F15); SSMIS (DMSP F16, F17, F18, F19)\n+ AMSR2 (GCOM-W1)\n+ MHS (NOAA 18,19) \n+ MHS (METOP A,B)\n+ ATMS (NPP)\n+ SAPHIR (MT1)\n\nThis provides the bulk of the 3-hour coverage achieved by GPM. For each sensor, there are nearrealtime (NRT) products, standard products, and climate products. These differ only in the amount of data that are available within 3 hours, 48 hours, and 3 months of collection, as well as the ancillary data used. The NRT product uses GANAL forecast fields. Standard products use the GANAL analysis product, while the climate product uses ECMWF reanalysis in order to allow for consistent data records with earlier missions. These earlier data may be archived separately. The main strength of the product is the large sampling provided.\n\nThe GPM radiometer algorithms are Bayesian-type algorithms. These algorithms search an apriori database of potential rain profiles and retrieve a weighted average of these entries based upon the proximity of the observed brightness temperature (Tb) to the simulated Tb corresponding to each rain profile. By using the same a-priori database of rain profiles, with appropriate simulated Tb for each constellation sensor, the Bayesian method is completely parametric and thus well suited for GPM's constellation approach. The a-priori information will be supplied by the combined algorithm supplied by GPM's core satellite as soon after launch as feasible. Databases for V0 of the algorithm had to be constructed from various sources as described in the ATBD. The solution provides a mean rain rate as well as the vertical structure of cloud and precipitation hydrometeors and their uncertainty.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_2AGPROFF08SSMI_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM SSM/I on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF08SSMI_CLIM) at GES DISC",
-            "graphic-preview-description": "GPM SSM/I on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km (GPM_2AGPROFF08SSMI_CLIM)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/2A-CLIM-BR.F13.SSMI.GPROF2017v2.19971229-S011549-E025747.014268.V05A.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF08%2FGPROFCLIM%2F2A%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF08%2FGPROFCLIM%2F2A%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/2A-CLIM-BR.F13.SSMI.GPROF2017v2.19971229-S011549-E025747.014268.V05A.PNG",
-                    "description": "GPM SSM/I on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km (GPM_2AGPROFF08SSMI_CLIM)",
                     "@type": "dcat:Distribution",
+                    "description": "GPM SSM/I on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km (GPM_2AGPROFF08SSMI_CLIM)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/2A-CLIM-BR.F13.SSMI.GPROF2017v2.19971229-S011549-E025747.014268.V05A.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFF08SSMI_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFF08SSMI_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFF08SSMI_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFF08SSMI_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFF08SSMI_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFF08SSMI_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFF08SSMI_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFF08SSMI_CLIM_07",
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
@@ -1651830,86 +1651806,112 @@
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
-                    "downloadURL": "https://www.wmo-sat.info/oscar/instruments/view/533",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://www.wmo-sat.info/oscar/instruments/view/533",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "GPM SSM/I on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km (GPM_2AGPROFF08SSMI_CLIM)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/2A-CLIM-BR.F13.SSMI.GPROF2017v2.19971229-S011549-E025747.014268.V05A.PNG",
+            "identifier": "C2264133957-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "precipitation",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F08/GPROFCLIM/2A/07",
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
+            "series-name": "GPM_2AGPROFF08SSMI_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1987-07-09T00:00:00Z/1991-12-31T23:59:59.999Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SSM/I on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF08SSMI_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FX-NAVCAM-2-CR2-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains RAW DATA of the CRUISE 2 Phase from 28 June 2005 until 16 March 2006. The primary target was comet 9P/Tempel 1. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, adding of the FITS version, clarification of calibration target, document updates and resolve other minor outstanding errata.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-x-navcam-2-cr2-v1.1",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "9p/tempel 1 (1867 g1)",
                 "checkout",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FX-NAVCAM-2-CR2-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-x-navcam-2-cr2-v1.1",
-            "description": "This dataset contains RAW DATA of the CRUISE 2 Phase from 28 June 2005 until 16 March 2006. The primary target was comet 9P/Tempel 1. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, adding of the FITS version, clarification of calibration target, document updates and resolve other minor outstanding errata.",
-            "title": "ROSETTA-ORBITER 9P/CHECK NAVCAM 2 CRUISE 2 V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 9P/CHECK NAVCAM 2 CRUISE 2 V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-I0065-2-IMGBORRELLYKPNO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The data set consists of ground-based images of comet 19P/Borrelly in the R filter taken at the Kitt Peak 2.1m for three nights from September 21-23, 2001, bracketing the Deep Space 1 encounter. Raw, as well as reduced images are included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-i0065-2-imgborrellykpno-v1.0_xus4-aduf",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "pg 0231+051",
                 "calibration",
@@ -1651917,194 +1651919,168 @@
                 "support archives",
                 "pg 2213-006"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-I0065-2-IMGBORRELLYKPNO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-i0065-2-imgborrellykpno-v1.0_xus4-aduf",
-            "description": "The data set consists of ground-based images of comet 19P/Borrelly in the R filter taken at the Kitt Peak 2.1m for three nights from September 21-23, 2001, bracketing the Deep Space 1 encounter. Raw, as well as reduced images are included.",
-            "title": "IMAGES OF COMET 19P/BORRELLY FROM 9/21-23, 2001 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IMAGES OF COMET 19P/BORRELLY FROM 9/21-23, 2001 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/DOPPLER/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Biggerstaff, Michael I, Jerry  Guynes and Gordon  Carrie.2002. CAMEX-4 SHARED MOBILE ATMOSPHERIC RESEARCH AND TEACHING RADARS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/DOPPLER/DATA301",
-            "issued": "2002-05-08",
-            "temporal": "2001-08-27T00:00:00Z/2001-09-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-20",
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
-            "identifier": "C1979101931-GHRC_DAAC",
             "description": "The CAMEX-4 Shared Mobile Atmospheric Research and Teching Radars dataset was collected by the Shared Mobile Atmospheric Research and Teaching Radar (SMART-R), which is a portable 5 cm Doppler radar. All equipment (e.g., antenna, power generator, processors, and readout computers) are truck mounted to provide maximum transportability. Originally located in the Florida Keys during CAMEX-4, the radar was moved to the Venice Florida area for landfall of TS Gabrielle on September 14, 2001.",
-            "graphic-preview-description": "N/A",
-            "title": "CAMEX-4 SHARED MOBILE ATMOSPHERIC RESEARCH AND TEACHING RADARS V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/SMART-R/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FDOPPLER%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FDOPPLER%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4gsmart",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4gsmart",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/SMART-R/browse/SR1010901210500.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/SMART-R/browse/SR1010901210500.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4gsmart/c4gsmart_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4gsmart/c4gsmart_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/SMART-R/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/SMART-R/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/SMART-R/browse/",
+            "identifier": "C1979101931-GHRC_DAAC",
+            "issued": "2002-05-08",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/DOPPLER/DATA301",
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
             "spatial": "-100.0 10.0 -60.0 50.0",
+            "temporal": "2001-08-27T00:00:00Z/2001-09-28T23:59:59Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 SHARED MOBILE ATMOSPHERIC RESEARCH AND TEACHING RADARS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR4B-CRUISE4B-V1.4",
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
-                "dark",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the CRUISE 4-2 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr4b-cruise4b-v1.4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dark",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR4B-CRUISE4B-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr4b-cruise4b-v1.4",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the CRUISE 4-2 mission phase",
-            "title": "ROSETTA-ORBITER CRUISE 4-2 OSIWAC 2 EDR data",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CRUISE 4-2 OSIWAC 2 EDR data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-06-28",
-            "temporal": "2021-06-28T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "iss",
-                "coords",
-                "ephemeris",
-                "international",
-                "coordinates",
-                "location",
-                "space",
-                "station",
-                "topo",
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
-            "identifier": "nasa-iss-data_2021-06-28_xuux-mkfk",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-06-28",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1652227,25 +1652203,63 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-06-28_xuux-mkfk",
+            "issued": "2021-06-28",
+            "keyword": [
+                "iss",
+                "coords",
+                "ephemeris",
+                "international",
+                "coordinates",
+                "location",
+                "space",
+                "station",
+                "topo",
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
+            "temporal": "2021-06-28T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-06-28"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xuvj-a3rb",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We investigated differentially regulated genes in human Jurkat T lymphocytic cells in 20s and 5min microgravity and in hypergravity and compared expression profiles to identify potential gravity-regulated genes and adaptation processes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-188",
+                    "mediaType": "text/html",
+                    "title": "Dynamic gene expression response to altered gravity in human T cells (sounding rocket flight)"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-188_xuvj-a3rb",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "rna extraction",
                 "treatment protocol",
@@ -1652256,47 +1652270,42 @@
                 "labeling",
                 "growth protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xuvj-a3rb",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-188_xuvj-a3rb",
-            "description": "We investigated differentially regulated genes in human Jurkat T lymphocytic cells in 20s and 5min microgravity and in hypergravity and compared expression profiles to identify potential gravity-regulated genes and adaptation processes.",
-            "title": "Dynamic gene expression response to altered gravity in human T cells (sounding rocket flight)",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-188",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Dynamic gene expression response to altered gravity in human T cells (sounding rocket flight)"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Dynamic gene expression response to altered gravity in human T cells (sounding rocket flight)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/trmm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://trmm.gsfc.nasa.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Kumanchik",
+                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
+            },
+            "description": "The Tropical Rainfall Measuring Mission (TRMM) is a joint mission between NASA and the Japan Aerospace Exploration Agency (JAXA) designed to monitor and study tropical rainfall.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/trmm/TRMM-vFINAL.fbx.zip",
+                    "mediaType": "application/octet-stream"
+                }
             ],
+            "identifier": "NASA-416",
+            "issued": "2018-06-25",
             "keyword": [
                 "earth science",
                 "trmm",
@@ -1652307,45 +1652316,45 @@
                 "3d model",
                 "eyes on the earth 3d"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Kumanchik",
-                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
-            },
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/trmm",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-416",
-            "description": "The Tropical Rainfall Measuring Mission (TRMM) is a joint mission between NASA and the Japan Aerospace Exploration Agency (JAXA) designed to monitor and study tropical rainfall.",
-            "title": "NASA 3D Models: TRMM",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/trmm/TRMM-vFINAL.fbx.zip",
-                    "mediaType": "application/octet-stream"
-                }
+            "references": [
+                "http://trmm.gsfc.nasa.gov/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: TRMM"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2nd_PSR_catalog/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://arxiv.org/abs/1305.4385"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "The LAT Second Pulsar Catalog is available as a .tgz (tarred and zipped) archive file. The archive includes a main catalog FITS file with the data from the paper tables, images of the light curve and spectral energy distributions (SEDs) for each pulsar, FITS files containing the data points used in those images, and the timing parameters used in the analysis. A full description of the online archive is given in Appendix B of the preprint. Upon final publication, this catalog will also be generated as a BROWSE table that will be linked to this page.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2nd_PSR_catalog/combined_2PC_SED.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-0000223__5",
+            "issued": "2018-06-25",
             "keyword": [
                 "gssc",
                 "gamma-ray",
@@ -1652363,66 +1652372,36 @@
                 "glast ssc",
                 "glast"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2nd_PSR_catalog/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000223__5",
-            "description": "The LAT Second Pulsar Catalog is available as a .tgz (tarred and zipped) archive file. The archive includes a main catalog FITS file with the data from the paper tables, images of the light curve and spectral energy distributions (SEDs) for each pulsar, FITS files containing the data points used in those images, and the timing parameters used in the analysis. A full description of the online archive is given in Appendix B of the preprint. Upon final publication, this catalog will also be generated as a BROWSE table that will be linked to this page.",
-            "title": "LAT Second Catalog of Gamma-ray Pulsars",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2nd_PSR_catalog/combined_2PC_SED.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://arxiv.org/abs/1305.4385"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT Second Catalog of Gamma-ray Pulsars"
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
-                "ask the academy",
-                "appel",
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
-            "identifier": "NASA-862__8",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1652430,856 +1652409,879 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__8",
+            "issued": "2018-06-25",
+            "keyword": [
+                "sharing",
+                "ask the academy",
+                "appel",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC4-V1.0",
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
+            "description": "The Cassini Radio Science Saturn and Ring Occultation Experiment (SROC4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 10 and June 11, 2007, during the Tour subphase of the Cassini mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc4-v1.0_xuzp-3ppj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc4-v1.0_xuzp-3ppj",
-            "description": "The Cassini Radio Science Saturn and Ring Occultation Experiment (SROC4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 10 and June 11, 2007, during the Tour subphase of the Cassini mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SROC4 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-MDIS-5-RDR-LOI-V1.0",
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
+            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes Map Projected Low- Incidence Angle Basemap RDRs (LOIs) which comprise a global map of I/F measured by the NAC or WAC filter 7 (both centered near 750 nm) during the Extended Mission at low solar incidence angles to accentuate albedo and albedo variations, photometrically normalized to a solar incidence angle (i) = 30 degrees, emission angle (e) = 0 degrees, and phase angle (g) = 30 degrees, at a spatial sampling of 256 pixels per degree. The LOI data set is a companion to the Basemap Data Record (BDR) data set, High Incidence Angle Illuminated from the East (HIE) data set, and High Incidence Angle Illuminated from the West (HIW) data set, all of which are also composed of WAC filter 7 and NAC images, except acquired at higher solar incidence angles centered at 68 to 78 degrees to highlight topography. The map is divided into 54 'tiles', each representing the NW, NE, SW, or SE quadrant of one of the 13 non-polar or one of the 2 polar quadrangles or 'Mercury charts' already defined by the USGS. Each tile also contains 5 backplanes: observation ID; BDR metric, a metric used to determine the stacking order of component images, modified for the higher incidence angle centered near 78 degrees; solar incidence angle; emission angle; and phase angle.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-mdis-5-rdr-loi-v1.0_xv2y-b9na",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mercury",
+                "messenger"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-MDIS-5-RDR-LOI-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-mdis-5-rdr-loi-v1.0_xv2y-b9na",
-            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes Map Projected Low- Incidence Angle Basemap RDRs (LOIs) which comprise a global map of I/F measured by the NAC or WAC filter 7 (both centered near 750 nm) during the Extended Mission at low solar incidence angles to accentuate albedo and albedo variations, photometrically normalized to a solar incidence angle (i) = 30 degrees, emission angle (e) = 0 degrees, and phase angle (g) = 30 degrees, at a spatial sampling of 256 pixels per degree. The LOI data set is a companion to the Basemap Data Record (BDR) data set, High Incidence Angle Illuminated from the East (HIE) data set, and High Incidence Angle Illuminated from the West (HIW) data set, all of which are also composed of WAC filter 7 and NAC images, except acquired at higher solar incidence angles centered at 68 to 78 degrees to highlight topography. The map is divided into 54 'tiles', each representing the NW, NE, SW, or SE quadrant of one of the 13 non-polar or one of the 2 polar quadrangles or 'Mercury charts' already defined by the USGS. Each tile also contains 5 backplanes: observation ID; BDR metric, a metric used to determine the stacking order of component images, modified for the higher incidence angle centered near 78 degrees; solar incidence angle; emission angle; and phase angle.",
-            "title": "MESS MDIS MAP PROJ LOW-INCIDENCE ANGLE\n                                      BASEMAP RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESS MDIS MAP PROJ LOW-INCIDENCE ANGLE\n                                      BASEMAP RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/SSF1DEGHOUR_L3.001B",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-05-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NOAA20/CERES/SSF1DEGHOUR_L3.001B. https://doi.org/10.5067/NOAA20/CERES/SSF1DEGHOUR_L3.001B.",
-            "issued": "2020-03-18",
-            "temporal": "2018-05-01T00:00:00Z/2024-10-21T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-01",
-            "keyword": [
-                "atmospheric radiation",
-                "aerosols",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "clouds",
-                "earth science"
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
-            "identifier": "C2698408408-LARC_ASDC",
             "description": "The Clouds and the Earth's Radiant Energy System (CERES) Single Scanner Footprint One Degree (SSF1deg) Hour provides regional averages of CERES Top of Atmosphere (TOA) fluxes, clouds derived from a co-located imager and aerosols on a 1-degree latitude and longitude grid. This single satellite product uses the primary CERES instrument in cross-track mode. TOA fluxes are provided for clear-sky and all-sky conditions for longwave (LW), shortwave (SW), and window wavelength bands. The incoming daily solar irradiance is from the Solar Radiation and Climate Experiment (SORCE) and Total Solar Irradiance (TSI). The cloud properties are averaged for day and night (24-hour) and day-only periods. Cloud properties are stratified into four atmospheric layers (surface-700 hPa, 700 hPa - 500 hPa, 500 hPa - 300 hPa, 300 hPa - 100 hPa) and a total of all layers. The aerosols are averaged instantaneous values from the co-located imager. CERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. The CERES instrument (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "CERES Regionally Averaged TOA Fluxes, Clouds and Aerosols Hourly NOAA-20 Edition 1B",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FSSF1DEGHOUR_L3.001B",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FSSF1DEGHOUR_L3.001B",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/",
-                    "description": "Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Project Home Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/SSF1DEGHOUR_L3.001B",
-                    "description": "DOI data set landing page for CER_SSF1deg-Hour_NOAA20P-VIIRS_Edition1B",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_SSF1deg-Hour_NOAA20P-VIIRS_Edition1B",
+                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/SSF1DEGHOUR_L3.001B",
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
-                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/SSF1degHourEd41Selection.jsp",
-                    "description": "CERES_SSF1deg_Ed4.1 Subsetting and Browsing",
                     "@type": "dcat:Distribution",
+                    "description": "CERES_SSF1deg_Ed4.1 Subsetting and Browsing",
+                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/SSF1degHourEd41Selection.jsp",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
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
-                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Signs of Change in the Tropics - New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring Mission satellite.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Signs of Change in the Tropics - New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring Mission satellite.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/DelicateBalance/balance2.php",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
-                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Aqua-CERES First Light.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Aqua-CERES First Light.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
-                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day - Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day - Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
-                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day - These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day - These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
-                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction - Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction - Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
-                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog - Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog - Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
-                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation - These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation - These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/global-maps/CERES_NETFLUX_M",
-                    "description": "NASA Earth Observatory Article: Net Radiation - The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Net Radiation - The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/global-maps/CERES_NETFLUX_M",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Observing/obs_5.php",
-                    "description": "NASA Earth Observatory Article: Space-based Observations of the Earth (Thermal radiation emitted from the Earth's surface and clouds on March 1, 2000 as seen by the Clouds and Earth's Radiant Energy System (CERES))",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Space-based Observations of the Earth (Thermal radiation emitted from the Earth's surface and clouds on March 1, 2000 as seen by the Clouds and Earth's Radiant Energy System (CERES))",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Observing/obs_5.php",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/AM1/terra_animations.php",
-                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet - Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that...",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet - Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that...",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/AM1/terra_animations.php",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
-                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight - The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight - The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
-                    "description": "NASA Earth Observatory Article: The Water Cycle - MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Water Cycle - MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2984/tropical-cloud-systems-and-ceres",
-                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day - CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day - CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/2984/tropical-cloud-systems-and-ceres",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
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
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#noaa20",
-                    "description": "CERES Overview of NOAA-20",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of NOAA-20",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#noaa20",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ssf1deg-hour.pdf",
-                    "description": "CERES Hourly Gridded TOA/Surface Fluxes and Clouds (SSF1deg-Hour) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Hourly Gridded TOA/Surface Fluxes and Clouds (SSF1deg-Hour) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ssf1deg-hour.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF_R4V1.pdf",
-                    "description": "CERES Data Products Catalog R4V110/1/2004 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R4V110/1/2004 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF_R4V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/coastal_water.pdf",
-                    "description": "Discussion of the Coastal Water Percentage Issue",
                     "@type": "dcat:Distribution",
+                    "description": "Discussion of the Coastal Water Percentage Issue",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/coastal_water.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#single-scanner-footprint-ssf",
-                    "description": "CERES Data Products Browse, Subset, and Order: Single Scanner Footprint (SSF)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Browse, Subset, and Order: Single Scanner Footprint (SSF)",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#single-scanner-footprint-ssf",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_ssf_SampleRead_R3-358.txt",
-                    "description": "Sample read software for CERES SSF Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read software for CERES SSF Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_ssf_SampleRead_R3-358.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/aqua_rev.pdf",
-                    "description": "CERES Aqua Revision_1 Table",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Aqua Revision_1 Table",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/aqua_rev.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF1deg-Hour/NOAA20-VIIRS_Edition1B/",
-                    "description": "ASDC Direct Data Download for CER_SSF1deg-Hour_NOAA20-VIIRS_Edition1B",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_SSF1deg-Hour_NOAA20-VIIRS_Edition1B",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF1deg-Hour/NOAA20-VIIRS_Edition1B/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF1deg-Hour/NOAA20-VIIRS_Edition1B/contents.html",
-                    "description": "OPeNDAP data access for CER_SSF1deg-Hour_NOAA20-VIIRS_Edition1B",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_SSF1deg-Hour_NOAA20-VIIRS_Edition1B",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF1deg-Hour/NOAA20-VIIRS_Edition1B/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C2698408408-LARC_ASDC",
+            "issued": "2020-03-18",
+            "keyword": [
+                "atmospheric radiation",
+                "aerosols",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/SSF1DEGHOUR_L3.001B",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-08-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0 -90.0 180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-05-01T00:00:00Z/2024-10-21T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Regionally Averaged TOA Fluxes, Clouds and Aerosols Hourly NOAA-20 Edition 1B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MULTI-5-67P-SHAPE-V2.0",
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
+            "description": "This data set contains a collection of shape models and their associated reference frame for the Rosetta target 67P/Churyumov-Gerasimenko 1 (1969 R1).  These were produced by Rosetta mission teams, based on OSIRIS and NAVCAM image data obtained at the comet. This is version 2.0 of this data collection.  Since the last version, the SPG_LAM_PSI SHAP5, SPG_DLR SHAP4S, and SPC_ESA MTP019 shape models have been added to this collection.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-multi-5-67p-shape-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MULTI-5-67P-SHAPE-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-multi-5-67p-shape-v2.0",
-            "description": "This data set contains a collection of shape models and their associated reference frame for the Rosetta target 67P/Churyumov-Gerasimenko 1 (1969 R1).  These were produced by Rosetta mission teams, based on OSIRIS and NAVCAM image data obtained at the comet. This is version 2.0 of this data collection.  Since the last version, the SPG_LAM_PSI SHAP5, SPG_DLR SHAP4S, and SPC_ESA MTP019 shape models have been added to this collection.",
-            "title": "SHAPE MODELS OF 67P/CHURYUMOV-GERASIMENKO V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SHAPE MODELS OF 67P/CHURYUMOV-GERASIMENKO V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1177-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-12T20:25:40.000 to 2015-11-13T01:00:33.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1177-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1177-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1177-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-12T20:25:40.000 to 2015-11-13T01:00:33.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1177 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1177 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1134-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-27T14:32:35.000 to 2015-10-27T17:17:01.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1134-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1134-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1134-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-27T14:32:35.000 to 2015-10-27T17:17:01.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1134 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1134 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D33.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand1 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D33.061. https://doi.org/10.5067/MODIS/MCD43D33.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "land surface",
-                "national geospatial data asset",
-                "earth science",
-                "ngda",
-                "surface radiative properties"
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
-            "identifier": "C2540270747-LPCLOUD",
-            "description": "The MCD43D33 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) QA ValidObs Band 1 dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. MCD43D33 provides MODIS band 1 valid observation quality information for the MCD43D products. \r\n\r\nMCD43D33 contains the valid observation quality layer representing each of the 16 days of the retrieval period for MODIS band 1.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand1 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D33 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) QA ValidObs Band 1 dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. MCD43D33 provides MODIS band 1 valid observation quality information for the MCD43D products. \r\n\r\nMCD43D33 contains the valid observation quality layer representing each of the 16 days of the retrieval period for MODIS band 1.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D33.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D33.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D33.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D33.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540270747-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540270747-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D33.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D33.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D33",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D33",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D33.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D33.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540270747-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "land surface",
+                "national geospatial data asset",
+                "earth science",
+                "ngda",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D33.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand1 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2374",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Zhang, Y., and Y. Liu. 2024. MODIS-derived Annual Vegetation Resilience, 2000-2019. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2374",
-            "issued": "2024-09-30",
-            "temporal": "2000-01-01T00:00:00Z/2019-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-02",
-            "keyword": [
-                "climate indicators",
-                "vegetation",
-                "national geospatial data asset",
-                "ngda",
-                "land surface",
-                "land surface/agriculture indicators",
-                "earth science",
-                "biosphere",
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
-            "identifier": "C3255176825-ORNL_CLOUD",
             "description": "This dataset provides estimates of vegetation resilience in the Arctic Boreal Vulnerability Experiment (ABoVE) core domain at annual time steps for 2000-2019 and at 300-m spatial resolution. Vegetation resilience is defined as the recovery rate from deviations, due to climate perturbations or disturbances, to the equilibrium state. It is quantified as the negative temporal lag-1 autocorrelation of Enhanced Vegetation Index (EVI). Using a time series of MODIS EVI, the vegetation resilience was estimated using a Bayesian dynamic linear model. The mapped vegetation resilience was derived from Terra EVI products (MOD13Q1v061) across 175 ABoVE B grid tiles over the ABoVE core domain. The estimated mean resilience, upper boundary, and lower boundary results are provided for each tile in cloud optimized GeoTIFF (COG) format.",
-            "graphic-preview-description": "The map of vegetation resilience for the year 2019 in the ABoVE core domain.",
-            "title": "MODIS-derived Annual Vegetation Resilience, 2000-2019",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Annual_Veg_Resilience_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2374",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2374",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/ABoVE_Annual_Veg_Resilience/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/ABoVE_Annual_Veg_Resilience/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/ABoVE_Annual_Veg_Resilience_2374.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/ABoVE_Annual_Veg_Resilience_2374.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Annual_Veg_Resilience.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Annual_Veg_Resilience.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2374",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2374",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/ABoVE_Annual_Veg_Resilience_2374.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/ABoVE_Annual_Veg_Resilience_2374.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_Annual_Veg_Resilience/comp/ABoVE_Annual_Veg_Resilience.pdf",
-                    "description": "MODIS-derived Annual Vegetation Resilience, 2000-2019: ABoVE_Annual_Veg_Resilience.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-derived Annual Vegetation Resilience, 2000-2019: ABoVE_Annual_Veg_Resilience.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_Annual_Veg_Resilience/comp/ABoVE_Annual_Veg_Resilience.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Annual_Veg_Resilience_Fig1.jpg",
-                    "description": "The map of vegetation resilience for the year 2019 in the ABoVE core domain.",
                     "@type": "dcat:Distribution",
+                    "description": "The map of vegetation resilience for the year 2019 in the ABoVE core domain.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Annual_Veg_Resilience_Fig1.jpg",
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
+            "graphic-preview-description": "The map of vegetation resilience for the year 2019 in the ABoVE core domain.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Annual_Veg_Resilience_Fig1.jpg",
+            "identifier": "C3255176825-ORNL_CLOUD",
+            "issued": "2024-09-30",
+            "keyword": [
+                "climate indicators",
+                "vegetation",
+                "national geospatial data asset",
+                "ngda",
+                "land surface",
+                "land surface/agriculture indicators",
+                "earth science",
+                "biosphere",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2374",
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
             "spatial": "-170.01 50.26 -98.97 76.23",
+            "temporal": "2000-01-01T00:00:00Z/2019-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS-derived Annual Vegetation Resilience, 2000-2019"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/AircraftRemoteSensing_DC8_DIAL_Data_1",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "2024-09-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/AircraftRemoteSensing_DC8_DIAL_Data_1.",
-            "issued": "2001-02-27",
-            "temporal": "2001-02-15T00:00:00Z/2001-04-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2001-04-10",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmospheric radiation",
-                "atmosphere",
-                "earth science",
-                "spectral/engineering",
-                "lidar",
-                "aerosols"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "2024-09-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/AircraftRemoteSensing_DC8_DIAL_Data_1.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2812929569-LARC_CLOUD",
             "description": "TRACE-P_AircraftRemoteSensing_DC8_DIAL_Data is the remotely sensed Differential Absorption Lidar (DIAL) data collected onboard the DC-8 aircraft during the Transport and Chemical Evolution over the Pacific (TRACE-P) suborbital campaign. Data collection for this product is complete.\r\n\r\nThe NASA TRACE-P mission was a part of NASA\u2019s Global Tropospheric Experiment (GTE) \u2013 an assemblage of missions conducted from 1983-2001 with various research goals and objectives.\u202fTRACE-P was a multi-organizational campaign with NASA, the National Center for Atmospheric Research (NCAR), and several US universities.\u202fTRACE-P deployed\u202fits payloads in the Pacific between the months of March and April 2001 with the goal of studying the air chemistry emerging\u202ffrom Asia\u202fto the western Pacific.\u202fAlong with this, TRACE-P had the objective\u202fstudying\u202fthe chemical evolution of the air as it moved away from Asia.\u202f \r\n\r\nIn order to accomplish its goals, the NASA DC-8 aircraft and NASA P-3B aircraft were deployed, each equipped with various instrumentation.\u202fTRACE-P also relied on ground sites,\u202fand\u202fsatellites\u202fto collect data. The DC-8 aircraft was equipped with 19 instruments in total\u202fwhile the P-3B\u202fboasted\u202f21 total instruments.\u202fSome instruments on the DC-8 include the Nephelometer, the GCMS, the Nitric Oxide Chemiluminescence, the Differential Absorption Lidar (DIAL), and the Dual Channel Collectors and Fluorometers, HPLC. The Nephelometer was utilized to gather data on various\u202fwavelengths\u202fincluding\u202faerosol\u202fscattering\u202f(450, 550, 700nm), aerosol absorption (565nm), equivalent BC mass, and air density ratio. The GCMS was responsible for capturing a multitude of compounds in the atmosphere, some of which include CH4, CH3CHO, CH3Br, CH3Cl, CHBr3, and C2H6O.\u202fDIAL was used for a variety of measurements, some of which include aerosol wavelength dependence (1064/587nm), IR aerosol scattering ratio (1064nm),\u202ftropopause heights and ozone columns, visible aerosol scattering ratio, composite tropospheric ozone cross-sections, and visible aerosol depolarization. Finally, the Dual Channel Collectors and Fluorometers, HPLC collected data on H2O2, CH3OOH, and CH2O in the atmosphere.\u202fThe P-3B aircraft was equipped with various instruments for TRACE-P, some of which include\u202fthe MSA/CIMS, the Non-dispersive IR Spectrometer, the PILS-Ion Chromatograph, and the\u202fCondensation particle counter and Pulse Height Analysis (PHA). The\u202fMSA/CIMS measured OH, H2SO4, MSA, and HNO3. The Non-dispersive IR Spectrometer took measurements on CO2 in the atmosphere. The PILS-Ion Chromatograph recorded measurements of compounds and elements in the atmosphere, including sodium, calcium, potassium, magnesium, chloride, NH4, NO3, and SO4. Finally, the Condensation particle counter and PHA was used to gather data on total UCN, UCN 3-8nm, and UCN 3-4nm. Along with the aircrafts, ground stations measured air quality from China along with C2H2, C2H6, CO, and HCN.\u202fFinally, satellites imagery was used to collect a multitude of data, some of the uses were to observe the history of lightning flashes,\u202fSeaWiFS\u202fcloud imagery, 8-day exposure to TOMS aerosols, and\u202fSeaWiFS\u202faerosol optical thickness. The imagery was used to best aid in planning for the aircraft deployment.",
-            "title": "TRACE-P DC-8 Remotely Sensed Differential Absorption Lidar (DIAL) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-P%2FAircraftRemoteSensing_DC8_DIAL_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-P%2FAircraftRemoteSensing_DC8_DIAL_Data_1",
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
                     "title": "The dataset's home page"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2812929569-LARC_CLOUD",
-                    "description": "Earthdata Search for TRACE-P_AircraftRemoteSensing_DC8_DIAL_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TRACE-P_AircraftRemoteSensing_DC8_DIAL_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2812929569-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/AircraftRemoteSensing_DC8_DIAL_Data_1",
-                    "description": "DOI data set landing page for TRACE-P_AircraftRemoteSensing_DC8_DIAL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TRACE-P_AircraftRemoteSensing_DC8_DIAL_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/AircraftRemoteSensing_DC8_DIAL_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2812929569-LARC_CLOUD",
+            "issued": "2001-02-27",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science",
+                "spectral/engineering",
+                "lidar",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/AircraftRemoteSensing_DC8_DIAL_Data_1",
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
             "spatial": "-180.0 13.8 180.0 45.54",
+            "temporal": "2001-02-15T00:00:00Z/2001-04-11T00:00:00Z",
             "theme": [
                 "TRACE-P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRACE-P DC-8 Remotely Sensed Differential Absorption Lidar (DIAL) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-GRNS-3-NS-CDR-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER Neutron Spectrometer (NS) calibrated data records (CDRs). The NS experiment is a neutron spectrometer designed to observe spectra of neutrons emitted from Mercury's surface in the energy range from 0.01 eV to 7 MeV. There are five NS CDR data products: raw neutron spectra, NS counter data, galactic cosmic ray (GCR) spectra, engineering data, and gamma-ray burst data. This is version 2 of this data set; version 1 has been superceded.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-grns-3-ns-cdr-v2.0_xvc7-ee63",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "venus",
@@ -1653287,504 +1653289,513 @@
                 "messenger",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-GRNS-3-NS-CDR-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-grns-3-ns-cdr-v2.0_xvc7-ee63",
-            "description": "Abstract ======== This data set consists of the MESSENGER Neutron Spectrometer (NS) calibrated data records (CDRs). The NS experiment is a neutron spectrometer designed to observe spectra of neutrons emitted from Mercury's surface in the energy range from 0.01 eV to 7 MeV. There are five NS CDR data products: raw neutron spectra, NS counter data, galactic cosmic ray (GCR) spectra, engineering data, and gamma-ray burst data. This is version 2 of this data set; version 1 has been superceded.",
-            "title": "MESSENGER E/V/H GRNS 3 NEUTRON SPECTROMETER CDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER E/V/H GRNS 3 NEUTRON SPECTROMETER CDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/418/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
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
-            "identifier": "DASHLINK_418",
             "description": "NEW RSW Fine Fully Tetrahedral Grid with Viscous Wind Tunnel wall at the root. This grid is for a node-based unstructured solver.  Note that the CGNS file is very large and is gzipped.\r\n\r\nQuad Surface Faces=         0\r\nTria Surface Faces=    553258\r\nNodes             =  23997526\r\nTotal Elements    = 142995542\r\nHex Elements      =         0\r\nPent_5 Elements   =         0\r\nPent_6 Elements   =         0\r\nTet Elements      = 142995542\r\nBL Tet Elements   = 126168161",
-            "title": "NEW RSW & Wall Fine Fully Tetrahedral Grid",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet.info",
-                    "description": "grid information",
                     "@type": "dcat:Distribution",
+                    "description": "grid information",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet.info",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_fine_tet.info"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet.mapbc",
-                    "description": "Mapbc (for FUN3D)",
                     "@type": "dcat:Distribution",
+                    "description": "Mapbc (for FUN3D)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet.mapbc",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_fine_tet.mapbc"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet.tags",
-                    "description": "tags for bc",
                     "@type": "dcat:Distribution",
+                    "description": "tags for bc",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet.tags",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_fine_tet.tags"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet14.surf",
-                    "description": "surface grid",
                     "@type": "dcat:Distribution",
+                    "description": "surface grid",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet14.surf",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_fine_tet14.surf"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_mixed.b8_2.ugrid",
-                    "description": "UGRID Format Grid file",
                     "@type": "dcat:Distribution",
+                    "description": "UGRID Format Grid file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_mixed.b8_2.ugrid",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_fine_mixed.b8.ugrid"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet.cgns.gz",
-                    "description": "CGNS Format Grid File (gzipped)",
                     "@type": "dcat:Distribution",
+                    "description": "CGNS Format Grid File (gzipped)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_fine_tet.cgns.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "rsw_fine_tet.cgns.gz"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_418",
+            "issued": "2011-07-01",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/418/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "NEW RSW & Wall Fine Fully Tetrahedral Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/26bx-en20",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Waking the Bear: Understanding Circumpolar Bear Ceremonialism, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/26bx-en20.",
-            "issued": "1995-01-01",
-            "temporal": "1995-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-31",
-            "keyword": [
-                "human dimensions",
-                "social behavior",
-                "earth science",
-                "not provided"
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
-            "identifier": "C2041709662-NSIDCV0",
             "description": "For centuries, Indigenous peoples across Eurasia and North American have maintained harmonious relations with bears with whom they share the world, honoring this relationship through elaborate ceremonies. At present, this website describes the bear ceremonies of Siberian people, the Mansi and the Khanty, through a rich narrative illustrated by photos, videos, and audio recordings. The content is in both English and Russian.\n\nBetween 2021 to 2022, the research project aims to reach out to Native American and First Nations communities in the United States and Canada, whose concern has been indicated by the unique Grizzly Bear Treaty of 2016, initiated by the Piikani First Nation of Canada and signed by representatives of more than a hundred tribes. The hope is that the website might provide the focus for a future, multidisciplinary Indigenous-led forum on sharing the world with bears and other-than-human persons.",
-            "title": "Waking the Bear: Understanding Circumpolar Bear Ceremonialism, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F26bx-en20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F26bx-en20",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eloka-arctic.org/bears",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://eloka-arctic.org/bears",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/26bx-en20",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/26bx-en20",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/26bx-en20",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/26bx-en20",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C2041709662-NSIDCV0",
+            "issued": "1995-01-01",
+            "keyword": [
+                "human dimensions",
+                "social behavior",
+                "earth science",
+                "not provided"
             ],
+            "landingPage": "https://doi.org/10.7265/26bx-en20",
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
+            "temporal": "1995-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Waking the Bear: Understanding Circumpolar Bear Ceremonialism, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0579-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-13T11:00:30.000 to 2015-02-13T13:49:02.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0579-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0579-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0579-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-13T11:00:30.000 to 2015-02-13T13:49:02.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0579 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0579 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHTMI-3UR71",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Remote Sensing Systems (REMSS). 2017-11-30. GHRSST Level 3U Global Subskin Sea Surface Temperature from TMI onboard TRMM satellite. Version 7.1a. TMI 25km gridded SST data set. Santa Rosa, CA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Remote Sensing Systems. https://doi.org/10.5067/GHTMI-3UR71. http://www.remss.com. Remote Sensing Systems (REMSS), Remote Sensing Systems, 2017-11-30, GHRSST Level 3U Global Subskin Sea Surface Temperature from TMI onboard  TRMM satellite, http://www.remss.com.",
-            "issued": "2017-09-19",
-            "temporal": "1997-12-08T00:00:00Z/2015-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-09-19",
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
-            "identifier": "C2617176783-POCLOUD",
-            "description": "The Tropical Rainfall Measuring Mission (TRMM) Microwave Imager (TMI) is a well calibrated passive microwave radiometer, similar to the Special Sensor Microwave Imager (SSM/I), that contains lower frequency channels required for sea surface temperature  (SST) retrievals. The TRMM is part of the NASA's mission to planet Earth, and is a joint venture between NASA and the Japan Aerospace Exploration Agency (JAXA) to measure precipitation, water vapor, sea surface temperature (SST) and surface wind in the global tropical regions and was launched in 27 November 1997 from the Tanegashima Space Center in Tanegashima, Japan. The TRMM satellite travels west to east in a 402 km altitude semi-equatorial processing orbit that results in day-to-day changes in the observation time of any given earth location between 38S and 38N.  Remote Sensing Systems (REMSS) has produced a Version-7.1a TMI SST dataset for the Group for High Resolution Sea Surface Temperature (GHRSST) by applying an algorithm to the 10.7 GHz channel through a removal of surface roughness effects. In contrast to infrared SST observations, microwave retrievals can be measured through clouds, which are nearly transparent at 10.7 GHz. Microwave retrievals are also insensitive to water vapor and aerosols.  The algorithm for retrieving SSTs from radiometer data is described in \"AMSR Ocean Algorithm.\"",
-            "release-place": "Santa Rosa, CA, USA",
-            "series-name": "GHRSST Level 3U Global Subskin Sea Surface Temperature from TMI onboard TRMM satellite",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Remote Sensing Systems (REMSS)",
-            "title": "GHRSST Level 3U Global Subskin Sea Surface Temperature from TMI onboard  TRMM satellite",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TMI-REMSS-L3U-v7.1a.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Tropical Rainfall Measuring Mission (TRMM) Microwave Imager (TMI) is a well calibrated passive microwave radiometer, similar to the Special Sensor Microwave Imager (SSM/I), that contains lower frequency channels required for sea surface temperature  (SST) retrievals. The TRMM is part of the NASA's mission to planet Earth, and is a joint venture between NASA and the Japan Aerospace Exploration Agency (JAXA) to measure precipitation, water vapor, sea surface temperature (SST) and surface wind in the global tropical regions and was launched in 27 November 1997 from the Tanegashima Space Center in Tanegashima, Japan. The TRMM satellite travels west to east in a 402 km altitude semi-equatorial processing orbit that results in day-to-day changes in the observation time of any given earth location between 38S and 38N.  Remote Sensing Systems (REMSS) has produced a Version-7.1a TMI SST dataset for the Group for High Resolution Sea Surface Temperature (GHRSST) by applying an algorithm to the 10.7 GHz channel through a removal of surface roughness effects. In contrast to infrared SST observations, microwave retrievals can be measured through clouds, which are nearly transparent at 10.7 GHz. Microwave retrievals are also insensitive to water vapor and aerosols.  The algorithm for retrieving SSTs from radiometer data is described in \"AMSR Ocean Algorithm.\"",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHTMI-3UR71",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHTMI-3UR71",
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
-                    "downloadURL": "http://www.remss.com/missions/tmi",
-                    "description": "Samples, Interface Control Document describing file contents, background ppt and other info",
                     "@type": "dcat:Distribution",
+                    "description": "Samples, Interface Control Document describing file contents, background ppt and other info",
+                    "downloadURL": "http://www.remss.com/missions/tmi",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TMI-REMSS-L3U-v7.1a.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TMI-REMSS-L3U-v7.1a.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617176783-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617176783-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617176783-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617176783-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/common/open/sw/generic_nc_readers/idl/generic_nc_readers_idl.tgz",
-                    "description": "Generic Interactive Data Language readers for netCDF",
                     "@type": "dcat:Distribution",
+                    "description": "Generic Interactive Data Language readers for netCDF",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/common/open/sw/generic_nc_readers/idl/generic_nc_readers_idl.tgz",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/common/open/sw/generic_nc_readers/matlab/generic_nc_readers_matlab.tgz",
-                    "description": "Generic MATLAB readers for netCDF",
                     "@type": "dcat:Distribution",
+                    "description": "Generic MATLAB readers for netCDF",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/common/open/sw/generic_nc_readers/matlab/generic_nc_readers_matlab.tgz",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/common/open/sw/generic_nc_readers/python/generic_nc_readers_python.tgz",
-                    "description": "Generic Python readers for netCDF",
                     "@type": "dcat:Distribution",
+                    "description": "Generic Python readers for netCDF",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/common/open/sw/generic_nc_readers/python/generic_nc_readers_python.tgz",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/common/open/sw/generic_nc_readers/R/generic_nc_readers_R.tgz",
-                    "description": "Generic R readers for netCDF",
                     "@type": "dcat:Distribution",
+                    "description": "Generic R readers for netCDF",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/common/open/sw/generic_nc_readers/R/generic_nc_readers_R.tgz",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TMI-REMSS-L3U-v7.1a.jpg",
+            "identifier": "C2617176783-POCLOUD",
+            "issued": "2017-09-19",
+            "keyword": [
+                "earth science",
+                "ocean temperature",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHTMI-3UR71",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-09-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Santa Rosa, CA, USA",
+            "series-name": "GHRSST Level 3U Global Subskin Sea Surface Temperature from TMI onboard TRMM satellite",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1997-12-08T00:00:00Z/2015-01-01T23:59:59.999Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 3U Global Subskin Sea Surface Temperature from TMI onboard  TRMM satellite"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1229-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-02T12:29:05.000 to 2015-12-02T16:22:11.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1229-v1.0_xvju-bvcv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1229-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1229-v1.0_xvju-bvcv",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-02T12:29:05.000 to 2015-12-02T16:22:11.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1229 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1229 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_PSCMASK-STANDARD-V2-00",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_PSCMASK-STANDARD-V2-00.",
-            "issued": "2020-06-17",
-            "temporal": "2006-06-12T00:00:00Z/2021-04-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-17",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Pitts",
                 "hasEmail": "mailto:michael.c.pitts@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2212314288-LARC_ASDC",
             "description": "The Version 2 (V2) CALIPSO Lidar Level 2 Polar Stratospheric Clouds (PSC) data product ensemble describes the spatial distribution, optical properties, and composition of PSC layers observed by the CALIPSO lidar (CALIOP). The product contains profiles of PSC presence, composition, optical properties, and meteorological information on a uniform 5-km horizontal x 180-m vertical grid along CALIPSO orbit tracks. Aura Microwave Limb Sounder (MLS) measurements of the primary PSC condensable vapors HNO3 and H2O and a number of parameters from the Aura MLS V2 Derived Meteorological Products (DMPs) are also included in the V2 PSC data product ensemble.",
-            "title": "CALIPSO Lidar Level 2 Polar Stratospheric Clouds presents, composition, and optical properties, V2-00",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_PSCMASK-STANDARD-V2-00",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_PSCMASK-STANDARD-V2-00",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_pscmask_v2-00.php",
-                    "description": "Detailed Data Quality Summary for the CALIPSO Lidar Level 2 Polar Stratospheric Cloud (PSC) Version 2.00 Data Product",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed Data Quality Summary for the CALIPSO Lidar Level 2 Polar Stratospheric Cloud (PSC) Version 2.00 Data Product",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_pscmask_v2-00.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_summaries/psc/cal_lid_l2_pscmask_v2-00_desc.php",
-                    "description": "Data Product Descriptions for the CALIPSO Lidar Level 2 Polar Stratospheric Cloud (PSC) Version 2.00 Data Product",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Descriptions for the CALIPSO Lidar Level 2 Polar Stratospheric Cloud (PSC) Version 2.00 Data Product",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_summaries/psc/cal_lid_l2_pscmask_v2-00_desc.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_PSCMASK-STANDARD-V2-00",
-                    "description": "DOI data set landing page for CAL_LID_L2_PSCMASK-STANDARD-V2-00_V2-00",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L2_PSCMASK-STANDARD-V2-00_V2-00",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_PSCMASK-STANDARD-V2-00",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x94.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.94",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.94",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x94.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2212314288-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L2_PSCMask-Standard-V2-00_V2-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data).",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L2_PSCMask-Standard-V2-00_V2-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data).",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2212314288-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_PSCMask-Standard-V2-00/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L2_PSCMask-Standard-V2-00_V2-00",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L2_PSCMask-Standard-V2-00_V2-00",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_PSCMask-Standard-V2-00/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_PSCMask-Standard-V2-00/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L2_PSCMask-Standard-V2-00_V2-00",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L2_PSCMask-Standard-V2-00_V2-00",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_PSCMask-Standard-V2-00/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2212314288-LARC_ASDC",
+            "issued": "2020-06-17",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_PSCMASK-STANDARD-V2-00",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2006-06-12T00:00:00Z/2021-04-01T23:59:59.999Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Lidar Level 2 Polar Stratospheric Clouds presents, composition, and optical properties, V2-00"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xvr6-53es",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_vfm-valstage1-v3-02_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000179",
             "issued": "2018-06-25",
-            "temporal": "2011-11-01/2013-02-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "eos",
                 "radiation",
@@ -1653794,1355 +1653805,1319 @@
                 "aerosol",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xvr6-53es",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000179",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 Vertical Feature Mask Data V3-02",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_vfm-valstage1-v3-02_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2011-11-01/2013-02-28",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 Vertical Feature Mask Data V3-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SDRON-ATOM0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Saildrone. 2020-07-30. Saildrone ATOMIC field campaign surface measurements. Version 1.0. Saildrone Arctic ATOMIC Field Campaign Products. Saildrone Inc. 1050 W Tower Ave, Alameda, CA 94501. Archived by National Aeronautics and Space Administration, U.S. Government, Saildrone Inc. https://doi.org/10.5067/SDRON-ATOM0. http://podaac.jpl.nasa.gov/saildrone. Saildrone, Saildrone Inc, 2020-07-30, Saildrone field campaign surface and ADCP measurements for the Atlantic Tradewind Ocean-Atmosphere Mesoscale Interaction Campaign (ATOMIC) project, http://podaac.jpl.nasa.gov/saildrone.",
-            "issued": "2020-07-23",
-            "temporal": "2020-01-17T00:00:00Z/2020-03-02T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-07-23",
-            "keyword": [
-                "atmospheric temperature",
-                "ocean optics",
-                "ocean circulation",
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
-                "ocean chemistry",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric pressure",
-                "atmosphere"
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
-            "identifier": "C2491772162-POCLOUD",
-            "description": "Saildrone is a wind and solar powered unmanned surface vehicle (USV) capable of long distance deployments lasting up to 12 months and providing high quality, near real-time, multivariate surface ocean and atmospheric observations while transiting at typical speeds of 3-5 knots. The drone is autonomous in that it may be guided remotely from land while being completely wind driven. The saildrone ATOMIC (Atlantic Tradewind Ocean-Atmosphere Mesoscale Interaction Campaign) campaign involved the deployment of a fleet of saildrones, jointly funded by NASA and NOAA, in the Atlantic waters offshore of Barbados over a 45 day period from 17 January to 2 March 2020. The goal was to understand the Ocean-Atmosphere interaction particularly over the mesoscale ocean eddies in that region. The saildrones were equipped with a suite of instruments that included a CTD, IR pyrometer, fluorometer, dissolved oxygen sensor, anemometer, barometer, and Acoustic Doppler Current Profiler (ADCP).  Additionally, four temperature data loggers were positioned vertically along hull to provide further information on thermal variability near the ocean surface. This Saildrone ATOMIC dataset is comprised of two data files for each of the three NASA-funded saildrones deployed, one for the surface observations and one for the ADCP measuements.  The surface data files contain saildrone platform telemetry and near-surface observational data (air temperature, sea surface skin and bulk temperatures, salinity, oxygen and chlorophyll-a concentrations, barometric pressure, wind speed and direction) spanning the entire cruise at 1 minute temporal resolution. The ADCP files for each saildrone are at 5 minute resolution for the duration of the deployments. All data files are in netCDF format and CF/ACDD compliant consistent with the NOAA/NCEI specification.",
-            "release-place": "Saildrone Inc. 1050 W Tower Ave, Alameda, CA 94501",
-            "series-name": "Saildrone ATOMIC field campaign surface measurements",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Saildrone",
-            "title": "Saildrone field campaign surface and ADCP measurements for the Atlantic Tradewind Ocean-Atmosphere Mesoscale Interaction Campaign (ATOMIC) project",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_ATOMIC.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Saildrone is a wind and solar powered unmanned surface vehicle (USV) capable of long distance deployments lasting up to 12 months and providing high quality, near real-time, multivariate surface ocean and atmospheric observations while transiting at typical speeds of 3-5 knots. The drone is autonomous in that it may be guided remotely from land while being completely wind driven. The saildrone ATOMIC (Atlantic Tradewind Ocean-Atmosphere Mesoscale Interaction Campaign) campaign involved the deployment of a fleet of saildrones, jointly funded by NASA and NOAA, in the Atlantic waters offshore of Barbados over a 45 day period from 17 January to 2 March 2020. The goal was to understand the Ocean-Atmosphere interaction particularly over the mesoscale ocean eddies in that region. The saildrones were equipped with a suite of instruments that included a CTD, IR pyrometer, fluorometer, dissolved oxygen sensor, anemometer, barometer, and Acoustic Doppler Current Profiler (ADCP).  Additionally, four temperature data loggers were positioned vertically along hull to provide further information on thermal variability near the ocean surface. This Saildrone ATOMIC dataset is comprised of two data files for each of the three NASA-funded saildrones deployed, one for the surface observations and one for the ADCP measuements.  The surface data files contain saildrone platform telemetry and near-surface observational data (air temperature, sea surface skin and bulk temperatures, salinity, oxygen and chlorophyll-a concentrations, barometric pressure, wind speed and direction) spanning the entire cruise at 1 minute temporal resolution. The ADCP files for each saildrone are at 5 minute resolution for the duration of the deployments. All data files are in netCDF format and CF/ACDD compliant consistent with the NOAA/NCEI specification.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSDRON-ATOM0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSDRON-ATOM0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_ATOMIC.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_ATOMIC.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772162-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772162-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772162-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772162-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_ATOMIC.jpg",
+            "identifier": "C2491772162-POCLOUD",
+            "issued": "2020-07-23",
+            "keyword": [
+                "atmospheric temperature",
+                "ocean optics",
+                "ocean circulation",
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "ocean chemistry",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric pressure",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/SDRON-ATOM0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-07-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Saildrone Inc. 1050 W Tower Ave, Alameda, CA 94501",
+            "series-name": "Saildrone ATOMIC field campaign surface measurements",
             "spatial": "-59.4 7.4 -48.6 12.1",
+            "temporal": "2020-01-17T00:00:00Z/2020-03-02T23:59:59Z",
             "theme": [
                 "ATOMIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Saildrone field campaign surface and ADCP measurements for the Atlantic Tradewind Ocean-Atmosphere Mesoscale Interaction Campaign (ATOMIC) project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/137",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Briggs, J. 1994. Vegetation Species Reference (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/137",
-            "issued": "2024-05-06",
-            "temporal": "1989-10-31T00:00:00Z/1989-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
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
-            "identifier": "C2980719966-ORNL_CLOUD",
             "description": "LTER species names, codes, types, and other reference information",
-            "graphic-preview-description": "Browse Image",
-            "title": "Vegetation Species Reference (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F137",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F137",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_veg_ref/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_veg_ref/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Vegetation_Species_Reference.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Vegetation_Species_Reference.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/137",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/137",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_ref/comp/Vegetation_Species_Reference.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_ref/comp/Vegetation_Species_Reference.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_ref/comp/veg_ref.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_ref/comp/veg_ref.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_ref/comp/veg_ref.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_ref/comp/veg_ref.tdf",
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
+            "identifier": "C2980719966-ORNL_CLOUD",
+            "issued": "2024-05-06",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/137",
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
             "spatial": "-97.0 39.0 -95.0 40.0",
+            "temporal": "1989-10-31T00:00:00Z/1989-10-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Vegetation Species Reference (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/892/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-01-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Abhinav Saxena",
                 "hasEmail": "mailto:abhinav.saxena@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_892",
             "description": "Increasing demand for improved reliability and survivability of mission-critical systems is driving the\r\ndevelopment of health monitoring and Automated Contingency Management (ACM) systems. An ACM system is expected to adapt autonomously to fault conditions with the goal of still\r\nachieving mission objectives by allowing some degradation in system performance within permissible limits. ACM performance depends on supporting technologies like sensors\r\nand anomaly detection, diagnostic/prognostic and reasoning algorithms. This paper presents the development of a generic prototype test bench software framework for developing and\r\nvalidating ACM systems for advanced propulsion systems called the Propulsion ACM (PACM) Test Bench. The\r\narchitecture has been implemented for a Monopropellant Propulsion System (MPS) to demonstrate the validity of the approach. A Simulink model of the MPS has been developed\r\nalong with a fault injection module. It has been shown that the ACM system is capable of mitigating the failures by searching for an optimal strategy. Furthermore, few relevant\r\nexperiments have been presented to show proof of concepts.",
-            "title": "Automated Contingency Management for Propulsion Systems",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/download",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/ACM_ECC2007.pdf",
-                    "description": "ACM_ECC2007.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACM_ECC2007.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/ACM_ECC2007.pdf",
+                    "mediaType": "application/download",
                     "title": "ACM_ECC2007.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_892",
+            "issued": "2014-01-11",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/892/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Automated Contingency Management for Propulsion Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PRA-4-SUMM-BROWSE-48SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset consists of edited browse data derived from an original dataset obtained from the Voyager 2 Planetary Radio Astronomy (PRA) instrument in the vicinity of Neptune. Data are provided for 70 instrument channels covering the range from 1.2 kHz to 1326 kHz in uniform 19.2 kHz steps, each 1 kHz wide. Data are included for the period 1989:0:0:0 through 1989:23:59:59. In order to produce this dataset from the original raw PRA data, several steps have been taken:",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pra-4-summ-browse-48sec-v1.0_xvwf-dhvh",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PRA-4-SUMM-BROWSE-48SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pra-4-summ-browse-48sec-v1.0_xvwf-dhvh",
-            "description": "This dataset consists of edited browse data derived from an original dataset obtained from the Voyager 2 Planetary Radio Astronomy (PRA) instrument in the vicinity of Neptune. Data are provided for 70 instrument channels covering the range from 1.2 kHz to 1326 kHz in uniform 19.2 kHz steps, each 1 kHz wide. Data are included for the period 1989:0:0:0 through 1989:23:59:59. In order to produce this dataset from the original raw PRA data, several steps have been taken:",
-            "title": "VG2 NEP PRA RESAMPLED SUMMARY BROWSE 48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 NEP PRA RESAMPLED SUMMARY BROWSE 48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S%2FSW-CAPS-5-DDR-ION-MOMENTS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of all of the ion moments data generated from the Cassini Plasma Spectrometer (CAPS) ion mass spectrometer singles or time-of-flight uncalibrated data. The data set contains the derived ion moments data as follows: Ion Moments (ION_MOMT) Density, Temperature, Average Flow Speed, Average Flow Velocity Ions included are H+, H2+, and W+ (water group ions: O+, OH+, H2O+) The uncalibrated data were acquired in a mix of CAPS operating modes beginning with the first instrument checkout in January 1999 and containing throughout the Cassini Tour and through the end of prime mission.  The data set covers the time period from 1999-004T03:07:47 UT until end of prime mission (July 2008).  In addition, it will cover data received during extended missions.  Sampling rates were variable and depended upon the downlink capabilities and other activities on-board. For times when CAPS is not producing data due to being turned off or due to communication issues, the data set will not contain data. Additionally, there will be no data during times when the calculations are not possible.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-sw-caps-5-ddr-ion-moments-v1.0_xvx2-33h6",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S%2FSW-CAPS-5-DDR-ION-MOMENTS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-sw-caps-5-ddr-ion-moments-v1.0_xvx2-33h6",
-            "description": "This data set consists of all of the ion moments data generated from the Cassini Plasma Spectrometer (CAPS) ion mass spectrometer singles or time-of-flight uncalibrated data. The data set contains the derived ion moments data as follows: Ion Moments (ION_MOMT) Density, Temperature, Average Flow Speed, Average Flow Velocity Ions included are H+, H2+, and W+ (water group ions: O+, OH+, H2O+) The uncalibrated data were acquired in a mix of CAPS operating modes beginning with the first instrument checkout in January 1999 and containing throughout the Cassini Tour and through the end of prime mission.  The data set covers the time period from 1999-004T03:07:47 UT until end of prime mission (July 2008).  In addition, it will cover data received during extended missions.  Sampling rates were variable and depended upon the downlink capabilities and other activities on-board. For times when CAPS is not producing data due to being turned off or due to communication issues, the data set will not contain data. Additionally, there will be no data during times when the calculations are not possible.",
-            "title": "CASSINI ORBITER SAT/SW CAPS DERIVED ION MOMENTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER SAT/SW CAPS DERIVED ION MOMENTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/394",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lerdau, M. 1998. BOREAS TGB-08 Starch Concentration Data over the SSA-OBS and the SSA-OJP. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/394",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-24T00:00:00Z/1994-09-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
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
-            "identifier": "C2808132136-ORNL_CLOUD",
             "description": "Contains starch concentration data collected by TGB-08 from the SSA-OBS and SSA-OJP BOREAS sites in 1994.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-08 Starch Concentration Data over the SSA-OBS and the SSA-OJP",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F394",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F394",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb8scds/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb8scds/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB08_Starch_Conc.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB08_Starch_Conc.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/394",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/394",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb8scds/comp/TGB08_Starch_Conc.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb8scds/comp/TGB08_Starch_Conc.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb8scds/comp/TGB08_Starch_Conc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb8scds/comp/TGB08_Starch_Conc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb8scds/comp/TGB08_Starch_Conc.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb8scds/comp/TGB08_Starch_Conc.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb8scds/comp/tgb8scds.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb8scds/comp/tgb8scds.def",
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
+            "identifier": "C2808132136-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/394",
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
             "spatial": "-105.12 53.92 -104.69 53.99",
+            "temporal": "1994-05-24T00:00:00Z/1994-09-19T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-08 Starch Concentration Data over the SSA-OBS and the SSA-OJP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO2CLD.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Glynn Hulley. 2019-06-20. ECO2CLD.001. ECOSTRESS Cloud Mask Daily L2 Global 70 m V001. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO2CLD.001. https://doi.org/10.5067/ECOSTRESS/ECO2CLD.001. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2019-06-20",
-            "temporal": "2018-07-09T00:00:00Z/2024-09-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Glynn Hulley",
                 "hasEmail": "mailto:glynn.hulley@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1534730833-LPDAAC_ECS",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO2CLD Version 1 data product provides a cloud mask that can be used to determine cloud cover for the ECO1BRAD, ECO2LSTE, ECO3ETPTJPL, ECO4ESIPTJPL, and ECO4WUE data products. The ECOSTRESS Level 2 cloud product is derived using the five calibrated thermal bands in a multispectral cloud-conservative thresholding approach. The details of the algorithm are provided in the Algorithm Theoretical Basis Document (ATBD). The corresponding ECO1BGEO (https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001) data product is required to georeference the ECO2CLD data product.\r\n\r\nThe ECO2CLD Version 1 data product contains a single cloud mask layer. Information on how to interpret the bit fields in the cloud mask is provided in section 3.1 of the User Guide.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "ECO2CLD.001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Glynn Hulley",
-            "title": "ECOSTRESS Cloud Mask Daily L2 Global 70m V001",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.10.29/ECOSTRESS_L2_CLOUD_13108_017_20201028T073252_0601_01.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO2CLD Version 1 data product provides a cloud mask that can be used to determine cloud cover for the ECO1BRAD, ECO2LSTE, ECO3ETPTJPL, ECO4ESIPTJPL, and ECO4WUE data products. The ECOSTRESS Level 2 cloud product is derived using the five calibrated thermal bands in a multispectral cloud-conservative thresholding approach. The details of the algorithm are provided in the Algorithm Theoretical Basis Document (ATBD). The corresponding ECO1BGEO (https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001) data product is required to georeference the ECO2CLD data product.\r\n\r\nThe ECO2CLD Version 1 data product contains a single cloud mask layer. Information on how to interpret the bit fields in the cloud mask is provided in section 3.1 of the User Guide.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO2CLD.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO2CLD.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534730833-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534730833-LPDAAC_ECS",
+                    "mediaType": "application/xhdf5",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO2CLD.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO2CLD.001/",
+                    "mediaType": "application/xhdf5",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO2CLD.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO2CLD.001",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/423/ECO2_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/423/ECO2_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/296/ECO2_Cloud_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/296/ECO2_Cloud_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ecostress.jpl.nasa.gov/science",
-                    "description": "The ECOSTRESS website provides detailed information on the mission, instrument, products, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The ECOSTRESS website provides detailed information on the mission, instrument, products, etc.",
+                    "downloadURL": "https://ecostress.jpl.nasa.gov/science",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
-                    "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1573/Quick_Guide_for_Accessing_ECOSTRESS_Swath_Data_in_NASA_Earthdata_Search.pdf",
-                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1573/Quick_Guide_for_Accessing_ECOSTRESS_Swath_Data_in_NASA_Earthdata_Search.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.10.29/ECOSTRESS_L2_CLOUD_13108_017_20201028T073252_0601_01.1.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.10.29/ECOSTRESS_L2_CLOUD_13108_017_20201028T073252_0601_01.1.jpg",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOB/ECOSTRESS/ECO2CLD.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOB/ECOSTRESS/ECO2CLD.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.10.29/ECOSTRESS_L2_CLOUD_13108_017_20201028T073252_0601_01.1.jpg",
+            "identifier": "C1534730833-LPDAAC_ECS",
+            "issued": "2019-06-20",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO2CLD.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-09-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "ECO2CLD.001",
             "spatial": "-180.0 -54.0 180.0 54.0",
+            "temporal": "2018-07-09T00:00:00Z/2024-09-09T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Cloud Mask Daily L2 Global 70m V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0026-V1.0",
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
+            "description": "This is a Solar Conjunction measurement covering the time 2006-04-04T00:21:03.500 to 2006-04-04T03:37:13.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0026-v1.0_xvzc-8mjz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "sun",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0026-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0026-v1.0_xvzc-8mjz",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-04-04T00:21:03.500 to 2006-04-04T03:37:13.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0026 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0026 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1925",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wofsy, S.C., S. Afshar, H.M. Allen, E.C. Apel, E.C. Asher, B. Barletta, J. Bent, H. Bian, B.C. Biggs, D.R. Blake, N. Blake, I. Bourgeois, C.A. Brock, W.H. Brune, J.W. Budney, T.P. Bui, A. Butler, P. Campuzano-Jost, C.S. Chang, M. Chin, R. Commane, G. Correa, J.D. Crounse, P. D. Cullis, B.C. Daube, D.A. Day, J.M. Dean-Day, J.E. Dibb, J.P. DiGangi, G.S. Diskin, M. Dollner, J.W. Elkins, F. Erdesz, A.M. Fiore, C.M. Flynn, K.D. Froyd, D.W. Gesler, S.R. Hall, T.F. Hanisco, R.A. Hannun, A.J. Hills, E.J. Hintsa, A. Hoffman, R.S. Hornbrook, L.G. Huey, S. Hughes, J.L. Jimenez, B.J. Johnson, J.M. Katich, R.F. Keeling, M.J. Kim, A. Kupc, L.R. Lait, K. McKain, R.J. Mclaughlin, S. Meinardi, D.O. Miller, S.A. Montzka, F.L. Moore, E.J. Morgan, D.M. Murphy, L.T. Murray, B.A. Nault, J.A. Neuman, P.A. Newman, J.M. Nicely, X. Pan, W. Paplawsky, J. Peischl, M.J. Prather, D.J. Price, E.A. Ray, J.M. Reeves, M. Richardson, A.W. Rollins, K.H. Rosenlof, T.B. Ryerson, E. Scheuer, G.P. Schill, J.C. Schroder, J.P. Schwarz, J.M. St.Clair, S.D. Steenrod, B.B. Stephens, S.A. Strode, C. Sweeney, D. Tanner, A.P. Teng, A.B. Thames, C.R. Thompson, K. Ullmann, P.R. Veres, N.L. Wagner, A. Watt, R. Weber, B.B. Weinzierl, P.O. Wennberg, C.J. Williamson, J.C. Wilson, G.M. Wolfe, C.T. Woods, L.H. Zeng, and N. Vieznor. 2021. ATom: Merged Atmospheric Chemistry, Trace Gases, and Aerosols, Version 2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1925",
-            "issued": "2024-05-02",
-            "temporal": "2016-07-29T14:33:10Z/2018-05-21T23:38:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-03",
-            "keyword": [
-                "aerosols",
-                "air quality",
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C2367011141-ORNL_CLOUD",
             "description": "This dataset provides information on greenhouse gases and human-produced air pollution, including atmospheric concentrations of carbon dioxide (CO2), methane (CH4), tropospheric ozone (O3), and black carbon (BC) aerosols, collected during airborne campaigns conducted by NASA's Atmospheric Tomography (ATom) mission. This dataset includes merged data from all instruments plus additional data such as numbered profiles and distance flown. Merged data products have been created for seven different aggregation intervals (1 second, 10 seconds, and 5 instrument-specific intervals). In the case of data obtained over longer time intervals (e.g., flask data), the merge files provide (weighted) averages to match the sampling intervals. This comprehensive dataset will be used to improve the representation of chemically reactive gases and short-lived climate forcers in global models of atmospheric chemistry and climate.",
-            "graphic-preview-description": "Figure 1: Generalized overview of ATom flights. During each of the four campaigns, ATom flights originated from California, flew south over the Pacific Ocean, then north to the western Arctic, southwest to New Zealand, east to Chile and the Atlantic Ocean, north to Greenland, and returned to California across North America. During flights, the aircraft continuously profiled the atmosphere from 0.2 to 12 km altitude.",
-            "title": "ATom: Merged Atmospheric Chemistry, Trace Gases, and Aerosols, Version 2",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_merge_V2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1925",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1925",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/atom/ATom_merge_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/atom/ATom_merge_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_merge_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_merge_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1925",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1925",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_merge_V2/comp/ALLNAMES.txt",
-                    "description": "ATom: Merged Atmospheric Chemistry, Trace Gases, and Aerosols, Version 2: ALLNAMES.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Merged Atmospheric Chemistry, Trace Gases, and Aerosols, Version 2: ALLNAMES.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_merge_V2/comp/ALLNAMES.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_merge_V2/comp/ATom_merge_V2.pdf",
-                    "description": "ATom: Merged Atmospheric Chemistry, Trace Gases, and Aerosols, Version 2: ATom_merge_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Merged Atmospheric Chemistry, Trace Gases, and Aerosols, Version 2: ATom_merge_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_merge_V2/comp/ATom_merge_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_merge_V2/comp/ATom_merging_Rcode_20210804.pdf",
-                    "description": "ATom: Merged Atmospheric Chemistry, Trace Gases, and Aerosols, Version 2: ATom_merging_Rcode_20210804.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Merged Atmospheric Chemistry, Trace Gases, and Aerosols, Version 2: ATom_merging_Rcode_20210804.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_merge_V2/comp/ATom_merging_Rcode_20210804.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_merge_V2_Fig1.png",
-                    "description": "Figure 1: Generalized overview of ATom flights. During each of the four campaigns, ATom flights originated from California, flew south over the Pacific Ocean, then north to the western Arctic, southwest to New Zealand, east to Chile and the Atlantic Ocean, north to Greenland, and returned to California across North America. During flights, the aircraft continuously profiled the atmosphere from 0.2 to 12 km altitude.",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: Generalized overview of ATom flights. During each of the four campaigns, ATom flights originated from California, flew south over the Pacific Ocean, then north to the western Arctic, southwest to New Zealand, east to Chile and the Atlantic Ocean, north to Greenland, and returned to California across North America. During flights, the aircraft continuously profiled the atmosphere from 0.2 to 12 km altitude.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_merge_V2_Fig1.png",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1925/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1925/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Figure 1: Generalized overview of ATom flights. During each of the four campaigns, ATom flights originated from California, flew south over the Pacific Ocean, then north to the western Arctic, southwest to New Zealand, east to Chile and the Atlantic Ocean, north to Greenland, and returned to California across North America. During flights, the aircraft continuously profiled the atmosphere from 0.2 to 12 km altitude.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_merge_V2_Fig1.png",
+            "identifier": "C2367011141-ORNL_CLOUD",
+            "issued": "2024-05-02",
+            "keyword": [
+                "aerosols",
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "environmental impacts",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1925",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -86.18 180.0 82.94",
+            "temporal": "2016-07-29T14:33:10Z/2018-05-21T23:38:00Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: Merged Atmospheric Chemistry, Trace Gases, and Aerosols, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3PMDE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Monthly Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3PMDE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Monthly Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "salinity/density"
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
-            "identifier": "C2491756340-POCLOUD",
-            "description": "Aquarius Level 3 sea surface spiciness standard mapped image data contains gridded 1 degree spatial resolution spice data averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Monthly, Descending sea surface spiciness product for version 5.0 of the Aquarius data set. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Monthly Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Monthly Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SPICINESS_SMID_MONTHLY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface spiciness standard mapped image data contains gridded 1 degree spatial resolution spice data averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Monthly, Descending sea surface spiciness product for version 5.0 of the Aquarius data set. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3PMDE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3PMDE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SPICINESS_SMID_MONTHLY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SPICINESS_SMID_MONTHLY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756340-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756340-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756340-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756340-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SPICINESS_SMID_MONTHLY_V5.jpg",
+            "identifier": "C2491756340-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3PMDE",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Monthly Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Monthly Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-EAR3-EARTHSWINGBY3-V1.0",
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
+            "description": "Payload Checkout 10 (PC10) was an active checkout where a target independent opportunity to perform interactive operations and to request spacecraft pointing was given to all Rosetta payload teams. All Rosetta payload took part in this scenario The Active Payload Checkout 10 ran for 12 consecutive days starting on the 21th September 2009 until the 2th October 2009. This is the allocated time of the active PC10 scenario that preceded it PC10 consists of two phases. The 1st phase is a passive test (GD01) similar to the previous Passive Payload Checkouts the 2nd phase is an active test; GD02 is dealt with GIADA/VIRTIS interference test, in GD03 we upload on-board of new Context File settings performing and checking new procedures, GD_INT is dealt with GIADA/ROSINA interference test. The passive test (GD01), which includes standard procedures and full functional verification, was executed by switching on Main and Redundant I/Fs in sequence and executing similar procedures for the two cases. GD02, GD03 and GD_INT were executed only on Main I/F. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-ear3-earthswingby3-v1.0_xw3i-dbax",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-EAR3-EARTHSWINGBY3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-ear3-earthswingby3-v1.0_xw3i-dbax",
-            "description": "Payload Checkout 10 (PC10) was an active checkout where a target independent opportunity to perform interactive operations and to request spacecraft pointing was given to all Rosetta payload teams. All Rosetta payload took part in this scenario The Active Payload Checkout 10 ran for 12 consecutive days starting on the 21th September 2009 until the 2th October 2009. This is the allocated time of the active PC10 scenario that preceded it PC10 consists of two phases. The 1st phase is a passive test (GD01) similar to the previous Passive Payload Checkouts the 2nd phase is an active test; GD02 is dealt with GIADA/VIRTIS interference test, in GD03 we upload on-board of new Context File settings performing and checking new procedures, GD_INT is dealt with GIADA/ROSINA interference test. The passive test (GD01), which includes standard procedures and full functional verification, was executed by switching on Main and Redundant I/Fs in sequence and executing similar procedures for the two cases. GD02, GD03 and GD_INT were executed only on Main I/F. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
-            "title": "ROSETTA-ORBITER CHECK GIADA 2 EAR3 EARTHSWINGBY3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK GIADA 2 EAR3 EARTHSWINGBY3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/99/",
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
-            "identifier": "DASHLINK_99",
             "description": "AISRP Presentations from CIDU/AISRP 2009.",
-            "title": "AISRP Presentations",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AISRP_PI_Meeting_Li_2009_pub.pdf",
-                    "description": "Friday: Ron Li, Integration of Orbital, Descent and Ground Imagery for Topographic Capability Analysis in Mars Landed Missions",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Ron Li, Integration of Orbital, Descent and Ground Imagery for Topographic Capability Analysis in Mars Landed Missions",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AISRP_PI_Meeting_Li_2009_pub.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AISRP_PI_Meeting_Li_2009_pub.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/JGardner-AISR09.pdf",
-                    "description": "Friday: Jeffrey Gardner, Astronomy in the Cloud",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Jeffrey Gardner, Astronomy in the Cloud",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/JGardner-AISR09.pdf",
+                    "mediaType": "application/pdf",
                     "title": "JGardner-AISR09.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/4_AISR_Schafer.pdf",
-                    "description": "Wednesday: Chad Schafer, Stochastic Models for Nonstandard, High-Dimensional Data",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: Chad Schafer, Stochastic Models for Nonstandard, High-Dimensional Data",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/4_AISR_Schafer.pdf",
+                    "mediaType": "application/pdf",
                     "title": "4_AISR_Schafer.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/3_20091014_AISR_Dolan.pdf",
-                    "description": "Wednesday: John DolanAn Analytical Tool for Robot Mission Reliability Prediction",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: John DolanAn Analytical Tool for Robot Mission Reliability Prediction",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/3_20091014_AISR_Dolan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "3_20091014_AISR_Dolan.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/5_AISRP_2009_Ding.pdf",
-                    "description": "Wednesday: Wei Ding, Automatic Detection of Sub-Kilometer craters in High Res Planetary Images",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: Wei Ding, Automatic Detection of Sub-Kilometer craters in High Res Planetary Images",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/5_AISRP_2009_Ding.pdf",
+                    "mediaType": "application/pdf",
                     "title": "5_AISRP_2009_Ding.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/2.00_aisrp_pi_scargle.pdf",
-                    "description": "Wednesday: Jeff Scargle, Novel Methods for the Analysis of Photon-Limited Data ",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: Jeff Scargle, Novel Methods for the Analysis of Photon-Limited Data ",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/2.00_aisrp_pi_scargle.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2.00_aisrp_pi_scargle.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/2.15_Djorgovski.pdf",
-                    "description": "Wednesday: SG Djorgovski, Automated, Dynamical Event Classification and Response in a Robotic Sensor Network",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: SG Djorgovski, Automated, Dynamical Event Classification and Response in a Robotic Sensor Network",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/2.15_Djorgovski.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2.15_Djorgovski.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/3.45_Tilton_AISR_CIDU_2009.pdf",
-                    "description": "Wednesday: James Tilton, Object-Based Image Analysis Utilizing Image Segmentation Hierarchies",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: James Tilton, Object-Based Image Analysis Utilizing Image Segmentation Hierarchies",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/3.45_Tilton_AISR_CIDU_2009.pdf",
+                    "mediaType": "application/pdf",
                     "title": "3.45_Tilton_AISR_CIDU_2009.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/4.15Szapudi-AISR.pdf",
-                    "description": "Wednesday: Istvan Szapudi, Algorithms for Higher Order Spatial Statistics",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: Istvan Szapudi, Algorithms for Higher Order Spatial Statistics",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/4.15Szapudi-AISR.pdf",
+                    "mediaType": "application/pdf",
                     "title": "4.15Szapudi-AISR.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/4.45_weinberg_aisr.pdf",
-                    "description": "Wednesday: Martin Weinberg, UMass Bayesian Inference Engine",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: Martin Weinberg, UMass Bayesian Inference Engine",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/4.45_weinberg_aisr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "4.45_weinberg_aisr.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/connolly.pdf",
-                    "description": "Wednesday: Andrew Connolly, Streaming the Sky: Data Interfaces with Gadgets",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: Andrew Connolly, Streaming the Sky: Data Interfaces with Gadgets",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/connolly.pdf",
+                    "mediaType": "application/pdf",
                     "title": "connolly.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Talukder-AISR_PIMeeting_Oct2009-7.pdf",
-                    "description": "Wednesday: Ashit Talukder, GLYDER: Global Cyclone Detection and Tracking from Remote Satellite Data",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: Ashit Talukder, GLYDER: Global Cyclone Detection and Tracking from Remote Satellite Data",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Talukder-AISR_PIMeeting_Oct2009-7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Talukder-AISR_PIMeeting_Oct2009-7.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AISR09InvstgWrkshpLo.Final.pdf",
-                    "description": "Thursday: Martin Lo, Science Discovery with MTool on Massive High Dimensional Data",
                     "@type": "dcat:Distribution",
+                    "description": "Thursday: Martin Lo, Science Discovery with MTool on Massive High Dimensional Data",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AISR09InvstgWrkshpLo.Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AISR09InvstgWrkshpLo.Final.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AISRP_moratto.pdf",
-                    "description": "Thursday: Zachary Moratto, Automated Digital Terrain Model Generation from HiRISE & LROC Imagery",
                     "@type": "dcat:Distribution",
+                    "description": "Thursday: Zachary Moratto, Automated Digital Terrain Model Generation from HiRISE & LROC Imagery",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AISRP_moratto.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AISRP_moratto.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/LANG-AISR_2009.pdf",
-                    "description": "Thursday: Ken Lang, NASA\u2019S COSMOS",
                     "@type": "dcat:Distribution",
+                    "description": "Thursday: Ken Lang, NASA\u2019S COSMOS",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/LANG-AISR_2009.pdf",
+                    "mediaType": "application/pdf",
                     "title": "LANG-AISR_2009.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Kargupta-Slides.pdf",
-                    "description": "Thursday: Hillol Kargupta, Distributed and Peer-to-Peer Data Mining for Scalable Analysis of Data from Virtual Observatories",
                     "@type": "dcat:Distribution",
+                    "description": "Thursday: Hillol Kargupta, Distributed and Peer-to-Peer Data Mining for Scalable Analysis of Data from Virtual Observatories",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Kargupta-Slides.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Kargupta-Slides.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/wagstaff-oct14-PI-mtg.pdf",
-                    "description": "Wednesday: Kiri Wagstaff, Detecting Transient Surface Features Via Dynamic Landmarking",
                     "@type": "dcat:Distribution",
+                    "description": "Wednesday: Kiri Wagstaff, Detecting Transient Surface Features Via Dynamic Landmarking",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/wagstaff-oct14-PI-mtg.pdf",
+                    "mediaType": "application/pdf",
                     "title": "wagstaff-oct14-PI-mtg.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Wiliams_NASA_AISR_Talk_Oct_09.pdf",
-                    "description": "Friday: Brian Williams, Demonstration of Safe Human / Robot Coordination on the Athlete Lunar Rover",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Brian Williams, Demonstration of Safe Human / Robot Coordination on the Athlete Lunar Rover",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Wiliams_NASA_AISR_Talk_Oct_09.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Wiliams_NASA_AISR_Talk_Oct_09.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Quinnaisr09.pdf",
-                    "description": "Thursday: Thomas Quinn, Visualizing Terascale Datasets with Impostors",
                     "@type": "dcat:Distribution",
+                    "description": "Thursday: Thomas Quinn, Visualizing Terascale Datasets with Impostors",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Quinnaisr09.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Quinnaisr09.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/4.30_AISRP-2009-ptak.pdf",
-                    "description": "Friday: Andrew Ptak, On-the-fly and Grid Analysis of Astronomical Images",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Andrew Ptak, On-the-fly and Grid Analysis of Astronomical Images",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/4.30_AISRP-2009-ptak.pdf",
+                    "mediaType": "application/pdf",
                     "title": "4.30_AISRP-2009-ptak.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Belbruno_AISR2009Conf.pdf",
-                    "description": "Friday: Edward Belbruno, Controlling Sensitive Trajectories and Transfer Between Planetary Systems",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Edward Belbruno, Controlling Sensitive Trajectories and Transfer Between Planetary Systems",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Belbruno_AISR2009Conf.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Belbruno_AISR2009Conf.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/talk.pdf",
-                    "description": "Friday: Gabor Toth Adding New Physics and Numerics into the BATSRUS MHD Code",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Gabor Toth Adding New Physics and Numerics into the BATSRUS MHD Code",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/talk.pdf",
+                    "mediaType": "application/pdf",
                     "title": "talk.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/mighell2009OCT16.pdf",
-                    "description": "Friday: Kenneith Mighell, Parallel-Processing Astrophysical Image-Analysis Tools",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Kenneith Mighell, Parallel-Processing Astrophysical Image-Analysis Tools",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/mighell2009OCT16.pdf",
+                    "mediaType": "application/pdf",
                     "title": "mighell2009OCT16.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jewell_aisr_2009_fv.pdf",
-                    "description": "Friday: Jeffrey Jewell, Parallel-Processing Astrophysical Image-Analysis Tools",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Jeffrey Jewell, Parallel-Processing Astrophysical Image-Analysis Tools",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jewell_aisr_2009_fv.pdf",
+                    "mediaType": "application/pdf",
                     "title": "jewell_aisr_2009_fv.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Morris_aisrp_pi_2009.pdf",
-                    "description": "Friday: Robin Morris, How Well Do You Know That?",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Robin Morris, How Well Do You Know That?",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Morris_aisrp_pi_2009.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Morris_aisrp_pi_2009.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/20091016_AISR_BURL.pdf",
-                    "description": "Friday: Michael Burl, Directed Exploration of Complex Systems",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Michael Burl, Directed Exploration of Complex Systems",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/20091016_AISR_BURL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "20091016_AISR_BURL.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AISRP_-_Final.pdf",
-                    "description": "Friday: Mario Juric, GPU\u2010based Tools for Computational Astrophysics: N\u2010Body Integrators for Planetary Systems",
                     "@type": "dcat:Distribution",
+                    "description": "Friday: Mario Juric, GPU\u2010based Tools for Computational Astrophysics: N\u2010Body Integrators for Planetary Systems",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AISRP_-_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AISRP_-_Final.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/08.30_SSF_10_15_09.pdf",
-                    "description": "Thrusday: Stephen Fong, An Integrated Systems for Creating and Evaluating Biological Models",
                     "@type": "dcat:Distribution",
+                    "description": "Thrusday: Stephen Fong, An Integrated Systems for Creating and Evaluating Biological Models",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/08.30_SSF_10_15_09.pdf",
+                    "mediaType": "application/pdf",
                     "title": "08.30_SSF_10_15_09.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/aisrp09.pdf",
-                    "description": "Thursday: Joel Allred, Solar Magnetogram Synthesis: A Vital Data Analysis Component of A Space Weather Prediction Infrastructure",
                     "@type": "dcat:Distribution",
+                    "description": "Thursday: Joel Allred, Solar Magnetogram Synthesis: A Vital Data Analysis Component of A Space Weather Prediction Infrastructure",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/aisrp09.pdf",
+                    "mediaType": "application/pdf",
                     "title": "aisrp09.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_99",
+            "issued": "2010-09-10",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/99/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "AISRP Presentations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/DK01TW3NB06J",
             "citation": "William J. Blackwell, MIT Lincoln Laboratory. 2024-06-01. TROPICS05BRTTL1B. Version 0.2. TROPICS05\u00a0L1B Orbital Geolocated Native-Resolution Brightness Temperatures V0.2. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/DK01TW3NB06J. https://disc.gsfc.nasa.gov/datacollection/TROPICS05BRTTL1B_0.2.html. Digital Science Data.",
-            "issued": "2024-05-08",
-            "temporal": "2021-07-19T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "references": [
-                "https://doi.org/10.1002/qj.3290"
-            ],
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "microwave"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kristan Morgan",
                 "hasEmail": "mailto:kristan.l.morgan@nasa.gov"
             },
+            "creator": "William J. Blackwell, MIT Lincoln Laboratory",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2985145021-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The \"Time-Resolved Observations of Precipitation structure and storm Intensity with a Constellation of Smallsats\" (TROPICS) mission has a goal of providing nearly all-weather observations of three-dimensional temperature and humidity, as well as cloud ice and precipitation horizontal structure, at high temporal resolution to conduct high-value science investigations of tropical cyclones. The mission comprises a constellation of five identical Space Vehicles (SVs) conforming to the 3U form factor and hosting a passive microwave spectrometer payload.\n\nEach SV hosts an identical high-performance spectrometer named the TROPICS Millimeter-wave Sounder (TMS) that will provide temperature profiles using seven channels near the 118.75-GHz oxygen absorption line, water vapor profiles using three channels near the 183-GHz water vapor absorption line, imagery in a single channel near 90 GHz for precipitation measurements (when combined with higher resolution water vapor channels), and a single channel near 205 GHz that is more sensitive to cloud-sized ice particles.\n\nEach TROPICS netCDF file contains a granule of data with 81 spots and approximately 2880 scans, where a granule is defined as an orbit's worth of data.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TROPICS05BRTTL1B",
-            "creator": "William J. Blackwell, MIT Lincoln Laboratory",
-            "title": "TROPICS05\u00a0L1B Orbital Geolocated Native-Resolution Brightness Temperatures V0.2",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TROPICS03BRTTL1B_02.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDK01TW3NB06J",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDK01TW3NB06J",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1655152,457 +1655127,458 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS05BRTTL1B_0.2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS05BRTTL1B_0.2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TROPICS_L1B/TROPICS05BRTTL1B.0.2/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TROPICS_L1B/TROPICS05BRTTL1B.0.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TROPICS_L1B/TROPICS05BRTTL1B.0.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TROPICS_L1B/TROPICS05BRTTL1B.0.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICS05BRTTL1B_0.2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICS05BRTTL1B_0.2",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS-05_TROPICS-07_L1_Provisional_Release_README_Aug2024.pdf",
-                    "description": "TROPICS L1 README",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS L1 README",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS-05_TROPICS-07_L1_Provisional_Release_README_Aug2024.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TROPICS03BRTTL1B_02.png",
+            "identifier": "C2985145021-GES_DISC",
+            "issued": "2024-05-08",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/DK01TW3NB06J",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1002/qj.3290"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "TROPICS05BRTTL1B",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-07-19T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "TROPICS (EVI-3)",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPICS05\u00a0L1B Orbital Geolocated Native-Resolution Brightness Temperatures V0.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-3-ENGRDR-V1.0",
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
+            "description": "Calibrated or converted engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-3-engrdr-v1.0_xw6d-gazb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-3-ENGRDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-3-engrdr-v1.0_xw6d-gazb",
-            "description": "Calibrated or converted engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
-            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 3 ENGRDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 3 ENGRDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-LET-3-RDR-FLUX-32SEC-V1.0",
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
+            "description": "This data set contains COSPIN Low Energy Telescope (LET) particle flux rates from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-16.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-let-3-rdr-flux-32sec-v1.0_xw9q-u6ij",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-LET-3-RDR-FLUX-32SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-let-3-rdr-flux-32sec-v1.0_xw9q-u6ij",
-            "description": "This data set contains COSPIN Low Energy Telescope (LET) particle flux rates from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-16.",
-            "title": "ULY JUP COSPIN LOW ENERGY TELESCOPE 32\n                                        SEC PARTICLE FLUX",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULY JUP COSPIN LOW ENERGY TELESCOPE 32\n                                        SEC PARTICLE FLUX"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUBORBITAL/PISTON2018-2019-ONR-NOAA/AUTONOMOUS/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/SUBORBITAL/PISTON2018-2019-ONR-NOAA/AUTONOMOUS/DATA001.",
-            "issued": "2018-08-23",
-            "temporal": "2018-08-23T00:00:00Z/2018-11-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-04",
-            "keyword": [
-                "ocean pressure",
-                "oceans",
-                "earth science",
-                "ocean temperature",
-                "salinity/density",
-                "ocean circulation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elizabeth Thompson",
                 "hasEmail": "mailto:elizabeth.thompson@noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2566392214-LARC_ASDC",
             "description": "PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019 is the Propagation of Intra-Seasonal Tropical Oscillations (PISTON) 2018-2019 autonomous platform ocean data product. This product is the result of a joint effort that involved NASA as well as the Office of Naval Research (ONR), and National Oceanic and Atmospheric Administration (NOAA). Data was collected collection for this product using Sounding Oceanographic Lagrangian Observer II (SOLO-II) instruments. Data collection is complete.\r\n\r\nThe PISTON field campaign, sponsored by the Office of Naval Research (ONR) and the National Oceanic and Atmospheric Administration (NOAA), was designed to gain understanding and enhance the prediction capability of multi-scale tropical atmospheric convection and air-sea interaction in this region. PISTON targeted the Boreal Summer Intraseasonal Oscillation (BSISO), which defines the northward and eastward movement of convection associated with equatorial waves, the MJO, tropical cyclones, and the Maritime Continent monsoon during northern-hemispheric (boreal) summertime. PISTON completed three total shipboard cruises, deployed eight drifting ocean profiling floats and two full-depth ocean moorings, collaborated with a Japanese research vessel collecting similar data, and also made use of soundings from nearby islands. These activities took place in the Philippine Sea, which is in the tropical northwestern Pacific Ocean north of Palau, between August 2018 - September 2019, with each dataset spanning a slightly different amount of time. There were two US research vessels involved in PISTON: R/V Thomas G. Thompson in Aug-Sept and Sept-Oct 2018 and R/V Sally Ride in Sept 2019. The first 2018 cruise coincided collaborative activities with R/V Mirai. The 2019 cruise coincided with the NASA CAMP2Ex airborne field experiment (Clouds, Aerosol and Monsoon Processes-Philippines Experiment, please see more info below). The two specialized moorings were deployed north of Palau and collected data from August 2018 - Oct 2019 to document a time series of ocean characteristics beneath typhoons and other tropical weather disturbances. Toward the same goal, eight profiling ocean floats were also deployed ahead of typhoons in 2018. \r\n\r\nFor characterization of clouds and precipitation, the PISTON shipboard instrument payload included a scanning C-band dual-polarization Doppler radar (SEA-POL), a vertically-pointing Doppler W-band radar, and multiple vertically- and horizontally-scanning lidars. Rawinsondes were launched from the ships for atmospheric profiling. Additional radiosonde and precipitation radar data were collected from R/V Mirai via an international collaboration. Regular soundings were also archived from islands neighboring the Philippines and the Philippine Sea: Dongsha Island, Taiping Island, Yap, Palau, and Guam. Additional atmospheric sampling from the PISTON R/V Thompson 2018 and Sally Ride 2019 cruises included an electric field meter and disdrometer in 2018, and all-sky camera images in 2019. To document near-surface meteorological conditions, air-sea fluxes, and upper-ocean variability including ocean vertical profiles on these cruises, instruments were deployed on and towed from the ship. Additional profiles of ocean acoustics and oceanic chemistry were not archived but are available upon request by James N. Moum, Oregon State University, jim.moum@oregonstate.edu. A forecast team analyzed and predicted conditions of the weather and ocean throughout the PISTON experiment, which were not archived but are available upon request for future modeling and observational analysis studies (contacts: Sue Chen, US Naval Research Lab Monterey, sue.chen@nrlmry.navy.mil and Michael M. Bell, Colorado State University, mmbell@colostate.edu). \r\n\r\nThere are five total DOIs related to PISTON, separated by ship (and therefore year) as well as other platforms/locations that span multiple years:\r\nhttps://doi.org/10.5067/SUBORBITAL/PISTON2018-ONR-NOAA/RVTHOMPSON/DATA001",
-            "title": "PISTON 2018-2019 Autonomous Platform Ocean Datasets",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUBORBITAL%2FPISTON2018-2019-ONR-NOAA%2FAUTONOMOUS%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUBORBITAL%2FPISTON2018-2019-ONR-NOAA%2FAUTONOMOUS%2FDATA001",
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
-                    "downloadURL": "https://onrpiston.colostate.edu/index.html",
-                    "description": "Office of Naval Research (ONR) home page for PISTON",
                     "@type": "dcat:Distribution",
+                    "description": "Office of Naval Research (ONR) home page for PISTON",
+                    "downloadURL": "https://onrpiston.colostate.edu/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://onrpiston.colostate.edu/docs/PISTON_1page_21Mar2017_FINAL.pdf",
-                    "description": "PISTON Campaign Summary",
                     "@type": "dcat:Distribution",
+                    "description": "PISTON Campaign Summary",
+                    "downloadURL": "https://onrpiston.colostate.edu/docs/PISTON_1page_21Mar2017_FINAL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://onrpiston.colostate.edu/docs/science_plan.pdf",
-                    "description": "PISTON Science Plan",
                     "@type": "dcat:Distribution",
+                    "description": "PISTON Science Plan",
+                    "downloadURL": "https://onrpiston.colostate.edu/docs/science_plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/CAMP2EX/2018",
-                    "description": "CAMP2Ex Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "CAMP2Ex Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/CAMP2EX/2018",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2566392214-LARC_ASDC",
-                    "description": "Earthdata Search Client for PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2566392214-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SUBORBITAL/PISTON2018-2019-ONR-NOAA/AUTONOMOUS/DATA001",
-                    "description": "DOI for PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1",
+                    "downloadURL": "https://doi.org/10.5067/SUBORBITAL/PISTON2018-2019-ONR-NOAA/AUTONOMOUS/DATA001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1/",
-                    "description": "ASDC Direct Data Download for PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CAMP2Ex/PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1/contents.html",
-                    "description": "OPeNDAP data access for PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CAMP2Ex/PISTON-ONR-NOAA-Autonomous-Uncrewed_2018-2019_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2566392214-LARC_ASDC",
+            "issued": "2018-08-23",
+            "keyword": [
+                "ocean pressure",
+                "oceans",
+                "earth science",
+                "ocean temperature",
+                "salinity/density",
+                "ocean circulation"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUBORBITAL/PISTON2018-2019-ONR-NOAA/AUTONOMOUS/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>3.9491 123.2587 3.9491 134.7463 16.6721 134.7463 16.6721 123.2587 3.9491 123.2587</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-08-23T00:00:00Z/2018-11-09T23:59:59.999Z",
             "theme": [
                 "CAMP2Ex",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PISTON 2018-2019 Autonomous Platform Ocean Datasets"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/374/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-05-16",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
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
-            "identifier": "DASHLINK_374",
             "description": "This dataset is the fully tetrahdral fine mesh for the RSW configuration.",
-            "title": "RSW Fully Tet Fine Mesh",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine_tet.surf",
-                    "description": "surface file",
                     "@type": "dcat:Distribution",
+                    "description": "surface file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine_tet.surf",
+                    "mediaType": "application/octet-stream",
                     "title": "rswf_fine_tet.surf"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_medium_tet_2.tags",
-                    "description": "tags file",
                     "@type": "dcat:Distribution",
+                    "description": "tags file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_medium_tet_2.tags",
+                    "mediaType": "application/octet-stream",
                     "title": "rswf_medium_tet.tags"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine_tet.b8.ugrid",
-                    "description": "ugrid file",
                     "@type": "dcat:Distribution",
+                    "description": "ugrid file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine_tet.b8.ugrid",
+                    "mediaType": "application/octet-stream",
                     "title": "rswf_fine_tet.b8.ugrid"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_374",
+            "issued": "2011-05-16",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/374/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RSW Fully Tet Fine Mesh"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-EXT2-67P-V3.0",
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
+            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA EXTENSION 2 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes data sets with a lower version number. The updates include a new calibration algorithm and modified documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-ext2-67p-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-EXT2-67P-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-ext2-67p-v3.0",
-            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA EXTENSION 2 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes data sets with a lower version number. The updates include a new calibration algorithm and modified documentation.",
-            "title": "ROSETTA-ORBITER 67P MIRO 3 EXT2 V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIRO 3 EXT2 V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NOAA20/3A-MONTH/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFNOAA20ATMS. Version 07. GPM ATMS on NOAA-20 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/ATMS/NOAA20/3A-MONTH/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFNOAA20ATMS_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2017-12-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHRISTIAN KUMMEROW",
                 "hasEmail": "mailto:kummerow@atmos.colostate.edu"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264134864-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. \n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_3GPROFNOAA20ATMS",
-            "creator": "GPM Science Team",
-            "title": "GPM ATMS on NOAA-20 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA20ATMS) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from GPM ATMS on NOAA-20 GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFNOAA20ATMS)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFNOAA20ATMS_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNOAA20%2F3A-MONTH%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNOAA20%2F3A-MONTH%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFNOAA20ATMS_07.png",
-                    "description": "Surface Precipitation from GPM ATMS on NOAA-20 GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFNOAA20ATMS)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from GPM ATMS on NOAA-20 GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFNOAA20ATMS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFNOAA20ATMS_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFNOAA20ATMS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFNOAA20ATMS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFNOAA20ATMS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFNOAA20ATMS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFNOAA20ATMS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFNOAA20ATMS.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFNOAA20ATMS_07.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFNOAA20ATMS_07.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFNOAA20ATMS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFNOAA20ATMS_07",
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
@@ -1655612,398 +1655588,424 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
-                    "description": "Instrument Description from NOAA",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from NOAA",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
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
+            "graphic-preview-description": "Surface Precipitation from GPM ATMS on NOAA-20 GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFNOAA20ATMS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFNOAA20ATMS_07.png",
+            "identifier": "C2264134864-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NOAA20/3A-MONTH/07",
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
+            "series-name": "GPM_3GPROFNOAA20ATMS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-12-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM ATMS on NOAA-20 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA20ATMS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3SRAS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending 28-Day Running Mean Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3SRAS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending 28-Day Running Mean Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "salinity/density",
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
-            "identifier": "C2491756487-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the 28-Day\nrunning mean, Ascending sea surface salinity product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending 28-Day Running Mean Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending 28-Day Running Mean Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMIA_28DAY-RUNNINGMEAN_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the 28-Day\nrunning mean, Ascending sea surface salinity product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3SRAS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3SRAS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMIA_28DAY-RUNNINGMEAN_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMIA_28DAY-RUNNINGMEAN_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756487-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756487-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756487-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756487-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMIA_28DAY-RUNNINGMEAN_V5.jpg",
+            "identifier": "C2491756487-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "salinity/density",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3SRAS",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending 28-Day Running Mean Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending 28-Day Running Mean Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Huemmrich, K.F., and P.K. Campbell. 2022. Tundra Plant Leaf-level Spectral Reflectance and Chlorophyll Fluorescence, 2019-2021. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2005",
-            "issued": "2022-04-30",
-            "temporal": "2019-07-19T00:00:00Z/2021-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
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
-            "identifier": "C2262495547-ORNL_CLOUD",
             "description": "This dataset provides leaf-level visible-near infrared spectral reflectance, chlorophyll fluorescence spectra, species, plant functional type (PFT), and chlorophyll content of common high latitude plant samples collected near Fairbanks, Utqiagvik, and Toolik, Alaska, U.S., during the summers of 2019, 2020, and 2021. A FluoWat leaf clip was used to measure leaf-level visible-near infrared spectral reflectance and chlorophyll fluorescence spectra. Fluorescence yield (Fyield) was calculated as the ratio of the emitted fluorescence divided by the absorbed radiation for the wavelengths from 400 nm up to the wavelength of the cut off for the FluoWat low pass filter (either 650 or 700 nm). Chlorophyll content of samples was measured using a CCM-300 Chlorophyll Content. The data are provided in comma-separated values (.csv) format.",
-            "graphic-preview-description": "Schematic of FluoWat leaf clip operation for measuring leaf reflectance, transmittance, and upward and downward fluorescence (SIF). The leaf is placed in the clip and illuminated through the open port (A). Reflected and transmitted radiance are measured by attaching a fiber optic cable from the spectrometer to the top or bottom of the clip. To measure fluorescence spectra a low pass filter is placed across the illumination port (B). Two filters are applied in sequence, they block incident wavelengths above 650 nm and 700 nm, therefore any radiance measured in the longer wavelengths can come only from fluorescence. Source: Van Wittenberghe et al. (2015)",
-            "title": "Tundra Plant Leaf-level Spectral Reflectance and Chlorophyll Fluorescence, 2019-2021",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Tundra_Leaf_Spectra_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Tundra_Leaf_Spectra/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Tundra_Leaf_Spectra/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Tundra_Leaf_Spectra.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Tundra_Leaf_Spectra.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2005",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2005",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Tundra_Leaf_Spectra/comp/Tundra_Leaf_Spectra.pdf",
-                    "description": "Tundra Plant Leaf-level Spectral Reflectance and Chlorophyll Fluorescence, 2019-2021: Tundra_Leaf_Spectra.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Tundra Plant Leaf-level Spectral Reflectance and Chlorophyll Fluorescence, 2019-2021: Tundra_Leaf_Spectra.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Tundra_Leaf_Spectra/comp/Tundra_Leaf_Spectra.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Tundra_Leaf_Spectra_Fig1.png",
-                    "description": "Schematic of FluoWat leaf clip operation for measuring leaf reflectance, transmittance, and upward and downward fluorescence (SIF). The leaf is placed in the clip and illuminated through the open port (A). Reflected and transmitted radiance are measured by attaching a fiber optic cable from the spectrometer to the top or bottom of the clip. To measure fluorescence spectra a low pass filter is placed across the illumination port (B). Two filters are applied in sequence, they block incident wavelengths above 650 nm and 700 nm, therefore any radiance measured in the longer wavelengths can come only from fluorescence. Source: Van Wittenberghe et al. (2015)",
                     "@type": "dcat:Distribution",
+                    "description": "Schematic of FluoWat leaf clip operation for measuring leaf reflectance, transmittance, and upward and downward fluorescence (SIF). The leaf is placed in the clip and illuminated through the open port (A). Reflected and transmitted radiance are measured by attaching a fiber optic cable from the spectrometer to the top or bottom of the clip. To measure fluorescence spectra a low pass filter is placed across the illumination port (B). Two filters are applied in sequence, they block incident wavelengths above 650 nm and 700 nm, therefore any radiance measured in the longer wavelengths can come only from fluorescence. Source: Van Wittenberghe et al. (2015)",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Tundra_Leaf_Spectra_Fig1.png",
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
+            "graphic-preview-description": "Schematic of FluoWat leaf clip operation for measuring leaf reflectance, transmittance, and upward and downward fluorescence (SIF). The leaf is placed in the clip and illuminated through the open port (A). Reflected and transmitted radiance are measured by attaching a fiber optic cable from the spectrometer to the top or bottom of the clip. To measure fluorescence spectra a low pass filter is placed across the illumination port (B). Two filters are applied in sequence, they block incident wavelengths above 650 nm and 700 nm, therefore any radiance measured in the longer wavelengths can come only from fluorescence. Source: Van Wittenberghe et al. (2015)",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Tundra_Leaf_Spectra_Fig1.png",
+            "identifier": "C2262495547-ORNL_CLOUD",
+            "issued": "2022-04-30",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2005",
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
             "spatial": "-156.6 64.83 -147.81 71.31",
+            "temporal": "2019-07-19T00:00:00Z/2021-09-30T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tundra Plant Leaf-level Spectral Reflectance and Chlorophyll Fluorescence, 2019-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-X-HRIV-3-EPOXI-EXOPLANETS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set set contains calibrated images of eight known transiting extrasolar planetary systems (hot Jupiters) acquired by the Deep Impact High Resolution Visible CCD during the EPOCh phase of the EPOXI mission. From 22 January through 31 August 2008 the HRIV CCD collected over 172,000 usable, photometric-quality visible light images of these transiting planet systems: HAT-P-4, HAT-P-7, GJ 436, TrES-2, TrES-3, XO-2, XO-3, and WASP-3. Time series of continuous 50-second integrations were used with the clear filter (#6) to observe each system for about three weeks, typically covering five or more transits as well as secondary eclipses. An exception was XO-3 which was only observed briefly due to the spacecraft entering safe mode. The transiting planet systems were observed in the integrated light of the planet and star; no spatially resolved image of the planet was possible.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-x-hriv-3-epoxi-exoplanets-v1.0_xwiw-q9cb",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "tres-2",
                 "hat-p-4",
@@ -1656015,681 +1656017,658 @@
                 "tres-3",
                 "hat-p-7"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-X-HRIV-3-EPOXI-EXOPLANETS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-x-hriv-3-epoxi-exoplanets-v1.0_xwiw-q9cb",
-            "description": "This data set set contains calibrated images of eight known transiting extrasolar planetary systems (hot Jupiters) acquired by the Deep Impact High Resolution Visible CCD during the EPOCh phase of the EPOXI mission. From 22 January through 31 August 2008 the HRIV CCD collected over 172,000 usable, photometric-quality visible light images of these transiting planet systems: HAT-P-4, HAT-P-7, GJ 436, TrES-2, TrES-3, XO-2, XO-3, and WASP-3. Time series of continuous 50-second integrations were used with the clear filter (#6) to observe each system for about three weeks, typically covering five or more transits as well as secondary eclipses. An exception was XO-3 which was only observed briefly due to the spacecraft entering safe mode. The transiting planet systems were observed in the integrated light of the planet and star; no spatially resolved image of the planet was possible.",
-            "title": "EPOXI EXOPLANET TRANSIT OBS - HRIV CALIBRATED IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI EXOPLANET TRANSIT OBS - HRIV CALIBRATED IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1299",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Spruce, J.P., G.E. Gasser, and W.W. Hargrove. 2016. MODIS NDVI Data, Smoothed and Gap-filled, for the Conterminous US: 2000-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1299",
-            "issued": "2016-11-17",
-            "temporal": "2000-01-01T00:00:00Z/2015-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "biosphere",
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C2764637520-ORNL_CLOUD",
             "description": "This data set provides Moderate Resolution Imaging Spectroradiometer (MODIS) normalized difference vegetation index (NDVI) data, smoothed and gap-filled, for the conterminous US for the period 2000-01-01 through 2015-12-31. The data were generated using the NASA Stennis Time Series Product Tool (TSPT) to generate NDVI data streams from the Terra satellite (MODIS MOD13Q1 product) and Aqua satellite (MODIS MYD13Q1 product)  instruments.  TSPT produces NDVI data that are less affected by clouds and bad pixels.",
-            "graphic-preview-description": "Browse Image",
-            "title": "MODIS NDVI Data, Smoothed and Gap-filled, for the Conterminous US: 2000-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1299_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1299",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1299",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/US_MODIS_NDVI/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/US_MODIS_NDVI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/US_MODIS_NDVI.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/US_MODIS_NDVI.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1299",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1299",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/US_MODIS_NDVI/comp/US_MODIS_NDVI.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/US_MODIS_NDVI/comp/US_MODIS_NDVI.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1299_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1299_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1299/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1299/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1299_1_fit.png",
+            "identifier": "C2764637520-ORNL_CLOUD",
+            "issued": "2016-11-17",
+            "keyword": [
+                "biosphere",
+                "national geospatial data asset",
+                "ngda",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1299",
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
             "spatial": "-129.89 20.85 -62.56 50.56",
+            "temporal": "2000-01-01T00:00:00Z/2015-12-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS NDVI Data, Smoothed and Gap-filled, for the Conterminous US: 2000-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/ER2/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hobbs, Brian , Carl  Sorenson, Eric  Stith, Ryan  Bennett and Gary  Hoffmann.2022. ER-2 Navigation Data IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/ER2/DATA101",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-15T17:29:01Z/2022-02-28T19:57:22Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "sensor characteristics",
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
-            "identifier": "C1995566252-GHRC_DAAC",
             "description": "The NASA ER-2 Navigation Data IMPACTS dataset contains information recorded by the on-board navigation and data collection systems of the NASA ER-2 high-altitude research aircraft. In addition to typical navigation data (e.g., date, time, latitude/longitude, and altitude) it also contains outside meteorological parameters such as wind speed, wind direction, and temperature. These data were collected during the  Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign, a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic coast. IMPACTS aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands;  and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. The IMPACTS navigation dataset files are available from January 15, 2020 through February 28, 2022 in ASCII-ict format.",
-            "title": "ER-2 Navigation Data IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FER2%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FER2%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=er2navimpacts&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=er2navimpacts&ghrccloud%2Fdata%2F=",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.nasa.gov/centers/dryden/pdf/90464main_ER2handbook.pdf",
-                    "description": "ER-2 Airborne Laboratory Experimenter Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "ER-2 Airborne Laboratory Experimenter Handbook",
+                    "downloadURL": "https://www.nasa.gov/centers/dryden/pdf/90464main_ER2handbook.pdf",
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
-                    "downloadURL": "https://www.nasa.gov/centers/armstrong/news/FactSheets/FS-046-DFRC.html",
-                    "description": "NASA Armstrong Fact Sheet: ER-2 High-Altitude Airborne Science Aircraft",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Armstrong Fact Sheet: ER-2 High-Altitude Airborne Science Aircraft",
+                    "downloadURL": "https://www.nasa.gov/centers/armstrong/news/FactSheets/FS-046-DFRC.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/ER2Nav/doc/er2navimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/ER2Nav/doc/er2navimpacts_dataset.pdf",
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
-                    "description": "IMPACTS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Project Home Page",
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
+            "identifier": "C1995566252-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "sensor characteristics",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/ER2/DATA101",
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
             "spatial": "-118.284 31.9013 -64.8938 47.6964",
+            "temporal": "2020-01-15T17:29:01Z/2022-02-28T19:57:22Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ER-2 Navigation Data IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SASSIE-RVCTD2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Perez Valentin, Jaynise. 2023-05-08. SASSIE Arctic Field Campaign Castaway Data Fall 2022. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, SASSIE Project Data Manager, Frederick Bingham. https://doi.org/10.5067/SASSIE-RVCTD2. https://doi.org/10.5067/SASSIE-RVCTD2.",
-            "issued": "2022-09-09",
-            "temporal": "2022-09-09T15:00:00Z/2022-09-19T01:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-19",
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "earth science",
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
-            "identifier": "C2624100570-POCLOUD",
-            "description": "The Salinity and Stratification at the Sea Ice Edge (SASSIE) project is a NASA experiment that aims to understand how salinity anomalies in the upper ocean generated by melting sea ice affect sea surface temperature (SST), stratification, and subsequent sea-ice growth. SASSIE involved a field campaign that sampled the transition from summer melt to autumn ice advance in the Beaufort Sea during August-October 2022, making intensive in situ and remote sensing observations within ~200 km of the sea ice edge. This dataset contains profiles of upper ocean temperature, salinity, and density taken with a Shipboard CastAway Conductivity-Temperature-Depth instrument (CastAway-CTD). A total of 254 profiles were taken over the sampling period at various locations, typically every 30 minutes while the ship was underway, with a mean depth of 45m. Data are available in NetCDF format.",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Perez Valentin, Jaynise",
-            "title": "SASSIE Arctic Field Campaign Shipboard Castaway CTD Data Fall 2022 Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_SHIPBOARD_CASTAWAY_CTD_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Salinity and Stratification at the Sea Ice Edge (SASSIE) project is a NASA experiment that aims to understand how salinity anomalies in the upper ocean generated by melting sea ice affect sea surface temperature (SST), stratification, and subsequent sea-ice growth. SASSIE involved a field campaign that sampled the transition from summer melt to autumn ice advance in the Beaufort Sea during August-October 2022, making intensive in situ and remote sensing observations within ~200 km of the sea ice edge. This dataset contains profiles of upper ocean temperature, salinity, and density taken with a Shipboard CastAway Conductivity-Temperature-Depth instrument (CastAway-CTD). A total of 254 profiles were taken over the sampling period at various locations, typically every 30 minutes while the ship was underway, with a mean depth of 45m. Data are available in NetCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSASSIE-RVCTD2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSASSIE-RVCTD2",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2624100570-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2624100570-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2624100570-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2624100570-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SASSIE-RVCTD2",
-                    "description": "Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset Landing Page",
+                    "downloadURL": "https://doi.org/10.5067/SASSIE-RVCTD2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_SHIPBOARD_CASTAWAY_CTD_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_SHIPBOARD_CASTAWAY_CTD_V1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_SHIPBOARD_CASTAWAY_CTD_V1.jpg",
+            "identifier": "C2624100570-POCLOUD",
+            "issued": "2022-09-09",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SASSIE-RVCTD2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
             "spatial": "-152.5 72.0 -145.0 73.5",
+            "temporal": "2022-09-09T15:00:00Z/2022-09-19T01:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASSIE Arctic Field Campaign Shipboard Castaway CTD Data Fall 2022 Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/WBAND/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kollias, Pavlos .2014. GPM GROUND VALIDATION MCGILL W-BAND RADAR GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/WBAND/DATA301",
-            "issued": "2014-01-13",
-            "temporal": "2012-02-01T22:26:47Z/2012-02-29T20:56:13Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-24",
-            "keyword": [
-                "clouds",
-                "radar",
-                "spectral/engineering",
-                "atmospheric winds",
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
-            "identifier": "C1979831134-GHRC_DAAC",
             "description": "The GPM Ground Validation McGill W-Band Radar GCPEx dataset was collected from February 1, 2012 to February 29, 2012 at the CARE site in Ontario, Canada as a part of the GPM Cold-season Precipitation Experiment (GCPEx). This datset was collected to aid in the achievement of the over arching goal of GCPEx which is to characterize the ability of multi-frequency active and passive microwave sensors to detect and estimate falling snow. The W-Band radar is a single antenna, 94-GHz pulsed Doppler, vertical pointing radar system. Data products from the W-Band radar include radar reflectivity, Doppler moments, and Doppler spectra of variable lengths. The W-Band radar is primarily used to research various cloud properties. The GPM Ground Validation McGill W-Band Radar GCPEx dataset is available in netCDF format.",
-            "title": "GPM GROUND VALIDATION MCGILL W-BAND RADAR GCPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FWBAND%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FWBAND%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmwbandgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmwbandgcpex",
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mcgill/gpmxwbandgcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mcgill/gpmxwbandgcpex_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/VERTIX/doc/McGill_data_documentation_gcpex.txt",
-                    "description": "netcdf files created for both radars(WBAND, VERTIX) operated by McGill University",
                     "@type": "dcat:Distribution",
+                    "description": "netcdf files created for both radars(WBAND, VERTIX) operated by McGill University",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/VERTIX/doc/McGill_data_documentation_gcpex.txt",
+                    "mediaType": "text/html",
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
+            "identifier": "C1979831134-GHRC_DAAC",
+            "issued": "2014-01-13",
+            "keyword": [
+                "clouds",
+                "radar",
+                "spectral/engineering",
+                "atmospheric winds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/WBAND/DATA301",
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
             "spatial": "-79.781 44.2328 -79.7802 44.2336",
+            "temporal": "2012-02-01T22:26:47Z/2012-02-29T20:56:13Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION MCGILL W-BAND RADAR GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-3-RDR-STEP-12.8MIN-V1.0",
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
+            "description": "This far encounter step data set consists of the counting rate and flux data for electrons and ions from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Neptune. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Neptune far encounter, the entire LEPT (Low Energy Particle Telescope) and part of the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystems were turned on for data collection.  Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 12.8 minute rate and flux measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-3-rdr-step-12.8min-v1.0_xws2-rddd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-3-RDR-STEP-12.8MIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-3-rdr-step-12.8min-v1.0_xws2-rddd",
-            "description": "This far encounter step data set consists of the counting rate and flux data for electrons and ions from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Neptune. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Neptune far encounter, the entire LEPT (Low Energy Particle Telescope) and part of the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystems were turned on for data collection.  Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 12.8 minute rate and flux measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
-            "title": "VG2 LECP 12.8 MINUTE NEPTUNE\n                                      FAR ENCOUNTER STEP DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 LECP 12.8 MINUTE NEPTUNE\n                                      FAR ENCOUNTER STEP DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_HDF5_L2-V5.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-03-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/SAGEIII/LUNAR_HDF5_L2-V5.2. https://asdc.larc.nasa.gov/project/SAGE%20III-ISS.",
-            "issued": "2018-08-22",
-            "temporal": "2017-06-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Flittner",
                 "hasEmail": "mailto:david.e.flittner@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2066317192-LARC",
             "description": "g3blsp_52 is the Stratospheric Aerosol and Gas Experiment III (SAGE III) on the International Space Station (ISS) (SAGE III/ISS) Level 2 Lunar Event Species Profiles (HDF5) V052 data product. It contains all the species products for a single lunar event. SAGE III was Launched on February 19, 2017 on a SpaceX Falcon 9 from Kennedy Space Center, SAGE III-ISS is the second instrument from the SAGE III project, externally mounted on the ISS. This ISS-based instrument uses a technique known as occultation, which involves looking at the light from the Sun or Moon as it passes through Earth's atmosphere at the edge, or limb, of the planet to provide long-term monitoring of ozone vertical profiles of the stratosphere and mesosphere. The data provided by SAGE III-ISS includes key components of atmospheric composition and their long-term variability, focusing on the study of aerosols, chlorine dioxide, clouds, nitrogen dioxide, nitrogen trioxide, pressure and temperature, and water vapor. SAGE data has historically been used by the World Meteorological Organization to inform their periodic assessments of ozone depletion. These new observations from the International Space Station will continue the SAGE team's contributions to ongoing scientific understanding of the Earth's atmosphere.",
-            "title": "SAGE III/ISS L2 Lunar Event Species Profiles (HDF5) V052",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FLUNAR_HDF5_L2-V5.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FLUNAR_HDF5_L2-V5.2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sage.nasa.gov/",
-                    "description": "SAGE project home page",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE project home page",
+                    "downloadURL": "https://sage.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG-G3B.docx",
-                    "description": "SAGE III/ISS Data Products User\u2019s Guide, April 2021",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Data Products User\u2019s Guide, April 2021",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG-G3B.docx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_HDF5_L2-V5.2",
-                    "description": "DOI data set landing page for g3blsp_52",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for g3blsp_52",
+                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_HDF5_L2-V5.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/sageiii_iss_readers.tar",
-                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/sageiii_iss_readers.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/Release_Notes_v5.2.docx",
-                    "description": "SAGE III/ISS Version 5.2 Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Version 5.2 Release Notes",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/Release_Notes_v5.2.docx",
+                    "mediaType": "text/html",
                     "title": "View an important notice for this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
-                    "description": "NASA Open Source Agreement for Computer Software",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Open Source Agreement for Computer Software",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2066317192-LARC",
-                    "description": "Earthdata Search for g3blsp_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for g3blsp_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2066317192-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SAGE_III_ISS/g3blsp.052/",
-                    "description": "ASDC Direct Data Download for g3blsp_52",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for g3blsp_52",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SAGE_III_ISS/g3blsp.052/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/SAGE%20III-ISS",
-                    "description": "ASDC Data and Information for SAGE III-ISS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for SAGE III-ISS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/SAGE%20III-ISS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2066317192-LARC",
+            "issued": "2018-08-22",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_HDF5_L2-V5.2",
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
+            "temporal": "2017-06-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "SAGE III-ISS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAGE III/ISS L2 Lunar Event Species Profiles (HDF5) V052"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0777-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-15T09:29:45.000 to 2015-05-15T12:08:36.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0777-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0777-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0777-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-15T09:29:45.000 to 2015-05-15T12:08:36.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0777 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0777 V1.0"
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
-                "knowledge",
-                "appel",
-                "ask the academy",
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
-            "identifier": "NASA-862__25",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1656697,148 +1656676,178 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__25",
+            "issued": "2018-06-25",
+            "keyword": [
+                "knowledge",
+                "appel",
+                "ask the academy",
+                "sharing"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-NORMAL-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-normal-ops-v1.0_xwv8-cg4w",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-NORMAL-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-normal-ops-v1.0_xwv8-cg4w",
-            "description": "not applicable",
-            "title": "MER 1 MARS NAVIGATION CAMERA SURFACE NORMAL RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS NAVIGATION CAMERA SURFACE NORMAL RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1169",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nepstad, D.C., P.R. Moutinho, and P. Brando. 2013. LBA-ECO CD-05 Soil VWC and Meteorology, Rainfall Exclusion, Tapajos National Forest. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1169",
-            "issued": "2023-10-03",
-            "temporal": "1999-01-01T00:00:00Z/2007-04-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "land surface/agriculture indicators",
-                "climate indicators",
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
-            "identifier": "C2781551326-ORNL_CLOUD",
             "description": "This data set reports soil moisture expressed as volumetric water content (VWC), daily precipitation, air temperature, relative humidity, and dew point measurements conducted at the Seca Floresta site, km 67, Tapajos National Forest, Brazil. The measurements were part of the Rainfall Exclusion Experiment (REE) established to study the response of a humid Amazonian forest to severe drought.VWC was measured with continuous high-resolution frequency-domain reflectometry to 11-m depth in two 1-ha plots from 1999 to 2007. One plot was subjected to ~75 percent throughfall exclusion during the rainy season (exclusion) and another monitored under normal conditions (control). Daily precipitation was measured in the control plot and in a nearby clearing between 1999 and 2006 using wedge rain gauges. Air temperature, relative humidity, and dew point were measured along the vertical forest profile of the control and dry plots of the site between 2000 and 2003.There are three comma-delimited data files (.csv) with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-05 Soil VWC and Meteorology, Rainfall Exclusion, Tapajos National Forest",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1169",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1169",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD05_Micromet/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD05_Micromet/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD05_Micromet.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD05_Micromet.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1169",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1169",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD05_Micromet/comp/CD05_Micromet.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD05_Micromet/comp/CD05_Micromet.pdf",
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
+            "identifier": "C2781551326-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "land surface/agriculture indicators",
+                "climate indicators",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1169",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-2.75 -55.0",
+            "temporal": "1999-01-01T00:00:00Z/2007-04-20T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-05 Soil VWC and Meteorology, Rainfall Exclusion, Tapajos National Forest"
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
```

