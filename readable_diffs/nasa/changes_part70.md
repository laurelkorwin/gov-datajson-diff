# Change History for nasa.json (Part 70)

### Changes from 31606f9 to dd2190f (Part 59/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "NASA/JPL/PODAAC",
+            "series-name": "Smith and Reynolds NCDC Level 4 Historical Reconstructed Reconstructed Sea Level",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1950-01-03T00:00:00Z/2009-06-27T23:59:59Z",
             "theme": [
                 "ROSES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Reconstructed Sea Level Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103MOD.021",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2021-07-20. VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750 m. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/VJ103MOD.021. https://doi.org/10.5067/VIIRS/VJ103MOD.021.",
-            "issued": "2021-01-21",
-            "temporal": "2018-01-05T00:00:00Z/2024-06-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-05",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
-                "sensor characteristics",
-                "spectral/engineering",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kwofu Chiang",
                 "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2105084593-LAADS",
-            "description": "The VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m product, short-name VJ103MOD contains the derived line-of-sight (LOS) vectors for each of the 750-m moderate-resolution, or M-bands.  The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform\u2019s ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry.  It produces geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel.  The VJ103MOD product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, and quality flag for every pixel location.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation L1 6-Min Swath 750m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m product, short-name VJ103MOD contains the derived line-of-sight (LOS) vectors for each of the 750-m moderate-resolution, or M-bands.  The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform\u2019s ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry.  It produces geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel.  The VJ103MOD product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, and quality flag for every pixel location.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103MOD.021",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103MOD.021",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ103MOD.021",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ103MOD.021",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ103MOD--5201",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ103MOD--5201",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5201/VJ103MOD/",
-                    "description": "Direct access to VJ103MOD C 2.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to VJ103MOD C 2.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5201/VJ103MOD/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5201/VJ103MOD/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5201/VJ103MOD/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/NASA_VIIRS_L1B_UG_August_2021.pdf",
-                    "description": "VIIRS Level-1 User Guide - version 3",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS Level-1 User Guide - version 3",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/NASA_VIIRS_L1B_UG_August_2021.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/NASARevisedVIIRSGeolocationATBD2014.pdf",
-                    "description": "VIIRS Geolocation ATBD Link",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS Geolocation ATBD Link",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/NASARevisedVIIRSGeolocationATBD2014.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "identifier": "C2105084593-LAADS",
+            "issued": "2021-01-21",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "sensor characteristics",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103MOD.021",
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
+            "temporal": "2018-01-05T00:00:00Z/2024-06-10T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation L1 6-Min Swath 750m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2377",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Virkkala, A-M., B.M. Rogers, J.D. Watts, K. Arndt, S. Potter, I. Wargowsky, and S. Natali. 2024. Machine learning-based Arctic-boreal terrestrial ecosystem CO2 fluxes, 2001-2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2377",
-            "issued": "2024-11-04",
-            "temporal": "2001-01-01T00:00:00Z/2020-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "atmospheric chemistry",
-                "ecological dynamics",
-                "carbon flux",
-                "atmosphere",
-                "biosphere",
-                "earth science",
-                "climate indicators",
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
-            "identifier": "C3261062541-ORNL_CLOUD",
             "description": "This dataset provides gridded estimates of gross primary productivity (GPP), ecosystem respiration (Reco), and net ecosystem CO2 exchange (NEE) across the circumpolar terrestrial Arctic-boreal region at a 1-km spatial resolution. Monthly CO2 flux data from 2001 to 2020 were generated using terrestrial eddy covariance and chamber CO2 flux observations, combined with geospatial meteorological, remote sensing, topographical and soil data, all within a random forest modeling framework. Aggregated average annual NEE, average annual NEE with direct fire emissions added based on the Global Fire Emissions Database (GFED) product, and temporal trends in annual NEE rasters over 2002-2020 are also included. The data are provided in NetCDF and GeoTIFF formats.",
-            "graphic-preview-description": "Annual average terrestrial net ecosystem exchange (NEE) and direct fire emissions from 2002-2020 showing areas with net CO2 sinks (i.e. areas taking up CO2 from the atmosphere) and net CO2 sources (i.e. releasing net CO2 emissions to the atmosphere) (Virkkala et al., 2024).",
-            "title": "Machine learning-based Arctic-boreal terrestrial ecosystem CO2 fluxes, 2001-2020",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/CO2Fluxes_Arctic_Boreal_Domain_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2377",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2377",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/CO2Fluxes_Arctic_Boreal_Domain/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/CO2Fluxes_Arctic_Boreal_Domain/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/CO2Fluxes_Arctic_Boreal_Domain.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/CO2Fluxes_Arctic_Boreal_Domain.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2377",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2377",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/CO2Fluxes_Arctic_Boreal_Domain/comp/CO2Fluxes_Arctic_Boreal_Domain.pdf",
-                    "description": "Machine learning-based Arctic-boreal terrestrial ecosystem CO2 fluxes, 2001-2020: CO2Fluxes_Arctic_Boreal_Domain.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Machine learning-based Arctic-boreal terrestrial ecosystem CO2 fluxes, 2001-2020: CO2Fluxes_Arctic_Boreal_Domain.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/CO2Fluxes_Arctic_Boreal_Domain/comp/CO2Fluxes_Arctic_Boreal_Domain.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/CO2Fluxes_Arctic_Boreal_Domain_Fig1.jpg",
-                    "description": "Annual average terrestrial net ecosystem exchange (NEE) and direct fire emissions from 2002-2020 showing areas with net CO2 sinks (i.e. areas taking up CO2 from the atmosphere) and net CO2 sources (i.e. releasing net CO2 emissions to the atmosphere) (Virkkala et al., 2024).",
                     "@type": "dcat:Distribution",
+                    "description": "Annual average terrestrial net ecosystem exchange (NEE) and direct fire emissions from 2002-2020 showing areas with net CO2 sinks (i.e. areas taking up CO2 from the atmosphere) and net CO2 sources (i.e. releasing net CO2 emissions to the atmosphere) (Virkkala et al., 2024).",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/CO2Fluxes_Arctic_Boreal_Domain_Fig1.jpg",
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
+            "graphic-preview-description": "Annual average terrestrial net ecosystem exchange (NEE) and direct fire emissions from 2002-2020 showing areas with net CO2 sinks (i.e. areas taking up CO2 from the atmosphere) and net CO2 sources (i.e. releasing net CO2 emissions to the atmosphere) (Virkkala et al., 2024).",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/CO2Fluxes_Arctic_Boreal_Domain_Fig1.jpg",
+            "identifier": "C3261062541-ORNL_CLOUD",
+            "issued": "2024-11-04",
+            "keyword": [
+                "atmospheric chemistry",
+                "ecological dynamics",
+                "carbon flux",
+                "atmosphere",
+                "biosphere",
+                "earth science",
+                "climate indicators",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2377",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 33.68 180.0 90.0",
+            "temporal": "2001-01-01T00:00:00Z/2020-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Machine learning-based Arctic-boreal terrestrial ecosystem CO2 fluxes, 2001-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/896",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fisch, G., A. Lola, H. Soares, I. Silva, E. Rocha, C.A. Nobre, and R.L. Victoria. 2008. Pre-LBA FLUAMAZON Experiment Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/896",
-            "issued": "2023-11-19",
-            "temporal": "1989-11-23T00:00:00Z/1989-12-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmospheric winds",
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
-            "identifier": "C2804820806-ORNL_CLOUD",
             "description": "The FLUAMAZON Experiment data set includes meteorological data collected with radiosondes to examine the moisture flux from the northern coast of South America (near the mouth of the Amazon River) into central Amazonia.  The measurements were collected from November 23, to December 21, 1989 during the period of transition between the dry and humid seasons in the region.   Some of the studies performed with data from FLUAMAZON were related to the atmospheric thermodynamic structure over Amazonia.  During FLUAMAZON, radiosonde measurements were made simultaneously in five different locations: Alcantara, Belem, Oiapoque, Manaus, and Alta Floresta. ASCII text data files for each location have been compiled and compressed into site-specific zipped files.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Pre-LBA FLUAMAZON Experiment Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F896",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F896",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/physical_climate/FLUAMAZON/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/physical_climate/FLUAMAZON/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/Pre_LBA_FLUAMAZON.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/Pre_LBA_FLUAMAZON.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/896",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/896",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/physical_climate/FLUAMAZON/comp/Pre_LBA_FLUAMAZON.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/physical_climate/FLUAMAZON/comp/Pre_LBA_FLUAMAZON.pdf",
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
+            "identifier": "C2804820806-ORNL_CLOUD",
+            "issued": "2023-11-19",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/896",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-59.0 -9.0 -44.0 4.0",
+            "temporal": "1989-11-23T00:00:00Z/1989-12-21T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pre-LBA FLUAMAZON Experiment Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-3-EAR2-SPM-V1.0",
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
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the EAR2 (Earth fly-by 2) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-3-ear2-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-3-EAR2-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-3-ear2-spm-v1.0",
-            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the EAR2 (Earth fly-by 2) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER EARTH ROMAP 3 EAR2 SPM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER EARTH ROMAP 3 EAR2 SPM V1.0"
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
-                "index"
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
-            "identifier": "NASA-639",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r71)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -612981,568 +612961,564 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-639",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "dictionary",
+                "index"
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
+            "title": "PDS Data Dictionary (1r71)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-EXT2-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Rosetta Extension 2 mission phase, which took place between 2016-04-06 and 2016-06-30.  The current V2.0 data set supersedes the previous V1.0 data set with improved documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-ext2-v2.0_ctyz-men2",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-EXT2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-ext2-v2.0_ctyz-men2",
-            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Rosetta Extension 2 mission phase, which took place between 2016-04-06 and 2016-06-30.  The current V2.0 data set supersedes the previous V1.0 data set with improved documentation.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 EXT2 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 EXT2 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1284-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-25T17:31:45.000 to 2015-12-25T19:00:15.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1284-v1.0_ctz4-d538",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1284-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1284-v1.0_ctz4-d538",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-25T17:31:45.000 to 2015-12-25T19:00:15.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1284 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1284 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/ZO0X4QAX5WTD",
             "citation": "David Mocko, NASA/GSFC/HSL. 2014-03-01. NLDAS_VIC0125_M. Version 002. NLDAS VIC Land Surface Model L4 Monthly 0.125 x 0.125 degree V002. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ZO0X4QAX5WTD. https://disc.gsfc.nasa.gov/datacollection/NLDAS_VIC0125_M_002.html. Digital Science Data.",
-            "issued": "2014-03-01",
-            "temporal": "1979-01-01T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-03-01",
-            "references": [
-                "https://doi.org/10.1029/2011JD016048",
-                "https://doi.org/10.1029/2011JD016051",
-                "https://doi.org/10.1175/1520-0493(1997)125<2896:AOTLSA>2.0.CO;2",
-                "https://doi.org/10.1023/A:1000531001463",
-                "https://doi.org/10.1029/2002JD003296",
-                "https://doi.org/10.1029/1999JD900232",
-                "https://doi.org/10.1175/2009JHM1174.1",
-                "https://doi.org/10.1002/hyp.9214"
-            ],
-            "keyword": [
-                "atmosphere",
-                "snow/ice",
-                "precipitation",
-                "land surface",
-                "earth science",
-                "biosphere",
-                "atmospheric water vapor",
-                "surface radiative properties",
-                "surface thermal properties",
-                "vegetation",
-                "atmospheric temperature",
-                "surface water",
-                "soils",
-                "terrestrial hydrosphere",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SILBERSTEIN",
                 "hasEmail": "mailto:david.s.silberstein@nasa.gov"
             },
+            "creator": "David Mocko, NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1233767673-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This data set contains a series of land surface parameters simulated from the VIC land-surface model (LSM) for Phase 2 of the North American Land Data Assimilation System (NLDAS-2). The data are in 1/8th degree grid spacing and range from January 1979 to present. The temporal resolution is monthly. The file format is WMO GRIB-1. The NLDAS-2 monthly Noah model data were generated from the NLDAS-2 hourly Noah model data, as monthly accumulation for rainfall, snowfall, subsurface runoff, surface runoff, total evapotranspiration, snow melt, and monthly averages for other variables. Each monthly period is from 00Z at start of the month to 23:59Z at end of the month, with the exception of the very first month in the data set (January 1979), which starts at 00Z 02 January 1979. Also, for the first month (January 1979), since the variables listed as instantaneous in the README file do not have valid data exactly on 00Z 02 January 1979, this one hour is not included in the average for this one month. \n\nA brief description about the NLDAS-2 monthly VIC model data can be found from the dataset landing page for NLDAS_VIC0125_H_002 and the NLDAS-2 README document. \n\nDetails about the NLDAS-2 configuration of the VIC LSM can be found in Xia et al. (2012). The version of the VIC model for the NLDAS-2 VIC data available from the NASA GES DISC is VIC-4.0.3; this version of the VIC model is the same as used in Sheffield et al. (2003). \n\nThe NLDAS-2 VIC monthly data contain forty-three fields. The data set applies a user-defined parameter table to indicate the contents and parameter number. The GRIBTAB file shows a list of parameters for this data set, along with their Product Definition Section (PDS) IDs and units. \n\nFor information about the vertical layers of the Soil Moisture Content (PDS 086), Soil Temperature (PDS 085), and Liquid Soil Moisture Content, please see the README Document or the GrADS ctl file.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "NLDAS_VIC0125_M",
-            "creator": "David Mocko, NASA/GSFC/HSL",
-            "graphic-preview-description": "NLDAS-2 VIC Monthly 0.125 degree Top 1-meter Soil Moisture Content  [kg/m^2] July 2010",
-            "title": "NLDAS VIC Land Surface Model L4 Monthly 0.125 x 0.125 degree V002 (NLDAS_VIC0125_M) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_VIC0125_M_002.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZO0X4QAX5WTD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZO0X4QAX5WTD",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_VIC0125_M_002.png",
-                    "description": "NLDAS-2 VIC Monthly 0.125 degree Top 1-meter Soil Moisture Content  [kg/m^2] July 2010",
                     "@type": "dcat:Distribution",
+                    "description": "NLDAS-2 VIC Monthly 0.125 degree Top 1-meter Soil Moisture Content  [kg/m^2] July 2010",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_VIC0125_M_002.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_VIC0125_M_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_VIC0125_M_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_VIC0125_M.002/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_VIC0125_M.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_VIC0125_M",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_VIC0125_M",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_VIC0125_M.002",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_VIC0125_M.002",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_VIC0125_M.002/doc/gribtab_NLDAS_VIC.002.txt",
-                    "description": "The GRIBTAB file contains a list of variables, along with the GRIB Product Definition Section (PDS) ID, variable short name, long names, and unit.",
                     "@type": "dcat:Distribution",
+                    "description": "The GRIBTAB file contains a list of variables, along with the GRIB Product Definition Section (PDS) ID, variable short name, long names, and unit.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_VIC0125_M.002/doc/gribtab_NLDAS_VIC.002.txt",
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
+            "graphic-preview-description": "NLDAS-2 VIC Monthly 0.125 degree Top 1-meter Soil Moisture Content  [kg/m^2] July 2010",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_VIC0125_M_002.png",
+            "identifier": "C1233767673-GES_DISC",
+            "issued": "2014-03-01",
+            "keyword": [
+                "atmosphere",
+                "snow/ice",
+                "precipitation",
+                "land surface",
+                "earth science",
+                "biosphere",
+                "atmospheric water vapor",
+                "surface radiative properties",
+                "surface thermal properties",
+                "vegetation",
+                "atmospheric temperature",
+                "surface water",
+                "soils",
+                "terrestrial hydrosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ZO0X4QAX5WTD",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-03-01",
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
+                "https://doi.org/10.1175/1520-0493(1997)125<2896:AOTLSA>2.0.CO;2",
+                "https://doi.org/10.1023/A:1000531001463",
+                "https://doi.org/10.1029/2002JD003296",
+                "https://doi.org/10.1029/1999JD900232",
+                "https://doi.org/10.1175/2009JHM1174.1",
+                "https://doi.org/10.1002/hyp.9214"
+            ],
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "NLDAS_VIC0125_M",
             "spatial": "-125.0 25.0 -67.0 53.0",
+            "temporal": "1979-01-01T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "NLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NLDAS VIC Land Surface Model L4 Monthly 0.125 x 0.125 degree V002 (NLDAS_VIC0125_M) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DC3_Miscellaneous_DLR-Falcon_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-04-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DC3_Miscellaneous_DLR-Falcon_Data_1.",
-            "issued": "2021-03-12",
-            "temporal": "2012-05-29T00:00:00Z/2012-06-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "keyword": [
-                "atmosphere",
-                "altitude",
-                "earth science",
-                "atmospheric winds"
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
-            "identifier": "C2050607974-LARC_ASDC",
             "description": "DC3_Miscellaneous_DLR-Falcon_Data are miscellaneous data collected onboard the DLR Falcon aircraft during the Deep Convective Clouds and Chemistry (DC3) field campaign. This product features data from the Global Forecast System (GFS) model. Data collection for this product is complete.\r\n\r\nThe Deep Convective Clouds and Chemistry (DC3) field campaign sought to understand the dynamical, physical, and lightning processes of deep, mid-latitude continental convective clouds and to define the impact of these clouds on upper tropospheric composition and chemistry. DC3 was conducted from May to June 2012 with a base location of Salina, Kansas. Observations were conducted in northeastern Colorado, west Texas to central Oklahoma, and northern Alabama in order to provide a wide geographic sample of storm types and boundary layer compositions, as well as to sample convection.\r\nDC3 had two primary science objectives. The first was to investigate storm dynamics and physics, lightning and its production of nitrogen oxides, cloud hydrometeor effects on wet deposition of species, surface emission variability, and chemistry in anvil clouds. Observations related to this objective focused on the early stages of active convection. The second objective was to investigate changes in upper tropospheric chemistry and composition after active convection. Observations related to this objective focused on the 12-48 hours following convection. This objective also served to explore seasonal change of upper tropospheric chemistry.\r\nIn addition to using the NSF/NCAR Gulfstream-V (GV) aircraft, the NASA DC-8 was used during DC3 to provide in-situ measurements of the convective storm inflow and remotely-sensed measurements used for flight planning and column characterization. DC3 utilized ground-based radar networks spread across its observation area to measure the physical and kinematic characteristics of storms. Additional sampling strategies relied on lightning mapping arrays, radiosondes, and precipitation collection. Lastly, DC3 used data collected from various satellite instruments to achieve its goals, focusing on measurements from CALIOP onboard CALIPSO and CPL onboard CloudSat. In addition to providing an extensive set of data related to deep, mid-latitude continental convective clouds and analyzing their impacts on upper tropospheric composition and chemistry, DC3 improved models used to predict convective transport. DC3 improved knowledge of convection and chemistry, and provided information necessary to understanding the processes relating to ozone in the upper troposphere.",
-            "title": "DC3 Miscellaneous DLR-Falcon Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDC3_Miscellaneous_DLR-Falcon_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDC3_Miscellaneous_DLR-Falcon_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.eol.ucar.edu/field_projects/dc3",
-                    "description": "NCAR/UCAR EOL DC3 Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "NCAR/UCAR EOL DC3 Project Page",
+                    "downloadURL": "https://www.eol.ucar.edu/field_projects/dc3",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
-                    "description": "DC3/SEAC4RS Data Management Plan",
                     "@type": "dcat:Distribution",
+                    "description": "DC3/SEAC4RS Data Management Plan",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.eol.ucar.edu/projects/dc3/documents/SPO_DC3_revised.pdf",
-                    "description": "DC3 Scientific Program Overview",
                     "@type": "dcat:Distribution",
+                    "description": "DC3 Scientific Program Overview",
+                    "downloadURL": "https://archive.eol.ucar.edu/projects/dc3/documents/SPO_DC3_revised.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.eol.ucar.edu/projects/dc3/documents/EDO_DC3_revised.pdf",
-                    "description": "DC3 Experimental Design Overview ",
                     "@type": "dcat:Distribution",
+                    "description": "DC3 Experimental Design Overview ",
+                    "downloadURL": "https://archive.eol.ucar.edu/projects/dc3/documents/EDO_DC3_revised.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/96/8/bams-d-13-00290.1.xml",
-                    "description": "DC3 Overview Paper",
                     "@type": "dcat:Distribution",
+                    "description": "DC3 Overview Paper",
+                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/96/8/bams-d-13-00290.1.xml",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://www2.acom.ucar.edu/dc3",
-                    "description": "NCAR/UCAR ACOM DC3 Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "NCAR/UCAR ACOM DC3 Project Home Page",
+                    "downloadURL": "https://www2.acom.ucar.edu/dc3",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/78101/the-anatomy-of-a-thunderstorm/",
-                    "description": "NASA Earth Observatory \"The Anatomy of a Thunderstorm\" Article",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory \"The Anatomy of a Thunderstorm\" Article",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/78101/the-anatomy-of-a-thunderstorm/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/78497/when-wildfire-smoke-and-thunderstorms-collide/",
-                    "description": "NASA Earth Observatory \"When Wildfire, Smoke, and Thunderstorms Collide\" Article",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory \"When Wildfire, Smoke, and Thunderstorms Collide\" Article",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/78497/when-wildfire-smoke-and-thunderstorms-collide/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dc3blog.wordpress.com/",
-                    "description": "DC3 Blog",
                     "@type": "dcat:Distribution",
+                    "description": "DC3 Blog",
+                    "downloadURL": "https://dc3blog.wordpress.com/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.eol.ucar.edu/project/DC3",
-                    "description": "NCAR/UCAR EOL Data Webpage",
                     "@type": "dcat:Distribution",
+                    "description": "NCAR/UCAR EOL Data Webpage",
+                    "downloadURL": "https://data.eol.ucar.edu/project/DC3",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/dryden/status_reports/DC-8_status_05_21_12.html",
-                    "description": "NASA DC3 Status Report",
                     "@type": "dcat:Distribution",
+                    "description": "NASA DC3 Status Report",
+                    "downloadURL": "https://www.nasa.gov/centers/dryden/status_reports/DC-8_status_05_21_12.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2050607974-LARC_ASDC",
-                    "description": "Earthdata Search for DC3_Miscellaneous_DLR-Falcon_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DC3_Miscellaneous_DLR-Falcon_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2050607974-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DC3/Miscellaneous_DLR-Falcon_Data_1/",
-                    "description": "ASDC Direct Data Download for DC3_Miscellaneous_DLR-Falcon_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DC3_Miscellaneous_DLR-Falcon_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DC3/Miscellaneous_DLR-Falcon_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2050607974-LARC_ASDC",
+            "issued": "2021-03-12",
+            "keyword": [
+                "atmosphere",
+                "altitude",
+                "earth science",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DC3_Miscellaneous_DLR-Falcon_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-04-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -110.0 25.0 -90.0 45.0 -90.0 45.0 -110.0 25.0 -110.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2012-05-29T00:00:00Z/2012-06-14T23:59:59.999Z",
             "theme": [
                 "DC3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DC3 Miscellaneous DLR-Falcon Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast.bus-demeo.taxonomy&version=1.0",
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
+            "description": "The Bus-DeMeo asteroid taxonomy          classification system, described in DeMeo et al. (2009), is based on   reflectance spectrum characteristics for 371 asteroids measured over   the wavelength 0.45 to 2.45 microns.  This system of 24 classes is     constructed using principal component analysis, following most closely the visible wavelength taxonomy of Bus (1999), which itself builds     upon the system of Tholen (1984).  Nearly all of the Bus taxonomy      classes are preserved, with one new class (Sv) defined.  This data set includes a table of classifications in the Bus-DeMeo system for the    371 asteroids upon which the system is based.  It also includes mean   spectra for each of the classes.",
+            "identifier": "urn:nasa:pds:ast.bus-demeo.taxonomy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "multiple asteroids",
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast.bus-demeo.taxonomy&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ast.bus-demeo.taxonomy",
-            "description": "The Bus-DeMeo asteroid taxonomy          classification system, described in DeMeo et al. (2009), is based on   reflectance spectrum characteristics for 371 asteroids measured over   the wavelength 0.45 to 2.45 microns.  This system of 24 classes is     constructed using principal component analysis, following most closely the visible wavelength taxonomy of Bus (1999), which itself builds     upon the system of Tholen (1984).  Nearly all of the Bus taxonomy      classes are preserved, with one new class (Sv) defined.  This data set includes a table of classifications in the Bus-DeMeo system for the    371 asteroids upon which the system is based.  It also includes mean   spectra for each of the classes.",
-            "title": "BUS-DEMEO ASTEROID TAXONOMY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "BUS-DEMEO ASTEROID TAXONOMY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9-M-IRIS-3-RDR-V1.0",
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
-                "mariner71",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The dataset contains measurements from the infrared interferometer spectrometer and ancillary data. Each record of the dataset consists of a header and a spectral observation of Mars geometry of the observation. The dataset is ordered by time as measured by the Data Acquisition System (DAS) time (1 DAS count is approximately 1.2 sec.). Two IRIS frames are completed every 35 DAS counts calibration observation (alternately of interstellar space and an internal calibration blackbody), and is therefore absent from the calibrated dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-m-iris-3-rdr-v1.0_cu52-qvcw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mariner71",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9-M-IRIS-3-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-m-iris-3-rdr-v1.0_cu52-qvcw",
-            "description": "The dataset contains measurements from the infrared interferometer spectrometer and ancillary data. Each record of the dataset consists of a header and a spectral observation of Mars geometry of the observation. The dataset is ordered by time as measured by the Data Acquisition System (DAS) time (1 DAS count is approximately 1.2 sec.). Two IRIS frames are completed every 35 DAS counts calibration observation (alternately of interstellar space and an internal calibration blackbody), and is therefore absent from the calibrated dataset.",
-            "title": "MARINER9 IRIS RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARINER9 IRIS RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-MVIC-3-PLUTO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Pluto encounter mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-mvic-3-pluto-v1.0_cu7x-9u42",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "nix",
                 "pluto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-MVIC-3-PLUTO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-mvic-3-pluto-v1.0_cu7x-9u42",
-            "description": "This data set contains Calibrated data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Pluto encounter mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS\n      MVIC PLUTO ENCOUNTER\n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS\n      MVIC PLUTO ENCOUNTER\n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/703/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-04-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
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
-            "identifier": "DASHLINK_703",
             "description": "In summary, this paper lays a simple flight plan optimization strategy based on the particle filtering framework described in [5]. This is meant as a first step in formalizing computationally tractable stochastic programming techniques to optimally generate flight plans in response to battery life predictions. This approach takes advantage of the PF framework to simultaneously generate the optimal/sub-optimal flight plan simultaneously with predicting the RUL. Several steps lie ahead like a comparative analysis of alternative stochastic models in terms of optimality as well as computational cost. These options will need to be validated by flight tests where robustness to environmental conditions like air temperature and density as well as wind speed can be evaluated. The notion of risk-tolerance can be introduced via appropriate objective functions, thus allowing a non-zero risk of the dead stick condition in order to use more battery power.",
-            "title": "Optimizing Battery Life for Electric UAVs using a Bayesian Framework",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_IEEEAero_BatteryUAV.pdf",
-                    "description": "2012_IEEEAero_BatteryUAV.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2012_IEEEAero_BatteryUAV.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_IEEEAero_BatteryUAV.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2012_IEEEAero_BatteryUAV.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_703",
+            "issued": "2013-04-25",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/703/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Optimizing Battery Life for Electric UAVs using a Bayesian Framework"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-08-18",
-            "temporal": "2021-08-18T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "ephemeris",
-                "topo",
-                "trajectory",
-                "coordinates",
-                "space",
-                "location",
-                "iss",
-                "station",
-                "coords",
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
-            "identifier": "nasa-iss-data_2021-08-18_cucd-9ish",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-08-18",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -613665,315 +613641,315 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-08-18_cucd-9ish",
+            "issued": "2021-08-18",
+            "keyword": [
+                "ephemeris",
+                "topo",
+                "trajectory",
+                "coordinates",
+                "space",
+                "location",
+                "iss",
+                "station",
+                "coords",
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
+            "temporal": "2021-08-18T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-08-18"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H46W980H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2005-12-31. Last of the Wild Project, Version 2, 2005 (LWP-2): Global Human Influence Index (HII) Dataset (IGHP). Version 2.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H46W980H. https://doi.org/10.7927/H46W980H.",
-            "issued": "2005-12-31",
-            "temporal": "1995-01-01T00:00:00Z/2004-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4M61H5F",
-                "https://doi.org/10.7927/H4GF0RFQ",
-                "https://doi.org/10.7927/H4348H83",
-                "https://doi.org/10.7927/H4ZC80SS",
-                "https://doi.org/10.7927/H4BP00QC"
-            ],
-            "keyword": [
-                "land surface",
-                "biosphere",
-                "earth science",
-                "ecosystems",
-                "land use/land cover"
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
-            "identifier": "C179001854-SEDAC",
-            "description": "The Global Human Influence Index Dataset of the Last of the Wild Project, Version 2, 2005 (LWP-2) is a global dataset of 1-kilometer grid cells, created from nine global data layers covering human population pressure (population density), human land use and infrastructure (built-up areas, nighttime lights, land use/land cover), and human access (coastlines, roads, railroads, navigable rivers). The dataset  in Interrupted Goode Homolosine Projection (IGHP) is produced by the Wildlife Conservation Society (WCS) and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Last of the Wild Project, Version 2, 2005 (LWP-2): Global Human Influence Index (HII) Dataset (IGHP)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v2/wildareas-v2-human-influence-index-ighp/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Human Influence Index Dataset of the Last of the Wild Project, Version 2, 2005 (LWP-2) is a global dataset of 1-kilometer grid cells, created from nine global data layers covering human population pressure (population density), human land use and infrastructure (built-up areas, nighttime lights, land use/land cover), and human access (coastlines, roads, railroads, navigable rivers). The dataset  in Interrupted Goode Homolosine Projection (IGHP) is produced by the Wildlife Conservation Society (WCS) and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH46W980H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH46W980H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v2/wildareas-v2-human-influence-index-ighp/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v2/wildareas-v2-human-influence-index-ighp/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-ighp/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-ighp/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-ighp",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-ighp",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v2/wildareas-v2-human-influence-index-ighp/sedac-logo.jpg",
+            "identifier": "C179001854-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "land surface",
+                "biosphere",
+                "earth science",
+                "ecosystems",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.7927/H46W980H",
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
+                "https://doi.org/10.7927/H4348H83",
+                "https://doi.org/10.7927/H4ZC80SS",
+                "https://doi.org/10.7927/H4BP00QC"
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
+            "title": "Last of the Wild Project, Version 2, 2005 (LWP-2): Global Human Influence Index (HII) Dataset (IGHP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-2-LAUNCH-V1.0",
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
-                "new horizons",
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Alice UV Imager instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-2-launch-v1.0_cuf8-zdf9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "new horizons",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-2-LAUNCH-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-2-launch-v1.0_cuf8-zdf9",
-            "description": "This data set contains Raw data taken by the New Horizons Alice UV Imager instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS ALICE POST-LAUNCH CHECKOUT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS ALICE POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/UD6O2YXON5UR",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRVM3D. Version 1. TROPESS Chemical Reanalysis Meridional Wind Monthly 3-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/UD6O2YXON5UR. https://disc.gsfc.nasa.gov/datacollection/TRPSCRVM3D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmospheric winds",
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
-            "identifier": "C2837626879-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Meridional Wind Monthly 3-dimensional Product contains vertical meridional wind component (v vector) values, a meteorological field. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at monthly resolution, and a spatial resolution of 1.125 x 1.125 degrees at 27 pressure levels between 1000 and 60 hPa. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRVM3D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Meridional Wind Monthly 3-dimensional Product V1 (TRPSCRVM3D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRVM3D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUD6O2YXON5UR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUD6O2YXON5UR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRVM3D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRVM3D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRVM3D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRVM3D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRVM3D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRVM3D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRVM3D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRVM3D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_METFIELDS/TRPSCRVM3D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_METFIELDS/TRPSCRVM3D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_METFIELDS/TRPSCRVM3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_METFIELDS/TRPSCRVM3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRVM3D_Sample.png",
+            "identifier": "C2837626879-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmospheric winds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/UD6O2YXON5UR",
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
+            "series-name": "TRPSCRVM3D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Meridional Wind Monthly 3-dimensional Product V1 (TRPSCRVM3D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0044-V1.0",
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
-                "sun",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-04-27T00:03:06.500 to 2006-04-27T03:14:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0044-v1.0_cufm-zibg",
+            "issued": "2018-06-26",
+            "keyword": [
+                "sun",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0044-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0044-v1.0_cufm-zibg",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-04-27T00:03:06.500 to 2006-04-27T03:14:07.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0044 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0044 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-25",
-            "temporal": "2021-05-25T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "location",
-                "iss",
-                "international",
-                "ephemeris",
-                "coords",
-                "coordinates",
-                "topo",
-                "station",
-                "space",
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
-            "identifier": "nasa-iss-data_2021-05-25_cugc-gbaf",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-05-25",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -614096,242 +614072,245 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-05-25_cugc-gbaf",
+            "issued": "2021-05-25",
+            "keyword": [
+                "location",
+                "iss",
+                "international",
+                "ephemeris",
+                "coords",
+                "coordinates",
+                "topo",
+                "station",
+                "space",
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
+            "temporal": "2021-05-25T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-05-25"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SWAP-2-PLUTO-V3.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains SWAP observations taken during the                the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for SWAP.                                 This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and     the end of October, 2016, completing the delivery of all data covering   the Pluto Encounter and subsequent Calibration Campaign.                 Also, updates were made to the calibration files, documentation, and     catalog files.  Finally, downlink data several days beyond the end of    the nominal end of mission phase were included in this data set in an    attempt to fill out the products at the nominal end of mission phase;    refer to the CONFIDENCE_LEVEL_NOTE in this data set catalog for more     details.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-swap-2-pluto-v3.0_cuj8-vakp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SWAP-2-PLUTO-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-swap-2-pluto-v3.0_cuj8-vakp",
-            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains SWAP observations taken during the                the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for SWAP.                                 This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and     the end of October, 2016, completing the delivery of all data covering   the Pluto Encounter and subsequent Calibration Campaign.                 Also, updates were made to the calibration files, documentation, and     catalog files.  Finally, downlink data several days beyond the end of    the nominal end of mission phase were included in this data set in an    attempt to fill out the products at the nominal end of mission phase;    refer to the CONFIDENCE_LEVEL_NOTE in this data set catalog for more     details.",
-            "title": "NEW HORIZONS                            \n      SWAP PLUTO ENCOUNTER                                                    \n      RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SWAP PLUTO ENCOUNTER                                                    \n      RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1138-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-28T20:07:20.000 to 2015-10-29T05:04:08.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1138-v1.0_cukm-m2mc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1138-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1138-v1.0_cukm-m2mc",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-28T20:07:20.000 to 2015-10-29T05:04:08.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1138 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1138 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-2-EDR-EROS%2FORBIT-V1.0",
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
+            "description": "This data set contains the NEAR magnetometer (MAG) data for the EROS/ORBIT phase. The data set begins on 2000-01-11T00:00:00.000 and ends 2001-02-12T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw magnetometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-2-edr-eros-orbit-v1.0_cunr-xuwv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-2-EDR-EROS%2FORBIT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-2-edr-eros-orbit-v1.0_cunr-xuwv",
-            "description": "This data set contains the NEAR magnetometer (MAG) data for the EROS/ORBIT phase. The data set begins on 2000-01-11T00:00:00.000 and ends 2001-02-12T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw magnetometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
-            "title": "NEAR MAG DATA FOR EROS/ORBIT",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR MAG DATA FOR EROS/ORBIT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LEISA-3-PLUTO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Linear Etalon Imaging Spectral Array                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-leisa-3-pluto-v1.0_cunt-yuzk",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "pluto",
                 "charon",
                 "new horizons"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LEISA-3-PLUTO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-leisa-3-pluto-v1.0_cunt-yuzk",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Linear Etalon Imaging Spectral Array                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      LEISA PLUTO ENCOUNTER                                                   \n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      LEISA PLUTO ENCOUNTER                                                   \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FX-ALICE-2-EAR1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 2 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first earth swing-by phase of the Rosetta mission, which occurred 2004-10-17 to 2005-04-04.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-x-alice-2-ear1-v1.0_cuq3-w4yv",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "international rosetta mission",
                 "unknown",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FX-ALICE-2-EAR1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-x-alice-2-ear1-v1.0_cuq3-w4yv",
-            "description": "This data set contains CODMAC level 2 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first earth swing-by phase of the Rosetta mission, which occurred 2004-10-17 to 2005-04-04.",
-            "title": "ROSETTA-ORBITER CAL/CHECK ALICE 2 EAR1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL/CHECK ALICE 2 EAR1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_ant_phase_map_meta_gps_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Jet Propulsion Laboratory, JPL GDGPS GPS antenna phase maps meta data product, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/GDGPS_ant_phase_map_meta_gps_001",
-            "issued": "1992-01-01",
-            "temporal": "2023-10-01T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "keyword": [
-                "geodetics",
-                "gravity/gravitational field",
-                "earth science",
-                "tectonics",
-                "solid earth"
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
-            "identifier": "C2761694705-CDDIS",
             "description": "This product contains file names and URLs to files containing antenna phase map data used in the real-time GPS POD processing. In particular, the IGS ANTEX file name used for the processing is provided. Additional meta data items may include information that identifies the real-time filter source populating the GPS real-time POD products (see \"pos\", \"quat\", and \"tdp\" products). The product is generated at JPL's Global Differential GPS Operations Centers.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS daily antenna phase maps (meta data, 24-hour files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_ant_phase_map_meta_gps_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_ant_phase_map_meta_gps_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -614347,101 +614326,124 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2761694705-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "geodetics",
+                "gravity/gravitational field",
+                "earth science",
+                "tectonics",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_ant_phase_map_meta_gps_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-10-01T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS daily antenna phase maps (meta data, 24-hour files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-MAG-2-PKT-J0-RAW-PKTS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains magnetic field vectors acquired by the Galileo magnetometer at the Io flyby on Dec 7 (341), 1995 and for the remainder of the mission after the Phase 2 flight Software load in May 1996. Packetized data replaced the Experimenter Data Records (EDRs) that were the raw data product in Phase 1. These are raw data provided in their original packet form. Processing done internal to the instrument remains in the data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-mag-2-pkt-j0-raw-pkts-v1.0_cuq9-k746",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "galileo",
                 "io",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-MAG-2-PKT-J0-RAW-PKTS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-mag-2-pkt-j0-raw-pkts-v1.0_cuq9-k746",
-            "description": "This data set contains magnetic field vectors acquired by the Galileo magnetometer at the Io flyby on Dec 7 (341), 1995 and for the remainder of the mission after the Phase 2 flight Software load in May 1996. Packetized data replaced the Experimenter Data Records (EDRs) that were the raw data product in Phase 1. These are raw data provided in their original packet form. Processing done internal to the instrument remains in the data set.",
-            "title": "GO JUP EDITED MAG RAW PHASE 2 PACKETS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUP EDITED MAG RAW PHASE 2 PACKETS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-TAXONOMY-V5.0",
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
+            "description": "This data set is a collection of asteroid taxonomic classifications from various classification methods, collected from the literature.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-taxonomy-v5.0_curw-efx4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-TAXONOMY-V5.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-taxonomy-v5.0_curw-efx4",
-            "description": "This data set is a collection of asteroid taxonomic classifications from various classification methods, collected from the literature.",
-            "title": "ASTEROID TAXONOMY V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID TAXONOMY V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-CUBE-V1.1",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-cube-v1.1_cutf-yy8v",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "titan",
                 "pandora",
@@ -614468,604 +614470,583 @@
                 "telesto",
                 "tethys"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-CUBE-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-cube-v1.1_cutf-yy8v",
-            "description": "Spectrographic observations of Jupiter, Saturnian rings, satellites, atmospheres and the interplanetary medium in the far and extreme ultraviolet.",
-            "title": "CASSINI ORBITER SATURN UVIS SPATIAL SPECTRAL IMAGE CUBE 1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER SATURN UVIS SPATIAL SPECTRAL IMAGE CUBE 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/A9O02ZH0J94R",
             "citation": "Kai Yang. 2017-06-20. OMPS_NPP_NMSO2_L2. Version 2. OMPS-NPP L2 NM Sulfur Dioxide (SO2) Total and Tropospheric Column swath orbital V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/A9O02ZH0J94R. https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMSO2_L2_2.html. Digital Science Data.",
-            "issued": "2017-06-20",
-            "temporal": "2012-01-26T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-20",
-            "references": [
-                "https://doi.org/10.1029/2008GL036036"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAI YANG, PH. D",
                 "hasEmail": "mailto:kai.yang.1@nasa.gov"
             },
+            "creator": "Kai Yang",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1396070103-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMPS-NPP L2 NM Sulfur Dioxide (SO2) Total and Tropospheric Column swath orbital collection 2 version 2.0 product contains the retrieved sulfur dioxide (SO2) measured by the Ozone Mapping and Profiling Suite (OMPS) Nadir-Mapper (NM) sensor on the Suomi-NPP satellite. A direct vertical column fitting (DVCF) algorithm is used to retrieve the SO2 total column amount and column amounts in the lower (centered at 2.5 km), middle (centered at 7.5 km) and upper (centered at 11 km) troposphere, as well as the lower stratosphere (centered at 16 km).\n\nEach granule contains data from the daylight portion for a single orbit or about 50 minutes. Spatial coverage is global (-90 to  90 degrees latitude), and there are about 14 orbits per day each with a swath width of 2600 km. There are 35 pixels in the cross-track direction, with a pixel resolution of about 50 km x 50 km at nadir. The files are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_NPP_NMSO2_L2",
-            "creator": "Kai Yang",
-            "graphic-preview-description": "OMPS Logo",
-            "title": "OMPS-NPP L2 NM Sulfur Dioxide (SO2) Total and Tropospheric Column swath orbital V2 (OMPS_NPP_NMSO2_L2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMSO2_L2_2.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FA9O02ZH0J94R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FA9O02ZH0J94R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMSO2_L2_2.jpeg",
-                    "description": "OMPS Logo",
                     "@type": "dcat:Distribution",
+                    "description": "OMPS Logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMSO2_L2_2.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMSO2_L2_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMSO2_L2_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMSO2_L2.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMSO2_L2.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NMSO2_L2.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NMSO2_L2.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMSO2_L2_2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMSO2_L2_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMSO2_L2.2/doc/README.OMPS_NPP_NMSO2_L2.2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMSO2_L2.2/doc/README.OMPS_NPP_NMSO2_L2.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://jointmission.gsfc.nasa.gov/",
-                    "description": "Joint Polar Satellite System (JPSS) mission home page",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) mission home page",
+                    "downloadURL": "https://jointmission.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "OMPS Logo",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMSO2_L2_2.jpeg",
+            "identifier": "C1396070103-GES_DISC",
+            "issued": "2017-06-20",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/A9O02ZH0J94R",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-06-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2008GL036036"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMPS_NPP_NMSO2_L2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-26T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-NPP L2 NM Sulfur Dioxide (SO2) Total and Tropospheric Column swath orbital V2 (OMPS_NPP_NMSO2_L2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPZDZYELYG1A",
             "citation": "Sheffield, J. at Princeton University,  NASA/GSFC/GES_DISC. 2018-11-01. PET_PU_3H025. Version 001. RM-OBS/PU Potential Evapotranspiration and Supporting Forcing L4 3-hourly 0.25x0.25 degree V001. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPZDZYELYG1A. https://disc.gsfc.nasa.gov/datacollection/PET_PU_3H025_001.html. Digital Science Data.",
-            "issued": "2018-11-15",
-            "temporal": "1984-01-01T00:00:00Z/2006-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-15",
-            "references": [
-                "https://doi.org/10.1175/JCLI3790.1"
-            ],
-            "keyword": [
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SUHUNG SHEN",
                 "hasEmail": "mailto:suhung.shen@nasa.gov"
             },
+            "creator": "Sheffield, J. at Princeton University,  NASA/GSFC/GES_DISC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1575363595-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Princeton University MEaSUREs Potential Evapotranspiration (PET) dataset provides a set of estimates of PET based on near surface meteorology and surface radiation data derived from a combination of reanalysis, satellite and gridded gauge data. The rationale of the project is to reduce the error from the input meteorological forcing and provide a variety of widely-used PET methods for different research and application purposes.\n\nPET is estimated using three methods: Penman open-water method (Penman), Priestley-Taylor method (PT), Reference crop evapotranspiration using the UN Food and Agricultural Organization approach (FAO). The Penman equation assumes PET occurs from an open water surface and calculates PET based on observations of surface net radiation, near-surface air temperature, wind speed, and specific humidity (Shuttleworth, 1993). The PT equation calculates PET based on surface net radiation and near-surface air temperature and does not account for the aerodynamic component (Priestley and Taylor, 1972). The FAO equation is a specific application of the Penman-Monteith equation for crop and short-grass reference surfaces and is based on surface net radiation, near-surface air temperature, wind speed, and specific humidity (Allen, 1998). \n\nThis first version of dataset is estimated at a 3 hourly temporal resolution and 0.25x0.25 degrees spatial resolution globally, spanning the 23-year period 1984-2006. Datasets are stored as a 3-dimensional array with dimension 720 x 1440 x 8 for each day, in NetCDF-4 format.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "PET_PU_3H025",
-            "creator": "Sheffield, J. at Princeton University,  NASA/GSFC/GES_DISC",
-            "graphic-preview-description": "Sample images of RM-OBS/PU Potential Evapotranspiration 3-hourly 0.25x0.25 Degree [mm] Version 001 for Jan 01, 1984 at 00Z (left) and 12Z (right).",
-            "title": "RM-OBS/PU Potential Evapotranspiration and Supporting Forcing L4 3-hourly 0.25x0.25 degree V001 (PET_PU_3H025) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PET_PU_3H025_001.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPZDZYELYG1A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPZDZYELYG1A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PET_PU_3H025_001.png",
-                    "description": "Sample images of RM-OBS/PU Potential Evapotranspiration 3-hourly 0.25x0.25 Degree [mm] Version 001 for Jan 01, 1984 at 00Z (left) and 12Z (right).",
                     "@type": "dcat:Distribution",
+                    "description": "Sample images of RM-OBS/PU Potential Evapotranspiration 3-hourly 0.25x0.25 Degree [mm] Version 001 for Jan 01, 1984 at 00Z (left) and 12Z (right).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PET_PU_3H025_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/PET_PU_3H025_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/PET_PU_3H025_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/PET_PU/PET_PU_3H025.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/PET_PU/PET_PU_3H025.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=PET_PU_3H025",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=PET_PU_3H025",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/PET_PU/PET_PU_3H025.001/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/PET_PU/PET_PU_3H025.001/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/PET_PU/PET_PU_3H025.001/doc/README.PET_PU_3H025_V001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/PET_PU/PET_PU_3H025.001/doc/README.PET_PU_3H025_V001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://hydrology.princeton.edu/data.pgf.php",
-                    "description": "Hydrology Project Web Site at Princeton University",
                     "@type": "dcat:Distribution",
+                    "description": "Hydrology Project Web Site at Princeton University",
+                    "downloadURL": "http://hydrology.princeton.edu/data.pgf.php",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto",
-                    "description": "How to read and plot the data.",
                     "@type": "dcat:Distribution",
+                    "description": "How to read and plot the data.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "graphic-preview-description": "Sample images of RM-OBS/PU Potential Evapotranspiration 3-hourly 0.25x0.25 Degree [mm] Version 001 for Jan 01, 1984 at 00Z (left) and 12Z (right).",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PET_PU_3H025_001.png",
+            "identifier": "C1575363595-GES_DISC",
+            "issued": "2018-11-15",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPZDZYELYG1A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-11-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1175/JCLI3790.1"
+            ],
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "PET_PU_3H025",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "1984-01-01T00:00:00Z/2006-12-31T23:59:59Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RM-OBS/PU Potential Evapotranspiration and Supporting Forcing L4 3-hourly 0.25x0.25 degree V001 (PET_PU_3H025) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-ROVER-6-RDR-PLACES-V1.0",
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
-                "mars science laboratory",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rover-6-rdr-places-v1.0_cv2h-r5bf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-ROVER-6-RDR-PLACES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rover-6-rdr-places-v1.0_cv2h-r5bf",
-            "description": "NULL",
-            "title": "MSL MARS ROVER 6 RDR PLACES ROVER\n                                      MOTION COUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS ROVER 6 RDR PLACES ROVER\n                                      MOTION COUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-TVS-2-RDR-HALLEY-V1.0",
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
-                "vega 1"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "For the TV SYSTEM, 95 images were sent as a 7-d FITS file with little information in the FITS headers. In addition, to the size of the image (NAXIS1 and NAXIS2), the values for NAXIS3 and NAXIS4 were labeled 'TIME' interpreted as exposure time in seconds. The following procedure was used to convert NAXIS3 information:",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-tvs-2-rdr-halley-v1.0_cv3c-yrzf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "vega 1"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-TVS-2-RDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-tvs-2-rdr-halley-v1.0_cv3c-yrzf",
-            "description": "For the TV SYSTEM, 95 images were sent as a 7-d FITS file with little information in the FITS headers. In addition, to the size of the image (NAXIS1 and NAXIS2), the values for NAXIS3 and NAXIS4 were labeled 'TIME' interpreted as exposure time in seconds. The following procedure was used to convert NAXIS3 information:",
-            "title": "VEGA1 TV SYSTEM IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VEGA1 TV SYSTEM IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA323",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRH3SPM. Version 006. AIRS/Aqua L3 Monthly Support Monthly Product (AIRS+AMSU+HSB) 1 degree x 1 degree V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA323. https://disc.gsfc.nasa.gov/datacollection/AIRH3SPM_006.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2003-03-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-03-01",
-            "keyword": [
-                "clouds",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "earth science",
-                "land surface",
-                "oceans",
-                "ocean temperature",
-                "precipitation",
-                "surface radiative properties",
-                "surface thermal properties",
-                "atmospheric radiation",
-                "atmospheric chemistry",
-                "atmosphere",
-                "altitude",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1238517247-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The L3 support products are similar to the L3 standard products but contain fields which are not fully validated, or are inputs or intermediary values. Because no quality control information is available for some of these fields, values from failed retrievals may be included.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRH3SPM",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "title": "AIRS/Aqua L3 Monthly Support Product (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3SPM) at GES DISC",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (With HSB)\".",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3SPM_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA323",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA323",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3SPM_006.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (With HSB)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (With HSB)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3SPM_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRH3SPM_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRH3SPM_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRH3SPM.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRH3SPM.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRH3SPM.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRH3SPM.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRH3SPM+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRH3SPM+006",
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
                 }
             ],
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (With HSB)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3SPM_006.png",
+            "identifier": "C1238517247-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "clouds",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "earth science",
+                "land surface",
+                "oceans",
+                "ocean temperature",
+                "precipitation",
+                "surface radiative properties",
+                "surface thermal properties",
+                "atmospheric radiation",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA323",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRH3SPM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2003-03-01T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 Monthly Support Product (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3SPM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-SW-3-FGM-CAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract                                                                    ========                                                                    This data set consists of the Juno FGM calibrated observations. The       FGM sensor block uses two miniature ring-core fluxgate sensors to         measure the magnetic field in three components of the vector field        There are multiple FGM data products to accomodate different              coordinate systems.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-sw-3-fgm-cal-v1.0_cvcs-xy6f",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "jupiter",
                 "juno"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-SW-3-FGM-CAL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-sw-3-fgm-cal-v1.0_cvcs-xy6f",
-            "description": "Abstract                                                                    ========                                                                    This data set consists of the Juno FGM calibrated observations. The       FGM sensor block uses two miniature ring-core fluxgate sensors to         measure the magnetic field in three components of the vector field        There are multiple FGM data products to accomodate different              coordinate systems.",
-            "title": "JUNO FGM CALIBRATED DATA SW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "JUNO FGM CALIBRATED DATA SW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/157",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Condit, R., D.M. Windsor, and S.P. Hubbell. 2013. NPP Tropical Forest: Barro Colorado, Panama, 1969-1990, R1 . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/157",
-            "issued": "2023-08-17",
-            "temporal": "1929-01-01T00:00:00Z/2000-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "ecological dynamics",
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
-            "identifier": "C2752547387-ORNL_CLOUD",
             "description": "This data set contains three ASCII files (.txt format). One file provides net primary productivity (NPP) data for the moist lowland tropical forest on Barro Colorado Island, Panama. NPP estimates are based on field measurements of litterfall accumulation, tree growth and mortality, and herbivory. Above-ground biomass and LAI are also reported. The other two files provide climate data recorded onsite.Annual litterfall accumulation (leaf + twig + other litterfall) averaged 1,064 g/m2/year, excluding losses to herbivory, on the central plateau of the island and in the Lutz catchment (1969-1979) and 1,246 g/m2/year at Poacher's Peninsula (1986-1990). Herbivory due to insects (about 50 g/m2/year) was estimated from leaf litterfall (1974-1977) by measuring holes and gaps in fallen leaves. An additional 30 g/m2/year may be lost to vertebrate herbivores which leave no identifiable traces in litter traps. Coarse wood litterfall due to tree damage may represent an additional 46 g/m2/year. Above-ground biomass averaged 27,425 g/m2 based on inventory data collected every 5 years from 1985 to 2000 and allometric regression equations. Tree growth of 554 g/m2/year was based on above-ground biomass changes during the three census intervals. Tree mortality of 2-3% was estimated by recording dead or missing trees (1982-1990). LAI of 7.3 was based on the average area of leaves that fell per area of ground per year. Overall, above-ground NPP for Barro Colorado Island was estimated at 1,800 g/m2/year.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Tropical Forest: Barro Colorado, Panama, 1969-1990, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F157",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F157",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_BRR/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_BRR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BRR.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BRR.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/157",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/157",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_BRR/comp/NPP_BRR.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_BRR/comp/NPP_BRR.pdf",
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
+            "identifier": "C2752547387-ORNL_CLOUD",
+            "issued": "2023-08-17",
+            "keyword": [
+                "ecological dynamics",
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/157",
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
             "spatial": "9.15 -79.85",
+            "temporal": "1929-01-01T00:00:00Z/2000-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Tropical Forest: Barro Colorado, Panama, 1969-1990, R1"
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
-                "rss",
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
-            "identifier": "NASA-571",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (96)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -615073,1113 +615054,1110 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-571",
+            "issued": "2018-06-25",
+            "keyword": [
+                "rss",
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
+            "title": "PDS Odyssey Radio Science Data (96)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-ESC4-V1.0",
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
+            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the comet escort 4 phase (ESC4). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 22 Oct 2015 and 31 Dec 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-esc4-v1.0_cvkx-6jqz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-ESC4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-esc4-v1.0_cvkx-6jqz",
-            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the comet escort 4 phase (ESC4). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 22 Oct 2015 and 31 Dec 2015.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 3 ESC4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 3 ESC4 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IWGD4WFMCQNW",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx17 Boise State University Terrestrial Laser Scanner (TLS) Point Cloud V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/IWGD4WFMCQNW.",
-            "issued": "2016-09-26",
-            "temporal": "2016-09-26T00:00:00Z/2017-02-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-02-25",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C1586132415-NSIDC_ECS",
             "description": "This data set contains terrestrial laser scanner (TLS) point cloud data collected as part of the 2017 SnowEx campaign in Grand Mesa, Colorado. Data were collected under both snow-off (September 2016) and snow-on (February 2017) conditions, at both open and forested locations. Multiple scans were conducted at each site and registered together using common targets. Each point contains X, Y, and Z coordinates (Easting, Northing, and Elevation), as well as intensity (i). These TLS data can be used to determine snow depth and explore the interactions between snow and vegetation.",
-            "title": "SnowEx17 Boise State University Terrestrial Laser Scanner (TLS) Point Cloud V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIWGD4WFMCQNW",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIWGD4WFMCQNW",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_TLS_PC_BSU.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_TLS_PC_BSU.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?tag_key=gov.nasa.eosdis&p=C1586132415-NSIDC_ECS&m=34.787109375%21-108.8173828125%215%211%210%210%2C2&tl=1532888258%214%21%21&q=SNEX17_TLS_PC_BSU&ok=SNEX17_TLS_PC_BSU&ac=true",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?tag_key=gov.nasa.eosdis&p=C1586132415-NSIDC_ECS&m=34.787109375%21-108.8173828125%215%211%210%210%2C2&tl=1532888258%214%21%21&q=SNEX17_TLS_PC_BSU&ok=SNEX17_TLS_PC_BSU&ac=true",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_TLS_PC_BSU/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_TLS_PC_BSU/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_TLS_PC_BSU.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_TLS_PC_BSU.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?tag_key=gov.nasa.eosdis&p=C1586132415-NSIDC_ECS&m=34.787109375%21-108.8173828125%215%211%210%210%2C2&tl=1532888258%214%21%21&q=SNEX17_TLS_PC_BSU&ok=SNEX17_TLS_PC_BSU&ac=true",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?tag_key=gov.nasa.eosdis&p=C1586132415-NSIDC_ECS&m=34.787109375%21-108.8173828125%215%211%210%210%2C2&tl=1532888258%214%21%21&q=SNEX17_TLS_PC_BSU&ok=SNEX17_TLS_PC_BSU&ac=true",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_TLS_PC_BSU/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_TLS_PC_BSU/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IWGD4WFMCQNW",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/IWGD4WFMCQNW",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IWGD4WFMCQNW",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/IWGD4WFMCQNW",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1586132415-NSIDC_ECS",
+            "issued": "2016-09-26",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "lidar"
+            ],
+            "landingPage": "https://doi.org/10.5067/IWGD4WFMCQNW",
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
+            "title": "SnowEx17 Boise State University Terrestrial Laser Scanner (TLS) Point Cloud V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_daily_landonly_local_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_daily_landonly_local_1. https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_daily_landonly_local_1.",
-            "issued": "2023-10-27",
-            "temporal": "1983-07-01T00:00:00Z/1987-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1987-12-31",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
-                "clouds",
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
-            "identifier": "C2791476513-LARC_ASDC",
             "description": "GEWEXSRB_Rel4_1-IP_Longwave_daily_landonly_local is the Global Energy and Water Exchanges (GEWEX) Surface Radiation Budget (SRB) Integrated Product (Rel-4) Longwave Daily Average by Local Land-only data product. It contains land-only global fields of 26 longwave surface, Top of Atmosphere (TOA), and atmospheric profile radiative parameters derived with the Longwave algorithm of the NASA World Climate Research Programme/Global Energy and Water-Cycle Experiment (WCRP/GEWEX) Surface Radiation Budget (SRB) Project. This version is an extension of Release 4-Integrated Product with land-only fluxes due to a missing key input from the main data set. The fluxes include all-sky, clear-sky, and pristine-sky TOA upward fluxes (outgoing longwave radiation, OLR), all-sky, clear-sky, and pristine-sky upward and downward fluxes at the tropopause, 200hPa, 500hPa, and surface. A status flag of filled cloud properties is also included. Inputs to the longwave algorithm are cloud information based on ISCCP HXS, meteorology from ISCCP nnHIRS, Landflux surface, and MERRA-2 conditionally. The temporal range is July 1983 through December 1987. These data are averaged by local solar time from 3-hourly values. Data collection for this product is complete.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "GEWEX SRB Integrated Product (Rel-4_1) Longwave Daily Average by Local Land-only Fluxes",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/gewex-rfa.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4_1-IP_Longwave_daily_landonly_local_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4_1-IP_Longwave_daily_landonly_local_1",
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
-                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_daily_landonly_local_1",
-                    "description": "DOI data set landing page for GEWEXSRB_Rel4_1-IP_Longwave_daily_landonly_local_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for GEWEXSRB_Rel4_1-IP_Longwave_daily_landonly_local_1",
+                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_daily_landonly_local_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_Public_Release_Announcement.pdf",
-                    "description": "SRB Release 4 Announcement",
                     "@type": "dcat:Distribution",
+                    "description": "SRB Release 4 Announcement",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_Public_Release_Announcement.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_ATBD.pdf",
-                    "description": "SRB Rel4-IP Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "SRB Rel4-IP Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/SRB",
-                    "description": "ASDC Data and Information for SRB",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for SRB",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/SRB",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2791476513-LARC_ASDC",
-                    "description": "Earthdata Search for GEWEXSRB_Rel4_1-IP_Longwave_daily_landonly_local_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for GEWEXSRB_Rel4_1-IP_Longwave_daily_landonly_local_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2791476513-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/gewex-rfa.png",
-                    "description": "Mission Logo",
                     "@type": "dcat:Distribution",
+                    "description": "Mission Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/gewex-rfa.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4_1-IP/Longwave_daily_landonly_local_1/",
-                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4_1-IP_Longwave_daily_landonly_local_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4_1-IP_Longwave_daily_landonly_local_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4_1-IP/Longwave_daily_landonly_local_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4_1-IP/Longwave_daily_landonly_local_1/contents.html",
-                    "description": "OPeNDAP data access for GEWEXSRB_Rel4_1-IP_Longwave_daily_landonly_local_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GEWEXSRB_Rel4_1-IP_Longwave_daily_landonly_local_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4_1-IP/Longwave_daily_landonly_local_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/gewex-rfa.png",
+            "identifier": "C2791476513-LARC_ASDC",
+            "issued": "2023-10-27",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_daily_landonly_local_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1987-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1983-07-01T00:00:00Z/1987-12-31T23:59:59.999Z",
             "theme": [
                 "SRB",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEWEX SRB Integrated Product (Rel-4_1) Longwave Daily Average by Local Land-only Fluxes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67P-M28-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-04-05T23:25:00.000 to 2016-05-03T23:25:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67p-m28-reflect-v1.0_cvv3-wcme",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67P-M28-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67p-m28-reflect-v1.0_cvv3-wcme",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-04-05T23:25:00.000 to 2016-05-03T23:25:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP028 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP028 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-S-SW-CPI-4-SUMM-1HR-V1.0",
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
-                "pioneer 11",
-                "saturn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 11 cruise Charged Particle Instrument (CPI) 1 hour count data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-s-sw-cpi-4-summ-1hr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pioneer 11",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-S-SW-CPI-4-SUMM-1HR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-s-sw-cpi-4-summ-1hr-v1.0",
-            "description": "Pioneer 11 cruise Charged Particle Instrument (CPI) 1 hour count data.",
-            "title": "P11 SATURN SOLAR WIND CPI CRUISE 1 HOUR\n                                      COUNT DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P11 SATURN SOLAR WIND CPI CRUISE 1 HOUR\n                                      COUNT DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-05-13. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0005.",
-            "issued": "1999-05-13",
-            "temporal": "1998-05-11T00:00:00Z/1998-06-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-02",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "microwave"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WAYNE SCHUBERT",
                 "hasEmail": "mailto:waynes@rayleigh.atmos.colostate.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000960-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.FIRE ACE Millimeter-wave Imaging Radiometer flown aboard the ER2.",
-            "title": "First ISCCP Regional Experiment (FIRE) Arctic Cloud Experiment (ACE) ER-2 Millimeter-wave Imaging Radiometer (MIR)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0005",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000960-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_ACE_ER2_MIR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_ACE_ER2_MIR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000960-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_er2_mir.f",
-                    "description": "Readme to Read FIRE_ACE_ER2_MIR data files for a given flight and print selected parameters for every 1000th record - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to Read FIRE_ACE_ER2_MIR data files for a given flight and print selected parameters for every 1000th record - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_er2_mir.f",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/data/logs/er-2/ace_ER-2_fltloglist.pdf",
-                    "description": "FIRE-ACE ER-2 Flight Logs and Flight Track Images",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE-ACE ER-2 Flight Logs and Flight Track Images",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/data/logs/er-2/ace_ER-2_fltloglist.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/fire_ace_er2_mir.readme",
-                    "description": "Readme Information about Millimeter-wave Imaging Radiometer (MIR) flown onboard the ER2 aircraft during the FIRE-ACE field campaign",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about Millimeter-wave Imaging Radiometer (MIR) flown onboard the ER2 aircraft during the FIRE-ACE field campaign",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/fire_ace_er2_mir.readme",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0005",
-                    "description": "DOI data set landing page for FIRE_ACE_ER2_MIR_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_ACE_ER2_MIR_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0005",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/index.pdf",
-                    "description": "FIRE Arctic Cloud Experiment (FIRE.ACE) Home Page Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Arctic Cloud Experiment (FIRE.ACE) Home Page Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/index.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ace_ampr",
-                    "description": "Readme Information about the data provided by the AMPR flown onboard the ER2 aircraft during the FIRE ACE field campaign",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the data provided by the AMPR flown onboard the ER2 aircraft during the FIRE ACE field campaign",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ace_ampr",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_ampr.f",
-                    "description": "Program to read SRB Release 3 Shortwave 3 Hourly nc - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Program to read SRB Release 3 Shortwave 3 Hourly nc - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_ampr.f",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_ER2_MIR/",
-                    "description": "ASDC Direct Data Download for FIRE_ACE_ER2_MIR_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_ACE_ER2_MIR_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_ER2_MIR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_ER2_MIR/contents.html",
-                    "description": "OPeNDAP data access for FIRE_ACE_ER2_MIR_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_ACE_ER2_MIR_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_ER2_MIR/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000960-LARC_ASDC",
+            "issued": "1999-05-13",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0005",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>34.9 -174.31 34.9 -117.8 78.2 -117.8 78.2 -174.31 34.9 -174.31</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1998-05-11T00:00:00Z/1998-06-06T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Arctic Cloud Experiment (ACE) ER-2 Millimeter-wave Imaging Radiometer (MIR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR4A-MAG-V1.0",
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
+            "description": "This archive contains level 3 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the CR4A (cruise 4A) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr4a-mag-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR4A-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr4a-mag-v1.0",
-            "description": "This archive contains level 3 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the CR4A (cruise 4A) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 3 CR4A MAG\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL ROMAP 3 CR4A MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-09-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1.",
-            "issued": "2021-03-19",
-            "temporal": "2013-08-12T00:00:00Z/2013-09-22T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-20",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds"
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
-            "identifier": "C2119341668-LARC_ASDC",
             "description": "SEAC4RS_Cloud_AircraftInSitu_Learjet_Data are in-situ cloud data collected onboard the Learjet aircraft during the Studies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEA4CRS) airborne field study. Data collection for this product is complete.\r\n\r\nStudies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEAC4RS) airborne field study was conducted in August and September of 2013. The field operation was based in Houston, Texas. The primary SEAC4RS science objectives are: to determine how pollutant emissions are redistributed via deep convection throughout the troposphere; to determine the evolution of gases and aerosols in deep convective outflow and the implications for UT/LS chemistry; to identify the influences and feedbacks of aerosol particles from anthropogenic pollution and biomass burning on meteorology and climate through changes in the atmospheric heat budget (i.e., semi-direct effect) or through microphysical changes in clouds (i.e., indirect effects); and lastly, to serve as a calibration and validation test bed for future satellite instruments and missions.\r\n\r\nThe airborne observational data were collected from three aircraft platforms: the NASA DC-8, ER-2, and SPEC LearJet. Both the NASA DC-8 and ER-2 aircraft were instrumented for comprehensive in-situ and remote sensing measurements of the trace gas, aerosol properties, and cloud properties. In addition, radiative fluxes and meteorological parameters were also recorded. The NASA DC-8 was mostly responsible for tropospheric sampling, while the NASA ER-2 was operating in the lower stratospheric regime. The SPEC LearJet was dedicated to in-situ cloud characterizations. To accomplish the science objectives, the flight plans were designed to investigate the influence of biomass burning and pollution, their temporal evolution, and ultimately, impacts on meteorological processes which can, in turn, feedback on regional air quality. With respect to meteorological feedbacks, the opportunity to examine the impact of polluting aerosols on cloud properties and dynamics was of particular interest.",
-            "title": "SEAC4RS Learjet Aircraft In-Situ Cloud Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
-                    "description": "DOI data set landing page for SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341668-LARC_ASDC",
-                    "description": "Earthdata Search for SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341668-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/Cloud_AircraftInSitu_Learjet_Data_1/",
-                    "description": "ASDC Direct Data Download for SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/Cloud_AircraftInSitu_Learjet_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2119341668-LARC_ASDC",
+            "issued": "2021-03-19",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Cloud_AircraftInSitu_Learjet_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>27.0 -100.0 27.0 -85.0 38.0 -85.0 38.0 -100.0 27.0 -100.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-08-12T00:00:00Z/2013-09-22T23:59:59.999Z",
             "theme": [
                 "SEAC4RS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEAC4RS Learjet Aircraft In-Situ Cloud Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0103",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-25. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0103.",
-            "issued": "1999-10-20",
-            "temporal": "1991-11-22T00:00:00Z/1991-12-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-11",
-            "keyword": [
-                "infrared wavelengths",
-                "atmosphere",
-                "spectral/engineering",
-                "visible wavelengths",
-                "earth science",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EDWIN ELORANTA",
                 "hasEmail": "mailto:eloranta@lidar.meteor.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001189-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.This data set contains images of cirrus clouds advected over the HSRL during FIRE Cirrus 2 in Coffeyville, Kansas. These images consist of both the lidar backscatter and the depolarization ratio of backscatter radiation.",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus 2 High Spectral Resolution Lidar (HSRL) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0103",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0103",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001189-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_HSRL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_HSRL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001189-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_hsrl_vil_dataset.pdf",
-                    "description": "FIRE Cirrus 2 High Spectral Resolution Lidar (HSRL)/Volume Imaging Lidar (VIL) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 High Spectral Resolution Lidar (HSRL)/Volume Imaging Lidar (VIL) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_hsrl_vil_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_hsrl.txt",
-                    "description": "FIRE II Data with Altitude vs. Time (RTI) and Cirrus Scan gif pictures Readme",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE II Data with Altitude vs. Time (RTI) and Cirrus Scan gif pictures Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_hsrl.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0103",
-                    "description": "DOI data set landing page for FIRE_CI2_HSRL_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_HSRL_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0103",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire2_cirrus/mission_summaries.html",
-                    "description": "ASDC List of FIRE II - Cirrus Mission Summaries Available",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of FIRE II - Cirrus Mission Summaries Available",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire2_cirrus/mission_summaries.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_HSRL/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_HSRL_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_HSRL_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_HSRL/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_HSRL/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_HSRL_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_HSRL_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_HSRL/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001189-LARC_ASDC",
+            "issued": "1999-10-20",
+            "keyword": [
+                "infrared wavelengths",
+                "atmosphere",
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0103",
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
             "spatial": "37.1 -95.57",
+            "temporal": "1991-11-22T00:00:00Z/1991-12-06T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus 2 High Spectral Resolution Lidar (HSRL) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945873-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "oceans",
-                "ocean temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sdps@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "OB.DAAC"
-            },
-            "identifier": "C1641945873-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Global Mapped 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3SMI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3SMI/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/NSST/R2019.0",
-                    "description": "MODIS-Aqua L3M 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3M 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/NSST/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Aqua MODIS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Aqua MODIS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1641945873-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945873-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "OB.DAAC"
+            },
             "spatial": "-180.0 90.0 -180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua MODIS Global Mapped 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/BMX7AJZSHXKX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX04 Surface Roughness Data, Sonora, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/BMX7AJZSHXKX.",
-            "issued": "2004-07-30",
-            "temporal": "2004-07-30T00:00:00Z/2004-08-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-08-25",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "topography"
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
-            "identifier": "C1386205589-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThe data set SMEX04 Surface Roughness Data is comprised of data collected over the regional study areas of Arizona, USA and Sonora, Mexico as part of the 2004 Soil Moisture Experiment (SMEX04).",
-            "title": "SMEX04 Surface Roughness Data, Sonora, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FBMX7AJZSHXKX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FBMX7AJZSHXKX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/ancillary_data/surface_roughness/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/ancillary_data/surface_roughness/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/ancillary_data/surface_roughness/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/ancillary_data/surface_roughness/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/BMX7AJZSHXKX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/BMX7AJZSHXKX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/BMX7AJZSHXKX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/BMX7AJZSHXKX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205589-NSIDCV0",
+            "issued": "2004-07-30",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/BMX7AJZSHXKX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-08-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-110.704 29.8521 -109.7159 32.0809",
+            "temporal": "2004-07-30T00:00:00Z/2004-08-25T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX04 Surface Roughness Data, Sonora, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NSGDR-L2R00",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/JPL/PO.DAAC. 2006-02-20. NSCAT High Resolution R-MGDR, Selected Ocean Wind Vectors (JPL). Version 2. NSCAT High Resolution R-MGDR, Selected Ocean Wind Vectors (JPL). PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/NSGDR-L2R00. https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/nscat/doc/l25_usersguide.pdf. NASA/JPL/PO.DAAC, PO.DAAC, 2006-02-20, NSCAT High Resolution R-MGDR, Selected Ocean Wind Vectors (JPL), https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/nscat/doc/l25_usersguide.pdf.",
-            "issued": "2009-09-10",
-            "temporal": "1996-09-15T00:00:00Z/1997-06-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-01-21",
-            "keyword": [
-                "ocean winds",
-                "earth science",
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
-            "identifier": "C2617226887-POCLOUD",
-            "description": "The NASA Scatterometer (NSCAT) Level 2.5 high-resolution reduced MGDR contains only wind vector data (sigma-0 is excluded) in 25 km wind vector cell (WVC) swaths which contain daily data from ascending and descending passes. Wind vectors are accurate to within 2 m/s (vector speed) and 20 degrees (vector direction). Wind vectors are not considered valid in rain contaminated regions; rain flags and precipitation information are not provided. Data is flagged where measurements are either missing or ambiguous. In the presence of land or sea ice winds values are set to 0. Wind vectors are processed using the NSCAT-2 geophysical model function.",
-            "release-place": "PO.DAAC",
-            "series-name": "NSCAT High Resolution R-MGDR, Selected Ocean Wind Vectors (JPL)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA/JPL/PO.DAAC",
-            "title": "NSCAT High Resolution R-MGDR, Selected Ocean Wind Vectors (JPL)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_W25_RMGDR_V2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NASA Scatterometer (NSCAT) Level 2.5 high-resolution reduced MGDR contains only wind vector data (sigma-0 is excluded) in 25 km wind vector cell (WVC) swaths which contain daily data from ascending and descending passes. Wind vectors are accurate to within 2 m/s (vector speed) and 20 degrees (vector direction). Wind vectors are not considered valid in rain contaminated regions; rain flags and precipitation information are not provided. Data is flagged where measurements are either missing or ambiguous. In the presence of land or sea ice winds values are set to 0. Wind vectors are processed using the NSCAT-2 geophysical model function.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNSGDR-L2R00",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNSGDR-L2R00",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_W25_RMGDR_V2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_W25_RMGDR_V2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/nscat/doc/l25_usersguide.pdf",
-                    "description": "Dataset User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset User Guide",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/nscat/doc/l25_usersguide.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226887-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226887-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226887-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226887-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_W25_RMGDR_V2.jpg",
+            "identifier": "C2617226887-POCLOUD",
+            "issued": "2009-09-10",
+            "keyword": [
+                "ocean winds",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/NSGDR-L2R00",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-01-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "PO.DAAC",
+            "series-name": "NSCAT High Resolution R-MGDR, Selected Ocean Wind Vectors (JPL)",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-09-15T00:00:00Z/1997-06-29T23:59:59.999Z",
             "theme": [
                 "NSCAT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NSCAT High Resolution R-MGDR, Selected Ocean Wind Vectors (JPL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/kepler-ba",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://kepler.nasa.gov/"
-            ],
-            "keyword": [
-                "3d model",
-                "kepler",
-                "satellite",
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
-            "identifier": "NASA-375",
             "description": "The Kepler Mission is specifically designed to survey a portion of our region of the Milky Way galaxy to discover Earth-sized planets in or near the habitable zones of their stars and determine how many of the billions of stars in our galaxy have such planets. Kepler was launched in March 2009. This package includes models of Kepler, the photometer, and the solar array. By Ball Aerospace.",
-            "title": "NASA 3D Models: Kepler Photometer",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -616187,195 +616165,193 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-375",
+            "issued": "2018-06-25",
+            "keyword": [
+                "3d model",
+                "kepler",
+                "satellite",
+                "spacecraft"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/kepler-ba",
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
+                "http://kepler.nasa.gov/"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Kepler Photometer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M18-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m18-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M18-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m18-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP018 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP018 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/cwbs-vsd8",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "sample collection",
-                "nucleic acid sequencing",
-                "sequence assembly",
-                "nucleic acid extraction",
-                "radiation",
-                "library construction"
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
-            "identifier": "nasa_genelab_GLDS-132_cwbs-vsd8",
             "description": "The whole-genome sequences of eight fungal strains that were selected for exposure to microgravity at the International Space Station are presented here. These baseline sequences will help to understand the observed production of novel bioactive compounds.",
-            "title": "Whole genome sequencing and assembly of Eukaryotic microbes isolated from ISS environmental surface Kirovograd region soil Chernobyl Nuclear Power Plant and Chernobyl Exclusion Zone",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-132",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-132",
+                    "mediaType": "text/html",
                     "title": "Whole genome sequencing and assembly of Eukaryotic microbes isolated from ISS environmental surface Kirovograd region soil Chernobyl Nuclear Power Plant and Chernobyl Exclusion Zone"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-132_cwbs-vsd8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "sample collection",
+                "nucleic acid sequencing",
+                "sequence assembly",
+                "nucleic acid extraction",
+                "radiation",
+                "library construction"
+            ],
+            "landingPage": "https://data.nasa.gov/d/cwbs-vsd8",
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
+            "title": "Whole genome sequencing and assembly of Eukaryotic microbes isolated from ISS environmental surface Kirovograd region soil Chernobyl Nuclear Power Plant and Chernobyl Exclusion Zone"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPC/GPROFCLIM/3A-DAY/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFMETOPCMHS_DAY_CLIM. Version 07. GPM MHS on METOP-C (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/MHS/METOPC/GPROFCLIM/3A-DAY/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFMETOPCMHS_DAY_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2018-11-16T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHRISTIAN KUMMEROW",
                 "hasEmail": "mailto:kummerow@atmos.colostate.edu"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264135780-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions are no longer available and have been superseded by Version 07. \n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_3GPROFMETOPCMHS_DAY_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM MHS on METOP-C (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPCMHS_DAY_CLIM) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from  MHS on METOP-C GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFMETOPCMHS_DAY)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFMETOPCMHS_DAY_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPC%2FGPROFCLIM%2F3A-DAY%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPC%2FGPROFCLIM%2F3A-DAY%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFMETOPCMHS_DAY_CLIM_07.png",
-                    "description": "Surface Precipitation from  MHS on METOP-C GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFMETOPCMHS_DAY)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from  MHS on METOP-C GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFMETOPCMHS_DAY)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFMETOPCMHS_DAY_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFMETOPCMHS_DAY_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFMETOPCMHS_DAY_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFMETOPCMHS_DAY_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFMETOPCMHS_DAY_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFMETOPCMHS_DAY_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFMETOPCMHS_DAY_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFMETOPCMHS_DAY_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFMETOPCMHS_DAY_CLIM_07",
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
@@ -616385,134 +616361,170 @@
                     "title": "View this dataset's algorithm theoretical basis document"
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
+            "graphic-preview-description": "Surface Precipitation from  MHS on METOP-C GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFMETOPCMHS_DAY)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFMETOPCMHS_DAY_CLIM_07.png",
+            "identifier": "C2264135780-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPC/GPROFCLIM/3A-DAY/07",
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
+            "series-name": "GPM_3GPROFMETOPCMHS_DAY_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-11-16T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM MHS on METOP-C (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPCMHS_DAY_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/K7Y2D8QQVZ4L",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L2 Radiometer Half-Orbit 36 km EASE-Grid Soil Moisture V009. Version 009. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/K7Y2D8QQVZ4L.",
-            "issued": "2015-03-31",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
-            "keyword": [
-                "spectral/engineering",
-                "soils",
-                "microwave",
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
-            "identifier": "C2938663609-NSIDC_CPRD",
             "description": "This Level-2 (L2) soil moisture product provides estimates of global land surface conditions retrieved by the Soil Moisture Active Passive (SMAP) passive microwave radiometer during 6:00 a.m. descending and 6:00 p.m. ascending half-orbit passes. SMAP L-band brightness temperatures are resampled to an Earth-fixed, global, cylindrical 36 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0) [and made available as the SPL1CTB product], and the gridded brightness temperatures are then used to derive gridded soil moisture data.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP L2 Radiometer Half-Orbit 36 km EASE-Grid Soil Moisture V009",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-197,-70,143,87&l=SMAP_L2_Passive_Night_Soil_Moisture_Option3,SMAP_L2_Passive_Night_Soil_Moisture_Option2,SMAP_L2_Passive_Night_Soil_Moisture_Option1,SMAP_L2_Passive_Day_Soil_Moisture_Option3,SMAP_L2_Passive_Day_Soil_Moisture_Option2,SMAP_L2_Passive_Day_Soil_Moisture_Option1,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FK7Y2D8QQVZ4L",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FK7Y2D8QQVZ4L",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL2SMP+V009",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL2SMP+V009",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938663609-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938663609-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-197%2C-70%2C143%2C87&l=SMAP_L2_Passive_Night_Soil_Moisture_Option3%2CSMAP_L2_Passive_Night_Soil_Moisture_Option2%2CSMAP_L2_Passive_Night_Soil_Moisture_Option1%2CSMAP_L2_Passive_Day_Soil_Moisture_Option3%2CSMAP_L2_Passive_Day_Soil_Moisture_Option2%2CSMAP_L2_Passive_Day_Soil_Moisture_Option1%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-197%2C-70%2C143%2C87&l=SMAP_L2_Passive_Night_Soil_Moisture_Option3%2CSMAP_L2_Passive_Night_Soil_Moisture_Option2%2CSMAP_L2_Passive_Night_Soil_Moisture_Option1%2CSMAP_L2_Passive_Day_Soil_Moisture_Option3%2CSMAP_L2_Passive_Day_Soil_Moisture_Option2%2CSMAP_L2_Passive_Day_Soil_Moisture_Option1%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/K7Y2D8QQVZ4L",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/K7Y2D8QQVZ4L",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/K7Y2D8QQVZ4L",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/K7Y2D8QQVZ4L",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-197,-70,143,87&l=SMAP_L2_Passive_Night_Soil_Moisture_Option3,SMAP_L2_Passive_Night_Soil_Moisture_Option2,SMAP_L2_Passive_Night_Soil_Moisture_Option1,SMAP_L2_Passive_Day_Soil_Moisture_Option3,SMAP_L2_Passive_Day_Soil_Moisture_Option2,SMAP_L2_Passive_Day_Soil_Moisture_Option1,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C2938663609-NSIDC_CPRD",
+            "issued": "2015-03-31",
+            "keyword": [
+                "spectral/engineering",
+                "soils",
+                "microwave",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/K7Y2D8QQVZ4L",
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
+            "title": "SMAP L2 Radiometer Half-Orbit 36 km EASE-Grid Soil Moisture V009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985741-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "Sentinel-1B Dual-pol ground projected high and full resolution metadata",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1327985741-ASF",
             "issued": "2016-08-20",
-            "temporal": "2016-04-25T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
             "keyword": [
                 "frozen ground",
                 "earth science",
@@ -616539,75 +616551,39 @@
                 "glaciers/ice sheets",
                 "cryosphere"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985741-ASF.html",
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
-            "identifier": "C1327985741-ASF",
-            "description": "Sentinel-1B Dual-pol ground projected high and full resolution metadata",
-            "title": "SENTINEL-1B_DUAL_POL_METADATA_GRD_HIGH_RES",
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
+            "temporal": "2016-04-25T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SENTINEL-1B_DUAL_POL_METADATA_GRD_HIGH_RES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-04-01",
-            "temporal": "2021-04-01T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coordinates",
-                "station",
-                "space",
-                "location",
-                "iss",
-                "international",
-                "ephemeris",
-                "trajectory",
-                "coords",
-                "topo"
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
-            "identifier": "nasa-iss-data_2021-04-01",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-04-01",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -616730,482 +616706,508 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-04-01",
+            "issued": "2021-04-01",
+            "keyword": [
+                "coordinates",
+                "station",
+                "space",
+                "location",
+                "iss",
+                "international",
+                "ephemeris",
+                "trajectory",
+                "coords",
+                "topo"
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
+            "temporal": "2021-04-01T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-04-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-A-FPA-3-RDR-IMPS-V1.0",
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
-                "infrared astronomical satellite",
-                "asteroid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This product represents averaged radiometric diameters and geometric albedos derived from observations made by the Infrared Astronomical Satellite in 1983 for 1796 numbered asteroids and 88 unnumbered asteroids whose orbital elements were determined using astrometry from two or more apparitions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-a-fpa-3-rdr-imps-v1.0_cwi3-jufs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "infrared astronomical satellite",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-A-FPA-3-RDR-IMPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-a-fpa-3-rdr-imps-v1.0_cwi3-jufs",
-            "description": "This product represents averaged radiometric diameters and geometric albedos derived from observations made by the Infrared Astronomical Satellite in 1983 for 1796 numbered asteroids and 88 unnumbered asteroids whose orbital elements were determined using astrometry from two or more apparitions.",
-            "title": "IMPS DIAMETERS AND ALBEDOS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IMPS DIAMETERS AND ALBEDOS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0507-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-26T01:43:05.000 to 2014-12-26T12:10:06.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0507-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0507-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0507-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-26T01:43:05.000 to 2014-12-26T12:10:06.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0507 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0507 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-SSH-1.1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2023-11-30. SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version 1.1. Version 1.1. SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version 1.1. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.5067/SWOT-SSH-1.1. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-07-21",
-            "temporal": "2022-12-16T00:00:00Z/2023-12-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-21",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean waves",
-                "sea surface topography"
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
-            "identifier": "C2746459620-POCLOUD",
-            "description": "Sea surface height data product with data from the KaRIn swath spanning 60 km on both sides of nadir with a nadir gap. Product provides sea surface height, sea surface height anomaly, wind speed, significant waveheight, on a geographically fixed, swath-aligned 2x2 km2 grid, as well as sea surface height on a 250x250 m2 native grid. Gridded; full swath for each half orbit. Available in netCDF-4 file format.",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version 1.1",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version 1.1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_DEFAULT_THUMBNAIL.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Sea surface height data product with data from the KaRIn swath spanning 60 km on both sides of nadir with a nadir gap. Product provides sea surface height, sea surface height anomaly, wind speed, significant waveheight, on a geographically fixed, swath-aligned 2x2 km2 grid, as well as sea surface height on a 250x250 m2 native grid. Gridded; full swath for each half orbit. Available in netCDF-4 file format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-SSH-1.1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-SSH-1.1",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2746459620-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2746459620-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2746459620-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2746459620-POCLOUD",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56407_SWOT_Product_Description_L2_LR_SSH_20220902_RevA.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56407_SWOT_Product_Description_L2_LR_SSH_20220902_RevA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_DEFAULT_THUMBNAIL.jpg",
+            "identifier": "C2746459620-POCLOUD",
+            "issued": "2022-07-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean waves",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-SSH-1.1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Jet Propulsion Laboratory",
+            "series-name": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version 1.1",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2023-12-04T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-GLID1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Luc Rainville. 2019-10-24. SPURS-2 Seaglider data for the E. Tropical Pacific field campaign. Version 1.0. SPURS-2 Field Campaign Waveglider Data Products. APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-GLID1. http://podaac.jpl.nasa.gov/SPURS. Luc Rainville, SPURS Data Management PI, Fred Bingham, 2019-10-24, SPURS-2 Seaglider data for the E. Tropical Pacific field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-08-14",
-            "temporal": "2016-08-24T16:18:24Z/2017-11-07T00:03:55Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-14",
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
-            "identifier": "C2491772350-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. The Seaglider is an autonomous profiler measuring salinity and temperature. A total of five Seagliders were deployed over the two SPURS2 cruises. Three Seagliders were deployed on the first Revelle cruise in August 2016, recovered by the Lady Amber after 7 months and redeployed, to be retrieved finally during the second cruise in November 2017. One of the Seagliders was deployed alongside and tracked the Lagrangian array across the study region, diving to depths of 1000m. All Seaglider data files are in netCDF format with standards compliant metadata.",
-            "release-place": "APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA",
-            "series-name": "SPURS-2 Seaglider data for the E. Tropical Pacific field campaign",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Luc Rainville",
-            "title": "SPURS-2 Seaglider data for the E. Tropical Pacific field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_SEAGLIDER.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. The Seaglider is an autonomous profiler measuring salinity and temperature. A total of five Seagliders were deployed over the two SPURS2 cruises. Three Seagliders were deployed on the first Revelle cruise in August 2016, recovered by the Lady Amber after 7 months and redeployed, to be retrieved finally during the second cruise in November 2017. One of the Seagliders was deployed alongside and tracked the Lagrangian array across the study region, diving to depths of 1000m. All Seaglider data files are in netCDF format with standards compliant metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-GLID1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-GLID1",
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
-                    "downloadURL": "http://spurs.jpl.nasa.gov/",
-                    "description": "Project Website for SPURS",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for SPURS",
+                    "downloadURL": "http://spurs.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_SEAGLIDER.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_SEAGLIDER.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772350-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772350-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772350-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772350-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_SEAGLIDER.jpg",
+            "identifier": "C2491772350-POCLOUD",
+            "issued": "2019-08-14",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-GLID1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA",
+            "series-name": "SPURS-2 Seaglider data for the E. Tropical Pacific field campaign",
             "spatial": "-126.122 8.994 -122.128 12.022",
+            "temporal": "2016-08-24T16:18:24Z/2017-11-07T00:03:55Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 Seaglider data for the E. Tropical Pacific field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GRGAD-20C06",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GRACE. 2018-05-10. GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS CSR (GAD). Version 6.0. GRACE_GAD_L2_GRAV_CSR_RL06. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, CSR. https://doi.org/10.5067/GRGAD-20C06. https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/. GRACE, CSR, 2018-05-10, GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS CSR RELEASE 6.0 GAD, https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/.",
-            "issued": "2018-04-26",
-            "temporal": "2002-04-05T00:00:00Z/2017-06-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "gravity/gravitational field",
-                "earth science",
-                "solid earth"
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
-            "identifier": "C2491772128-POCLOUD",
-            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of ocean bottom pressure derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements, produced by the Center for Space Research (CSR) at University of Texas at Austin.  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
-            "release-place": "JPL",
-            "series-name": "GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS CSR (GAD)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "GRACE",
-            "title": "GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS CSR RELEASE 6.0 GAD",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAD_L2_GRAV_CSR_RL06.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of ocean bottom pressure derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements, produced by the Center for Space Research (CSR) at University of Texas at Austin.  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGAD-20C06",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGAD-20C06",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ProdSpecDoc_v4.6.pdf",
-                    "description": "Product Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product Specification Document",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ProdSpecDoc_v4.6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ReleaseNotes_csr_RL06.txt",
-                    "description": "Release Notes for GRACE L-2 products - version UTCSR RL-06",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes for GRACE L-2 products - version UTCSR RL-06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ReleaseNotes_csr_RL06.txt",
+                    "mediaType": "text/html",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAD_L2_GRAV_CSR_RL06.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAD_L2_GRAV_CSR_RL06.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-CSR006_ProcStd_v5.0.pdf",
-                    "description": "UTCSR Level-2 Processing Standards Document For Level-2 Product Release 06",
                     "@type": "dcat:Distribution",
+                    "description": "UTCSR Level-2 Processing Standards Document For Level-2 Product Release 06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-CSR006_ProcStd_v5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/L2/CSR/RL06/README.txt",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/L2/CSR/RL06/README.txt",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772128-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772128-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772128-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772128-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAD_L2_GRAV_CSR_RL06.jpg",
+            "identifier": "C2491772128-POCLOUD",
+            "issued": "2018-04-26",
+            "keyword": [
+                "gravity/gravitational field",
+                "earth science",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/GRGAD-20C06",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL",
+            "series-name": "GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS CSR (GAD)",
             "spatial": "-180.0 -88.0 180.0 88.0",
+            "temporal": "2002-04-05T00:00:00Z/2017-06-30T00:00:00Z",
             "theme": [
                 "GRACE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS CSR RELEASE 6.0 GAD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-3-EAR2-EARTHSWINGBY2-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the EARTH SWING-BY 2 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-3-ear2-earthswingby2-v1.4_cwpt-ks42",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "moon",
@@ -617214,421 +617216,431 @@
                 "vega",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-3-EAR2-EARTHSWINGBY2-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-3-ear2-earthswingby2-v1.4_cwpt-ks42",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the EARTH SWING-BY 2 mission phase",
-            "title": "ROSETTA-ORBITER EARTH SWING-BY 2 OSINAC\n                                      3 RDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH SWING-BY 2 OSINAC\n                                      3 RDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/HI97S5EBWP1R",
             "citation": "NOAA NESDIS. 2022-08-22. VISSRGOES3IMVIS. Version 001. VISSR/GOES-3 Visible Imagery on 70mm Film V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/HI97S5EBWP1R. https://disc.gsfc.nasa.gov/datacollection/VISSRGOES3IMVIS_001.html. Digital Science Data.",
-            "issued": "2018-03-21",
-            "temporal": "1979-05-02T00:00:00Z/1979-06-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-21",
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
+            "creator": "NOAA NESDIS",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2387026798-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "VISSRGOES3IMVIS is the Visible Infrared Spin-Scan Radiometer (VISSR) Visible Imagery on 70mm Film data product from the third Geostationary Operational Environmental Satellite (GOES-3). This set of visible imagery (0.55 to 0.70 micrometer) was originally produced on commercial image-generation equipment from digital tapes and was made available on 70-mm film, from which they were later scanned to digital TIFF image files. Each TIFF scan contains 2 or 3 pictures, and there are several hundred scans from an original 70 mm film roll which are combined into a ZIP file. Each picture contains a title on the top boundary and a 33-level gray scale on the right boundary that represents brightness temperatures. It may have a combination of the following options: 1) contrast enhancement, 2) image sectorization, and 3) 1/16-size imagery. The maximum effective size covers 500 sq km, represented by 4000 by 3904 pixels. Each element has a maximum resolution of 3.7 km. The title contains the satellite identification, picture number, picture type, coordinate numbers of the top left pixel relative to the visible sensor, start time of sectorized image, and pixel scaling and sector size identification.\n\nThe GOES-3 satellite was parked over the equator at longitude 135W from 1978 through 1981 viewing the hemisphere below the satellite. It was moved to its final operational position at 135W on Dec 19, 1975. The VISSR experiment was operated by the NOAA National Environmental Satellite Data and Information Service (NESDIS), as well as scientists from NASA Goddard Space Flight Center.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00247 (old ID 75-100A-01B).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "VISSRGOES3IMVIS",
-            "creator": "NOAA NESDIS",
-            "title": "VISSR/GOES-3 Visible Imagery on 70mm Film V001 (VISSRGOES3IMVIS) at GES DISC",
-            "graphic-preview-description": "Typical GOES-3 VISSR visible 70mm film image.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES3IMVIS_001.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHI97S5EBWP1R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHI97S5EBWP1R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES3IMVIS_001.png",
-                    "description": "Typical GOES-3 VISSR visible 70mm film image.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical GOES-3 VISSR visible 70mm film image.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES3IMVIS_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRGOES3IMVIS_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRGOES3IMVIS_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES3IMVIS.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES3IMVIS.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRGOES3IMVIS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRGOES3IMVIS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES3IMVIS.001/doc/README.VISSRSMSGOESIM.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES3IMVIS.001/doc/README.VISSRSMSGOESIM.001.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES3IMVIS_001.png",
+            "identifier": "C2387026798-GES_DISC",
+            "issued": "2018-03-21",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/HI97S5EBWP1R",
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
+            "series-name": "VISSRGOES3IMVIS",
             "spatial": "135.0 -90.0 -45.0 90.0",
+            "temporal": "1979-05-02T00:00:00Z/1979-06-08T23:59:59.999Z",
             "theme": [
                 "GOES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VISSR/GOES-3 Visible Imagery on 70mm Film V001 (VISSRGOES3IMVIS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4C24TCF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chinese Academy of Surveying and Mapping - CASM China in Time and Space - CITAS - University of Washington, and Center for International Earth Science Information Network - CIESIN. 1996-05-31. China Dimensions Data Collection: China Administrative Regions GIS Data: 1:1M, County Level, 1990. Version 1.01. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4C24TCF. https://doi.org/10.7927/H4C24TCF.",
-            "issued": "1996-05-31",
-            "temporal": "1990-12-31T00:00:00Z/1990-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-05-31",
-            "references": [
-                "https://doi.org/10.7927/H4RB72JW",
-                "https://doi.org/10.7927/H4QC01D2",
-                "https://doi.org/10.7927/H4GT5K3V",
-                "https://doi.org/10.7927/H4KK98PS",
-                "https://doi.org/10.7927/H4MK69T5",
-                "https://doi.org/10.7927/H4ZW1HVD",
-                "https://doi.org/10.7927/H47D2S2F",
-                "https://doi.org/10.7927/H43N21B3",
-                "https://doi.org/10.7927/H4V40S4D",
-                "https://doi.org/10.7927/H4FT8HZ2"
-            ],
-            "keyword": [
-                "boundaries",
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
-            "identifier": "C179001737-SEDAC",
-            "description": "The China Administrative Regions GIS Data: 1:1M, County Level, 1990 consists of geographic boundary data for the administrative regions of China as of 31 December 1990. The data includes the geographical location, area, administrative division code, and county and island name. The data are at a scale of one to one million (1:1M) at the national, provincial, and county level. This data set is produced in collaboration with the Center for International Earth Science Information Network (CIESIN), Chinese Academy of Surveying and Mapping (CASM), and the University of Washington as part of the China in Time and Space (CITAS) project.",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Chinese Academy of Surveying and Mapping - CASM China in Time and Space - CITAS - University of Washington, and Center for International Earth Science Information Network - CIESIN",
-            "title": "China Dimensions Data Collection: China Administrative Regions GIS Data: 1:1M, County Level, 1990",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-admin-regions-gis-1990/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The China Administrative Regions GIS Data: 1:1M, County Level, 1990 consists of geographic boundary data for the administrative regions of China as of 31 December 1990. The data includes the geographical location, area, administrative division code, and county and island name. The data are at a scale of one to one million (1:1M) at the national, provincial, and county level. This data set is produced in collaboration with the Center for International Earth Science Information Network (CIESIN), Chinese Academy of Surveying and Mapping (CASM), and the University of Washington as part of the China in Time and Space (CITAS) project.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4C24TCF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4C24TCF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-admin-regions-gis-1990/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-admin-regions-gis-1990/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-admin-regions-gis-1990/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-admin-regions-gis-1990/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-admin-regions-gis-1990",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-admin-regions-gis-1990",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-admin-regions-gis-1990/sedac-logo.jpg",
+            "identifier": "C179001737-SEDAC",
+            "issued": "1996-05-31",
+            "keyword": [
+                "boundaries",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4C24TCF",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4RB72JW",
+                "https://doi.org/10.7927/H4QC01D2",
+                "https://doi.org/10.7927/H4GT5K3V",
+                "https://doi.org/10.7927/H4KK98PS",
+                "https://doi.org/10.7927/H4MK69T5",
+                "https://doi.org/10.7927/H4ZW1HVD",
+                "https://doi.org/10.7927/H47D2S2F",
+                "https://doi.org/10.7927/H43N21B3",
+                "https://doi.org/10.7927/H4V40S4D",
+                "https://doi.org/10.7927/H4FT8HZ2"
+            ],
+            "release-place": "Saginaw, MI",
             "spatial": "73.0 18.0 135.0 54.0",
+            "temporal": "1990-12-31T00:00:00Z/1990-12-31T00:00:00Z",
             "theme": [
                 "CDDC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "China Dimensions Data Collection: China Administrative Regions GIS Data: 1:1M, County Level, 1990"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-2LSNTR-F08",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2023-07-31. Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography F08. Version F08. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-2LSNTR-F08.",
-            "issued": "2023-02-18",
-            "temporal": "2020-11-30T00:00:00Z/2024-12-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
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
-            "identifier": "C2619444013-POCLOUD",
-            "description": "Provides low resolution (LR) non-time critical (NTC; 60-day latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed, along with 1 Hz and 20 Hz measurements from the radar altimeter, orbit altitude, environmental range corrections, instrument corrections, and geophysical models. The NTC product is analogous to the Jason-3 GDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography F08",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides low resolution (LR) non-time critical (NTC; 60-day latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed, along with 1 Hz and 20 Hz measurements from the radar altimeter, orbit altitude, environmental range corrections, instrument corrections, and geophysical models. The NTC product is analogous to the Jason-3 GDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LSNTR-F08",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LSNTR-F08",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_STD_OST_NTC_F08",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_STD_OST_NTC_F08",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619444013-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619444013-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619444013-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619444013-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08.jpg",
+            "identifier": "C2619444013-POCLOUD",
+            "issued": "2023-02-18",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean waves",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-2LSNTR-F08",
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
+            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography F08"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/147/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-22",
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
-            "identifier": "DASHLINK_147",
             "description": "We present a set of novel algorithms which we call sequenceMiner that detect and characterize anomalies in large sets of high-dimensional symbol sequences that arise from recordings of switch sensors in the cockpits of commercial airliners. While the algorithms we present are general and domain-independent, we focus on a specific problem that is critical to determining the system-wide health of a fleet of aircraft. The approach taken uses\r\nunsupervised clustering of sequences using the normalized length of the longest common subsequence (nLCS) as a similarity measure, followed by detailed outlier analysis to detect anomalies. In this method, an outlier sequence is defined as a sequence that is far away from the cluster centre. We present new algorithms for outlier analysis that provide comprehensible indicators as to why a particular sequence is deemed to be an outlier. The algorithms provide a coherent description to an analyst of the anomalies in the sequence when compared to more normal sequences. In the final section of the paper we demonstrate the effectiveness of sequenceMiner for anomaly detection on a real set of discrete sequence data from a fleet of commercial airliners. We show that sequenceMiner discovers actionable and operationally significant safety events. We also compare our innovations with standard HiddenMarkov Models, and show that our methods are superior.",
-            "title": "Anomaly Detection and Diagnosis Algorithms for Discrete Symbols",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Anomaly_Detection-2008.pdf",
-                    "description": "Paper",
                     "@type": "dcat:Distribution",
+                    "description": "Paper",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Anomaly_Detection-2008.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Anomaly_Detection-2008.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_147",
+            "issued": "2010-09-22",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/147/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Anomaly Detection and Diagnosis Algorithms for Discrete Symbols"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/cwzb-2ui3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "All analysis results presented here are preliminary and are not intended as an official catalog of Fermi-LAT detected GRBs. Please consult the table's caveat page for analysis details and other important information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/observations/types/grbs/lat_grbs/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000226",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "cgro",
                 "compton",
@@ -617646,249 +617658,248 @@
                 "balloon",
                 "bursts"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/cwzb-2ui3",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000226",
-            "description": "All analysis results presented here are preliminary and are not intended as an official catalog of Fermi-LAT detected GRBs. Please consult the table's caveat page for analysis details and other important information.",
-            "title": "Fermi LAT GRBs",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/observations/types/grbs/lat_grbs/",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Fermi LAT GRBs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TCSP/MTP/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Mahoney, Michael J.2006. TCSP ER-2 MICROWAVE TEMPERATURE PROFILER (MTP) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/TCSP/MTP/DATA201",
-            "issued": "2006-04-12",
-            "temporal": "2005-07-02T12:58:40Z/2005-07-27T11:39:46Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmospheric temperature",
-                "altitude",
-                "spectral/engineering",
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1979951897-GHRC_DAAC",
             "description": "The TCSP ER-2 Microwave Temperature Profiler (MTP) dataset was collected by the  ER-2 Microwave Temperature Profiler (MTP), which is a passive microwave radiometer which measures the thermal emission from oxygen molecules in the atmosphere for a selection of elevation angles (normally 10 between +60 and -58 degrees). The current observing frequencies are 55.5, 56.6 and 58.8 GHz. Measured 'brightness temperature' versus elevation angle is converted to air temperature versus altitude using a modified statistical retrieval procedure with a Bayesian component. An altitude temperature profile (ATP) is produced in this manner every 13 seconds or approximately 3 km along the flight path. The ATP can be used to produce a color-coded temperature curtain (CTC) of the temperature field which the ER2 has flown through, and to identify the tropopause location. ATPs can also be used to locate altitudes where the air is cold enough to condense nitric acid or water vapor to form polar stratospheric clouds (PSCs). The TCSP mission collected data for research and documentation of cyclogenesis, the interaction of temperature, humidity, precipitation, wind and air pressure that creates ideal birthing conditions for tropical storms, hurricanes and related phenomena. The goal of this mission was to help us better understand how hurricanes and other tropical storms are formed and intensify.",
-            "graphic-preview-description": "N/A",
-            "title": "TCSP ER-2 MICROWAVE TEMPERATURE PROFILER (MTP) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/mtp/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FMTP%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FMTP%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspmtp",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspmtp",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/mtp/browse/TZS_20050705.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/mtp/browse/TZS_20050705.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/tcsp/tcspmtp/tcspmtp_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/tcsp/tcspmtp/tcspmtp_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/mtp/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/mtp/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/mtp/browse/",
+            "identifier": "C1979951897-GHRC_DAAC",
+            "issued": "2006-04-12",
+            "keyword": [
+                "atmospheric temperature",
+                "altitude",
+                "spectral/engineering",
+                "atmosphere",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/TCSP/MTP/DATA201",
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
             "spatial": "-99.737 4.684 -65.918 24.784",
+            "temporal": "2005-07-02T12:58:40Z/2005-07-27T11:39:46Z",
             "theme": [
                 "TCSP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TCSP ER-2 MICROWAVE TEMPERATURE PROFILER (MTP) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/344",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dang, Q.L., H. Margolis, and M.R. Coyea. 1998. BOREAS TE-09 Photosynthetic Response Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/344",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-24T00:00:00Z/1994-09-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "ecological dynamics",
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
-            "identifier": "C2808129563-ORNL_CLOUD",
             "description": "Contains photosynthetic response of boreal tree species to varied parameters.  Collected by TE-09 BOREAS group in the Northern Study Area.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-09 Photosynthetic Response Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F344",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F344",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te09prd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te09prd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE09_Photo_Resp.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE09_Photo_Resp.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/344",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/344",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te09prd/comp/te09prd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te09prd/comp/te09prd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te09prd/comp/TE09_Photo_Resp.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te09prd/comp/TE09_Photo_Resp.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te09prd/comp/TE09_Photo_Resp.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te09prd/comp/TE09_Photo_Resp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te09prd/comp/TE09_Photo_Resp.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te09prd/comp/TE09_Photo_Resp.txt",
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
+            "identifier": "C2808129563-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "ecological dynamics",
+                "vegetation",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/344",
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
             "spatial": "-98.67 55.88 -98.48 55.93",
+            "temporal": "1994-05-24T00:00:00Z/1994-09-19T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-09 Photosynthetic Response Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://daac.ornl.gov/MODIS/MODIS-menu/modis_webservice.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://data.nasa.gov/developer"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jason Duley",
+                "hasEmail": "mailto:jason.duley@nasa.gov"
+            },
+            "description": "The MODIS Web service provides users with subsets of MODIS Land Products through standards based SOAP (Simple Object Access Protocol) Web service.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The MODIS Web service provides users with subsets of MODIS Land Products through standards based SOAP (Simple Object Access Protocol) Web service.",
+                    "downloadURL": "http://daac.ornl.gov/MODIS/MODIS-menu/modis_webservice.html",
+                    "mediaType": "text/html",
+                    "title": "MODIS Web Service API"
+                }
             ],
+            "identifier": "API-16",
+            "issued": "2015-11-30",
             "keyword": [
                 "python",
                 "api",
@@ -617901,105 +617912,103 @@
                 "products",
                 "r"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jason Duley",
-                "hasEmail": "mailto:jason.duley@nasa.gov"
-            },
+            "landingPage": "http://daac.ornl.gov/MODIS/MODIS-menu/modis_webservice.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "API-16",
-            "description": "The MODIS Web service provides users with subsets of MODIS Land Products through standards based SOAP (Simple Object Access Protocol) Web service.",
-            "title": "MODIS Web Service API",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://daac.ornl.gov/MODIS/MODIS-menu/modis_webservice.html",
-                    "description": "The MODIS Web service provides users with subsets of MODIS Land Products through standards based SOAP (Simple Object Access Protocol) Web service.",
-                    "@type": "dcat:Distribution",
-                    "title": "MODIS Web Service API"
-                }
+            "references": [
+                "https://data.nasa.gov/developer"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MODIS Web Service API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/BIOSOPE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/BIOSOPE/DATA001.",
-            "issued": "2004-10-26",
-            "temporal": "2004-10-26T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean optics",
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
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
-            "identifier": "C1633360162-OB_DAAC",
             "description": "Measurements made during the BIOSOPE: Biogeochemistry and Optics South Pacific Experiment in 2004.",
-            "title": "Biogeochemistry and Optics South Pacific Experiment",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBIOSOPE%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBIOSOPE%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BIOSOPE/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BIOSOPE/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360162-OB_DAAC",
+            "issued": "2004-10-26",
+            "keyword": [
+                "ocean chemistry",
+                "ocean optics",
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/BIOSOPE/DATA001",
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
+            "temporal": "2004-10-26T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Biogeochemistry and Optics South Pacific Experiment"
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
+            "description": "EPPS, GRNS, MAG, MASCS, MDIS, MLA, RSS, SPICE, XRS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20100315-2.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-582",
+            "issued": "2018-06-25",
             "keyword": [
                 "xrs",
                 "epps",
@@ -618012,301 +618021,271 @@
                 "pds",
                 "rss"
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
-            "identifier": "NASA-582",
-            "description": "EPPS, GRNS, MAG, MASCS, MDIS, MLA, RSS, SPICE, XRS",
-            "title": "PDS MESSENGER Data Release 5",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20100315-2.shtml",
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
+            "title": "PDS MESSENGER Data Release 5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1024-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-10T21:23:10.000 to 2015-09-11T05:26:02.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1024-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1024-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1024-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-10T21:23:10.000 to 2015-09-11T05:26:02.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1024 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1024 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1940",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and R.O. Green. 2021. MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Fall 2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1940",
-            "issued": "2023-06-19",
-            "temporal": "2020-09-17T20:01:40Z/2020-10-15T21:52:56Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "visible wavelengths",
-                "spectral/engineering",
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
-            "identifier": "C2731651592-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected as part of the Western Diversity Time Series (WDTS, formerly HyspIRI) program during nine flights aboard a NASA ER-2 aircraft over selected areas of California, U.S, from 2020-09-17 to 2020-10-15. The WDTS program will observe California's ecosystems and provide critical information on natural disasters such as volcanoes, wildfires, and drought. MASTER products can identify vegetation type and health and provide a benchmark for the state of the ecosystems against which future changes can be assessed. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes the flight path, spectral band information, instrument configuration, ancillary notes, and summary information for each deployment, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and an RGB composite image from flight track 09 acquired on 15 October 2020 near Yosemite National Park, California, U.S. Source: MASTERL1B_2190600_09_20201015_2007_2021_V01.jpg",
-            "title": "MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Fall 2020",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_SeptOct_2020_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1940",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1940",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_WDTS_SeptOct_2020/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_WDTS_SeptOct_2020/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_SeptOct_2020.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_SeptOct_2020.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1940",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1940",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_WDTS_SeptOct_2020/comp/MASTER_WDTS_SeptOct_2020.pdf",
-                    "description": "MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Fall 2020: MASTER_WDTS_SeptOct_2020.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Fall 2020: MASTER_WDTS_SeptOct_2020.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_WDTS_SeptOct_2020/comp/MASTER_WDTS_SeptOct_2020.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_SeptOct_2020_Fig1.jpg",
-                    "description": "Single-band images and an RGB composite image from flight track 09 acquired on 15 October 2020 near Yosemite National Park, California, U.S. Source: MASTERL1B_2190600_09_20201015_2007_2021_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and an RGB composite image from flight track 09 acquired on 15 October 2020 near Yosemite National Park, California, U.S. Source: MASTERL1B_2190600_09_20201015_2007_2021_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_SeptOct_2020_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and an RGB composite image from flight track 09 acquired on 15 October 2020 near Yosemite National Park, California, U.S. Source: MASTERL1B_2190600_09_20201015_2007_2021_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_SeptOct_2020_Fig1.jpg",
+            "identifier": "C2731651592-ORNL_CLOUD",
+            "issued": "2023-06-19",
+            "keyword": [
+                "visible wavelengths",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1940",
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
             "spatial": "-123.75 31.95 -112.49 40.98",
+            "temporal": "2020-09-17T20:01:40Z/2020-10-15T21:52:56Z",
             "theme": [
                 "MASTER",
                 "WDTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Fall 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-RNRDR",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Steven A. Rutledge. 2019-03-28. SPURS-2 research vessel along track SEA-POL rain radar imaging data for E. Tropical Pacific R/V Revelle-2 cruise. Version 1.0. SPURS Field Campaign SEA-POL Rain Radar Products. Department of Atmospheric Science, Colorado State University, Fort Collins, Colorado, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-RNRDR. http://podaac.jpl.nasa.gov/SPURS. Steven A. Rutledge, SPURS Data Management PI, Fred Bingham, 2019-03-28, SPURS-2 research vessel along track SEA-POL rain radar imaging data for E. Tropical Pacific R/V Revelle-2 cruise, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-03-12",
-            "temporal": "2017-10-22T00:05:04Z/2017-11-10T23:00:03Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-12",
-            "keyword": [
-                "atmosphere",
-                "precipitation",
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
-            "identifier": "C2491772345-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. The SEA-POL rain radar instrument was employed over the period 22 Oct.-10 Nov. 2017 during the second SPURS-2 R/V Revelle cruise. SEA-POL (seagoing-polarimetric radar) is a C-band, Doppler polarimetric radar system providing 240-degree sector coverage centered on the ships bow via its 1-degree beam width antenna. SEA-POL was used primarily to map rainfall in SPURS-2. The resulting dataset is a series of gridded netCDF data files for a 20 day period at 5-20 minute intervals comprised of rain rate and rain accumulation fields.",
-            "release-place": "Department of Atmospheric Science, Colorado State University, Fort Collins, Colorado, USA",
-            "series-name": "SPURS-2 research vessel along track SEA-POL rain radar imaging data for E. Tropical Pacific R/V Revelle-2 cruise",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Steven A. Rutledge",
-            "title": "SPURS-2 research vessel along track SEA-POL rain radar imaging data for E. Tropical Pacific R/V Revelle-2 cruise",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_RAINRADAR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. The SEA-POL rain radar instrument was employed over the period 22 Oct.-10 Nov. 2017 during the second SPURS-2 R/V Revelle cruise. SEA-POL (seagoing-polarimetric radar) is a C-band, Doppler polarimetric radar system providing 240-degree sector coverage centered on the ships bow via its 1-degree beam width antenna. SEA-POL was used primarily to map rainfall in SPURS-2. The resulting dataset is a series of gridded netCDF data files for a 20 day period at 5-20 minute intervals comprised of rain rate and rain accumulation fields.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-RNRDR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-RNRDR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_RAINRADAR.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_RAINRADAR.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772345-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772345-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772345-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772345-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_RAINRADAR.jpg",
+            "identifier": "C2491772345-POCLOUD",
+            "issued": "2019-03-12",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-RNRDR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Department of Atmospheric Science, Colorado State University, Fort Collins, Colorado, USA",
+            "series-name": "SPURS-2 research vessel along track SEA-POL rain radar imaging data for E. Tropical Pacific R/V Revelle-2 cruise",
             "spatial": "-125.57 5.06 -119.89 24.2",
+            "temporal": "2017-10-22T00:05:04Z/2017-11-10T23:00:03Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 research vessel along track SEA-POL rain radar imaging data for E. Tropical Pacific R/V Revelle-2 cruise"
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
-            "identifier": "NASA-862__40",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -618314,169 +618293,192 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__40",
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
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1520",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rogers, B.M., A.J. Soja, M.L. Goulden, and J.T. Randerson. 2017. Fire Intensity and Burn Severity Metrics for Circumpolar Boreal Forests, 2001-2013. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1520",
-            "issued": "2017-07-24",
-            "temporal": "2001-01-01T00:00:00Z/2013-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-15",
-            "keyword": [
-                "natural hazards",
-                "biosphere",
-                "national geospatial data asset",
-                "ecosystems",
-                "human dimensions",
-                "vegetation",
-                "surface radiative properties",
-                "ecological dynamics",
-                "earth science",
-                "land surface",
-                "ngda"
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
-            "identifier": "C2767484391-ORNL_CLOUD",
             "description": "This data set provides products characterizing immediate and longer-term ecosystem changes from fires in the circumpolar boreal forests of Northern Eurasia and North America. The data include fire intensity (fire radiative power; FRP), increase in spring albedo, decrease in tree cover, normalized burn ratio, normalized difference vegetation index, and land surface temperature, as well as three derived fire metrics: crown scorch, vegetation destruction, and fire-induced tree mortality. Longer-term changes are indicated by mean albedo determined 5-12 years after fires, mean percent decrease in tree cover 5-7 years after fires, and mean annual burned percentage. The data cover the period 2001-2013 and are provided at quarter, half, and one degree resolutions for boreal forests within the 40 to 80 degree North circumpolar region. The data were derived from a variety of sources including MODIS products, climate reanalysis data, and forest inventories. A data file with identified boreal forest area (pixels), as defined by climate and vegetation type, and a file with the defined North American and Eurasian boreal forest study regions are included.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Fire Intensity and Burn Severity Metrics for Circumpolar Boreal Forests, 2001-2013",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1520_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1520",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1520",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Boreal_Fire_Severity_Metrics/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Boreal_Fire_Severity_Metrics/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Boreal_Fire_Severity_Metrics.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Boreal_Fire_Severity_Metrics.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1520",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1520",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Boreal_Fire_Severity_Metrics/comp/Boreal_Fire_Severity_Metrics.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Boreal_Fire_Severity_Metrics/comp/Boreal_Fire_Severity_Metrics.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Boreal_Fire_Severity_Metrics/comp/Boreal_Fire_Severity_Metrics_Fig1.png",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Boreal_Fire_Severity_Metrics/comp/Boreal_Fire_Severity_Metrics_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1520_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1520_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1520",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1520",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1520_1_fit.png",
+            "identifier": "C2767484391-ORNL_CLOUD",
+            "issued": "2017-07-24",
+            "keyword": [
+                "natural hazards",
+                "biosphere",
+                "national geospatial data asset",
+                "ecosystems",
+                "human dimensions",
+                "vegetation",
+                "surface radiative properties",
+                "ecological dynamics",
+                "earth science",
+                "land surface",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1520",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 40.0 180.0 80.0",
+            "temporal": "2001-01-01T00:00:00Z/2013-12-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "CARVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Fire Intensity and Burn Severity Metrics for Circumpolar Boreal Forests, 2001-2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M14-V2.0",
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
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m14-v2.0_cxes-wf35",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M14-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m14-v2.0_cxes-wf35",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSIWAC 3 RDR MTP014 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSIWAC 3 RDR MTP014 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-3-DIDR-HALLEY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Spectroscopy and Spectrophotometry Network collected 352 files that represented the digitized spectra from plate material. In some cases, the non-Halley targets for the spectroscopic observations can be grouped according to 'laboratory' calibration, dark, bias, flatfield, sky, and photometric standards. In the first category, a large number of 'arcs' and 'lamps' were used as follows: HE-NE, TH-AR, NE-AR, CU-AR, CU-NE, Thorium, Tungsten, Quartz, and Rubidium. For the 'sky' observers used the twilight, moonlight, and blank sky. The most common 'photometric' standards were stars, but observers also included other comets (Hartley-Goode), asteroids (Ceres), reflection nebulae (R8), and emission nebulae (NGC1982, NGC7000). A list of these stellar calibration targets follows: HD 140283, HD 184711, HD89688, HD102870, HD120086, HD13974, HD219188, HD 25680, HD 19445, HD18803, HD30455, HD26912, SAO 1280, HZ15, CD-22 7696, GD 190, GC5106, GC2188, GC2192, G19113213, G 99-37, L745-46A, Feige 15, Feige 56, Landolt 98, Landolt 92, Van Beuren, RHO ORION, CHI 1 ORION, 29 PI LEO. For this data, no distinction about 'reduction' is distinguished for this process. The data cover the date range from 1985 October 17 through 1986 December 12.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-3-didr-halley-v1.0_cxhi-qkyp",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "emission nebula",
                 "cal lamps",
@@ -618489,191 +618491,165 @@
                 "reflection nebula",
                 "comet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-3-DIDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-3-didr-halley-v1.0_cxhi-qkyp",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Spectroscopy and Spectrophotometry Network collected 352 files that represented the digitized spectra from plate material. In some cases, the non-Halley targets for the spectroscopic observations can be grouped according to 'laboratory' calibration, dark, bias, flatfield, sky, and photometric standards. In the first category, a large number of 'arcs' and 'lamps' were used as follows: HE-NE, TH-AR, NE-AR, CU-AR, CU-NE, Thorium, Tungsten, Quartz, and Rubidium. For the 'sky' observers used the twilight, moonlight, and blank sky. The most common 'photometric' standards were stars, but observers also included other comets (Hartley-Goode), asteroids (Ceres), reflection nebulae (R8), and emission nebulae (NGC1982, NGC7000). A list of these stellar calibration targets follows: HD 140283, HD 184711, HD89688, HD102870, HD120086, HD13974, HD219188, HD 25680, HD 19445, HD18803, HD30455, HD26912, SAO 1280, HZ15, CD-22 7696, GD 190, GC5106, GC2188, GC2192, G19113213, G 99-37, L745-46A, Feige 15, Feige 56, Landolt 98, Landolt 92, Van Beuren, RHO ORION, CHI 1 ORION, 29 PI LEO. For this data, no distinction about 'reduction' is distinguished for this process. The data cover the date range from 1985 October 17 through 1986 December 12.",
-            "title": "IHW COMET HALLEY DIGITIZED PHOTOGRAPHIC SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY DIGITIZED PHOTOGRAPHIC SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67PCHURYUMOV-M35-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67pchuryumov-m35-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67PCHURYUMOV-M35-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67pchuryumov-m35-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP035 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP035 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/99FTCYYYLAQ0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Global Seasonal-Snow Classification, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.5067/99FTCYYYLAQ0.",
-            "issued": "1981-01-01",
-            "temporal": "1981-01-01T00:00:00Z/2019-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-31",
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
-            "identifier": "C2218487926-NSIDCV0",
             "description": "This data set consists of global, seasonal snow classifications\u2014e.g., tundra, boreal forest, maritime, ephemeral, prairie, montane forest, and ice\u2014determined from air temperature, precipitation, and wind speed climatologies. Data are available on global, North America, and Eurasia latitude-longitude grids at four resolutions: 10 arcsec (~300 m), 30 arcsec (~1 km), 2.5 arcmin (~5 km), and 0.5\u00b0 (~50 km).",
-            "title": "Global Seasonal-Snow Classification, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F99FTCYYYLAQ0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F99FTCYYYLAQ0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0768_global_seasonal_snow_classification_v01",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0768_global_seasonal_snow_classification_v01",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0768_global_seasonal_snow_classification_v01",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0768_global_seasonal_snow_classification_v01",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0768_global_seasonal_snow_classification_v01",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0768_global_seasonal_snow_classification_v01",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/99FTCYYYLAQ0",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/99FTCYYYLAQ0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/99FTCYYYLAQ0",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/99FTCYYYLAQ0",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2218487926-NSIDCV0",
+            "issued": "1981-01-01",
+            "keyword": [
+                "earth science",
+                "snow/ice",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/99FTCYYYLAQ0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1981-01-01T00:00:00Z/2019-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Seasonal-Snow Classification, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-j7aj4gr",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2019-10-09. S5P_L2__AER_LH_HiR. Version 1. Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 5.5km x 3.5km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-j7aj4gr. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_LH_HiR_1.html. Digital Science Data.",
-            "issued": "2017-05-05",
-            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-05",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "air quality"
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
-            "identifier": "C1627516290-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__AER_LH_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P TROPOMI aerosol layer height algorithm applies a forward model, which includes DISAMAR (Determining Instrument Specifications and Analyzing Methods for Atmospheric Retrieval, a Layer-Based Orders of Scattering algorithm) to calculate monochromatic reflectance, and also employs a neural network scheme for speedy processor performance. Data retrieval uses the Optimal Estimation Method (OEM) for spectral fitting with various aerosol layer pressures and aerosol optical thicknesses in the Oxygen-A band (758 -770nm). The aerosol baseline model assumes a single uniformly distributed aerosol layer with a fixed pressure thickness and a constant aerosol volume extinction coefficient and single scattering albedo. The aerosol parameterization is particularly suitable for elevated non-scattering aerosols such as volcanic ash, desert dust and biomass burning plume. The product main outputs include the mid-pressure and mid-altitude of aerosol layers, aerosol optical thickness at 760nm, error estimates, and other relevant diagnostics.\n\nStarting from orbit #12432 on March 7th of 2020, the S-NPP auxiliary cloud data source used in the aerosol layer height product data processing has been transitioned from the VIIRS Cloud Mask (VCM) into the Enterprise Cloud Mask (ECM).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__AER_LH_HiR",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__AER_LH_HiR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__AER_LH_HiR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__AER_LH_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P TROPOMI aerosol layer height algorithm applies a forward model, which includes DISAMAR (Determining Instrument Specifications and Analyzing Methods for Atmospheric Retrieval, a Layer-Based Orders of Scattering algorithm) to calculate monochromatic reflectance, and also employs a neural network scheme for speedy processor performance. Data retrieval uses the Optimal Estimation Method (OEM) for spectral fitting with various aerosol layer pressures and aerosol optical thicknesses in the Oxygen-A band (758 -770nm). The aerosol baseline model assumes a single uniformly distributed aerosol layer with a fixed pressure thickness and a constant aerosol volume extinction coefficient and single scattering albedo. The aerosol parameterization is particularly suitable for elevated non-scattering aerosols such as volcanic ash, desert dust and biomass burning plume. The product main outputs include the mid-pressure and mid-altitude of aerosol layers, aerosol optical thickness at 760nm, error estimates, and other relevant diagnostics.\n\nStarting from orbit #12432 on March 7th of 2020, the S-NPP auxiliary cloud data source used in the aerosol layer height product data processing has been transitioned from the VIIRS Cloud Mask (VCM) into the Enterprise Cloud Mask (ECM).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-j7aj4gr",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-j7aj4gr",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -618683,155 +618659,160 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_LH_HiR_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_LH_HiR_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__AER_LH_HiR_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__AER_LH_HiR_1",
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
+            "identifier": "C1627516290-GES_DISC",
+            "issued": "2017-05-05",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5270/S5P-j7aj4gr",
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
+            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__AER_LH_HiR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-3-EAR2-CALIBRATED-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains CALIBRATED DATA of the second Earth Flyby(EAR2).\nThe closest approach (CA) took place on November 13, 2007 at 20:57",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-3-ear2-calibrated-v3.0_cxii-2qj8",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-3-EAR2-CALIBRATED-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-3-ear2-calibrated-v3.0_cxii-2qj8",
-            "description": "This dataset contains CALIBRATED DATA of the second Earth Flyby(EAR2).\nThe closest approach (CA) took place on November 13, 2007 at 20:57",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 3 EAR2 CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 3 EAR2 CALIBRATED V3.0"
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
-                "planetary science",
-                "geography",
-                "space science",
-                "safety",
-                "lessons learned",
-                "knowledge sharing"
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
-            "identifier": "NASA-0000026__2",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "This web page leads to a database of images and information about the 150 major impact craters on Callisto and is updated semi-regularly based on continuing analysis of Voyager images.",
-            "title": "Callisto Crater Database",
-            "programCode": [
-                "026:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -618839,237 +618820,265 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "NASA-0000026__2",
+            "issued": "2018-06-25",
+            "keyword": [
+                "planetary science",
+                "geography",
+                "space science",
+                "safety",
+                "lessons learned",
+                "knowledge sharing"
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
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2023",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Berner, L.T., and S.J. Goetz. 2022. ABoVE: Landsat Vegetation Greenness Trends, Boreal Forest Biome, 1985-2019. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2023",
-            "issued": "2022-04-30",
-            "temporal": "1985-01-01T00:00:00Z/2019-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biospheric indicators",
-                "biosphere",
-                "vegetation",
-                "land use/land cover",
-                "land surface",
-                "ecosystems",
-                "earth science",
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
-            "identifier": "C2262495772-ORNL_CLOUD",
             "description": "This dataset provides information on interannual trends in annual maximum vegetation greenness from 1985 to 2019 for recently undisturbed areas in the boreal forest biome. Multi-decadal changes in remotely sensed vegetation greenness provide evidence of an emerging boreal biome shift driven by climate warming. Annual maximum vegetation greenness was assessed at about 100,000 random sample locations using an ensemble of spectral vegetation indices (NDVI, EVI2, kNDVI, and NIRv) derived from Landsat products. The dataset provides raster data summarizing vegetation greenness trends for sample locations stratified by Ecological Land Unit in GeoTIFF format. These raster data span the circum-hemispheric boreal forest biome between 45 to 70 degrees north at 300 m resolution. Estimates of uncertainty were generated using Monte Carlo simulations. Interannual trends in annual maximum vegetation greenness from 1985 to 2019 and 2000 to 2019 are provided for sample locations with adequate data for time series analysis; these data are in comma-separated values (CSV) format.",
-            "graphic-preview-description": "Change in greenness of boreal forest across the northern hemisphere between 2000 to 2019, estimated from an ensemble of vegetation indices derived from Landsat imagery. Source: boreal_greenness_median_percent_change_2000to2019_p500.tif",
-            "title": "ABoVE: Landsat Vegetation Greenness Trends, Boreal Forest Biome, 1985-2019",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/BorealForest_Greenness_Trends_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2023",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2023",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/BorealForest_Greenness_Trends/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/BorealForest_Greenness_Trends/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/BorealForest_Greenness_Trends.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/BorealForest_Greenness_Trends.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2023",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2023",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/BorealForest_Greenness_Trends/comp/BorealForest_Greenness_Trends.pdf",
-                    "description": "ABoVE: Landsat Vegetation Greenness Trends, Boreal Forest Biome, 1985-2019: BorealForest_Greenness_Trends.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Landsat Vegetation Greenness Trends, Boreal Forest Biome, 1985-2019: BorealForest_Greenness_Trends.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/BorealForest_Greenness_Trends/comp/BorealForest_Greenness_Trends.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/BorealForest_Greenness_Trends_Fig1.jpg",
-                    "description": "Change in greenness of boreal forest across the northern hemisphere between 2000 to 2019, estimated from an ensemble of vegetation indices derived from Landsat imagery. Source: boreal_greenness_median_percent_change_2000to2019_p500.tif",
                     "@type": "dcat:Distribution",
+                    "description": "Change in greenness of boreal forest across the northern hemisphere between 2000 to 2019, estimated from an ensemble of vegetation indices derived from Landsat imagery. Source: boreal_greenness_median_percent_change_2000to2019_p500.tif",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/BorealForest_Greenness_Trends_Fig1.jpg",
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
+            "graphic-preview-description": "Change in greenness of boreal forest across the northern hemisphere between 2000 to 2019, estimated from an ensemble of vegetation indices derived from Landsat imagery. Source: boreal_greenness_median_percent_change_2000to2019_p500.tif",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/BorealForest_Greenness_Trends_Fig1.jpg",
+            "identifier": "C2262495772-ORNL_CLOUD",
+            "issued": "2022-04-30",
+            "keyword": [
+                "biospheric indicators",
+                "biosphere",
+                "vegetation",
+                "land use/land cover",
+                "land surface",
+                "ecosystems",
+                "earth science",
+                "climate indicators"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2023",
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
             "spatial": "-180.0 45.0 180.0 72.0",
+            "temporal": "1985-01-01T00:00:00Z/2019-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Landsat Vegetation Greenness Trends, Boreal Forest Biome, 1985-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NAMMA/HYGROMETER/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Diskin, Glenn S and James R Podolske.2006. NAMMA DIODE LASER HYGROMETER (DLH) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/NAMMA/HYGROMETER/DATA201",
-            "issued": "2006-06-01",
-            "temporal": "2006-08-19T13:32:00Z/2006-09-12T19:48:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-19",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor"
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
-            "identifier": "C1979885952-GHRC_DAAC",
             "description": "The NAMMA Diode Laser Hygrometer (DLH) dataset uses the DLH, a near-infrared spectrometer operating from aircraft platforms, was developed by NASA's Langley and Ames Research Centers. It measures water vapor mixing ratio and derives water vapor partial pressure, relative humidity, and water vapor flux. Based upon near-infrared tunable diode technology, its spectrometer provides true in situ monitoring of water vapor concentrations with precision levels exceeding those of existing Lyman alpha and frost point hygrometers. These data files were generated during support of the NASA African Monsoon Multidisciplinary Analyses (NAMMA) campaign, a field research investigation sponsored by the Science Mission Directorate of the National Aeronautics and Space Administration (NASA). This mission was based in the Cape Verde Islands, 350 miles off the coast of Senegal in west Africa. Commencing in August 2006, NASA scientists employed surface observation networks and aircraft to characterize the evolution and structure of African Easterly Waves (AEWs) and Mesoscale Convective Systems over continental western Africa, and their associated impacts on regional water and energy budgets.",
-            "title": "NAMMA DIODE LASER HYGROMETER (DLH) V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FHYGROMETER%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FHYGROMETER%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namdlh",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namdlh",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namdlh/namdlh_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namdlh/namdlh_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/namma",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/namma",
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
+            "identifier": "C1979885952-GHRC_DAAC",
+            "issued": "2006-06-01",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/NAMMA/HYGROMETER/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-34.1533 7.03833 -10.5583 21.9783",
+            "temporal": "2006-08-19T13:32:00Z/2006-09-12T19:48:00Z",
             "theme": [
                 "NAMMA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NAMMA DIODE LASER HYGROMETER (DLH) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M09-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m09-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M09-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m09-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP009 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP009 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/cloudsat",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/cloudsat/main/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Kumanchik",
+                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
+            },
+            "description": "Launched in April 2006, CloudSat monitors the state of the Earth\u2019s atmosphere and weather with a sophisticated radar system. The instrument, jointly developed with the Canadian Space Agency, can predict which clouds produce rain, observe snowfall, and monitor the moisture content of clouds.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/models/cloudsat/Cloudsat.fbx.zip",
+                    "mediaType": "application/octet-stream"
+                }
             ],
+            "identifier": "NASA-328",
+            "issued": "2018-06-26",
             "keyword": [
                 "3d model",
                 "spacecraft",
@@ -619080,175 +619089,168 @@
                 "a-train",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Kumanchik",
-                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
-            },
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/cloudsat",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-328",
-            "description": "Launched in April 2006, CloudSat monitors the state of the Earth\u2019s atmosphere and weather with a sophisticated radar system. The instrument, jointly developed with the Canadian Space Agency, can predict which clouds produce rain, observe snowfall, and monitor the moisture content of clouds.",
-            "title": "NASA 3D Models: CloudSat",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/models/cloudsat/Cloudsat.fbx.zip",
-                    "mediaType": "application/octet-stream"
-                }
+            "references": [
+                "http://www.nasa.gov/mission_pages/cloudsat/main/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: CloudSat"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2141",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and R.O. Green. 2023. MASTER: Western Diversity Time Series Campaign, WDTS, September 2022. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2141",
-            "issued": "2023-06-19",
-            "temporal": "2022-09-02T19:31:31Z/2022-09-09T20:38:49Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "surface radiative properties",
-                "spectral/engineering",
-                "visible wavelengths",
-                "earth science",
-                "surface thermal properties",
-                "infrared wavelengths",
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
-            "identifier": "C2731785942-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected as part of the Western Diversity Time Series (WDTS, formerly HyspIRI) airborne campaign during five flights aboard a NASA ER-2 aircraft over California and Nevada, U.S., from 2022-09-02 to 2022-09-09. The WDTS campaign will observe California's ecosystems and provide critical information on natural disasters such as volcanoes, wildfires, and drought. MASTER products can identify vegetation type and health and provide a benchmark for the state of the ecosystems against which future changes can be assessed. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes the flight path, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single band images and an RGB composite image from flight track 02 acquired on 09 September 2022 over the site of the Mosquito Fire west of Lake Tahoe, California, U.S. Source: MASTERL1B_2263100_02_20220909_1948_1954_V02.jpg",
-            "title": "MASTER: Western Diversity Time Series Campaign, WDTS, September 2022",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Fall_2022_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2141",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2141",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_WDTS_Fall_2022/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_WDTS_Fall_2022/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Fall_2022.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Fall_2022.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2141",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2141",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_WDTS_Fall_2022/comp/MASTER_WDTS_Fall_2022.pdf",
-                    "description": "MASTER: Western Diversity Time Series Campaign, WDTS, September 2022: MASTER_WDTS_Fall_2022.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Western Diversity Time Series Campaign, WDTS, September 2022: MASTER_WDTS_Fall_2022.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_WDTS_Fall_2022/comp/MASTER_WDTS_Fall_2022.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Fall_2022_Fig1.jpg",
-                    "description": "Single band images and an RGB composite image from flight track 02 acquired on 09 September 2022 over the site of the Mosquito Fire west of Lake Tahoe, California, U.S. Source: MASTERL1B_2263100_02_20220909_1948_1954_V02.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single band images and an RGB composite image from flight track 02 acquired on 09 September 2022 over the site of the Mosquito Fire west of Lake Tahoe, California, U.S. Source: MASTERL1B_2263100_02_20220909_1948_1954_V02.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Fall_2022_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single band images and an RGB composite image from flight track 02 acquired on 09 September 2022 over the site of the Mosquito Fire west of Lake Tahoe, California, U.S. Source: MASTERL1B_2263100_02_20220909_1948_1954_V02.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Fall_2022_Fig1.jpg",
+            "identifier": "C2731785942-ORNL_CLOUD",
+            "issued": "2023-06-19",
+            "keyword": [
+                "surface radiative properties",
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science",
+                "surface thermal properties",
+                "infrared wavelengths",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2141",
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
             "spatial": "-123.75 33.53 -118.12 40.98",
+            "temporal": "2022-09-02T19:31:31Z/2022-09-09T20:38:49Z",
             "theme": [
                 "MASTER",
                 "WDTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Western Diversity Time Series Campaign, WDTS, September 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-MIMI-2-INCA-UNCALIB-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Imaging Neutral Camera (INCA) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission.  The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values of counts in the form of rates and of rate images for the INCA sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data are presented in a set of tables which are of variable length and use a comma to separate various fields.  This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI INCA archive.  A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI INCA archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-inca-uncalib-v1.1_cxqt-mmnj",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "cassini-huygens",
                 "saturn",
                 "jupiter",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-MIMI-2-INCA-UNCALIB-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-inca-uncalib-v1.1_cxqt-mmnj",
-            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Imaging Neutral Camera (INCA) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission.  The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values of counts in the form of rates and of rate images for the INCA sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data are presented in a set of tables which are of variable length and use a comma to separate various fields.  This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI INCA archive.  A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI INCA archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
-            "title": "CASSINI E/J/S/SW MIMI INCA SENSOR UNCALIBRATED DATA V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI E/J/S/SW MIMI INCA SENSOR UNCALIBRATED DATA V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-3-JUPITER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons Alice UV Imager instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-3-jupiter-v1.0_cxu9-n4hd",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "callisto",
@@ -619259,377 +619261,357 @@
                 "calibration",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-3-JUPITER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-3-jupiter-v1.0_cxu9-n4hd",
-            "description": "This data set contains Calibrated data taken by the New Horizons Alice UV Imager instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0699-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-09T09:52:05.000 to 2015-04-09T20:40:16.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0699-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0699-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0699-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-09T09:52:05.000 to 2015-04-09T20:40:16.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0699 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0699 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-08-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1.",
-            "issued": "1997-10-07",
-            "temporal": "1997-10-07T00:00:00Z/1997-11-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-11-12",
-            "keyword": [
-                "atmosphere",
-                "air quality",
-                "altitude",
-                "atmospheric chemistry",
-                "atmospheric radiation",
-                "earth science",
-                "lidar",
-                "spectral/engineering"
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
-            "identifier": "C2761597892-LARC_ASDC",
             "description": "SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1 is the Differential Absorption Lidar (DIAL) remotely sensed data collected onboard the DC-8 aircraft during the SONEX suborbital campaign. Data collection is complete.\r\n\r\nThe SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) was an international, multi-organizational mission that took place in October-November 1997. NASA was the US sponsor of SONEX that partnered with POLINAT-2 (Pollution from Aircraft Emissions in the North Atlantic Flight Corridor) funded by the German DLR (Deutsches Zentrum f\u00fcr Luft- und Raumfahrt) or German Aerospace Agency. NASA flew the DC-8 aircraft out of NASA/Ames Research Center. DLR operated an instrumented Falcon 20 aircraft. The staging locations for NAFC sampling were primarily Bangor, Maine (US), and Shannon, Ireland. Subsonic aircraft emissions impact several aspects of atmospheric composition: nitrogen oxides (NOx), CO, and hydrocarbons from emissions can perturb upper tropospheric/lower stratospheric (UT/LS) ozone; water vapor, soot, and sulfur oxides (SOx) emitted by aircraft may perturb clouds and aerosols, changing UT/LS radiative forcing and global temperature.\r\nIn SONEX and POLINAT, flights were conducted in the vicinity of the North Atlantic Flight Coordinator (NAFC) to observe the impact of aircraft emissions on NOx and ozone (O3). The DC-8 aircraft payload (Singh et al., 1999) primarily measured in-situ CO, CO2, hydrocarbons/halocarbons, O3, aerosols (Dibb et al., 2000), OH/HO2, water vapor, nitric acid (Talbot et al., 1999), photolysis rates, temperature, pressure, winds, NOx, and NOy.\r\nThree sampling approaches were implemented during SONEX. First, special meteorological (Fuelberg et al., 2000) were developed to allow targeted sampling for air parcels affected by aircraft emissions and various meteorological events, e.g., convection, lightning (Jeker et al., 2000), stratospheric intrusions (Cho et al., 2000). Second, because the NAFC had not been extensively sampled in the past, it was important for SONEX to characterize the climatology of trace species like CN (Wang et al., 2000), NOx and NOy (Koike et al., 2000). Third, tracers (Simpson et al., 2000; Thompson et al., 1999) and model sensitivity studies (Meijer et al., 2000) were employed for Air Mass Identification. This sampling strategy answered the following questions: Where and when are air masses found with the greatest aircraft influence? When and where was stratospheric air sampled? SONEX showed a substantial impact of aircraft emissions on UT/LS NOx and CN in the vicinity of fresh aircraft emissions. However, during October-November 1997 over the NAFC, UT/LS NOx was dominated by surface emissions redistributed by convection and augmented by lightning.",
-            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) Differential Absorption Lidar (DIAL) Remotely Sensed Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
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
-                    "description": "Ames File Format",
                     "@type": "dcat:Distribution",
+                    "description": "Ames File Format",
+                    "downloadURL": "https://espo.nasa.gov/content/Ames_Format_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2761597892-LARC_ASDC",
-                    "description": "Earthdata Search client for SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2761597892-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
-                    "description": "DOI for SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/AircraftRemoteSensing_DC8_DIAL_Data_1/",
-                    "description": "ASDC Direct Data Download for SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/AircraftRemoteSensing_DC8_DIAL_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2761597892-LARC_ASDC",
+            "issued": "1997-10-07",
+            "keyword": [
+                "atmosphere",
+                "air quality",
+                "altitude",
+                "atmospheric chemistry",
+                "atmospheric radiation",
+                "earth science",
+                "lidar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.89 -129.402 19.89 13.023 69.127 13.023 69.127 -129.402 19.89 -129.402</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1997-10-07T00:00:00Z/1997-11-13T23:59:59.999Z",
             "theme": [
                 "SONEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) Differential Absorption Lidar (DIAL) Remotely Sensed Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHMTB-2PN20",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Naval Oceanographic Office. 2020-07-24. GHRSST Level 2P Global 1m Sea Surface Temperature v2.0 from the Advanced Very High Resolution Radiometer (AVHRR) on the MetOp-B satellite produced by NAVO. Version 2.0. METOP-A AVHRR GAC L2P swath SST dataset. Stennis Space Center, MS, USA. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHMTB-2PN20. https://podaac.jpl.nasa.gov/GHRSST. Naval Oceanographic Office, Naval Oceanographic Office, 2020-07-24, GHRSST Level 2P Global Sea Surface Temperature v2.0 from the AVHRR on the MetOp-B satellite produced by NAVO, https://podaac.jpl.nasa.gov/GHRSST.",
-            "issued": "2020-06-11",
-            "temporal": "2020-06-22T12:09:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
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
-            "identifier": "C2036877502-POCLOUD",
-            "description": "A global Group for High Resolution Sea Surface Temperature (GHRSST) Level 2P data set containing multi-channel Sea Surface Temperature (SST) retrievals derived in real-time from the Advanced Very High Resolution Radiometer (AVHRR) level-1B data from the Meteorological Operational-B (MetOp-B) satellite. The SST data in this data set are used operationally in oceanographic analyses and forecasts by the US Naval Oceanographic Office (NAVO). The MetOp satellite program is a European multi-satellite  program to provide weather data services for monitoring climate and improving weather forecasts. MetOp-A,  MetOp-B and Metop-C were respectively launched on 19 Oct 2006,  17 September 2012 and 7 November 2018. The program was jointly established by the European Space Agency (ESA) and the European Organization for the Exploitation of Meteorological Satellites (EUMETSAT) with the US National Oceanic and Atmospheric Administration (NOAA) contributing the AVHRR sensor. AVHRR instruments measure the radiance of the Earth in 5 (or 6) relatively wide spectral bands. The first two are centered around the red (0.6 micron) and near-infrared (0.9 micron) regions, the third one is located around 4 (3.6) micron, and the last two sample the emitted thermal radiation, around 11 and 12 micron, respectively. The legacy 5 band instrument is known as AVHRR/2 while the more recent version, the AVHRR/3 (first carried on the NOAA-15 platform), acquires data in a 6th channel located at 1.6 micron. Typically, the 11 and 12 micron channels are used to derive SST sometimes in combination with the 3.5 micron channel.  The swath of the AVHRR sensor is a relatively large 2400 km. All MetOp platforms are sun synchronous and generally view the same earth location twice a day (latitude dependent). The ground native resolution of the AVHRR instruments is approximately 1.1 km at nadir and degrades off nadir. This particular data set is produced from legacy Global Area Coverage (GAC) data that are derived from a sample averaging of the full resolution global AVHRR data. Four out of every five samples along the scan line are used to compute on average value and the data from only every third scan line are processed, yielding an effective 4 km spatial resolution at nadir. The v2.0 is the updated version from current v1.0 with extensive algorithm improvements and upgrades. The major improvements include: 1) Significant changes in contaminant/cloud detection; 2) Increased the spatial resolution from 9 km to 4 km; 3) Updated compliance with GDS2, ACDD 1.3, and CF 1.6; and 4) Removed the dependency on the High-resolution Infrared Radiation Sounder (HIRS) sensor (only available to MetOp-A/B), thus allowing for the consistent inter-calibration and the processing of MetOp-A/B/C data",
-            "release-place": "Stennis Space Center, MS, USA",
-            "series-name": "GHRSST Level 2P Global 1m Sea Surface Temperature v2.0 from the Advanced Very High Resolution Radiometer (AVHRR) on the MetOp-B satellite produced by NAVO",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Naval Oceanographic Office",
-            "title": "GHRSST Level 2P Global Sea Surface Temperature v2.0 from the AVHRR on the MetOp-B satellite produced by NAVO",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRMTB_G-NAVO-L2P-v2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A global Group for High Resolution Sea Surface Temperature (GHRSST) Level 2P data set containing multi-channel Sea Surface Temperature (SST) retrievals derived in real-time from the Advanced Very High Resolution Radiometer (AVHRR) level-1B data from the Meteorological Operational-B (MetOp-B) satellite. The SST data in this data set are used operationally in oceanographic analyses and forecasts by the US Naval Oceanographic Office (NAVO). The MetOp satellite program is a European multi-satellite  program to provide weather data services for monitoring climate and improving weather forecasts. MetOp-A,  MetOp-B and Metop-C were respectively launched on 19 Oct 2006,  17 September 2012 and 7 November 2018. The program was jointly established by the European Space Agency (ESA) and the European Organization for the Exploitation of Meteorological Satellites (EUMETSAT) with the US National Oceanic and Atmospheric Administration (NOAA) contributing the AVHRR sensor. AVHRR instruments measure the radiance of the Earth in 5 (or 6) relatively wide spectral bands. The first two are centered around the red (0.6 micron) and near-infrared (0.9 micron) regions, the third one is located around 4 (3.6) micron, and the last two sample the emitted thermal radiation, around 11 and 12 micron, respectively. The legacy 5 band instrument is known as AVHRR/2 while the more recent version, the AVHRR/3 (first carried on the NOAA-15 platform), acquires data in a 6th channel located at 1.6 micron. Typically, the 11 and 12 micron channels are used to derive SST sometimes in combination with the 3.5 micron channel.  The swath of the AVHRR sensor is a relatively large 2400 km. All MetOp platforms are sun synchronous and generally view the same earth location twice a day (latitude dependent). The ground native resolution of the AVHRR instruments is approximately 1.1 km at nadir and degrades off nadir. This particular data set is produced from legacy Global Area Coverage (GAC) data that are derived from a sample averaging of the full resolution global AVHRR data. Four out of every five samples along the scan line are used to compute on average value and the data from only every third scan line are processed, yielding an effective 4 km spatial resolution at nadir. The v2.0 is the updated version from current v1.0 with extensive algorithm improvements and upgrades. The major improvements include: 1) Significant changes in contaminant/cloud detection; 2) Increased the spatial resolution from 9 km to 4 km; 3) Updated compliance with GDS2, ACDD 1.3, and CF 1.6; and 4) Removed the dependency on the High-resolution Infrared Radiation Sounder (HIRS) sensor (only available to MetOp-A/B), thus allowing for the consistent inter-calibration and the processing of MetOp-A/B/C data",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMTB-2PN20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMTB-2PN20",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "Portal to the GHRSST Global Data Assembly Center and data access",
                     "@type": "dcat:Distribution",
+                    "description": "Portal to the GHRSST Global Data Assembly Center and data access",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRMTB_G-NAVO-L2P-v2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRMTB_G-NAVO-L2P-v2.0.jpg",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/G-XVII_Proceedings_Washington_Issue3.pdf",
-                    "description": "Thermal uniformity analysis of SST data fields",
                     "@type": "dcat:Distribution",
+                    "description": "Thermal uniformity analysis of SST data fields",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/G-XVII_Proceedings_Washington_Issue3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
-                    "description": "GHRSST Data Specification (GDS) 2",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Data Specification (GDS) 2",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877502-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877502-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877502-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877502-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRMTB_G-NAVO-L2P-v2.0.jpg",
+            "identifier": "C2036877502-POCLOUD",
+            "issued": "2020-06-11",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHMTB-2PN20",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Stennis Space Center, MS, USA",
+            "series-name": "GHRSST Level 2P Global 1m Sea Surface Temperature v2.0 from the Advanced Very High Resolution Radiometer (AVHRR) on the MetOp-B satellite produced by NAVO",
             "spatial": "-180.0 -70.0 180.0 80.0",
+            "temporal": "2020-06-22T12:09:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 2P Global Sea Surface Temperature v2.0 from the AVHRR on the MetOp-B satellite produced by NAVO"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/cy5f-mm9i",
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
-            "identifier": "NASA-0000038__26",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -619637,251 +619619,247 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__26",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nen",
+                "space science",
+                "wise",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/cy5f-mm9i",
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
-            "landingPage": "https://doi.org/10.5067/AIRCRAFT/ARISE_Radiation_AircraftInSitu_C130_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-11-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AIRCRAFT/ARISE_Radiation_AircraftInSitu_C130_Data_1.",
-            "issued": "2020-09-24",
-            "temporal": "2014-08-30T00:00:00Z/2014-10-05T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-11",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Smith",
                 "hasEmail": "mailto:william.l.smith@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1968754505-LARC_ASDC",
             "description": "ARISE_Radiation_AircraftInSitu_C130_Data_1 is the Arctic Radiation - IceBridge Sea & Ice Experiment (ARISE) 2014 in-situ cloud data product. This product is a result of a joint effort of the Radiation Sciences, Cryospheric Sciences and Airborne Sciences programs of the Earth Science Division in NASA's Science Mission Directorate in Washington. Data were collected via the Solar Spectral Flux Radiometer (SSFR), BroadBand Radiometer (BBR), and Spectrometers for Sky-Scanning, Sun-Tracking Atmospheric Research (4STAR). Data collection is complete.\r\n\r\nARISE was NASA's first Arctic airborne campaign designed to take simultaneous measurements of ice, clouds and the levels of incoming and outgoing radiation, the balance of which determined the degree of climate warming. Over the past few decades, an increase in global temperatures led to decreased Arctic summer sea ice. Typically, Arctic sea ice reflects sunlight from the Earth. However, a loss of sea ice means there is more open water to absorb heat from the sun, enhancing warming in the region. More open water can also cause the release of more moisture into the atmosphere. This additional moisture could affect cloud formation and the exchange of heat from Earth\u2019s surface to space. Conducted during the peak of summer ice melt (August 28, 2014-October 1, 2014), ARISE was designed to study and collect data on thinning sea ice, measure cloud and atmospheric properties in the Arctic, and to address questions about the relationship between retreating sea ice and the Arctic climate. During the campaign, instruments on NASA\u2019s C-130 aircraft conducted measurements of spectral and broadband radiative flux profiles, quantified surface characteristics, cloud properties, and atmospheric state parameters under a variety of Arctic atmospheric and surface conditions (e.g. open water, sea ice, and land ice). When possible, C-130 flights were coordinated to fly under satellite overpasses. The primary aerial focus of ARISE was over Arctic sea ice and open water, with minor coverage over Greenland land ice. Through these efforts, the ARISE field campaign helped improve cloud and sea ice computer modeling in the Arctic.",
-            "title": "ARISE 2014 C-130 In-Situ Radiation Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FARISE_Radiation_AircraftInSitu_C130_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FARISE_Radiation_AircraftInSitu_C130_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/arise",
-                    "description": "ESPO home page for ARISE",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO home page for ARISE",
+                    "downloadURL": "https://espo.nasa.gov/arise",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/press/2014/august/nasa-to-investigate-climate-impacts-of-arctic-sea-ice-loss/",
-                    "description": "Video: NASA to Investigate Climate Impacts of Arctic Sea Ice Loss",
                     "@type": "dcat:Distribution",
+                    "description": "Video: NASA to Investigate Climate Impacts of Arctic Sea Ice Loss",
+                    "downloadURL": "https://www.nasa.gov/press/2014/august/nasa-to-investigate-climate-impacts-of-arctic-sea-ice-loss/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AIRCRAFT/ARISE_Radiation_AircraftInSitu_C130_Data_1",
-                    "description": "DOI data set landing page for ARISE_Radiation_AircraftInSitu_C130_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ARISE_Radiation_AircraftInSitu_C130_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/AIRCRAFT/ARISE_Radiation_AircraftInSitu_C130_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968754505-LARC_ASDC",
-                    "description": "Earthdata Search for ARISE_Radiation_AircraftInSitu_C130_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ARISE_Radiation_AircraftInSitu_C130_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968754505-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/arise/index.html",
-                    "description": "ARISE Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ARISE Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/arise/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/arise/mission-flight-docs",
-                    "description": "ARISE Flight Documents",
                     "@type": "dcat:Distribution",
+                    "description": "ARISE Flight Documents",
+                    "downloadURL": "https://espo.nasa.gov/arise/mission-flight-docs",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/98/7/bams-d-14-00277.1.xml",
-                    "description": "ARISE Mission Overview",
                     "@type": "dcat:Distribution",
+                    "description": "ARISE Mission Overview",
+                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/98/7/bams-d-14-00277.1.xml",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ARISE/2014",
-                    "description": "ARISE Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "ARISE Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ARISE/2014",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/ARISE/pdocuments",
-                    "description": "ARISE support documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ARISE support documentation",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/ARISE/pdocuments",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARISE/Radiation_AircraftInSitu_C130_Data_1/",
-                    "description": "ASDC Direct Data Download for ARISE_Radiation_AircraftInSitu_C130_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ARISE_Radiation_AircraftInSitu_C130_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARISE/Radiation_AircraftInSitu_C130_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ARISE/Radiation_AircraftInSitu_C130_Data_1/contents.html",
-                    "description": "OPeNDAP data access for ARISE_Radiation_AircraftInSitu_C130_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for ARISE_Radiation_AircraftInSitu_C130_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ARISE/Radiation_AircraftInSitu_C130_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1968754505-LARC_ASDC",
+            "issued": "2020-09-24",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/AIRCRAFT/ARISE_Radiation_AircraftInSitu_C130_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>35.0 -170.0 35.0 -72.0 82.0 -72.0 82.0 -170.0 35.0 -170.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2014-08-30T00:00:00Z/2014-10-05T23:59:59.999Z",
             "theme": [
                 "ARISE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ARISE 2014 C-130 In-Situ Radiation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD09GQ.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2021-02-07. MODIS/Aqua Surface Reflectance Daily L2G Global 250m SIN Grid NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MYD09GQ.NRT.061.",
-            "issued": "2021-02-07",
-            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "surface radiative properties",
-                "ngda",
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
-            "identifier": "C2007650640-LANCEMODIS",
-            "description": "The MODIS/Aqua Surface Reflectance Daily L2G Global 250m SIN Grid Near Real Time (NRT) product is an estimate of the surface spectral reflectance as it would be measured at ground level in the absence of atmospheric scattering or absorption. Low-level data are corrected for atmospheric gases and aerosols, yielding a level-2 basis for several higher-order gridded level-2 (L2G) and level-3 products.MYD09GQ provides Bands 1 and 2 at a 250-meter resolution in a daily gridded L2G product in the Sinusoidal projection. Science Data Sets provided for this product include reflectance for Bands 1 and 2 a quality rating observation coverage and observation number. This product is meant to be used in conjunction with MYD09GA where important quality and viewing geometry information is stored.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Aqua Surface Reflectance Daily L2G Global 250 m SIN Grid NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Surface Reflectance Daily L2G Global 250m SIN Grid Near Real Time (NRT) product is an estimate of the surface spectral reflectance as it would be measured at ground level in the absence of atmospheric scattering or absorption. Low-level data are corrected for atmospheric gases and aerosols, yielding a level-2 basis for several higher-order gridded level-2 (L2G) and level-3 products.MYD09GQ provides Bands 1 and 2 at a 250-meter resolution in a daily gridded L2G product in the Sinusoidal projection. Science Data Sets provided for this product include reflectance for Bands 1 and 2 a quality rating observation coverage and observation number. This product is meant to be used in conjunction with MYD09GA where important quality and viewing geometry information is stored.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09GQ.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09GQ.NRT.061",
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
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MYD09GQ",
-                    "description": "Direct access to the download site and directory hosting the MYD09GQ 6.1NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MYD09GQ 6.1NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MYD09GQ",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C2007650640-LANCEMODIS",
+            "issued": "2021-02-07",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "surface radiative properties",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD09GQ.NRT.061",
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
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Surface Reflectance Daily L2G Global 250 m SIN Grid NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSPF14/SSMI/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chris Kidd. PRECIP_SSMI_F14. Version 1. NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F14 NASA PPS L1C V06 Tbs. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/DMSPF14/SSMI/DATA201. https://measures.gsfc.nasa.gov/datacollection/PRECIP_SSMI_F14_1.html. Digital Science Data.",
-            "issued": "2021-06-10",
-            "temporal": "1995-05-07T17:25:08Z/2008-08-24T00:48:18Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-10",
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C2368309429-GES_DISC",
-            "description": "The data presented in this level 2 orbital product are rain rate estimates expressed as mm/hour determined from brightness temperatures (Tbs) obtained from the Special Sensor Microwave/Imager (SSM/I) flown on the US Defense Meteorological Satellite Program (DMSP) F14 mission. Most of the products generated in this data set are based upon the algorithms developed for the 3rd Algorithm Intercomparison Project (AIP-3) of the Global Precipitation Climatology Project (GPCP).  Details of these 15 algorithms and development of a quality score which is a measure of confidence in the estimate, along with processing and algorithmic flags, can be found in the Algorithm Theoretical Basis Document  (ATBD).  The data in this product cover the period from 1997 to 2008 with one file per orbit.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "PRECIP_SSMI_F14",
             "creator": "Chris Kidd",
-            "title": "NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F14 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F14) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PRECIP_SSMI_F14.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The data presented in this level 2 orbital product are rain rate estimates expressed as mm/hour determined from brightness temperatures (Tbs) obtained from the Special Sensor Microwave/Imager (SSM/I) flown on the US Defense Meteorological Satellite Program (DMSP) F14 mission. Most of the products generated in this data set are based upon the algorithms developed for the 3rd Algorithm Intercomparison Project (AIP-3) of the Global Precipitation Climatology Project (GPCP).  Details of these 15 algorithms and development of a quality score which is a measure of confidence in the estimate, along with processing and algorithmic flags, can be found in the Algorithm Theoretical Basis Document  (ATBD).  The data in this product cover the period from 1997 to 2008 with one file per orbit.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSPF14%2FSSMI%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSPF14%2FSSMI%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -619921,549 +619899,582 @@
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Precipitation/PRECIP_SSMI_F14.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Precipitation/PRECIP_SSMI_F14.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PRECIP_SSMI_F14.png",
+            "identifier": "C2368309429-GES_DISC",
+            "issued": "2021-06-10",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSPF14/SSMI/DATA201",
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
+            "series-name": "PRECIP_SSMI_F14",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1995-05-07T17:25:08Z/2008-08-24T00:48:18Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F14 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F14) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "OMPS_NPP_NMSO2_PCA_L2",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/SO2/DATA205",
             "citation": "Can Li, Nickolay A. Krotkov, Peter Leonard, Joanna Joiner. 2020-07-30. OMPS_NPP_NMSO2_PCA_L2. Version 2. OMPS/NPP PCA SO2 Total Column 1-Orbit L2 Swath 50x50km V2. Greenbelt, MD, USA. OMPS_NPP_NMSO2_PCA_L2. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/SO2/DATA205. https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMSO2_PCA_L2_2.html. Digital Science Data.",
-            "issued": "2020-07-29",
-            "temporal": "2012-01-26T21:52:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-07-29",
-            "references": [
-                "https://doi.org/10.5194/amt-10-1495-2017",
-                "https://doi.org/10.5194/amt-10-445-2017",
-                "https://doi.org/10.1002/2013GL058134",
-                "https://doi.org/10.5194/amt-2020-186"
-            ],
-            "keyword": [
-                "climate indicators",
-                "natural hazards",
-                "human dimensions",
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality",
-                "earth science",
-                "paleoclimate indicators"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Can Li, PH. D",
                 "hasEmail": "mailto:can.li@nasa.gov"
             },
+            "creator": "Can Li, Nickolay A. Krotkov, Peter Leonard, Joanna Joiner",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1917909223-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMPS_NPP_NMSO2_PCA_L2 product is part of the MEaSUREs (Making Earth Science Data Records for Use in Research Environments) suite of products.\n\nIt is retrieved from the NASA/NOAA Suomi National Polar-orbiting Partnership (SNPP) Ozone Mapping and Profiler Suite (OMPS) Nadir Mapper (NM) spectrometer and provides contiguous daily global monitoring of anthropogenic and volcanic sulfur dioxide (SO2), an important pollutant and aerosol precursor that affects both air quality and the climate. The product is based on the NASA Goddard Space Flight Center principal component analysis (PCA) spectral fitting algorithm (Li et al., 2013, 2017), and continues (Zhang et al., 2017) NASA's Earth Observing System (EOS) standard Aura/Ozone Monitoring Instrument SO2 product (OMSO2). \n\nThe latest OMPS_NPP_NMSO2_PCA_L2 V2 product uses new Jacobian lookup tables and more realistic model based a priori profiles in anthropogenic SO2 retrievals. This helps to more accurately account for the pixel-to-pixel variation in SO2 sensitivity due to different factors such as the vertical distribution of SO2, solar and viewing angles, surface reflectivity, and cloudiness. As compared with the previous OMPS_NPP_NMSO2_PCA_L2 V1.2 product that assumes the same SO2 sensitivity for all OMPS pixels, the new V2 anthropogenic SO2 retrievals have reduced retrieval biases especially over background regions (see Figure 1 for an example). The same updated PCA SO2 retrieval algorithm (Li et al., 2020) is also used to produce the recently released OMSO2 V2 product (doi:10.5067/Aura/OMI/DATA2022). The new OMPS_NPP_NMSO2_PCA_L2 V2 product thus offers enhanced consistency between the NASA EOS standard (OMI) and continuity (OMPS) SO2 data records\n\nSulfur Dioxide (SO2) is a short-lived gas primarily produced by volcanoes, power plants, refineries, metal smelting and burning of fossil fuels. Where SO2 remains near the Earth's surface, it is toxic, causes acid rain, and degrades air quality. Where SO2 is lofted into the free troposphere, it forms aerosols that can alter cloud reflectivity and precipitation. In the stratosphere, volcanic SO2 forms sulfate aerosols that can result in climate change.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_NPP_NMSO2_PCA_L2",
-            "creator": "Can Li, Nickolay A. Krotkov, Peter Leonard, Joanna Joiner",
-            "graphic-preview-description": "Annual mean SO2 vertical column densities (VCDs) in Dobson Units (DU, 1 DU = 2.69 \u00d71016 molecules/cm2) for 2018 from the OMPS_NPP_NMSO2_PCA_L2 V2.0 product. Pixels with large cloud fractions (> 0.3) or solar zenith angles (> 65\u00ba) or near the edge of the swath (rows 1-2 and 35-36 out of 36 OMPS rows) or low sensitivities to SO2 (air mass factor, AMF < 0.3) have been excluded. In addition, days with large volcanic plumes from explosive eruptions have also been excluded. Areas having major anthropogenic SO2 sources (e.g., India, eastern China, the Middle East, and South Africa) or degassing volcanoes (e.g., Kilauea and Etna) can be identified from the map.",
-            "title": "OMPS/NPP PCA SO2 Total Column 1-Orbit L2 Swath 50x50km V2 (OMPS_NPP_NMSO2_PCA_L2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/OMPS_NPP_NMSO2_PCA_L2.v2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FSO2%2FDATA205",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FSO2%2FDATA205",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/OMPS_NPP_NMSO2_PCA_L2.v2.png",
-                    "description": "Annual mean SO2 vertical column densities (VCDs) in Dobson Units (DU, 1 DU = 2.69 \u00d71016 molecules/cm2) for 2018 from the OMPS_NPP_NMSO2_PCA_L2 V2.0 product. Pixels with large cloud fractions (> 0.3) or solar zenith angles (> 65\u00ba) or near the edge of the swath (rows 1-2 and 35-36 out of 36 OMPS rows) or low sensitivities to SO2 (air mass factor, AMF < 0.3) have been excluded. In addition, days with large volcanic plumes from explosive eruptions have also been excluded. Areas having major anthropogenic SO2 sources (e.g., India, eastern China, the Middle East, and South Africa) or degassing volcanoes (e.g., Kilauea and Etna) can be identified from the map. ",
                     "@type": "dcat:Distribution",
+                    "description": "Annual mean SO2 vertical column densities (VCDs) in Dobson Units (DU, 1 DU = 2.69 \u00d71016 molecules/cm2) for 2018 from the OMPS_NPP_NMSO2_PCA_L2 V2.0 product. Pixels with large cloud fractions (> 0.3) or solar zenith angles (> 65\u00ba) or near the edge of the swath (rows 1-2 and 35-36 out of 36 OMPS rows) or low sensitivities to SO2 (air mass factor, AMF < 0.3) have been excluded. In addition, days with large volcanic plumes from explosive eruptions have also been excluded. Areas having major anthropogenic SO2 sources (e.g., India, eastern China, the Middle East, and South Africa) or degassing volcanoes (e.g., Kilauea and Etna) can be identified from the map. ",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/OMPS_NPP_NMSO2_PCA_L2.v2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMSO2_PCA_L2_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMSO2_PCA_L2_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/SO2/OMPS_NPP_NMSO2_PCA_L2.2",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/SO2/OMPS_NPP_NMSO2_PCA_L2.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/SO2/OMPS_NPP_NMSO2_PCA_L2.2",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/SO2/OMPS_NPP_NMSO2_PCA_L2.2",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMSO2_PCA_L2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMSO2_PCA_L2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://so2.gsfc.nasa.gov/",
-                    "description": "Global Sulfur Dioxide Monitoring Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Global Sulfur Dioxide Monitoring Home Page",
+                    "downloadURL": "https://so2.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/README.OMPS_NPP_NMSO2_PCA_L2.v2.pdf",
-                    "description": "README document",
                     "@type": "dcat:Distribution",
+                    "description": "README document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/README.OMPS_NPP_NMSO2_PCA_L2.v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "Annual mean SO2 vertical column densities (VCDs) in Dobson Units (DU, 1 DU = 2.69 \u00d71016 molecules/cm2) for 2018 from the OMPS_NPP_NMSO2_PCA_L2 V2.0 product. Pixels with large cloud fractions (> 0.3) or solar zenith angles (> 65\u00ba) or near the edge of the swath (rows 1-2 and 35-36 out of 36 OMPS rows) or low sensitivities to SO2 (air mass factor, AMF < 0.3) have been excluded. In addition, days with large volcanic plumes from explosive eruptions have also been excluded. Areas having major anthropogenic SO2 sources (e.g., India, eastern China, the Middle East, and South Africa) or degassing volcanoes (e.g., Kilauea and Etna) can be identified from the map.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/OMPS_NPP_NMSO2_PCA_L2.v2.png",
+            "identifier": "C1917909223-GES_DISC",
+            "issue-identification": "OMPS_NPP_NMSO2_PCA_L2",
+            "issued": "2020-07-29",
+            "keyword": [
+                "climate indicators",
+                "natural hazards",
+                "human dimensions",
+                "atmospheric chemistry",
+                "atmosphere",
+                "air quality",
+                "earth science",
+                "paleoclimate indicators"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/SO2/DATA205",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-07-29",
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
+            "series-name": "OMPS_NPP_NMSO2_PCA_L2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-26T21:52:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS/NPP PCA SO2 Total Column 1-Orbit L2 Swath 50x50km V2 (OMPS_NPP_NMSO2_PCA_L2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-E-HRII-3%2F4-EPOXI-EARTH-V1.0",
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
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set set contains version 1.0 of calibrated, 1.05- to 4.8-micron spectra of Earth acquired by the High Resolution Infrared Spectrometer (HRII) during the EPOCh phase of the EPOXI mission. Three sets of observations were acquired on 18-19 March, 28-29 May, and 4-5 June 2008 to characterize Earth as an analog for extrasolar planets. Each observing period lasted approximately 24 hours, and spectra were acquired twice per hour. During the observing period in May, the Moon transited across Earth as seen from the spacecraft. Additional Earth observations are planned for the mission, and these data will be added to a future version of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-e-hrii-3-4-epoxi-earth-v1.0_cybx-eupe",
+            "issued": "2018-06-26",
+            "keyword": [
+                "epoxi",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-E-HRII-3%2F4-EPOXI-EARTH-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-e-hrii-3-4-epoxi-earth-v1.0_cybx-eupe",
-            "description": "This data set set contains version 1.0 of calibrated, 1.05- to 4.8-micron spectra of Earth acquired by the High Resolution Infrared Spectrometer (HRII) during the EPOCh phase of the EPOXI mission. Three sets of observations were acquired on 18-19 March, 28-29 May, and 4-5 June 2008 to characterize Earth as an analog for extrasolar planets. Each observing period lasted approximately 24 hours, and spectra were acquired twice per hour. During the observing period in May, the Moon transited across Earth as seen from the spacecraft. Additional Earth observations are planned for the mission, and these data will be added to a future version of this data set.",
-            "title": "EPOXI EARTH OBS - HRII CALIBRATED SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI EARTH OBS - HRII CALIBRATED SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/DOPPLER/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Griffin, Nancy F.2002. CAMEX-4 NOAA WP-3D RADAR [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/DOPPLER/DATA101",
-            "issued": "2002-12-20",
-            "temporal": "2001-09-03T15:17:13Z/2001-09-19T20:41:41Z",
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
-            "identifier": "C1995553989-GHRC_DAAC",
             "description": "The CAMEX-4 NPAA WP-3D Radar dataset used the NOAA WP-3D Orion aircraft, which has two separate research radars to collect meteorological data. One is mounted on the lower fuselage (C-band), and the other is located in the tail (X-band). CAMEX-4 focused on the study of tropical cyclone (hurricane) development, tracking, intensification, and landfalling impacts using NASA-funded aircraft and surface remote sensing instrumentation. Data from these radars consist of reflectivity in range and azimuth coordinates collected either in the horizontal (lower fuselage) or vertical (tail radar) planes. Doppler radial velocity is also collected by the tail radar.  For further information and to obtain this data, please contact GHRC at support-ghrc@earthdata.nasa.gov",
-            "title": "CAMEX-4 NOAA WP-3D RADAR V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FDOPPLER%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FDOPPLER%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/CAMEX-4/DOPPLER/DATA101",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "http://dx.doi.org/10.5067/CAMEX-4/DOPPLER/DATA101",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4p3rad/c4p3rad_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4p3rad/c4p3rad_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4p3rad/NOAA_P3_Radar2.pdf",
-                    "description": "ROS SECTION 2 Tape Format",
                     "@type": "dcat:Distribution",
+                    "description": "ROS SECTION 2 Tape Format",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4p3rad/NOAA_P3_Radar2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4p3rad/NOAA_P3_Radar.doc",
-                    "description": "NOAA P-3 RADAR DATA/AOC STANDARD TAPES",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA P-3 RADAR DATA/AOC STANDARD TAPES",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4p3rad/NOAA_P3_Radar.doc",
+                    "mediaType": "application/msword",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4p3rad/subr.f",
-                    "description": "AOC STANDARD TAPE READING SUBROUTINEs",
                     "@type": "dcat:Distribution",
+                    "description": "AOC STANDARD TAPE READING SUBROUTINEs",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4p3rad/subr.f",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
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
+            "identifier": "C1995553989-GHRC_DAAC",
+            "issued": "2002-12-20",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/DOPPLER/DATA101",
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
+            "temporal": "2001-09-03T15:17:13Z/2001-09-19T20:41:41Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 NOAA WP-3D RADAR V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/GOES/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hood, Robbie E and Matthew  Smith.2002. CAMEX-4 GOES-8 PRODUCTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/GOES/DATA101",
-            "issued": "2002-11-06",
-            "temporal": "2001-08-03T00:00:00Z/2001-09-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "visible wavelengths",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "atmospheric water vapor"
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
-            "identifier": "C1979102757-GHRC_DAAC",
             "description": "The CAMEX-4 GOES-8 Products dataset was collected during the CAMEX-4 field campaign, which ocused on the study of tropical cyclone (hurricane) development, tracking, intensification, and landfalling impacts using NASA-funded aircraft and surface remote sensing instrumentation. In support of the fourth Convection and Moisture Experiment (CAMEX-4), imagery from the Geostationary Operational Environmental Satellite 8 (GOES-8) was collected and archived. Three channels were archived: channel 1-- visible (0.65 microns), channel 2-- infrared (11 microns) and channel 3-- known as the water vapor channel (6.75 microns). Data files are available in McIDAS format, and browse imagery is also available.",
-            "graphic-preview-description": "N/A",
-            "title": "CAMEX-4 GOES-8 PRODUCTS V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FGOES%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FGOES%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4sg8",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4sg8",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/vis/c4sg8B_vs_2001.218_1045.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/vis/c4sg8B_vs_2001.218_1045.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/ir4/c4sg8B_ir_2001.218_0615.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/ir4/c4sg8B_ir_2001.218_0615.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/wv/c4sg8B_wv_2001.218_0645.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/wv/c4sg8B_wv_2001.218_0645.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4sg8/c4sg8_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4sg8/c4sg8_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/GOES8/browse/",
+            "identifier": "C1979102757-GHRC_DAAC",
+            "issued": "2002-11-06",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "visible wavelengths",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/GOES/DATA101",
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
             "spatial": "-130.0 15.0 -10.0 75.0",
+            "temporal": "2001-08-03T00:00:00Z/2001-09-21T23:59:59Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 GOES-8 PRODUCTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-2-EDR-V1.1",
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
-                "mars global surveyor",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "All level zero accelerometer data are packaged by periapsis number for each aerobraking orbit. Each orbit is identified by a folder with name Pyyyy where 'yyyy' is the four digit periapsis number. Level 0 z-axis accelerometer data are provided every 0.1 seconds during an interval of time that generally assures that the initial and final data points are taken at least 200 km above the surface of Mars. Additional data, required to reduce accelerometer counts to acceleration on the spacecraft, are provided at lower sampling rates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-2-edr-v1.1_cyd2-e2ee",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-2-EDR-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-2-edr-v1.1_cyd2-e2ee",
-            "description": "All level zero accelerometer data are packaged by periapsis number for each aerobraking orbit. Each orbit is identified by a folder with name Pyyyy where 'yyyy' is the four digit periapsis number. Level 0 z-axis accelerometer data are provided every 0.1 seconds during an interval of time that generally assures that the initial and final data points are taken at least 200 km above the surface of Mars. Additional data, required to reduce accelerometer counts to acceleration on the spacecraft, are provided at lower sampling rates.",
-            "title": "MGS ACCELEROMETER RAW DATA RECORDS V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS ACCELEROMETER RAW DATA RECORDS V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-2-EDR-EROS%2FORBIT-V1.0",
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
+            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-2-edr-eros-orbit-v1.0_cyjx-pp9d",
+            "issued": "2021-05-21",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-2-EDR-EROS%2FORBIT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-2-edr-eros-orbit-v1.0_cyjx-pp9d",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR NLR DATA FOR EROS/ORBIT",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR NLR DATA FOR EROS/ORBIT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NIMBUS/NmTHIR67-1H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus Temperature-Humidity Infrared Radiometer 6.7 \u00b5m Water Vapor Swath L1, HDF5 V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NIMBUS/NmTHIR67-1H.",
-            "issued": "1970-05-10",
-            "temporal": "1970-05-10T00:00:00Z/1971-03-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1971-03-25",
-            "keyword": [
-                "atmospheric water vapor",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
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
-            "identifier": "C1701077919-NSIDC_ECS",
             "description": "This data set (NmTHIR67-1H) consists of daily, global radiative temperatures measured in the 6.7 \u00b5m window (6.5 \u00b5m - 7.0 \u00b5m) by the Temperature-Humidity Infrared Radiometer (THIR) on board the Nimbus 4 satellite. The THIR 6.7 \u00b5m window was used to map the water vapor distribution in the upper troposphere and stratosphere.",
-            "title": "Nimbus Temperature-Humidity Infrared Radiometer 6.7 \u00b5m Water Vapor Swath L1, HDF5 V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmTHIR67-1H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmTHIR67-1H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR67-1H.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR67-1H.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001320-NSIDC_ECS&m=-32.765625%211.40625%211%211%210%210%2C2&q=NmTHIR67-1H",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001320-NSIDC_ECS&m=-32.765625%211.40625%211%211%210%210%2C2&q=NmTHIR67-1H",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR67-1H/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR67-1H/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR67-1H",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR67-1H",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR67-1H",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR67-1H",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1701077919-NSIDC_ECS",
+            "issued": "1970-05-10",
+            "keyword": [
+                "atmospheric water vapor",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/NIMBUS/NmTHIR67-1H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1971-03-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-05-10T00:00:00Z/1971-03-25T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus Temperature-Humidity Infrared Radiometer 6.7 \u00b5m Water Vapor Swath L1, HDF5 V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/cykx-2qix",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Robert Michael Swan",
+                "hasEmail": "mailto:robert.m.swan@jpl.nasa.gov"
+            },
+            "description": "This dataset was built for training and validating terrain classification models for Mars, which may be useful in future autonomous rover efforts. It consists of ~326K semantic segmentation full image labels on 35K images from Curiosity, Opportunity, and Spirit rovers, collected through crowdsourcing. Each image was labeled by 10 people to ensure greater quality and agreement of the crowdsourced labels. It also includes ~1.5K validation labels annotated by the rover planners and scientists from NASA\u2019s MSL (Mars Science Laboratory) mission, which operates the Curiosity rover, and MER (Mars Exploration Rovers) mission, which operated the Spirit and Opportunity rovers.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.nasa.gov/download/cykx-2qix/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://data.nasa.gov/api/views/cykx-2qix",
             "issued": "2021-05-11",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
             "keyword": [
                 "citizen science",
                 "mer-b",
@@ -620477,504 +620488,467 @@
                 "mer-a",
                 "autonomous"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Robert Michael Swan",
-                "hasEmail": "mailto:robert.m.swan@jpl.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/cykx-2qix",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:011"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA JPL"
             },
-            "identifier": "https://data.nasa.gov/api/views/cykx-2qix",
-            "description": "This dataset was built for training and validating terrain classification models for Mars, which may be useful in future autonomous rover efforts. It consists of ~326K semantic segmentation full image labels on 35K images from Curiosity, Opportunity, and Spirit rovers, collected through crowdsourcing. Each image was labeled by 10 people to ensure greater quality and agreement of the crowdsourced labels. It also includes ~1.5K validation labels annotated by the rover planners and scientists from NASA\u2019s MSL (Mars Science Laboratory) mission, which operates the Curiosity rover, and MER (Mars Exploration Rovers) mission, which operated the Spirit and Opportunity rovers.",
-            "title": "AI4MARS: A Dataset for Terrain-Aware Autonomous Driving on Mars",
-            "programCode": [
-                "026:011"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.nasa.gov/download/cykx-2qix/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "AI4MARS: A Dataset for Terrain-Aware Autonomous Driving on Mars"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL2ASLS_L2.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2019-06-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MISR/MIL2ASLS_L2.002. https://asdc.larc.nasa.gov/project/MISR.",
-            "issued": "2004-03-31",
-            "temporal": "2000-02-24T00:00:00Z/2017-06-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-02-22",
-            "keyword": [
-                "atmospheric radiation",
-                "vegetation",
-                "earth science",
-                "atmosphere",
-                "land use/land cover",
-                "land surface",
-                "biosphere"
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
-            "identifier": "C43677707-LARC",
             "description": "MIL2ASLS_2 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 2 Land Surface parameters version 2 data product. It contains a variety of information on the Earth's surface; such ashemispherical directional reflectance factor (HDRF), bihemispherical reflectance (BHR) (i.e., albedo), bidirectional reflectance factor (BRF), directional hemispherical reflectance (DHR), BRF model parameters, Fractional absorbed Photosysenthetically Active Radiation (FPAR), and terrain-referenced view and illumination angles. A surface retrieval is conducted on regions for which valid land aerosol retrieval exists. The retrieval is performed using the corrected equivalent reflectances, retrieved aerosol parameters, and auxiliary information from the Simulated MISR Ancillary Radiative Transfer (SMART) dataset. The spectral and Photosynthetically Active spectral Region (PAR)-integrated BHR and DHR are retrieved, along with the spectral land HDRF and BRF and BRF model parameters, for all valid land and inland water subregions. Subregion surface classification and leaf area index (LAI) and regional FPAR are also determined. Subregion variability is also calculated for land regions. Data collection for this product was completed in June 2017.\r\rThe MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward, and four cameras pointing aftward. It takes seven minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally Gaussian, centered at 443, 555, 670, and 865 nm.\r\rMISR itself is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the affects of sunlight on Earth, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 2 Surface parameters V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL2ASLS_L2.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL2ASLS_L2.002",
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
-                    "description": "Data Product Specification for MISR - Revision S, April 15, 2011   ",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR - Revision S, April 15, 2011   ",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MIL2ASLS_L2.002",
-                    "description": "DOI data set landing page for MIL2ASLS_2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MIL2ASLS_2",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MIL2ASLS_L2.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/ecs_pge_history_L2_PR.cgi",
-                    "description": "MISR Level 2 Current Production Report",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 2 Current Production Report",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/ecs_pge_history_L2_PR.cgi",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L2_AS_Products.pdf",
-                    "description": "MISR Level 2 Aerosol/Surface Products Quality Statement - July 01, 2014",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 2 Aerosol/Surface Products Quality Statement - July 01, 2014",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L2_AS_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_LAND_V023.20180125.pdf",
-                    "description": "Data Product Specification for the MISR Level 2 Land Surface Product - Incorporating the Science Data Processing Interface Control Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for the MISR Level 2 Land Surface Product - Incorporating the Science Data Processing Interface Control Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_LAND_V023.20180125.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C43677707-LARC",
-                    "description": "Earthdata Search for MIL2ASLS_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MIL2ASLS_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C43677707-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MIL2ASLS.002/",
-                    "description": "ASDC Direct Data Download for MIL2ASLS_2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MIL2ASLS_2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MIL2ASLS.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MIL2ASLS.002/contents.html",
-                    "description": "OPeNDAP data access for MIL2ASLS_2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MIL2ASLS_2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MIL2ASLS.002/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/meteosat_ncep_dx_table.doc",
-                    "description": "MISR User Definitions - Direct File Download (.doc)",
                     "@type": "dcat:Distribution",
+                    "description": "MISR User Definitions - Direct File Download (.doc)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/meteosat_ncep_dx_table.doc",
+                    "mediaType": "application/msword",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR_BROWSE_INFO/",
-                    "description": "MISR Browse Tool",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Browse Tool",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR_BROWSE_INFO/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc.html",
-                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc.html",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/ecs_pge_history_L2new_PR.cgi",
-                    "description": "MISR Level 2 New Production Report",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 2 New Production Report",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/ecs_pge_history_L2new_PR.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/LarcECSColL2Products.cgi",
-                    "description": "MISR Processing Status: Level 2 Products",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Processing Status: Level 2 Products",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/LarcECSColL2Products.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/misr_loc/misr_date_orbit.cgi",
-                    "description": "MISR Orbit Tool",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Orbit Tool",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/misr_loc/misr_date_orbit.cgi",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/Mission/",
-                    "description": "MISR Mission Overview",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Mission Overview",
+                    "downloadURL": "https://misr.jpl.nasa.gov/Mission/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
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
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/tracking",
-                    "description": "NASA Earth Observatory Article: Tracking Clouds\u00a0-\u00a0Tune in to the evening weather report on any given day, and you'll no doubt see satellite images of clouds.",
+                {
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge9.html",
-                    "description": "ASDC overview of MISR Level 2 Aerosol and Land Versioning for Aerosol and Land Surface Products",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC overview of MISR Level 2 Aerosol and Land Versioning for Aerosol and Land Surface Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge9.html",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v42_RevP.pdf",
-                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007 ",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007 ",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v42_RevP.pdf",
+                    "mediaType": "application/pdf",
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
+            "identifier": "C43677707-LARC",
+            "issued": "2004-03-31",
+            "keyword": [
+                "atmospheric radiation",
+                "vegetation",
+                "earth science",
+                "atmosphere",
+                "land use/land cover",
+                "land surface",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL2ASLS_L2.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-02-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2017-06-01T23:59:59Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 2 Surface parameters V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL5P/S5P_L1B_RA_BD5_HiR.1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2019-08-06. S5P_L1B_RA_BD5_HiR. Version 1. Sentinel-5P TROPOMI L1B Radiance product band 5 (NIR detector) 5.5km x 3.5km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/SENTINEL5P/S5P_L1B_RA_BD5_HiR.1. https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD5_HiR_1.html. Digital Science Data.",
-            "issued": "2014-12-09",
-            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-09",
-            "keyword": [
-                "platform characteristics",
-                "ultraviolet wavelengths",
-                "atmospheric radiation",
-                "earth science",
-                "sensor characteristics",
-                "spectral/engineering",
-                "atmosphere"
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
-            "identifier": "C1627516271-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L1B_RA_BD5_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L1B_RA_BD5_HiR",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Radiance product band 5 (NIR detector) L1B 5.5km x 3.5km V1 (S5P_L1B_RA_BD5_HiR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_RA_BD5_HiR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L1B_RA_BD5_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL5P%2FS5P_L1B_RA_BD5_HiR.1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL5P%2FS5P_L1B_RA_BD5_HiR.1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -620984,766 +620958,803 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD5_HiR_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD5_HiR_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD5_HiR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD5_HiR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD5_HiR.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD5_HiR.1/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_RA_BD5_HiR_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_RA_BD5_HiR_1",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_RA_BD5_HiR_1.png",
+            "identifier": "C1627516271-GES_DISC",
+            "issued": "2014-12-09",
+            "keyword": [
+                "platform characteristics",
+                "ultraviolet wavelengths",
+                "atmospheric radiation",
+                "earth science",
+                "sensor characteristics",
+                "spectral/engineering",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL5P/S5P_L1B_RA_BD5_HiR.1",
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
+            "series-name": "S5P_L1B_RA_BD5_HiR",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Radiance product band 5 (NIR detector) L1B 5.5km x 3.5km V1 (S5P_L1B_RA_BD5_HiR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SR-VIMS-4%2F5-OCC-V2.0",
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
-                "s rings"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains derived\nradial occultation profiles of the rings of Saturn based on stellar\noccultations made with the Cassini VIMS instrument during the Cassini\nnominal mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sr-vims-4-5-occ-v2.0_cysz-pryk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "s rings"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SR-VIMS-4%2F5-OCC-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sr-vims-4-5-occ-v2.0_cysz-pryk",
-            "description": "This data set contains derived\nradial occultation profiles of the rings of Saturn based on stellar\noccultations made with the Cassini VIMS instrument during the Cassini\nnominal mission.",
-            "title": "CASSINI SATURN VIMS RING OCC 2005-2009",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI SATURN VIMS RING OCC 2005-2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/SOUNDING/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Waldstreicher, Jeff  and Stacy  Brodzik.2022. NOAA Soundings IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/SOUNDING/DATA201",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:00:00Z/2020-02-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "atmosphere",
-                "altitude",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric pressure"
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
-            "identifier": "C1995866540-GHRC_DAAC",
             "description": "The NOAA Soundings IMPACTS dataset was collected from January 1, 2020 through February 29, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign. The goal of IMPACTS was to provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution, examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands, and improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. These radiosonde data files include wind direction, dew point temperature, geopotential height, mixing ratio, atmospheric pressure, relative humidity, wind speed, temperature, potential temperature, equivalent potential temperature, and virtual potential temperature measurements at various levels of the troposphere. The data are available in netCDF-4 format.",
-            "title": "NOAA Soundings IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FSOUNDING%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FSOUNDING%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=noaasndimpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=noaasndimpacts",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.weather.gov/upperair/factsheet",
-                    "description": "Radiosonde Observations",
                     "@type": "dcat:Distribution",
+                    "description": "Radiosonde Observations",
+                    "downloadURL": "https://www.weather.gov/upperair/factsheet",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.weather.gov/upperair",
-                    "description": "Upper Air Observations",
                     "@type": "dcat:Distribution",
+                    "description": "Upper Air Observations",
+                    "downloadURL": "https://www.weather.gov/upperair",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.weather.gov/upperair/radiosonde",
-                    "description": "Weather Balloon Instrument/Radiosonde Information",
                     "@type": "dcat:Distribution",
+                    "description": "Weather Balloon Instrument/Radiosonde Information",
+                    "downloadURL": "https://www.weather.gov/upperair/radiosonde",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nws.noaa.gov/ops2/ops22/sfsc%20html/DCS%20Test%20Plan%20with%20Attachments.pdf",
-                    "description": "Upper Air Data Continuity Study Test Plan for the Sippican B2 and Vaisala RS92 NGP Radiosondes",
                     "@type": "dcat:Distribution",
+                    "description": "Upper Air Data Continuity Study Test Plan for the Sippican B2 and Vaisala RS92 NGP Radiosondes",
+                    "downloadURL": "http://www.nws.noaa.gov/ops2/ops22/sfsc%20html/DCS%20Test%20Plan%20with%20Attachments.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/Vaisala%20Radiosonde%20RS92%20Users%20Guide_M210295EN-J.pdf",
-                    "description": "Vaisala Radiosonde RS92-SGP User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Vaisala Radiosonde RS92-SGP User\u2019s Guide",
+                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/Vaisala%20Radiosonde%20RS92%20Users%20Guide_M210295EN-J.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NOAA_soundings/doc/noaasndimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NOAA_soundings/doc/noaasndimpacts_dataset.pdf",
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
+            "identifier": "C1995866540-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "atmosphere",
+                "altitude",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/SOUNDING/DATA201",
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
             "spatial": "-93.5747 32.885 -69.9489 44.9175",
+            "temporal": "2020-01-01T00:00:00Z/2020-02-29T23:59:59Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA Soundings IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D04.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Parameter 1 Band 2 Daily L3 Global 30 ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D04.061. https://doi.org/10.5067/MODIS/MCD43D04.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "surface radiative properties",
-                "ngda",
-                "earth science",
-                "land surface",
-                "national geospatial data asset"
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
-            "identifier": "C2532014841-LPCLOUD",
-            "description": "The MCD43D04 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter data set is a daily 16-day product. This product incorporates the Climate Modeling Grid (CMG) structure in which each file geographically covers the entire earth rather than the 10 degree x 10 degree latitude and longitude tiling system utilized by the standard MODIS land products. Unlike the standard CMG pixel resolution of 5600 meters the MCD43D products are 1000 meters, consequently, because of the large file size each product contains just one layer. The Julian date in the granule ID of each specific file represents the 9th day of the 16 day composite period, and consequently the observations are weighted to estimate the BRDF/Albedo for that day. The layer in the MCD43D04 is the Bidirectional Reflectance Distribution Function isotropic parameter for MODIS band 2. This isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the Albedo and BRDF value for MODIS band 2.",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter 1 Band 2 Daily L3 Global 30 ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D04 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter data set is a daily 16-day product. This product incorporates the Climate Modeling Grid (CMG) structure in which each file geographically covers the entire earth rather than the 10 degree x 10 degree latitude and longitude tiling system utilized by the standard MODIS land products. Unlike the standard CMG pixel resolution of 5600 meters the MCD43D products are 1000 meters, consequently, because of the large file size each product contains just one layer. The Julian date in the granule ID of each specific file represents the 9th day of the 16 day composite period, and consequently the observations are weighted to estimate the BRDF/Albedo for that day. The layer in the MCD43D04 is the Bidirectional Reflectance Distribution Function isotropic parameter for MODIS band 2. This isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the Albedo and BRDF value for MODIS band 2.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D04.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D04.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D04.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D04.061",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D04.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D04.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2532014841-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2532014841-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD43D04.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD43D04.061/contents.html",
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
-                    "downloadURL": "https://www.umb.edu/spectralmass/terra_aqua_modis/v061",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/terra_aqua_modis/v061",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D04",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D04",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43D04",
-                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43D04",
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
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aquaTerra&ver=C61",
-                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aquaTerra&ver=C61",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 }
             ],
+            "identifier": "C2532014841-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "surface radiative properties",
+                "ngda",
+                "earth science",
+                "land surface",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D04.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter 1 Band 2 Daily L3 Global 30 ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/918/",
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
-            "identifier": "DASHLINK_918",
             "description": "Ballscrew jam fault datasets (diagnostic and prognostic)",
-            "title": "2010_09_12 Lab",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-zip-compressed",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_12.zip",
-                    "description": "2010_09_12.zip",
                     "@type": "dcat:Distribution",
+                    "description": "2010_09_12.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_12.zip",
+                    "mediaType": "application/x-zip-compressed",
                     "title": "2010_09_12.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_918",
+            "issued": "2014-07-02",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/918/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "2010_09_12 Lab"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-MAG-4-48.0SEC",
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
+            "description": "This data set includes Voyager 1 Saturn encounter magnetometer data that have been resampled at a 48.0 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus Saturn Longitude System (-SLS). All of the magnetic field data are calibrated (see the instrument calibration description for more details). The SLS coordinate system is defined in Desch and Kaiser, 1981 and the reference documents for this dataset are: Ness et al, 1982 Acuna,Connerney,and Ness, 1983 Connerney,Acuna,and Ness, 1983 Behannon,Lepping,and Ness, 1983",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-mag-4-48.0sec_cyx4-a32w",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-MAG-4-48.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-mag-4-48.0sec_cyx4-a32w",
-            "description": "This data set includes Voyager 1 Saturn encounter magnetometer data that have been resampled at a 48.0 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus Saturn Longitude System (-SLS). All of the magnetic field data are calibrated (see the instrument calibration description for more details). The SLS coordinate system is defined in Desch and Kaiser, 1981 and the reference documents for this dataset are: Ness et al, 1982 Acuna,Connerney,and Ness, 1983 Connerney,Acuna,and Ness, 1983 Behannon,Lepping,and Ness, 1983",
-            "title": "VOYAGER 1 SATURN MAGNETOMETER RESAMPLED DATA 48.0 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 SATURN MAGNETOMETER RESAMPLED DATA 48.0 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/NGLI_LAKE_BOURNE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/NGLI_LAKE_BOURNE/DATA001.",
-            "issued": "2001-04-18",
-            "temporal": "2001-04-18T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "earth science",
-                "ocean temperature",
-                "ocean optics",
-                "oceans",
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
-            "identifier": "C1633360520-OB_DAAC",
             "description": "Measurements made under the Northern Gulf Littoral Initiative (NGLI) in the Gulf of Mexico near the Mississippi River outflow region in 2001.",
-            "title": "Northern Gulf Littoral Initiative (NGLI) measurements in Lake Bourne, Louisiana",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FNGLI_LAKE_BOURNE%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FNGLI_LAKE_BOURNE%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/NGLI_Lake_Bourne/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/NGLI_Lake_Bourne/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360520-OB_DAAC",
+            "issued": "2001-04-18",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "ocean temperature",
+                "ocean optics",
+                "oceans",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/NGLI_LAKE_BOURNE/DATA001",
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
+            "temporal": "2001-04-18T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Northern Gulf Littoral Initiative (NGLI) measurements in Lake Bourne, Louisiana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-4-EAR2-EARTH-REFLECT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the EARTH SWING-BY 2 mission phase, covering the period  from 2007-09-13T00:00:00.000 to 2008-01-27T23:59:59.000. The prime target is planet Earth. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-4-ear2-earth-reflect-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "moon",
                 "international rosetta mission",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-4-EAR2-EARTH-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-4-ear2-earth-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the EARTH SWING-BY 2 mission phase, covering the period  from 2007-09-13T00:00:00.000 to 2008-01-27T23:59:59.000. The prime target is planet Earth. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER EARTH OSINAC 4 EAR2 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH OSINAC 4 EAR2 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0480-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-09T00:52:20.000 to 2014-12-09T12:45:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0480-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0480-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0480-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-09T00:52:20.000 to 2014-12-09T12:45:59.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0480 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0480 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1073",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stackhouse, P.W., S.K. Gupta, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2012. ISLSCP II Cloud and Meteorology Parameters. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1073",
-            "issued": "2023-10-15",
-            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
-            "keyword": [
-                "earth science",
-                "clouds",
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
-            "identifier": "C2785316430-ORNL_CLOUD",
             "description": "This data set contains cloud and meteorology data on a 1.0 degree x 1.0 degree spatial resolution. There are eight data files (*.zip) with this data set for several cloud parameters (monthly only) and meteorological parameters including monthly surface skin temperature, monthly total column ozone, and water vapor burdens for the period 1986-1995. All monthly parameters include files with a monthly mean value, a monthly standard deviation, and monthly minimum and maximum values.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Cloud and Meteorology Parameters",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1073_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1073",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1073",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/radiation_clouds/srb_clouds_1deg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/radiation_clouds/srb_clouds_1deg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/srb_clouds_1deg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/srb_clouds_1deg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1073",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1073",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_clouds_1deg/comp/0_srb_clouds_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_clouds_1deg/comp/0_srb_clouds_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_clouds_1deg/comp/1_srb_radiation_clouds_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_clouds_1deg/comp/1_srb_radiation_clouds_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_clouds_1deg/comp/srb_clouds_1deg.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_clouds_1deg/comp/srb_clouds_1deg.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1073_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1073_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1073",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1073",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1073_1_fit.png",
+            "identifier": "C2785316430-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1073",
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
+            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II Cloud and Meteorology Parameters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESHDOL_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "issued": "2013-03-29",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-10-28",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor"
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
-            "identifier": "C191856315-LARC",
             "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "title": "TES/Aura L2 HDO Limb V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESHDOL_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESHDOL_L2.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C191856315-LARC",
+            "issued": "2013-03-29",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TESHDOL_L2.006",
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
+            "title": "TES/Aura L2 HDO Limb V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/czbk-vrdf",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John M. Kusterer",
+                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
+            },
+            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l3_apro_combined-beta-v1-30_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000131",
             "issued": "2018-06-25",
-            "temporal": "2013-03-01/2014-06-05",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "cloud",
                 "satellite",
@@ -621753,420 +621764,389 @@
                 "climate",
                 "eos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/czbk-vrdf",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000131",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Combined Lidar L3 Data V1-30",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l3_apro_combined-beta-v1-30_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2013-03-01/2014-06-05",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Combined Lidar L3 Data V1-30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4PN93PB",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2018-12-31. Gridded Population of the World, Version 4 (GPWv4): Population Count Adjusted to Match 2015 Revision of UN WPP Country Totals, Revision 11. Version 4.11. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4PN93PB. https://doi.org/10.7927/H4PN93PB.",
-            "issued": "2018-12-31",
-            "temporal": "2000-07-01T00:00:00Z/2020-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-31",
-            "references": [
-                "https://doi.org/10.1080/23754931.2015.1014272",
-                "https://doi.org/10.7927/H4BC3WMT",
-                "https://doi.org/10.7927/H42Z13KG",
-                "https://doi.org/10.7927/H4Z60M4Z",
-                "https://doi.org/10.7927/H4TD9VDP",
-                "https://doi.org/10.7927/H4JW8BX5",
-                "https://doi.org/10.7927/H49C6VHW",
-                "https://doi.org/10.7927/H45Q4T5F",
-                "https://doi.org/10.7927/H46M34XX",
-                "https://doi.org/10.7927/H4F47M65",
-                "https://doi.org/10.7927/H4JQ0XZW"
-            ],
-            "keyword": [
-                "population",
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
-            "identifier": "C1597158382-SEDAC",
-            "description": "The Gridded Population of the World, Version 4 (GPWv4): Population Count Adjusted to Match 2015 Revision of UN WPP Country Totals, Revision 11 consists of estimates of human population (number of persons per pixel) consistent with national censuses and population registers with respect to relative spatial distribution, but adjusted to match the 2015 Revision of the United Nation's World Population Prospects (UN WPP) country totals for the years 2000, 2005, 2010, 2015, and 2020.\u00ef\u00bf\u00bdA proportional allocation gridding algorithm, utilizing approximately 13.5 million national and sub-national administrative Units, was used to assign population counts to 30 arc-second grid cells. The data files were produced as global rasters at 30 arc-second (~1 km at the equator) resolution. To enable faster global processing, and in support of research commUnities, the 30 arc-second adjusted count data were aggregated to 2.5 arc-minute, 15 arc-minute, 30 arc-minute and 1 degree resolutions.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Gridded Population of the World, Version 4 (GPWv4): Population Count Adjusted to Match 2015 Revision of UN WPP Country Totals, Revision 11",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Gridded Population of the World, Version 4 (GPWv4): Population Count Adjusted to Match 2015 Revision of UN WPP Country Totals, Revision 11 consists of estimates of human population (number of persons per pixel) consistent with national censuses and population registers with respect to relative spatial distribution, but adjusted to match the 2015 Revision of the United Nation's World Population Prospects (UN WPP) country totals for the years 2000, 2005, 2010, 2015, and 2020.\u00ef\u00bf\u00bdA proportional allocation gridding algorithm, utilizing approximately 13.5 million national and sub-national administrative Units, was used to assign population counts to 30 arc-second grid cells. The data files were produced as global rasters at 30 arc-second (~1 km at the equator) resolution. To enable faster global processing, and in support of research commUnities, the 30 arc-second adjusted count data were aggregated to 2.5 arc-minute, 15 arc-minute, 30 arc-minute and 1 degree resolutions.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4PN93PB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4PN93PB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v4/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11-global-2015-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v4/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11-global-2015-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11/maps",
+            "identifier": "C1597158382-SEDAC",
+            "issued": "2018-12-31",
+            "keyword": [
+                "population",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4PN93PB",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.1080/23754931.2015.1014272",
+                "https://doi.org/10.7927/H4BC3WMT",
+                "https://doi.org/10.7927/H42Z13KG",
+                "https://doi.org/10.7927/H4Z60M4Z",
+                "https://doi.org/10.7927/H4TD9VDP",
+                "https://doi.org/10.7927/H4JW8BX5",
+                "https://doi.org/10.7927/H49C6VHW",
+                "https://doi.org/10.7927/H45Q4T5F",
+                "https://doi.org/10.7927/H46M34XX",
+                "https://doi.org/10.7927/H4F47M65",
+                "https://doi.org/10.7927/H4JQ0XZW"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-07-01T00:00:00Z/2020-07-01T00:00:00Z",
             "theme": [
                 "GPW",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gridded Population of the World, Version 4 (GPWv4): Population Count Adjusted to Match 2015 Revision of UN WPP Country Totals, Revision 11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-BIBLIOGRAPHY-V2.0",
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
+            "description": "Compilation of asteroid and asteroid-related references, covering the period 1621-1993.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-bibliography-v2.0_czmi-k7sg",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-BIBLIOGRAPHY-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-bibliography-v2.0_czmi-k7sg",
-            "description": "Compilation of asteroid and asteroid-related references, covering the period 1621-1993.",
-            "title": "ASTEROID BIBLIOGRAPHY V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID BIBLIOGRAPHY V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-4-LINEARIZED-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-4-linearized-ops-v1.0_czqc-247q",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-4-LINEARIZED-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-4-linearized-ops-v1.0_czqc-247q",
-            "description": "NULL",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA\n                                    LINEARIZED RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS HAZARD AVOID CAMERA\n                                    LINEARIZED RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/LANDMET/ANC004",
             "citation": "William B. Rossow. 2016-12-15. LANDMET_ANC_SM. Version 1. LANDMET Ancillary Soil Moisture data L3 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/LANDMET/ANC004. https://disc.gsfc.nasa.gov/datacollection/LANDMET_ANC_SM_1.html. Digital Science Data.",
-            "issued": "2016-11-22",
-            "temporal": "1998-01-01T00:00:00Z/2007-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-11-22",
-            "keyword": [
-                "agriculture",
-                "ecosystems",
-                "soils",
-                "earth science",
-                "land surface",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SUHUNG SHEN",
                 "hasEmail": "mailto:suhung.shen@nasa.gov"
             },
+            "creator": "William B. Rossow",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1374187876-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This ancillary climatology soil porosity and wetlands coverage information were derived from the daily GEWEX fusion of satellite active and passive microwave measurements. These quantities are re-mapped to a 1.0 degree equal-area grid from the original 0.25 degree equal-angle map grid.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "LANDMET_ANC_SM",
-            "creator": "William B. Rossow",
-            "title": "LANDMET Ancillary Soil Moisture data L3 V1 (LANDMET_ANC_SM) at GES DISC",
-            "graphic-preview-description": "This is a sample image of porosity from ancillary product LANDMET_ANC_SM_L3_v1",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LANDMET_ANC_SM_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FLANDMET%2FANC004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FLANDMET%2FANC004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LANDMET_ANC_SM_1.png",
-                    "description": "This is a sample image of porosity from ancillary product LANDMET_ANC_SM_L3_v1",
                     "@type": "dcat:Distribution",
+                    "description": "This is a sample image of porosity from ancillary product LANDMET_ANC_SM_L3_v1",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LANDMET_ANC_SM_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LANDMET_ANC_SM_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LANDMET_ANC_SM_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/LANDMET/LANDMET_ANC_SM.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/LANDMET/LANDMET_ANC_SM.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LANDMET_ANC_SM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LANDMET_ANC_SM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/LANDMET/LANDMET_ANC_SM.1/contents.html",
-                    "description": "Access to the data via OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access to the data via OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/LANDMET/LANDMET_ANC_SM.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/LANDMET/LANDMET_ANC_SM.1/doc/README.LANDMET_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/LANDMET/LANDMET_ANC_SM.1/doc/README.LANDMET_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "This is a sample image of porosity from ancillary product LANDMET_ANC_SM_L3_v1",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LANDMET_ANC_SM_1.png",
+            "identifier": "C1374187876-GES_DISC",
+            "issued": "2016-11-22",
+            "keyword": [
+                "agriculture",
+                "ecosystems",
+                "soils",
+                "earth science",
+                "land surface",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/LANDMET/ANC004",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-11-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "LANDMET_ANC_SM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1998-01-01T00:00:00Z/2007-12-31T23:59:59Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LANDMET Ancillary Soil Moisture data L3 V1 (LANDMET_ANC_SM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR5-V1.0",
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
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 1 and 3, 2006 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr5-v1.0_czyz-sw53",
+            "issued": "2021-05-21",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR5-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr5-v1.0_czyz-sw53",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 1 and 3, 2006 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
-            "title": "CASSINI RSS RAW DATA SET - TIGR5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TIGR5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-2-LAUNCH-V1.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-2-launch-v1.0_d22s-fyzu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar wind",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-2-LAUNCH-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-2-launch-v1.0_d22s-fyzu",
-            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS SWAP POST-LAUNCH CHECKOUT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS SWAP POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://eros.usgs.gov/imagegallery/landsat-state-mosaics",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "earth science",
-                "images",
-                "usgs",
-                "landsat",
-                "mosaic",
-                "imagery"
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
-            "identifier": "NASA-913",
             "description": "The Earth Resources Observation and Science (EROS) Center manages the this gallery of images of the 50 U.S. states plus Puerto Rico as derived by Landsat data.",
-            "title": "Earth Resources Observation and Science (EROS) Center's Landsat State Mosaics Gallery",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -622174,276 +622154,277 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-913",
+            "issued": "2014-04-29",
+            "keyword": [
+                "earth science",
+                "images",
+                "usgs",
+                "landsat",
+                "mosaic",
+                "imagery"
+            ],
+            "landingPage": "http://eros.usgs.gov/imagegallery/landsat-state-mosaics",
+            "modified": "2020-01-29",
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
+            "title": "Earth Resources Observation and Science (EROS) Center's Landsat State Mosaics Gallery"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/154",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-10-01",
-            "temporal": "2014-10-01T00:00:00Z/2021-09-01T00:00:00Z",
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
-                "jpl irad",
-                "active",
-                "jet propulsion laboratory",
-                "program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Mccleese",
                 "hasEmail": "mailto:daniel.j.mccleese@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "N/A"
-            },
-            "identifier": "TECHPORT_154",
             "description": "&lt;p&gt;Innovative projects are sought in the areas of basic research, fundamental research, applied research, development and systems and other concept formulation studies. Projects combining both science and technology are encouraged.&lt;/p&gt;",
-            "title": "Center Independent Research &amp; Developments: JPL IRAD Program",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/154",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_154",
+            "issued": "2014-10-01",
+            "keyword": [
+                "jpl irad",
+                "active",
+                "jet propulsion laboratory",
+                "program"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/154",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "N/A"
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
+            "temporal": "2014-10-01T00:00:00Z/2021-09-01T00:00:00Z",
+            "title": "Center Independent Research &amp; Developments: JPL IRAD Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR_Volcano_Research/KILVOLC_FlowerKahn2021_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Terra/MISR_Volcano_Research/KILVOLC_FlowerKahn2021_1.",
-            "issued": "2021-02-05",
-            "temporal": "2000-10-25T00:00:00Z/2018-08-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-06",
-            "keyword": [
-                "tectonics",
-                "solid earth",
-                "geomorphic landforms/processes",
-                "earth science",
-                "atmosphere",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ralph Kahn",
                 "hasEmail": "mailto:ralph.a.kahn@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2134682585-LARC_ASDC",
             "description": "The KILVOLC_FlowerKahn2021_1 dataset is the MISR Derived Case Study Data for Kilauea Volcanic Eruptions Including Geometric Plume Height and Qualitative Radiometric Particle Property Information version 1 dataset. It comprises MISR-derived output from a comprehensive analysis of Kilauea volcanic eruptions (2000-2018). Data collection for this dataset is complete. The data presented here are analyzed and discussed in the following paper: Flower, V.J.B., and R.A. Kahn, 2021. Twenty years of NASA-EOS multi-sensor satellite observations at K\u012blauea volcano (2000-2019). J. Volc. Geo. Res. (in press).\r\n\r\nThe data is subdivided by date and MISR orbit number. Within each case folder, there are up to 11 files relating to an individual MISR overpass. Files include plume height records (from both the red and blue spectral bands) derived from the MISR INteractive eXplorer (MINX) program, displayed in: map view, downwind profile plot (along with the associated wind vectors retrieved at plume elevation), a histogram of retrieved plume heights and a text file containing the digital plume height values. An additional JPG is included delineating the plume analysis region, start point for assessing downwind distance, and input wind direction used to initialize the MINX retrieval. A final two files are generated from the MISR Research Aerosol (RA) retrieval algorithm (Limbacher, J.A., and R.A. Kahn, 2014. MISR Research-Aerosol-Algorithm: Refinements For Dark Water Retrievals. Atm. Meas. Tech. 7, 1-19, doi:10.5194/amt-7-1-2014). These files include the RA model output in HDF5, and an associated JPG of key derived variables (e.g. Aerosol Optical Depth, Angstrom Exponent, Single Scattering Albedo, Fraction of Non-Spherical components, model uncertainty classifications and example camera views). \r\n\r\nFile numbers per folder vary depending on the retrieval conditions of specific observations. RA plume retrievals are limited when cloud cover was widespread or the solar radiance was insufficient to run the RA. In these cases the RA files are not included in the individual folders. \r\nIn cases where activity was observed from multiple volcanic zones in a single overpass, individual folders containing data relating to a single region, are included, and defined by a qualifier (e.g. '_1').",
-            "graphic-preview-description": "The MISR INteractive eXplorer (MINX) program, for determining the altitude of plumes and performing particle property analysis using the MISR standard aerosol retrieval product, is a stand-alone software package developed at the NASA Jet Propulsion Laboratory (JPL) and distributed through Github. This program allows the user to ingest the MISR Level 1 data, select regions for analysis and output visualizations of features, like those included in this data set.",
-            "title": "MISR Derived Case Study Data for Kilauea Volcanic Eruptions Including Geometric Plume Height and Qualitative Radiometric Particle Property Information",
-            "graphic-preview-file": "https://github.com/nasa/MINX/releases",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR_Volcano_Research%2FKILVOLC_FlowerKahn2021_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR_Volcano_Research%2FKILVOLC_FlowerKahn2021_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://github.com/nasa/MINX/releases",
-                    "description": "The MISR INteractive eXplorer (MINX) program, for determining the altitude of plumes and performing particle property analysis using the MISR standard aerosol retrieval product, is a stand-alone software package developed at the NASA Jet Propulsion Laboratory (JPL) and distributed through Github. This program allows the user to ingest the MISR Level 1 data, select regions for analysis and output visualizations of features, like those included in this data set.",
                     "@type": "dcat:Distribution",
+                    "description": "The MISR INteractive eXplorer (MINX) program, for determining the altitude of plumes and performing particle property analysis using the MISR standard aerosol retrieval product, is a stand-alone software package developed at the NASA Jet Propulsion Laboratory (JPL) and distributed through Github. This program allows the user to ingest the MISR Level 1 data, select regions for analysis and output visualizations of features, like those included in this data set.",
+                    "downloadURL": "https://github.com/nasa/MINX/releases",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Terra/MISR_Volcano_Research/KILVOLC_FlowerKahn2021_1",
-                    "description": "DOI data set landing page for KILVOLC_FlowerKahn2021_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for KILVOLC_FlowerKahn2021_1",
+                    "downloadURL": "https://doi.org/10.5067/Terra/MISR_Volcano_Research/KILVOLC_FlowerKahn2021_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2134682585-LARC_ASDC",
-                    "description": "Earthdata Search for KILVOLC_FLOWERKAHN2021_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for KILVOLC_FLOWERKAHN2021_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2134682585-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/Volcano_Research/KILVOLC_FlowerKahn2021_1/",
-                    "description": "ASDC Direct Data Download for KILVOLC_FlowerKahn2021_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for KILVOLC_FlowerKahn2021_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/Volcano_Research/KILVOLC_FlowerKahn2021_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-description": "The MISR INteractive eXplorer (MINX) program, for determining the altitude of plumes and performing particle property analysis using the MISR standard aerosol retrieval product, is a stand-alone software package developed at the NASA Jet Propulsion Laboratory (JPL) and distributed through Github. This program allows the user to ingest the MISR Level 1 data, select regions for analysis and output visualizations of features, like those included in this data set.",
+            "graphic-preview-file": "https://github.com/nasa/MINX/releases",
+            "identifier": "C2134682585-LARC_ASDC",
+            "issued": "2021-02-05",
+            "keyword": [
+                "tectonics",
+                "solid earth",
+                "geomorphic landforms/processes",
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR_Volcano_Research/KILVOLC_FlowerKahn2021_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>14.0 -161.0 14.0 -150.0 25.0 -150.0 25.0 -161.0 14.0 -161.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-10-25T00:00:00Z/2018-08-01T23:59:59.999Z",
             "theme": [
                 "MISR_Volcano_Research",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Derived Case Study Data for Kilauea Volcanic Eruptions Including Geometric Plume Height and Qualitative Radiometric Particle Property Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4XW4GQ1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gaffin, S.R., X. Xing, and G. Yetman. 2002-07-31. Country-Level GDP and Downscaled Projections Based on the SRES A1, A2, B1, and B2 Marker Scenarios, 1990-2100. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4XW4GQ1. https://doi.org/10.7927/H4XW4GQ1.",
-            "issued": "2002-07-31",
-            "temporal": "1990-01-01T00:00:00Z/2100-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-07-31",
-            "references": [
-                "https://doi.org/10.7927/H4T43R01",
-                "https://doi.org/10.7927/H4PC308P",
-                "https://doi.org/10.7927/H4NC5Z4X",
-                "https://doi.org/10.7927/H4HQ3WTH"
-            ],
-            "keyword": [
-                "atmosphere",
-                "socioeconomics",
-                "human dimensions",
-                "earth science",
-                "air quality"
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
-            "identifier": "C179001917-SEDAC",
-            "description": "The Country-Level GDP and Downscaled Projections Based on the Special Report on Emissions Scenarios (SRES) A1, A2, B1, and B2 marker scenarios, 1990-2100, were developed using the 1990 base year GDP (Gross Domestic Product) from national accounts database available from the UN Statistics Division. SRES regional GDP growth rates were calculated from 1990 to 2100 based on the SRES marker model regional data and applied uniformly to each country that fell within the SRES-defined regions. This data set is produced and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Gaffin, S.R., X. Xing, and G. Yetman",
-            "title": "Country-Level GDP and Downscaled Projections Based on the SRES A1, A2, B1, and B2 Marker Scenarios, 1990-2100",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/sdp/sdp-downscaled-gdp-a1a2b1b2-1990-2100/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Country-Level GDP and Downscaled Projections Based on the Special Report on Emissions Scenarios (SRES) A1, A2, B1, and B2 marker scenarios, 1990-2100, were developed using the 1990 base year GDP (Gross Domestic Product) from national accounts database available from the UN Statistics Division. SRES regional GDP growth rates were calculated from 1990 to 2100 based on the SRES marker model regional data and applied uniformly to each country that fell within the SRES-defined regions. This data set is produced and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4XW4GQ1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4XW4GQ1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdp/sdp-downscaled-gdp-a1a2b1b2-1990-2100/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdp/sdp-downscaled-gdp-a1a2b1b2-1990-2100/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-gdp-a1a2b1b2-1990-2100/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-gdp-a1a2b1b2-1990-2100/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-gdp-a1a2b1b2-1990-2100/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-gdp-a1a2b1b2-1990-2100/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-gdp-a1a2b1b2-1990-2100",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-gdp-a1a2b1b2-1990-2100",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/sdp/sdp-downscaled-gdp-a1a2b1b2-1990-2100/sedac-logo.jpg",
+            "identifier": "C179001917-SEDAC",
+            "issued": "2002-07-31",
+            "keyword": [
+                "atmosphere",
+                "socioeconomics",
+                "human dimensions",
+                "earth science",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4XW4GQ1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4T43R01",
+                "https://doi.org/10.7927/H4PC308P",
+                "https://doi.org/10.7927/H4NC5Z4X",
+                "https://doi.org/10.7927/H4HQ3WTH"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1990-01-01T00:00:00Z/2100-12-31T00:00:00Z",
             "theme": [
                 "SDP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Country-Level GDP and Downscaled Projections Based on the SRES A1, A2, B1, and B2 Marker Scenarios, 1990-2100"
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
-            "identifier": "NASA-723",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (80)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -622451,216 +622432,244 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-723",
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
+            "title": "PDS Odyssey Radio Science Data (80)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0113",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0113.",
-            "issued": "1999-11-07",
-            "temporal": "1991-11-13T00:00:00Z/1991-12-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-12",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric radiation",
-                "earth science",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID STARR",
                 "hasEmail": "mailto:starr@climate.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001195-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.The PAMS data set was collected during the FIRE Cirrus Phase II experiment from Nov. 13, 1991 to Dec. 7, 1991 at six sites. There are 25 data files for each of 6 sites where PAMS data were collected.",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II Portable Automated Mesonet Station (PAMS) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0113",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0113",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001195-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_PAMS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_PAMS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001195-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_PAMS/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_PAMS_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_PAMS_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_PAMS/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_pams_dataset.pdf",
-                    "description": "FIRE Cirrus 2 Portable Automated Mesonet Station (PAMS) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 Portable Automated Mesonet Station (PAMS) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_pams_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_pams.ps",
-                    "description": "FIRE Cirrus 2 - Direct File Download (.ps) Readme",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 - Direct File Download (.ps) Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_pams.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_lib.c",
-                    "description": "fci2_lib Program for reading FIRE Cirrus II data sets - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "fci2_lib Program for reading FIRE Cirrus II data sets - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_lib.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_sw.c",
-                    "description": "Sample read routines for all FIRE Cirrus II data sets in ASCII format - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read routines for all FIRE Cirrus II data sets in ASCII format - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_sw.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_sw.h",
-                    "description": "Subroutines to read DX data from a DX file - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Subroutines to read DX data from a DX file - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_sw.h",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/genpro.c",
-                    "description": "Program to read GENPRO Formatted Files - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Program to read GENPRO Formatted Files - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/genpro.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci2",
-                    "description": "Makefile.fci2 Release: 1.1 Date: 3/22/94",
                     "@type": "dcat:Distribution",
+                    "description": "Makefile.fci2 Release: 1.1 Date: 3/22/94",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0113",
-                    "description": "DOI data set landing page for FIRE_CI2_PAMS_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_PAMS_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0113",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_PAMS/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_PAMS_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_PAMS_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_PAMS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire2_cirrus/mission_summaries.html",
-                    "description": "ASDC List of FIRE II - Cirrus Mission Summaries Available",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of FIRE II - Cirrus Mission Summaries Available",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire2_cirrus/mission_summaries.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001195-LARC_ASDC",
+            "issued": "1999-11-07",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0113",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>35.66 -97.16 35.66 -95.09 38.01 -95.09 38.01 -97.16 35.66 -97.16</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1991-11-13T00:00:00Z/1991-12-07T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II Portable Automated Mesonet Station (PAMS) Data"
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
+            "description": "Exp: Round Synthetic Jets for Separation Control on 2-D Ramp This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Roundjet/Baseline.tar.gz",
+                    "mediaType": "application/x-gzip"
+                }
             ],
+            "identifier": "NASA-852",
+            "issued": "2018-06-25",
             "keyword": [
                 "turbulence",
                 "separation",
@@ -622672,503 +622681,467 @@
                 "ramp",
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
-            "identifier": "NASA-852",
-            "description": "Exp: Round Synthetic Jets for Separation Control on 2-D Ramp This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: Round Synthetic Jets for Separation Control on 2-D Ramp",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Roundjet/Baseline.tar.gz",
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
+            "title": "Turbulence Models: Data from Other Experiments: Round Synthetic Jets for Separation Control on 2-D Ramp"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/MULTIPLE/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Poellot, Michael R, Andrew J Heymsfield and Aaron  Bansemer.2017. GPM Ground Validation UND Citation Cloud Microphysics OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/MULTIPLE/DATA201",
-            "issued": "2017-09-15",
-            "temporal": "2015-11-12T18:49:13Z/2015-12-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-25",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "atmosphere",
-                "atmospheric water vapor"
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
-            "identifier": "C1979132803-GHRC_DAAC",
             "description": "The GPM Ground Validation UND Citation Cloud Microphysics OLYMPEX dataset includes measurements of cloud microphysics, state of the atmosphere parameters, three-dimensional winds, and turbulence. These measurements were taken during the OLYMPEX campaign by the University of North Dakota\u2019s (UND) Cessna Citation II aircraft over a series of 20 flights totaling roughly 60 flight hours. The UND Citation Cloud Microphysics data are stored as separate files for each flight, with a primary (*.olympex) file containing both direct and derived parameters. Raw data files for each instrument are also archived for investigators who wish to use their own processing software. Data are available from flights that occurred from November 12, 2015 through December 19, 2015 in ASCII, ASCII-csv, and binary formats, while browse images are available in PNG format.",
-            "graphic-preview-description": "Sample Browse Image",
-            "title": "GPM Ground Validation UND Citation Cloud Microphysics OLYMPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/cloud_microphysics_Citation/UND_cloud_microphysics/browse/20151124_155525/CP20151124_161619_333.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FMULTIPLE%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FMULTIPLE%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmcmolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmcmolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/cloud_microphysics_Citation/UND_cloud_microphysics/browse/20151124_155525/CP20151124_161619_333.png",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/cloud_microphysics_Citation/UND_cloud_microphysics/browse/20151124_155525/CP20151124_161619_333.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://olympex.atmos.washington.edu/docs/OLYMPEX_OpsPlan.pdf",
-                    "description": "OLYMPEX Ground Validation Experiment Field Operations Plans (Version 3)",
                     "@type": "dcat:Distribution",
+                    "description": "OLYMPEX Ground Validation Experiment Field Operations Plans (Version 3)",
+                    "downloadURL": "http://olympex.atmos.washington.edu/docs/OLYMPEX_OpsPlan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.scieng.com/pdf/M300Reference.pdf",
-                    "description": "M300 Reference Guide - Description of Instrument Measurement Output",
                     "@type": "dcat:Distribution",
+                    "description": "M300 Reference Guide - Description of Instrument Measurement Output",
+                    "downloadURL": "http://www.scieng.com/pdf/M300Reference.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.specinc.com/sites/default/files/software_and_manuals/2D-S_Technical%20Manual_rev3.1_20110228.pdf",
-                    "description": "2D-S Technical Manual Rev. 3.1: A Two Dimensional, Stereo, Particle Imaging Probe (Also includes Documentation for Model 2D-128)",
                     "@type": "dcat:Distribution",
+                    "description": "2D-S Technical Manual Rev. 3.1: A Two Dimensional, Stereo, Particle Imaging Probe (Also includes Documentation for Model 2D-128)",
+                    "downloadURL": "http://www.specinc.com/sites/default/files/software_and_manuals/2D-S_Technical%20Manual_rev3.1_20110228.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.specinc.com/sites/default/files/software_and_manuals/CPI_Technical%20Manual_rev1.2_20130226.pdf",
-                    "description": "Cloud Particle Image CPD V2.5 User\u2019s Manual",
                     "@type": "dcat:Distribution",
+                    "description": "Cloud Particle Image CPD V2.5 User\u2019s Manual",
+                    "downloadURL": "http://www.specinc.com/sites/default/files/software_and_manuals/CPI_Technical%20Manual_rev1.2_20130226.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.specinc.com/sites/default/files/software_and_manuals/HVPS_Technical%20Manual_rev1.2_20130227.pdf",
-                    "description": "HVPS V3 Technical Manual Rev. 1.2: A High Volume Precipitation Spectrometer",
                     "@type": "dcat:Distribution",
+                    "description": "HVPS V3 Technical Manual Rev. 1.2: A High Volume Precipitation Spectrometer",
+                    "downloadURL": "http://www.specinc.com/sites/default/files/software_and_manuals/HVPS_Technical%20Manual_rev1.2_20130227.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/cloud_microphysics_Citation/UND_cloud_microphysics/doc/gpmcmolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/cloud_microphysics_Citation/UND_cloud_microphysics/doc/gpmcmolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1007/s12145-010-0061-4",
-                    "description": "Airborne Data Processing and Analysis Software Package",
                     "@type": "dcat:Distribution",
+                    "description": "Airborne Data Processing and Analysis Software Package",
+                    "downloadURL": "http://dx.doi.org/10.1007/s12145-010-0061-4",
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
+            "graphic-preview-description": "Sample Browse Image",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/cloud_microphysics_Citation/UND_cloud_microphysics/browse/20151124_155525/CP20151124_161619_333.png",
+            "identifier": "C1979132803-GHRC_DAAC",
+            "issued": "2017-09-15",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "atmosphere",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/MULTIPLE/DATA201",
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
             "spatial": "-126.129 46.2209 -97.1811 48.3535",
+            "temporal": "2015-11-12T18:49:13Z/2015-12-19T23:59:59Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation UND Citation Cloud Microphysics OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1105-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-16T20:31:55.000 to 2015-10-16T23:45:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1105-v1.0_d2nc-eu72",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1105-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1105-v1.0_d2nc-eu72",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-16T20:31:55.000 to 2015-10-16T23:45:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1105 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1105 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-CR2-V1.0",
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
+            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR2 phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-cr2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-CR2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-cr2-v1.0",
-            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR2 phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 CR2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 CR2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC1-67PCHURYUMOV-M10-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-11-21 to 2014-12-19.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc1-67pchuryumov-m10-v1.0_d2px-dc8v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC1-67PCHURYUMOV-M10-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc1-67pchuryumov-m10-v1.0_d2px-dc8v",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-11-21 to 2014-12-19.",
-            "title": "ROSETTA-ORBITER COMET ESCORT1 OSIWAC 3 RDR MTP 010 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT1 OSIWAC 3 RDR MTP 010 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C%2FSW-MISCHA-3-RDR-ORIGINAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes the original Vega 1 MISCHA data delivery to PDS. The data were provided by Magda Delva of the MISCHA instrument team. The data are provided in ASCII format as well as the original IBM/PC binary format in which they were delivered to PDS. This data set was created for purposes of 'safing' these data. Significant concerns exist with regards to data quality. Specifically one of the instrument sensors saturated near closest approach to the comet Halley.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-sw-mischa-3-rdr-original-v1.0_d2tf-4f2i",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "halley",
                 "solar wind",
                 "vega 1",
                 "1p/halley 1 (1682 q1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C%2FSW-MISCHA-3-RDR-ORIGINAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-sw-mischa-3-rdr-original-v1.0_d2tf-4f2i",
-            "description": "This data set includes the original Vega 1 MISCHA data delivery to PDS. The data were provided by Magda Delva of the MISCHA instrument team. The data are provided in ASCII format as well as the original IBM/PC binary format in which they were delivered to PDS. This data set was created for purposes of 'safing' these data. Significant concerns exist with regards to data quality. Specifically one of the instrument sensors saturated near closest approach to the comet Halley.",
-            "title": "VEGA1 ORIGINAL MISCHA DATA SUBMISSION",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VEGA1 ORIGINAL MISCHA DATA SUBMISSION"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D31.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D31. Version 001. VIIRS/NPP BRDF/Albedo Parameter 1 NIR Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D31.001. https://doi.org/10.5067/VIIRS/VNP43D31.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
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
-            "identifier": "C1607327301-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 1 NIR product (VNP43D31) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D31 is the BRDF isotropic parameter for the VIIRS NIR broadband (0.865 \u03bcm). The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for the VIIRS NIR broadband.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D31",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 1 NIR Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 1 NIR product (VNP43D31) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D31 is the BRDF isotropic parameter for the VIIRS NIR broadband (0.865 \u03bcm). The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for the VIIRS NIR broadband.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D31.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D31.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D31.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D31.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D31.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D31.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607327301-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607327301-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D31.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D31.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D31",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D31",
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
+            "identifier": "C1607327301-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D31.001",
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
+            "series-name": "VNP43D31",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 1 NIR Daily L3 Global 30 ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA1004",
             "citation": "Marcel Dobber. 2007-09-20. OML1BRVG. Version 003. OMI/Aura Level 1B VIS Global Geolocated Earth Shine Radiances 1-orbit L2 Swath 13x24 km V003. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA1004. https://disc.gsfc.nasa.gov/datacollection/OML1BRVG_003.html. Digital Science Data.",
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
-                "earth science",
-                "spectral/engineering",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JEROME ALFRED",
                 "hasEmail": "mailto:jerome.m.alfred@nasa.gov"
             },
+            "creator": "Marcel Dobber",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239966754-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Aura Ozone Monitoring Instrument (OMI) Level-1B (L1B) Geo-located Earth View VIS Radiance, Global-Mode (OML1BRVG) Version-3 product contains geo-located Earth view spectral radiances from the VIS detector in the wavelength range of 349 to 504 nm conducted in the global measurement mode. In the standard global measurement mode, OMI observes 60 ground pixels (13 km x 24 km at nadir) across the swath (13 km x 48 km at nadir). Each file contains data from the day lit portion of an orbit (~60 minutes) and is roughly 200 MB in size. There are approximately 14 orbits per day. Once a month, in one orbit, OMI performs dark measurements, it does not perform radiance measurements. In addition, OMI performs spatial zoom measurements one day per month. For that day, this product also contains UV2 measurements that are rebinned from the spatial zoom-in measurements. In original spatial zoom mode the nadir ground pixel size is 13 x 12 km and measurements are available only for the UV2 and VIS wavelengths (306 to 432 nm). The shortname for this OMI Level-1B Product is OML1BRVG. The lead algorithm scientist for this product is Dr. Marcel Dobber from the Royal Netherlands Meteorological Institude (KNMI).\n\nThe OML1BRVG files are stored in the HDF4 based EOS Hierarchical Data Format (HDF-EOS). The radiances for the earth measurements (also referred as signal) and its precision are stored as a 16-bit mantissa and an 8-bit exponent. The signal can be computed using the equation: signal = mantissa x 10^exponent. For the precision, the same exponent is used as for the signal.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OML1BRVG",
-            "creator": "Marcel Dobber",
-            "title": "OMI/Aura Level 1B VIS Global Geolocated Earth Shine Radiances 1-orbit L2 Swath 13x24 km V003 (OML1BRVG) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BRVG_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA1004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA1004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -623178,73 +623151,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BRVG_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BRVG_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRVG.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRVG.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BRVG_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BRVG_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRVG.003/doc/README.OML1B.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRVG.003/doc/README.OML1B.pdf",
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
@@ -623254,58 +623227,61 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BRVG_003.png",
+            "identifier": "C1239966754-GES_DISC",
+            "issued": "2004-08-09",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA1004",
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
+            "series-name": "OML1BRVG",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Level 1B VIS Global Geolocated Earth Shine Radiances 1-orbit L2 Swath 13x24 km V003 (OML1BRVG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/FZU47Y00Q79U",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lesley Ott. 2020-02-14. GEOS_CASAGFED_M_FLUX. Version 2. GEOS-Carb CASA-GFED Monthly Fire Fuel NPP Rh NEE Fluxes 0.5 degree x 0.5 degree V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/FZU47Y00Q79U. https://disc.gsfc.nasa.gov/datacollection/GEOS_CASAGFED_M_FLUX_2.html.",
-            "issued": "2019-10-02",
-            "temporal": "2003-01-01T00:00:00Z/2016-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-02",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "ocean chemistry",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lesley Ott",
                 "hasEmail": "mailto:Lesley.Ott@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1701034725-GES_DISC",
-            "description": "This product provides Monthly average Net Primary Production (NPP), heterotrophic respiration (Rh), wildfire emissions (FIRE), and\nfuel wood burning emissions (FUEL) derived from the Carnegie-Ames-Stanford-Approach \u2013 Global Fire Emissions Database version 3 (CASA-\nGFED3) model.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GEOS_CASAGFED_M_FLUX",
             "creator": "Lesley Ott",
-            "title": "GEOS-Carb CASA-GFED Monthly Fire Fuel NPP Rh NEE Fluxes 0.5 degree x 0.5 degree V2 (GEOS_CASAGFED_M_FLUX) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/GEOS_CASAGFED_NEE_201607.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This product provides Monthly average Net Primary Production (NPP), heterotrophic respiration (Rh), wildfire emissions (FIRE), and\nfuel wood burning emissions (FUEL) derived from the Carnegie-Ames-Stanford-Approach \u2013 Global Fire Emissions Database version 3 (CASA-\nGFED3) model.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFZU47Y00Q79U",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFZU47Y00Q79U",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -623315,426 +623291,452 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GEOS_CASAGFED_M_FLUX_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GEOS_CASAGFED_M_FLUX_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CMS/GEOS_CASAGFED_M_FLUX.2",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CMS/GEOS_CASAGFED_M_FLUX.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CMS/GEOS_CASAGFED_M_FLUX.2/doc/README.CASA_GFED.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CMS/GEOS_CASAGFED_M_FLUX.2/doc/README.CASA_GFED.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CMS/GEOS_CASAGFED_M_FLUX.2",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CMS/GEOS_CASAGFED_M_FLUX.2",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GEOS_CASAGFED_M_FLUX",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GEOS_CASAGFED_M_FLUX",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/GEOS_CASAGFED_NEE_201607.png",
+            "identifier": "C1701034725-GES_DISC",
+            "issued": "2019-10-02",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "ocean chemistry",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/FZU47Y00Q79U",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GEOS_CASAGFED_M_FLUX",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2003-01-01T00:00:00Z/2016-12-31T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEOS-Carb CASA-GFED Monthly Fire Fuel NPP Rh NEE Fluxes 0.5 degree x 0.5 degree V2 (GEOS_CASAGFED_M_FLUX) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-MDIS-5-RDR-HIE-V1.0",
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
```

