# Change History for nasa.json (Part 97)

### Changes from 31606f9 to dd2190f (Part 86/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/tims1bil.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/tims1bil.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/TIMS_L1B.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/TIMS_L1B.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/TIMS_L1B.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/TIMS_L1B.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/TIMS_L1B.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/TIMS_L1B.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/tims_level_1b_inv.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/tims1bsq/comp/tims_level_1b_inv.dat",
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
+            "identifier": "C2813517035-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "land surface",
+                "surface radiative properties",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/436",
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
+            "temporal": "1994-04-16T00:00:00Z/1994-09-17T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Level-1B TIMS Imagery: At Sensor Radiance in BSQ Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS%2FS-RPWS-3-LPUI-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Cassini Radio and Plasma Wave Science (RPWS) Langmuir Probe Sweep voltage-current data set comprises calibrated Voltage-Current (U-I) characteristics acquired almost continuously from most mission phases during the entire Cassini mission.  The full data set of Voltage-Current characteristics is intended to become the most comprehensive and complete data set from which thermal plasma parameters can be derived in the Cassini RPWS archive.  Data are presented in text tables and are organised so as to have fixed-length records for ease in data handling.  These can be used to derive higher level data products like thermal plasma parameters, e.g., electron density and temperature.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-s-rpws-3-lpui-v1.0_i5zz-knr9",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "iapetus",
@@ -899486,1305 +899488,1315 @@
                 "hyperion",
                 "dione"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS%2FS-RPWS-3-LPUI-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-s-rpws-3-lpui-v1.0_i5zz-knr9",
-            "description": "The Cassini Radio and Plasma Wave Science (RPWS) Langmuir Probe Sweep voltage-current data set comprises calibrated Voltage-Current (U-I) characteristics acquired almost continuously from most mission phases during the entire Cassini mission.  The full data set of Voltage-Current characteristics is intended to become the most comprehensive and complete data set from which thermal plasma parameters can be derived in the Cassini RPWS archive.  Data are presented in text tables and are organised so as to have fixed-length records for ease in data handling.  These can be used to derive higher level data products like thermal plasma parameters, e.g., electron density and temperature.",
-            "title": "CASSINI SS/S RPWS CALIBRATED LP POTENTIAL CURRENT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI SS/S RPWS CALIBRATED LP POTENTIAL CURRENT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-SP1-2-RDR-HALLEY-V1.0",
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
-                "vega 2"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A number of datasets from the VEGA missions were submitted by Dyachkov at IKI as FITS files (binary data) using the GROUPS form or multidimensioned arrays. In addition, little information was provided except for the date, spacecraft, and experiment. Sometimes in the GROUPS parameters (Pvalues), there were experiment parameters such as 'time' indicated and by inference this could be determined to be exposure time versus a clock time. Since there was at least one extensive set of observations (TVS images), that were provided by IKI in this manner and a separate facility (KFKI) with the proper IHW keywords, it was possible to make estimates as to the meaning of 'time' with proper units (seconds).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-sp1-2-rdr-halley-v1.0_i677-rbxu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "vega 2"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-SP1-2-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-sp1-2-rdr-halley-v1.0_i677-rbxu",
-            "description": "A number of datasets from the VEGA missions were submitted by Dyachkov at IKI as FITS files (binary data) using the GROUPS form or multidimensioned arrays. In addition, little information was provided except for the date, spacecraft, and experiment. Sometimes in the GROUPS parameters (Pvalues), there were experiment parameters such as 'time' indicated and by inference this could be determined to be exposure time versus a clock time. Since there was at least one extensive set of observations (TVS images), that were provided by IKI in this manner and a separate facility (KFKI) with the proper IHW keywords, it was possible to make estimates as to the meaning of 'time' with proper units (seconds).",
-            "title": "VEGA2 DUST PARTICLE IMPACT PLASMA DETECTOR DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VEGA2 DUST PARTICLE IMPACT PLASMA DETECTOR DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHG18-2PO29",
             "citation": "NOAA/NESDIS/STAR. 2023-07-18. GHRSST L2P ACSPO America Region SST from GOES ABI. Version 2.90. GHRSST L2P NOAA/ACSPO GOES-18/ABI  America Region Sea Surface Temperature v2.90 dataset\r\n. Camp Springs, MD (USA). Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHG18-2PO29\r\n\r\n. https://www.star.nesdis.noaa.gov/star/index.php.",
-            "issued": "2020-03-31",
-            "temporal": "2022-06-07T00:00:00Z/2023-07-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-31",
-            "references": [
-                "https://doi.org/10.3390/rs8010079"
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
-            "identifier": "C2731035022-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The G18-ABI-L2P-ACSPO-v2.90 dataset produced by the NOAA Advanced Clear Sky Processor for Ocean (ACSPO) system is used to derive  Sea Surface Skin Temperature (SST) from the Advanced Baseline Imager (ABI) onboard the GOES-18 satellite. NOAA\u2019s GOES-18 (aka, GOES-T) was launched on March 1, 2022, replacing GOES-17 as GOES West in January 2023. It is the third satellite in the geostationary GOES\u2013R Series, the Western Hemisphere\u2019s most sophisticated weather-observing and environmental-monitoring system. The Advanced Baseline Imager (ABI) is the primary instrument on the GOES-R Series for imaging Earth\u2019s weather, oceans, and environment. <br><br>\r\nG18/ABI maps SST in a Full Disk (FD) area from 163E-77W and 60S-60N, with a spatial resolution of 2km/nadir to 15km/VZA 67-deg, and 10-min temporal sampling. The 10-min FD data are subsequently collated in time, to produce the 1-hr product, with improved coverage and reduced cloud leakages and image noise. The L2P is produced in netCDF4 GDS2 format, with 24 granules per day, and a total data volume 1.5 GB/day. The near-real time (NRT) data are updated hourly, with several hours latency. The NRT files are replaced with Delayed Mode (DM) files, with a latency of ~2-months. File names remain unchanged, and DM vs NRT can be identified by different time stamps and global attributes inside the files (MERRA instead of GFS for atmospheric profiles, and same day CMC L4 analyses in DM instead of one-day delayed in NRT processing). <br><br>\r\nPixel earth locations are not reported in the granules, as they remain unchanged from granule to granule. Those can be obtained using a flat lat/lon file or a Python script available at Documents tab under How-To section. The ACSPO G18 ABI SSTs are continuously validated in SQUAM (Dash et al, 2010). A reduced size (0.1GB/day), 0.02-deg equal-angle gridded L3C product is available at https://podaac.jpl.nasa.gov/dataset/G18-ABI-L3C-ACSPO-v2.90.",
-            "release-place": "Camp Springs, MD (USA)",
-            "series-name": "GHRSST L2P ACSPO America Region SST from GOES ABI",
             "creator": "NOAA/NESDIS/STAR",
-            "title": "GHRSST L2P NOAA/ACSPO GOES-18/ABI  America Region Sea Surface Temperature v2.90 dataset",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/G18-ABI-L2P-ACSPO-v2.90.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The G18-ABI-L2P-ACSPO-v2.90 dataset produced by the NOAA Advanced Clear Sky Processor for Ocean (ACSPO) system is used to derive  Sea Surface Skin Temperature (SST) from the Advanced Baseline Imager (ABI) onboard the GOES-18 satellite. NOAA\u2019s GOES-18 (aka, GOES-T) was launched on March 1, 2022, replacing GOES-17 as GOES West in January 2023. It is the third satellite in the geostationary GOES\u2013R Series, the Western Hemisphere\u2019s most sophisticated weather-observing and environmental-monitoring system. The Advanced Baseline Imager (ABI) is the primary instrument on the GOES-R Series for imaging Earth\u2019s weather, oceans, and environment. <br><br>\r\nG18/ABI maps SST in a Full Disk (FD) area from 163E-77W and 60S-60N, with a spatial resolution of 2km/nadir to 15km/VZA 67-deg, and 10-min temporal sampling. The 10-min FD data are subsequently collated in time, to produce the 1-hr product, with improved coverage and reduced cloud leakages and image noise. The L2P is produced in netCDF4 GDS2 format, with 24 granules per day, and a total data volume 1.5 GB/day. The near-real time (NRT) data are updated hourly, with several hours latency. The NRT files are replaced with Delayed Mode (DM) files, with a latency of ~2-months. File names remain unchanged, and DM vs NRT can be identified by different time stamps and global attributes inside the files (MERRA instead of GFS for atmospheric profiles, and same day CMC L4 analyses in DM instead of one-day delayed in NRT processing). <br><br>\r\nPixel earth locations are not reported in the granules, as they remain unchanged from granule to granule. Those can be obtained using a flat lat/lon file or a Python script available at Documents tab under How-To section. The ACSPO G18 ABI SSTs are continuously validated in SQUAM (Dash et al, 2010). A reduced size (0.1GB/day), 0.02-deg equal-angle gridded L3C product is available at https://podaac.jpl.nasa.gov/dataset/G18-ABI-L3C-ACSPO-v2.90.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHG18-2PO29%0D%0A%0D%0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHG18-2PO29%0D%0A%0D%0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/G18-ABI-L2P-ACSPO-v2.90.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/G18-ABI-L2P-ACSPO-v2.90.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/GOES18/STAR/docs/geo_nav.py",
-                    "description": "Python script to determine geolocations",
                     "@type": "dcat:Distribution",
+                    "description": "Python script to determine geolocations",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/GOES18/STAR/docs/geo_nav.py",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
-                    "description": "In situ SST Quality Monitor v2.10",
                     "@type": "dcat:Distribution",
+                    "description": "In situ SST Quality Monitor v2.10",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/x-netcdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/GOES18/STAR/docs/G18_137_0_W.nc",
-                    "description": "Example input file for python geolocation script",
                     "@type": "dcat:Distribution",
+                    "description": "Example input file for python geolocation script",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/GOES18/STAR/docs/G18_137_0_W.nc",
+                    "mediaType": "application/x-netcdf",
                     "title": "View this dataset's how-to documentation"
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
-                    "description": "SST Quality Monitor 2.1",
                     "@type": "dcat:Distribution",
+                    "description": "SST Quality Monitor 2.1",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2731035022-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2731035022-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2731035022-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2731035022-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/G18-ABI-L2P-ACSPO-v2.90.jpg",
+            "identifier": "C2731035022-POCLOUD",
+            "issued": "2020-03-31",
+            "keyword": [
+                "earth science",
+                "ocean temperature",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHG18-2PO29",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.3390/rs8010079"
+            ],
+            "release-place": "Camp Springs, MD (USA)",
+            "series-name": "GHRSST L2P ACSPO America Region SST from GOES ABI",
             "spatial": "163.0 -60.0 -77.0 60.0",
+            "temporal": "2022-06-07T00:00:00Z/2023-07-31T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST L2P NOAA/ACSPO GOES-18/ABI  America Region Sea Surface Temperature v2.90 dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYDATML2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Aqua Aerosol, Cloud and Water Vapor Subset 5-Min L2 Swath 5km and 10km. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MYDATML2.061. https://dx.doi.org/10.5067/MODIS/MYDATML2.061.",
-            "issued": "2017-10-01",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "atmospheric water vapor",
-                "clouds",
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
-            "identifier": "C1444200390-LAADS",
-            "description": "The MODIS/Aqua Aerosol, Cloud and Water Vapor Subset 5-Min L2 Swath 5km and 10km (MYDATML2) product contains a combination of key high interest science parameters. The ATML2 product provides a subset of datasets from the suite of atmosphere team products on both a 10 km scale (aerosols) and 5km scale (native 5 km cloud properties and a 5x5 pixel sample of the 1km cloud datasets). The ATML2 product employs the same 5x5 pixel sampling scheme for the 1km native resolution Level 2 products as is used in the MOD08 Level 3 global aggregated product, an approach that has been shown to retain statistical integrity for multi-day aggregations. \r\n\r\nThe C6 significantly increases the number of datasets included in the ATML2 product, including the full suite of QA datasets. Since the ATML2 data granule file size is significantly smaller than the combined size of the individual L2 products, and because the 1 km pixel sampling is consistent with the L3 algorithm, the ATML2 product is a more practical means for the user community to develop research L3 algorithms for their own specific purposes.\r\n\r\nFor more information, visit the MODIS Atmosphere website at: \r\nhttps://modis-atmos.gsfc.nasa.gov/products/joint-atm",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Aerosol, Cloud and Water Vapor Subset 5-Min L2 Swath 5km and 10km",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Aerosol, Cloud and Water Vapor Subset 5-Min L2 Swath 5km and 10km (MYDATML2) product contains a combination of key high interest science parameters. The ATML2 product provides a subset of datasets from the suite of atmosphere team products on both a 10 km scale (aerosols) and 5km scale (native 5 km cloud properties and a 5x5 pixel sample of the 1km cloud datasets). The ATML2 product employs the same 5x5 pixel sampling scheme for the 1km native resolution Level 2 products as is used in the MOD08 Level 3 global aggregated product, an approach that has been shown to retain statistical integrity for multi-day aggregations. \r\n\r\nThe C6 significantly increases the number of datasets included in the ATML2 product, including the full suite of QA datasets. Since the ATML2 data granule file size is significantly smaller than the combined size of the individual L2 products, and because the 1 km pixel sampling is consistent with the L3 algorithm, the ATML2 product is a more practical means for the user community to develop research L3 algorithms for their own specific purposes.\r\n\r\nFor more information, visit the MODIS Atmosphere website at: \r\nhttps://modis-atmos.gsfc.nasa.gov/products/joint-atm",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDATML2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDATML2.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDATML2.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDATML2.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDATML2--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDATML2--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDATML2/",
-                    "description": "Direct access to MYDATML2 C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MYDATML2 C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDATML2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDATML2/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDATML2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1444200390-LAADS",
+            "issued": "2017-10-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "atmospheric water vapor",
+                "clouds",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYDATML2.061",
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
+            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Aerosol, Cloud and Water Vapor Subset 5-Min L2 Swath 5km and 10km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F13/SSMI/DATA303",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F13 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F13/SSMI/DATA303",
-            "issued": "2012-08-08",
-            "temporal": "1995-04-30T00:00:00Z/2009-11-07T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "ocean winds",
-                "precipitation",
-                "oceans",
-                "atmospheric winds",
-                "clouds",
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
-            "identifier": "C1979923135-GHRC_DAAC",
             "description": "The RSS SSM/I Ocean Product Grids Weekly Average from DMSP F13 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F13 for weekly averages.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F13 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F13%2FSSMI%2FDATA303",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F13%2FSSMI%2FDATA303",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif13w",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif13w",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/1996/f13_ssmi_19960608v7_wk_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/1996/f13_ssmi_19960608v7_wk_RR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/1996/f13_ssmi_19960608v7_wk_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/1996/f13_ssmi_19960608v7_wk_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/1996/f13_ssmi_19960608v7_wk_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/1996/f13_ssmi_19960608v7_wk_WS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/1996/f13_ssmi_19960608v7_wk_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/1996/f13_ssmi_19960608v7_wk_CW.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f13/weekly/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f13/weekly/",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f13/weekly/browse/",
+            "identifier": "C1979923135-GHRC_DAAC",
+            "issued": "2012-08-08",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "ocean winds",
+                "precipitation",
+                "oceans",
+                "atmospheric winds",
+                "clouds",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F13/SSMI/DATA303",
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
+            "temporal": "1995-04-30T00:00:00Z/2009-11-07T23:59:59Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F13 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/B9DRKO62I5Q9",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge Sander AIRGrav L3 Bathymetry, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/B9DRKO62I5Q9.",
-            "issued": "2009-10-01",
-            "temporal": "2009-10-01T00:00:00Z/2009-11-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-11-30",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "bathymetry/seafloor topography"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kirsteen Tinto",
                 "hasEmail": "mailto:tinto@ldeo.columbia.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386246480-NSIDCV0",
             "description": "This data set contains bathymetry of Antarctic ice shelves based on measurements from the Sander Geophysics Airborne Inertially Referenced Gravimeter (AIRGrav) system. The data were collected as part of Operation IceBridge funded aircraft survey campaigns.",
-            "title": "IceBridge Sander AIRGrav L3 Bathymetry, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB9DRKO62I5Q9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB9DRKO62I5Q9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IGBTH3_AIRGravBathymetry_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IGBTH3_AIRGravBathymetry_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/B9DRKO62I5Q9",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/B9DRKO62I5Q9",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/B9DRKO62I5Q9",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/B9DRKO62I5Q9",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246480-NSIDCV0",
+            "issued": "2009-10-01",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "bathymetry/seafloor topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/B9DRKO62I5Q9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-11-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2009-10-01T00:00:00Z/2009-11-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge Sander AIRGrav L3 Bathymetry, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C135857534-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team and processed/stored at the Langley DAAC. Product is the MISR Level 2 FIRSTLOOK TOA/Cloud Stereo parameters. See ProductionDateTime for published date.",
-            "issued": "2007-05-16",
-            "temporal": "2007-06-01T01:32:07Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-15",
-            "keyword": [
-                "clouds",
-                "atmosphere",
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
-            "identifier": "C135857534-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 2 FIRSTLOOK TOA/Cloud Stereo parameters V001 contains the stereoscopically-derived winds, heights and cloud mask along with associated data, produced using ancillary inputs of Terrestrial Atmosphere and Surface Climatology (TASC) from the previous time period.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 2 FIRSTLOOK TOA/Cloud Stereo parameters V001",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C135857534-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C135857534-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C135857534-LARC",
+            "issued": "2007-05-16",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C135857534-LARC.html",
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
+            "temporal": "2007-06-01T01:32:07Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 2 FIRSTLOOK TOA/Cloud Stereo parameters V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-ANAGLYPH-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-anaglyph-ops-v1.0_i6h5-awsa",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-ANAGLYPH-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-anaglyph-ops-v1.0_i6h5-awsa",
-            "description": "NULL",
-            "title": "MER 1 MARS PANORAMIC CAMERA\n                                      ANAGLYPH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS PANORAMIC CAMERA\n                                      ANAGLYPH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/9Y3FAARO60W0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge Geometrics 823A Cesium Magnetometer L0 Raw Magnetic Field, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/9Y3FAARO60W0.",
-            "issued": "2009-01-01",
-            "temporal": "2009-01-01T00:00:00Z/2010-12-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2010-12-18",
-            "keyword": [
-                "earth science",
-                "geomagnetism",
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
-            "identifier": "C1386246589-NSIDCV0",
             "description": "This data set contains magnetic field readings taken over Antarctica using the Geometrics 823 Sensor/Magnetometer. The data were collected by scientists working on the Investigating the Cryospheric Evolution of the Central Antarctic Plate (ICECAP) project, which is funded by the National Science Foundation (NSF) and the Natural Environment Research Council (NERC), with additional support from NASA Operation IceBridge.",
-            "title": "IceBridge Geometrics 823A Cesium Magnetometer L0 Raw Magnetic Field, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9Y3FAARO60W0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9Y3FAARO60W0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IMGEO0_GeoMagRaw_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IMGEO0_GeoMagRaw_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9Y3FAARO60W0",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/9Y3FAARO60W0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9Y3FAARO60W0",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/9Y3FAARO60W0",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246589-NSIDCV0",
+            "issued": "2009-01-01",
+            "keyword": [
+                "earth science",
+                "geomagnetism",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/9Y3FAARO60W0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2010-12-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2009-01-01T00:00:00Z/2010-12-18T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge Geometrics 823A Cesium Magnetometer L0 Raw Magnetic Field, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-3-PLUTO-V2.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains PEPSSI observations taken during the              the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-3-pluto-v2.0_i6jp-33u4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-3-PLUTO-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-3-pluto-v2.0_i6jp-33u4",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains PEPSSI observations taken during the              the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
-            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4F769GP",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2012-07-09. National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 3 (PLACE III). Version 3.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4F769GP. https://doi.org/10.7927/H4F769GP.",
-            "issued": "2012-07-09",
-            "temporal": "1990-01-01T00:00:00Z/2010-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-07-09",
-            "references": [
-                "https://doi.org/10.7927/H4PN93H3",
-                "https://doi.org/10.7927/H4JW8BSC"
-            ],
-            "keyword": [
-                "boundaries",
-                "topography",
-                "human dimensions",
-                "earth science",
-                "land surface",
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
-            "identifier": "C1000000006-SEDAC",
-            "description": "The National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 3 (PLACE III) data set contains estimates of national-level aggregations in urban, rural, and total designations of territorial extent and population size by biome, climate zone, coastal proximity zone, elevation zone, and population density zone, for 232 statistical areas (countries and other UN recognized territories). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 3 (PLACE III)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 3 (PLACE III) data set contains estimates of national-level aggregations in urban, rural, and total designations of territorial extent and population size by biome, climate zone, coastal proximity zone, elevation zone, and population density zone, for 232 statistical areas (countries and other UN recognized territories). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4F769GP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4F769GP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nagdc/nagdc-population-landscape-climate-estimates-v3/place3-biomes-global-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nagdc/nagdc-population-landscape-climate-estimates-v3/place3-biomes-global-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v3/maps",
+            "identifier": "C1000000006-SEDAC",
+            "issued": "2012-07-09",
+            "keyword": [
+                "boundaries",
+                "topography",
+                "human dimensions",
+                "earth science",
+                "land surface",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4F769GP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-07-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4PN93H3",
+                "https://doi.org/10.7927/H4JW8BSC"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "1990-01-01T00:00:00Z/2010-12-31T00:00:00Z",
             "theme": [
                 "NAGDC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 3 (PLACE III)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3SVCS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Climatology Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3SVCS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Climatology Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "salinity/density",
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
-            "identifier": "C2491756473-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the seasonal climatology sea surface salinity product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Climatology Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Climatology Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_SEASONAL-CLIMATOLOGY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the seasonal climatology sea surface salinity product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3SVCS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3SVCS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_SEASONAL-CLIMATOLOGY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_SEASONAL-CLIMATOLOGY_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756473-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756473-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756473-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756473-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_SEASONAL-CLIMATOLOGY_V5.jpg",
+            "identifier": "C2491756473-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3SVCS",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Climatology Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Climatology Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331490447-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "ecosystems",
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C2331490447-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Terra MODIS Global Mapped Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Mapped/Terra-MODIS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Mapped/Terra-MODIS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/IOP/2022",
-                    "description": "MODIS-Terra L3M Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3M Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/IOP/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODIST/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Terra MODIS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Terra MODIS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODIST/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2331490447-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "ecosystems",
+                "national geospatial data asset",
+                "ngda",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331490447-OB_DAAC.html",
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
+            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Terra MODIS Global Mapped Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0316-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-25T05:37:05.000 to 2014-09-25T15:12:04.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0316-v1.0_i6ms-3mki",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0316-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0316-v1.0_i6ms-3mki",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-25T05:37:05.000 to 2014-09-25T15:12:04.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0316 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0316 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V3.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains SDC observations taken during the                 the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for SDC.                                  This is version 3.0 of this data set.  Changes since version 2.0         include the final batch of Pluto mission phase data, downlinked          between the end of January, 2016 and late in October, 2016, including    a Stim calibration in July.  Also, updates were made to the              documentation and catalog files, primarily to implement suggestions      from the V2.0 peer review.  A new table of SDC Ram (velocity)            ancillary data has been provided, and the SDC on/off and Stim tables     have been extended in time to cover the new data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v3.0_i6q5-vcrz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v3.0_i6q5-vcrz",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains SDC observations taken during the                 the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for SDC.                                  This is version 3.0 of this data set.  Changes since version 2.0         include the final batch of Pluto mission phase data, downlinked          between the end of January, 2016 and late in October, 2016, including    a Stim calibration in July.  Also, updates were made to the              documentation and catalog files, primarily to implement suggestions      from the V2.0 peer review.  A new table of SDC Ram (velocity)            ancillary data has been provided, and the SDC on/off and Stim tables     have been extended in time to cover the new data.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V3.0"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT1-EDITED2-V1.0",
-            "bureauCode": [
-                "026:00"
-            ],
-            "issued": "2021-05-21",
             "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
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
+            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the ROSETTA EXTENSION 1\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains uncalibrated raw\ndata, i.e. the digital output of the instrument. This version\nreorganizes the data into fewer files with longer time series and sorted\nby type of measurement. It also supersedes previous versions that were\nsplit into MTPs. The version number starts over from V1.0 due to a\nchange in naming convention.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext1-edited2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT1-EDITED2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext1-edited2-v1.0",
-            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the ROSETTA EXTENSION 1\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains uncalibrated raw\ndata, i.e. the digital output of the instrument. This version\nreorganizes the data into fewer files with longer time series and sorted\nby type of measurement. It also supersedes previous versions that were\nsplit into MTPs. The version number starts over from V1.0 due to a\nchange in naming convention.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT1 EDITED2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT1 EDITED2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243168866-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SMAP Level 1A Radar Receive Only Data Quality Information Version 2",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1243168866-ASF",
             "issued": "2015-07-08",
-            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-25",
             "keyword": [
                 "earth science",
                 "active remote sensing",
@@ -900797,354 +900809,320 @@
                 "smap",
                 "spectral/engineering"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243168866-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-25",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1243168866-ASF",
-            "description": "SMAP Level 1A Radar Receive Only Data Quality Information Version 2",
-            "title": "SMAP_L1A_RADAR_RECEIVE_ONLY_QA_V002",
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
+            "title": "SMAP_L1A_RADAR_RECEIVE_ONLY_QA_V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2068",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, P.S. Chaves, L.K. Balick, and W.L. Pickles. 2022. MASTER: Airborne Science, California-Nevada, March, 2002. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2068",
-            "issued": "2023-07-09",
-            "temporal": "2002-03-08T18:36:10Z/2002-04-07T17:48:35Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "infrared wavelengths",
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
-            "identifier": "C2731762222-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during six flights aboard a DOE B-200 aircraft over California and Nevada, U.S., on 2002-03-08 to 2002-04-07. This deployment was coordinated by the U.S. Department of Energy's Remote Sensing Laboratory (RSL) located at Nellis Air Force Base near Las Vegas, Nevada. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 10-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 5 acquired on 8 March 2002 over the Mojave Desert southwest of Baker, California, U.S. Source: MASTERL1B_0200102_09_20020308_1945_1947_V01.jpg",
-            "title": "MASTER: Airborne Science, California-Nevada, March, 2002",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2002_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2068",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2068",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_March_2002/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_March_2002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2002.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2002.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2068",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2068",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_March_2002/comp/MASTER_RSL_March_2002.pdf",
-                    "description": "MASTER: Airborne Science, California-Nevada, March, 2002: MASTER_RSL_March_2002.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, California-Nevada, March, 2002: MASTER_RSL_March_2002.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_March_2002/comp/MASTER_RSL_March_2002.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2002_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 5 acquired on 8 March 2002 over the Mojave Desert southwest of Baker, California, U.S. Source: MASTERL1B_0200102_09_20020308_1945_1947_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 5 acquired on 8 March 2002 over the Mojave Desert southwest of Baker, California, U.S. Source: MASTERL1B_0200102_09_20020308_1945_1947_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2002_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 5 acquired on 8 March 2002 over the Mojave Desert southwest of Baker, California, U.S. Source: MASTERL1B_0200102_09_20020308_1945_1947_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2002_Fig1.jpg",
+            "identifier": "C2731762222-ORNL_CLOUD",
+            "issued": "2023-07-09",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2068",
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
             "spatial": "-116.69 33.68 -114.28 36.61",
+            "temporal": "2002-03-08T18:36:10Z/2002-04-07T17:48:35Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, California-Nevada, March, 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AVHRR/N07_AVH02C1.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The Long-Term Data Record (LTDR) project. 2023-08-02. NOAA-07 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/AVHRR/N07_AVH02C1.006.",
-            "issued": "2022-08-01",
-            "temporal": "1981-06-24T00:00:00Z/1985-02-02T23:59:59.900Z",
-            "@type": "dcat:Dataset",
-            "modified": "1985-02-02",
-            "keyword": [
-                "atmospheric radiation",
-                "surface radiative properties",
-                "spectral/engineering",
-                "atmosphere",
-                "land surface",
-                "infrared wavelengths",
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
-            "identifier": "C2738885504-LAADS",
-            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe NOAA-07 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG, short-name N07_AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N07_AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "The Long-Term Data Record (LTDR) project",
-            "title": "NOAA-07 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe NOAA-07 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG, short-name N07_AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N07_AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAVHRR%2FN07_AVH02C1.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAVHRR%2FN07_AVH02C1.006",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/M1_AVH02C1--466",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/M1_AVH02C1--466",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/M1_AVH02C1/",
-                    "description": "Direct access to C6 M1_AVH02C1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to C6 M1_AVH02C1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/M1_AVH02C1/",
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
+            "identifier": "C2738885504-LAADS",
+            "issued": "2022-08-01",
+            "keyword": [
+                "atmospheric radiation",
+                "surface radiative properties",
+                "spectral/engineering",
+                "atmosphere",
+                "land surface",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AVHRR/N07_AVH02C1.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1985-02-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1981-06-24T00:00:00Z/1985-02-02T23:59:59.900Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-07 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2024-01-22. VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.002. https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.002.",
-            "issued": "2024-01-10",
-            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VINCENT Chiang",
                 "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2837614124-LANCEMODIS",
-            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m, short-name VJ203DNB_NRT is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-based NASA VIIRS L1 terrain-corrected geolocation product, and contains the derived line-of-sight (LOS) vectors for the single panchromatic Day-Night band (DNB). The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform's ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry. It provides geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel. The VJ203DNB product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, lunar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, moon illumination fraction and phase angle, and quality flag for every pixel location.\r\n\r\n\r\nThe J2 VIIRS geolocation underwent an on-orbit validation. Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands. The Day-Night band (DNB) geolocation error of about 2000 m was corrected. Further, the geolocation biases in the scan profile were also corrected. All these corrections bring the geolocation uncertainties for the J2 L1 products to within 75 m (1-sigma) in both the along-scan and along-track directions.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m, short-name VJ203DNB_NRT is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-based NASA VIIRS L1 terrain-corrected geolocation product, and contains the derived line-of-sight (LOS) vectors for the single panchromatic Day-Night band (DNB). The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform's ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry. It provides geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel. The VJ203DNB product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, lunar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, moon illumination fraction and phase angle, and quality flag for every pixel location.\r\n\r\n\r\nThe J2 VIIRS geolocation underwent an on-orbit validation. Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands. The Day-Night band (DNB) geolocation error of about 2000 m was corrected. Further, the geolocation biases in the scan profile were also corrected. All these corrections bring the geolocation uncertainties for the J2 L1 products to within 75 m (1-sigma) in both the along-scan and along-track directions.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203DNB_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203DNB_NRT.002",
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
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
-                    "description": "Direct access to data from MODAPS public site.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2837614124-LANCEMODIS",
+            "issued": "2024-01-10",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3809-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-04T06:25:37 to 2015-09-04T14:44:38.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3809-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3809-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3809-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-04T06:25:37 to 2015-09-04T14:44:38.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3809 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3809 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/esa-91oxxtk",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Rutherford Appleton Laboratory (RAL). 2019-08-19. S5P_L2__NP_BD3_HiR. Version 1. Sentinel-5P TROPOMI SNPP VIIRS cloud product band 3 (UVIS detector) 1-Orbit L2 5.5km x 3.5km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/esa-91oxxtk. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__NP_BD3_HiR_1.html. Digital Science Data.",
-            "issued": "2018-07-18",
-            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-18",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Siddans",
                 "hasEmail": "mailto:richard.siddans@stfc.ac.uk"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1627516279-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__NP_BD3_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P is flying in a loose formation with U.S. Suomi National Polar-orbiting Partnership (SNPP) so that S5P is able to utilize the high spatial resolution capability of the Visible Infrared Imager Radiometer Suite (VIIRS) instrument. S5P_L2_NP_BDx product contains VIIRS cloud information for each S5P across-track observation in a given band (i.e. band 3, band 6 and band 7). In addition to the nominal filed-of-view (FOV), the S5P_NPPC products are also generated for three scaled FOVs both in along and across-track directions to account for the presence of cloud covering a more extended area than the nominal FOV. The main output of S5P_L2_NP_BDx are the number of VIIRS pixels classified as confidently cloudy, probably cloudy, probably clear, and confidently clear; and the VIIRS sun-normalized radiance information in band M7, M9, and M11 such as mean, standard deviation, as well as number of valid radiance contributions.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__NP_BD3_HiR",
             "creator": "Copernicus Sentinel data processed by ESA, Rutherford Appleton Laboratory (RAL)",
-            "title": "Sentinel-5P TROPOMI SNPP VIIRS cloud product band 3 (UVIS detector) 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__NP_BD3_HiR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__NP_BD3_HiR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__NP_BD3_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P is flying in a loose formation with U.S. Suomi National Polar-orbiting Partnership (SNPP) so that S5P is able to utilize the high spatial resolution capability of the Visible Infrared Imager Radiometer Suite (VIIRS) instrument. S5P_L2_NP_BDx product contains VIIRS cloud information for each S5P across-track observation in a given band (i.e. band 3, band 6 and band 7). In addition to the nominal filed-of-view (FOV), the S5P_NPPC products are also generated for three scaled FOVs both in along and across-track directions to account for the presence of cloud covering a more extended area than the nominal FOV. The main output of S5P_L2_NP_BDx are the number of VIIRS pixels classified as confidently cloudy, probably cloudy, probably clear, and confidently clear; and the VIIRS sun-normalized radiance information in band M7, M9, and M11 such as mean, standard deviation, as well as number of valid radiance contributions.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2Fesa-91oxxtk",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2Fesa-91oxxtk",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -901154,458 +901132,454 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__NP_BD3_HiR_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__NP_BD3_HiR_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__NP_BD3_HiR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__NP_BD3_HiR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__NP_BD3_HiR.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__NP_BD3_HiR.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__NP_BD3_HiR_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__NP_BD3_HiR_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-NPP-ATBD-NPP-Clouds",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-NPP-ATBD-NPP-Clouds",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Mission-Performance-Centre-NPP-Cloud-Readme",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Mission-Performance-Centre-NPP-Cloud-Readme",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-NPP-Cloud-product",
-                    "description": "Product User Manual Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-NPP-Cloud-product",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__NP_BD3_HiR_1.png",
+            "identifier": "C1627516279-GES_DISC",
+            "issued": "2018-07-18",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5270/esa-91oxxtk",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "S5P_L2__NP_BD3_HiR",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI SNPP VIIRS cloud product band 3 (UVIS detector) 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__NP_BD3_HiR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/CERES/SSF_Terra-FM1_L2.004A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2014-10-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/CERES/SSF_Terra-FM1_L2.004A.",
-            "issued": "2015-05-11",
-            "temporal": "2000-03-01T00:00:00Z/2023-04-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-13",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric winds",
-                "clouds",
-                "earth science",
-                "land surface",
-                "surface radiative properties",
-                "atmospheric radiation",
-                "atmospheric temperature"
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
-            "identifier": "C7460991-LARC_ASDC",
             "description": "CER_SSF_Terra-FM1-MODIS_Edition4A is the Clouds and the Earth's Radiant Energy System (CERES) Single Scanner Footprint (SSF) Top-of-the-Atmosphere (TOA)/Surface Fluxes, Clouds and Aerosols Terra- Flight Model 1 (FM1) Edition 4A data product, which was collected using the CERES-FM1 instrument on the Terra platform. Data collection for this product is in progress.\r\n\r\nCERES SSF TOA/Surface Fluxes are data for a single scanner instrument. The SSF combines instantaneous CERES data with scene information from a higher-resolution imager such as Visible/Infrared Scanner (VIRS) on the Tropical Measuring Mission (TRMM), Moderate-Resolution Imaging Spectroradiometer (MODIS) on Terra and Aqua, and Visible Infrared Imaging Radiometer Suite (VIIRS) on Suomi- National Polar-orbiting Partnership (NPP). Scene identification and cloud properties are defined at the higher imager resolution and these data are averaged over the larger CERES footprint. For each CERES footprint, the SSF contains the number of cloud layers and for each layer the cloud amount, height, temperature, pressure, optical depth, emissivity, ice and liquid water path, and water particle size. The SSF also contains the CERES filtered radiances for the total, shortwave (SW), and window (WN) channels and the unfiltered SW, longwave (LW), and WN radiances. The SW, LW, and WN radiances at spacecraft altitude are converted to TOA fluxes based on the imager-defined scene. These TOA fluxes are used to estimate surface fluxes. On the SSF, only footprints with adequate imager coverage are included, which are much less than the full set of footprints on the CERES ES-8 product.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES Single Scanner Footprint (SSF) TOA/Surface Fluxes, Clouds and Aerosols Terra-FM1 Edition4A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FSSF_Terra-FM1_L2.004A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FSSF_Terra-FM1_L2.004A",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/SSF_Terra-FM1_L2.004A",
-                    "description": "DOI data set landing page for CER_SSF_Terra-FM1-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_SSF_Terra-FM1-MODIS_Edition4A",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/SSF_Terra-FM1_L2.004A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7460991-LARC_ASDC",
-                    "description": "Earthdata Search for CER_SSF_Terra-FM1-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_SSF_Terra-FM1-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7460991-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF-Ed4_R5V1.pdf",
-                    "description": "CERES Data Products Catalog for Edition4-1 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog for Edition4-1 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF-Ed4_R5V1.pdf",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/SSF_CG_R2V1.pdf",
-                    "description": "Single Satellite Footprint TOA/Surface Fluxes and Clouds (SSF) Collection Document Release 2 Version 1",
                     "@type": "dcat:Distribution",
+                    "description": "Single Satellite Footprint TOA/Surface Fluxes and Clouds (SSF) Collection Document Release 2 Version 1",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/SSF_CG_R2V1.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_SSF_Terra-Aqua_Edition4A.pdf",
-                    "description": "Quality Summary: CERES_SSF_Terra-Aqua_Edition 4A (6/30/2016)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_SSF_Terra-Aqua_Edition 4A (6/30/2016)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_SSF_Terra-Aqua_Edition4A.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ssf.pdf",
-                    "description": "CERES Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ssf.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_ssf_SampleRead_R5-1039.txt",
-                    "description": "Readme Information on CER_SSF Edition1A and Edition4A Data Sets",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information on CER_SSF Edition1A and Edition4A Data Sets",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_ssf_SampleRead_R5-1039.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/inversion_SampleRead_SSF_R5-1039.zip",
-                    "description": "Read Software Package - CERES SSF R5 V1 - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - CERES SSF R5 V1 - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/inversion_SampleRead_SSF_R5-1039.zip",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF_R4V1.pdf",
-                    "description": "CERES Data Products Catalog R4V110/1/2004 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)view related",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R4V110/1/2004 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)view related",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF_R4V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
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
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/cer_ssf_trmm-pfm-virs_subset-edition1_read_packageSSF_DPC_010008.ps",
-                    "description": "Read Me - CERES Data Products Catalog R3V2, October 2000, section 2.5 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Me - CERES Data Products Catalog R3V2, October 2000, section 2.5 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/cer_ssf_trmm-pfm-virs_subset-edition1_read_packageSSF_DPC_010008.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#ssf-level-2",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#ssf-level-2",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
@@ -901621,78 +901595,106 @@
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF/Terra-FM1-MODIS_Edition4A/",
-                    "description": "ASDC Direct Data Download for CER_SSF_Terra-FM1-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_SSF_Terra-FM1-MODIS_Edition4A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF/Terra-FM1-MODIS_Edition4A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF/Terra-FM1-MODIS_Edition4A/contents.html",
-                    "description": "OPeNDAP data access for CER_SSF_Terra-FM1-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_SSF_Terra-FM1-MODIS_Edition4A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF/Terra-FM1-MODIS_Edition4A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C7460991-LARC_ASDC",
+            "issued": "2015-05-11",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric winds",
+                "clouds",
+                "earth science",
+                "land surface",
+                "surface radiative properties",
+                "atmospheric radiation",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/CERES/SSF_Terra-FM1_L2.004A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 -89.99999 180.0 89.99999 180.0 90.0 180.0 90.0 -180.0 89.99999 -180.0 -89.99999 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-03-01T00:00:00Z/2023-04-24T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Single Scanner Footprint (SSF) TOA/Surface Fluxes, Clouds and Aerosols Terra-FM1 Edition4A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M21-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-09-22T23:25:00.000 to 2015-10-20T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m21-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M21-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m21-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-09-22T23:25:00.000 to 2015-10-20T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP021 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP021 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alcross_apo_agile&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains data collected from the Apache Point Observatory  3.5m Telescope AGILE instrument during observations of the impact of the LCROSS spacecraft on the moon on October 9, 2009. The bundle contains raw and calibration data products.",
+            "identifier": "urn:nasa:pds:lcross_apo_agile",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "lunar crater observation and sensing satellite",
                 "1aurigae",
@@ -901703,39 +901705,46 @@
                 "hip2942",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alcross_apo_agile&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:lcross_apo_agile",
-            "description": "This bundle contains data collected from the Apache Point Observatory  3.5m Telescope AGILE instrument during observations of the impact of the LCROSS spacecraft on the moon on October 9, 2009. The bundle contains raw and calibration data products.",
-            "title": "LCROSS Apache Point Observatory 3.5m Telescope AGILE Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LCROSS Apache Point Observatory 3.5m Telescope AGILE Data Bundle"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20091118.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-610",
+            "issued": "2018-06-25",
             "keyword": [
                 "pds",
                 "hazcam",
@@ -901747,256 +901756,256 @@
                 "mb",
                 "pancam"
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
-            "identifier": "NASA-610",
-            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 22",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20091118.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 22"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/9ryj-6467",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Small, C.,  and Center for International Earth Science Information Network - CIESIN - Columbia University. 2020-06-23. VIIRS Plus DMSP Change in Lights (VIIRS+DMSP dLIGHT). Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/9ryj-6467. https://doi.org/10.7927/9ryj-6467.",
-            "issued": "2020-06-23",
-            "temporal": "1992-01-01T00:00:00Z/2013-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-23",
-            "references": [
-                "https://doi.org/10.7927/69wp-8547."
-            ],
-            "keyword": [
-                "infrastructure",
-                "human dimensions",
-                "earth science",
-                "sustainability",
-                "population",
-                "economic resources",
-                "human settlements"
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
-            "identifier": "C1879283378-SEDAC",
-            "description": "The VIIRS Plus DMSP Change in Lights (VIIRS+DMSP dLIGHT) data set fuses nighttime lights imagery from the U.S. Air Force Defense Meteorological Satellite Program (DMSP) Operational Linescan System (OLS) with a stable night light composite from the next generation Suomi National Polar-orbiting Partnership (NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Day-Night Band to map the spatial distribution and temporal evolution of global nighttime lights between 1992 and 2015. The product visualizes changes in both brightness and extent of nocturnal low lights over two decades while minimizing the spatial overextent (overglow) and bright saturation that compromise the DMSP-OLS composites. The map product utilizes annual DMSP-OLS stable lights composites, produced by the NOAA Earth Observation Group and archived at the NOAA National Geophysical Data Center (NGDC), in a tri-temporal global change map. To achieve greater spatial resolution and radiometric accuracy, the DMSP-OLS composites are co-registered and fused with the 2015 VIIRS annual composite from NGDC. The final product therefore retains the spatial detail and dynamic range of the VIIRS product, and the decadal change information from DMSP-OLS images.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Small, C.,  and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "VIIRS Plus DMSP Change in Lights (VIIRS+DMSP dLIGHT)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS Plus DMSP Change in Lights (VIIRS+DMSP dLIGHT) data set fuses nighttime lights imagery from the U.S. Air Force Defense Meteorological Satellite Program (DMSP) Operational Linescan System (OLS) with a stable night light composite from the next generation Suomi National Polar-orbiting Partnership (NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Day-Night Band to map the spatial distribution and temporal evolution of global nighttime lights between 1992 and 2015. The product visualizes changes in both brightness and extent of nocturnal low lights over two decades while minimizing the spatial overextent (overglow) and bright saturation that compromise the DMSP-OLS composites. The map product utilizes annual DMSP-OLS stable lights composites, produced by the NOAA Earth Observation Group and archived at the NOAA National Geophysical Data Center (NGDC), in a tri-temporal global change map. To achieve greater spatial resolution and radiometric accuracy, the DMSP-OLS composites are co-registered and fused with the 2015 VIIRS annual composite from NGDC. The final product therefore retains the spatial detail and dynamic range of the VIIRS product, and the decadal change information from DMSP-OLS images.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F9ryj-6467",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F9ryj-6467",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-viirs-dmsp-dlight/sdei-viirs-dmsp-dlight-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-viirs-dmsp-dlight/sdei-viirs-dmsp-dlight-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdei-viirs-dmsp-dlight/maps",
+            "identifier": "C1879283378-SEDAC",
+            "issued": "2020-06-23",
+            "keyword": [
+                "infrastructure",
+                "human dimensions",
+                "earth science",
+                "sustainability",
+                "population",
+                "economic resources",
+                "human settlements"
+            ],
+            "landingPage": "https://doi.org/10.7927/9ryj-6467",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/69wp-8547."
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -56.0 180.0 84.0",
+            "temporal": "1992-01-01T00:00:00Z/2013-01-01T00:00:00Z",
             "theme": [
                 "SDEI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS Plus DMSP Change in Lights (VIIRS+DMSP dLIGHT)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC%2FOSIWAC-5-STEINS-SHAPE-V1.0",
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
-                "2867 steins",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Shape model of asteroid 2867 Steins, as derived from the Rosetta images obtained around the time of closest approach.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-osiwac-5-steins-shape-v1.0_i83k-p8xp",
+            "issued": "2018-06-26",
+            "keyword": [
+                "2867 steins",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC%2FOSIWAC-5-STEINS-SHAPE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-osiwac-5-steins-shape-v1.0_i83k-p8xp",
-            "description": "Shape model of asteroid 2867 Steins, as derived from the Rosetta images obtained around the time of closest approach.",
-            "title": "PLATE SHAPE MODEL OF ASTEROID STEINS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PLATE SHAPE MODEL OF ASTEROID STEINS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC14-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC14) Raw Data Archive is a time-ordered collection of radio science raw data acquired on August 1, 2001, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc14-v1.0_i846-78wx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC14-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc14-v1.0_i846-78wx",
-            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC14) Raw Data Archive is a time-ordered collection of radio science raw data acquired on August 1, 2001, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC14 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SROC14 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-3-CR4B-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the second half of the Cruise 4 phase, which took place between 2008-10-06 and 2009-09-13.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-3-cr4b-v1.0_i84v-9ce9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-3-CR4B-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-3-cr4b-v1.0_i84v-9ce9",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the second half of the Cruise 4 phase, which took place between 2008-10-06 and 2009-09-13.",
-            "title": "ROSETTA-ORBITER CAL ALICE 3 CR4B V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL ALICE 3 CR4B V1.0"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20071210.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-607",
+            "issued": "2018-06-25",
             "keyword": [
                 "rss",
                 "pds",
@@ -902008,420 +902017,392 @@
                 "crism",
                 "sharad"
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
-            "identifier": "NASA-607",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 3",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20071210.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0009",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0009.",
-            "issued": "1999-10-04",
-            "temporal": "1998-05-20T00:00:00Z/1998-06-22T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-02",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HERMANN GERBER",
                 "hasEmail": "mailto:gerber@access.digex.net"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000943-LARC_ASDC",
             "description": "This data set consists of light scattering measurements provided by the 4-channel nephelometer g-meter instrument flown onboard the University of Washington's CV580 aircraft during the FIRE ACE field campaign.The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.",
-            "title": "First ISCCP Regional Experiment (FIRE) Arctic Cloud Experiment (ACE) CV580 Aircraft G-Meter Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0009",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0009",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000943-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_ACE_UWCV580_GMETER_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_ACE_UWCV580_GMETER_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000943-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_uwcv580_gmeter.c",
-                    "description": "Standard C Library Call for FIRE_ACE_UWCV580_GMETER - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Standard C Library Call for FIRE_ACE_UWCV580_GMETER - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_uwcv580_gmeter.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/data/uw_cv580.pdf",
-                    "description": "University of Washington CV-580 Flight Tracks during FIRE-ACE",
                     "@type": "dcat:Distribution",
+                    "description": "University of Washington CV-580 Flight Tracks during FIRE-ACE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/data/uw_cv580.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ace_uwcv580_gmeter",
-                    "description": "Readme Information about the data provided by the G-meter instrument flown onboard the University of Washington's CV580 aircraft during the FIRE ACE field campaign",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the data provided by the G-meter instrument flown onboard the University of Washington's CV580 aircraft during the FIRE ACE field campaign",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ace_uwcv580_gmeter",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0009",
-                    "description": "DOI data set landing page for FIRE_ACE_UWCV580_GMETER_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_ACE_UWCV580_GMETER_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0009",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/index.pdf",
-                    "description": "FIRE Arctic Cloud Experiment (FIRE.ACE) Home Page Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Arctic Cloud Experiment (FIRE.ACE) Home Page Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/index.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_UWCV580_GMETER/",
-                    "description": "ASDC Direct Data Download for FIRE_ACE_UWCV580_GMETER_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_ACE_UWCV580_GMETER_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_UWCV580_GMETER/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_UWCV580_GMETER/contents.html",
-                    "description": "OPeNDAP data access for FIRE_ACE_UWCV580_GMETER_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_ACE_UWCV580_GMETER_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_UWCV580_GMETER/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000943-LARC_ASDC",
+            "issued": "1999-10-04",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0009",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>68.0 -171.7 68.0 -154.0 77.8 -154.0 77.8 -171.7 68.0 -171.7</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1998-05-20T00:00:00Z/1998-06-22T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Arctic Cloud Experiment (ACE) CV580 Aircraft G-Meter Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/135",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nelson, A., J. Killeen, L. Ballou, T. Shah, and C. Hays. 1994. Vegetation Biophysical Data (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/135",
-            "issued": "2024-05-06",
-            "temporal": "1987-05-26T00:00:00Z/1989-08-18T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "vegetation",
-                "earth science",
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
-            "identifier": "C2980707152-ORNL_CLOUD",
             "description": "Measurements of leaf area index and biomass of different canopy components",
-            "graphic-preview-description": "Browse Image",
-            "title": "Vegetation Biophysical Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F135",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F135",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_veg_biop/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_veg_biop/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Vegetation_Biophysical_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Vegetation_Biophysical_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/135",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/135",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_biop/comp/Vegetation_Biophysical_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_biop/comp/Vegetation_Biophysical_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_biop/comp/veg_biop.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_biop/comp/veg_biop.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_biop/comp/veg_biop.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_veg_biop/comp/veg_biop.tdf",
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
+            "identifier": "C2980707152-ORNL_CLOUD",
+            "issued": "2024-05-06",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "biosphere",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/135",
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
             "spatial": "-96.61 38.98 -96.45 39.12",
+            "temporal": "1987-05-26T00:00:00Z/1989-08-18T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Vegetation Biophysical Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2859376221-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ARIA. 2024-02-07. ARIA Sentinel-1 Geocoded Unwrapped Interferograms. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Alaska Satellite Facility Distributed Active Archive Center. https://asf.alaska.edu/data-sets/derived-data-sets/sentinel-1-interferograms/. Buzzanga, Brett, et al. \u201cToward sustained monitoring of subsidence at the coast using InSAR and GPS: An application in Hampton Roads, Virginia.\u201d Geophysical Research Letters 47.18 (2020): e2020GL090013.",
-            "issued": "2014-10-25",
-            "temporal": "2014-06-15T03:44:43Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "keyword": [
-                "earth science",
-                "solid earth",
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
-            "identifier": "C2859376221-ASF",
-            "description": "Level-2 interferometric products generated by the Jet Propulsion Lab (JPL) ARIA project. The creation, discovery, and distribution of these products support InSAR science around tectonically active regions, volcanoes, or areas of subsidence/uplift. The generation of the ARIA-S1-GUNW products was in part funded through collaborations with the AWS Open Data Program and NASA ROSES.",
-            "graphic-preview-description": "Image to represent the collection",
             "creator": "ARIA",
-            "title": "ARIA Sentinel-1 Geocoded Unwrapped Interferograms",
-            "graphic-preview-file": "https://s3.amazonaws.com/grfn-static/SENTINEL-1_INTERFEROGRAMS_browse.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Level-2 interferometric products generated by the Jet Propulsion Lab (JPL) ARIA project. The creation, discovery, and distribution of these products support InSAR science around tectonically active regions, volcanoes, or areas of subsidence/uplift. The generation of the ARIA-S1-GUNW products was in part funded through collaborations with the AWS Open Data Program and NASA ROSES.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.asf.alaska.edu/",
-                    "description": "ASF data search and download interface",
                     "@type": "dcat:Distribution",
+                    "description": "ASF data search and download interface",
+                    "downloadURL": "https://search.asf.alaska.edu/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through VERTEX"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aria.jpl.nasa.gov/",
-                    "description": "ARIA Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ARIA Project Home Page",
+                    "downloadURL": "https://aria.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ACCESS-Cloud-Based-InSAR/DockerizedTopsApp",
-                    "description": "Processor for generating ARIA S1 GUNW products",
                     "@type": "dcat:Distribution",
+                    "description": "Processor for generating ARIA S1 GUNW products",
+                    "downloadURL": "https://github.com/ACCESS-Cloud-Based-InSAR/DockerizedTopsApp",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/data/catalog/alaska-satellite-facility-distributed-active-archive-center-aria-s1-gunw-version-1/",
-                    "description": "Landing page for ARIA S1 GUNW products",
                     "@type": "dcat:Distribution",
+                    "description": "Landing page for ARIA S1 GUNW products",
+                    "downloadURL": "https://earthdata.nasa.gov/data/catalog/alaska-satellite-facility-distributed-active-archive-center-aria-s1-gunw-version-1/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://s3.amazonaws.com/grfn-static/SENTINEL-1_INTERFEROGRAMS_browse.png",
-                    "description": "Image to represent the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Image to represent the collection",
+                    "downloadURL": "https://s3.amazonaws.com/grfn-static/SENTINEL-1_INTERFEROGRAMS_browse.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Image to represent the collection",
+            "graphic-preview-file": "https://s3.amazonaws.com/grfn-static/SENTINEL-1_INTERFEROGRAMS_browse.png",
+            "identifier": "C2859376221-ASF",
+            "issued": "2014-10-25",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "tectonics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2859376221-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-06-15T03:44:43Z/2024-12-23T00:00:00Z",
             "theme": [
                 "ARIA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ARIA Sentinel-1 Geocoded Unwrapped Interferograms"
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
-            "identifier": "NASA-768",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (23)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -902429,60 +902410,81 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-768",
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
+            "title": "PDS Odyssey Radio Science Data (23)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67P-M30-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67p-m30-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67P-M30-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67p-m30-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP030 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP030 RDR-INFLDSTR V1.0"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-3-didr-halley-v1.0_i8gr-ehki",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark",
                 "comet",
@@ -902495,326 +902497,338 @@
                 "cal lamps",
                 "international halley watch"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-3-DIDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-3-didr-halley-v1.0_i8gr-ehki",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Spectroscopy and Spectrophotometry Network collected 352 files that represented the digitized spectra from plate material. In some cases, the non-Halley targets for the spectroscopic observations can be grouped according to 'laboratory' calibration, dark, bias, flatfield, sky, and photometric standards. In the first category, a large number of 'arcs' and 'lamps' were used as follows: HE-NE, TH-AR, NE-AR, CU-AR, CU-NE, Thorium, Tungsten, Quartz, and Rubidium. For the 'sky' observers used the twilight, moonlight, and blank sky. The most common 'photometric' standards were stars, but observers also included other comets (Hartley-Goode), asteroids (Ceres), reflection nebulae (R8), and emission nebulae (NGC1982, NGC7000). A list of these stellar calibration targets follows: HD 140283, HD 184711, HD89688, HD102870, HD120086, HD13974, HD219188, HD 25680, HD 19445, HD18803, HD30455, HD26912, SAO 1280, HZ15, CD-22 7696, GD 190, GC5106, GC2188, GC2192, G19113213, G 99-37, L745-46A, Feige 15, Feige 56, Landolt 98, Landolt 92, Van Beuren, RHO ORION, CHI 1 ORION, 29 PI LEO. For this data, no distinction about 'reduction' is distinguished for this process. The data cover the date range from 1985 October 17 through 1986 December 12.",
-            "title": "IHW COMET HALLEY DIGITIZED PHOTOGRAPHIC SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY DIGITIZED PHOTOGRAPHIC SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kelly, R. D. 1994. Aircraft Flux - Raw: U of Wy. (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/10",
-            "issued": "2024-05-02",
-            "temporal": "1987-08-11T00:00:00Z/1989-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-03",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
-                "altitude",
-                "vegetation",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "biosphere",
-                "atmospheric winds",
-                "atmospheric temperature",
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
-            "identifier": "C2968533497-ORNL_CLOUD",
             "description": "Raw (unmodified) boundary layer fluxes recorded on aircraft flights over Konza",
-            "graphic-preview-description": "Browse Image",
-            "title": "Aircraft Flux-Raw: U of Wy. (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_AF_raw_wyo/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_AF_raw_wyo/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/air_flux_raw_wy.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/air_flux_raw_wy.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/10",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/10",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_wyo/comp/aflux_kl.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_wyo/comp/aflux_kl.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_wyo/comp/af_raw.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_wyo/comp/af_raw.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_wyo/comp/air_flux_raw_wy.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_wyo/comp/air_flux_raw_wy.pdf",
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
+            "identifier": "C2968533497-ORNL_CLOUD",
+            "issued": "2024-05-02",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere",
+                "altitude",
+                "vegetation",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "biosphere",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/10",
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
             "spatial": "-102.0 37.0 -95.0 40.0",
+            "temporal": "1987-08-11T00:00:00Z/1989-10-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aircraft Flux-Raw: U of Wy. (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/271",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Peck, E.L., and T.R. Carroll. 1998. BOREAS HYD-06 Ground Gravimetric Soil Moisture Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/271",
-            "issued": "2023-11-22",
-            "temporal": "1993-09-08T00:00:00Z/1994-09-05T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "vegetation",
-                "land surface",
-                "earth science",
-                "biosphere",
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
-            "identifier": "C2807632009-ORNL_CLOUD",
             "description": "Contains the measurements of soil moisture that were made at various sites on the ground by HYD-06.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS HYD-06 Ground Gravimetric Soil Moisture Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F271",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F271",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h06grsmd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h06grsmd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD06_GRNDSM.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD06_GRNDSM.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/271",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/271",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h06grsmd/comp/h06grsmd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h06grsmd/comp/h06grsmd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h06grsmd/comp/HYD06_GRNDSM.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h06grsmd/comp/HYD06_GRNDSM.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h06grsmd/comp/HYD06_GRNDSM.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h06grsmd/comp/HYD06_GRNDSM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h06grsmd/comp/HYD06_GRNDSM.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h06grsmd/comp/HYD06_GRNDSM.txt",
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
+            "identifier": "C2807632009-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "vegetation",
+                "land surface",
+                "earth science",
+                "biosphere",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/271",
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
             "spatial": "-106.33 53.38 -98.23 57.0",
+            "temporal": "1993-09-08T00:00:00Z/1994-09-05T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS HYD-06 Ground Gravimetric Soil Moisture Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-A-ROMAP-3-AST1-SPM-V1.0",
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
-                "2867 steins"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the AST1 (Steins fly-by) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-a-romap-3-ast1-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "2867 steins"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-A-ROMAP-3-AST1-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-a-romap-3-ast1-spm-v1.0",
-            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the AST1 (Steins fly-by) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER STEINS ROMAP 3 AST1 SPM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER STEINS ROMAP 3 AST1 SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-SUMM-ELE-BR-96SEC-V1.0",
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
+            "description": "THIS DATA SET CONTAINS THE THERMAL ELECTRON DENSITY AND TEMPERATURE IN THE PLS ENERGY RANGE (10-5950 EV) FROM VOYAGER 2 AT SATURN DERIVED BY FITTING THE LOW ENERGY ELECTRON COMPONENT WITH A  MAXWELLIAN DISTRIBUTION, AND THE MOMENT DENSITY AND TEMPERATURE OF THE HOT ELECTRONS CALCULATED AFTER THE SIGNAL FROM THE THERMAL COMPONENT IS SUBTRACTED FROM THE ELECTRON SPECTRA.  IT IS A SUBSET OF THE DATA SET VG2-S-PLS-5-ELE-FIT-96.0SEC WHICH SHOULD BE OBTAINED BEFORE THIS DATA IS USED.  SPACECRAFT CHARGING MAY RESULT IN FACTOR OF 2-3 ERRORS IN THE THERMAL ELECTRON DENSITY.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-summ-ele-br-96sec-v1.0_i8qg-5aik",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-SUMM-ELE-BR-96SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-summ-ele-br-96sec-v1.0_i8qg-5aik",
-            "description": "THIS DATA SET CONTAINS THE THERMAL ELECTRON DENSITY AND TEMPERATURE IN THE PLS ENERGY RANGE (10-5950 EV) FROM VOYAGER 2 AT SATURN DERIVED BY FITTING THE LOW ENERGY ELECTRON COMPONENT WITH A  MAXWELLIAN DISTRIBUTION, AND THE MOMENT DENSITY AND TEMPERATURE OF THE HOT ELECTRONS CALCULATED AFTER THE SIGNAL FROM THE THERMAL COMPONENT IS SUBTRACTED FROM THE ELECTRON SPECTRA.  IT IS A SUBSET OF THE DATA SET VG2-S-PLS-5-ELE-FIT-96.0SEC WHICH SHOULD BE OBTAINED BEFORE THIS DATA IS USED.  SPACECRAFT CHARGING MAY RESULT IN FACTOR OF 2-3 ERRORS IN THE THERMAL ELECTRON DENSITY.",
-            "title": "VOYAGER 2 SATURN PLASMA DERIVED ELECTRON\n                                      BROWSE 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 2 SATURN PLASMA DERIVED ELECTRON\n                                      BROWSE 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/i8rc-4sju",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Plants exhibit a robust transcriptional response to gamma radiation which includes the induction of transcripts required for homologous recombination and the suppression of transcripts that promote cell cycle progression. Various DNA damaging agents induce different spectra of DNA damage as well as collateral damage to other cellular components and therefore are not expected to provoke identical responses by the cell. Here we study the effects of two different types of ionizing radiation (IR) treatment HZE (1 GeV Fe26+ high mass high charge and high energy relativistic particles) and gamma photons on the transcriptome of Arabidopsis thaliana seedlings. Both types of IR induce small clusters of radicals that can result in the formation of double strand breaks (DSBs) but HZE also produces linear arrays of extremely clustered damage. We performed these experiments across a range of time points (1.5-24 h after irradiation) in both wild-type plants and in mutants defective in the DSB-sensing protein kinase ATM. The two types of IR exhibit a shared double strand break-repair-related damage response although they differ slightly in the timing degree and ATM-dependence of the response. The ATM-dependent DNA metabolism-related transcripts of the DSB response were also induced by other DNA damaging agents but were not induced by conventional stresses. Both Gamma and HZE irradiation induced at 24 h post-irradiation ATM-dependent transcripts associated with a variety of conventional stresses; these were overrepresented for pathogen response rather than DNA metabolism. In contrast only HZE-irradiated plants at 1.5 h after irradiation exhibited an additional and very extensive transcriptional response shared with plants experiencing extended night. This response was not apparent in gamma-irradiated plants. We treated 5-day-old WT and atm-1 seedlings of Arabidopsis thaliana with 100 Gy of Gamma radiation (over a span of 15 minutes) or 30 Gy of HZE (over a span of approximately 12 minutes). Gamma irradiations were completed at 8:40 am while HZE irradiations were conducted in two runs (due to space limitations) which were completed at 1:09 and 1:28pm respectively. Gamma treated seedlings were sampled at 10:10 am 11:40 am 2:55 pm 8:40 pm and 8:40 am. HZE treated seedlings were sampled at 2:39 pm 4:09 pm 7:24 pm 1:09 am and 1:09 pm. Un-irradiated WT and atm-1 control seedlings were sampled at 10:45 am on Day #1 and 9:15 am on Day #2. There are a total of 22 experimental or control conditions with two replicates per condition yielding 44 samples overall.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-46",
+                    "mediaType": "text/html",
+                    "title": "Gamma radiation and HZE treatment of seedlings in Arabidopsis"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-46_i8rc-4sju",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse61484-2",
                 "ionizing radiation",
@@ -902839,82 +902853,82 @@
                 "sample treatment protocol",
                 "time after treatment"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/i8rc-4sju",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-46_i8rc-4sju",
-            "description": "Plants exhibit a robust transcriptional response to gamma radiation which includes the induction of transcripts required for homologous recombination and the suppression of transcripts that promote cell cycle progression. Various DNA damaging agents induce different spectra of DNA damage as well as collateral damage to other cellular components and therefore are not expected to provoke identical responses by the cell. Here we study the effects of two different types of ionizing radiation (IR) treatment HZE (1 GeV Fe26+ high mass high charge and high energy relativistic particles) and gamma photons on the transcriptome of Arabidopsis thaliana seedlings. Both types of IR induce small clusters of radicals that can result in the formation of double strand breaks (DSBs) but HZE also produces linear arrays of extremely clustered damage. We performed these experiments across a range of time points (1.5-24 h after irradiation) in both wild-type plants and in mutants defective in the DSB-sensing protein kinase ATM. The two types of IR exhibit a shared double strand break-repair-related damage response although they differ slightly in the timing degree and ATM-dependence of the response. The ATM-dependent DNA metabolism-related transcripts of the DSB response were also induced by other DNA damaging agents but were not induced by conventional stresses. Both Gamma and HZE irradiation induced at 24 h post-irradiation ATM-dependent transcripts associated with a variety of conventional stresses; these were overrepresented for pathogen response rather than DNA metabolism. In contrast only HZE-irradiated plants at 1.5 h after irradiation exhibited an additional and very extensive transcriptional response shared with plants experiencing extended night. This response was not apparent in gamma-irradiated plants. We treated 5-day-old WT and atm-1 seedlings of Arabidopsis thaliana with 100 Gy of Gamma radiation (over a span of 15 minutes) or 30 Gy of HZE (over a span of approximately 12 minutes). Gamma irradiations were completed at 8:40 am while HZE irradiations were conducted in two runs (due to space limitations) which were completed at 1:09 and 1:28pm respectively. Gamma treated seedlings were sampled at 10:10 am 11:40 am 2:55 pm 8:40 pm and 8:40 am. HZE treated seedlings were sampled at 2:39 pm 4:09 pm 7:24 pm 1:09 am and 1:09 pm. Un-irradiated WT and atm-1 control seedlings were sampled at 10:45 am on Day #1 and 9:15 am on Day #2. There are a total of 22 experimental or control conditions with two replicates per condition yielding 44 samples overall.",
-            "title": "Gamma radiation and HZE treatment of seedlings in Arabidopsis",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-46",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Gamma radiation and HZE treatment of seedlings in Arabidopsis"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Gamma radiation and HZE treatment of seedlings in Arabidopsis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-RVM1-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft.  These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the RVM1 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-rvm1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-RVM1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-rvm1-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft.  These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the RVM1 mission phase.",
-            "title": "ROSETTA-ORBITER X SREM 5 RVM1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER X SREM 5 RVM1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/i8th-whn4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The introduction of generally recognized as safe (GRAS) probiotic microbes into the spaceflight food system has the potential for use as a safe non-invasive daily countermeasure to crew microbiome and immune dysregulation. However the microgravity effects on the stress tolerances and genetic expression of probiotic bacteria must be determined to confirm translation of strain benefits and to identify potential for optimization of growth survival and strain selection for spaceflight. The work presented here demonstrates the translation of characteristics of a GRAS probiotic bacteria to a microgravity analog environment. Lactobacillus acidophilus ATCC 4356 was grown in the low shear modeled microgravity (LSMMG) orientation and the control orientation in the rotating wall vessel (RWV) to determine the effect of LSMMG on the growth survival through stress challenge and gene expression of the strain. No differences were observed between the LSMMG and control grown L. acidophilus suggesting that the strain will behave similarly in spaceflight and may be expected to confer Earth-based benefits.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-199",
+                    "mediaType": "text/html",
+                    "title": "Response to Low Shear Modeled Microgravity Indicates Translation of Lactobacillus acidophilus ATCC 4356 Benefits to Spaceflight"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-199_i8th-whn4",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "library construction",
                 "sample treatment protocol",
@@ -902924,78 +902938,42 @@
                 "nucleic acid sequencing",
                 "nucleic acid extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/i8th-whn4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-199_i8th-whn4",
-            "description": "The introduction of generally recognized as safe (GRAS) probiotic microbes into the spaceflight food system has the potential for use as a safe non-invasive daily countermeasure to crew microbiome and immune dysregulation. However the microgravity effects on the stress tolerances and genetic expression of probiotic bacteria must be determined to confirm translation of strain benefits and to identify potential for optimization of growth survival and strain selection for spaceflight. The work presented here demonstrates the translation of characteristics of a GRAS probiotic bacteria to a microgravity analog environment. Lactobacillus acidophilus ATCC 4356 was grown in the low shear modeled microgravity (LSMMG) orientation and the control orientation in the rotating wall vessel (RWV) to determine the effect of LSMMG on the growth survival through stress challenge and gene expression of the strain. No differences were observed between the LSMMG and control grown L. acidophilus suggesting that the strain will behave similarly in spaceflight and may be expected to confer Earth-based benefits.",
-            "title": "Response to Low Shear Modeled Microgravity Indicates Translation of Lactobacillus acidophilus ATCC 4356 Benefits to Spaceflight",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-199",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Response to Low Shear Modeled Microgravity Indicates Translation of Lactobacillus acidophilus ATCC 4356 Benefits to Spaceflight"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Response to Low Shear Modeled Microgravity Indicates Translation of Lactobacillus acidophilus ATCC 4356 Benefits to Spaceflight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2511",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Manney, G., Santee, M., Froidevaux, L., Livesey, N. and Read, W.. 2020-06-11. ML2HNO3. Version 005. MLS/Aura Level 2 Nitric Acid (HNO3) Mixing Ratio V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2511. https://disc.gsfc.nasa.gov/datacollection/ML2HNO3_005.html. Digital Science Data.",
-            "issued": "2020-02-04",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "NATHANIEL LIVESEY",
-                "hasEmail": "mailto:livesey@mls.jpl.nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+                "fn": "NATHANIEL LIVESEY",
+                "hasEmail": "mailto:livesey@mls.jpl.nasa.gov"
             },
-            "identifier": "C1729925263-GES_DISC",
-            "description": "ML2HNO3 is the EOS Aura Microwave Limb Sounder (MLS) standard product for nitric acid derived from radiances measured by the 240 GHz radiometer at and below 10 hPa, and from the 190 GHz radiometer above 10 hPa. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 1.47 hPa (1.0 hPa under enhanced conditions), and the vertical resolution is between about 3 and 5 km. Users of the ML2HNO3 data product should read section 3.12 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2HNO3",
             "creator": "Manney, G., Santee, M., Froidevaux, L., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Nitric Acid (HNO3) Mixing Ratio V005 (ML2HNO3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2HNO3_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2HNO3 is the EOS Aura Microwave Limb Sounder (MLS) standard product for nitric acid derived from radiances measured by the 240 GHz radiometer at and below 10 hPa, and from the 190 GHz radiometer above 10 hPa. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 1.47 hPa (1.0 hPa under enhanced conditions), and the vertical resolution is between about 3 and 5 km. Users of the ML2HNO3 data product should read section 3.12 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2511",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2511",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -903005,87 +902983,123 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2HNO3_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2HNO3_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2HNO3.005/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2HNO3.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2HNO3.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2HNO3.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2HNO3_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2HNO3_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2HNO3_005.png",
+            "identifier": "C1729925263-GES_DISC",
+            "issued": "2020-02-04",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2511",
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
+            "series-name": "ML2HNO3",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Nitric Acid (HNO3) Mixing Ratio V005 (ML2HNO3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/i92q-zgzp",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The spaceflight experiment was carried out using male C57BL/10J mice (8 weeks old at launch). Wild type mice (n=3) were launched by Space Shuttle Discovery and housed on the International Space Station (ISS) for 91 days. They returned to the Earth by Space Shuttle Atlantis. But only one mouse returned to the Earth alive. Whole brain was sampled from the mouse killed by inhalation of carbon dioxide at the Life Sciences Support Facility of Kennedy Space Center within 3-4 hours after landing. After the spaceflight experiment the on-ground experiment was also carried out at the Advanced Biotechnology Center in Genova Italy. A mouse with the same species sex and age was housed in mice drawer system (MDS) which was utilized for the spaceflight (SF) mice for 3 months as the ground control (GC). Another mouse was housed in normal vivarium cage as the laboratory control (LC). Amount of food and water supplementation and environmental conditions were simulated as the flight group. After 3 months brain was sampled from one mouse in group GC and LC respectively. Comprehensive analyses of gene expression were performed in the right brain. Total of 4,000 genes were analyzed. The expression levels of 60 genes significantly changed in response to SF compared with LC and/or GC. The 15 and 16 genes were up- (> 2 folds) and down-regulated (< 0.5 folds) respectively following SF vs. GC. The levels of 58 genes were significantly altered by housing in MDS in space and/or on the ground. Forty seven and 11 genes were significantly up- and down-regulated vs. LC. Twenty seven out of these genes responded to caging in MDS both in space and on the ground. Further 31 genes were influenced by housing in MDS on the Earth. Responses of the characteristics of brain to long-term gravitational unloading were investigated in mice.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-33",
+                    "mediaType": "text/html",
+                    "title": "Gene responses in mouse brain to long-term exposure to microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-33_i92q-zgzp",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse32077-5",
                 "gravity",
@@ -903107,111 +903121,99 @@
                 "p-gse32077-1",
                 "image_aquisition"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/i92q-zgzp",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-33_i92q-zgzp",
-            "description": "The spaceflight experiment was carried out using male C57BL/10J mice (8 weeks old at launch). Wild type mice (n=3) were launched by Space Shuttle Discovery and housed on the International Space Station (ISS) for 91 days. They returned to the Earth by Space Shuttle Atlantis. But only one mouse returned to the Earth alive. Whole brain was sampled from the mouse killed by inhalation of carbon dioxide at the Life Sciences Support Facility of Kennedy Space Center within 3-4 hours after landing. After the spaceflight experiment the on-ground experiment was also carried out at the Advanced Biotechnology Center in Genova Italy. A mouse with the same species sex and age was housed in mice drawer system (MDS) which was utilized for the spaceflight (SF) mice for 3 months as the ground control (GC). Another mouse was housed in normal vivarium cage as the laboratory control (LC). Amount of food and water supplementation and environmental conditions were simulated as the flight group. After 3 months brain was sampled from one mouse in group GC and LC respectively. Comprehensive analyses of gene expression were performed in the right brain. Total of 4,000 genes were analyzed. The expression levels of 60 genes significantly changed in response to SF compared with LC and/or GC. The 15 and 16 genes were up- (> 2 folds) and down-regulated (< 0.5 folds) respectively following SF vs. GC. The levels of 58 genes were significantly altered by housing in MDS in space and/or on the ground. Forty seven and 11 genes were significantly up- and down-regulated vs. LC. Twenty seven out of these genes responded to caging in MDS both in space and on the ground. Further 31 genes were influenced by housing in MDS on the Earth. Responses of the characteristics of brain to long-term gravitational unloading were investigated in mice.",
-            "title": "Gene responses in mouse brain to long-term exposure to microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-33",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Gene responses in mouse brain to long-term exposure to microgravity"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Gene responses in mouse brain to long-term exposure to microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206686-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rock glaciers in the Pyrenees, Spain and France, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1990-01-01",
-            "temporal": "1990-01-01T00:00:00Z/1997-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-12-31",
-            "keyword": [
-                "snow/ice",
-                "land surface",
-                "earth science",
-                "frozen ground",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eduardo Pison",
                 "hasEmail": "mailto:emartinez@uam.es"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206686-NSIDCV0",
             "description": "This study and inventory of active rock glaciers was carried out by means of the usual techniques used in the study of alpine permafrost. First, the rock glaciers were located by means of aerial photography and field work. Second, a detailed geomorphological map was prepared, to detect the active processes in each rock glacier. This includes geotransect and surface analysis (clast roundness, clast forms, particle orientation and lichenometric measurements). Third, complementary measurements (water temperature and BTS [bottom temperature of snow] measurements) were carried out. These three studies allowed us to determine the activity or inactivity of previously detailed landforms, and to classify them as active, inactive, or relict rock glaciers. The external landforms, frontal slope, vertical organization, flow forms, absence of lichens and the descriptive parameters of rock glaciers allowed us to classify them as relict or active ones.  On the Besiberri, Gemelos, and Argualas rock glaciers we have carried out photogrammetric studies, and on the Argualas rock glacier we carried out a topographic survey from 1991 and also geoelectric soundings (San Jose et al. 1992; Serrano et al. 1995; Fabre et al. 1995). These data are presented on the CAPS Version 1.0 CD-ROM, June\n1998.",
-            "title": "Rock glaciers in the Pyrenees, Spain and France, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD285_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD285_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD285/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD285/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD285/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD285/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206686-NSIDCV0",
+            "issued": "1990-01-01",
+            "keyword": [
+                "snow/ice",
+                "land surface",
+                "earth science",
+                "frozen ground",
+                "cryosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206686-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1997-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-0.333 42.333 0.917 42.833",
+            "temporal": "1990-01-01T00:00:00Z/1997-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Rock glaciers in the Pyrenees, Spain and France, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIRO-2-CVP-COMMISSIONING-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the Commissioning phase of the Rosetta mission by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-miro-2-cvp-commissioning-v1.0_i93n-p7n8",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "unknown",
@@ -903221,1045 +903223,1054 @@
                 "m42",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIRO-2-CVP-COMMISSIONING-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-miro-2-cvp-commissioning-v1.0_i93n-p7n8",
-            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the Commissioning phase of the Rosetta mission by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER CHECK MIRO 2 CVP COMMISSIONING V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CHECK MIRO 2 CVP COMMISSIONING V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESATMTL_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "issued": "2013-03-29",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-10-28",
-            "keyword": [
-                "atmospheric temperature",
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
-                "name": "LaRC"
-            },
-            "identifier": "C191856297-LARC",
             "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "title": "TES/Aura L2 Atmospheric Temperatures Limb V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESATMTL_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESATMTL_L2.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C191856297-LARC",
+            "issued": "2013-03-29",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TESATMTL_L2.006",
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
+            "title": "TES/Aura L2 Atmospheric Temperatures Limb V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-21",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2019-05-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-21.",
-            "issued": "2019-05-08",
-            "temporal": "2020-07-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-08",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JACQUES PELON",
                 "hasEmail": "mailto:jacques.pelon@aero.jussieu.fr"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1969999412-LARC_ASDC",
             "description": "CAL_IIR_L2_Track-Standard-V4-20 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) Infrared Imaging Radiometer (IIR) Level 2 Track, Version 4-21 data product. Data for this product was collected using the CALIPSO IIR instrument. Data collection for this product is ongoing. This product contains emissivity and cloud particle data related to pixels co-located to the lidar track. The version of this product was changed from 4-20 to 4-21 to account for a change in the operating system of the CALIPSO production cluster.\r\n\r\nCALIPSO was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), IIR, and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Infrared Imaging Radiometer (IIR) Level 2 Track, V4-21",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIR%2FCALIPSO%2FCAL_IIR_L2_Track-Standard-V4-21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIR%2FCALIPSO%2FCAL_IIR_L2_Track-Standard-V4-21",
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_iir_l2_trackswath_v4-20.php",
-                    "description": "Detailed quality summary of the V4.20 IIR Level 2 data product",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed quality summary of the V4.20 IIR Level 2 data product",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_iir_l2_trackswath_v4-20.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_summaries/iir/cal_iir_l2_track_v4-20_desc.php",
-                    "description": "User's guide description document of the V4.20 IIR Level 2 Track data product",
                     "@type": "dcat:Distribution",
+                    "description": "User's guide description document of the V4.20 IIR Level 2 Track data product",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_summaries/iir/cal_iir_l2_track_v4-20_desc.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
-                    "description": "CALIPSO - List of publications",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of publications",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
-                    "description": "CALIPSO - Data Availability Site",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Availability Site",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
-                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/project_documentation.php",
-                    "description": "CALIPSO - List of project documentation (Data Products Catalog and ATBDs)",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of project documentation (Data Products Catalog and ATBDs)",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/project_documentation.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
-                    "description": "CALIPSO Data User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/faq.php",
-                    "description": "CALIPSO Data User\u2019s Guide - Frequently Asked Questions",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide - Frequently Asked Questions",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/faq.php",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
-                    "description": "CALIPSO Tilt Mode Geometry Anomaly",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Tilt Mode Geometry Anomaly",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
-                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
+                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://calipso.cnes.fr/fr",
-                    "description": "French (CNES) CALIPSO Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "French (CNES) CALIPSO Home Page",
+                    "downloadURL": "https://calipso.cnes.fr/fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.icare.univ-lille.fr",
-                    "description": "ICARE Data and Services Center Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Data and Services Center Home Page",
+                    "downloadURL": "https://www.icare.univ-lille.fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
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
-                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
-                    "description": "NASA Mission Overview of CALIPSO",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Mission Overview of CALIPSO",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/ASDC_CALIPSO_Overview_2015.pdf",
-                    "description": "Overview of CALIPSO Data at the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of CALIPSO Data at the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/ASDC_CALIPSO_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
-                    "description": "Overview of CALIPSO Data Product Maturity",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of CALIPSO Data Product Maturity",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_release_summary_statement.html",
-                    "description": "CALIPSO Data Release Summary Statement",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data Release Summary Statement",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_release_summary_statement.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
-                    "description": "CALIPSO Products Overview",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Products Overview",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1969999412-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_IIR_L2_Track-Standard-V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_IIR_L2_Track-Standard-V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1969999412-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-21",
-                    "description": "DOI data set landing page for CAL_IIR_L2_Track-Standard-V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_IIR_L2_Track-Standard-V4-21",
+                    "downloadURL": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-21",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/IIR_L2_Track-Standard-V4-21/",
-                    "description": "ASDC Direct Data Download for CAL_IIR_L2_Track-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_IIR_L2_Track-Standard-V4-21_V4-21",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/IIR_L2_Track-Standard-V4-21/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/IIR_L2_Track-Standard-V4-21/contents.html",
-                    "description": "OPeNDAP data access for CAL_IIR_L2_Track-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_IIR_L2_Track-Standard-V4-21_V4-21",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/IIR_L2_Track-Standard-V4-21/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1969999412-LARC_ASDC",
+            "issued": "2019-05-08",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-05-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2020-07-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Infrared Imaging Radiometer (IIR) Level 2 Track, V4-21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/830",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dentener, F.J. 2006. Global Maps of Atmospheric Nitrogen Deposition, 1860, 1993, and 2050. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/830",
-            "issued": "2023-10-02",
-            "temporal": "1860-01-01T00:00:00Z/2050-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "keyword": [
-                "atmospheric chemistry",
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
-            "identifier": "C2776896954-ORNL_CLOUD",
             "description": "This data set provides global gridded estimates of atmospheric deposition of total inorganic nitrogen (N), NHx (NH3 and NH4+), and NOy (all oxidized forms of nitrogen other than N2O), in mg N/m2/year, for the years 1860 and 1993 and projections for the year 2050. The data set was generated using a global three-dimensional chemistry-transport model (TM3) with a spatial resolution of 5 degrees longitude by 3.75 degrees latitude (Jeuken et al., 2001; Lelieveld and Dentener, 2000). Nitrogen emissions estimates (Van Aardenne et al., 2001) and projection scenario data (IPCC, 1996; 2000) were used as input to the model.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Global Maps of Atmospheric Nitrogen Deposition, 1860, 1993, and 2050",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/830_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F830",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F830",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/global_N_deposition_maps/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/global_N_deposition_maps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/global_N_deposition_maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/global_N_deposition_maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/830",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/830",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_deposition_maps/comp/deposition_maps.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_deposition_maps/comp/deposition_maps.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_deposition_maps/comp/global_N_deposition_maps.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_deposition_maps/comp/global_N_deposition_maps.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_deposition_maps/comp/global_N_deposition_maps_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_deposition_maps/comp/global_N_deposition_maps_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/830_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/830_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=830",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=830",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/830_1_fit.png",
+            "identifier": "C2776896954-ORNL_CLOUD",
+            "issued": "2023-10-02",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/830",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1860-01-01T00:00:00Z/2050-12-31T23:59:59Z",
             "theme": [
                 "Climate",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Maps of Atmospheric Nitrogen Deposition, 1860, 1993, and 2050"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/rht8-jv78",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2022-05-24. National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 4 (PLACE IV). Version 4.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/rht8-jv78. https://doi.org/10.7927/rht8-jv78.",
-            "issued": "2022-05-24",
-            "temporal": "2000-01-01T00:00:00Z/2020-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-24",
-            "references": [
-                "https://doi.org/10.7927/H4PN93H3",
-                "https://doi.org/10.7927/H4JW8BSC",
-                "https://doi.org/10.7927/H4F769GP",
-                "https://doi.org/10.7927/y2wq-pv06"
-            ],
-            "keyword": [
-                "topography",
-                "human dimensions",
-                "earth science",
-                "land surface",
-                "population",
-                "boundaries"
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
-            "identifier": "C2287385195-SEDAC",
-            "description": "The National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 4 (PLACE IV) provides measures of population (head counts) and land area (square kilometers) as totals and by urban and rural designation, within multiple biophysical themes for 248 statistical areas (countries and other territories recognized by the United Nations (UN)), UN geographic regions and subregions, and World Bank economic classifications. It improves upon previous versions by providing these estimates at both the national level, and where possible, at subnational administrative level 1 for the years 2000, 2005, 2010, 2015, and 2020, and by 5-year and broad age groups for the year 2010.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 4 (PLACE IV)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 4 (PLACE IV) provides measures of population (head counts) and land area (square kilometers) as totals and by urban and rural designation, within multiple biophysical themes for 248 statistical areas (countries and other territories recognized by the United Nations (UN)), UN geographic regions and subregions, and World Bank economic classifications. It improves upon previous versions by providing these estimates at both the national level, and where possible, at subnational administrative level 1 for the years 2000, 2005, 2010, 2015, and 2020, and by 5-year and broad age groups for the year 2010.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Frht8-jv78",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Frht8-jv78",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nagdc/nagdc-population-landscape-climate-estimates-v4/nagdc-population-landscape-climate-estimates-v4-biomes-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nagdc/nagdc-population-landscape-climate-estimates-v4/nagdc-population-landscape-climate-estimates-v4-biomes-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v4/maps",
+            "identifier": "C2287385195-SEDAC",
+            "issued": "2022-05-24",
+            "keyword": [
+                "topography",
+                "human dimensions",
+                "earth science",
+                "land surface",
+                "population",
+                "boundaries"
+            ],
+            "landingPage": "https://doi.org/10.7927/rht8-jv78",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4PN93H3",
+                "https://doi.org/10.7927/H4JW8BSC",
+                "https://doi.org/10.7927/H4F769GP",
+                "https://doi.org/10.7927/y2wq-pv06"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "2000-01-01T00:00:00Z/2020-01-01T00:00:00Z",
             "theme": [
                 "NAGDC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 4 (PLACE IV)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/566/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-04-16",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
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
-            "identifier": "DASHLINK_566",
             "description": "Draft Agenda, april 16, 2012",
-            "title": "Agenda",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Agenda_Sat_draft5.jpg",
-                    "description": "Sat",
                     "@type": "dcat:Distribution",
+                    "description": "Sat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Agenda_Sat_draft5.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "AePW Agenda_Sat_draft5.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Agenda_Draft5_Sunday.jpg",
-                    "description": "Sun",
                     "@type": "dcat:Distribution",
+                    "description": "Sun",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Agenda_Draft5_Sunday.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "AePW Agenda_Draft5_Sunday.jpg"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Agenda_Draft5.pdf",
-                    "description": "Draft agenda to download",
                     "@type": "dcat:Distribution",
+                    "description": "Draft agenda to download",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Agenda_Draft5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AePW Agenda_Draft5.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_566",
+            "issued": "2012-04-16",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/566/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Agenda"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GRAIL-L-LGRS-3-CDR-V1.0",
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
-                "gravity recovery and interior laboratory",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated and resampled engineering (e.g., star tracker data and timing) and science data acquired from the Lunar Gravity and Ranging System (LGRS) on the two spacecraft comprising the Gravity Recovery and Interior Laboratory (GRAIL) mission. The data in the set are at NASA Level 1 and have been archived for general use. Products in this set have been derived from NASA Level 0 (the LGRS EDR data set) by the GRAIL Science Data System (SDS). The observations were used to generate high-resolution gravity field models of the Moon. The data set includes all of the Level 1 LGRS data from the GRAIL mission (March-December 2012).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.grail-l-lgrs-3-cdr-v1.0_i9aq-fv6d",
+            "issued": "2018-06-26",
+            "keyword": [
+                "gravity recovery and interior laboratory",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GRAIL-L-LGRS-3-CDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.grail-l-lgrs-3-cdr-v1.0_i9aq-fv6d",
-            "description": "This data set contains calibrated and resampled engineering (e.g., star tracker data and timing) and science data acquired from the Lunar Gravity and Ranging System (LGRS) on the two spacecraft comprising the Gravity Recovery and Interior Laboratory (GRAIL) mission. The data in the set are at NASA Level 1 and have been archived for general use. Products in this set have been derived from NASA Level 0 (the LGRS EDR data set) by the GRAIL Science Data System (SDS). The observations were used to generate high-resolution gravity field models of the Moon. The data set includes all of the Level 1 LGRS data from the GRAIL mission (March-December 2012).",
-            "title": "GRAIL MOON LGRS CALIBRATED AND RESAMPLED SCIENCE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GRAIL MOON LGRS CALIBRATED AND RESAMPLED SCIENCE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.euv.modelled&version=13.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains solar irradiance spectra in 1-nm bins from 0-190 nm. The spectra are generated based upon the Flare Irradiance Spectra Model - Mars (FISM-M) using the EUV calibrated band irrandiance and interpolated Earth-based solar indices and measurements as proxies. The data were provided  by the MAVEN EUV team in CDF format.",
+            "identifier": "urn:nasa:pds:maven.euv.modelled_i9bi-6gsi",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "maven euv modelled",
                 "mars",
                 "mars atmosphere and volatile evolution mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.euv.modelled&version=13.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:maven.euv.modelled_i9bi-6gsi",
-            "description": "This bundle contains solar irradiance spectra in 1-nm bins from 0-190 nm. The spectra are generated based upon the Flare Irradiance Spectra Model - Mars (FISM-M) using the EUV calibrated band irrandiance and interpolated Earth-based solar indices and measurements as proxies. The data were provided  by the MAVEN EUV team in CDF format.",
-            "title": "MAVEN EUV Modelled Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAVEN EUV Modelled Data Bundle"
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
+            "description": "The Juno Waves calibrated burst waveform full resolution data set includes all high rate science electric field waveforms from 50Hz up to 45.25 MHz and magnetic field waveforms from 50Hz to 20kHz with sample rates that depend on the receiver used to obtain the waveforms.  This is the complete waveform data set containing all high rate binning mode data and record mode data received from Waves from launch until the end of mission including initial checkout, the Earth flyby, the Jupiter orbits and cruise. Data are acquired from the Waves Low Frequency Receiver (LFR) and High Frequency Receiver (HFR) and are typically losslessly compressed on board.  These data are presented in binary SERIES objects.  This data set comprises highest temporal resolution data obtained by Waves (or all other Juno instruments, for that matter).  Pre-rendered spectrograms generated from these data are included as well to provide the user with a quick view of the content of the data.  This data set should be among the last used of any in the Waves archive as it provides highly detailed information on very short isolated intervals in time.  The Waves full resolution survey data provide context for these data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-e-j-ss-wav-3-cdr-bstfull-v1.0_i9ck-6a6s",
             "issued": "2021-05-21",
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
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-e-j-ss-wav-3-cdr-bstfull-v1.0_i9ck-6a6s",
-            "description": "The Juno Waves calibrated burst waveform full resolution data set includes all high rate science electric field waveforms from 50Hz up to 45.25 MHz and magnetic field waveforms from 50Hz to 20kHz with sample rates that depend on the receiver used to obtain the waveforms.  This is the complete waveform data set containing all high rate binning mode data and record mode data received from Waves from launch until the end of mission including initial checkout, the Earth flyby, the Jupiter orbits and cruise. Data are acquired from the Waves Low Frequency Receiver (LFR) and High Frequency Receiver (HFR) and are typically losslessly compressed on board.  These data are presented in binary SERIES objects.  This data set comprises highest temporal resolution data obtained by Waves (or all other Juno instruments, for that matter).  Pre-rendered spectrograms generated from these data are included as well to provide the user with a quick view of the content of the data.  This data set should be among the last used of any in the Waves archive as it provides highly detailed information on very short isolated intervals in time.  The Waves full resolution survey data provide context for these data.",
-            "title": "JUNO E/J/S/SS WAVES CALIBRATED BURST FULL RESOLUTION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JUNO E/J/S/SS WAVES CALIBRATED BURST FULL RESOLUTION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M06-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m06-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M06-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m06-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP006 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP006 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/ECOA/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/ECOA/DATA001.",
-            "issued": "2015-06-01",
-            "temporal": "2015-06-01T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "ocean chemistry",
-                "earth science",
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
-            "identifier": "C1633360204-OB_DAAC",
             "description": "East Coast Ocean Acidification cruise",
-            "title": "East Coast Ocean Acidification cruise",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FECOA%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FECOA%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ECOA/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ECOA/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360204-OB_DAAC",
+            "issued": "2015-06-01",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "ocean chemistry",
+                "earth science",
+                "salinity/density",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/ECOA/DATA001",
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
+            "temporal": "2015-06-01T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "East Coast Ocean Acidification cruise"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3RACS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Annual Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3RACS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Annual Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "ocean temperature",
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
-            "identifier": "C2491742866-POCLOUD",
-            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, Annual, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the Annual ancillary sea surface temperature product associated with version 5.0  of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Annual Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Annual Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_ANNUAL_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, Annual, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the Annual ancillary sea surface temperature product associated with version 5.0  of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3RACS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3RACS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_ANNUAL_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_ANNUAL_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491742866-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491742866-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491742866-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491742866-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_ANNUAL_V5.jpg",
+            "identifier": "C2491742866-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3RACS",
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
+            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Annual Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Annual Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/i9ek-hfxm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Baker",
+                "hasEmail": "mailto:john.g.baker@nasa.gov"
+            },
+            "description": "Numerically-generated gravitational waveforms for circular inspiral into Kerr black holes. These waveforms were developed using Scott Hughes' black hole perturbation theory code (the \"Teukolsky code\").",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://astrogravs.gsfc.nasa.gov/docs/lit/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000128",
             "issued": "2018-06-25",
-            "temporal": "1957-01-01/2005-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ligo",
                 "gravitational waves",
@@ -904269,430 +904280,420 @@
                 "space science",
                 "neutron stars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John Baker",
-                "hasEmail": "mailto:john.g.baker@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/i9ek-hfxm",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000128",
-            "description": "Numerically-generated gravitational waveforms for circular inspiral into Kerr black holes. These waveforms were developed using Scott Hughes' black hole perturbation theory code (the \"Teukolsky code\").",
-            "title": "Astrophysical Gravitational Wave Sources Literature Catalog",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://astrogravs.gsfc.nasa.gov/docs/lit/",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "1957-01-01/2005-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Astrophysical Gravitational Wave Sources Literature Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-URAP-4-SUMM-PFR-AVG-E-10MIN-V1.0",
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
-                "ulysses",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A. UDS data files ------------------- Eight files are provided that conform to the UDS conventions regarding the naming of files and the format of the data. The eight files are divided into 4 pairs of files with each pair consisting of a file containing data averaged over a 10 minute period and a file containing the maximum data value during the same 10 minute period. The 4 pairs of file contain data for the RAR, the PFR, WFA - magnetic field, and WFA - magnetic field.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-urap-4-summ-pfr-avg-e-10min-v1.0_i9fc-qmpb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "ulysses",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-URAP-4-SUMM-PFR-AVG-E-10MIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-urap-4-summ-pfr-avg-e-10min-v1.0_i9fc-qmpb",
-            "description": "A. UDS data files ------------------- Eight files are provided that conform to the UDS conventions regarding the naming of files and the format of the data. The eight files are divided into 4 pairs of files with each pair consisting of a file containing data averaged over a 10 minute period and a file containing the maximum data value during the same 10 minute period. The 4 pairs of file contain data for the RAR, the PFR, WFA - magnetic field, and WFA - magnetic field.",
-            "title": "ULY JUP URAP PLASMA FREQ REC AVERAGE E-FIELD 10 MIN",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULY JUP URAP PLASMA FREQ REC AVERAGE E-FIELD 10 MIN"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-D-UDDS-5-DUST-V3.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains the data from the Ulysses dust detector system (UDDS) from start of mission through the end of mission, 1990-2007. (As the dust detector was turned off after Nov. 30, 2007, this is the last date for which UDDS data is recorded.) Included are the dust impact data, noise data, laboratory calibration data, and location and orientation of the spacecraft and instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-d-udds-5-dust-v3.1_i9gi-hj7j",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "ulysses",
                 "calibration",
                 "dust"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-D-UDDS-5-DUST-V3.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-d-udds-5-dust-v3.1_i9gi-hj7j",
-            "description": "This data set contains the data from the Ulysses dust detector system (UDDS) from start of mission through the end of mission, 1990-2007. (As the dust detector was turned off after Nov. 30, 2007, this is the last date for which UDDS data is recorded.) Included are the dust impact data, noise data, laboratory calibration data, and location and orientation of the spacecraft and instrument.",
-            "title": "ULYSSES DUST DETECTION SYSTEM V3.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULYSSES DUST DETECTION SYSTEM V3.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V8.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v8.0_i9i9-2pby",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V8.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v8.0_i9i9-2pby",
-            "description": "Groundbased radar detections of asteroids, collected from the published literature by S. J. Ostro.",
-            "title": "ASTEROID RADAR V8.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID RADAR V8.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0877-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-04T21:08:45.000 to 2015-07-05T03:10:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0877-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0877-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0877-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-04T21:08:45.000 to 2015-07-05T03:10:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0877 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0877 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/LTVB4GPCOTK2",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2I3NVAER. Version 5.12.4. MERRA-2 inst3_3d_aer_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Aerosol Mixing Ratio V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/LTVB4GPCOTK2. https://disc.gsfc.nasa.gov/datacollection/M2I3NVAER_5.12.4.html. Digital Science Data.",
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
-                "atmospheric water vapor",
-                "earth science",
-                "aerosols",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812882-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2I3NVAER (or  inst3_3d_aer_Nv) is an instantaneous 3-dimensional 3-hourly data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of aerosol mixing ratio parameters at 72 model layers, such as dust, sulphur dioxide, sea salt, black carbon, and organic carbon.  The data field is available every three hour starting from 00:00 UTC, e.g.: 00:00, 03:00, \u2026 , 21:00 UTC. Section 4.2 of the MERRA-2 File Specification document provides pressure values nominal for a 1000 hPa surface pressure and refers to the top edge of the layer. The lev=1 is for the top layer, and lev=72 is for the bottom (or surface) model layer. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2I3NVAER",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2I3NVAER variable",
-            "title": "MERRA-2 inst3_3d_aer_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Aerosol Mixing Ratio 0.625 x 0.5 degree V5.12.4 (M2I3NVAER) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I3NVAER_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLTVB4GPCOTK2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLTVB4GPCOTK2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I3NVAER_5.12.4.png",
-                    "description": "M2I3NVAER variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2I3NVAER variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I3NVAER_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2I3NVAER_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2I3NVAER_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVAER.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVAER.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2I3NVAER",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2I3NVAER",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2I3NVAER.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2I3NVAER.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2I3NVAER.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2I3NVAER.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2I3NVAER.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2I3NVAER.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVAER.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVAER.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2I3NVAER variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I3NVAER_5.12.4.png",
+            "identifier": "C1276812882-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "aerosols",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/LTVB4GPCOTK2",
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
+            "series-name": "M2I3NVAER",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 inst3_3d_aer_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Aerosol Mixing Ratio 0.625 x 0.5 degree V5.12.4 (M2I3NVAER) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Q0AVPHN3250H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge UAF L1B HF Geolocated Radar Echo Strength Profiles V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/Q0AVPHN3250H.",
-            "issued": "2013-03-22",
-            "temporal": "2013-03-22T00:00:00Z/2016-08-16T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-08-16",
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
-            "identifier": "C2027966332-NSIDC_ECS",
             "description": "This data set contains radar echograms acquired by the University of Alaska Fairbanks High-Frequency Radar Sounder over select glaciers in Alaska. The data are provided in HDF5 formatted files, which include important metadata for interpreting the data. Browse images are also available.",
-            "title": "IceBridge UAF L1B HF Geolocated Radar Echo Strength Profiles V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQ0AVPHN3250H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQ0AVPHN3250H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRUAFHF1B.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRUAFHF1B.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2027966332-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=IRUAFHF1B&tl=1601390090%214%21%21&m=55.293751678684046%21-177.59448335049868%213%211%210%210%2C2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2027966332-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=IRUAFHF1B&tl=1601390090%214%21%21&m=55.293751678684046%21-177.59448335049868%213%211%210%210%2C2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/icebridge/portal/map",
-                    "description": "Tool to visualize, search, and download IceBridge data.",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to visualize, search, and download IceBridge data.",
+                    "downloadURL": "https://nsidc.org/icebridge/portal/map",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRUAFHF1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRUAFHF1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Q0AVPHN3250H",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/Q0AVPHN3250H",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Q0AVPHN3250H",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/Q0AVPHN3250H",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2027966332-NSIDC_ECS",
+            "issued": "2013-03-22",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Q0AVPHN3250H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-08-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-157.0 56.0 -129.0 63.0",
+            "temporal": "2013-03-22T00:00:00Z/2016-08-16T23:59:59.999Z",
             "theme": [
                 "2013_AK_UAF",
                 "2014_AK_UAF",
@@ -904700,256 +904701,232 @@
                 "2016_AK_UAF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge UAF L1B HF Geolocated Radar Echo Strength Profiles V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-POS-5-SUMM-HGCOORDS-48SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains Voyager 2 position vectors relative to the Sun in both cartesian and spherical Heliographic coordinates for the time when Voyager 2 was near Uranus but not within its magnetosphere. The position vectors are given every 48 seconds. The units of the vector components are Au and degrees. Vectors are stored as 4-byte floating point values.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pos-5-summ-hgcoords-48sec-v1.0_i9mh-yuap",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "uranus",
                 "voyager",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-POS-5-SUMM-HGCOORDS-48SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pos-5-summ-hgcoords-48sec-v1.0_i9mh-yuap",
-            "description": "This dataset contains Voyager 2 position vectors relative to the Sun in both cartesian and spherical Heliographic coordinates for the time when Voyager 2 was near Uranus but not within its magnetosphere. The position vectors are given every 48 seconds. The units of the vector components are Au and degrees. Vectors are stored as 4-byte floating point values.",
-            "title": "VG2 URA TRAJECTORY DERIV SUMM HELIOGRAPHIC COORDS 48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 URA TRAJECTORY DERIV SUMM HELIOGRAPHIC COORDS 48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0715-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-18T08:15:10.000 to 2015-04-18T10:29:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0715-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0715-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0715-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-18T08:15:10.000 to 2015-04-18T10:29:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0715 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0715 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/B0HL940D452L",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge CAMBOT L1B Geolocated Images V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/B0HL940D452L.",
-            "issued": "2018-10-10",
-            "temporal": "2018-10-10T00:00:00Z/2019-11-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-20",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Studinger",
                 "hasEmail": "mailto:michael.studinger@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1659416445-NSIDC_ECS",
             "description": "This data set contains high-resolution imagery taken with the Continuous Airborne Mapping By Optical Translator (CAMBOT) system over Antarctica and Greenland. The data were collected as part of Operation IceBridge funded aircraft survey campaigns.",
-            "title": "IceBridge CAMBOT L1B Geolocated Images V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB0HL940D452L",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB0HL940D452L",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/icebridge/portal/map",
-                    "description": "Tool to visualize, search, and download IceBridge data.",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to visualize, search, and download IceBridge data.",
+                    "downloadURL": "https://nsidc.org/icebridge/portal/map",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IOCAM1B.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IOCAM1B.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1659416445-NSIDC_ECS&q=iocam1b&m=-143.17234601407074%21-36.69873046875%210%211%210%210%2C2&tl=1559661355%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1659416445-NSIDC_ECS&q=iocam1b&m=-143.17234601407074%21-36.69873046875%210%211%210%210%2C2&tl=1559661355%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IOCAM1B/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IOCAM1B/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/B0HL940D452L",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/B0HL940D452L",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/B0HL940D452L",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/B0HL940D452L",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1659416445-NSIDC_ECS",
+            "issued": "2018-10-10",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/B0HL940D452L",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-11-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 60.0 180.0 90.0",
+            "temporal": "2018-10-10T00:00:00Z/2019-11-20T23:59:59.999Z",
             "theme": [
                 "2018_AN_NASA",
                 "2019_AN_NASA",
                 "2019_GR_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge CAMBOT L1B Geolocated Images V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acassini_high_rate_detector&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The High Rate Detector (HRD) from the    University of Chicago is an independent part of the CDA instrument on  the Cassini Orbiter that measures the dust flux and particle mass      distribution of dust particles hitting the HRD detectors.  This data   set includes all data from the HRD through the end of the mission,     Sept. 15, 2017.  Please refer to Srama et al. (2004) for a detailed    HRD description.",
+            "identifier": "urn:nasa:pds:cassini_high_rate_detector",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration target",
                 "cassini-huygens",
                 "dust"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acassini_high_rate_detector&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:cassini_high_rate_detector",
-            "description": "The High Rate Detector (HRD) from the    University of Chicago is an independent part of the CDA instrument on  the Cassini Orbiter that measures the dust flux and particle mass      distribution of dust particles hitting the HRD detectors.  This data   set includes all data from the HRD through the end of the mission,     Sept. 15, 2017.  Please refer to Srama et al. (2004) for a detailed    HRD description.",
-            "title": "CASSINI HIGH RATE DETECTOR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI HIGH RATE DETECTOR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567672-USGS_LTA.html",
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
-                "agriculture",
-                "surface radiative properties",
-                "land surface",
-                "forest science",
-                "agricultural engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LONG TERM ARCHIVE",
                 "hasEmail": "mailto:lta@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220567672-USGS_LTA",
             "description": "The National Agriculture Imagery Program (NAIP) acquires aerial imagery during the agricultural growing seasons in the continental U.S. A primary goal of the NAIP program is to make digital ortho photography available to governmental agencies and the public within a year of acquisition.\n \nNAIP is administered by the USDA's Farm Service Agency (FSA) through the Aerial Photography Field Office in Salt Lake City. This \"leaf-on\" imagery is used as a base layer for GIS programs in FSA's County Service Centers, and is used to maintain the Common Land Unit (CLU) boundaries.",
-            "title": "National Agriculture Imagery Program (NAIP)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n         \n         Typically, all data available from USGS/EROS are downloadable at no cost  to the user. there are some cases when a service fee is required to  convert the analog film record to a digital file. This non-refundable fee  is $30 per scene/frame.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n         \n         Typically, all data available from USGS/EROS are downloadable at no cost  to the user. there are some cases when a service fee is required to  convert the analog film record to a digital file. This non-refundable fee  is $30 per scene/frame.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
@@ -904959,62 +904936,87 @@
                     "title": "Access to this dataset's extended metadata"
                 }
             ],
+            "identifier": "C1220567672-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "topography",
+                "agriculture",
+                "surface radiative properties",
+                "land surface",
+                "forest science",
+                "agricultural engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567672-USGS_LTA.html",
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
+            "title": "National Agriculture Imagery Program (NAIP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2788-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-03-05T15:55:50 to 2011-03-05T18:49:57.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2788-v1.0_i9s3-kbj6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2788-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2788-v1.0_i9s3-kbj6",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-03-05T15:55:50 to 2011-03-05T18:49:57.500.",
-            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2788 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2788 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M03-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m03-v3.0_i9sv-5fcs",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
@@ -905024,486 +905026,462 @@
                 "vega",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M03-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m03-v3.0_i9sv-5fcs",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 3 PRL-MTP003 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 3 PRL-MTP003 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5X63JV3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AIDJEX Beaufort Sea Upward Looking Sonar April 1976, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5X63JV3.",
-            "issued": "1976-04-07",
-            "temporal": "1976-04-07T00:00:00Z/1976-04-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1976-04-10",
-            "keyword": [
-                "cryosphere",
-                "earth science",
-                "oceans",
-                "sea ice"
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
-            "identifier": "C1386206523-NSIDCV0",
             "description": "This data contains Upward Looking Sonar (ULS) profiles of the underside of the Arctic pack ice along three transects whose total length is 777 nautical miles. The data were obtained by the USS Gurnard (SSN-662), a U.S. Navy submarine, on a traverse of the AIDJEX Main Experiment area in the Beaufort Sea from 07 April 1976 to 10 April 1976. The sea ice thickness derived from the ULS is given in feet.\n\nThe data are in a single ASCII text file: Aidjex_04_1976_uls.txt. The data in this text file are not formatted into columns; all data are presented in one long row separated by spaces. Little is known about the format of the file, so caution should be used when working with the data. NSIDC is providing this data as part of our effort to preserve historical data.  The data file begins with nine values that appear to be header information. These nine values include latitude and longitude values along with other unknown values. After the header, there are approximately 2100 measurements of what NSIDC believes is sea ice thickness in feet, however it is unclear how often these measurements were taken. After these 2100 values, another header of nine values occurs followed again by 2100 measurements. The file continues in this pattern through the remainder of the file. Users with information about the contents of the file are encouraged to contact <a href=\"mailto:nsidc.org\">NSIDC User Services</a>.\n\nTwo supporting documents that provide some background have been scanned and included as PDF files. These are AIDJEX_ULS_background.pdf and AIDJEX_ULS_format.pdf. \n\nThese data are available via FTP. \n\n<strong>Note:</strong> These data are in a raw format with unknown fields and are being provided as is for preservation purposes. A processed version of the data are available in the <a href=\"/data/g01360.html\">Submarine Upward Looking Sonar Ice Draft Profile Data and Statistics</a> data set.",
-            "title": "AIDJEX Beaufort Sea Upward Looking Sonar April 1976, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5X63JV3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5X63JV3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02191_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02191_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5X63JV3",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5X63JV3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5X63JV3",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5X63JV3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206523-NSIDCV0",
+            "issued": "1976-04-07",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "oceans",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5X63JV3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1976-04-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-155.0 70.0 -137.0 76.0",
+            "temporal": "1976-04-07T00:00:00Z/1976-04-10T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIDJEX Beaufort Sea Upward Looking Sonar April 1976, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/739/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-05-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
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
-            "identifier": "DASHLINK_739",
             "description": "Prognostics is an emerging concept in condition basedmaintenance(CBM)ofcriticalsystems.Alongwith developing the fundamentals of being able to confidently predict Remaining Useful Life (RUL), the technology calls for fielded applications as it inches towards maturation. This requires a stringent performance evaluation so that the significance of the concept can be fully exploited. Currently, prognostics concepts lack standard definitions and suffer from ambiguous and inconsistent interpretations. This lack of standards is in part due to the varied end-user requirements for different applications, time scales, available information, domain dynamics, etc. to name a few issues. Instead, the research community has used a variety of metrics based largely on convenience with respect to their respective requirements. Very little attention has been focused on establishing a common ground to compare different efforts. This paper surveys the metrics that are already used for prognostics in a variety of domains including medicine, nuclear, automotive, aerospace, and electronics. It also considers other domains that involve prediction-related tasks, such as weather and finance. Differences and similarities between these domains and health maintenancehave been analyzed to help understand what performance evaluation methods may or may not be borrowed. Further, these metrics have been categorized in several ways that may be useful in deciding upon a suitable subset for a specific application. Some important prognostic concepts have been defined using a notational framework that enables interpretation of different metrics coherently. Last, but not the least, a list of metrics has been suggested to assess critical aspects of RUL predictions before they are fielded in real applications.",
-            "title": "A Survey of Metrics for Performance Evaluation of Prognostics",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2008_IEEEPHM_MetricsSurvey.pdf",
-                    "description": "2008_IEEEPHM_MetricsSurvey.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2008_IEEEPHM_MetricsSurvey.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2008_IEEEPHM_MetricsSurvey.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2008_IEEEPHM_MetricsSurvey.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_739",
+            "issued": "2013-05-13",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/739/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Survey of Metrics for Performance Evaluation of Prognostics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0534.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs Northern Hemisphere State of Cryosphere Daily 25km EASE-Grid 2.0 V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0534.001.",
-            "issued": "1999-01-01",
-            "temporal": "1999-01-01T00:00:00Z/2012-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-12-31",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "snow/ice",
-                "earth science",
-                "sea ice",
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C1402083137-NSIDC_ECS",
             "description": "This data set, part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, reports the location of Northern Hemisphere snow cover and sea ice extent, the status of melt onset across Greenland and Arctic sea ice, and the level of agreement between three different snow cover data sources.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "MEaSUREs Northern Hemisphere State of Cryosphere Daily 25km EASE-Grid 2.0 V001",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?p=arctic&l=BlueMarble_NextGeneration,MEaSUREs_Sea_Ice_Snow_Extent,Coastlines&t=1999-01-01",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FCRYOSPHERE%2Fnsidc-0534.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FCRYOSPHERE%2Fnsidc-0534.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0534.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0534.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1402083137-NSIDC_ECS&q=NSIDC-0534&m=-22%21-70.6875%211%211%210%210%2C2&tl=1576704762%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1402083137-NSIDC_ECS&q=NSIDC-0534&m=-22%21-70.6875%211%211%210%210%2C2&tl=1576704762%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0534/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0534/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0534.001",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0534.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0534.001",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0534.001",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?p=arctic&l=BlueMarble_NextGeneration,MEaSUREs_Sea_Ice_Snow_Extent,Coastlines&t=1999-01-01",
+            "identifier": "C1402083137-NSIDC_ECS",
+            "issued": "1999-01-01",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "earth science",
+                "sea ice",
+                "national geospatial data asset",
+                "ngda",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0534.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "1999-01-01T00:00:00Z/2012-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs Northern Hemisphere State of Cryosphere Daily 25km EASE-Grid 2.0 V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/L3_CLOUD_OCCURRENCE-STANDARD-V1-00",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-12-05. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/L3_CLOUD_OCCURRENCE-STANDARD-V1-00. https://asdc.larc.nasa.gov/project/CALIPSO.",
-            "issued": "2018-11-06",
-            "temporal": "2006-06-01T00:00:00Z/2017-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-06",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHARLES Trepte",
                 "hasEmail": "mailto:charles.r.trepte@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1575511329-LARC_ASDC",
             "description": "CAL_LID_L3_Cloud_Occurrence-Standard-V1-00 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) Lidar Level 3 Cloud Occurrence Data, Standard Version 1-00 data product. This data product was collected using the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP) instrument. Data collection for this product is complete. \r\rThis product reports global distributions of clouds on a uniform spatial grid. All level 3 parameters are derived from the CALIPSO level 2 data, with a temporal averaging of one month. \r\rCALIPSO was launched on April 28, 2006 and continues to collect data necessary to study the impact of clouds and aerosols on the Earth's radiation budget and climate . It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Lidar Level 3 Cloud Occurrence Data, Standard V1-00",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FL3_CLOUD_OCCURRENCE-STANDARD-V1-00",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FL3_CLOUD_OCCURRENCE-STANDARD-V1-00",
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
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/L3_CLOUD_OCCURRENCE-STANDARD-V1-00",
-                    "description": "DOI data set landing page for CAL_LID_L3_Cloud_Occurrence-Standard-V1-00_V1-00",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L3_Cloud_Occurrence-Standard-V1-00_V1-00",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/L3_CLOUD_OCCURRENCE-STANDARD-V1-00",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575511329-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L3_Cloud_Occurrence-Standard-V1-00_V1-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L3_Cloud_Occurrence-Standard-V1-00_V1-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575511329-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L3_Cloud_Occurrence-Standard-V1-00/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L3_Cloud_Occurrence-Standard-V1-00_V1-00",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L3_Cloud_Occurrence-Standard-V1-00_V1-00",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L3_Cloud_Occurrence-Standard-V1-00/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l3_cloud_occurrence_v1-00.php",
-                    "description": "Detailed Data Quality Summary for the CALIPSO Version 1.00 Lidar Level 3 Cloud Occurrence Monthly Data Product",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed Data Quality Summary for the CALIPSO Version 1.00 Lidar Level 3 Cloud Occurrence Monthly Data Product",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l3_cloud_occurrence_v1-00.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
-                    "description": "CALIPSO Data User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
-                    "description": "CALIPSO - Data Availability Site",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Availability Site",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
-                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/project_documentation.php",
-                    "description": "CALIPSO - List of project documentation (Data Products Catalog and ATBDs)",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of project documentation (Data Products Catalog and ATBDs)",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/project_documentation.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/faq.php",
-                    "description": "CALIPSO Data User\u2019s Guide - Frequently Asked Questions",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide - Frequently Asked Questions",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/faq.php",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
-                    "description": "CALIPSO Tilt Mode Geometry Anomaly",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Tilt Mode Geometry Anomaly",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
-                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
+                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://calipso.cnes.fr/fr",
-                    "description": "French (CNES) CALIPSO Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "French (CNES) CALIPSO Home Page",
+                    "downloadURL": "https://calipso.cnes.fr/fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.icare.univ-lille.fr",
-                    "description": "ICARE Data and Services Center Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Data and Services Center Home Page",
+                    "downloadURL": "https://www.icare.univ-lille.fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
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
-                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
-                    "description": "NASA Mission Overview of CALIPSO",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Mission Overview of CALIPSO",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/ASDC_CALIPSO_Overview_2015.pdf",
-                    "description": "Overview of CALIPSO Data at the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of CALIPSO Data at the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/ASDC_CALIPSO_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L3_Cloud_Occurrence-Standard-V1-00/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L3_Cloud_Occurrence-Standard-V1-00_V1-00",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L3_Cloud_Occurrence-Standard-V1-00_V1-00",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L3_Cloud_Occurrence-Standard-V1-00/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
-                    "description": "Overview of CALIPSO Data Product Maturity",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of CALIPSO Data Product Maturity",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_release_summary_statement.html",
-                    "description": "CALIPSO Data Release Summary Statement",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data Release Summary Statement",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_release_summary_statement.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
-                    "description": "CALIPSO Products Overview",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Products Overview",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
-                    "description": "ICARE Programmers Toolbox",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Programmers Toolbox",
+                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
                 }
             ],
+            "identifier": "C1575511329-LARC_ASDC",
+            "issued": "2018-11-06",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/L3_CLOUD_OCCURRENCE-STANDARD-V1-00",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-11-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -85.0 180.0 85.0",
+            "temporal": "2006-06-01T00:00:00Z/2017-01-01T23:59:59Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Lidar Level 3 Cloud Occurrence Data, Standard V1-00"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2913027533-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee. 2022-03-01. OCO2_L2_Diagnostic. Version 11.2. OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information V11.2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Diagnostic_11.2.html. Digital Science Data.",
-            "issued": "2024-04-01",
-            "temporal": "2019-11-30T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-01",
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
-            "identifier": "C2913027533-GES_DISC",
-            "description": "Version 11.2 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection encompass various data fields used for diagnostic and pre-processing, including aerosol optical depth, albedo, absorption coefficients, fluorescence, XCO2 uncertainties, averaging kernel, surface type, etc.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_Diagnostic",
             "creator": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee",
-            "title": "OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information V11.2 (OCO2_L2_Diagnostic) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Dia_10__10132021.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11.2 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection encompass various data fields used for diagnostic and pre-processing, including aerosol optical depth, albedo, absorption coefficients, fluorescence, XCO2 uncertainties, averaging kernel, surface type, etc.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -905512,262 +905490,298 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Diagnostic_11.2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Diagnostic_11.2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Diagnostic.11.2/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Diagnostic.11.2/",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Diagnostic.11.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Diagnostic.11.2/contents.html",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Dia_10__10132021.png",
+            "identifier": "C2913027533-GES_DISC",
+            "issued": "2024-04-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2913027533-GES_DISC.html",
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
+            "series-name": "OCO2_L2_Diagnostic",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-11-30T00:00:00Z/2024-04-22T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information V11.2 (OCO2_L2_Diagnostic) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "http://techport.nasa.gov/view/64",
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
-                "cif",
-                "program",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrew Keys",
                 "hasEmail": "mailto:andrew.keys@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_64",
             "description": "&lt;p&gt;\r\n\tTo stimulate and encourage creativity and innovation within the NASA Centers. The activities are envisioned to fall within the scope of NASA Space Technology or technology addressing a significant National need.&lt;/p&gt;",
-            "title": "Center Innovation Fund Program",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/64",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_64",
+            "issued": "2018-06-25",
+            "keyword": [
+                "cif",
+                "program",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/64",
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
+            "title": "Center Innovation Fund Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/84",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Goward, S.N., J. Yang, and K.F. Huemmrich. 1994. SE-590 Landscape Reflectances (OTTER). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/84",
-            "issued": "2023-11-19",
-            "temporal": "1990-10-06T00:00:00Z/1990-10-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
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
-            "identifier": "C2804776928-ORNL_CLOUD",
             "description": "Bidirectional spectal reflectance factors of landscape elements (litter, soil, bark, scrubs & grasses, leaves) measured by Spectron SE590 spectroradiometer",
-            "graphic-preview-description": "Browse Image",
-            "title": "SE-590 Landscape Reflectances (OTTER)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/otter_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F84",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F84",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/otter/spectra_se590_landscape/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/otter/spectra_se590_landscape/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/OTTER/guides/SE590_Landscape_Reflectance_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/OTTER/guides/SE590_Landscape_Reflectance_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/84",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/84",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_landscape/comp/goward.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_landscape/comp/goward.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_landscape/comp/se590.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_landscape/comp/se590.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_landscape/comp/SE590_Landscape_Reflectance_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_landscape/comp/SE590_Landscape_Reflectance_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/otter_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/otter_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/otter_logo_square.png",
+            "identifier": "C2804776928-ORNL_CLOUD",
+            "issued": "2023-11-19",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/84",
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
             "spatial": "-123.95 44.29 -121.33 45.07",
+            "temporal": "1990-10-06T00:00:00Z/1990-10-11T23:59:59Z",
             "theme": [
                 "OTTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SE-590 Landscape Reflectances (OTTER)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition38/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "Press kit for ISS mission Expedition 38 from 09/2013-03/2014. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Press Kit PDF",
+                    "downloadURL": "http://www.nasa.gov/sites/default/files/files/NP-2013-11-028-JSC-Expedition-38-summary.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "ISS 38 Press Kit"
+                }
+            ],
+            "identifier": "OCIO-Fitara-48",
             "issued": "2014-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "2013",
                 "schedule",
@@ -905780,121 +905794,109 @@
                 "38",
                 "2014"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition38/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:037"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "JSC"
             },
-            "identifier": "OCIO-Fitara-48",
-            "description": "Press kit for ISS mission Expedition 38 from 09/2013-03/2014. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
-            "title": "ISS Expedition 38 Press Kit",
-            "programCode": [
-                "026:037"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/sites/default/files/files/NP-2013-11-028-JSC-Expedition-38-summary.pdf",
-                    "description": "Press Kit PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "ISS 38 Press Kit"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ISS Expedition 38 Press Kit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/806/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-07-23",
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
-            "identifier": "DASHLINK_806",
             "description": "An approach for predicting remaining useful life of power MOSFETs (metal oxide field effect transistor) devices has been developed. Power MOSFETs are semiconductor switching devices that are instrumental in electronics equipment such as those used in operation and control of modern aircraft and spacecraft. The MOSFETs examined here were aged under thermal overstress in a controlled experiment and continuous performance degradation data were collected from the accelerated aging experiment. Die- attach degradation was determined to be the primary failure mode. The collected run-to-failure data were analyzed and it was revealed that ON-state resistance increased as die-attach degraded under high thermal stresses. Results from finite element simulation analysis support the observations from the experimental data. Data-driven and model based prognostics algorithms were investigated where ON-state resistance was used as the primary precursor of failure feature. A Gaussian process regression algorithm was explored as an example for a data-driven technique and an extended Kalman filter and a particle filter were used as examples for model-based techniques. Both methods were able to provide valid results. Prognostic performance metrics were employed to evaluate and compare the algorithms.",
-            "title": "Prognostics of Power MOSFETs under Thermal Stress Accelerated Aging using Data-Driven and Model-Based Methodologies",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/TN_3991_Celaya.pdf",
-                    "description": "TN_3991_Celaya.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "TN_3991_Celaya.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/TN_3991_Celaya.pdf",
+                    "mediaType": "application/pdf",
                     "title": "TN_3991_Celaya.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_806",
+            "issued": "2013-07-23",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/806/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Prognostics of Power MOSFETs under Thermal Stress Accelerated Aging using Data-Driven and Model-Based Methodologies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M08-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-23 to 2014-10-24.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m08-v1.0_iabe-chqt",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M08-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m08-v1.0_iabe-chqt",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-23 to 2014-10-24.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 008 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 008 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-V%2FE%2FJ%2FS%2FSS-RPWS-4-SUMM-KEY60S-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Cassini Radio and Plasma Wave Science (RPWS) calibrated summary key parameter data set includes reduced temporal and spectral resolution spectral information calibrated in units of spectral density for the entire Cassini mission.  This data set includes calibrated values binned and averaged within 1 minute by 0.1 decade spectral channels for all times during the mission including the two Venus flybys, the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data for this data set are acquired by the RPWS Low Frequency Receiver (LFR), Medium Frequency Receiver (MFR), and High Frequency Receiver (HFR).  Data are presented in a set of fixed-record-length tables.  This data set is intended to provide numerical summary data which can be used in conjunction with other Cassini fields and particles key parameter data sets to establish trends, select events, or simply as a browse data set for the Cassini RPWS archive.  This data set should be among the first used by a user of any of the RPWS archive as it will lead one to information required to search for more detailed or highly specialized products.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-v-e-j-s-ss-rpws-4-summ-key60s-v1.0_iaci-czgv",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "phoebe",
                 "cassini-huygens",
@@ -905912,76 +905914,44 @@
                 "iapetus",
                 "hyperion"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-V%2FE%2FJ%2FS%2FSS-RPWS-4-SUMM-KEY60S-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-v-e-j-s-ss-rpws-4-summ-key60s-v1.0_iaci-czgv",
-            "description": "The Cassini Radio and Plasma Wave Science (RPWS) calibrated summary key parameter data set includes reduced temporal and spectral resolution spectral information calibrated in units of spectral density for the entire Cassini mission.  This data set includes calibrated values binned and averaged within 1 minute by 0.1 decade spectral channels for all times during the mission including the two Venus flybys, the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data for this data set are acquired by the RPWS Low Frequency Receiver (LFR), Medium Frequency Receiver (MFR), and High Frequency Receiver (HFR).  Data are presented in a set of fixed-record-length tables.  This data set is intended to provide numerical summary data which can be used in conjunction with other Cassini fields and particles key parameter data sets to establish trends, select events, or simply as a browse data set for the Cassini RPWS archive.  This data set should be among the first used by a user of any of the RPWS archive as it will lead one to information required to search for more detailed or highly specialized products.",
-            "title": "CASSINI V/E/J/S/SS RPWS SUMMARY KEY PARAMETER 60S V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI V/E/J/S/SS RPWS SUMMARY KEY PARAMETER 60S V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/KMJ8Q9ZA1Y3K",
             "citation": "AIRS project, Jet  Propulsion Laboratory. 2022-01-31. SNDRAQIML1CCALSUBRND. Version 2. Sounder SIPS: Aqua AIRS Level-1C Calibration Subset: Random Full Spectra, V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/KMJ8Q9ZA1Y3K. https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML1CCALSUBRND_2.html. Digital Science Data.",
-            "issued": "2022-01-05",
-            "temporal": "2002-08-31T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-26",
-            "references": [
-                "https://doi.org/10.3390/rs12172743",
-                "https://doi.org/10.3390/rs12081338"
-            ],
-            "keyword": [
-                "atmosphere",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "oceans",
-                "ocean heat budget",
-                "earth science",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.f.iredell@nasa.gov"
             },
+            "creator": "AIRS project, Jet  Propulsion Laboratory",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2210183595-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. AIRS/Aqua Level-1C calibration subset including clear cases, special calibration sites, random nadir spots, and high clouds. Infrared temperature sounders generate a large amount of Level-1B spectral data.  For example, the AIRS instrument with 2378 channels, its visible light component and AMSU with 15 channels create 3x240 files each day, for a total of over 500 MB of data. \n\nThe purpose of the Calibration Data Subsets is extract key information from these data into a few daily files to:\n    1. Facilitate a quick evaluation of the absolute calibration of the instruments.\n    2. Facilitate an assessment of the instrument performance under clear, cloudy, and extreme hot and cold conditions.\n    3. Facilitate the evaluation of instrument trends and their significance relative to climate trends.\n    4. Facilitate the comparison of AIRS with CrIS using their equivalent data subsets.\nThe output files are constructed from Level-1B or Level-1C IR and MW brightness or antenna temperatures.  Each file contains selected observations taken from a nominal 24-hour period.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRAQIML1CCALSUBRND",
-            "creator": "AIRS project, Jet  Propulsion Laboratory",
-            "title": "Sounder SIPS: Aqua AIRS Level-1C Calibration Subset: Random Full Spectra V2 (SNDRAQIML1CCALSUBRND) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML1CCALSUBRND.2.amsua.bt.channel3.20220111.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKMJ8Q9ZA1Y3K",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKMJ8Q9ZA1Y3K",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -905991,186 +905961,228 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML1CCALSUBRND_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML1CCALSUBRND_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Calibration_Subsets/SNDRAQIML1CCALSUBRND.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Calibration_Subsets/SNDRAQIML1CCALSUBRND.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Calibration_Subsets/SNDRAQIML1CCALSUBRND.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Calibration_Subsets/SNDRAQIML1CCALSUBRND.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIML1CCALSUBRND+2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIML1CCALSUBRND+2",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SNDRAQIML1CCALSUBRND_2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SNDRAQIML1CCALSUBRND_2.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/ATBD_CalSub_AIRS.CrIS.SNPP.20230210.pdf",
-                    "description": "ATBD documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD documentation",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/ATBD_CalSub_AIRS.CrIS.SNPP.20230210.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML1CCALSUBRND.2.amsua.bt.channel3.20220111.png",
+            "identifier": "C2210183595-GES_DISC",
+            "issued": "2022-01-05",
+            "keyword": [
+                "atmosphere",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "oceans",
+                "ocean heat budget",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/KMJ8Q9ZA1Y3K",
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
+            "references": [
+                "https://doi.org/10.3390/rs12172743",
+                "https://doi.org/10.3390/rs12081338"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRAQIML1CCALSUBRND",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Aqua AIRS Level-1C Calibration Subset: Random Full Spectra V2 (SNDRAQIML1CCALSUBRND) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805813-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2024-07-19",
-            "temporal": "2017-11-29T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "ocean temperature",
-                "earth science",
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
-            "identifier": "C3166805813-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-20 VIIRS Level-3 Global Binned Triple-window Sea Surface Temperature (SST3) - Near Real Time (NRT) Data, version 2024.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
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
+            "identifier": "C3166805813-OB_DAAC",
+            "issued": "2024-07-19",
+            "keyword": [
+                "ocean temperature",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805813-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-11-29T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-20 VIIRS Level-3 Global Binned Triple-window Sea Surface Temperature (SST3) - Near Real Time (NRT) Data, version 2024.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-4-CR4A-V1.0",
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
+            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 4A mission phase, which occurred during July 2008.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-4-cr4a-v1.0_iamk-e48u",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-4-CR4A-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-4-cr4a-v1.0_iamk-e48u",
-            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 4A mission phase, which occurred during July 2008.",
-            "title": "ROSETTA-ORBITER CAL ALICE 4 CR4A V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL ALICE 4 CR4A V1.0"
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
+            "description": "These images display several of Neptune's moons approved by the International Astronomical Union (IAU).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/proteus.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-198",
             "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "images",
                 "moons",
@@ -906182,329 +906194,326 @@
                 "imagery",
                 "proteus"
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
-            "identifier": "OCIO-Fitara-198",
-            "description": "These images display several of Neptune's moons approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Neptunian System: Proteus",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/proteus.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Neptunian System: Proteus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1292-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-27T17:25:20.000 to 2015-12-28T00:35:06.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1292-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1292-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1292-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-27T17:25:20.000 to 2015-12-28T00:35:06.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1292 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1292 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141685-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 FIRSTLOOK Component Global Cloud Product covering a day's products;See ProductionDateTime for Published date.",
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
-            "identifier": "C156141685-LARC",
             "description": "This file contains the public MISR Level 3 FIRSTLOOK Component Global Cloud Product covering a day",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 FIRSTLOOK Component Global Cloud Product covering a day V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141685-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141685-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C156141685-LARC",
+            "issued": "2007-07-30",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141685-LARC.html",
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
+            "title": "MISR Level 3 FIRSTLOOK Component Global Cloud Product covering a day V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/N4CJ9HTW7WJL",
             "citation": "Kevin W. Bowman. 2021-03-08. TRPSDL2O3CRSWCF. Version 1. TROPESS CrIS-SNPP L2 Ozone for West Coast Fires, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/N4CJ9HTW7WJL. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRSWCF_1.html. Digital Science Data.",
-            "issued": "2021-01-22",
-            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-22",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1029/2006JD007258",
-                "https://doi.org/10.5194/acp-10-9901-2010",
-                "https://doi.org/10.1029/2007JD008819",
-                "https://doi.org/10.5194/amt-6-1413-2013",
-                "https://doi.org/10.5194/amt-11-5587-2018"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1980429446-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Ozone for West Coast Fires, Standard Product contains the vertical distribution of the retrieved atmospheric state of ozone (O3), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. This product focuses on the CONUS region (20N-60N; 150W-40W) for the time period from 2020-08-01 to 2020-10-31, during the outbreak of U.S. West Coast wildfires. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 26 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2O3CRSWCF",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS/SNPP O3 (West Coast Fires, Special Product) at 261 hPa on 12 September 2020.",
-            "title": "TROPESS CrIS-SNPP L2 Ozone for West Coast Fires, Standard Product V1 (TRPSDL2O3CRSWCF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSWCF_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FN4CJ9HTW7WJL",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FN4CJ9HTW7WJL",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSWCF_Sample.png",
-                    "description": "TROPESS CrIS/SNPP O3 (West Coast Fires, Special Product) at 261 hPa on 12 September 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS/SNPP O3 (West Coast Fires, Special Product) at 261 hPa on 12 September 2020.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSWCF_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRSWCF_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRSWCF_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2O3CRSWCF.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2O3CRSWCF.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3CRSWCF_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3CRSWCF_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2O3CRSWCF.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2O3CRSWCF.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2O3CRSWCF.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2O3CRSWCF.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS/SNPP O3 (West Coast Fires, Special Product) at 261 hPa on 12 September 2020.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSWCF_Sample.png",
+            "identifier": "C1980429446-GES_DISC",
+            "issued": "2021-01-22",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/N4CJ9HTW7WJL",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-01-22",
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
+            "series-name": "TRPSDL2O3CRSWCF",
             "spatial": "-150.0 20.0 -40.0 60.0",
+            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Ozone for West Coast Fires, Standard Product V1 (TRPSDL2O3CRSWCF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.0",
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
+            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.0_iatq-9pd9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.0_iatq-9pd9",
-            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
-            "title": "CASSINI SATURN UVIS SOLAR STELLAR BRIGHTNESS TIME SERIES 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI SATURN UVIS SOLAR STELLAR BRIGHTNESS TIME SERIES 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/iau7-5dni",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "['\"rna extraction\"' '\"labeling\"' '\"nucleic acid hybridization\"' '\"data collection\"' '\"treatment protocol\"' '\"sample collection\"']",
-                "['\"hindlimb unloading\"' '\"age\"' '\"study subject\"' '\"time\"']"
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
-            "identifier": "nasa_genelab_GLDS-354_iau7-5dni",
             "description": "['\"The annotation of the Affymetrix HTA 2.0 array was updated to optimise the detection of RNA in human skeletal muscle biopsy samples by removing invalid and low signal-high-variance probes (as for CDF GPL24047). The probes were then summarized into groups (probe-sets) reflecting either an ensembl full transcript identifier (FL-ENST, GPL24047) or just the probes targeting the 3\\' UTR or the 5\\' UTR of that particular ENST. Therefore, 3 different CDF were used to process the HTA 2.0 arrays in this study. Note that each CEL file was GC adjusted using APT while our custom CDF pipeline removes any probe that has >80% or <20% GC content (~50,000). The analysis was carried out only on the pairs of probe-sets i.e. FL-ENST vs 3\\'UTR or FL-ENST vs 5\\'UTR or 3\\'UTR vs 5\\'UTR. Dynamic muscle loading alters tissue phenotype reflecting altered metabolic and functional demands. In humans, heterogeneous adaptation to loading complicates identification of the underpinning molecular regulators. We present a within-person analysis strategy that reduced heterogeneity for changes in muscle mass by ~40% and employed a genome-wide transcriptome method that modeled each mRNA from coding exons and 3\u2019/5\u2019 untranslated (UTR) regions. Our strategy detected ~3-4 times more regulated genes than similarly sized studies, including substantial UTR-selective regulation that other methods would not detect. We discovered a core of 141 genes correlated to muscle growth validated from newly analyzed independent samples (n=100). Further validating these identified genes, via RNAi in primary muscle cells, we demonstrate that members of the core genes were regulators of protein synthesis e.g. Molecular Transducers of Physical Activity in Humans MoTrPAC. Employing proteome-constrained networks and pathway analysis revealed notable relationships with the molecular characteristics of human muscle aging and insulin sensitivity, as well as potential drug-therapies.\"']",
-            "title": "['\"Molecular Transducers of Human Skeletal Muscle Remodeling under Different Loading States\"']",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-354",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-354",
+                    "mediaType": "text/html",
                     "title": "['\"Molecular Transducers of Human Skeletal Muscle Remodeling under Different Loading States\"']"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-354_iau7-5dni",
+            "issued": "2021-05-21",
+            "keyword": [
+                "['\"rna extraction\"' '\"labeling\"' '\"nucleic acid hybridization\"' '\"data collection\"' '\"treatment protocol\"' '\"sample collection\"']",
+                "['\"hindlimb unloading\"' '\"age\"' '\"study subject\"' '\"time\"']"
+            ],
+            "landingPage": "https://data.nasa.gov/d/iau7-5dni",
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
+            "title": "['\"Molecular Transducers of Human Skeletal Muscle Remodeling under Different Loading States\"']"
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
+            "description": "A sampling of aircraft icing encounter reports from GA and Commuter flight crews.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://asrs.arc.nasa.gov/docs/rpsts/icing.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-807",
+            "issued": "2018-06-25",
             "keyword": [
                 "flight crew",
                 "general",
@@ -906514,404 +906523,407 @@
                 "icing",
                 "commuter"
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
-            "identifier": "NASA-807",
-            "description": "A sampling of aircraft icing encounter reports from GA and Commuter flight crews.",
-            "title": "Aviation Safety Reporting System: Commuter and GA Icing Incidents",
-            "programCode": [
-                "026:021"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://asrs.arc.nasa.gov/docs/rpsts/icing.pdf",
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
+            "title": "Aviation Safety Reporting System: Commuter and GA Icing Incidents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2PANNS.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2PANNS.008. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere",
-                "air quality"
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
-            "identifier": "C1618265601-LARC",
             "description": "TL2PANNS_8 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Atmospheric Temperatures Limb Version 8 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. It consisted of information for one molecular species for an entire Global Survey or Special Observation. TES Level 2 data contained retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits. Nadir and limb observations were in separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. \r\rA nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. A Global Survey consists of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species volume mixing ratios (VMRs), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object wa bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals were not reported. \r\rThe organization of data within the Swath object was based on a superset of the Upper Atmosphere Research Satellite (UARS) pressure levels that was used to report concentrations of trace atmospheric gases. The reporting grid was the same pressure grid used for modeling. There were 67 reporting levels from 1211.53 hPa, which allowed for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products reported values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files each observation could potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels were not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresponding to altitudes below the cloud top or surface, where measurements were not possible, a fill value was applied.\r\rTo minimize the duplication of information between the individual species standard products, data fields common to each species (such as spacecraft coordinates, emissivity, and other data fields) have been collected into a separate standard product, termed the TES L2 Ancillary Data product (ESDT short name: TL2ANC). U",
-            "title": "TES/Aura L2 Peroxyacyl Nitrate Nadir Special Observation V008",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2PANNS.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2PANNS.008",
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2PANNS.008",
-                    "description": "DOI data set landing page for TL2PANNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2PANNS_8",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2PANNS.008",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1618265601-LARC",
-                    "description": "Earthdata Search for TL2PANNS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2PANNS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1618265601-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2PANNS.008/contents.html",
-                    "description": "OPeNDAP data access for TL2PANNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2PANNS_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2PANNS.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2PANNS.008/",
-                    "description": "ASDC Direct Data Download for TL2PANNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2PANNS_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2PANNS.008/",
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
+            "identifier": "C1618265601-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2PANNS.008",
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
+            "title": "TES/Aura L2 Peroxyacyl Nitrate Nadir Special Observation V008"
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
-                "atmospheric pressure",
-                "altitude",
-                "spectral/engineering",
-                "platform characteristics",
-                "ocean temperature",
-                "oceans",
-                "infrared wavelengths",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul Bui",
                 "hasEmail": "mailto:thaopaul.v.bui@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2662399958-LARC_ASDC",
             "description": "SONEX_TraceGas_AircraftInSitu_DC8_Data_1 is the in-situ meteorological and navigation data collected onboard the DC-8 aircraft during the SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) suborbital campaign. Data collection for this product is complete.\r\nThe SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) was an international, multi-organizational mission that took place in October-November 1997. NASA was the US sponsor of SONEX that partnered with POLINAT-2 (Pollution from Aircraft Emissions in the North Atlantic Flight Corridor) funded by the German DLR (Deutsches Zentrum f\u00fcr Luft- und Raumfahrt) or German Aerospace Agency. NASA flew the DC-8 aircraft out of NASA/Ames Research Center. DLR operated an instrumented Falcon 20 aircraft. The staging locations for NAFC sampling were primarily Bangor, Maine (US), and Shannon, Ireland. Subsonic aircraft emissions impact several aspects of atmospheric composition: nitrogen oxides (NOx), CO, and hydrocarbons from emissions can perturb upper tropospheric/lower stratospheric (UT/LS) ozone; water vapor, soot, and sulfur oxides (SOx) emitted by aircraft may perturb clouds and aerosols, changing UT/LS radiative forcing and global temperature.\r\nIn SONEX and POLINAT, flights were conducted in the vicinity of the North Atlantic Flight Coordinator (NAFC) to observe the impact of aircraft emissions on NOx and ozone (O3). The DC-8 aircraft payload (Singh et al., 1999) primarily measured in-situ CO, CO2, hydrocarbons/halocarbons, O3, aerosols (Dibb et al., 2000), OH/HO2, water vapor, nitric acid (Talbot et al., 1999), photolysis rates, temperature, pressure, winds, NOx, and NOy.\r\nThree sampling approaches were implemented during SONEX. First, special meteorological (Fuelberg et al., 2000) were developed to allow targeted sampling for air parcels affected by aircraft emissions and various meteorological events, e.g., convection, lightning (Jeker et al., 2000), stratospheric intrusions (Cho et al., 2000). Second, because the NAFC had not been extensively sampled in the past, it was important for SONEX to characterize the climatology of trace species like CN (Wang et al., 2000), NOx and NOy (Koike et al., 2000). Third, tracers (Simpson et al., 2000; Thompson et al., 1999) and model sensitivity studies (Meijer et al., 2000) were employed for Air Mass Identification. This sampling strategy answered the following questions: Where and when are air masses found with the greatest aircraft influence? When and where was stratospheric air sampled? SONEX showed a substantial impact of aircraft emissions on UT/LS NOx and CN in the vicinity of fresh aircraft emissions. However, during October-November 1997 over the NAFC, UT/LS NOx was dominated by surface emissions redistributed by convection and augmented by lightning.",
-            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) DC-8 In-Situ Meteorological and Navigation Data",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2662399958-LARC_ASDC",
-                    "description": "Earthdata Search for SONEX_MetNav_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for SONEX_MetNav_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2662399958-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_MetNav_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI for SONEX_MetNav_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for SONEX_MetNav_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_MetNav_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/MetNav_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SONEX_MetNav_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SONEX_MetNav_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/MetNav_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2662399958-LARC_ASDC",
+            "issued": "1997-10-07",
+            "keyword": [
+                "atmospheric pressure",
+                "altitude",
+                "spectral/engineering",
+                "platform characteristics",
+                "ocean temperature",
+                "oceans",
+                "infrared wavelengths",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmosphere"
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.89 -129.403 19.89 13.023 69.127 13.023 69.127 -129.403 19.89 -129.403</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1997-10-07T00:00:00Z/1997-11-13T23:59:59.999Z",
             "theme": [
                 "SONEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) DC-8 In-Situ Meteorological and Navigation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-RADWAV-3-RDR-GIACOBIN-ZIN-V1.0",
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
-                "international cometary explorer",
-                "giacobini-zinner"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The data are presented as the values of the density and temperature of the electrons measured (radio mapping) during the tail crossing of comet Giacobini-Zinner by ISEE-3/ICE as derived from spectroscopy of the thermal noise spectrum. The data was provided to the National Space Science Data Center (NASA/GSFC) by the Principal Investigator of the Radio Mapping Experiment on ISEE-3/ICE, Dr. Jean-Louis Steinberg of the Observatoire de Paris, Meudon, France cover the time interval 10:00 - 12:00 UT on September 11, 1985. The time resolution is 54 seconds.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-radwav-3-rdr-giacobin-zin-v1.0_iayc-7mwa",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international cometary explorer",
+                "giacobini-zinner"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-RADWAV-3-RDR-GIACOBIN-ZIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-radwav-3-rdr-giacobin-zin-v1.0_iayc-7mwa",
-            "description": "The data are presented as the values of the density and temperature of the electrons measured (radio mapping) during the tail crossing of comet Giacobini-Zinner by ISEE-3/ICE as derived from spectroscopy of the thermal noise spectrum. The data was provided to the National Space Science Data Center (NASA/GSFC) by the Principal Investigator of the Radio Mapping Experiment on ISEE-3/ICE, Dr. Jean-Louis Steinberg of the Observatoire de Paris, Meudon, France cover the time interval 10:00 - 12:00 UT on September 11, 1985. The time resolution is 54 seconds.",
-            "title": "ICE RADIO WAVE ELECTRON MAPPING DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ICE RADIO WAVE ELECTRON MAPPING DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/iazm-2zqa",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brent Holben",
+                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
+            },
+            "description": "The SDA dataset uses the spectral behavior of AOD to partition between fine and coarse modes, without a size-cutoff radius of the type used by the Dubovik and King [2000] inversion algorithm. The SDA data are derived from the direct-Sun observations rather than almucantar scans. Datasets are available at annual, monthly and daily accrurals.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aeronet.gsfc.nasa.gov/cgi-bin/bamgomas_interactive",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000127",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "earth science",
                 "clouds",
@@ -906921,45 +906933,35 @@
                 "precipitable water",
                 "radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brent Holben",
-                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/iazm-2zqa",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000127",
-            "description": "The SDA dataset uses the spectral behavior of AOD to partition between fine and coarse modes, without a size-cutoff radius of the type used by the Dubovik and King [2000] inversion algorithm. The SDA data are derived from the direct-Sun observations rather than almucantar scans. Datasets are available at annual, monthly and daily accrurals.",
-            "title": "AERONET-SDA Retrievals",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aeronet.gsfc.nasa.gov/cgi-bin/bamgomas_interactive",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "AERONET-SDA Retrievals"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-3-PLUTOCRUISE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Long Range Reconnaissance Imager                                       instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-3-plutocruise-v1.0_ib6q-2fg3",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "kerberos",
                 "136472 makemake",
@@ -906977,135 +906979,111 @@
                 "sun",
                 "uranus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-3-PLUTOCRUISE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-3-plutocruise-v1.0_ib6q-2fg3",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Long Range Reconnaissance Imager                                       instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      LORRI PLUTO CRUISE                                                      \n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      LORRI PLUTO CRUISE                                                      \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0220-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-18T23:34:55.000 to 2014-08-19T01:41:47.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0220-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0220-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0220-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-18T23:34:55.000 to 2014-08-19T01:41:47.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0220 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0220 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0686-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-01T06:42:05.000 to 2015-04-01T12:16:08.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0686-v1.0_ibbe-2z8x",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0686-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0686-v1.0_ibbe-2z8x",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-01T06:42:05.000 to 2015-04-01T12:16:08.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0686 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0686 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/hammer",
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
-                "tools",
-                "3d model",
-                "hammer",
-                "equipment"
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
-            "identifier": "NASA-356",
             "description": "Polygons: 38840 Vertices: 22394",
-            "title": "NASA 3D Models: Hammer",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -907113,21 +907091,54 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-356",
+            "issued": "2018-06-25",
+            "keyword": [
+                "tools",
+                "3d model",
+                "hammer",
+                "equipment"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/hammer",
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
+            "title": "NASA 3D Models: Hammer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ibfc-yy8j",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmapro-prov-v3-01_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000151",
             "issued": "2018-06-25",
-            "temporal": "2006-06-13/2011-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "cloud",
                 "climate",
@@ -907137,72 +907148,40 @@
                 "radiation",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/ibfc-yy8j",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000151",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 Aerosol Profile Data V3-01",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmapro-prov-v3-01_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2011-10-31",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 Aerosol Profile Data V3-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_daily_POD_att_quats_gal_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/GNSS/GDGPS_daily_POD_att_quats_gal_001.",
-            "issued": "1992-01-01",
-            "temporal": "2023-10-01T00:00:00Z/2024-11-18T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "keyword": [
-                "earth science",
-                "tectonics",
-                "solid earth",
-                "gravity/gravitational field",
-                "geodetics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-cddis@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDDIS"
-            },
-            "identifier": "C2768943631-CDDIS",
             "description": "This product contains a time series of attitude quaternion components for healthy satellites in the Galileo constellation that are accumulated every minute throughout the day. The product is generated at JPL's Global Differential GPS Operations Centers in real-time. The data in this product can be concatenated with other daily products to provide larger coverage in time.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD Attitude Quaternions (30-second sampling, 24-hour files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_POD_att_quats_gal_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_POD_att_quats_gal_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -907218,972 +907197,995 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2768943631-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "tectonics",
+                "solid earth",
+                "gravity/gravitational field",
+                "geodetics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_daily_POD_att_quats_gal_001",
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
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD Attitude Quaternions (30-second sampling, 24-hour files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TCSP/GOES-IM/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hood, Robbie E and Matthew  Smith.2007. TCSP GOES VISIBLE AND INFRARED IMAGES [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/TCSP/GOES-IM/DATA101",
-            "issued": "2007-03-21",
-            "temporal": "2005-07-01T00:15:00Z/2005-07-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "visible wavelengths",
-                "spectral/engineering",
-                "infrared wavelengths",
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
-            "identifier": "C1976770777-GHRC_DAAC",
             "description": "The TCSP GOES Visible and Infrared Images dataset was collected in support of the Tropical Cloud Systems and Processes (TCSP) mission, visible and infrared imagery from the Geostationary Operational Environmental Satellite 11 and 12 (GOES11, GOES 12) was collected and archived. Two channels were archived: channel 1-- visible (0.65 microns), and channel 2-- infrared (11 microns). Data files in McIDAS format as well as browse images were created. The TCSP mission collected data for research and documentation of cyclogenesis, the interaction of temperature, humidity, precipitation, wind and air pressure that creates ideal birthing conditions for tropical storms, hurricanes and related phenomena. The goal of this mission was to help us better understand how hurricanes and other tropical storms are formed and intensify.",
-            "graphic-preview-description": "N/A",
-            "title": "TCSP GOES VISIBLE AND INFRARED IMAGES V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/goes/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FGOES-IM%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FGOES-IM%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspgoes",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspgoes",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/goes/browse/ir4/TCSP_G11-200507062030.ir4.ara.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/goes/browse/ir4/TCSP_G11-200507062030.ir4.ara.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/goes/browse/vis/TCSP_G11-200507062030.vis.ara.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/goes/browse/vis/TCSP_G11-200507062030.vis.ara.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/tcsp/tcspgoes/tcspgoes_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/tcsp/tcspgoes/tcspgoes_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/goes/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/goes/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/goes/browse/",
+            "identifier": "C1976770777-GHRC_DAAC",
+            "issued": "2007-03-21",
+            "keyword": [
+                "visible wavelengths",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TCSP/GOES-IM/DATA101",
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
             "spatial": "-115.0 4.0 -62.0 32.0",
+            "temporal": "2005-07-01T00:15:00Z/2005-07-31T23:59:59Z",
             "theme": [
                 "TCSP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TCSP GOES VISIBLE AND INFRARED IMAGES V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0552-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-28T06:16:58.000 to 2015-01-28T11:06:24.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0552-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0552-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0552-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-28T06:16:58.000 to 2015-01-28T11:06:24.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0552 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0552 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1.",
-            "issued": "2022-01-07",
-            "temporal": "2008-03-18T00:00:00Z/2008-07-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-20",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alan Fried",
                 "hasEmail": "mailto:fried@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836775-LARC_ASDC",
             "description": "ARCTAS_TraceGas_AircraftInSitu_DC8_Data is the in-situ trace gas data collected by the DC-8 aircraft during the Arctic Research of the Composition of the Troposphere from Aircraft & Satellites (ARCTAS) mission. Data was collected by the Trace Organic Gas Analyzer (TOGA), Airborne Tropospheric Hydroxides Sensor (ATHOS), HOx Chemical Ionization Mass Spectrometer (HOxCIMS), Thermal Dissociation - Laser Induced Fluorescence (TD-LIF), Differential Absorption of CO, CH4, N2) Measurements (DACOM), Differential Absorption Lider (DIAL), Chemical Ionization Mass Spectrometer (CIMS), Non-dispersive Infrared Gas Analyzer (NDIR Gas Analyzer), NCAR NOxyO3, and the Proton Transfer Reaction Mass Spectrometer (PTR-MS). Data was also collected by gas chromatography and fluorescence spectroscopy. Data collection for this product is complete.\r\n\r\nThe Arctic is a critical region in understanding climate change. The responses of the Arctic to environmental perturbations such as warming, pollution, and emissions from forest fires in boreal Eurasia and North America include key processes such as the melting of ice sheets and permafrost, a decrease in snow albedo, and the deposition of halogen radical chemistry from sea salt aerosols to ice. ARCTAS was a field campaign that explored environmental processes related to the high degree of climate sensitivity in the Arctic. ARCTAS was part of NASA\u2019s contribution to the International Global Atmospheric Chemistry (IGAC) Polar Study using Aircraft, Remote Sensing, Surface Measurements, and Models of Climate, Chemistry, Aerosols, and Transport (POLARCAT) Experiment for the International Polar Year 2007-2008.\r\n\r\nARCTAS had four primary objectives. The first was to understand long-range transport of pollution to the Arctic. Pollution brought to the Arctic from northern mid-latitude continents has environmental consequences, such as modifying regional and global climate and affecting the ozone budget. Prior to ARCTAS, these pathways remained largely uncertain. The second objective was to understand the atmospheric composition and climate implications of boreal forest fires; the smoke emissions from which act as an atmospheric perturbation to the Arctic by impacting the radiation budget and cloud processes and contributing to the production of tropospheric ozone. The third objective was to understand aerosol radiative forcing from climate perturbations, as the Arctic is an important place for understanding radiative forcing due to the rapid pace of climate change in the region and its unique radiative environment. The fourth objective of ARCTAS was to understand chemical processes with a focus on ozone, aerosols, mercury, and halogens. Additionally, ARCTAS sought to develop capabilities for incorporating data from aircraft and satellites related to pollution and related environmental perturbations in the Arctic into earth science models, expanding the potential for those models to predict future environmental change.\r\n\r\nARCTAS consisted of two, three-week aircraft deployments conducted in April and July 2008. The spring deployment sought to explore arctic haze, stratosphere-troposphere exchange, and sunrise photochemistry. April was chosen for the deployment phase due to historically being the peak in the seasonal accumulation of pollution from northern mid-latitude continents in the Arctic. The summer deployment sought to understand boreal forest fires at their most active seasonal phase in addition to stratosphere-troposphere exchange and summertime photochemistry.\r\n\r\nDuring ARCTAS, three NASA aircrafts, the DC-8, P-3B, and BE-200, conducted measurements and were equipped with suites of in-situ and remote sensing instrumentation. Airborne data was used in conjunction with satellite observations from AURA, AQUA, CloudSat, PARASOL, CALIPSO, and MISR.\r\n\r\nThe ASDC houses ARCTAS aircraft data, along with data related to MISR, a satellite instrument aboard the Terra satellite which provides measurements that provide i",
-            "title": "ARCTAS DC-8 Aircraft In-situ Trace Gas Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/arctas",
-                    "description": "ESPO Home Page for ARCTAS",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for ARCTAS",
+                    "downloadURL": "https://espo.nasa.gov/arctas",
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
-                    "downloadURL": "https://www.nasa.gov/mission_pages/arctas/",
-                    "description": "ARCTAS Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ARCTAS Home Page",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/arctas/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/arctas/docs/arctas_wp.pdf",
-                    "description": "ARCTAS White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "ARCTAS White Paper",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/arctas/docs/arctas_wp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "description": "ASDC Home Page for MISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Home Page for MISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/cgi-bin/ic2008r",
-                    "description": "ARCTAS Final Data Comparison Results",
                     "@type": "dcat:Distribution",
+                    "description": "ARCTAS Final Data Comparison Results",
+                    "downloadURL": "https://www-air.larc.nasa.gov/cgi-bin/ic2008r",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acp.copernicus.org/articles/10/5191/2010/",
-                    "description": "ARCTAS Overview Paper",
                     "@type": "dcat:Distribution",
+                    "description": "ARCTAS Overview Paper",
+                    "downloadURL": "https://acp.copernicus.org/articles/10/5191/2010/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARCTAS/TraceGas_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARCTAS/TraceGas_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836775-LARC_ASDC",
-                    "description": "Earthdata Search Client for ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836775-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI for ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2569836775-LARC_ASDC",
+            "issued": "2022-01-07",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_TraceGas_AircraftInSitu_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-01-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>32.0 -180.0 32.0 180.0 90.0 180.0 90.0 -180.0 32.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2008-03-18T00:00:00Z/2008-07-14T23:59:59.999Z",
             "theme": [
                 "ARCTAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ARCTAS DC-8 Aircraft In-situ Trace Gas Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0498-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-21T00:26:00.000 to 2014-12-21T12:41:43.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0498-v1.0_ibq7-ga58",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0498-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0498-v1.0_ibq7-ga58",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-21T00:26:00.000 to 2014-12-21T12:41:43.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0498 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0498 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_VFM-Standard-V4-21",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_VFM-Standard-V4-21.",
-            "issued": "2018-09-06",
-            "temporal": "2020-07-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-09-06",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "clouds",
-                "earth science",
-                "lidar",
-                "spectral/engineering"
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
-            "identifier": "C1978624326-LARC_ASDC",
             "description": "CAL_LID_L2_VFM-Standard-V4-21 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) Lidar Level 2 Vertical Feature Mask (VFM), Version 4-21 data product. Data for this product was collected using the CALIPSO Cloud-Aerosol Lidar with Orthogonal Polarization (CALIOP) instrument. The version of this product was changed from 4-20 to 4-21 to account for a change in the operating system of the CALIPSO production cluster. Data collection for this product is ongoing.\r\n\r\nCALIPSO was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Lidar Level 2 Vertical Feature Mask (VFM), V4-21",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_VFM-Standard-V4-21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_VFM-Standard-V4-21",
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
-                    "description": "Data Quality Summary for the CALIPSO Version 4.20 and V4.21 Lidar Level 2 Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality Summary for the CALIPSO Version 4.20 and V4.21 Lidar Level 2 Data Products",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/faq.php",
-                    "description": "CALIPSO Data User\u2019s Guide - Frequently Asked Questions",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide - Frequently Asked Questions",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/faq.php",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/project_documentation.php",
-                    "description": "CALIPSO - List of project documentation (Data Products Catalog and ATBDs)",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of project documentation (Data Products Catalog and ATBDs)",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/project_documentation.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
-                    "description": "CALIPSO - List of publications",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of publications",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
-                    "description": "CALIPSO - Data Availability Site",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Availability Site",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://calipso.cnes.fr/fr",
-                    "description": "French (CNES) CALIPSO Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "French (CNES) CALIPSO Home Page",
+                    "downloadURL": "https://calipso.cnes.fr/fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_VFM-Standard-V4-21",
-                    "description": "DOI data set landing page for CAL_LID_L2_VFM-Standard-V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L2_VFM-Standard-V4-21",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_VFM-Standard-V4-21",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1978624326-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L2_VFM-Standard-V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L2_VFM-Standard-V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1978624326-LARC_ASDC",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
-                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
+                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
-                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
-                    "description": "CALIPSO Data User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
-                    "description": "CALIPSO Tilt Mode Geometry Anomaly Anomalies",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Tilt Mode Geometry Anomaly Anomalies",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.icare.univ-lille.fr",
-                    "description": "ICARE Data and Services Center Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Data and Services Center Home Page",
+                    "downloadURL": "https://www.icare.univ-lille.fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/ASDC_CALIPSO_Overview_2015.pdf",
-                    "description": "Overview of CALIPSO Data at the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of CALIPSO Data at the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/ASDC_CALIPSO_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://subset.larc.nasa.gov/calipso/",
-                    "description": "CALIPSO Search and Subsetting Web Application",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Search and Subsetting Web Application",
+                    "downloadURL": "https://subset.larc.nasa.gov/calipso/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
-                    "description": "Overview of CALIPSO Data Product Maturity",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of CALIPSO Data Product Maturity",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_release_summary_statement.html",
-                    "description": "CALIPSO Data Release Summary Statement",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data Release Summary Statement",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_release_summary_statement.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
-                    "description": "CALIPSO Products Overview",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Products Overview",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
-                    "description": "ICARE Programmers Toolbox",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Programmers Toolbox",
+                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_VFM-Standard-V4-21/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L2_VFM-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L2_VFM-Standard-V4-21_V4-21",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_VFM-Standard-V4-21/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_VFM-Standard-V4-21/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L2_VFM-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L2_VFM-Standard-V4-21_V4-21",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_VFM-Standard-V4-21/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1978624326-LARC_ASDC",
+            "issued": "2018-09-06",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "clouds",
+                "earth science",
+                "lidar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_VFM-Standard-V4-21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-09-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2020-07-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Lidar Level 2 Vertical Feature Mask (VFM), V4-21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-06-04 to 2014-06-18.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m04-v1.0_ibsv-27rz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m04-v1.0_ibsv-27rz",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-06-04 to 2014-06-18.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR DATA MTP 004",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR DATA MTP 004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/REPORTS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A.2016. GPM GROUND VALIDATION CAMPAIGN REPORTS IPHEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IPHEX/REPORTS/DATA101",
-            "issued": "2016-07-28",
-            "temporal": "2014-03-06T17:00:00Z/2014-06-16T23:59:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-12",
-            "keyword": [
-                "spectral/engineering",
-                "platform characteristics",
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
-            "identifier": "C1979623084-GHRC_DAAC",
             "description": "The Global Precipitation Measurement (GPM) Ground Validation Integrated Precipitation and Hydrology Experiment (IPHEx) campaign was centered in the Southern Appalachians and spanned into the Piedmont and Coastal Plain regions of North Carolina. The campaign sought to characterize warm season orographic precipitation regimes, and the relationship between precipitation regimes and hydrologic processes in regions of complex terrain. The GPM Ground Validation Mission Reports IPHEx dataset contains reports from the intense campaign period which occurred during May 1, 2014 to June 13, 2014. This dataset consists of various reports filed by the scientists during the campaign. This dataset includes flight reports, weather forecasts, GPM flight forecasts,  instrument reports, mission science reports, and plan-of-day reports. Many reports have additional information included as attachments.",
-            "title": "GPM GROUND VALIDATION CAMPAIGN REPORTS IPHEx V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FREPORTS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FREPORTS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=gpmmisrepiphx&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=gpmmisrepiphx&ghrccloud%2Fdata%2F=",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/reports/doc/gpmmisrepiphx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/reports/doc/gpmmisrepiphx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
+            "identifier": "C1979623084-GHRC_DAAC",
+            "issued": "2016-07-28",
+            "keyword": [
+                "spectral/engineering",
+                "platform characteristics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/REPORTS/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-83.09 35.08 -81.0 36.02",
+            "temporal": "2014-03-06T17:00:00Z/2014-06-16T23:59:00Z",
             "theme": [
                 "IPHEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION CAMPAIGN REPORTS IPHEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/633/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
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
-            "identifier": "DASHLINK_633",
             "description": "The following zip files contain individual flight recorded data in Matlab file format. There are 186 parameters each with a data structure that contains the following:\r\n\r\n<pre>\r\n-sensor recordings\r\n-sampling rate\r\n-units\r\n-parameter description\r\n-parameter ID\r\n</pre>",
-            "title": "Flight Data For Tail 655",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_1.zip",
-                    "description": "Tail 655 Set 1",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 655 Set 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_1.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_655_1.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_2.zip",
-                    "description": "Tail 655 Set 2",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 655 Set 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_2.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_655_2.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_3.zip",
-                    "description": "Tail 655 Set 3",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 655 Set 3",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_3.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_655_3.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_4.zip",
-                    "description": "Tail 655 Set 4",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 655 Set 4",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_4.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_655_4.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_5.zip",
-                    "description": "Tail 655 Set 5",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 655 Set 5",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_5.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_655_5.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_6.zip",
-                    "description": "Tail 655 Set 6",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 655 Set 6",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_6.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_655_6.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_7.zip",
-                    "description": "Tail_655 Set 7\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_655 Set 7\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_7.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_655_7.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_8.zip",
-                    "description": "Tail_655 Set 8\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_655 Set 8\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_655_8.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_655_8.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_633",
+            "issued": "2012-12-04",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/633/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Flight Data For Tail 655"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/6L166FFRPCPP",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs Greenland Monthly Image Mosaics from MODIS V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/6L166FFRPCPP.",
-            "issued": "2008-03-01",
-            "temporal": "2008-03-01T00:00:00Z/2016-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-30",
-            "keyword": [
-                "national geospatial data asset",
-                "climate indicators",
-                "cryosphere",
-                "cryospheric indicators",
-                "earth science",
-                "glaciers/ice sheets",
-                "ngda"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ted Scambos",
                 "hasEmail": "mailto:scambos@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1524053173-NSIDC_ECS",
             "description": "This data set, part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, consists of monthly image mosaics of the Greenland coastline and ice sheet periphery constructed from composited MODIS imagery.\n\nSee <a href=\"http://nsidc.org/data/measures/gimp\">Greenland Ice Mapping Project (GIMP)</a> for related data.",
-            "title": "MEaSUREs Greenland Monthly Image Mosaics from MODIS V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6L166FFRPCPP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6L166FFRPCPP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0724.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0724.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1524053173-NSIDC_ECS&q=NSIDC-0724&m=34.875%21-106.3828125%212%211%210%210%2C2&tl=1576074348%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1524053173-NSIDC_ECS&q=NSIDC-0724&m=34.875%21-106.3828125%212%211%210%210%2C2&tl=1576074348%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0724/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0724/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6L166FFRPCPP",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/6L166FFRPCPP",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6L166FFRPCPP",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/6L166FFRPCPP",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1524053173-NSIDC_ECS",
+            "issued": "2008-03-01",
+            "keyword": [
+                "national geospatial data asset",
+                "climate indicators",
+                "cryosphere",
+                "cryospheric indicators",
+                "earth science",
+                "glaciers/ice sheets",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/6L166FFRPCPP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-109.0 57.0 11.0 85.0",
+            "temporal": "2008-03-01T00:00:00Z/2016-09-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs Greenland Monthly Image Mosaics from MODIS V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/PVI/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wolff, David  and Larry  Bliven.2019. GPM Ground Validation Precipitation Video Imager (PVI) LPVEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/LPVEX/PVI/DATA101",
-            "issued": "2019-07-25",
-            "temporal": "2010-09-17T15:41:00Z/2011-05-11T09:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-25",
-            "keyword": [
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
-            "identifier": "C1979687446-GHRC_DAAC",
             "description": "The GPM Ground Validation Precipitation Video Imager (PVI) LPVEx dataset consists of precipitation particle images and drop size distribution (DSD) data collected by the Precipitation Video Imager (PVI) during the Global Precipitation Measurement (GPM) mission Light Precipitation Validation Experiment (LPVEx) field campaign. This field campaign took place around the Gulf of Finland in September and October of 2010. The goal of the campaign was to provide additional high-latitude, light rainfall measurements for the improvement of GPM satellite precipitation algorithms. The PVI instrument was designed by Dr. Larry Bliven at NASA Wallops Flight Facility. Data files are available from September 17, 2010 through May 11, 2011 in Excel format and contain the average, minimum, and logarithmic DSD bin sizes and number of particles per unit time. Browse images are available in BMP and JPG formats.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM Ground Validation Precipitation Video Imager (PVI) LPVEx V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/pvi/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FPVI%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FPVI%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmpvilpvex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmpvilpvex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/bmp",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/pvi/browse/Level_2/20100918/lpvex_pvi_20100918_snow_D_lin_I.bmp",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/pvi/browse/Level_2/20100918/lpvex_pvi_20100918_snow_D_lin_I.bmp",
+                    "mediaType": "image/bmp",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/LPVEX/DATA101",
-                    "description": "LPVEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "LPVEx Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/LPVEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/pvi/doc/gpmpvilpvex_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/pvi/doc/gpmpvilpvex_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2008JTECHA1148.1",
-                    "description": "Presenting the Snowflake Video Imager (SVI)",
                     "@type": "dcat:Distribution",
+                    "description": "Presenting the Snowflake Video Imager (SVI)",
+                    "downloadURL": "https://doi.org/10.1175/2008JTECHA1148.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/LPVEx",
-                    "description": "LPVEx Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "LPVEx Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/LPVEx",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/pvi/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/pvi/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/pvi/browse/",
+            "identifier": "C1979687446-GHRC_DAAC",
+            "issued": "2019-07-25",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/PVI/DATA101",
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
             "spatial": "104.99 39.99 105.01 40.01",
+            "temporal": "2010-09-17T15:41:00Z/2011-05-11T09:59:59Z",
             "theme": [
                 "LPVEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Precipitation Video Imager (PVI) LPVEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M13-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m13-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark",
                 "international rosetta mission",
@@ -908192,479 +908194,454 @@
                 "calibration",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M13-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m13-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSINAC 2 EDR MTP013 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSINAC 2 EDR MTP013 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/331",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kucharik, C.J., and J.M. Norman. 1998. BOREAS TE-06 Multiband Vegetation Imager Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/331",
-            "issued": "2023-11-22",
-            "temporal": "1994-07-26T00:00:00Z/1996-07-26T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "ecosystems",
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
-            "identifier": "C2808128688-ORNL_CLOUD",
             "description": "Describes the average data values derived from the multi-vegetation imager used by TE-06 during the BOREAS project.Describes the single point data values derived from the multi-vegetation imager used by TE-06 during the BOREAS project.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-06 Multiband Vegetation Imager Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F331",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F331",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te6mltvg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te6mltvg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE06_Multi_Veg_Imager.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE06_Multi_Veg_Imager.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/331",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/331",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/TE06_Multi_Veg_Imager.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/TE06_Multi_Veg_Imager.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/TE06_Multi_Veg_Imager.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/TE06_Multi_Veg_Imager.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/TE06_Multi_Veg_Imager.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/TE06_Multi_Veg_Imager.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/te13_boreas_canopy.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/te13_boreas_canopy.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/te13_boreas_site_loc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/te13_boreas_site_loc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/te6mltvg.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te6mltvg/comp/te6mltvg.def",
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
+            "identifier": "C2808128688-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "ecosystems",
+                "vegetation",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/331",
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
             "spatial": "-106.12 53.63 -98.62 55.84",
+            "temporal": "1994-07-26T00:00:00Z/1996-07-26T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-06 Multiband Vegetation Imager Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/FC3BVJ88Y8A2",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2IUNXLFO. Version 5.12.4. MERRA-2 instU_2d_lfo_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Land Surface Forcings V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/FC3BVJ88Y8A2. https://disc.gsfc.nasa.gov/datacollection/M2IUNXLFO_5.12.4.html. Digital Science Data.",
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
-                "atmospheric water vapor",
-                "earth science",
-                "atmospheric pressure",
-                "atmosphere",
-                "altitude",
-                "atmospheric winds",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812842-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2IUNXLFO (or  instU_2d_lfo_Nx) is an instantaneous 2-dimensional monthly diurnal means data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of land surface forcing parameters, such as height, specific humidity, wind, and air temperature of the model surface layer.  It consists of the monthly mean of the data fields on each hour starting from 00:00 UTC, e.g.:  00:00, 01:00, \u2026 , 23:00 UTC. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2IUNXLFO",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2IUNXLFO variable",
-            "title": "MERRA-2 instU_2d_lfo_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2IUNXLFO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNXLFO_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFC3BVJ88Y8A2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFC3BVJ88Y8A2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNXLFO_5.12.4.png",
-                    "description": "M2IUNXLFO variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2IUNXLFO variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNXLFO_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2IUNXLFO_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2IUNXLFO_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNXLFO.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNXLFO.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2IUNXLFO",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2IUNXLFO",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2IUNXLFO.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2IUNXLFO.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2IUNXLFO.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2IUNXLFO.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2IUNXLFO.5.12.4_Aggregation.ncml",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2IUNXLFO.5.12.4_Aggregation.ncml",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNXLFO.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNXLFO.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2IUNXLFO variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNXLFO_5.12.4.png",
+            "identifier": "C1276812842-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "atmospheric pressure",
+                "atmosphere",
+                "altitude",
+                "atmospheric winds",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/FC3BVJ88Y8A2",
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
+            "series-name": "M2IUNXLFO",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 instU_2d_lfo_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2IUNXLFO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494027-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "earth science",
-                "ocean optics",
-                "ecosystems",
-                "oceans",
-                "biosphere"
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
-            "identifier": "C2340494027-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Suomi-NPP VIIRS Global Binned Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L3B/IOP/2022",
-                    "description": "VIIRS-Suomi-NPP L3B Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3B Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L3B/IOP/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2340494027-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "ecosystems",
+                "oceans",
+                "biosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494027-OB_DAAC.html",
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
+            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suomi-NPP VIIRS Global Binned Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000562-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 1B2 terrain-projected Radiance parameters subset for the ARCTAS region;See ProductionDateTime for published date.",
-            "issued": "2015-09-24",
-            "temporal": "2008-04-02T00:00:00Z/2008-07-24T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-08-02",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
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
-            "identifier": "C1000000562-LARC",
             "description": "This file contains Terrain-projected TOA Radiance subset for the ARCTAS region,resampled at the surface and topographically corrected, as well as geometrically corrected by PGE22",
-            "title": "MISR L1B2 Terrain Product subset for the ARCTAS region V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000562-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000562-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1000000562-LARC",
+            "issued": "2015-09-24",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000562-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-08-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-157.0 54.0 -110.0 71.0",
+            "temporal": "2008-04-02T00:00:00Z/2008-07-24T23:59:59Z",
             "theme": [
                 "ARCTAS_2008",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR L1B2 Terrain Product subset for the ARCTAS region V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NC505NHFIHCY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "UW-Madison Space Science and Engineering Center: Hank Revercomb; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow. 2020-06-01. SNDRSNCrISL1BIMG. Version 2. S-NPP CrIS IMG: Collocated VIIRS level 1 / cloud mask statistical summary V2. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/NC505NHFIHCY. https://disc.gsfc.nasa.gov/datacollection/SNDRSNCrISL1BIMG_2.html. Digital Science Data.",
-            "issued": "2012-03-01",
-            "temporal": "2012-01-20T12:42:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-02",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "visible wavelengths",
-                "infrared wavelengths"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FENG DING",
                 "hasEmail": "mailto:Feng.Ding@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1943072252-GES_DISC",
-            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Normal Spectral Resolution (NSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Suomi National Polar-orbiting Partnership Project (SNPP). In December 2014, the CrIS instrument on the SNPP satellite doubled the spectral resolution of shortwave infrared data being transmitted to the ground.  In November 2015, additional points were included at the ends of the longwave and shortwave interferograms to improve the quality of the calibration.  Prior to November 2, 2015 the data are only available in Normal Spectral Resolution, after November 2, 2015 at 16:06 UTC, the data are available in both NSR and Full Spectral Resolution (FSR). \n\nThe NSR files have 1,317 channels: 163 shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 437 midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nThe Visible Infrared Imaging Radiometer Suite (VIIRS) has 22 imaging and radiometric bands covering wavelengths from 0.41 to 12.5 microns. It provides the sensor data records for clouds, sea surface temperature, ocean color, and others. This IMG product primarily contains statistics of the VIIRS cloud mask and VIIRS L1B data within each CrIS footprint..",
-            "release-place": "Greenbelt, MD",
-            "series-name": "SNDRSNCrISL1BIMG",
             "creator": "UW-Madison Space Science and Engineering Center: Hank Revercomb; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow",
-            "title": "S-NPP CrIS IMG: Collocated VIIRS level 1 / cloud mask statistical summary V2 (SNDRSNCrISL1BIMG) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNCrISL1BIMG_2.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Normal Spectral Resolution (NSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Suomi National Polar-orbiting Partnership Project (SNPP). In December 2014, the CrIS instrument on the SNPP satellite doubled the spectral resolution of shortwave infrared data being transmitted to the ground.  In November 2015, additional points were included at the ends of the longwave and shortwave interferograms to improve the quality of the calibration.  Prior to November 2, 2015 the data are only available in Normal Spectral Resolution, after November 2, 2015 at 16:06 UTC, the data are available in both NSR and Full Spectral Resolution (FSR). \n\nThe NSR files have 1,317 channels: 163 shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 437 midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nThe Visible Infrared Imaging Radiometer Suite (VIIRS) has 22 imaging and radiometric bands covering wavelengths from 0.41 to 12.5 microns. It provides the sensor data records for clouds, sea surface temperature, ocean color, and others. This IMG product primarily contains statistics of the VIIRS cloud mask and VIIRS L1B data within each CrIS footprint..",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNC505NHFIHCY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNC505NHFIHCY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -908674,399 +908651,424 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNCrISL1BIMG_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNCrISL1BIMG_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level1/SNDRSNCrISL1BIMG.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level1/SNDRSNCrISL1BIMG.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNCrISL1BIMG+002",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNCrISL1BIMG+002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level1/SNDRSNCrISL1BIMG.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level1/SNDRSNCrISL1BIMG.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/D0001-M01-S01-002_JPSS_ATBD_CrIS-SDR_C.pdf",
-                    "description": "Joint Polar Satellite System (JPSS) Cross-track Infrared Sounder (CrIS) Sensor Data Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) Cross-track Infrared Sounder (CrIS) Sensor Data Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/D0001-M01-S01-002_JPSS_ATBD_CrIS-SDR_C.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_L1B_SNPP.DeltaATBD_V2.0.pdf",
-                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_L1B_SNPP.DeltaATBD_V2.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_VIIRS_IMG_Product_Users_Guide_v2B.pdf",
-                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) IMG/IMG_COL Product Users\u2019 Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) IMG/IMG_COL Product Users\u2019 Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_VIIRS_IMG_Product_Users_Guide_v2B.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.5_ProductQuality/NASA_SNPP_CrIS_L1B_Quality_Flags_V2.0.pdf",
-                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.5_ProductQuality/NASA_SNPP_CrIS_L1B_Quality_Flags_V2.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNCrISL1BIMG_2.png",
+            "identifier": "C1943072252-GES_DISC",
+            "issued": "2012-03-01",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "visible wavelengths",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/NC505NHFIHCY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "SNDRSNCrISL1BIMG",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-20T12:42:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "S-NPP CrIS IMG: Collocated VIIRS level 1 / cloud mask statistical summary V2 (SNDRSNCrISL1BIMG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.torino.polarimetry&version=1.0",
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
-                "none",
-                "multiple asteroids"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains asteroid          polarimetric observations made during 1995-2005 with the Torino        photopolarimeter at the 2.15-m telescope at El Leoncito Observatory in Argentina.  These observations are reported in Cellino et al. (2005).",
+            "identifier": "urn:nasa:pds:gbo.ast.torino.polarimetry",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none",
+                "multiple asteroids"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.torino.polarimetry&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast.torino.polarimetry",
-            "description": "This data set contains asteroid          polarimetric observations made during 1995-2005 with the Torino        photopolarimeter at the 2.15-m telescope at El Leoncito Observatory in Argentina.  These observations are reported in Cellino et al. (2005).",
-            "title": "TORINO ASTEROID POLARIMETRY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TORINO ASTEROID POLARIMETRY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHMWI-4FR51",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Remote Sensing Systems. 2022-04-22. GHRSST Level 4 MW_IR_OI Global Foundation Sea Surface Temperature Analysis. Version 5.1. MW-IR optimum interpolated SST data set. Santa Rosa, CA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Remote Sensing Systems. https://doi.org/10.5067/GHMWI-4FR51. http://www.remss.com.",
-            "issued": "2017-09-30",
-            "temporal": "2002-06-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-09-30",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "earth science",
-                "national geospatial data asset",
-                "ngda"
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
-            "identifier": "C2205102254-POCLOUD",
-            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) global Level 4 sea surface temperature analysis produced daily on a 0.09-degree grid at Remote Sensing Systems. This product uses optimal interpolation (OI) from microwave (MW) sensors including the Tropical Rainfall Measuring Mission (TRMM) Microwave Imager (TMI), the NASA Advanced Microwave Scanning Radiometer-EOS (AMSR-E), the WindSat on the Coriolis satellite, the Global Precipitation Measurement (GPM) Microwave Imager (GMI), and the Advanced Microwave Scanning Radiometer 2 (AMSR2) onboard the GCOM-W1 satellite, as well as infrared (IR) sensors such as the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Aqua and Terra platforms and the Visible Infrared Imaging Radiometer Suite (VIIRS) on board the Suomi-NPP and NOAA-20 satellites. These MW sensors are used through the SST production based on the sensor data availability. The through-cloud capabilities of microwave radiometers provide a valuable picture of global sea surface temperature (SST) while infrared radiometers (i.e., MODIS) have a higher spatial resolution. This analysis does not use any in situ SST data such as drifting buoy SST. Compared with the previous version 5.0 dataset, version 5.1 is processed using updated input files, VIIRS on NOAA-20 is included, the sensor-specific error statistics (SSES) for each microwave sensor are updated, and deficiencies in the OI processing have been addressed.",
-            "release-place": "Santa Rosa, CA, USA",
-            "series-name": "GHRSST Level 4 MW_IR_OI Global Foundation Sea Surface Temperature Analysis",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Remote Sensing Systems",
-            "title": "GHRSST Level 4 MW_IR_OI Global Foundation Sea Surface Temperature analysis version 5.1 from REMSS",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MW_IR_OI-REMSS-L4-GLOB-v5.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) global Level 4 sea surface temperature analysis produced daily on a 0.09-degree grid at Remote Sensing Systems. This product uses optimal interpolation (OI) from microwave (MW) sensors including the Tropical Rainfall Measuring Mission (TRMM) Microwave Imager (TMI), the NASA Advanced Microwave Scanning Radiometer-EOS (AMSR-E), the WindSat on the Coriolis satellite, the Global Precipitation Measurement (GPM) Microwave Imager (GMI), and the Advanced Microwave Scanning Radiometer 2 (AMSR2) onboard the GCOM-W1 satellite, as well as infrared (IR) sensors such as the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Aqua and Terra platforms and the Visible Infrared Imaging Radiometer Suite (VIIRS) on board the Suomi-NPP and NOAA-20 satellites. These MW sensors are used through the SST production based on the sensor data availability. The through-cloud capabilities of microwave radiometers provide a valuable picture of global sea surface temperature (SST) while infrared radiometers (i.e., MODIS) have a higher spatial resolution. This analysis does not use any in situ SST data such as drifting buoy SST. Compared with the previous version 5.0 dataset, version 5.1 is processed using updated input files, VIIRS on NOAA-20 is included, the sensor-specific error statistics (SSES) for each microwave sensor are updated, and deficiencies in the OI processing have been addressed.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMWI-4FR51",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMWI-4FR51",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MW_IR_OI-REMSS-L4-GLOB-v5.1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MW_IR_OI-REMSS-L4-GLOB-v5.1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.ghrsst.org",
-                    "description": "GHRSST Project homepage",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project homepage",
+                    "downloadURL": "http://www.ghrsst.org",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/measurements/sea-surface-temperature/oisst-description",
-                    "description": "Microwave Infrared OI SST Product Description",
                     "@type": "dcat:Distribution",
+                    "description": "Microwave Infrared OI SST Product Description",
+                    "downloadURL": "http://www.remss.com/measurements/sea-surface-temperature/oisst-description",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "GHRSST Information",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Information",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205102254-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205102254-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205102254-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205102254-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MW_IR_OI-REMSS-L4-GLOB-v5.1.jpg",
+            "identifier": "C2205102254-POCLOUD",
+            "issued": "2017-09-30",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHMWI-4FR51",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Santa Rosa, CA, USA",
+            "series-name": "GHRSST Level 4 MW_IR_OI Global Foundation Sea Surface Temperature Analysis",
             "spatial": "-179.0 -90.0 180.0 90.0",
+            "temporal": "2002-06-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 4 MW_IR_OI Global Foundation Sea Surface Temperature analysis version 5.1 from REMSS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M08-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m08-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M08-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m08-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP008 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP008 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2010",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, R.S. Hipskind, R.K. Meentemeyer, and D.A. Shoemaker. 2022. MASTER: California Fire-Burn Area Emergency Response, California, August 2008. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2010",
-            "issued": "2023-06-29",
-            "temporal": "2008-08-20T22:31:19Z/2008-08-27T22:45:41Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "infrared wavelengths",
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
-            "identifier": "C2731702588-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during four flights aboard a DOE B200 aircraft over California, U.S., from 2008-08-20 to 2008-08-27. Objectives included mapping for  California Fire-Burn Area Emergency Response (BAER). This deployment was coordinated by the U.S. Department of Energy's Remote Sensing Laboratory (RSL) located at Nellis Air Force Base near Las Vegas, Nevada. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 10-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 1 as acquired on 24 August 2008 over Ammo fire location northwest of Oceanside, California, U.S. Source: MASTERL1B_0800508_01_20080824_2101_2102_V01.jpg",
-            "title": "MASTER: California Fire-Burn Area Emergency Response, California, August 2008",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2008_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2010",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2010",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_August_2008/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_August_2008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2008.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2008.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2010",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2010",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_August_2008/comp/MASTER_RSL_August_2008.pdf",
-                    "description": "MASTER: California Fire-Burn Area Emergency Response, California, August 2008: MASTER_RSL_August_2008.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: California Fire-Burn Area Emergency Response, California, August 2008: MASTER_RSL_August_2008.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_August_2008/comp/MASTER_RSL_August_2008.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2008_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 1 as acquired on 24 August 2008 over Ammo fire location northwest of Oceanside, California, U.S. Source: MASTERL1B_0800508_01_20080824_2101_2102_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 1 as acquired on 24 August 2008 over Ammo fire location northwest of Oceanside, California, U.S. Source: MASTERL1B_0800508_01_20080824_2101_2102_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2008_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 1 as acquired on 24 August 2008 over Ammo fire location northwest of Oceanside, California, U.S. Source: MASTERL1B_0800508_01_20080824_2101_2102_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2008_Fig1.jpg",
+            "identifier": "C2731702588-ORNL_CLOUD",
+            "issued": "2023-06-29",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2010",
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
             "spatial": "-122.57 32.54 -116.55 37.84",
+            "temporal": "2008-08-20T22:31:19Z/2008-08-27T22:45:41Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: California Fire-Burn Area Emergency Response, California, August 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFTAB-3-RDR-HALLEY-V2.0",
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
-                "international halley watch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains filter set parameters for all IR filters referenced in any of the data sets archived by the International Halley Watch (IHW) Infrared Studies Network (IRSN).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irftab-3-rdr-halley-v2.0_ic7i-cyfb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "calibration",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFTAB-3-RDR-HALLEY-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irftab-3-rdr-halley-v2.0_ic7i-cyfb",
-            "description": "This data set contains filter set parameters for all IR filters referenced in any of the data sets archived by the International Halley Watch (IHW) Infrared Studies Network (IRSN).",
-            "title": "IHW COMET HALLEY INFRARED FILTER SETS, V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY INFRARED FILTER SETS, V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-HIC-3-RDR-HIGHRES-COUNTRATE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set provides energetic (MeV) ion count rates and events measured by the Heavy Ion Counter (HIC) instrument on the Galileo spacecraft. These data are derived from high time resolution raw data that were recorded to tape and then played back later in the orbit. There are two basic types of data files associated with the full-rate reduced data: Detector Count Rates and Events (Pulse Heights).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-3-rdr-highres-countrate-v1.0_ic7k-bg8x",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "io",
                 "callisto",
@@ -909077,342 +909079,349 @@
                 "galileo",
                 "ganymede"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-HIC-3-RDR-HIGHRES-COUNTRATE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-3-rdr-highres-countrate-v1.0_ic7k-bg8x",
-            "description": "This data set provides energetic (MeV) ion count rates and events measured by the Heavy Ion Counter (HIC) instrument on the Galileo spacecraft. These data are derived from high time resolution raw data that were recorded to tape and then played back later in the orbit. There are two basic types of data files associated with the full-rate reduced data: Detector Count Rates and Events (Pulse Heights).",
-            "title": "GO JUP HIC HIGHRES ENERGETIC ION COUNT RATE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUP HIC HIGHRES ENERGETIC ION COUNT RATE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-DLRE-5-PRP-V1.0",
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
-                "lunar reconnaissance orbiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set consists of the Diviner Lunar Radiometer Experiment Polar Resource Products also known as PRPs.   The DLRE is a surface pushbroom mapper that  measures emitted thermal radiation and reflected solar radiation  from the surface of the moon. Two Diviner solar channels measure 0.3-3 micrometers reflected solar radiation.  Three Diviner channels near 8 micrometers classify regolith mineralogy by mapping the location of the Christiansen feature.  The remaining four Diviner channels measure surface temperature in four spectral bands ranging from 12.5 micrometers to beyond 200 micrometers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-dlre-5-prp-v1.0_icaz-7f4j",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "lunar reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-DLRE-5-PRP-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-dlre-5-prp-v1.0_icaz-7f4j",
-            "description": "This data set consists of the Diviner Lunar Radiometer Experiment Polar Resource Products also known as PRPs.   The DLRE is a surface pushbroom mapper that  measures emitted thermal radiation and reflected solar radiation  from the surface of the moon. Two Diviner solar channels measure 0.3-3 micrometers reflected solar radiation.  Three Diviner channels near 8 micrometers classify regolith mineralogy by mapping the location of the Christiansen feature.  The remaining four Diviner channels measure surface temperature in four spectral bands ranging from 12.5 micrometers to beyond 200 micrometers.",
-            "title": "LRO DLRE 5 POLAR RESOURCE PRODUCT",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LRO DLRE 5 POLAR RESOURCE PRODUCT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PDDQ8CUTFGJ5",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Soil Climate Analysis Network (SCAN): Oklahoma, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/PDDQ8CUTFGJ5.",
-            "issued": "2003-06-01",
-            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-31",
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric winds",
-                "earth science",
-                "precipitation",
-                "atmospheric water vapor",
-                "soils",
-                "agriculture"
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
-            "identifier": "C1386204211-NSIDCV0",
             "description": "This data set contains measurements taken during the Soil Moisture Experiment 2003 (SMEX03) from sensors at Soil Climate Analysis Network (SCAN) stations located in Fort Reno and Little Washita, OK, USA.",
-            "title": "SMEX03 Soil Climate Analysis Network (SCAN): Oklahoma, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPDDQ8CUTFGJ5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPDDQ8CUTFGJ5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ground_soil_moisture/SCAN/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ground_soil_moisture/SCAN/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ground_soil_moisture/SCAN/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ground_soil_moisture/SCAN/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PDDQ8CUTFGJ5",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/PDDQ8CUTFGJ5",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PDDQ8CUTFGJ5",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/PDDQ8CUTFGJ5",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204211-NSIDCV0",
+            "issued": "2003-06-01",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric winds",
+                "earth science",
+                "precipitation",
+                "atmospheric water vapor",
+                "soils",
+                "agriculture"
+            ],
+            "landingPage": "https://doi.org/10.5067/PDDQ8CUTFGJ5",
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
             "spatial": "-98.02 34.95 -97.98 35.55",
+            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Soil Climate Analysis Network (SCAN): Oklahoma, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-MIMI-2-LEMMS-UNCALIB-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Low Energy Magnetospheric Measurement System (LEMMS) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission.  The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values for each energy channel for the LEMMS sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data are presented in a set of tables which are of variable length and use a comma to separate various fields.  This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI LEMMS archive.  A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI LEMMS archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-lemms-uncalib-v1.1_icdp-7jhx",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "cassini-huygens",
                 "jupiter",
                 "saturn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-MIMI-2-LEMMS-UNCALIB-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-lemms-uncalib-v1.1_icdp-7jhx",
-            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Low Energy Magnetospheric Measurement System (LEMMS) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission.  The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values for each energy channel for the LEMMS sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data are presented in a set of tables which are of variable length and use a comma to separate various fields.  This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI LEMMS archive.  A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI LEMMS archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
-            "title": "CASSINI E/J/S/SW MIMI LEMMS SENSOR UNCALIBRATED DATA V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI E/J/S/SW MIMI LEMMS SENSOR UNCALIBRATED DATA V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-07-26. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1.",
-            "issued": "2021-08-17",
-            "temporal": "2013-01-12T00:00:00Z/2013-02-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-26",
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
-            "identifier": "C2404262882-LARC_ASDC",
             "description": "DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data contains remotely sensed data collected by the Airborne Compact Atmospheric Mapper (ACAM) onboard NASA's B-200 aircraft during the California (San Joaquin Valley) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the California deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ California Deployment B-200 Aircraft Remotely Sensed Airborne Compact Atmospheric Mapper Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
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
-                    "downloadURL": "https://www.spiedigitallibrary.org/conference-proceedings-of-spie/7452/74520Q/Remote-sensing-capabilities-of-the-Airborne-Compact-Atmospheric-Mapper/10.1117/12.827035.full?SSO=1",
-                    "description": "ACAM Overview Paper",
                     "@type": "dcat:Distribution",
+                    "description": "ACAM Overview Paper",
+                    "downloadURL": "https://www.spiedigitallibrary.org/conference-proceedings-of-spie/7452/74520Q/Remote-sensing-capabilities-of-the-Airborne-Compact-Atmospheric-Mapper/10.1117/12.827035.full?SSO=1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
-                    "description": "DOI for DISCOVERAQ_CALIFORNIA_AIRCRAFTREMOTESENSING_B200_ACAM_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_CALIFORNIA_AIRCRAFTREMOTESENSING_B200_ACAM_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2404262882-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_CALIFORNIA_AIRCRAFTREMOTESENSING_B200_ACAM_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_CALIFORNIA_AIRCRAFTREMOTESENSING_B200_ACAM_DATA_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2404262882-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_AircraftRemoteSensing_B200_ACAM_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_AircraftRemoteSensing_B200_ACAM_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/California_AircraftRemoteSensing_B200_ACAM_Data_1/contents.html",
-                    "description": "OPeNDAP data access for DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/California_AircraftRemoteSensing_B200_ACAM_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2404262882-LARC_ASDC",
+            "issued": "2021-08-17",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_ACAM_Data_1",
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
+            "temporal": "2013-01-12T00:00:00Z/2013-02-10T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ California Deployment B-200 Aircraft Remotely Sensed Airborne Compact Atmospheric Mapper Data"
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
+            "description": "CFD Validation of Synthetic Jets and Turbulent Separation Control. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://cfdval2004.larc.nasa.gov/Presentations/Seattle_08_flowcontrol.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-848__13",
+            "issued": "2018-06-25",
             "keyword": [
                 "experiment",
                 "synthetic",
@@ -909423,589 +909432,556 @@
                 "separation",
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
-            "identifier": "NASA-848__13",
-            "description": "CFD Validation of Synthetic Jets and Turbulent Separation Control. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: CFD Validation of Synthetic Jets and Turbulent Separation Control",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://cfdval2004.larc.nasa.gov/Presentations/Seattle_08_flowcontrol.pdf",
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
+            "title": "Turbulence Models: Data from Other Experiments: CFD Validation of Synthetic Jets and Turbulent Separation Control"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MK0BQ0W0O973",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Alabama, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MK0BQ0W0O973.",
-            "issued": "2003-06-25",
-            "temporal": "2003-06-25T00:00:00Z/2003-07-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-17",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "microwave"
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
-            "identifier": "C1386204277-NSIDCV0",
             "description": "The Polarimetric Scanning Radiometer (PSR) is an airborne microwave imaging radiometer developed and operated by the National Oceanic and Atmospheric Administration (NOAA) Environmental Technology Laboratory. This data set includes brightness temperature data for the C-band and X-band.",
-            "title": "SMEX03 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Alabama, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMK0BQ0W0O973",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMK0BQ0W0O973",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/aircraft_remote_sensing/PSR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/aircraft_remote_sensing/PSR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/aircraft_remote_sensing/PSR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/aircraft_remote_sensing/PSR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MK0BQ0W0O973",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MK0BQ0W0O973",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MK0BQ0W0O973",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MK0BQ0W0O973",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204277-NSIDCV0",
+            "issued": "2003-06-25",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/MK0BQ0W0O973",
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
             "spatial": "-87.09 34.66 -85.77 35.19",
+            "temporal": "2003-06-25T00:00:00Z/2003-07-17T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Alabama, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0479-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-07T20:57:05.000 to 2014-12-08T00:37:09.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0479-v1.0_icgt-8z4q",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0479-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0479-v1.0_icgt-8z4q",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-07T20:57:05.000 to 2014-12-08T00:37:09.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0479 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0479 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CO2LN.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2CO2LN.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-08-01T00:00:00Z/2015-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "air quality",
-                "atmospheric chemistry",
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
-            "identifier": "C1607585871-LARC",
             "description": "TL2CO2LN_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Carbon Dioxide Lite Nadir Version 7 data product. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) are also provided. L2 modeled spectra are evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compares observed spectra to the modeled spectra and iteratively updates the atmospheric parameters. L2 standard product files include information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consists of a maximum of 16 consecutive orbits.\r\rA Nadir sequence within the TES Global Survey is a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations currently only use a single set of filter mix.\r\rA Global Survey consists of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals are performed. Each observation is the input for retrievals of species Volume Mixing Ratios (VMR), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density and other diagnostic quantities. Each TES Level 2 standard product reports information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object is bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product can have a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals are not reported.\r\rThe organization of data within the Swath object is based on a superset of the UARS pressure levels used to report concentrations of trace atmospheric gases. The reporting grid is the same pressure grid used for modeling. There are 67 reporting levels from 1211.53 hPa, which allows for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products will report values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files each observation can potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels are not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresponding to altitudes below the cloud top or surface, where measurements were not possible, a fill value will be applied. \r\rTo minimize the duplication of information between the individual species standard products, data fields common to each species (such as spacecraft coordinates, emissivities, and other data fields) have been collected into a separate standard product, termed the TES L2 Ancillary Data product (ESDT short name: TL2ANC). Users of this product should also obtain the Ancillary Data product.",
-            "title": "TES/Aura L2 Carbon Dioxide Lite Nadir V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CO2LN.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CO2LN.007",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_2_std.pdf",
-                    "description": "TES Level 2 Versioning - Level 2 Standard and Special Observation Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 2 Versioning - Level 2 Standard and Special Observation Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_2_std.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Lite_Products_Users_Guide.pdf",
-                    "description": "AVDC TES Lite products user\u2019s guide",
                     "@type": "dcat:Distribution",
+                    "description": "AVDC TES Lite products user\u2019s guide",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Lite_Products_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
-                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CO2LN.007",
-                    "description": "DOI data set landing page for TL2CO2LN_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2CO2LN_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CO2LN.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CO2LN.007/contents.html",
-                    "description": "OPeNDAP data access for TL2CO2LN_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2CO2LN_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CO2LN.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1607585871-LARC",
-                    "description": "Earthdata Search for TL2CO2LN_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2CO2LN_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1607585871-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CO2LN.007/",
-                    "description": "ASDC Direct Data Download for TL2CO2LN_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2CO2LN_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CO2LN.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
```

