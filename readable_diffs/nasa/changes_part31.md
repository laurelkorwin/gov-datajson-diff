# Change History for nasa.json (Part 31)

### Changes from 31606f9 to dd2190f (Part 20/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mahli-4-rdr-img-v1.0_5m4b-vzbw",
-            "description": "NULL",
-            "title": "MSL MARS HAND LENS IMAGER 4\n                                      RDR IMAGE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS HAND LENS IMAGER 4\n                                      RDR IMAGE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5ZS2TFT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MASAM2: Daily 4 km Arctic Sea Ice Concentration, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5ZS2TFT.",
-            "issued": "2012-07-03",
-            "temporal": "2012-07-03T00:00:00Z/2024-07-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-06",
-            "keyword": [
-                "cryosphere",
-                "sea ice",
-                "earth science"
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
-            "identifier": "C1386246292-NSIDCV0",
             "description": "The MASIE-AMSR2 (MASAM2) daily 4 km sea ice concentration is a prototype concentration product that is a blend of two other daily sea ice data products: ice coverage from the Multisensor Analyzed Sea Ice Extent (MASIE) product at a 4 km grid cell size and ice concentration from the Advanced Microwave Scanning Radiometer 2 (AMSR2) at a 10 km grid cell size. MASAM2 was developed to meet a need for greater accuracy and higher resolution in ice concentration fields that are used to initialize an operational sea ice forecast model. By applying some simple rules to blend the two sources, a 4 km concentration product is produced that can be used in the model.  This prototype covers July 2012 to present.",
-            "title": "MASAM2: Daily 4 km Arctic Sea Ice Concentration, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5ZS2TFT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5ZS2TFT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G10005/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G10005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G10005/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G10005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5ZS2TFT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5ZS2TFT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5ZS2TFT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5ZS2TFT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246292-NSIDCV0",
+            "issued": "2012-07-03",
+            "keyword": [
+                "cryosphere",
+                "sea ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5ZS2TFT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 29.08 180.0 90.0",
+            "temporal": "2012-07-03T00:00:00Z/2024-07-08T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASAM2: Daily 4 km Arctic Sea Ice Concentration, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SMP50-3SPCS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Remote Sensing Systems (RSS). 2022-02-25. RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean Validated Dataset. Version 5.0. SMAP Sea Surface Salinity Products. Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Remote Sensing Systems (RSS). https://doi.org/10.5067/SMP50-3SPCS. http://podaac.jpl.nasa.gov/smap. Remote Sensing Systems (RSS), Remote Sensing Systems (RSS), 2022-02-25, RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.0 Validated Dataset, http://podaac.jpl.nasa.gov/smap.",
-            "issued": "2021-01-13",
-            "temporal": "2015-03-27T12:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-13",
-            "keyword": [
-                "earth science",
-                "oceans",
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
-            "identifier": "C2208425700-POCLOUD",
-            "description": "The version 5.0 SMAP-SSS level 3, 8-Day running mean gridded product is based on the fifth release of the validated standard mapped sea surface salinity (SSS) data from the NASA Soil Moisture Active Passive (SMAP) observatory, produced operationally by Remote Sensing Systems (RSS). The major changes in Version 5.0 from Version 4 are: (1) the addition of formal uncertainty estimates to all salinity retrieval products. (2) Sea-ice flagging and sea-ice side-lobe correction based on direct ingestion of AMSR-2 brightness temperature (TB) measurements. This is in contrast to Version 4 and earlier versions in which the sea-ice correction was based on an external sea-ice concentration product. The use of AMSR-2 TB measurements in the SMAP Version 5 products allows for salinity retrievals closer to the sea-ice edge and aids in the detection of large icebergs near the Antarctic. Daily data files for this product are based on SSS averages spanning an 8-day moving time window.  SMAP data begins on April 1,2015 and is ongoing. L3 products are global in extent with a default spatial resolution of approximately 70KM. The datasets are gridded at 0.25degree x 0.25degree. Note that while a SSS 40KM variable is also included in the product, for most open ocean applications, the  default SSS variable (70KM) is best used as they are significantly less noisy than the 40KM data.  The SMAP satellite is in a near-polar orbit at an inclination of 98 degrees and an altitude of 685 km. It has an ascending node time of 6 pm and is sun-synchronous. With its 1000km swath, SMAP achieves global coverage in approximately 3 days, but has an exact orbit repeat cycle of 8 days.  On board instruments include a highly sensitive L-band radiometer operating at 1.41GHz and an L-band 1.26GHz radar sensor providing complementary active and passive sensing capabilities.  Malfunction of the SMAP scatterometer on 7 July, 2015, has necessitated the use of collocated wind speed, primarily from WindSat, for the surface roughness correction required for the surface salinity retrieval.",
-            "release-place": "Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA",
-            "series-name": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean Validated Dataset",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Remote Sensing Systems (RSS)",
-            "title": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.0 Validated Dataset",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The version 5.0 SMAP-SSS level 3, 8-Day running mean gridded product is based on the fifth release of the validated standard mapped sea surface salinity (SSS) data from the NASA Soil Moisture Active Passive (SMAP) observatory, produced operationally by Remote Sensing Systems (RSS). The major changes in Version 5.0 from Version 4 are: (1) the addition of formal uncertainty estimates to all salinity retrieval products. (2) Sea-ice flagging and sea-ice side-lobe correction based on direct ingestion of AMSR-2 brightness temperature (TB) measurements. This is in contrast to Version 4 and earlier versions in which the sea-ice correction was based on an external sea-ice concentration product. The use of AMSR-2 TB measurements in the SMAP Version 5 products allows for salinity retrievals closer to the sea-ice edge and aids in the detection of large icebergs near the Antarctic. Daily data files for this product are based on SSS averages spanning an 8-day moving time window.  SMAP data begins on April 1,2015 and is ongoing. L3 products are global in extent with a default spatial resolution of approximately 70KM. The datasets are gridded at 0.25degree x 0.25degree. Note that while a SSS 40KM variable is also included in the product, for most open ocean applications, the  default SSS variable (70KM) is best used as they are significantly less noisy than the 40KM data.  The SMAP satellite is in a near-polar orbit at an inclination of 98 degrees and an altitude of 685 km. It has an ascending node time of 6 pm and is sun-synchronous. With its 1000km swath, SMAP achieves global coverage in approximately 3 days, but has an exact orbit repeat cycle of 8 days.  On board instruments include a highly sensitive L-band radiometer operating at 1.41GHz and an L-band 1.26GHz radar sensor providing complementary active and passive sensing capabilities.  Malfunction of the SMAP scatterometer on 7 July, 2015, has necessitated the use of collocated wind speed, primarily from WindSat, for the surface roughness correction required for the surface salinity retrieval.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP50-3SPCS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP50-3SPCS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V5/SMAP_NASA_RSS_Salinity_Release_V5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V5/SMAP_NASA_RSS_Salinity_Release_V5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/missions/smap",
-                    "description": "Remote Sensing Systems SMAP Sea Surface Salinity Website",
                     "@type": "dcat:Distribution",
+                    "description": "Remote Sensing Systems SMAP Sea Surface Salinity Website",
+                    "downloadURL": "http://www.remss.com/missions/smap",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/L3/RSS/README.txt",
-                    "description": "Know issues README",
                     "@type": "dcat:Distribution",
+                    "description": "Know issues README",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/L3/RSS/README.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/smap",
-                    "description": "SMAP-SSS Project and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "SMAP-SSS Project and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/smap",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_ancillaries.txt",
-                    "description": "Dynamically updated RSS webpage listing L2 files with missing ancillary inputs",
                     "@type": "dcat:Distribution",
+                    "description": "Dynamically updated RSS webpage listing L2 files with missing ancillary inputs",
+                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_ancillaries.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_orbits.txt",
-                    "description": "Dynamically updated RSS webpage listing L2 files with Bad Orbits",
                     "@type": "dcat:Distribution",
+                    "description": "Dynamically updated RSS webpage listing L2 files with Bad Orbits",
+                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_orbits.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V5/SMAP_NASA_RSS_Salinity_Release_V5.0.pdf",
-                    "description": "SMAP-SSS V5.0 Technical Guide (ATBD, Validation Analysis, Product Format Specification)",
                     "@type": "dcat:Distribution",
+                    "description": "SMAP-SSS V5.0 Technical Guide (ATBD, Validation Analysis, Product Format Specification)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V5/SMAP_NASA_RSS_Salinity_Release_V5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/README.KnownIssues.txt",
-                    "description": "Information on Data Outages & Known Issues",
                     "@type": "dcat:Distribution",
+                    "description": "Information on Data Outages & Known Issues",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/README.KnownIssues.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2208425700-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2208425700-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2208425700-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2208425700-POCLOUD",
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
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Data Subscriber",
                     "downloadURL": "https://github.com/podaac/data-subscriber",
-                    "mediaType": "text/html",
-                    "description": "Data Subscriber"
+                    "mediaType": "text/html"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V5.jpg",
+            "identifier": "C2208425700-POCLOUD",
+            "issued": "2021-01-13",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMP50-3SPCS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-01-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA",
+            "series-name": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean Validated Dataset",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-03-27T12:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "SMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.0 Validated Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-L-MMTO_CLIO-3-CDR-LCROSS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This archive contains calibrated observations of the 2009-10-09 impact of the LCROSS spacecraft on the moon by the CLIO instrument on the MMT Observatory 6.5m telescope. The archive consists of calibrated FITS images of the event. This is one of several data sets of Earth-based observations of the impact.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-l-mmto_clio-3-cdr-lcross-v1.0_5mat-xifq",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "bias",
@@ -198821,278 +198823,252 @@
                 "lunar crater observation and sensing satellite",
                 "sky"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-L-MMTO_CLIO-3-CDR-LCROSS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-l-mmto_clio-3-cdr-lcross-v1.0_5mat-xifq",
-            "description": "This archive contains calibrated observations of the 2009-10-09 impact of the LCROSS spacecraft on the moon by the CLIO instrument on the MMT Observatory 6.5m telescope. The archive consists of calibrated FITS images of the event. This is one of several data sets of Earth-based observations of the impact.",
-            "title": "MMT OBSERVATORY 6.5M CLIO CALIBRATED OBSERVATIONS OF LCROSS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MMT OBSERVATORY 6.5M CLIO CALIBRATED OBSERVATIONS OF LCROSS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/192/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Indir Jaganjac",
+                "hasEmail": "mailto:ijaganjac@yahoo.com"
+            },
+            "description": "Universal log-periodic correction to renormalization group scaling for rupture stress prediction from acoustic emissions.",
+            "identifier": "DASHLINK_192",
             "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "nasa",
                 "dashlink",
                 "ames"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Indir Jaganjac",
-                "hasEmail": "mailto:ijaganjac@yahoo.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/192/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_192",
-            "description": "Universal log-periodic correction to renormalization group scaling for rupture stress prediction from acoustic emissions.",
-            "title": "IJ",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "IJ"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-4-AST1-STEINS-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the STEINS FLY-BY mission phase, covering the period  from 2008-08-04T00:00:00.000 to 2008-10-05T23:59:59.000. The prime target is asteroid 2867 Steins. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-4-ast1-steins-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "2867 steins"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-4-AST1-STEINS-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-4-ast1-steins-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the STEINS FLY-BY mission phase, covering the period  from 2008-08-04T00:00:00.000 to 2008-10-05T23:59:59.000. The prime target is asteroid 2867 Steins. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER STEINS OSIWAC 4 AST1 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER STEINS OSIWAC 4 AST1 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07-V2.0",
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
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. This version V2.0 supersedes previous deliveries of the same dataset. Note that the two datasets RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07-V1.0 and RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07B-V1.0 have been merged into one dataset: RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m07-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m07-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. This version V2.0 supersedes previous deliveries of the same dataset. Note that the two datasets RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07-V1.0 and RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07B-V1.0 have been merged into one dataset: RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
-            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 3 RDR MTP007 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 3 RDR MTP007 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-RPCMIP-3-CVP1-V1.0",
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
+            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the COMMISSIONING 1 mission phase. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-rpcmip-3-cvp1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-RPCMIP-3-CVP1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-rpcmip-3-cvp1-v1.0",
-            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the COMMISSIONING 1 mission phase. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER CAL RPCMIP 3 CVP1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL RPCMIP 3 CVP1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-MDIS-5-RDR-MDR-V1.0",
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
+            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes the Multispectral Reduced Data Records for the WAC. The Map Projected Multispectral RDR (MDR) data set consists of a global color map of I/F in the 8 filters used for multispectral mapping during the primary mission, photometrically normalized to a solar incidence angle (i) = 30 degrees, emission angle (e) = 0 degrees, and phase angle (g) = 30 degrees at a spatial sampling of 64 pixels per degree. The map is divided into 54 segments or 'tiles', each representing the NW, NE, SW, or SE quadrant of one of the 13 non-polar or one of the 2 polar quadrangles or 'Mercury charts' already defined by the USGS. Each tile is composed of 8 bands corresponding to 8 of the 11 WAC filters. Each tile also contains backplanes describing ancillary information. The subset of 8 of 11 available multispectral filters was selected on account of limitations in MESSENGER solid-state recorder space, and more or less evenly samples the spectral range of MDIS.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-mdis-5-rdr-mdr-v1.0_5mff-xeem",
+            "issued": "2018-06-26",
+            "keyword": [
+                "messenger",
+                "mercury"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-MDIS-5-RDR-MDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-mdis-5-rdr-mdr-v1.0_5mff-xeem",
-            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes the Multispectral Reduced Data Records for the WAC. The Map Projected Multispectral RDR (MDR) data set consists of a global color map of I/F in the 8 filters used for multispectral mapping during the primary mission, photometrically normalized to a solar incidence angle (i) = 30 degrees, emission angle (e) = 0 degrees, and phase angle (g) = 30 degrees at a spatial sampling of 64 pixels per degree. The map is divided into 54 segments or 'tiles', each representing the NW, NE, SW, or SE quadrant of one of the 13 non-polar or one of the 2 polar quadrangles or 'Mercury charts' already defined by the USGS. Each tile is composed of 8 bands corresponding to 8 of the 11 WAC filters. Each tile also contains backplanes describing ancillary information. The subset of 8 of 11 available multispectral filters was selected on account of limitations in MESSENGER solid-state recorder space, and more or less evenly samples the spectral range of MDIS.",
-            "title": "MESSENGER MDIS MAP PROJECTED MULTISPECTRAL RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER MDIS MAP PROJECTED MULTISPECTRAL RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC4-MTP023-V1.0",
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
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase 4 from 17th Nov 2015 to 15th Dec 2015 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc4-mtp023-v1.0_5mg7-am8j",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC4-MTP023-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc4-mtp023-v1.0_5mg7-am8j",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase 4 from 17th Nov 2015 to 15th Dec 2015 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 4 MTP023 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 4 MTP023 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-07-01",
-            "temporal": "2021-07-01T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "trajectory",
-                "iss",
-                "international",
-                "ephemeris",
-                "coords",
-                "coordinates",
-                "space",
-                "location",
-                "station",
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
-            "identifier": "nasa-iss-data_2021-07-01_5mhk-q3y6",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-07-01",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -199215,841 +199191,874 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-07-01_5mhk-q3y6",
+            "issued": "2021-07-01",
+            "keyword": [
+                "trajectory",
+                "iss",
+                "international",
+                "ephemeris",
+                "coords",
+                "coordinates",
+                "space",
+                "location",
+                "station",
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
+            "temporal": "2021-07-01T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-07-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3314-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-02T04:48:39.000 to 2012-08-02T07:17:04.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3314-v1.0_5mhs-4gwe",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3314-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3314-v1.0_5mhs-4gwe",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-02T04:48:39.000 to 2012-08-02T07:17:04.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3314 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3314 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/10.7927/g2n9-ca10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Di, Q., Y. Wei, A. Shtein, X. Xing, E. Castro, H. Amini, C. Hultquist, L. Shi, I. Kloog, R. Silvern, J. Kelly, M. B. Sabath, C. Choirat, P. Koutrakis, A. Lyapustin, Y. Wang, L. J. Mickley, Y. Daouk, and J. Schwartz. 2024-01-30. Daily and Annual PM2.5 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016). Version 1.10. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/10.7927/g2n9-ca10. https://doi.org/10.7927/g2n9-ca10.",
-            "issued": "2024-01-30",
-            "temporal": "2000-01-01T00:00:00Z/2016-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-30",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "air quality",
-                "atmosphere"
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
-            "identifier": "C2848642054-SEDAC",
-            "description": "The Daily and Annual PM2.5 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016) data set includes predictions of PM2.5 concentration in grid cells at a resolution of 1-km for the years 2000-2016. A generalized additive model was used that accounted for geographic difference to ensemble daily predictions of three machine learning models: neural network, random forest, and gradient boosting. The three machine learners incorporated multiple predictors, including satellite data, meteorological variables, land-use variables, elevation, chemical transport model predictions, several reanalysis data sets, and others. The annual predictions were calculated by averaging the daily predictions for each year in each grid cell. The ensembled model demonstrated better predictive performance than the individual machine learners with 10-fold cross-validated R-squared values of 0.86 for daily predictions and 0.89 for annual predictions. In version 1.10, the completeness of daily PM2.5 predictions have been enhanced by employing linear interpolation to impute missing values. Specifically, for days with small spatial patches of missing data with less than 100 grid cells, inverse distance weighting interpolation was used to fill the missing grid cells. Other missing daily PM2.5 predictions were interpolated from the nearest days with available data. Annual predictions were updated by averaging the imputed daily predictions for each year in each grid cell. These daily and annual PM2.5 predictions allow public health researchers to respectively estimate the short- and long-term effects of PM2.5 exposures on human health, supporting the U.S. Environmental Protection Agency (EPA) for the revision of the National Ambient Air Quality Standards for 24-hour average and annual average concentrations of PM2.5. The data are available in RDS and GeoTIFF formats for statistical research and geospatial analysis.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Di, Q., Y. Wei, A. Shtein, X. Xing, E. Castro, H. Amini, C. Hultquist, L. Shi, I. Kloog, R. Silvern, J. Kelly, M. B. Sabath, C. Choirat, P. Koutrakis, A. Lyapustin, Y. Wang, L. J. Mickley, Y. Daouk, and J. Schwartz",
-            "title": "Daily and Annual PM2.5 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Daily and Annual PM2.5 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016) data set includes predictions of PM2.5 concentration in grid cells at a resolution of 1-km for the years 2000-2016. A generalized additive model was used that accounted for geographic difference to ensemble daily predictions of three machine learning models: neural network, random forest, and gradient boosting. The three machine learners incorporated multiple predictors, including satellite data, meteorological variables, land-use variables, elevation, chemical transport model predictions, several reanalysis data sets, and others. The annual predictions were calculated by averaging the daily predictions for each year in each grid cell. The ensembled model demonstrated better predictive performance than the individual machine learners with 10-fold cross-validated R-squared values of 0.86 for daily predictions and 0.89 for annual predictions. In version 1.10, the completeness of daily PM2.5 predictions have been enhanced by employing linear interpolation to impute missing values. Specifically, for days with small spatial patches of missing data with less than 100 grid cells, inverse distance weighting interpolation was used to fill the missing grid cells. Other missing daily PM2.5 predictions were interpolated from the nearest days with available data. Annual predictions were updated by averaging the imputed daily predictions for each year in each grid cell. These daily and annual PM2.5 predictions allow public health researchers to respectively estimate the short- and long-term effects of PM2.5 exposures on human health, supporting the U.S. Environmental Protection Agency (EPA) for the revision of the National Ambient Air Quality Standards for 24-hour average and annual average concentrations of PM2.5. The data are available in RDS and GeoTIFF formats for statistical research and geospatial analysis.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2Fg2n9-ca10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2Fg2n9-ca10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-pm2-5-concentrations-contiguous-us-1-km-v1-10-2000-2016/sedac-logo.jpg",
+            "identifier": "C2848642054-SEDAC",
+            "issued": "2024-01-30",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.7927/10.7927/g2n9-ca10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 17.0 -65.0 72.0",
+            "temporal": "2000-01-01T00:00:00Z/2016-12-31T00:00:00Z",
             "theme": [
                 "AQDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Daily and Annual PM2.5 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RELPCEXB0MY3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge LVIS-GH L2 Geolocated Surface Elevation Product V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/RELPCEXB0MY3.",
-            "issued": "2013-10-30",
-            "temporal": "2013-10-26T00:00:00Z/2013-11-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-14",
-            "keyword": [
-                "land surface",
-                "topography",
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
-            "identifier": "C1000000780-NSIDC_ECS",
             "description": "This data set contains surface elevation data measured by the NASA Land, Vegetation, and Ice Sensor (LVIS), an airborne lidar scanning laser altimeter, aboard the Global Hawk Unmanned Aerial Vehicle. The data were collected as part of NASA Operation IceBridge funded campaigns.",
-            "title": "IceBridge LVIS-GH L2 Geolocated Surface Elevation Product V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRELPCEXB0MY3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRELPCEXB0MY3",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILVGH2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILVGH2.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000780-NSIDC_ECS&m=-32.484375%2120.25%211%211%210%210%2C2&q=ILVGH2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000780-NSIDC_ECS&m=-32.484375%2120.25%211%211%210%210%2C2&q=ILVGH2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILVGH2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILVGH2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/RELPCEXB0MY3",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/RELPCEXB0MY3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/RELPCEXB0MY3",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/RELPCEXB0MY3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000780-NSIDC_ECS",
+            "issued": "2013-10-30",
+            "keyword": [
+                "land surface",
+                "topography",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/RELPCEXB0MY3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-11-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2013-10-26T00:00:00Z/2013-11-14T23:59:59.999Z",
             "theme": [
                 "2013_AN_NASA",
                 "2013_GR_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge LVIS-GH L2 Geolocated Surface Elevation Product V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-4-CR4A-V1.0",
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
+            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 4A mission phase, which occurred during July 2008.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-4-cr4a-v1.0_5mmq-j9wq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-4-CR4A-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-4-cr4a-v1.0_5mmq-j9wq",
-            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 4A mission phase, which occurred during July 2008.",
-            "title": "ROSETTA-ORBITER CAL ALICE 4 CR4A V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL ALICE 4 CR4A V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-AIS-EXT3-V1.0",
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
+            "description": "The Mars Express MARSIS Active Ionospheric Sounder (AIS) full resolution data set includes all spectral information calibrated in units of spectral density for the Mars Express third extended mission, EXT3.  The data set consists of a transmit frequency followed by a time series of spectral density measurements of the received power.  Browse products contain a spectrogram overview plot and individual ionograms for each sounding  activity.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ais-ext3-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-AIS-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ais-ext3-v1.0",
-            "description": "The Mars Express MARSIS Active Ionospheric Sounder (AIS) full resolution data set includes all spectral information calibrated in units of spectral density for the Mars Express third extended mission, EXT3.  The data set consists of a transmit frequency followed by a time series of spectral density measurements of the received power.  Browse products contain a spectrogram overview plot and individual ionograms for each sounding  activity.",
-            "title": "MARS EXPRESS MARSIS RDR ACTIVE IONOSPHERE SOUNDING EXT3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARSIS RDR ACTIVE IONOSPHERE SOUNDING EXT3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD08_E3.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Aqua Aerosol Cloud Water Vapor Ozone 8-Day L3 Global 1Deg CMG. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MYD08_E3.061. https://doi.org/10.5067/MODIS/MYD08_E3.061.",
-            "issued": "2017-10-01",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "ngda",
-                "atmospheric radiation",
-                "aerosols",
-                "weather events",
-                "national geospatial data asset",
-                "earth science",
-                "clouds",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric chemistry"
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
-            "identifier": "C1443743314-LAADS",
-            "description": "The MODIS/Aqua Aerosol Cloud Water Vapor Ozone 8-Day L3 Global 1Deg CMG product (MYD08_E3) contains 8-Day 1 degree x 1 degree grid average values of atmospheric parameters related to atmospheric aerosol particle properties, total ozone burden, atmospheric water vapor, cloud optical and physical properties, and atmospheric stability indices. This product also provides standard deviations, quality assurance weighted means and other statistically derived quantities for each parameter. \r\n\r\nThe MYD08_E3 contains nearly 1000 statistical datasets (SDS's) that are derived from the Level-3 MODIS Atmosphere Daily Global Product. Statistics are computed over a 1 degree equal-angle lat-lon grid that spans an 8-Day interval. Since the grid cells are 1 degree by 1 degree, the output grid is always 360 pixels in width and 180 pixels in length.\r\n\r\nMYD08_E3 product files are stored in Hierarchical Data Format (HDF-EOS). Each gridded global parameter is stored as Scientific Data Sets (SDS) within the file. \r\n\r\nThe MODIS 8-Day Product will be used in the simultaneously study of clouds, water vapor, aerosol , trace gases, land surface and oceanic properties, as well as the interaction between them and their effect on the Earth's energy budget and climate. This product will also be used to investigate seasonal and inter-annual changes in cirrus (semi-transparent) global cloud cover and cloud phase with multispectral observations at high spatial resolution.\r\n\r\nFor more information about the MYD08_E3 product, please visit the MODIS-Atmosphere site at:\r\nhttps://modis-atmos.gsfc.nasa.gov/products/eight-day",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Aerosol Cloud Water Vapor Ozone 8-Day L3 Global 1Deg CMG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Aerosol Cloud Water Vapor Ozone 8-Day L3 Global 1Deg CMG product (MYD08_E3) contains 8-Day 1 degree x 1 degree grid average values of atmospheric parameters related to atmospheric aerosol particle properties, total ozone burden, atmospheric water vapor, cloud optical and physical properties, and atmospheric stability indices. This product also provides standard deviations, quality assurance weighted means and other statistically derived quantities for each parameter. \r\n\r\nThe MYD08_E3 contains nearly 1000 statistical datasets (SDS's) that are derived from the Level-3 MODIS Atmosphere Daily Global Product. Statistics are computed over a 1 degree equal-angle lat-lon grid that spans an 8-Day interval. Since the grid cells are 1 degree by 1 degree, the output grid is always 360 pixels in width and 180 pixels in length.\r\n\r\nMYD08_E3 product files are stored in Hierarchical Data Format (HDF-EOS). Each gridded global parameter is stored as Scientific Data Sets (SDS) within the file. \r\n\r\nThe MODIS 8-Day Product will be used in the simultaneously study of clouds, water vapor, aerosol , trace gases, land surface and oceanic properties, as well as the interaction between them and their effect on the Earth's energy budget and climate. This product will also be used to investigate seasonal and inter-annual changes in cirrus (semi-transparent) global cloud cover and cloud phase with multispectral observations at high spatial resolution.\r\n\r\nFor more information about the MYD08_E3 product, please visit the MODIS-Atmosphere site at:\r\nhttps://modis-atmos.gsfc.nasa.gov/products/eight-day",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD08_E3.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD08_E3.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD08_E3.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD08_E3.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/products/eight-day",
-                    "description": "The MYD08_E3 product description",
                     "@type": "dcat:Distribution",
+                    "description": "The MYD08_E3 product description",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/products/eight-day",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/L3_C61_Changes_v2.pdf",
-                    "description": "The MODIS Atmosphere Eight Day Global product version 6 to 6.1 change document",
                     "@type": "dcat:Distribution",
+                    "description": "The MODIS Atmosphere Eight Day Global product version 6 to 6.1 change document",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/L3_C61_Changes_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/L3_ATBD_C6_C61_2019_02_20.pdf",
-                    "description": "Atmospheric Profile product ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "Atmospheric Profile product ATBD",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/L3_ATBD_C6_C61_2019_02_20.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYD08_E3--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYD08_E3--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD08_E3/",
-                    "description": "Direct access to MYD08_E3 C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MYD08_E3 C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD08_E3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYD08_E3/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYD08_E3/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1443743314-LAADS",
+            "issued": "2017-10-01",
+            "keyword": [
+                "ngda",
+                "atmospheric radiation",
+                "aerosols",
+                "weather events",
+                "national geospatial data asset",
+                "earth science",
+                "clouds",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD08_E3.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-17",
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
+            "title": "MODIS/Aqua Aerosol Cloud Water Vapor Ozone 8-Day L3 Global 1Deg CMG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-IDS%2FLCS-3-RDR-BORRELLY-MCDNLD-V1.0",
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
-                "19p/borrelly 1 (1904 y2)",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "McDonald Observatory (IDS and LCS) column density observations of 19P/Borrelly during the 1981, 1987-8 and 1994 apparitions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-ids-lcs-3-rdr-borrelly-mcdnld-v1.0_5mrt-6qv3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "19p/borrelly 1 (1904 y2)",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-IDS%2FLCS-3-RDR-BORRELLY-MCDNLD-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-ids-lcs-3-rdr-borrelly-mcdnld-v1.0_5mrt-6qv3",
-            "description": "McDonald Observatory (IDS and LCS) column density observations of 19P/Borrelly during the 1981, 1987-8 and 1994 apparitions.",
-            "title": "MCDONALD OBS. COLUMN DENSITY OBSERVATIONS OF 19P/BORRELLY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MCDONALD OBS. COLUMN DENSITY OBSERVATIONS OF 19P/BORRELLY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-OCC-PROF-RTPD-V1.0",
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
-                "magellan",
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes vertical profiles of refractivity, temperature, pressure and density in the neutral Venus atmosphere. The data set is composed of the following parameter fields (listed as the field name followed by a description).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-occ-prof-rtpd-v1.0_5mt5-niwb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "magellan",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-OCC-PROF-RTPD-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-occ-prof-rtpd-v1.0_5mt5-niwb",
-            "description": "This data set includes vertical profiles of refractivity, temperature, pressure and density in the neutral Venus atmosphere. The data set is composed of the following parameter fields (listed as the field name followed by a description).",
-            "title": "MAGELLAN V RSS 5 OCCULTATION PROFILE REF TEMP PRES DENS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAGELLAN V RSS 5 OCCULTATION PROFILE REF TEMP PRES DENS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F11/SSMI/DATA303",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F11 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F11/SSMI/DATA303",
-            "issued": "2012-08-08",
-            "temporal": "1991-12-01T00:00:00Z/2000-05-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "oceans",
-                "atmosphere",
-                "precipitation",
-                "clouds",
-                "earth science",
-                "atmospheric winds",
-                "ocean winds",
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
-            "identifier": "C1979910004-GHRC_DAAC",
             "description": "The RSS SSM/I Ocean Product Grids Weekly Average from DMSP F11 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F11 for weekly averages.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F11 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F11%2FSSMI%2FDATA303",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F11%2FSSMI%2FDATA303",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif11w",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif11w",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/1991/f11_ssmi_19911207v7_wk_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/1991/f11_ssmi_19911207v7_wk_RR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/1991/f11_ssmi_19911207v7_wk_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/1991/f11_ssmi_19911207v7_wk_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/1991/f11_ssmi_19911207v7_wk_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/1991/f11_ssmi_19911207v7_wk_WS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/1991/f11_ssmi_19911207v7_wk_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/1991/f11_ssmi_19911207v7_wk_CW.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ssmi.pdf",
-                    "description": "A Well Calibrated Ocean Algorithm for SSM/I",
                     "@type": "dcat:Distribution",
+                    "description": "A Well Calibrated Ocean Algorithm for SSM/I",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ssmi.pdf",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/rain.pdf",
-                    "description": "SSM/I Rain Retrievals Within an Unified All-Weather Ocean Algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "SSM/I Rain Retrievals Within an Unified All-Weather Ocean Algorithm",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/rain.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f11/weekly/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f11/weekly/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f11/weekly/browse/",
+            "identifier": "C1979910004-GHRC_DAAC",
+            "issued": "2012-08-08",
+            "keyword": [
+                "oceans",
+                "atmosphere",
+                "precipitation",
+                "clouds",
+                "earth science",
+                "atmospheric winds",
+                "ocean winds",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F11/SSMI/DATA303",
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
+            "temporal": "1991-12-01T00:00:00Z/2000-05-20T23:59:59Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F11 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CVP1-V1.0",
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
+            "description": "This archive contains edited data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the Commissioning 1 phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.  This data set supersedes RO/RL-CAL-CONSERT-2-CVP-V1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cvp1-v1.0_5mtx-a73h",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CVP1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cvp1-v1.0_5mtx-a73h",
-            "description": "This archive contains edited data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the Commissioning 1 phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.  This data set supersedes RO/RL-CAL-CONSERT-2-CVP-V1.0.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                            2 CVP1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                            2 CVP1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M24-STR-REFL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m24-str-refl-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M24-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m24-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP024 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP024 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L1/DATA/1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ADEOS-I/OCTS/L1/DATA/1.",
-            "issued": "2017-01-11",
-            "temporal": "1996-11-01T00:00:00Z/1997-06-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-10",
-            "keyword": [
-                "ocean optics",
-                "oceans",
-                "earth science"
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
-            "identifier": "C1200034340-OB_DAAC",
             "description": "On August 17, 1996, the Japanese Space Agency (NASDA - National Space Development Agency)\nlaunched the Advanced Earth Observing Satellite (ADEOS). ADEOS was in a descending, Sun\nsynchronous orbit with a nominal equatorial crossing time of 10:30 a.m. Amoung the\ninstruments carried aboard the ADEOS spacecraft was the Ocean Color and Temperature\nScanner (OCTS). OCTS is an optical radiometer with 12 bands covering the visible, near\ninfrared and thermal infrared regions. (Eight of the bands are in the VIS/NIR. These are\nthe only bands calibrated and processed by the OBPG) OCTS has a swath width of\napproximately 1400 km, and a nominal nadir resolution of 700 m. The instrument operated\nat three tilt states (20 degrees aft, nadir and 20 degrees fore), similar to SeaWiFS.",
-            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Data Regional Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL1%2FDATA%2F1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL1%2FDATA%2F1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/OCTS/L1/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/OCTS/L1/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L1/DATA/1",
-                    "description": "OB.DAAC OCTS ADEOS-I L1 Data Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OCTS ADEOS-I L1 Data Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L1/DATA/1",
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
+            "identifier": "C1200034340-OB_DAAC",
+            "issued": "2017-01-11",
+            "keyword": [
+                "ocean optics",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L1/DATA/1",
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
+            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Data Regional Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/iss-6628",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/station/main/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Beth Beck",
+                "hasEmail": "mailto:beth.beck@nasa.gov"
+            },
+            "description": "Model of the ISS. Polygons: 6628 Vertices: 7239",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/iss-6628/ISSComplete1.fbx.zip",
+                    "mediaType": "application/octet-stream"
+                }
             ],
+            "identifier": "NASA-366",
+            "issued": "2018-06-25",
             "keyword": [
                 "iss",
                 "space stations",
@@ -200059,404 +200068,367 @@
                 "3d model",
                 "structures"
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
-            "identifier": "NASA-366",
-            "description": "Model of the ISS. Polygons: 6628 Vertices: 7239",
-            "title": "NASA 3D Models: International Space Station",
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/iss-6628",
+            "modified": "2020-01-29",
             "programCode": [
                 "026:045",
                 "026:046"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/iss-6628/ISSComplete1.fbx.zip",
-                    "mediaType": "application/octet-stream"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/station/main/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: International Space Station"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/PANAMACITY/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/PANAMACITY/DATA001.",
-            "issued": "1993-10-05",
-            "temporal": "1993-10-05T00:02:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "ocean chemistry",
-                "oceans",
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
-            "identifier": "C1633360586-OB_DAAC",
             "description": "Measurements taken in the Gulf of Mexico near Panama City, Florida in 1993.",
-            "title": "Panama City, Florida optical measurements in 1993",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPANAMACITY%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPANAMACITY%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PanamaCity/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PanamaCity/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360586-OB_DAAC",
+            "issued": "1993-10-05",
+            "keyword": [
+                "ocean optics",
+                "ocean chemistry",
+                "oceans",
+                "earth science",
+                "salinity/density",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/PANAMACITY/DATA001",
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
+            "temporal": "1993-10-05T00:02:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Panama City, Florida optical measurements in 1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LICK1M-SR-CCDC-4-OCC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lick1m-sr-ccdc-4-occ-v1.0_5n3q-6x33",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "s rings",
                 "saturn",
                 "saturn occultation of 28 sagittarius 1989"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LICK1M-SR-CCDC-4-OCC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lick1m-sr-ccdc-4-occ-v1.0_5n3q-6x33",
-            "description": "not applicable",
-            "title": "LICK1M SR CCD-CAM RESAMPLED RING OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LICK1M SR CCD-CAM RESAMPLED RING OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1428",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Steiner, N., K.C. McDonald, E. Podest, C.E. Miller, and S.J. Dinardo. 2017. CARVE: L1 Airborne Forward Looking Infrared Radiance Counts, Alaska, 2013-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1428",
-            "issued": "2017-04-06",
-            "temporal": "2013-04-03T00:00:00Z/2015-11-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
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
-            "identifier": "C2236316372-ORNL_CLOUD",
             "description": "This data set provides earth referenced radiance counts measured by the Forward Looking Infrared (FLIR) camera aboard the CARVE aircraft between April 2013 and November 2015 for the Carbon in Arctic Reservoirs Vulnerability Experiment (CARVE). The FLIR camera records images of the surface temperature while measuring concentrations of atmospheric carbon dioxide, methane, and ozone. Thermal images from the FLIR camera will be used to characterize land surfaces underlain by permafrost during specific phases in the freeze-thaw cycle. The measurements included in this data set are crucial for understanding changes in Arctic carbon cycling and the potential threats posed by thawing of Arctic permafrost.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CARVE: L1 Airborne Forward Looking Infrared Radiance Counts, Alaska, 2013-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1428_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1428",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1428",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/carve/campaign/CARVE_L1_Infrared/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/carve/campaign/CARVE_L1_Infrared/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_Infrared.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_Infrared.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1428",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1428",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L1_Infrared/comp/CARVE_L1_Infrared.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L1_Infrared/comp/CARVE_L1_Infrared.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1428_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1428_1_fit.png",
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
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1428/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1428/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1428_1_fit.png",
+            "identifier": "C2236316372-ORNL_CLOUD",
+            "issued": "2017-04-06",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1428",
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
             "spatial": "-168.07 58.84 -132.24 71.36",
+            "temporal": "2013-04-03T00:00:00Z/2015-11-13T23:59:59Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE: L1 Airborne Forward Looking Infrared Radiance Counts, Alaska, 2013-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3B/CHL/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3B/CHL/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "ocean optics",
-                "ocean chemistry",
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
-            "identifier": "C2340494025-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Binned Chlorophyll (CHL) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3B%2FCHL%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3B%2FCHL%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3B/CHL/2022",
-                    "description": "VIIRS-Suomi-NPP L3B Chlorophyll (CHL) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3B Chlorophyll (CHL) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3B/CHL/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2340494025-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "ocean optics",
+                "ocean chemistry",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3B/CHL/2022",
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
+            "temporal": "2012-01-02T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suomi-NPP VIIRS Global Binned Chlorophyll (CHL) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPB/1C/07",
             "citation": "Wesley Berg. 2022-05-09. GPM_1CMETOPBMHS. GPM MHS on METOP-B Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/MHS/METOPB/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CMETOPBMHS_07.html. Digital Science Data.",
-            "issued": "2022-05-01",
-            "temporal": "2012-09-25T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric water vapor",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264133072-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\n1CAMSR2 contains common calibrated brightness temperature from the AMSR2 passive microwave instrument flown on the GCOMW1 satellite. This products contains 6 swaths. Swath 1 has channels 10.65V 10.65H. Swath 2 has channels 18.7V 18.7H. Swath 3 has channels 23.8V 23.8H. Swath 4 has channels 36.5V 36.5H. Swath S5 has 2 high frequency A-Scan channels (89V 89H). Swath S6 has 2 high frequency B-Scan channels (89V 89H). Data for all six swaths is observed in the same revolution of the instrument. High frequency A and high frequency B data are observed in separate feedhorns. All 1C products have a common L1C data structure, simple and generic. Each L1C swath includes scan time, latitude and longitude, scan status, quality, incidence angle, Sun glint angle, and the intercalibrated brightness temperature (Tc). One or more swaths are included in a product. The radiometer data are recalibrated to a common basis so that precipitation products derived from them are consistent.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_1CMETOPBMHS",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from METOPB (GPM_1CMETOPBMHS)",
-            "title": "GPM MHS on METOP-B Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CMETOPBMHS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.METOPB.MHS.XCAL2016-V.20150101-S000815-E014936.011867.V05A.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPB%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPB%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.METOPB.MHS.XCAL2016-V.20150101-S000815-E014936.011867.V05A.PNG",
-                    "description": "Common Calibrated Brightness Temperature from METOPB (GPM_1CMETOPBMHS)",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from METOPB (GPM_1CMETOPBMHS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.METOPB.MHS.XCAL2016-V.20150101-S000815-E014936.011867.V05A.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CMETOPBMHS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CMETOPBMHS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CMETOPBMHS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CMETOPBMHS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CMETOPBMHS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CMETOPBMHS.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CMETOPBMHS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CMETOPBMHS_07",
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
@@ -200466,136 +200438,175 @@
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.METOPB.MHS.XCAL2016-V.20150101-S000815-E014936.011867.V05A.PNG",
+            "identifier": "C2264133072-GES_DISC",
+            "issued": "2022-05-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric water vapor",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPB/1C/07",
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
+            "series-name": "GPM_1CMETOPBMHS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-09-25T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM MHS on METOP-B Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CMETOPBMHS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/6IX22IHXNWBT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX02 Land Surface Information: Land Use Classification, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/6IX22IHXNWBT.",
-            "issued": "2002-05-14",
-            "temporal": "2002-05-14T00:00:00Z/2002-07-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-07-17",
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
-            "identifier": "C1386250256-NSIDCV0",
             "description": "This data set consists of land use classification data collected for the Iowa Soil Moisture Experiment 2002 (SMEX02) study region. The land use classification image provides information about vegetation present in the study area.",
-            "title": "SMEX02 Land Surface Information: Land Use Classification, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6IX22IHXNWBT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6IX22IHXNWBT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/ancillary_data/landuse_classification/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/ancillary_data/landuse_classification/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/ancillary_data/landuse_classification/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/ancillary_data/landuse_classification/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6IX22IHXNWBT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/6IX22IHXNWBT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6IX22IHXNWBT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/6IX22IHXNWBT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250256-NSIDCV0",
+            "issued": "2002-05-14",
+            "keyword": [
+                "land use/land cover",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/6IX22IHXNWBT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-07-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-93.8 41.7 -93.2 42.04",
+            "temporal": "2002-05-14T00:00:00Z/2002-07-17T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX02 Land Surface Information: Land Use Classification, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/5nbr-6nr9",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_01kmclay-valstage1-V3-01_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000161",
             "issued": "2018-06-25",
-            "temporal": "2006-06-13/2011-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "cloud",
                 "climate",
@@ -200605,536 +200616,539 @@
                 "radiation",
                 "eos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/5nbr-6nr9",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000161",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 1 km Cloud Layer Data V3-01",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_01kmclay-valstage1-V3-01_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2011-10-31",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 1 km Cloud Layer Data V3-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0598-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-23T10:45:45.000 to 2015-02-23T22:11:29.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0598-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0598-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0598-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-23T10:45:45.000 to 2015-02-23T22:11:29.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0598 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0598 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/086OMZDJP2W6",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx23 Mar22 IOP Snow Depth Measurements V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/086OMZDJP2W6.",
-            "issued": "2022-03-08",
-            "temporal": "2022-03-08T00:00:00Z/2022-03-23T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-23",
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
-            "identifier": "C3154261714-NSIDC_ECS",
             "description": "The data set contains snow depth measurements from two regions of Alaska, USA collected during the March 2022 intensive observation period (IOP) as part of the NASA SnowEx 2023 field campaign. The study sites include three boreal forest sites in the Fairbanks region of central Alaska (the Bonanza Creek Experimental Forest, Caribou Poker Creek watershed, and Farmer\u2019s Loop/Creamer\u2019s Field) and a coastal tundra site in the North Slope region (Arctic coastal plain). Snow depth measurements collected from the study sampling sites during the subsequent field season are available as <a href=\"https://nsidc.org/data/snex23_mar23_sd/versions/1\">SnowEx23 Mar23 IOP Snow Depth Measurements, Version 1</a>.",
-            "title": "SnowEx23 Mar22 IOP Snow Depth Measurements V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F086OMZDJP2W6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F086OMZDJP2W6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/086OMZDJP2W6",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/086OMZDJP2W6",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/086OMZDJP2W6",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/086OMZDJP2W6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3154261714-NSIDC_ECS",
+            "issued": "2022-03-08",
+            "keyword": [
+                "snow/ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/086OMZDJP2W6",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-149.597 64.699 -147.49 70.085",
+            "temporal": "2022-03-08T00:00:00Z/2022-03-23T23:59:59.999Z",
             "theme": [
                 "SnowEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx23 Mar22 IOP Snow Depth Measurements V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2789632196-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "2022-10-01",
-            "temporal": "2021-12-21T00:00:00Z/2024-04-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-08",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sawaengphokhai Parnchai",
                 "hasEmail": "mailto:parnchai.k.sawaengphokhai@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2789632196-LARC_ASDC",
             "description": "FLASH_TISA_Terra-NOAA20_Version4C is the Fast Longwave And SHortwave Fluxes (FLASHFlux) Daily Gridded Top-of-Atmosphere (TOA) and Surfaces/Clouds Version 4C data product. This product contains low latency (< 7 days from observations) combined Terra and NOAA-20 FLASHFlux Single Scanner Footprint (SSF) globally gridded TOA and parameterized surface radiative fluxes for applied science uses. Data collection for this product is in progress.\r\n\r\nFLASHFlux data are a product line of the Clouds and the Earth's Radiant Energy Systems (CERES) project designed to process and release TOA and surface radiative fluxes for applied sciences and education uses. The FLASHFlux data product is a rapid-release product based on the algorithms developed for and data collected by the CERES project. CERES is currently producing world-class climate data products derived from measurements taken aboard NASA's Terra, Aqua, and NOAA-20 spacecraft. While of exceptional fidelity, these data products require considerable processing time to assure quality, verify accuracy, and assess precision. The result is that CERES data are typically released up to six months after acquiring the initial measurements. Such delays are of little consequence for climate studies, especially considering the improved quality of the released data products. Thus, FLASHFlux products are not intended to achieve climate quality. FLASHFlux data products were envisioned as a resource whereby CERES data could be provided to the community within a few days of the initial measurements, with some calibration accuracy requirements relaxed to gain speed. \r\n\r\nThe SSF TOA/Surface Fluxes and Clouds product contains one hour of instantaneous FLASHFlux data for a single CERES scanner instrument. The SSF combines instantaneous CERES data with scene information from a higher-resolution imager, such as Moderate-Resolution Imaging Spectroradiometer (MODIS) on the Terra and Aqua satellites and meteorological and ozone information from The Goddard Earth Observing System (GEOS) GEOS-IT Atmospheric Data Assimilation System. NOAA-20 SSF combines instantaneous CERES data with scene information from the Visible Infrared Imaging Radiometer Suite (VIIRS). Scene identification and cloud properties are defined at the higher image resolution, and these data are averaged over the larger CERES footprint. For each CERES footprint, the SSF contains Top-of-Atmosphere fluxes in SW, LW, and NET, surface fluxes using the Langley parameterized shortwave and longwave algorithms, and cloud information. CERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES mission is a follow-up to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. CERES instrument Flight Model 5 (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite and the CERES instrument (FM6) was launched on board NOAA's next generation of polar-orbiting satellites on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "FLASHFlux Daily Gridded TOA and Surfaces/Clouds data Version 4C",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CERES",
-                    "description": "ASDC Data and Information for CERES",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CERES",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CERES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2789632196-LARC_ASDC",
-                    "description": "Earthdata Search for FLASH_TISA_Terra-NOAA20_Version4C (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FLASH_TISA_Terra-NOAA20_Version4C (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2789632196-LARC_ASDC",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#flashflux-gridded-fluxes-level-3",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#flashflux-gridded-fluxes-level-3",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/FLASH_TISASelection.jsp",
-                    "description": "CERES TOOL URL",
                     "@type": "dcat:Distribution",
+                    "description": "CERES TOOL URL",
+                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/FLASH_TISASelection.jsp",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the CERES Ordering Tool"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FLASH/TISA/Terra-NOAA20_Version4C/",
-                    "description": "ASDC Direct Data Download for FLASH_TISA_Terra-NOAA20_Version4C",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FLASH_TISA_Terra-NOAA20_Version4C",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FLASH/TISA/Terra-NOAA20_Version4C/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FLASH/TISA/Terra-NOAA20_Version4C/contents.html",
-                    "description": "OPeNDAP data access for FLASH_TISA_Terra-NOAA20_Version4C",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FLASH_TISA_Terra-NOAA20_Version4C",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FLASH/TISA/Terra-NOAA20_Version4C/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C2789632196-LARC_ASDC",
+            "issued": "2022-10-01",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2789632196-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-03-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2021-12-21T00:00:00Z/2024-04-08T00:00:00Z",
             "theme": [
                 "FLASHFLUX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FLASHFlux Daily Gridded TOA and Surfaces/Clouds data Version 4C"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-2-CR2-9P-TEMPEL1-V1.0",
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
-                "9p/tempel 1 (1867 g1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Spectroscopic, Continuum and Engineering data taken by the Microwave Instrument for the Rosetta Orbiter (MIRO) during the second cruise phase of the mission. The data consist primarily of observations of comet 9P/Tempel 1 before, during and after the planned collision of the Deep Impact mission impactor spacecraft with that comet in July 2005. The data are presented as a series of binary table files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-2-cr2-9p-tempel1-v1.0_5nfp-jk2m",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "9p/tempel 1 (1867 g1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-2-CR2-9P-TEMPEL1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-2-cr2-9p-tempel1-v1.0_5nfp-jk2m",
-            "description": "This data set contains Spectroscopic, Continuum and Engineering data taken by the Microwave Instrument for the Rosetta Orbiter (MIRO) during the second cruise phase of the mission. The data consist primarily of observations of comet 9P/Tempel 1 before, during and after the planned collision of the Deep Impact mission impactor spacecraft with that comet in July 2005. The data are presented as a series of binary table files.",
-            "title": "ROSETTA-ORBITER 9P MIRO 2 CR2 9P-TEMPEL1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 9P MIRO 2 CR2 9P-TEMPEL1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0955-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-11T03:04:05.000 to 2015-08-11T15:53:58.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0955-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0955-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0955-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-11T03:04:05.000 to 2015-08-11T15:53:58.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0955 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0955 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC1-MTP011-V1.0",
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
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase from 19th Dec 2014 to 13th Jan 2015 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc1-mtp011-v1.0_5nkn-rdz8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC1-MTP011-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc1-mtp011-v1.0_5nkn-rdz8",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase from 19th Dec 2014 to 13th Jan 2015 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 1 MTP011 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 1 MTP011 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1044-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-19T21:14:10.000 to 2015-09-20T05:26:05.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1044-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1044-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1044-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-19T21:14:10.000 to 2015-09-20T05:26:05.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1044 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1044 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D60.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo NIR Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D60.061. https://doi.org/10.5067/MODIS/MCD43D60.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "national geospatial data asset",
-                "earth science",
-                "ngda",
-                "land surface",
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
-            "identifier": "C2540273187-LPCLOUD",
-            "description": "The MCD43D60 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D60 is the white-sky albedo for the MODIS NIR broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo NIR Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D60 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D60 is the white-sky albedo for the MODIS NIR broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D60.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D60.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D60.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D60.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273187-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273187-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D60.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D60.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D60",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D60",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D60.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D60.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540273187-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "national geospatial data asset",
+                "earth science",
+                "ngda",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D60.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo NIR Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/5nre-cam4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "To further development of our gene expression approach to biodosimetry we have employed whole genome microarray expression profiling as a discovery platform to identify genes with the potential to distinguish radiation dose across an exposure range relevant for medical decision-making in a radiological emergency. Human peripheral blood from healthy donors was irradiated ex vivo and a 74-gene consensus signature was identified that distinguished between four radiation doses (0.5 2 5 and 8 Gy) and control samples. The same set of genes separated samples by exposure level at both six and 24 hours after treatment with overlap evident only at the highest two doses (5 and 8 Gy). Expression of five genes (CDKN1A FDXR SESN1 BBC3 and PHPT1) from this signature was quantified in the same RNA samples by real-time PCR confirming low variability between donors as well as the predicted radiation response pattern. Experiment Overall Design: Radiation induced gene expression in human blood was measured at 6 and 24 hours after exposure to doses of 0 0.5 2 5 and 8 Gy g-rays. Five independent experiments were performed at each time (6 or 24 hours) using different donors for each experiment",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-152",
+                    "mediaType": "text/html",
+                    "title": "Transcription profiling of human peripheral blood to development gene expression signatures for practical radiation biodosimetry"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-152_5nre-cam4",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "bioassay_data_transformation",
                 "timepoint",
@@ -201154,1462 +201168,1426 @@
                 "p-g8917-4",
                 "feature_extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/5nre-cam4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-152_5nre-cam4",
-            "description": "To further development of our gene expression approach to biodosimetry we have employed whole genome microarray expression profiling as a discovery platform to identify genes with the potential to distinguish radiation dose across an exposure range relevant for medical decision-making in a radiological emergency. Human peripheral blood from healthy donors was irradiated ex vivo and a 74-gene consensus signature was identified that distinguished between four radiation doses (0.5 2 5 and 8 Gy) and control samples. The same set of genes separated samples by exposure level at both six and 24 hours after treatment with overlap evident only at the highest two doses (5 and 8 Gy). Expression of five genes (CDKN1A FDXR SESN1 BBC3 and PHPT1) from this signature was quantified in the same RNA samples by real-time PCR confirming low variability between donors as well as the predicted radiation response pattern. Experiment Overall Design: Radiation induced gene expression in human blood was measured at 6 and 24 hours after exposure to doses of 0 0.5 2 5 and 8 Gy g-rays. Five independent experiments were performed at each time (6 or 24 hours) using different donors for each experiment",
-            "title": "Transcription profiling of human peripheral blood to development gene expression signatures for practical radiation biodosimetry",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-152",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcription profiling of human peripheral blood to development gene expression signatures for practical radiation biodosimetry"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcription profiling of human peripheral blood to development gene expression signatures for practical radiation biodosimetry"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/5nrj-s94f",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "sample collection",
-                "simulated microgravity",
-                "sequence analysis data transformation",
-                "nucleic acid sequencing",
-                "nucleic acid extraction",
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
-            "identifier": "nasa_genelab_GLDS-119_5nrj-s94f",
             "description": "Spaceflight imposes numerous adaptive challenges for terrestrial life. The reduction in gravity or microgravity represents a novel environment that can disrupt homeostasis of many physiological processes. Additionally it is becoming increasingly clear that an organism  s microbiome is critical for host health and examining its resiliency in microgravity represents a new frontier for space biology research. In this study we examine the impact of microgravity on the interactions between the squid Euprymna scolopes and its beneficial symbiont Vibrio fischeri which form a highly specific binary mutualism. First animals inoculated with V. fischeri aboard the space shuttle showed effective colonization of the host light organ the site of the symbiosis during spaceflight. Second RNA-Seq analysis of squid exposed to modeled microgravity conditions exhibited extensive differential gene expression in the presence and absence of the symbiotic partner. Transcriptomic analyses revealed in the absence of the symbiont during modeled microgravity there was an enrichment of genes and pathways associated with the innate immune and oxidative stress response. The results suggest that V. fischeri may help modulate the host stress responses under modeled microgravity. This study provides a window into the adaptive responses that the host animal and its symbiont use during modeled microgravity.",
-            "title": "Effect of microgravity on an animal-bacteria symbiosis",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-119",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-119",
+                    "mediaType": "text/html",
                     "title": "Effect of microgravity on an animal-bacteria symbiosis"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-119_5nrj-s94f",
+            "issued": "2021-05-21",
+            "keyword": [
+                "sample collection",
+                "simulated microgravity",
+                "sequence analysis data transformation",
+                "nucleic acid sequencing",
+                "nucleic acid extraction",
+                "library construction"
+            ],
+            "landingPage": "https://data.nasa.gov/d/5nrj-s94f",
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
+            "title": "Effect of microgravity on an animal-bacteria symbiosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L21C_RAD.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Mike Smyth, Tom Logan, William Johnson. 2023-05-18. ECOSTRESS Tiled Top of Atmosphere Calibrated Radiance Instantaneous L1C Global 70 m v002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L21C_RAD.002. https://doi.org/10.5067/ECOSTRESS/ECO_L1CT_RAD.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2023-05-18",
-            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-18",
-            "keyword": [
-                "land surface",
-                "surface thermal properties",
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
-            "identifier": "C2595678301-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\nThe ECOSTRESS Tiled Top of Atmosphere Calibrated Radiance Instantaneous Level 1 Global 70 m (ECO_L1CT_RAD) Version 2 data product provides at-sensor calibrated radiance values retrieved for five thermal infrared (TIR) bands operating between 8 and 12.5 \u00b5m. This tiled data product is generated from the ECO_L1CG_RAD (https://doi.org/10.5067/ECOSTRESS/ECO_L1CG_RAD.002) Version 2 data product using a modified version of the Military Grid Reference System (MGRS) (https://hls.gsfc.nasa.gov/products-description/tiling-system/), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 meter (m) spatial resolution. Each ECOSTRESS pixel can be assumed to remain at the same location at each timestep within a tile.\r\nThe ECO_L1CT_RAD Version 2 data product contains 12 layers distributed in Cloud Optimized GeoTIFF (COG) format consisting of separate files containing five TIR bands, associated data quality indicators, and cloud and water masks. \r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Missing scan data/striping features: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see Section 3.3.2 of the ECO_L1B_RAD User Guide.\r\n*Scan overlap: An overlap between ECOSTRESS scans results in a clear line overlap and repeating data. Additional information is available in Section 3.2 of the ECO_L1B_RAD User Guide.\r\n*Scan flipping: Improvements to the visualization of the data to compensate for instrument orientation are discussed in Section 3.4 of the ECO_L1B_RAD User Guide.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "title": "ECOSTRESS Tiled Top of Atmosphere Calibrated Radiance Instantaneous L1C Global 70 m V002",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L1CT_RAD.002/ECOv002_L1CT_RAD_26553_007_15SWB_20230313T025821_0710_01/ECOv002_L1CT_RAD_26553_007_15SWB_20230313T025821_0710_01.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\nThe ECOSTRESS Tiled Top of Atmosphere Calibrated Radiance Instantaneous Level 1 Global 70 m (ECO_L1CT_RAD) Version 2 data product provides at-sensor calibrated radiance values retrieved for five thermal infrared (TIR) bands operating between 8 and 12.5 \u00b5m. This tiled data product is generated from the ECO_L1CG_RAD (https://doi.org/10.5067/ECOSTRESS/ECO_L1CG_RAD.002) Version 2 data product using a modified version of the Military Grid Reference System (MGRS) (https://hls.gsfc.nasa.gov/products-description/tiling-system/), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 meter (m) spatial resolution. Each ECOSTRESS pixel can be assumed to remain at the same location at each timestep within a tile.\r\nThe ECO_L1CT_RAD Version 2 data product contains 12 layers distributed in Cloud Optimized GeoTIFF (COG) format consisting of separate files containing five TIR bands, associated data quality indicators, and cloud and water masks. \r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Missing scan data/striping features: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see Section 3.3.2 of the ECO_L1B_RAD User Guide.\r\n*Scan overlap: An overlap between ECOSTRESS scans results in a clear line overlap and repeating data. Additional information is available in Section 3.2 of the ECO_L1B_RAD User Guide.\r\n*Scan flipping: Improvements to the visualization of the data to compensate for instrument orientation are discussed in Section 3.4 of the ECO_L1B_RAD User Guide.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L21C_RAD.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L21C_RAD.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2595678301-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2595678301-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L1CT_RAD.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L1CT_RAD.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/223/ECO1B_Geolocation_ATBD_V1.pdf",
-                    "description": "The Geolocation ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Geolocation ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/223/ECO1B_Geolocation_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/227/ECO_Earthdata_Search_Quick_Guide.pdf",
-                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/227/ECO_Earthdata_Search_Quick_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1655/ECO_L1C-4_Grid_Tile_User_Guide_V2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1655/ECO_L1C-4_Grid_Tile_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L1CT_RAD.002/ECOv002_L1CT_RAD_26553_007_15SWB_20230313T025821_0710_01/ECOv002_L1CT_RAD_26553_007_15SWB_20230313T025821_0710_01.png",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L1CT_RAD.002/ECOv002_L1CT_RAD_26553_007_15SWB_20230313T025821_0710_01/ECOv002_L1CT_RAD_26553_007_15SWB_20230313T025821_0710_01.png",
+                    "mediaType": "image/png",
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
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L1CT_RAD.002/ECOv002_L1CT_RAD_26553_007_15SWB_20230313T025821_0710_01/ECOv002_L1CT_RAD_26553_007_15SWB_20230313T025821_0710_01.png",
+            "identifier": "C2595678301-LPCLOUD",
+            "issued": "2023-05-18",
+            "keyword": [
+                "land surface",
+                "surface thermal properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L21C_RAD.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-05-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
+            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Tiled Top of Atmosphere Calibrated Radiance Instantaneous L1C Global 70 m V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2131772275-GES_DISC.html",
             "citation": "EOS MLS Science Team. 2022-01-11. ML2SO2_NRT. Version 005. MLS/Aura Near-Real-Time L2 Sulfur Dioxide (SO2) Mixing Ratio V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/ML2SO2_NRT_005.html. Digital Science Data.",
-            "issued": "2021-09-21",
-            "temporal": "2021-09-21T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-21",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATHANIEL LIVESEY",
                 "hasEmail": "mailto:livesey@mls.jpl.nasa.gov"
             },
+            "creator": "EOS MLS Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2131772275-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "ML2SO2_NRT is the EOS Aura Microwave Limb Sounder (MLS) Near-Real-Time (NRT) product for sulfur dioxide (SO2). This product contains SO2 profiles derived from the 190 and 240 GHz regions. The NRT data are typically available within 3 hours of observation and are broken into files containing about 15 minutes of data. The most recent 7 days of data are available online. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The vertical coverage is from 215 to 10 hPa.\n\nThe MLS NRT algorithm uses a simplified fast forward model to meet Near Real Time data latency requirements and are therefore not as accurate as the retrievals that constitute the standard MLS products. Nevertheless the results are scientifically useful in selected regions of the Earth's atmosphere provided that the data are screened according to the recommendations in the MLS NRT User Guide and the MLS L2 Data Quality Document for Standard Products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2SO2_NRT",
-            "creator": "EOS MLS Science Team",
-            "title": "MLS/Aura Near-Real-Time L2 Sulfur Dioxide (SO2) Mixing Ratio V005 (ML2SO2_NRT) at GES DISC",
-            "graphic-preview-description": "Aura MLS logo",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2SO2_NRT_003.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2SO2_NRT_003.jpeg",
-                    "description": "Aura MLS logo",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2SO2_NRT_003.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2SO2_NRT_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2SO2_NRT_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aura_MLS_NRT/ML2SO2_NRT.005",
-                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aura_MLS_NRT/ML2SO2_NRT.005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aura_MLS_NRT/ML2SO2_NRT.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aura_MLS_NRT/ML2SO2_NRT.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/datacasting/ML2SO2_NRT.005.datacast-feed.xml",
-                    "description": "Access the data via datacasting.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via datacasting.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/datacasting/ML2SO2_NRT.005.datacast-feed.xml",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a datacast URL."
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2SO2_NRT_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2SO2_NRT_005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/NRT-user-guide-v5.pdf",
-                    "description": "Aura MLS Version 5 Level 2 Near-Real-Time Data User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS Version 5 Level 2 Near-Real-Time Data User Guide",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/NRT-user-guide-v5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/v5-0_data_quality_document.pdf",
-                    "description": "Aura MLS Version 5 Level 2 Data Quality and Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS Version 5 Level 2 Data Quality and Description Document",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/v5-0_data_quality_document.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mls.jpl.nasa.gov/",
-                    "description": "MLS Science Team home page",
                     "@type": "dcat:Distribution",
+                    "description": "MLS Science Team home page",
+                    "downloadURL": "https://mls.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Aura MLS logo",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2SO2_NRT_003.jpeg",
+            "identifier": "C2131772275-GES_DISC",
+            "issued": "2021-09-21",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2131772275-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-09-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML2SO2_NRT",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2021-09-21T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "Aura",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Near-Real-Time L2 Sulfur Dioxide (SO2) Mixing Ratio V005 (ML2SO2_NRT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MAHLI-4-RDR-Z-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mahli-4-rdr-z-v1.0_5nx7-gtbf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MAHLI-4-RDR-Z-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mahli-4-rdr-z-v1.0_5nx7-gtbf",
-            "description": "NULL",
-            "title": "MSL MARS HAND LENS IMAGER 4\n                                      RDR ZSTACK V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS HAND LENS IMAGER 4\n                                      RDR ZSTACK V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-L2X21",
             "citation": "CYGNSS. 2018-09-21. CYGNSS Level 2 Science Data Record. Version 2.1. CYGNSS Level 2 Science Data Record Version 2.1. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNS-L2X21. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2018-09-21, CYGNSS Level 2 Science Data Record Version 2.1, https://cygnss.engin.umich.edu/.",
-            "issued": "2018-05-14",
-            "temporal": "2017-03-18T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-05-14",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-20-0079.1"
-            ],
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "ocean winds",
-                "radar",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2251464495-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset contains the Version 2.1 CYGNSS Level 2 Science Data Record which provides the time-tagged and geolocated average wind speed (m/s) and mean square slope (MSS) with 25x25 kilometer resolution from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. This version supersedes Version 2.0. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). A subset of DDM data used in the direct processing of the average wind speed and MSS is co-located inside of the Level 2 data files. Only one netCDF data file is produced each day (each file containing data from up to 8 unique CYGNSS spacecraft) with a latency of approximately 6 days (or better) from the last recorded measurement time. The Version 2.1 release represents the second science-quality release. Here is a summary of improvements that reflect the quality of the Version 2.1 data release: 1) revised Geophysical Model Functions (GMFs) for both Fully Developed Seas (FDS) and Young Seas with Limited Fetch conditions, to be consistent with the calibration changes made to the v2.1 Level 1 science data products.; 2) Revised covariance matrix between DDMA and LES versions of the FDS wind speed retrieval, used by the minimum variance estimator, resulting from changes made to the v2.1 Level 1 science data products; 3) Revised debiasing algorithm coefficients used by the FDS L2 retrieval algorithm, resulting from changes made to the v2.1 Level 2 science data products; 4) revised quality control (Q/C) flags related to the required level of consistency between DDMA and LES versions of the FDS wind speed retrieval (the errors in the two retrievals are now less correlated so larger discrepancies are allowed; if either retrieval is not available, the sample receives a fatal Q/C flag); 5) new Q/C flag related to the block type of the GPS satellite which provided the transmitted signal. Samples using block II-F signals receive a fatal Q/C flag due to the higher level of uncertainty in their radiated power; 6) revised wind speed uncertainty values as a function of RCG and wind speed, plus a new dependence of the uncertainty on GPS block type to reflect the higher uncertainty in GPS radiated power for block II-F satellites.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 2 Science Data Record",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 2 Science Data Record Version 2.1",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_V2.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the Version 2.1 CYGNSS Level 2 Science Data Record which provides the time-tagged and geolocated average wind speed (m/s) and mean square slope (MSS) with 25x25 kilometer resolution from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. This version supersedes Version 2.0. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). A subset of DDM data used in the direct processing of the average wind speed and MSS is co-located inside of the Level 2 data files. Only one netCDF data file is produced each day (each file containing data from up to 8 unique CYGNSS spacecraft) with a latency of approximately 6 days (or better) from the last recorded measurement time. The Version 2.1 release represents the second science-quality release. Here is a summary of improvements that reflect the quality of the Version 2.1 data release: 1) revised Geophysical Model Functions (GMFs) for both Fully Developed Seas (FDS) and Young Seas with Limited Fetch conditions, to be consistent with the calibration changes made to the v2.1 Level 1 science data products.; 2) Revised covariance matrix between DDMA and LES versions of the FDS wind speed retrieval, used by the minimum variance estimator, resulting from changes made to the v2.1 Level 1 science data products; 3) Revised debiasing algorithm coefficients used by the FDS L2 retrieval algorithm, resulting from changes made to the v2.1 Level 2 science data products; 4) revised quality control (Q/C) flags related to the required level of consistency between DDMA and LES versions of the FDS wind speed retrieval (the errors in the two retrievals are now less correlated so larger discrepancies are allowed; if either retrieval is not available, the sample receives a fatal Q/C flag); 5) new Q/C flag related to the block type of the GPS satellite which provided the transmitted signal. Samples using block II-F signals receive a fatal Q/C flag due to the higher level of uncertainty in their radiated power; 6) revised wind speed uncertainty values as a function of RCG and wind speed, plus a new dependence of the uncertainty on GPS block type to reflect the higher uncertainty in GPS radiated power for block II-F satellites.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L2X21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L2X21",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0348-9_L2_v2.1_netCDF_Data_Dictionary.xlsx",
-                    "description": "Look-up table to define the Level 2 data variables",
                     "@type": "dcat:Distribution",
+                    "description": "Look-up table to define the Level 2 data variables",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0348-9_L2_v2.1_netCDF_Data_Dictionary.xlsx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://doi.org/10.1109/JSTARS.2018.2833075",
-                    "description": "Ruf, C., R. Balasubramaniam, 'Development of the CYGNSS Geophysical Model Function for Wind Speed', IEEE J. Sel. Topics Appl. Earth Obs. Remote Sens., doi: 10.1109/JSTARS.2018.2833075, 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., R. Balasubramaniam, 'Development of the CYGNSS Geophysical Model Function for Wind Speed', IEEE J. Sel. Topics Appl. Earth Obs. Remote Sens., doi: 10.1109/JSTARS.2018.2833075, 2018.",
+                    "downloadURL": "https://doi.org/10.1109/JSTARS.2018.2833075",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0138_ATBD_L2_Wind_Speed_Retrieval_Rev5_Aug2018_release.pdf",
-                    "description": "Level 2 Wind Speed Retrieval Algorithm Theoretical Basis Document, M. P. Clarizia, V. Zavarotny, C. Ruf, CYGNSS Project Document 148-0138, Rev 5, 17 Aug. 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 2 Wind Speed Retrieval Algorithm Theoretical Basis Document, M. P. Clarizia, V. Zavarotny, C. Ruf, CYGNSS Project Document 148-0138, Rev 5, 17 Aug. 2018.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0138_ATBD_L2_Wind_Speed_Retrieval_Rev5_Aug2018_release.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_V2.1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_V2.1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0139-L2-MSS-ATBD-R3.pdf",
-                    "description": "Level 2 Mean-Square Slope Retrieval Algorithm Theoretical Basis Document, V. Zavorotny, CYGNSS Project Document 148-0139, Rev 3, 22 September 2016.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 2 Mean-Square Slope Retrieval Algorithm Theoretical Basis Document, V. Zavorotny, CYGNSS Project Document 148-0139, Rev 3, 22 September 2016.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0139-L2-MSS-ATBD-R3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-20-0079.1",
-                    "description": "Asharaf, S., Waliser, D. E., Posselt, D. J., Ruf, C. S., Zhang, C., & Putra, A. W. (2021). CYGNSS Ocean Surface Wind Validation in the Tropics, Journal of Atmospheric and Oceanic Technology, 38(4), 711-724. https://doi.org/10.1175/JTECH-D-20-0079.1",
                     "@type": "dcat:Distribution",
+                    "description": "Asharaf, S., Waliser, D. E., Posselt, D. J., Ruf, C. S., Zhang, C., & Putra, A. W. (2021). CYGNSS Ocean Surface Wind Validation in the Tropics, Journal of Atmospheric and Oceanic Technology, 38(4), 711-724. https://doi.org/10.1175/JTECH-D-20-0079.1",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-20-0079.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2016.2541343",
-                    "description": "Clarizia, M. P., and C. S. Ruf, 'Wind Speed Retrieval Algorithm for the Cyclone Global Navigation Satellite System (CYGNSS) Mission', IEEE Trans Geosci. Remote Sens., doi:10.1109/TGRS.2016.2541343, 2016.",
                     "@type": "dcat:Distribution",
+                    "description": "Clarizia, M. P., and C. S. Ruf, 'Wind Speed Retrieval Algorithm for the Cyclone Global Navigation Satellite System (CYGNSS) Mission', IEEE Trans Geosci. Remote Sens., doi:10.1109/TGRS.2016.2541343, 2016.",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2016.2541343",
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
-                    "downloadURL": "https://cygnss.engin.umich.edu/",
-                    "description": "CYGNSS Mission Page at University of Michigan",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Mission Page at University of Michigan",
+                    "downloadURL": "https://cygnss.engin.umich.edu/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2251464495-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2251464495-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2251464495-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2251464495-POCLOUD",
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
-                    "downloadURL": "https://doi.org/10.3998/mpub.12741920",
-                    "description": "CYGNSS Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Handbook",
+                    "downloadURL": "https://doi.org/10.3998/mpub.12741920",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_V2.1.jpg",
+            "identifier": "C2251464495-POCLOUD",
+            "issued": "2018-05-14",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "ocean winds",
+                "radar",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-L2X21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-05-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1175/JTECH-D-20-0079.1"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "CYGNSS Level 2 Science Data Record",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "2017-03-18T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 2 Science Data Record Version 2.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/LWJ6TF5SZRG3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L4 Global 3-hourly 9 km EASE-Grid Surface and Root Zone Soil Moisture Analysis Update V007. Version 007. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/LWJ6TF5SZRG3.",
-            "issued": "2015-03-31",
-            "temporal": "2015-03-31T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-25",
-            "keyword": [
-                "earth science",
-                "soils",
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
-            "identifier": "C2938665508-NSIDC_CPRD",
             "description": "SMAP Level-4 (L4) surface and root zone soil moisture data are provided in three products:\n<ul> \n  <li>SMAP L4 Global 3-hourly 9 km EASE-Grid Surface and Root Zone Soil Moisture Geophysical Data (SPL4SMGP, DOI: 10.5067/EVKPQZ4AFC4D)</li>\n  <li>SMAP L4 Global 3-hourly 9 km EASE-Grid Surface and Root Zone Soil Moisture Analysis Update (SPL4SMAU, DOI: 10.5067/LWJ6TF5SZRG3)</li>\n  <li>SMAP L4 Global 9 km EASE-Grid Surface and Root Zone Soil Moisture Land Model Constants (SPL4SMLM, DOI: 10.5067/KN96XNPZM4EG).</li>\n</ul>\nFor each product, SMAP L-band brightness temperature data from descending and ascending half-orbit satellite passes (approximately 6:00 a.m. and 6:00 p.m. local solar time, respectively) are assimilated into a land surface model that is gridded using an Earth-fixed, global cylindrical 9 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0) projection.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP L4 Global 3-hourly 9 km EASE-Grid Surface and Root Zone Soil Moisture Analysis Update V007",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-196,-75,144,82&l=SMAP_L4_Soil_Temperature_Layer_1,SMAP_L4_Uncertainty_Analyzed_Surface_Soil_Moisture,SMAP_L4_Analyzed_Surface_Soil_Moisture,SMAP_L4_Analyzed_Root_Zone_Soil_Moisture,SMAP_L4_Uncertainty_Analyzed_Root_Zone_Soil_Moisture,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-03-31",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLWJ6TF5SZRG3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLWJ6TF5SZRG3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL4SMAU+V007",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL4SMAU+V007",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938665508-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938665508-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-196%2C-75%2C144%2C82&l=SMAP_L4_Soil_Temperature_Layer_1%2CSMAP_L4_Uncertainty_Analyzed_Surface_Soil_Moisture%2CSMAP_L4_Analyzed_Surface_Soil_Moisture%2CSMAP_L4_Analyzed_Root_Zone_Soil_Moisture%2CSMAP_L4_Uncertainty_Analyzed_Root_Zone_Soil_Moisture%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-03-31",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-196%2C-75%2C144%2C82&l=SMAP_L4_Soil_Temperature_Layer_1%2CSMAP_L4_Uncertainty_Analyzed_Surface_Soil_Moisture%2CSMAP_L4_Analyzed_Surface_Soil_Moisture%2CSMAP_L4_Analyzed_Root_Zone_Soil_Moisture%2CSMAP_L4_Uncertainty_Analyzed_Root_Zone_Soil_Moisture%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-03-31",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/LWJ6TF5SZRG3",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/LWJ6TF5SZRG3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/LWJ6TF5SZRG3",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/LWJ6TF5SZRG3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-196,-75,144,82&l=SMAP_L4_Soil_Temperature_Layer_1,SMAP_L4_Uncertainty_Analyzed_Surface_Soil_Moisture,SMAP_L4_Analyzed_Surface_Soil_Moisture,SMAP_L4_Analyzed_Root_Zone_Soil_Moisture,SMAP_L4_Uncertainty_Analyzed_Root_Zone_Soil_Moisture,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-03-31",
+            "identifier": "C2938665508-NSIDC_CPRD",
+            "issued": "2015-03-31",
+            "keyword": [
+                "earth science",
+                "soils",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/LWJ6TF5SZRG3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -85.044 180.0 85.044",
+            "temporal": "2015-03-31T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP L4 Global 3-hourly 9 km EASE-Grid Surface and Root Zone Soil Moisture Analysis Update V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M16-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m16-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M16-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m16-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP016 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP016 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-EXT3-CALIB2-V1.0",
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
+            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 3 mission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains instrument outputs in\nvolts and amperes, calibrated and corrected for instrument offsets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-ext3-calib2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-EXT3-CALIB2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-ext3-calib2-v1.0",
-            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 3 mission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains instrument outputs in\nvolts and amperes, calibrated and corrected for instrument offsets.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 3\nEXT3 CALIB2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 3\nEXT3 CALIB2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/826/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-07-29",
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
-            "identifier": "DASHLINK_826",
             "description": "Prognostic performance evaluation has gained significant attention in the past few years.*Currently, prognostics concepts lack standard definitions and suffer from ambiguous and inconsistent interpretations. This lack of standards is in part due to the varied end- user requirements for different applications, time scales, available information, domain dynamics, etc. to name a few. The research community has used a variety of metrics largely based on convenience and their respective requirements. Very little attention has been focused on establishing a standardized approach to compare different efforts. This paper presents several new evaluation metrics tailored for prognostics that were recently introduced and were shown to effectively evaluate various algorithms as compared to other conventional metrics. Specifically, this paper presents a detailed discussion on how these metrics should be interpreted and used. These metrics have the capability of incorporating probabilistic uncertainty estimates from prognostic algorithms. In addition to quantitative assessment they also offer a comprehensive visual perspective that can be used in designing the prognostic system. Several methods are suggested to customize these metrics for different applications. Guidelines are provided to help choose one method over another based on distribution characteristics. Various issues faced by prognostics and its performance evaluation are discussed followed by a formal notational framework to help standardize subsequent developments.",
-            "title": "Metrics for Offline Evaluation of Prognostic Performance",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_IJPHM_Metrics_2.pdf",
-                    "description": "2010_IJPHM_Metrics.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2010_IJPHM_Metrics.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_IJPHM_Metrics_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2010_IJPHM_Metrics.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_826",
+            "issued": "2013-07-29",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/826/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Metrics for Offline Evaluation of Prognostic Performance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-PRL-V1.0",
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
+            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the Prelanding phase (PRL). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 21 Jan 2014 and 19 Nov 2014.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-prl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-PRL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-prl-v1.0",
-            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the Prelanding phase (PRL). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 21 Jan 2014 and 19 Nov 2014.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 5 PRL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 5 PRL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD18A2.062",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dongdong Wang. 2024-03-07. MCD18A2.062. MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 1km SIN Grid V062. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD18A2.062. https://doi.org/10.5067/MODIS/MCD18A2.062. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-03-18",
-            "temporal": "2000-02-24T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-18",
-            "keyword": [
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "land surface",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dongdong Wang",
                 "hasEmail": "mailto:ddwang@umd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2486282714-LPCLOUD",
-            "description": "The MCD18A2 Version 6.2 is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Photosynthetically Active Radiation (PAR) gridded Level 3 product produced daily at 1 kilometer pixel resolution with estimates of PAR every 3 hours. PAR is incident solar radiation in the visible spectrum (400-700 nanometers) and is an important variable in land-surface models that address a variety of scientific and application issues. The MCD18 products are based on a prototyping algorithm that uses multi-temporal signatures of MODIS data to derive surface reflectance and then calculate incident PAR using the look-up table (LUT) approach. The LUTs consider different types of loadings of aerosols and clouds at a variety of illumination/viewing geometry. Global PAR products are generated from MODIS and geostationary satellite data. Additional details regarding the methodology used to create the data are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf)).\r\n\r\nProvided in the MOD18A2 product are layers for instantaneous PAR array for each individual MODIS overpass and 3-hour PAR array along with a View Zenith Angle layer.\r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Radiation products. Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18). \r\n\r\nThe Version 6.2 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: 1) MODIS shortwave infrared bands are included in the retrieval algorithm, which significantly reduces estimation uncertainties in cloud- and snow-covered pixels. \r\n2) An improved climatology of surface reflectance was produced and used in the retrieval algorithm.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "MCD18A2.062",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Dongdong Wang",
-            "title": "MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 1km SIN Grid V062",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800165776-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD18A2 Version 6.2 is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Photosynthetically Active Radiation (PAR) gridded Level 3 product produced daily at 1 kilometer pixel resolution with estimates of PAR every 3 hours. PAR is incident solar radiation in the visible spectrum (400-700 nanometers) and is an important variable in land-surface models that address a variety of scientific and application issues. The MCD18 products are based on a prototyping algorithm that uses multi-temporal signatures of MODIS data to derive surface reflectance and then calculate incident PAR using the look-up table (LUT) approach. The LUTs consider different types of loadings of aerosols and clouds at a variety of illumination/viewing geometry. Global PAR products are generated from MODIS and geostationary satellite data. Additional details regarding the methodology used to create the data are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf)).\r\n\r\nProvided in the MOD18A2 product are layers for instantaneous PAR array for each individual MODIS overpass and 3-hour PAR array along with a View Zenith Angle layer.\r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Radiation products. Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18). \r\n\r\nThe Version 6.2 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: 1) MODIS shortwave infrared bands are included in the retrieval algorithm, which significantly reduces estimation uncertainties in cloud- and snow-covered pixels. \r\n2) An improved climatology of surface reflectance was produced and used in the retrieval algorithm.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD18A2.062",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD18A2.062",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD18A2.062/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD18A2.062/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2486282714-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2486282714-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD18A2.062",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD18A2.062",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1658/MCD18_User_Guide_V62.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1658/MCD18_User_Guide_V62.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD18A2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD18A2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 1 has been achieved for the MODIS Surface Radiation products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the MODIS Surface Radiation products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18",
-                    "description": "Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP109/MOTA/MCD18A2.062/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP109/MOTA/MCD18A2.062/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800165776-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800165776-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800165776-LPCLOUD?h=85&w=85",
+            "identifier": "C2486282714-LPCLOUD",
+            "issued": "2021-03-18",
+            "keyword": [
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD18A2.062",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "MCD18A2.062",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 1km SIN Grid V062"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1141",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Betts, A.K., and C. Jakob. 2013. LBA-HMET PC-06 ECMWF Modeled Precipitation and Surface Flux, Rondonia, Brazil: 1999. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1141",
-            "issued": "2013-01-11",
-            "temporal": "1999-01-01T00:00:00Z/1999-03-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-18",
-            "keyword": [
-                "atmospheric temperature",
-                "precipitation",
-                "atmosphere",
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
-            "identifier": "C2768943309-ORNL_CLOUD",
             "description": "This data set provides the mean diurnal cycle of precipitation, near-surface thermodynamics, and surface fluxes generated from short-term forecasts from the European Centre for Medium-Range Weather Forecasts (ECMWF) model.The model outputs were 12- to 36-hour short-range forecasts, run at a triangular truncation of T319 and a vertical resolution of 60 levels, from each daily 1200 (UTC) analysis. The version of the forecast model used to prepare this data product was the operational ECMWF model in fall 2000, which included the tiled land-surface scheme (TESSEL) (Van den Hurk et al., 2000) and recent revisions to the convection, radiation, and cloud schemes described by Gregory et al., (2000). The ECMWF model was run for two Large-Scale Biosphere-Atmosphere Experiment in Amazonia (LBA) campaigns conducted in Rondonia, Brazil, during January and February of 1999: the Wet Season Atmospheric Mesoscale Campaign (WETAMC) and the Tropical Rainfall Measuring Mission (TRMM). See Silva Dias et al.,(2002) for additional information regarding the WETAMAC and TRMM campaigns. There are two comma-delimited data files with this data set: the ECMWF model output data and a file containing the mean hourly precipitation observations used to check the model output for biases.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-HMET PC-06 ECMWF Modeled Precipitation and Surface Flux, Rondonia, Brazil: 1999",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1141",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1141",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/physical_climate/PC06_ECMWF_LBA/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/physical_climate/PC06_ECMWF_LBA/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/PC06_ECMWF_LBA.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/PC06_ECMWF_LBA.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1141",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1141",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/physical_climate/PC06_ECMWF_LBA/comp/PC06_ECMWF_LBA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/physical_climate/PC06_ECMWF_LBA/comp/PC06_ECMWF_LBA.pdf",
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
+            "identifier": "C2768943309-ORNL_CLOUD",
+            "issued": "2013-01-11",
+            "keyword": [
+                "atmospheric temperature",
+                "precipitation",
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1141",
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
             "spatial": "-62.37 -10.85 -61.87 -10.75",
+            "temporal": "1999-01-01T00:00:00Z/1999-03-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-HMET PC-06 ECMWF Modeled Precipitation and Surface Flux, Rondonia, Brazil: 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D49.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang\r\n. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo VIS Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D49.061. https://doi.org/10.5067/MODIS/MCD43D49.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "ngda",
-                "surface radiative properties",
-                "land surface",
-                "earth science",
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
-            "identifier": "C2540271839-LPCLOUD",
-            "description": "The MCD43D49 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Black-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer.  \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic.  \r\n\r\nMCD43D49 is the black-sky albedo for the MODIS visible broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo VIS Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D49 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Black-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer.  \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic.  \r\n\r\nMCD43D49 is the black-sky albedo for the MODIS visible broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D49.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D49.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D49.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D49.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540271839-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540271839-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D49.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D49.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D49",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D49",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D49.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D49.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540271839-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "ngda",
+                "surface radiative properties",
+                "land surface",
+                "earth science",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D49.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo VIS Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-5-COLLECTED-MODELS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Collected shape and gravity models and related data for the NEAR targets 433 Eros and 253 Mathilde.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-5-collected-models-v1.0_5pcc-3mg9",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "near earth asteroid rendezvous",
                 "mathilde",
                 "eros"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-5-COLLECTED-MODELS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-5-collected-models-v1.0_5pcc-3mg9",
-            "description": "Collected shape and gravity models and related data for the NEAR targets 433 Eros and 253 Mathilde.",
-            "title": "NEAR COLLECTED TARGET MODELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR COLLECTED TARGET MODELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/498",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MacPherson, J.I., and R.L. Desjardins. 2000. BOREAS AFM-04 Twin Otter Aircraft Sounding Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/498",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-25T00:00:00Z/1996-08-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "atmospheric chemistry",
-                "atmospheric pressure"
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
-            "identifier": "C2808092218-ORNL_CLOUD",
             "description": "Measurements include concentrations of carbon dioxide and ozone, atmospheric pressure, dry bulb temperature, potential temperature, dewpoint temperature, calculated mixing ratio, and wind speed and direction at both the NSA and the SSA in 1994 and 1996.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS AFM-04 Twin Otter Aircraft Sounding Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F498",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F498",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/afm4toas/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/afm4toas/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM04_Soundings.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM04_Soundings.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/498",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/498",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/AFM04_Soundings.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/AFM04_Soundings.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/AFM04_Soundings.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/AFM04_Soundings.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/AFM04_Soundings.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/AFM04_Soundings.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/afm4toas.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/afm4toas.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/twinotter.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/twinotter.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/twinotter96.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/twinotter96.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/twinotter96_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm4toas/comp/twinotter96_doc.pdf",
+                    "mediaType": "application/pdf",
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
+            "identifier": "C2808092218-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "atmospheric chemistry",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/498",
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
             "spatial": "-106.42 53.21 -97.86 56.02",
+            "temporal": "1994-05-25T00:00:00Z/1996-08-08T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS AFM-04 Twin Otter Aircraft Sounding Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/PREPP/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/PREPP/DATA001.",
-            "issued": "2001-02-08",
-            "temporal": "2001-02-08T03:46:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "ocean optics",
-                "salinity/density",
-                "earth science",
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
-            "identifier": "C1633360621-OB_DAAC",
             "description": "Measurements made under the Pearl River Estuary Pollution Project (PREPP) near Hong Kong in 2001.",
-            "title": "Pearl River Estuary Pollution Project (PREPP)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPREPP%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPREPP%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PREPP/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PREPP/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "theme": [
-                "geospatial"
+            "identifier": "C1633360621-OB_DAAC",
+            "issued": "2001-02-08",
+            "keyword": [
+                "ocean temperature",
+                "ocean optics",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "oceans"
             ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/PREPP/DATA001",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2023-04-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2001-02-08T03:46:00Z/2023-04-17T00:00:00Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Pearl River Estuary Pollution Project (PREPP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2758503590-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "UW-Madison Space Science and Engineering Center: Joe Taylor; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow. 2023-09-15. SNDRJ2CrISL1B. Version 3. JPSS-2 CrIS Level 1B Beta Full Spectral Resolution V3. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/SNDRJ2CrISL1B_3.html. Digital Science Data.",
-            "issued": "2023-02-22",
-            "temporal": "2022-02-22T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-26",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
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
-            "identifier": "C2758503590-GES_DISC",
-            "description": "The goal of creating this product is to allow users to begin working with data from the CrIS instrument on-board the recently launched NOAA-21 / JPSS-2 (J2) satellite. The J2 beta product was generated using an updated version of the software that is used to generate the Version 3 SNPP and JPSS-1 (J1) products, which are currently available from GES DISC. Changes were made to allow J2 processing, but the underlying algorithm theoretical basis remains the same. It should be noted that work on refining the J2 calibration parameters is ongoing, and the parameters used in this release are preliminary. A future Version 4 set of products is planned for release after J2 has reached validated status, which will include optimized J2 parameters and will use a single software version for all three instruments incorporating various algorithm improvements. \n\nThe Cross-track Infrared Sounder (CrIS) Level 1B Full Spectral Resolution (FSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Joint Polar Satellite System-2 (JPSS-2) platform. This platform is also know as NOAA-21 (National Oceanic and Atmospheric Administration). The JPSS-2 mission with CrIS instrumentation is a follow-on to the Suomi National Polar-orbiting Partnership (SNPP)  mission. The CrIS instrumentation and data processing system is nearly identical to that of the SNPP satellite. \n\nCrIS is designed to be used with the ATMS (Advanced Technology Microwave Sounder) instrument. Processing the data from both of these instruments together is referred to as CrIMSS (Cross-Track Infrared and Microwave Sounder Suite).\n\n\nThe FSR files have 2,223 channels (*2211 apodized channels): 637 (*633) shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 869 (*865) midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 (*713)longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nAn issue has been observed in J2 CrIS data that impacts calibration of observations for a period of several minutes during each orbit. The issue occurs in the southern hemisphere during the descending part of the orbit, near a satellite solar zenith angle of -118 degrees. There is significant variability in affected latitudes throughout the year. The issue is indicated by non-zero quality flags in the Level 1B product. The root cause is believed to be variation in calibration views due to rapid instrument temperature changes after the J2 satellite passes from the Earth's shadow into direct sunlight. Potential solutions are being evaluated for implementation in a future product version. \n\nIf you were redirected to this page from a DOI from an older version, please note this is the current version of the product. Please contact the GES DISC user support if you need information about previous data collections.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "SNDRJ2CrISL1B",
             "creator": "UW-Madison Space Science and Engineering Center: Joe Taylor; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow",
-            "title": "JPSS-2 CrIS Level 1B Beta Full Spectral Resolution V3 (SNDRJ2CrISL1B) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ2CrISL1B.v3.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The goal of creating this product is to allow users to begin working with data from the CrIS instrument on-board the recently launched NOAA-21 / JPSS-2 (J2) satellite. The J2 beta product was generated using an updated version of the software that is used to generate the Version 3 SNPP and JPSS-1 (J1) products, which are currently available from GES DISC. Changes were made to allow J2 processing, but the underlying algorithm theoretical basis remains the same. It should be noted that work on refining the J2 calibration parameters is ongoing, and the parameters used in this release are preliminary. A future Version 4 set of products is planned for release after J2 has reached validated status, which will include optimized J2 parameters and will use a single software version for all three instruments incorporating various algorithm improvements. \n\nThe Cross-track Infrared Sounder (CrIS) Level 1B Full Spectral Resolution (FSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Joint Polar Satellite System-2 (JPSS-2) platform. This platform is also know as NOAA-21 (National Oceanic and Atmospheric Administration). The JPSS-2 mission with CrIS instrumentation is a follow-on to the Suomi National Polar-orbiting Partnership (SNPP)  mission. The CrIS instrumentation and data processing system is nearly identical to that of the SNPP satellite. \n\nCrIS is designed to be used with the ATMS (Advanced Technology Microwave Sounder) instrument. Processing the data from both of these instruments together is referred to as CrIMSS (Cross-Track Infrared and Microwave Sounder Suite).\n\n\nThe FSR files have 2,223 channels (*2211 apodized channels): 637 (*633) shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 869 (*865) midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 (*713)longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nAn issue has been observed in J2 CrIS data that impacts calibration of observations for a period of several minutes during each orbit. The issue occurs in the southern hemisphere during the descending part of the orbit, near a satellite solar zenith angle of -118 degrees. There is significant variability in affected latitudes throughout the year. The issue is indicated by non-zero quality flags in the Level 1B product. The root cause is believed to be variation in calibration views due to rapid instrument temperature changes after the J2 satellite passes from the Earth's shadow into direct sunlight. Potential solutions are being evaluated for implementation in a future product version. \n\nIf you were redirected to this page from a DOI from an older version, please note this is the current version of the product. Please contact the GES DISC user support if you need information about previous data collections.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -202618,583 +202596,589 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ2CrISL1B_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ2CrISL1B_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS2_Sounder_Level1/SNDRJ2CrISL1B.3/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS2_Sounder_Level1/SNDRJ2CrISL1B.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ2CrISL1B+3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ2CrISL1B+3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS2_Sounder_Level1/SNDRJ2CrISL1B.3/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS2_Sounder_Level1/SNDRJ2CrISL1B.3/",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SNDRJ2CrISL1B.v3.README.pdf",
-                    "description": "NASA J2 Cross Track Infrared Sounder (CrIS) Level 1B version 3 Beta Data Users\u2019 Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NASA J2 Cross Track Infrared Sounder (CrIS) Level 1B version 3 Beta Data Users\u2019 Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SNDRJ2CrISL1B.v3.README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ2CrISL1B.v3.png",
+            "identifier": "C2758503590-GES_DISC",
+            "issued": "2023-02-22",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2758503590-GES_DISC.html",
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
+            "series-name": "SNDRJ2CrISL1B",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-02-22T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "JPSS-2 CrIS Level 1B Beta Full Spectral Resolution V3 (SNDRJ2CrISL1B) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD44B.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charlene DiMiceli, Robert Sohlberg, John Townshend. 2022-10-20. MODIS/Terra Vegetation Continuous Fields Yearly L3 Global 250m SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD44B.061. https://doi.org/10.5067/MODIS/MOD44B.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2022-10-20",
-            "temporal": "2000-03-05T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-20",
-            "keyword": [
-                "vegetation",
-                "earth science",
-                "land surface",
-                "land use/land cover",
-                "national geospatial data asset",
-                "ngda",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Charlene DiMiceli",
                 "hasEmail": "mailto:sohlberg@umd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2565805839-LPCLOUD",
-            "description": "The MOD44B Version 6.1 Vegetation Continuous Fields (VCF) yearly product is a global representation of surface vegetation cover as gradations of three ground cover components: percent tree cover, percent non-tree cover, and percent non-vegetated (bare). VCF products provide a continuous, quantitative portrayal of land surface cover at 250 meter (m) pixel resolution, with a sub-pixel depiction of percent cover in reference to the three ground cover components. The sub-pixel mixture of ground cover estimates represents a revolutionary approach to the characterization of vegetative land cover that can be used to enhance inputs to environmental modeling and monitoring applications. \n\nThe MOD44B data product layers include percent tree cover, percent non-tree cover, percent non-vegetated, cloud cover, and quality indicators. The start date of the annual period for this product begins with day of year (DOY) 65 (March 6 except for leap year which corresponds to March 5). \n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Charlene DiMiceli, Robert Sohlberg, John Townshend",
-            "title": "MODIS/Terra Vegetation Continuous Fields Yearly L3 Global 250m SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2675567828-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MOD44B Version 6.1 Vegetation Continuous Fields (VCF) yearly product is a global representation of surface vegetation cover as gradations of three ground cover components: percent tree cover, percent non-tree cover, and percent non-vegetated (bare). VCF products provide a continuous, quantitative portrayal of land surface cover at 250 meter (m) pixel resolution, with a sub-pixel depiction of percent cover in reference to the three ground cover components. The sub-pixel mixture of ground cover estimates represents a revolutionary approach to the characterization of vegetative land cover that can be used to enhance inputs to environmental modeling and monitoring applications. \n\nThe MOD44B data product layers include percent tree cover, percent non-tree cover, percent non-vegetated, cloud cover, and quality indicators. The start date of the annual period for this product begins with day of year (DOY) 65 (March 6 except for leap year which corresponds to March 5). \n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD44B.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD44B.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD44B.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD44B.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565805839-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565805839-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD44B.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD44B.061",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1494/MOD44B_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1494/MOD44B_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/113/MOD44B_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/113/MOD44B_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MOD44B",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MOD44B",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 3 has been achieved for the MODIS Vegetation Continuous Fields data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the MODIS Vegetation Continuous Fields data product.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD44",
-                    "description": "Further details regarding MODIS land product validation for the MOD44 data are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MOD44 data are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD44",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2675567828-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2675567828-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
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
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2675567828-LPCLOUD?h=85&w=85",
+            "identifier": "C2565805839-LPCLOUD",
+            "issued": "2022-10-20",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "land surface",
+                "land use/land cover",
+                "national geospatial data asset",
+                "ngda",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD44B.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-05T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Vegetation Continuous Fields Yearly L3 Global 250m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-SS-MAG-4-SUMM-CRUISE-RTN-V1.0",
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
-                "solar system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains data acquired by the Galileo Magnetometer during the Interplanetary Cruise to Jupiter. The data are at varying resolution depending on the averaging constant applied to the instrument. The EDR files are given in IBM 370 binary representation and are stored in an extremely compact format.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-ss-mag-4-summ-cruise-rtn-v1.0_5phs-nsz8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-SS-MAG-4-SUMM-CRUISE-RTN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-ss-mag-4-summ-cruise-rtn-v1.0_5phs-nsz8",
-            "description": "This dataset contains data acquired by the Galileo Magnetometer during the Interplanetary Cruise to Jupiter. The data are at varying resolution depending on the averaging constant applied to the instrument. The EDR files are given in IBM 370 binary representation and are stored in an extremely compact format.",
-            "title": "GALILEO MAGNETOMETER CRUISE DATA (RTN COORDINATES)",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO MAGNETOMETER CRUISE DATA (RTN COORDINATES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PAL200-SR-CIRC-4-OCC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pal200-sr-circ-4-occ-v1.0_5pku-3zq4",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "s rings",
                 "saturn occultation of 28 sagittarius 1989",
                 "saturn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PAL200-SR-CIRC-4-OCC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pal200-sr-circ-4-occ-v1.0_5pku-3zq4",
-            "description": "not applicable",
-            "title": "PAL200 SR CASS-IR-CAM RESAMPLED RING OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PAL200 SR CASS-IR-CAM RESAMPLED RING OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC1-67PCHURYUMOV-M11-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-12-19 to 2015-01-13.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc1-67pchuryumov-m11-v1.0_5ps6-egwb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC1-67PCHURYUMOV-M11-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc1-67pchuryumov-m11-v1.0_5ps6-egwb",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-12-19 to 2015-01-13.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 3 RDR MTP 011 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 3 RDR MTP 011 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/8AE2ILXB5SM6",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/AMSR2 Unified L3 Global Daily 25 km EASE-Grid Snow Water Equivalent V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/8AE2ILXB5SM6.",
-            "issued": "2012-07-02",
-            "temporal": "2012-07-02T00:00:00Z/2024-12-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-09",
-            "keyword": [
-                "terrestrial hydrosphere",
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
-            "identifier": "C1601063219-NSIDC_ECS",
             "description": "This AMSR-E/AMSR2 Unified Level-3 (L3) data set provides daily estimates of Snow Water Equivalent (SWE). SWE was derived from brightness temperature measurements acquired by the Advanced Microwave Scanning Radiometer 2 (AMSR2) instrument on board the JAXA GCOM-W1 satellite. \n\nThe SWE data is rendered to an azimuthal 25 km Equal-Area Scalable Earth Grid (EASE-Grid) for both the Northern and Southern Hemisphere.\n\nNote: This data set uses JAXA AMSR2 Level-1R (L1R) input brightness temperatures that are calibrated, or unified, across the JAXA AMSR-E and JAXA AMSR2 L1R products.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "AMSR-E/AMSR2 Unified L3 Global Daily 25 km EASE-Grid Snow Water Equivalent V001",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-240,-110,192,106&l=Coastlines_15m,AMSRU2_Snow_Water_Equivalent_Daily,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8AE2ILXB5SM6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8AE2ILXB5SM6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AU_DySno.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AU_DySno.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AU_DySno+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AU_DySno+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AU_DySno/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AU_DySno/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-240%2C-110%2C192%2C106&l=Coastlines_15m%2CAMSRU2_Snow_Water_Equivalent_Daily%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-240%2C-110%2C192%2C106&l=Coastlines_15m%2CAMSRU2_Snow_Water_Equivalent_Daily%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8AE2ILXB5SM6",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/8AE2ILXB5SM6",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8AE2ILXB5SM6",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/8AE2ILXB5SM6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-240,-110,192,106&l=Coastlines_15m,AMSRU2_Snow_Water_Equivalent_Daily,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C1601063219-NSIDC_ECS",
+            "issued": "2012-07-02",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/8AE2ILXB5SM6",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-07-02T00:00:00Z/2024-12-16T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/AMSR2 Unified L3 Global Daily 25 km EASE-Grid Snow Water Equivalent V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/GAUGE/DATA202",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A, David  Wolff, Jianxin  Wang and Ali  Tokay.2016. GPM GROUND VALIDATION RAIN GAUGE PAIRS MC3E V2 [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/MC3E/GAUGE/DATA202",
-            "issued": "2016-07-28",
-            "temporal": "2011-04-22T00:45:00Z/2011-06-06T14:56:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "atmosphere",
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
-            "identifier": "C1979700643-GHRC_DAAC",
             "description": "The GPM Ground Validation Rain Gauge Pairs MC3E V2 data measures the amount of fallen precipitation collected by tipping bucket rain gauges made by Met One Instruments, Inc. and Campbell Scientific Corp.  Precipitation from each is collected to a resolution of 0.254 mm of liquid water for each bucket tip. These gauges record the rainfall at a 1-minute resolution. This data set has two types of files, the recorded rainfall value (mm) and a cubic-spline interpolated rain rate (mm/hr) produced using the method described in Wang, 2008. There are two rain gauges located on each station (A or B), each with their own set of data files. Data were collected from April 2011 through June 2011 as part of the GPM Ground Validation Mid-latitude Continental Convective Cloud Experiment (MC3E). Detailed information about the Met One Model 380 Precipitation Gauge is available at http://www.metone.com/docs/370_380_precipitation_gauge.pdf. Details about the Campbell Scientific rain gauge is found at https://s.campbellsci.com/documents/us/product-brochures/b_385.pdf.",
-            "title": "GPM GROUND VALIDATION RAIN GAUGE PAIRS MC3E V2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FGAUGE%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FGAUGE%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmrgnamc3e2",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmrgnamc3e2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://pmm.nasa.gov/GPM",
-                    "description": "GPM Mission Concept",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Mission Concept",
+                    "downloadURL": "http://pmm.nasa.gov/GPM",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/disdrometers_and_gauges/rain_gauge/doc/gpmrgnamc3e2_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/disdrometers_and_gauges/rain_gauge/doc/gpmrgnamc3e2_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/disdrometers_and_gauges/rain_gauge/doc/README_MC3E_APU-NASA_GMIN_v2.txt",
-                    "description": "Data format NASA MC3E Rain Gauge V2 GMIN files",
                     "@type": "dcat:Distribution",
+                    "description": "Data format NASA MC3E Rain Gauge V2 GMIN files",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/disdrometers_and_gauges/rain_gauge/doc/README_MC3E_APU-NASA_GMIN_v2.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/disdrometers_and_gauges/rain_gauge/doc/README_MC3E_APU-NASA_GAG_v2.txt",
-                    "description": "Data format NASA MC3E Rain Gauge V2 Gauge files",
                     "@type": "dcat:Distribution",
+                    "description": "Data format NASA MC3E Rain Gauge V2 Gauge files",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/disdrometers_and_gauges/rain_gauge/doc/README_MC3E_APU-NASA_GAG_v2.txt",
+                    "mediaType": "text/html",
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
+            "identifier": "C1979700643-GHRC_DAAC",
+            "issued": "2016-07-28",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/GAUGE/DATA202",
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
             "spatial": "-97.5515 36.5644 -97.4261 36.6381",
+            "temporal": "2011-04-22T00:45:00Z/2011-06-06T14:56:00Z",
             "theme": [
                 "MC3E",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION RAIN GAUGE PAIRS MC3E V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC2-67PCHURYUMOV-M14-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-03-10 to 2015-04-08.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc2-67pchuryumov-m14-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC2-67PCHURYUMOV-M14-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc2-67pchuryumov-m14-v1.0",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-03-10 to 2015-04-08.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 2 EDR MTP 014 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 2 EDR MTP 014 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/5pvz-kbwd",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2019-03-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-15",
-            "keyword": [
-                "turbulent boundary layer"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Albert Allen",
                 "hasEmail": "mailto:albert.r.allen@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Albert Allen"
-            },
-            "identifier": "https://data.nasa.gov/api/views/5pvz-kbwd",
             "description": "Wall pressure data acquired during flight tests at three flight conditions are provided: 48k feet altitude at Mach 0.86; 32k feet at Mach 0.70; and 24k feet at Mach 0.56. Details of the flight test, sensors, and sensor locations are given in a journal article that is referenced in the supporting documents datafile.",
-            "title": "Turbulent boundary layer wall pressure flight data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -203329,840 +203313,812 @@
                     "title": "B109_pt_10"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/5pvz-kbwd",
+            "issued": "2019-03-04",
+            "keyword": [
+                "turbulent boundary layer"
+            ],
+            "landingPage": "https://data.nasa.gov/d/5pvz-kbwd",
+            "modified": "2024-05-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Albert Allen"
+            },
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulent boundary layer wall pressure flight data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/418",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Zobler, L. 1999. Global Soil Types, 1-Degree Grid (Zobler). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/418",
-            "issued": "2024-04-30",
-            "temporal": "1972-01-01T00:00:00Z/1982-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "erosion/sedimentation",
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
-            "identifier": "C2216862716-ORNL_CLOUD",
             "description": "A global digital data base of soil properties is available at 1 degree longitude resolution.  For each land cell, the data base includes major and associated soil units, surface texture, and slope; phase and miscellaneous land units are included where available. The data base was compiled as part of an effort to improve modeling of the hydrologic cycle in the GISS Genreal Circulation Model.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Global Soil Types, 1-Degree Grid (Zobler)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/418_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F418",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F418",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_soil/ZoblerSoil/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_soil/ZoblerSoil/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/ZoblerSoil.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/ZoblerSoil.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/418",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/418",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/NASATM100685.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/NASATM100685.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/readme2.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/readme2.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/README_images",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/README_images",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/soil1x1.help",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/soil1x1.help",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/zobler1x1.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/zobler1x1.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/ZoblerSoil.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/ZoblerSoil.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/Zobler_NASA_TM_87802_1986.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/ZoblerSoil/comp/Zobler_NASA_TM_87802_1986.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/418_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/418_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=418",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=418",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/418_1_fit.png",
+            "identifier": "C2216862716-ORNL_CLOUD",
+            "issued": "2024-04-30",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "erosion/sedimentation",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/418",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1972-01-01T00:00:00Z/1982-01-01T23:59:59Z",
             "theme": [
                 "Soil",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Soil Types, 1-Degree Grid (Zobler)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEaSUREs/GLDTA/XAERDT_L2_ABI_G17.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2024-02-21. ABI/GOES-17 Dark Target Aerosol 10-Min L2 Full Disk 10 km. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MEaSUREs/GLDTA/XAERDT_L2_ABI_G17.001. https://doi.org/10.5067/MEaSUREs/GLDTA/XAERDT_L2_ABI_G17.001.",
-            "issued": "2023-09-05",
-            "temporal": "2019-01-01T00:00:00Z/2023-01-02T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-01",
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
-            "identifier": "C2859265967-LAADS",
-            "description": "The ABI/GOES-17 Dark Target Aerosol 10-Min L2 Full Disk 10 km product, short-name XAERDT_L2_ABI_G17 is provided at 10-km spatial resolution (at-nadir) and a 10-minute full-disk cadence that typically yields about 144 granules over the daylit hours of a 24-hour period.  The Geostationary Operational Environmental Satellite \u2013 GOES-17 served in the operational GOES-West position (near -137\u00b0W), from February 12, 2019, through January 4, 2023.  The GOES-16/ABI collection record spans from January 2019 through December 2022.\r\n\r\nThe XAERDT_L2_ABI_G17 product is a part of the Geostationary Earth Orbit (GEO)\u2013Low-Earth Orbit (LEO) Dark Target Aerosol project under NASA\u2019s Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, led by Robert Levy, uses a special version of the MODIS Dark Target (DT) aerosol retrieval algorithm to produce Aerosol Optical Depth (AOD) and other aerosol parameters derived independently from seven sensor/platform combinations, where 3 are in GEO and 4 are in LEO.  The 3 GEO sensors include Advanced Baseline Imagers (ABI) on both GOES-16 (GOES-East) and GOES-17 (GOES-West), and Advanced Himawari Imager (AHI) on Himawari-8. The 4 LEO sensors include MODIS on both Terra and Aqua, and VIIRS on both Suomi-NPP and NOAA-20.  Adding the LEO sensors reinforces a major goal of this project, which is to render a consistent science maturity level across DT aerosol products derived from both types and sources of orbital satellites.\r\n\r\nThe XAERDT_L2_ABI_G17 product, in netCDF4 format, contains 45 Science Data Set (SDS) layers that include 8 geolocation and 37 geophysical SDSs.\r\n\r\nFor more information consult LAADS product description page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/XAERDT_L2_ABI_G17\r\n\r\nOr, Dark Target aerosol team Page at: \r\nhttps://darktarget.gsfc.nasa.gov/",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "ABI/GOES-17 Dark Target Aerosol 10-Min L2 Full Disk 10 km",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ABI/GOES-17 Dark Target Aerosol 10-Min L2 Full Disk 10 km product, short-name XAERDT_L2_ABI_G17 is provided at 10-km spatial resolution (at-nadir) and a 10-minute full-disk cadence that typically yields about 144 granules over the daylit hours of a 24-hour period.  The Geostationary Operational Environmental Satellite \u2013 GOES-17 served in the operational GOES-West position (near -137\u00b0W), from February 12, 2019, through January 4, 2023.  The GOES-16/ABI collection record spans from January 2019 through December 2022.\r\n\r\nThe XAERDT_L2_ABI_G17 product is a part of the Geostationary Earth Orbit (GEO)\u2013Low-Earth Orbit (LEO) Dark Target Aerosol project under NASA\u2019s Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, led by Robert Levy, uses a special version of the MODIS Dark Target (DT) aerosol retrieval algorithm to produce Aerosol Optical Depth (AOD) and other aerosol parameters derived independently from seven sensor/platform combinations, where 3 are in GEO and 4 are in LEO.  The 3 GEO sensors include Advanced Baseline Imagers (ABI) on both GOES-16 (GOES-East) and GOES-17 (GOES-West), and Advanced Himawari Imager (AHI) on Himawari-8. The 4 LEO sensors include MODIS on both Terra and Aqua, and VIIRS on both Suomi-NPP and NOAA-20.  Adding the LEO sensors reinforces a major goal of this project, which is to render a consistent science maturity level across DT aerosol products derived from both types and sources of orbital satellites.\r\n\r\nThe XAERDT_L2_ABI_G17 product, in netCDF4 format, contains 45 Science Data Set (SDS) layers that include 8 geolocation and 37 geophysical SDSs.\r\n\r\nFor more information consult LAADS product description page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/XAERDT_L2_ABI_G17\r\n\r\nOr, Dark Target aerosol team Page at: \r\nhttps://darktarget.gsfc.nasa.gov/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEaSUREs%2FGLDTA%2FXAERDT_L2_ABI_G17.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEaSUREs%2FGLDTA%2FXAERDT_L2_ABI_G17.001",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/XAERDT_L2_ABI_G17--5019",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/XAERDT_L2_ABI_G17--5019",
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
+            "identifier": "C2859265967-LAADS",
+            "issued": "2023-09-05",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEaSUREs/GLDTA/XAERDT_L2_ABI_G17.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-01-01T00:00:00Z/2023-01-02T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "GOES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABI/GOES-17 Dark Target Aerosol 10-Min L2 Full Disk 10 km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/548",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Webb, R., C.E. Rosenzweig, and E.R. Levine. 2000. Global Soil Texture and Derived Water-Holding Capacities (Webb et al.). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/548",
-            "issued": "2022-02-13",
-            "temporal": "1950-01-01T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
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
-            "identifier": "C2216863033-ORNL_CLOUD",
             "description": "A standardized global data set of soil horizon thicknesses and textures (particle size distributions).",
-            "graphic-preview-description": "Browse Image",
-            "title": "Global Soil Texture and Derived Water-Holding Capacities (Webb et al.)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/548_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F548",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F548",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_soil/WebbRosenzweig/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_soil/WebbRosenzweig/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/WebbRosenzweig.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/WebbRosenzweig.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/548",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/548",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/readme2.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/readme2.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/WebbRosenzweig.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/WebbRosenzweig.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/zcontinent.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/zcontinent.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/zobler_106.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/WebbRosenzweig/comp/zobler_106.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/548_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/548_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=548",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=548",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/548_1_fit.png",
+            "identifier": "C2216863033-ORNL_CLOUD",
+            "issued": "2022-02-13",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/548",
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
+            "temporal": "1950-01-01T00:00:00Z/1996-12-31T23:59:59Z",
             "theme": [
                 "Soil",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Soil Texture and Derived Water-Holding Capacities (Webb et al.)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-EAR2-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the EAR2 phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-ear2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-EAR2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-ear2-v1.0",
-            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the EAR2 phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 EAR2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 EAR2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/105/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Santanu Das",
+                "hasEmail": "mailto:Santanu.Das-1@nasa.gov"
+            },
+            "description": "Paper on this topic has been submitted to KDD 2010.",
+            "identifier": "DASHLINK_105",
             "issued": "2010-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "nasa",
                 "dashlink",
                 "ames"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Santanu Das",
-                "hasEmail": "mailto:Santanu.Das-1@nasa.gov"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/105/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_105",
-            "description": "Paper on this topic has been submitted to KDD 2010.",
-            "title": "Multiple Kernel Learning based Heterogeneous Algorithm",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Multiple Kernel Learning based Heterogeneous Algorithm"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-EAR1-EARTHSWINGBY1-V1.0",
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
-                "unknown"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This volume contains Experiment Data acquired by GIADA during 'Earth swing-by 1' phase. More in detail it refers to the data provided during the following in-flight tests: 'Passive Payload Checkout n. 0' (PC0) held on 28/29-03-2005. It also contains documentation which describes the GIADA experiment. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-ear1-earthswingby1-v1.0_5q76-4a44",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-EAR1-EARTHSWINGBY1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-ear1-earthswingby1-v1.0_5q76-4a44",
-            "description": "This volume contains Experiment Data acquired by GIADA during 'Earth swing-by 1' phase. More in detail it refers to the data provided during the following in-flight tests: 'Passive Payload Checkout n. 0' (PC0) held on 28/29-03-2005. It also contains documentation which describes the GIADA experiment. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
-            "title": "ROSETTA-ORBITER CHECK GIADA 2 EAR1 EARTHSWINGBY1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CHECK GIADA 2 EAR1 EARTHSWINGBY1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/4SI45J6G6BW5",
             "citation": "GES DISC Northern Eurasian Earth Science Partnership Initiative Project. 2001-01-01. MOD11CM1D. Version 005. MODIS/Terra Monthly mean Day-Time Land Surface Temperature at 1x1 degree V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/4SI45J6G6BW5. https://disc.gsfc.nasa.gov/datacollection/MOD11CM1D_005.html. Digital Science Data.",
-            "issued": "2009-03-10",
-            "temporal": "2000-03-01T00:00:00Z/2015-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-06-30",
-            "keyword": [
-                "national geospatial data asset",
-                "land surface",
-                "earth science",
-                "ngda",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PETER ROMANOV, PHD",
                 "hasEmail": "mailto:Peter.Romanov@noaa.gov"
             },
+            "creator": "GES DISC Northern Eurasian Earth Science Partnership Initiative Project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239897978-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The dataset contains global monthly day-time land surface temperature averaged within 1 by 1 degree grid cells. The source for the data is MODIS/Terra MOD11C3 Collection 005 product (MODIS/Terra Monthly mean land surface temperature at 0.05 degree spatial resolution). The dataset covers the time period from 2000-03-01 to 2015-06-30.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MOD11CM1D",
-            "creator": "GES DISC Northern Eurasian Earth Science Partnership Initiative Project",
-            "title": "MODIS/Terra Monthly mean Day-Time Land Surface Temperature at 1x1 degree V005 (MOD11CM1D) at GES DISC",
-            "graphic-preview-description": "Sample image of MODIS-Terra global monthly daytime land surface temperature at 1x1 degree, July 2010",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MOD11CM1D_005.gif",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4SI45J6G6BW5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4SI45J6G6BW5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MOD11CM1D_005.gif",
-                    "description": "Sample image of MODIS-Terra global monthly daytime land surface temperature at 1x1 degree, July 2010",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image of MODIS-Terra global monthly daytime land surface temperature at 1x1 degree, July 2010",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MOD11CM1D_005.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MOD11CM1D_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MOD11CM1D_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Land_Surface_Temperature/MOD11CM1D.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Land_Surface_Temperature/MOD11CM1D.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Land_Surface_Temperature/MOD11CM1D.005/doc/README.MODIS_LST_1deg.005.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Land_Surface_Temperature/MOD11CM1D.005/doc/README.MODIS_LST_1deg.005.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/",
-                    "description": "MODIS Land Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Land Homepage",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample image of MODIS-Terra global monthly daytime land surface temperature at 1x1 degree, July 2010",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MOD11CM1D_005.gif",
+            "identifier": "C1239897978-GES_DISC",
+            "issued": "2009-03-10",
+            "keyword": [
+                "national geospatial data asset",
+                "land surface",
+                "earth science",
+                "ngda",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/4SI45J6G6BW5",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "MOD11CM1D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-01T00:00:00Z/2015-06-30T23:59:59.999Z",
             "theme": [
                 "NEESPI NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Monthly mean Day-Time Land Surface Temperature at 1x1 degree V005 (MOD11CM1D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/21N0ODR2Y2S8",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRNO26H3D. Version 1. TROPESS Chemical Reanalysis NO2 6-Hourly 3-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/21N0ODR2Y2S8. https://disc.gsfc.nasa.gov/datacollection/TRPSCRNO26H3D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
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
-            "identifier": "C2837624929-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis NO2 6-Hourly 3-dimensional Product contains vertical concentrations of nitrogen dioxide. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at 6-hourly resolution, and a spatial resolution of 1.125 x 1.125 degrees at 27 pressure levels between 1000 and 60 hPa. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRNO26H3D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis NO2 6-Hourly 3-dimensional Product V1 (TRPSCRNO26H3D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRNO26H3D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F21N0ODR2Y2S8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F21N0ODR2Y2S8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRNO26H3D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRNO26H3D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRNO26H3D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRNO26H3D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRNO26H3D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRNO26H3D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRNO26H3D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRNO26H3D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_6HR_VERTCONCS/TRPSCRNO26H3D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_6HR_VERTCONCS/TRPSCRNO26H3D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRNO26H3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRNO26H3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRNO26H3D_Sample.png",
+            "identifier": "C2837624929-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/21N0ODR2Y2S8",
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
+            "series-name": "TRPSCRNO26H3D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis NO2 6-Hourly 3-dimensional Product V1 (TRPSCRNO26H3D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYDCSR_B.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Aqua 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MYDCSR_B.061. https://doi.org/10.5067/MODIS/MYDCSR_B.061.",
-            "issued": "2017-10-01",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "microwave",
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
-            "identifier": "C1444160046-LAADS",
-            "description": "The MODIS/Aqua 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands (MYDCSR_B) product consists of 1-degree zonal mean clear-sky biases (observed minus calculated radiance differences) and associated statistics for bands 31 and 33-36 for each day from the previous eight-day period. Zonal means (5-zone moving averages) are created from the eight-day, 25-km radiance differences for daytime land, nighttime land, and ocean data separately. Day and night land data are combined south of -60 degrees latitude due to poor clear-sky sampling and the difficulty of discriminating between clear and cloudy conditions in this region. The zonal mean biases are utilized to correct clear-sky radiance calculations in the cloud top pressure (CO2 slicing) algorithm. The files are in Hierarchical Data Format (HDF).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands (MYDCSR_B) product consists of 1-degree zonal mean clear-sky biases (observed minus calculated radiance differences) and associated statistics for bands 31 and 33-36 for each day from the previous eight-day period. Zonal means (5-zone moving averages) are created from the eight-day, 25-km radiance differences for daytime land, nighttime land, and ocean data separately. Day and night land data are combined south of -60 degrees latitude due to poor clear-sky sampling and the difficulty of discriminating between clear and cloudy conditions in this region. The zonal mean biases are utilized to correct clear-sky radiance calculations in the cloud top pressure (CO2 slicing) algorithm. The files are in Hierarchical Data Format (HDF).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDCSR_B.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDCSR_B.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDCSR_B.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDCSR_B.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDCSR_B--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDCSR_B--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDCSR_B/",
-                    "description": "Direct access to MYDCSR_B C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MYDCSR_B C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDCSR_B/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDCSR_B/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDCSR_B/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1444160046-LAADS",
+            "issued": "2017-10-01",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "microwave",
+                "ultraviolet wavelengths",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYDCSR_B.061",
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
+            "title": "MODIS/Aqua 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MAG-1-PREMAP%2FHIGHRES-FLUX-V1.0",
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
+            "description": "This data set contains vector magnetic field data acquired by the Fluxgate section of the Magnetometer / Electron Reflectometer instrument aboard the Mars Global Surveyor (MGS) spacecraft. The data are provided at a variable time resolution depending on the telemetry rate available to the investigation for the time period beginning with Aerobraking Phase 1A (1997-09-12). The data in the dataset cover the entire premapping period (ends 1999-03-08).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mag-1-premap-highres-flux-v1.0_5qck-6y8e",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MAG-1-PREMAP%2FHIGHRES-FLUX-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mag-1-premap-highres-flux-v1.0_5qck-6y8e",
-            "description": "This data set contains vector magnetic field data acquired by the Fluxgate section of the Magnetometer / Electron Reflectometer instrument aboard the Mars Global Surveyor (MGS) spacecraft. The data are provided at a variable time resolution depending on the telemetry rate available to the investigation for the time period beginning with Aerobraking Phase 1A (1997-09-12). The data in the dataset cover the entire premapping period (ends 1999-03-08).",
-            "title": "MGS MARS MAG PRE-MAP DETAIL WORD RESOLUTION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS MARS MAG PRE-MAP DETAIL WORD RESOLUTION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA202",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-01-15. AIRS2RET. Version 006. AIRS/Aqua L2 Standard Physical Retrieval (AIRS-only) V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA202. https://disc.gsfc.nasa.gov/datacollection/AIRS2RET_006.html. Digital Science Data.",
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
-                "clouds",
-                "atmosphere",
-                "atmospheric water vapor",
-                "land surface",
-                "altitude",
-                "air quality",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "surface thermal properties",
-                "surface radiative properties",
-                "ocean temperature",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1243477381-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. This product is similar to AIRX2RET. It is a new product produced using AIRS IR only because the radiometric noise in AMSU channel 4 started to increase significantly (since June 2007). The AIRS Standard Retrieval Product consists of retrieved estimates of cloud and surface properties, plus profiles of retrieved temperature, water vapor, ozone, carbon monoxide and methane. Estimates of the errors associated with these quantities is also part of the Standard Product. The temperature profile vertical resolution is 28 levels total between 1100 mb and 0.1 mb, while moisture profile is reported at 14 atmospheric layers between 1100 mb and 50 mb. The horizontal resolution is 50 km. An AIRS granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240\ngranules per day, with an orbit repeat cycle of approximately 16 day.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS2RET",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "title": "AIRS/Aqua L2 Standard Physical Retrieval (AIRS-only) V006 (AIRS2RET) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2RET_006.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -204172,1393 +204128,1447 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2RET_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2RET_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRS2RET.006/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRS2RET.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRS2RET.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRS2RET.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2RET+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2RET+006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
-                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument,algorithms, and other AIRS-related activities can be found.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument,algorithms, and other AIRS-related activities can be found.",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2RET_006.jpeg",
+            "identifier": "C1243477381-GES_DISC",
+            "issued": "2002-08-30",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "atmospheric water vapor",
+                "land surface",
+                "altitude",
+                "air quality",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "surface thermal properties",
+                "surface radiative properties",
+                "ocean temperature",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA202",
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
+            "series-name": "AIRS2RET",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L2 Standard Physical Retrieval (AIRS-only) V006 (AIRS2RET) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNN-22512",
             "citation": "NOAA/NESDIS/STAR/SOCD. 2022-06-02. NOAA CYGNSS Level 2 Science Wind Speed 25-km. Version 1.2. NOAA CYGNSS Level 2 Science Wind Speed 25-km Product Version 1.2. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNN-22512. https://manati.star.nesdis.noaa.gov/products/CYGNSS.php. NOAA/NESDIS/STAR/SOCD, PO.DAAC, 2022-06-02, NOAA CYGNSS Level 2 Science Wind Speed 25-km Product Version 1.2, https://manati.star.nesdis.noaa.gov/products/CYGNSS.php.",
-            "issued": "2022-03-28",
-            "temporal": "2017-05-01T00:00:02Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-28",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2021.3087426"
-            ],
-            "keyword": [
-                "oceans",
-                "spectral/engineering",
-                "earth science",
-                "radar",
-                "ocean winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2254232941-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset contains the Version 1.2 NOAA CYGNSS Level 2 Science Wind Speed Product Version 1.2 which provides the time-tagged and geolocated average wind speed (m/s) in 25x25 kilometer grid cells along the measurement tracks from the Delay Doppler Mapping Instrument (DDMI) aboard the CYGNSS satellite constellation. This version corresponds to the second science-quality released through the PO.DAAC, as produced by NOAA/NESDIS using a specific geophysical model function (GMF version 1.0) and a track-wise debiasing algorithm as part of the wind speed retrieval process. The reported retrieval locations are determined by averaging the specular point locations falling within each 25 km grid cell. Version 1.2 includes four major updates compared to Version 1.1 ( https://doi.org/10.5067/CYGNN-22511 ), namely: 1) the inclusion of data associated to a spacecraft roll angle exceeding +/- 5 degrees; 2) an improved wind speed performance in the higher wind speed regime; 3) a full revision of the quality flags; 4) the inclusion of a wind speed retrieval error variable. Only one netCDF-4 data file is produced for each day (each file containing data from up to 8 unique CYGNSS spacecraft) with a latency of approximately 6 days (or better) from the last recorded measurement time. Formatting of the data variables and metadata designed to be consistent with the netCDF-4 formatting provided by the legacy CYGNSS mission Level 2 wind speed science data record (SDR).",
-            "release-place": "PO.DAAC",
-            "series-name": "NOAA CYGNSS Level 2 Science Wind Speed 25-km",
             "creator": "NOAA/NESDIS/STAR/SOCD",
-            "title": "NOAA CYGNSS Level 2 Science Wind Speed 25-km Product Version 1.2",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_NOAA_L2_SWSP_25KM_V1.2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the Version 1.2 NOAA CYGNSS Level 2 Science Wind Speed Product Version 1.2 which provides the time-tagged and geolocated average wind speed (m/s) in 25x25 kilometer grid cells along the measurement tracks from the Delay Doppler Mapping Instrument (DDMI) aboard the CYGNSS satellite constellation. This version corresponds to the second science-quality released through the PO.DAAC, as produced by NOAA/NESDIS using a specific geophysical model function (GMF version 1.0) and a track-wise debiasing algorithm as part of the wind speed retrieval process. The reported retrieval locations are determined by averaging the specular point locations falling within each 25 km grid cell. Version 1.2 includes four major updates compared to Version 1.1 ( https://doi.org/10.5067/CYGNN-22511 ), namely: 1) the inclusion of data associated to a spacecraft roll angle exceeding +/- 5 degrees; 2) an improved wind speed performance in the higher wind speed regime; 3) a full revision of the quality flags; 4) the inclusion of a wind speed retrieval error variable. Only one netCDF-4 data file is produced for each day (each file containing data from up to 8 unique CYGNSS spacecraft) with a latency of approximately 6 days (or better) from the last recorded measurement time. Formatting of the data variables and metadata designed to be consistent with the netCDF-4 formatting provided by the legacy CYGNSS mission Level 2 wind speed science data record (SDR).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNN-22512",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNN-22512",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
-                    "description": "Ruf, C., Asharaf, S., Balasubramaniam, R., Gleason, S., Lang, T., McKague, D., Twigg, D., and Waliser, D.. 2019. In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., Asharaf, S., Balasubramaniam, R., Gleason, S., Lang, T., McKague, D., Twigg, D., and Waliser, D.. 2019. In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://manati.star.nesdis.noaa.gov/products/CYGNSS.php",
-                    "description": "CYGNSS data documentation and references provided and hosted by NOAA/NESDIS/STAR.",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS data documentation and references provided and hosted by NOAA/NESDIS/STAR.",
+                    "downloadURL": "https://manati.star.nesdis.noaa.gov/products/CYGNSS.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_NOAA_L2_SWSP_25KM_V1.2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_NOAA_L2_SWSP_25KM_V1.2.jpg",
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
-                    "downloadURL": "https://doi.org/10.1109/IGARSS.2019.8898099",
-                    "description": "Said, F., Jelenak, Z., Park, J., Soisuvarn, S., and Chang, P. S.. 2019. A Track-Wise Wind Retrieval Algorithm for the CYGNSS Mission. IGARSS 2019 - 2019 IEEE International Geoscience and Remote Sensing Symposium, Yokohama, Japan. pp. 8711-8714. doi: 10.1109/IGARSS.2019.8898099",
                     "@type": "dcat:Distribution",
+                    "description": "Said, F., Jelenak, Z., Park, J., Soisuvarn, S., and Chang, P. S.. 2019. A Track-Wise Wind Retrieval Algorithm for the CYGNSS Mission. IGARSS 2019 - 2019 IEEE International Geoscience and Remote Sensing Symposium, Yokohama, Japan. pp. 8711-8714. doi: 10.1109/IGARSS.2019.8898099",
+                    "downloadURL": "https://doi.org/10.1109/IGARSS.2019.8898099",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00218.1",
-                    "description": "Ruf, C., Atlas, R., Chang, P., Clarizia, M., Garrison, J. Gleason, S., Katzberg, S., Jelenak, Z., Johnson, J., Majumdar, S., O'Brien, A., Posselt, D., Ridley, A., Rose, R., and Zavorotny, V.. 2015. New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., Atlas, R., Chang, P., Clarizia, M., Garrison, J. Gleason, S., Katzberg, S., Jelenak, Z., Johnson, J., Majumdar, S., O'Brien, A., Posselt, D., Ridley, A., Rose, R., and Zavorotny, V.. 2015. New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00218.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/basic_user_guide_noaa_l2_wind_v1.1.pdf",
-                    "description": "User Guide Compiled by the OSWT at NOAA-NESDIS-STAR",
                     "@type": "dcat:Distribution",
+                    "description": "User Guide Compiled by the OSWT at NOAA-NESDIS-STAR",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/basic_user_guide_noaa_l2_wind_v1.1.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2254232941-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2254232941-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254232941-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254232941-POCLOUD",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/atbd_noaa_l2_wind_v1.2_apr072022.pdf",
-                    "description": "Algorithm Theoretical Basis Document for the NOAA Level 2 CYGNSS Winds Datasets",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document for the NOAA Level 2 CYGNSS Winds Datasets",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/atbd_noaa_l2_wind_v1.2_apr072022.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/noaa/README.txt",
-                    "description": "README File",
                     "@type": "dcat:Distribution",
+                    "description": "README File",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/noaa/README.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2021.3087426",
-                    "description": "Sa\u00efd, F., Jelenak, Z., Park, J., and Chang, P. S.. 2021. The NOAA Track-Wise Wind Retrieval Algorithm and Product Assessment for CyGNSS. IEEE Transactions on Geoscience and Remote Sensing, vol. 60, pp. 1-24, Art no. 4202524, doi: 10.1109/TGRS.2021.3087426.",
                     "@type": "dcat:Distribution",
+                    "description": "Sa\u00efd, F., Jelenak, Z., Park, J., and Chang, P. S.. 2021. The NOAA Track-Wise Wind Retrieval Algorithm and Product Assessment for CyGNSS. IEEE Transactions on Geoscience and Remote Sensing, vol. 60, pp. 1-24, Art no. 4202524, doi: 10.1109/TGRS.2021.3087426.",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2021.3087426",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/GNSSR53802.2021.9617693",
-                    "description": "Sa\u00efd, F., Jelenak, Z., and Chang, P. S.. 2021. NOAA CYGNSS Wind Product: Recent Progress. 2021 IEEE Specialist Meeting on Reflectometry using GNSS and other Signals of Opportunity (GNSS+R), pp. 73-76, doi: 10.1109/GNSSR53802.2021.9617693.",
                     "@type": "dcat:Distribution",
+                    "description": "Sa\u00efd, F., Jelenak, Z., and Chang, P. S.. 2021. NOAA CYGNSS Wind Product: Recent Progress. 2021 IEEE Specialist Meeting on Reflectometry using GNSS and other Signals of Opportunity (GNSS+R), pp. 73-76, doi: 10.1109/GNSSR53802.2021.9617693.",
+                    "downloadURL": "https://doi.org/10.1109/GNSSR53802.2021.9617693",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_NOAA_L2_SWSP_25KM_V1.2.jpg",
+            "identifier": "C2254232941-POCLOUD",
+            "issued": "2022-03-28",
+            "keyword": [
+                "oceans",
+                "spectral/engineering",
+                "earth science",
+                "radar",
+                "ocean winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNN-22512",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1109/TGRS.2021.3087426"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "NOAA CYGNSS Level 2 Science Wind Speed 25-km",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "2017-05-01T00:00:02Z/2023-02-28T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA CYGNSS Level 2 Science Wind Speed 25-km Product Version 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L2/IOP/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/AQUA/MODIS/L2/IOP/2022.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "ngda",
-                "biosphere",
-                "national geospatial data asset",
-                "ecosystems",
-                "earth science"
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
-            "identifier": "C2330511303-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Regional Inherent Optical Properties (IOP) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL2%2FIOP%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL2%2FIOP%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/Aqua-MODIS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/Aqua-MODIS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L2/IOP/2022",
-                    "description": "MODIS-Aqua L2 Inherent Optical Properties (IOP) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L2 Inherent Optical Properties (IOP) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L2/IOP/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2330511303-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "ngda",
+                "biosphere",
+                "national geospatial data asset",
+                "ecosystems",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L2/IOP/2022",
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
+            "title": "Aqua MODIS Regional Inherent Optical Properties (IOP) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4ZK5DMF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Volcano Total Economic Loss Risk Deciles. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H4ZK5DMF. https://doi.org/10.7927/H4ZK5DMF.",
-            "issued": "2005-12-31",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4BR8Q45",
-                "https://doi.org/10.7927/H43B5X3R",
-                "https://doi.org/10.7927/H4736NT2"
-            ],
-            "keyword": [
-                "socioeconomics",
-                "natural hazards",
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
-            "identifier": "C179001793-SEDAC",
-            "description": "Global Volcano Total Economic Loss Risk Deciles is a 2.5 minute grid of global volcano total economic loss risks. First, subnational distributions of Gross Domestic Product (GDP) are computed using a two-fold process. Where applicable, the proportional contribution of subnational Units are determined following the methodology of Sachs et al. (2003) and these proportions are used against World Bank Development Indicators to determine a GDP value for the subnational Unit. Once a national GDP has been spatially stratified into the smallest administrative Units available, it is further distributed based upon Gridded Population of the World, Version 3 (GPWv3) population distributions. A per capita contribution value is determined for each Unit, and this value is multiplied by the population per grid cell. Once the GDP has been determined on a per grid cell basis, then the spatially variable loss rate as derived from EM-DAT historical records is used to determine the total economic loss posed to a grid cell by volcano hazards. The final surface does not present absolute values of total economic loss, but rather a relative decile (1-10) ranking of grid cells based upon the calculated economic loss risks. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank",
-            "title": "Global Volcano Total Economic Loss Risk Deciles",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Global Volcano Total Economic Loss Risk Deciles is a 2.5 minute grid of global volcano total economic loss risks. First, subnational distributions of Gross Domestic Product (GDP) are computed using a two-fold process. Where applicable, the proportional contribution of subnational Units are determined following the methodology of Sachs et al. (2003) and these proportions are used against World Bank Development Indicators to determine a GDP value for the subnational Unit. Once a national GDP has been spatially stratified into the smallest administrative Units available, it is further distributed based upon Gridded Population of the World, Version 3 (GPWv3) population distributions. A per capita contribution value is determined for each Unit, and this value is multiplied by the population per grid cell. Once the GDP has been determined on a per grid cell basis, then the spatially variable loss rate as derived from EM-DAT historical records is used to determine the total economic loss posed to a grid cell by volcano hazards. The final surface does not present absolute values of total economic loss, but rather a relative decile (1-10) ranking of grid cells based upon the calculated economic loss risks. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4ZK5DMF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4ZK5DMF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-volcano-total-economic-loss-risk-deciles/volcano-total-economic-loss-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-volcano-total-economic-loss-risk-deciles/volcano-total-economic-loss-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-total-economic-loss-risk-deciles/maps",
+            "identifier": "C179001793-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "socioeconomics",
+                "natural hazards",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4ZK5DMF",
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
+                "https://doi.org/10.7927/H4BR8Q45",
+                "https://doi.org/10.7927/H43B5X3R",
+                "https://doi.org/10.7927/H4736NT2"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 86.0",
+            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
             "theme": [
                 "NDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Volcano Total Economic Loss Risk Deciles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1720172416-GES_DISC.html",
             "citation": "NASA/GSFC. 2020-04-08. VISSRSMS1L1AOIPS. Version 001. VISSR/SMS-1 Level 1 Atmospheric and Oceanographic Image Processing System (AOIPS) Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/VISSRSMS1L1AOIPS_001.html. Digital Science Data.",
-            "issued": "2020-02-05",
-            "temporal": "1974-07-01T00:00:00Z/1979-04-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-18",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1720172416-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "VISSRSMS1L1AOIPS is the Visible Infrared Spin-Scan Radiometer (VISSR) Level 1 Atmospheric and Oceanographic Image Processing System (AOIPS) data product from the first Synchronous Meteorological Satellite (SMS-1). There are typically three data files for a scene of the Earth with radiances that were measured in the visible (0.55 to 0.70 micrometer) and/or IR (10.5 to 12.6 micrometer) wavelengths with a spatial resolution of 0.9 and 8 km, respectively. Files also include time, geolocation, orbit, attitude, and telemetry information. There are three types of data files in this product: one contains IR data, one contains the IR grid information (blank before 1974/10/29), and another contains VIS data. Each data file is structured with an AOIPS label, followed by an IPD label, and then an optional 8 telemetry records followed by a set of data records. Visible data are typically 3904 pixels by either 4000 or 2000 scan lines (5 or 2.5 minute scenes respectively). IR data are typically 976 pixels by either 500 or 250 scan lines (5 or 2.5 minute scenes respectively). A full scan of the Earth was made every 20 minutes.\n\nThe data were used to make 70mm film negatives and 9.5\u201d positive prints on a Dicomed Image Recording System.  Data for this product are available from 1974/07/01 through 1979/04/19 (with gaps plus no data between 1975/08/20 and 1979/02/17). The SMS-1 satellite was initially parked over the equator at longitude 45W on June 7, 1974 viewing the hemisphere below the satellite to support the GARP Atlantic Tropical Experiment (GATE). It was moved to its operational position at 75W on Nov 15, 1974 where it remained until GOES-1 was launched, after which SMS 1 was moved to 105W and placed in stand-by-mode as a backup to GOES-1 or SMS-2. The VISSR experiment was operated by the NOAA National Environmental Satellite Data and Information Service (NESDIS), as well as scientists from NASA Goddard Space Flight Center.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00018 (old ID 74-033A-01D).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "VISSRSMS1L1AOIPS",
-            "creator": "NASA/GSFC",
-            "title": "VISSR/SMS-1 Level 1 Atmospheric and Oceanographic Image Processing System (AOIPS) Data V001 (VISSRSMS1L1AOIPS) at GES DISC",
-            "graphic-preview-description": "Typical SMS 1 VISSR AOIPS data showing a visible scene at left, and an infrared scene with grid at right.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS1L1AOIPS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS1L1AOIPS_Sample.png",
-                    "description": "Typical SMS 1 VISSR AOIPS data showing a visible scene at left, and an infrared scene with grid at right.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical SMS 1 VISSR AOIPS data showing a visible scene at left, and an infrared scene with grid at right.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS1L1AOIPS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/datacollection/VISSRSMS1L1AOIPS_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/datacollection/VISSRSMS1L1AOIPS_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS1L1AOIPS.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS1L1AOIPS.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRSMS1L1AOIPS",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRSMS1L1AOIPS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS1L1AOIPS.001/doc/README.VISSRSMS1L1AOIPS.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS1L1AOIPS.001/doc/README.VISSRSMS1L1AOIPS.001.pdf",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SMS_GOES/SMS_Inventory.xlsx",
-                    "description": "SMS Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "SMS Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SMS_GOES/SMS_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Typical SMS 1 VISSR AOIPS data showing a visible scene at left, and an infrared scene with grid at right.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS1L1AOIPS_Sample.png",
+            "identifier": "C1720172416-GES_DISC",
+            "issued": "2020-02-05",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1720172416-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-05-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "VISSRSMS1L1AOIPS",
             "spatial": "-135.0 -90.0 45.0 90.0",
+            "temporal": "1974-07-01T00:00:00Z/1979-04-19T23:59:59.999Z",
             "theme": [
                 "GOES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VISSR/SMS-1 Level 1 Atmospheric and Oceanographic Image Processing System (AOIPS) Data V001 (VISSRSMS1L1AOIPS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1708939846-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS.",
-            "issued": "1976-01-01",
-            "temporal": "2016-01-01T00:00:00Z/2024-10-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-23",
-            "keyword": [
-                "tectonics",
-                "earth science",
-                "gravity/gravitational field",
-                "geodetics",
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
-            "identifier": "C1708939846-CDDIS",
             "description": "This dataset consists of ground-based Satellite Laser Ranging observation data (normal points, daily 24 hour files) from the NASA Crustal Dynamics Data Information System (CDDIS). SLR provides unambiguous range measurements to mm precision that can be aggregated over the global network to provide very accurate satellite orbits, time histories of station position and motion, and many other geophysical parameters. SLR operates in the optical region and is the only space geodetic technique that measures unambiguous range directly. Analysis of SLR data contributes to the terrestrial reference frame, modeling of the spatial and temporal variations of the Earth's gravitational field, and monitoring of millimeter-level variations in the location of the center of mass of the total Earth system (solid Earth-atmosphere-oceans). In addition, SLR provides precise orbit determination for spaceborne radar altimeter missions. It provides a means for sub-nanosecond global time transfer, and a basis for special tests of the Theory of General Relativity. Analysis Centers (ACs) of the International Laser Ranging Service (ILRS) retrieve SLR data on regular schedules to produce precise station positions and velocities for stations in the ILRS network. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/SLR/SLR_data_and_product_archive.html.",
-            "title": "Supporting Information for Satellite Laser Ranging (SLR) Data and Products from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/SLR_data_and_product_archive.html",
-                    "description": "URL for more information about SLR data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about SLR data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/SLR_data_and_product_archive.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1708939846-CDDIS",
+            "issued": "1976-01-01",
+            "keyword": [
+                "tectonics",
+                "earth science",
+                "gravity/gravitational field",
+                "geodetics",
+                "solid earth"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1708939846-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
+            "temporal": "2016-01-01T00:00:00Z/2024-10-28T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Supporting Information for Satellite Laser Ranging (SLR) Data and Products from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/520/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-02-03",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nikunj Oza",
                 "hasEmail": "mailto:Nikunj.C.Oza@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_520",
             "description": "Most complex aerospace systems have many text reports on safety, maintenance, and associated issues. The Aviation Safety Reporting System (ASRS) spans several decades and contains over 700 000 reports. The Aviation Safety Action Plan (ASAP) contains over 12 000 reports from various airlines. Problem categorizations have been developed for both ASRS and ASAP to enable identification of system problems. However, repository volume and complexity make human analysis difficult. Multiple experts are needed, and they often disagree on classifications. Even the same person has classified the same document differently at different times due to evolving experiences. Consistent classification is necessary to support tracking trends in problem categories over time. A decision support system that performs consistent document classification quickly and over large repositories would be useful. We discuss the results of two algorithms we have developed to classify ASRS and ASAP documents. The first is Mariana---a support vector machine (SVM) with simulated annealing, which is used to optimize hyperparameters for the model. The second method is classification built on top of nonnegative matrix factorization (NMF), which attempts to find a model that represents document features that add up in various combinations to form documents. We tested both methods on ASRS and ASAP documents with the latter categorized two different ways. We illustrate the potential of NMF to provide document features that are interpretable and indicative of topics. We also briefly discuss the tool that we have incorporated Mariana into in order to allow human experts to provide feedback on the document categorizations.",
-            "title": "Classification of Aeronautics System Health and Safety Documents",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/ozca09.pdf",
-                    "description": "ozca09.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ozca09.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/ozca09.pdf",
+                    "mediaType": "application/pdf",
                     "title": "ozca09.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/509",
-            "bureauCode": [
-                "026:00"
+            "identifier": "DASHLINK_520",
+            "issued": "2012-02-03",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
             ],
-            "citation": "Gruszka, F. 2000. BOREAS SERM Forest Cover Data Layers of the SSA in Vector Format. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/509",
-            "issued": "2023-11-22",
-            "temporal": "1993-01-01T00:00:00Z/1993-12-31T23:59:59Z",
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/520/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Classification of Aeronautics System Health and Safety Documents"
+        },
+        {
             "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "land use/land cover",
-                "earth science",
-                "terrestrial hydrosphere",
-                "surface water",
-                "agriculture",
-                "biosphere",
-                "ecological dynamics",
-                "vegetation",
-                "soils",
-                "forest science",
-                "land surface"
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "Gruszka, F. 2000. BOREAS SERM Forest Cover Data Layers of the SSA in Vector Format. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/509",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2808092515-ORNL_CLOUD",
             "description": "This data set was prepared by the SERM-FBIU.  The data include information on forest parameters and cover the area in and near the BOREAS SSA, excluding the PANP.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS SERM Forest Cover Data Layers of the SSA in Vector Format",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F509",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F509",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/ssafcovv/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/ssafcovv/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/SSA_For_Cov_Vector.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/SSA_For_Cov_Vector.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/509",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/509",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ssafcovv/comp/SSA_For_Cov_Vector.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ssafcovv/comp/SSA_For_Cov_Vector.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ssafcovv/comp/SSA_For_Cov_Vector.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ssafcovv/comp/SSA_For_Cov_Vector.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ssafcovv/comp/SSA_For_Cov_Vector.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ssafcovv/comp/SSA_For_Cov_Vector.txt",
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
+            "identifier": "C2808092515-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "land use/land cover",
+                "earth science",
+                "terrestrial hydrosphere",
+                "surface water",
+                "agriculture",
+                "biosphere",
+                "ecological dynamics",
+                "vegetation",
+                "soils",
+                "forest science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/509",
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
             "spatial": "-110.05 50.57 -94.08 59.34",
+            "temporal": "1993-01-01T00:00:00Z/1993-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS SERM Forest Cover Data Layers of the SSA in Vector Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CTFP72D3K806",
             "citation": "Xu Liu. 2023-10-30. SNDRSNIML2SFSPRET. Version 2. Sounder SIPS: Suomi NPP CrIMSS Level 2 SiFSAP Standard: Atmosphere cloud and surface geophysical state per footprint V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/CTFP72D3K806. https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2SFSPRET_2.html. Digital Science Data.",
-            "issued": "2015-11-02",
-            "temporal": "2015-11-02T00:00:00Z/2023-12-18T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://doi.org/10.5194/amt-16-4807-2023",
-                "https://doi.org/10.1016/j.atmosenv.2022.118956",
-                "https://doi.org/10.1109/IGARSS46834.2022.9884471",
-                "https://doi.org/10.3390/atmos13060876",
-                "https://doi.org/10.1016/j.atmosenv.2022.118956",
-                "https://doi.org/10.1109/IGARSS.2019.8898307",
-                "https://doi.org/10.1029/2017JD028063",
-                "https://doi.org/10.1109/TGRS.2017.2702006",
-                "https://doi.org/10.1364/OE.24.0A1514",
-                "https://doi.org/10.1364/AO.55.008236",
-                "https://doi.org/10.1002/qj.156",
-                "https://doi.org/10.1364/AO.45.000201",
-                "https://doi.org/10.5194/acp-9-9121-2009"
-            ],
-            "keyword": [
-                "solid earth",
-                "oceans",
-                "ocean temperature",
-                "atmospheric water vapor",
-                "atmospheric pressure",
-                "precipitation",
-                "surface thermal properties",
-                "atmosphere",
-                "atmospheric chemistry",
-                "land surface",
-                "geothermal dynamics",
-                "earth science",
-                "clouds",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Xu Liu",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2782356281-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "This level 2 standard product is generated by the SiFSAP (Single Field-of-View Sounder Atmospheric Products) algorithm. The SIFSAP algorithm provides retrieval for each sounder Field of View (FOV), therefore, it has 3-times higher horizontal spatial resolution and 9-time denser products compared to other current IR sounder products.  Since SiFSAP is an FOV-based algorithm, its product variables have an additional dimension which represents the number of FOVs. For CrIS instrument, there are 9 FOVs for each Field of Regard (FOR). The SiFSAP Level-2 retrieval products contain a variety of geophysical parameters retrieved from IR/MW sounder suites measurements, including profiles of temperature, water vapor and trace gas species as well as clouds and surface properties. This standard product provides retrievals on a reduced vertical profile (11 levels for water profiles and up to 27 for other profile variables). A level 2 granule has been set as 6 minutes of data. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRSNIML2SFSPRET",
-            "creator": "Xu Liu",
-            "graphic-preview-description": "Sample plot of SNPP SifSAP Level 2 standard retrieval.",
-            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 2 SiFSAP Standard: Atmosphere cloud and surface geophysical state per footprint V2 (at GESDISC)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2SFSPRET_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCTFP72D3K806",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCTFP72D3K806",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2SFSPRET_2.png",
-                    "description": "Sample plot of SNPP SifSAP Level 2 standard retrieval.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of SNPP SifSAP Level 2 standard retrieval.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2SFSPRET_2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2SFSPRET_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2SFSPRET_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SiFSAP/SSNDRSNIML2SFSPRET.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SiFSAP/SSNDRSNIML2SFSPRET.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SiFSAP/SNDRSNIML2SFSPRET.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SiFSAP/SNDRSNIML2SFSPRET.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML2SFSPRET+2",
-                    "description": "Search the Earthdata website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML2SFSPRET+2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SIFSAP.L2.V2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SIFSAP.L2.V2.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SIFSAP-ATBD.pdf",
-                    "description": "ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SIFSAP-ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SiFSAP.L2.V2.Validation_Testing_Report.pdf",
-                    "description": "Science Validation Report for SifSAP",
                     "@type": "dcat:Distribution",
+                    "description": "Science Validation Report for SifSAP",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/SiFSAP.L2.V2.Validation_Testing_Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 }
             ],
+            "graphic-preview-description": "Sample plot of SNPP SifSAP Level 2 standard retrieval.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2SFSPRET_2.png",
+            "identifier": "C2782356281-GES_DISC",
+            "issued": "2015-11-02",
+            "keyword": [
+                "solid earth",
+                "oceans",
+                "ocean temperature",
+                "atmospheric water vapor",
+                "atmospheric pressure",
+                "precipitation",
+                "surface thermal properties",
+                "atmosphere",
+                "atmospheric chemistry",
+                "land surface",
+                "geothermal dynamics",
+                "earth science",
+                "clouds",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/CTFP72D3K806",
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
+                "https://doi.org/10.5194/amt-16-4807-2023",
+                "https://doi.org/10.1016/j.atmosenv.2022.118956",
+                "https://doi.org/10.1109/IGARSS46834.2022.9884471",
+                "https://doi.org/10.3390/atmos13060876",
+                "https://doi.org/10.1016/j.atmosenv.2022.118956",
+                "https://doi.org/10.1109/IGARSS.2019.8898307",
+                "https://doi.org/10.1029/2017JD028063",
+                "https://doi.org/10.1109/TGRS.2017.2702006",
+                "https://doi.org/10.1364/OE.24.0A1514",
+                "https://doi.org/10.1364/AO.55.008236",
+                "https://doi.org/10.1002/qj.156",
+                "https://doi.org/10.1364/AO.45.000201",
+                "https://doi.org/10.5194/acp-9-9121-2009"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRSNIML2SFSPRET",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-11-02T00:00:00Z/2023-12-18T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 2 SiFSAP Standard: Atmosphere cloud and surface geophysical state per footprint V2 (at GESDISC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4TD9V7F",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN. 1996-12-31. Archive of Census Related Products (ACRP): 1990 ZIP Equivalency Files. Version 1.00. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4TD9V7F. https://doi.org/10.7927/H4TD9V7F.",
-            "issued": "1996-12-31",
-            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4Z60KZ9",
-                "https://doi.org/10.7927/H4G44N6R",
-                "https://doi.org/10.7927/H4BG2KWB",
-                "https://doi.org/10.7927/H47P8W9V",
-                "https://doi.org/10.7927/H43X84KH",
-                "https://doi.org/10.7927/H4057CV3",
-                "https://doi.org/10.7927/H4QN64NG",
-                "https://doi.org/10.7927/H46Q1V51",
-                "https://doi.org/10.7927/H42Z13FP"
-            ],
-            "keyword": [
-                "earth science",
-                "human dimensions",
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
-            "identifier": "C179001898-SEDAC",
-            "description": "The 1990 Zip Equivalency Files portion of the Archive of Census Related Products (ACRP) contains population and housing data derived from the U.S. Census Bureau's 1990 STF3B header file. The data are available at the census block and census blockgroup levels, and encompass 5-digit zip codes, POLygon IDentification (POLID) block fields that correspond to the POLID of the Tiger-based boundary file, and population centroids. This portion of the ACRP is produced by the Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN",
-            "title": "Archive of Census Related Products (ACRP): 1990 ZIP Equivalency Files",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-zip-code-equivalency-1990/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 1990 Zip Equivalency Files portion of the Archive of Census Related Products (ACRP) contains population and housing data derived from the U.S. Census Bureau's 1990 STF3B header file. The data are available at the census block and census blockgroup levels, and encompass 5-digit zip codes, POLygon IDentification (POLID) block fields that correspond to the POLID of the Tiger-based boundary file, and population centroids. This portion of the ACRP is produced by the Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4TD9V7F",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4TD9V7F",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-zip-code-equivalency-1990/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-zip-code-equivalency-1990/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-zip-code-equivalency-1990/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-zip-code-equivalency-1990/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-zip-code-equivalency-1990",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-zip-code-equivalency-1990",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-zip-code-equivalency-1990/sedac-logo.jpg",
+            "identifier": "C179001898-SEDAC",
+            "issued": "1996-12-31",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "infrastructure"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4TD9V7F",
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
+                "https://doi.org/10.7927/H4Z60KZ9",
+                "https://doi.org/10.7927/H4G44N6R",
+                "https://doi.org/10.7927/H4BG2KWB",
+                "https://doi.org/10.7927/H47P8W9V",
+                "https://doi.org/10.7927/H43X84KH",
+                "https://doi.org/10.7927/H4057CV3",
+                "https://doi.org/10.7927/H4QN64NG",
+                "https://doi.org/10.7927/H46Q1V51",
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
+            "title": "Archive of Census Related Products (ACRP): 1990 ZIP Equivalency Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa17leam_raw_worktape&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains fixed-width ASCII files of raw cleaned measurements acquired by the Lunar Ejecta And Meteorites (LEAM) Experiment at the Apollo 17 landing site for the time span of 01 March through 18 July 1976, which were the last 140 days of LEAM operation. These data were extracted from ALSEP normal-bit-rate Work Tape files.",
+            "identifier": "urn:nasa:pds:a17leam_raw_worktape",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "apollo 17",
                 "dust",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa17leam_raw_worktape&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:a17leam_raw_worktape",
-            "description": "This bundle contains fixed-width ASCII files of raw cleaned measurements acquired by the Lunar Ejecta And Meteorites (LEAM) Experiment at the Apollo 17 landing site for the time span of 01 March through 18 July 1976, which were the last 140 days of LEAM operation. These data were extracted from ALSEP normal-bit-rate Work Tape files.",
-            "title": "Apollo 17 ALSEP Work Tape Lunar Ejecta And Meteorites Experiment Raw Cleaned ASCII Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Apollo 17 ALSEP Work Tape Lunar Ejecta And Meteorites Experiment Raw Cleaned ASCII Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL1BL_L1.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2014-03-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL1BL_L1.005. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2013-01-18",
-            "temporal": "2004-08-22T00:00:00Z/2005-04-10T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
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
-            "identifier": "C1451577449-LARC",
             "description": "TL1BL_5 is the Tropospheric Emission Spectrometer (TES)/Aura L1B Spectra Limb Version 5 data product. TES Level 1B Spectra data contaisn radiometric calibrated spectral radiances and their corresponding noise equivalent spectral radiances (NESR). The geolocation, quality and some engineering data were also provided with this data product. \r\rTES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. Each L1B data file contained data from a single TES orbit starting from the South Pole Apex. A Nadir sequence within the TES Global Survey was two low resolution scans over the same ground locations, thus pointing directly to the surface of the earth. The Nadir standard product consisted of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. The Global Survey Limb observations, however, used a repeating sequence of filter wheel positions and were pointed at various off-nadir angles into the atmosphere. Special Observations were only scheduled during the 9 or 10 orbit gaps in the Global Surveys and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depends on the science requirement.",
-            "title": "TES/Aura L1B Spectra Limb V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL1BL_L1.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL1BL_L1.005",
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL1BL_L1.005",
-                    "description": "DOI data set landing page for TL1BL_5",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL1BL_5",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL1BL_L1.005",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1451577449-LARC",
-                    "description": "Earthdata Search for TL1BL_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL1BL_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1451577449-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL1BL.005/contents.html",
-                    "description": "OPeNDAP data access for TL1BL_5",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL1BL_5",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL1BL.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL1BL.005/",
-                    "description": "ASDC Direct Data Download for TL1BL_5",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL1BL_5",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL1BL.005/",
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
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L1BReadSoftwareV3.tar",
-                    "description": "TES Level 1B Version 3 Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 1B Version 3 Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L1BReadSoftwareV3.tar",
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L1B.cgi",
-                    "description": "Report of TES Level 1B Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 1B Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L1B.cgi",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_1b_std.pdf",
-                    "description": "TES Level 1B Versioning - Level 1B Standard and Special Observation Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 1B Versioning - Level 1B Standard and Special Observation Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_1b_std.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L1BReadSoftwareV3.txt",
-                    "description": "Basic IDL Tools for extraction information from TES L1B HDF product files Readme",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extraction information from TES L1B HDF product files Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L1BReadSoftwareV3.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L1B_products_v002.pdf",
-                    "description": "Aura-TES L1B Products: Version 2 Quality Description",
                     "@type": "dcat:Distribution",
+                    "description": "Aura-TES L1B Products: Version 2 Quality Description",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L1B_products_v002.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 }
             ],
+            "identifier": "C1451577449-LARC",
+            "issued": "2013-01-18",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL1BL_L1.005",
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
+            "temporal": "2004-08-22T00:00:00Z/2005-04-10T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L1B Spectra Limb V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1402",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Budney, J.W., R.Y-W. Chang, R. Commane, B.C. Daube, A. Dayalu, S.J. Dinardo, E.W. Gottlieb, A. Karion, J.O.W. Lindaas, C.E. Miller, J.B. Miller, S. Miller, M. Pender, J.V. Pittman, J. Samra, C. Sweeney, S.C. Wofsy, and B. Xiang. 2016. CARVE: L2 Merged Atmospheric CO2, CO, O3 and CH4 Concentrations, Alaska, 2012-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1402",
-            "issued": "2016-07-28",
-            "temporal": "2012-05-23T00:00:00Z/2014-11-09T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-26",
-            "keyword": [
-                "atmospheric water vapor",
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
-            "identifier": "C2236316133-ORNL_CLOUD",
             "description": "This data set provides atmospheric carbon dioxide (CO2), methane (CH4), carbon monoxide (CO), ozone (O3), and water vapor (H2O) concentrations from airborne campaigns over the Alaskan and Canadian arctic for the Carbon in Arctic Reservoirs Vulnerability Experiment (CARVE). These data are merged and gap-filled outputs from two different cavity ring-down spectrometers (CRDS; Picarro Inc.) flown aboard the CARVE aircraft and are presented at 5-second intervals throughout each flight. Aircraft latitude, longitude, and altitude are also provided. Flight campaigns took place from 2012 to 2015 between the months of March and November to enable investigation of both seasonal and inter-annual variability in atmospheric gas content. The measurements included in this data set are crucial for understanding changes in Arctic carbon cycling and the potential threats posed by thawing of Arctic permafrost.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CARVE: L2 Merged Atmospheric CO2, CO, O3 and CH4 Concentrations, Alaska, 2012-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/Fig1_CARVE_L2_AtmosGas_Merge.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1402",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1402",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/carve/campaign/CARVE_L2_AtmosGas_Merge/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/carve/campaign/CARVE_L2_AtmosGas_Merge/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/CARVE_L2_AtmosGas_Merge_1402.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/CARVE_L2_AtmosGas_Merge_1402.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L2_AtmosGas_Merge.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L2_AtmosGas_Merge.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1402",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1402",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/CARVE_L2_AtmosGas_Merge_1402.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/CARVE_L2_AtmosGas_Merge_1402.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L2_AtmosGas_Merge/comp/CARVE_L2_AtmosGas_Merge.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L2_AtmosGas_Merge/comp/CARVE_L2_AtmosGas_Merge.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/Fig1_CARVE_L2_AtmosGas_Merge.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/Fig1_CARVE_L2_AtmosGas_Merge.png",
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
+            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/Fig1_CARVE_L2_AtmosGas_Merge.png",
+            "identifier": "C2236316133-ORNL_CLOUD",
+            "issued": "2016-07-28",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1402",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-168.11 60.21 -131.76 71.56",
+            "temporal": "2012-05-23T00:00:00Z/2014-11-09T23:59:59Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE: L2 Merged Atmospheric CO2, CO, O3 and CH4 Concentrations, Alaska, 2012-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-2-EAR3-SPM-V1.0",
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
-                "earth",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 2 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the EAR3 (Earth fly-by 3) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-2-ear3-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-2-EAR3-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-2-ear3-spm-v1.0",
-            "description": "This archive contains level 2 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the EAR3 (Earth fly-by 3) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER EARTH ROMAP 2 EAR3 SPM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER EARTH ROMAP 2 EAR3 SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-HRSC-5-REFDR-DTM-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "N/A",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-hrsc-5-refdr-dtm-v1.0_5qu6-uuqq",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "deimos",
                 "phobos",
                 "mars express",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-HRSC-5-REFDR-DTM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-hrsc-5-refdr-dtm-v1.0_5qu6-uuqq",
-            "description": "N/A",
-            "title": "HRSC REDRS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "HRSC REDRS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://aeronet.gsfc.nasa.gov/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1993-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://aeronet.gsfc.nasa.gov/new_web/Documents/Inversion_products_V2.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brent Holben",
+                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
+            },
+            "describedBy": "http://aeronet.gsfc.nasa.gov/new_web/Documents/Inversion_products_V2.pdf",
+            "describedByType": "application/pdf",
+            "description": "AERONET inversion code provides aerosoloptical properties in the total atmospheric column derived from the direct and diffuse radiation measured byAERONETCimel sun/sky-radiometers. AERONET inversion developmentand researchactivitiesare described in the papers by Dubovik and King, [2000], Dubovik et al. [2000], Dubovik et al. [2002a], Dubovik et al. [2002b], Dubovik et al., [2006a], Sinyuk et al. [2006]. The Version 2(V2)inversion (or retrieval)products are summarized below. These products are available through the internal analysis system&#x0022;demonstrat&#x0022; and the AERONET website. Adetailed description of V2 AERONET retrieval will be provided in the paper by Dubovik et al., [2006b].",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/INV/INV_Level15_All_Points_V2.tar.gz",
+                    "mediaType": "application/x-tar"
+                }
             ],
+            "identifier": "NASA-0000004",
+            "issued": "2018-06-25",
             "keyword": [
                 "radiation",
                 "inversions",
@@ -205568,152 +205578,120 @@
                 "aerosols",
                 "clouds"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brent Holben",
-                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
-            },
+            "landingPage": "http://aeronet.gsfc.nasa.gov/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000004",
-            "description": "AERONET inversion code provides aerosoloptical properties in the total atmospheric column derived from the direct and diffuse radiation measured byAERONETCimel sun/sky-radiometers. AERONET inversion developmentand researchactivitiesare described in the papers by Dubovik and King, [2000], Dubovik et al. [2000], Dubovik et al. [2002a], Dubovik et al. [2002b], Dubovik et al., [2006a], Sinyuk et al. [2006]. The Version 2(V2)inversion (or retrieval)products are summarized below. These products are available through the internal analysis system&#x0022;demonstrat&#x0022; and the AERONET website. Adetailed description of V2 AERONET retrieval will be provided in the paper by Dubovik et al., [2006b].",
-            "title": "Level 1.5 Almucantar Inversion Products (except phase functions)",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/INV/INV_Level15_All_Points_V2.tar.gz",
-                    "mediaType": "application/x-tar"
-                }
+            "references": [
+                "http://aeronet.gsfc.nasa.gov/new_web/Documents/Inversion_products_V2.pdf"
             ],
             "spatial": "Global",
-            "describedBy": "http://aeronet.gsfc.nasa.gov/new_web/Documents/Inversion_products_V2.pdf",
-            "accrualPeriodicity": "irregular",
+            "temporal": "1993-01-01/2014-01-01",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Level 1.5 Almucantar Inversion Products (except phase functions)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0219-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-18T13:28:05.000 to 2014-08-18T18:47:55.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0219-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0219-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0219-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-18T13:28:05.000 to 2014-08-18T18:47:55.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0219 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0219 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-CR4A-V1.0",
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
+            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR4A phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-cr4a-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-CR4A-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-cr4a-v1.0",
-            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR4A phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 CR4A V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 CR4A V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3569",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Froidevaux, L., Livesey, N., Read, W., and Fuller, R.. 2021-04-29. ML3DZHCL. Version 005. MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Zonal and Similar Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3569. https://disc.gsfc.nasa.gov/datacollection/ML3DZHCL_005.html. Digital Science Data.",
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
-            "identifier": "C2042566665-GES_DISC",
-            "description": "ML3DZHCL is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for hydrogen chloride (HCl) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude), with each profile spaced 1.5  degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 100 to 0.316 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3DZHCL data product should read chapter 4 and section 3.10 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DZHCL",
             "creator": "Froidevaux, L., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZHCL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZHCL_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DZHCL is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for hydrogen chloride (HCl) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude), with each profile spaced 1.5  degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 100 to 0.316 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3DZHCL data product should read chapter 4 and section 3.10 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3569",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3569",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -205723,157 +205701,157 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZHCL_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZHCL_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZHCL.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZHCL.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZHCL.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZHCL.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZHCL_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZHCL_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZHCL_005.png",
+            "identifier": "C2042566665-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3569",
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
+            "series-name": "ML3DZHCL",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZHCL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC2-EDITED2-V1.0",
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
+            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the COMET ESCORT 2 mission\nphase where the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1\n(1969 R1). It contains uncalibrated raw data, i.e. the digital output of\nthe instrument. This version reorganizes the data into fewer files with\nlonger time series and sorted by type of measurement. It also supersedes\nprevious versions that were split into MTPs. The version number starts\nover from V1.0 due to a change in naming convention.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc2-edited2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC2-EDITED2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc2-edited2-v1.0",
-            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the COMET ESCORT 2 mission\nphase where the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1\n(1969 R1). It contains uncalibrated raw data, i.e. the digital output of\nthe instrument. This version reorganizes the data into fewer files with\nlonger time series and sorted by type of measurement. It also supersedes\nprevious versions that were split into MTPs. The version number starts\nover from V1.0 due to a change in naming convention.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC2 EDITED2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC2 EDITED2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Froidevaux, L., Livesey, N. and Read, W.. 2015-02-19. ML2HOCL. Version 004. MLS/Aura Level 2 Hypochlorous Acid (HOCl) Mixing Ratio V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2014. https://disc.gsfc.nasa.gov/datacollection/ML2HOCL_004.html. Digital Science Data.",
-            "issued": "2015-02-19",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-02-19",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1251101596-GES_DISC",
-            "description": "ML2HOCL is the EOS Aura Microwave Limb Sounder (MLS) standard product for  hypochlorous acid derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 10 to 2.15 hPa, and the vertical resolution is about 6 km. Users of the ML2OHCL data product should read section 3.14 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2HOCL",
             "creator": "Froidevaux, L., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Hypochlorous Acid (HOCl) Mixing Ratio V004 (ML2HOCL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2HOCL_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2HOCL is the EOS Aura Microwave Limb Sounder (MLS) standard product for  hypochlorous acid derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 10 to 2.15 hPa, and the vertical resolution is about 6 km. Users of the ML2OHCL data product should read section 3.14 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2014",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -205883,142 +205861,120 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2HOCL_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2HOCL_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2HOCL.004/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2HOCL.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2HOCL.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2HOCL.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2HOCL_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2HOCL_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2HOCL_004.png",
+            "identifier": "C1251101596-GES_DISC",
+            "issued": "2015-02-19",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2014",
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
+            "series-name": "ML2HOCL",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Hypochlorous Acid (HOCl) Mixing Ratio V004 (ML2HOCL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/RAEHAOH4VZM5",
             "citation": "AIRS project. 2019-12-15. AIRS2RET_NRT. Version 7.0. Aqua/AIRS L2 Near Real Time (NRT) Standard Physical Retrieval (AIRS-only) V7.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/RAEHAOH4VZM5. https://disc.gsfc.nasa.gov/datacollection/AIRS2RET_NRT_7.0.html. Digital Science Data.",
-            "issued": "2024-07-03",
-            "temporal": "2002-08-30T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-07",
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
-                "oceans",
-                "surface thermal properties",
-                "surface radiative properties",
-                "air quality",
-                "altitude",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "ocean temperature",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "clouds",
-                "earth science",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LENA IREDELL",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "AIRS project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1701805625-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) Level 2 Near Real Time (NRT) Standard Physical Retrieval (AIRS-only) product (AIRS2RET_NRT_7.0) differs from the routine product (AIRS2RET_7.0) in four ways to meet the three hour latency requirements of the Land Atmosphere NRT Capability Earth Observing System (LANCE): (1) The NRT granules are produced without previous or subsequent granules if those granules are not available within 5 minutes, (2) the predictive ephemeris/attitude data are used rather than the definitive ephemeris/attitude, (3) if the forecast surface pressure is unavailable, a surface climatology is used, and (4) no ice cloud properties retrievals are performed. The consequences of these differences are described in the AIRS Near Real Time (NRT) data products document. The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. This product is produced using AIRS IR only because the radiometric noise in several AMSU channels started to increase significantly (since June 2007). The AIRS Standard Retrieval Product consists of retrieved estimates of cloud and surface properties, plus profiles of retrieved temperature, water vapor, ozone, carbon monoxide and methane. Estimates of the errors associated with these quantities is also part of the Standard Product. The temperature profile vertical resolution is 28 levels total between 1100 mb and 0.1 mb, while moisture profile is reported at 14 atmospheric layers between 1100 mb and 50 mb. The horizontal resolution is 50 km. \n\nAn AIRS granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS2RET_NRT",
-            "creator": "AIRS project",
-            "title": "Aqua/AIRS L2 Near Real Time (NRT) Standard Physical Retrieval (AIRS-only) V7.0 at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2RET_7.0.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRAEHAOH4VZM5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRAEHAOH4VZM5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -206028,159 +205984,211 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2RET_NRT_7.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2RET_NRT_7.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRS2RET_NRT.7.0/",
-                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRS2RET_NRT.7.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_NRT/AIRS2RET_NRT.7.0",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_NRT/AIRS2RET_NRT.7.0",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2RET_NRT+7.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2RET_NRT+7.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
-                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument,algorithms, and other AIRS-related activities can be found.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument,algorithms, and other AIRS-related activities can be found.",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_the_AIRS_Mission.pdf",
-                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_the_AIRS_Mission.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L2_Product_User_Guide.pdf",
-                    "description": "AIRS/AMSU/HSB Version 7 Level 2 Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS/AMSU/HSB Version 7 Level 2 Product User Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L2_Product_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2RET_7.0.png",
+            "identifier": "C1701805625-GES_DISC",
+            "issued": "2024-07-03",
+            "keyword": [
+                "oceans",
+                "surface thermal properties",
+                "surface radiative properties",
+                "air quality",
+                "altitude",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "ocean temperature",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/RAEHAOH4VZM5",
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
+            "series-name": "AIRS2RET_NRT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "Aqua",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua/AIRS L2 Near Real Time (NRT) Standard Physical Retrieval (AIRS-only) V7.0 at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-TPE-COUNTS-V1.0",
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
-                "1 ceres",
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A global map thermal+epithermal         neutron counting rates binned on twenty-degree quasi-equal-area         pixels is provided. The map was determined from a time series           of the rate of neutron capture by lithium in the lithium-loaded         glass scintillator, part of the +Z phoswich sensor on Dawn's Gamma      Ray and Neutron Detector (GRaND). Neutrons in the thermal and           epithermal energy range contribute to the reaction. The data were       acquired while in low altitude mapping orbit, about 385 km from         Ceres' surface (about 0.8 body radii altitude). Prior to mapping,       the time series counting data were subjected to corrections for         variations in the flux of galactic cosmic rays and measurement          geometry, as described by PRETTYMANETAL2017.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-tpe-counts-v1.0_5r56-47cy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-TPE-COUNTS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-tpe-counts-v1.0_5r56-47cy",
-            "description": "A global map thermal+epithermal         neutron counting rates binned on twenty-degree quasi-equal-area         pixels is provided. The map was determined from a time series           of the rate of neutron capture by lithium in the lithium-loaded         glass scintillator, part of the +Z phoswich sensor on Dawn's Gamma      Ray and Neutron Detector (GRaND). Neutrons in the thermal and           epithermal energy range contribute to the reaction. The data were       acquired while in low altitude mapping orbit, about 385 km from         Ceres' surface (about 0.8 body radii altitude). Prior to mapping,       the time series counting data were subjected to corrections for         variations in the flux of galactic cosmic rays and measurement          geometry, as described by PRETTYMANETAL2017.",
-            "title": "DAWN GRAND MAP CERES TPE                \n                                      NEUTRON COUNTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN GRAND MAP CERES TPE                \n                                      NEUTRON COUNTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-3-RDR-WILD2-V3.0",
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
+            "description": "This data set contains RDR (calibrated) pre-encounter and encounter images taken by the Stardust Navigation Camera of comet 81P/Wild 2 (1978 A2). This is a new version of a subset of an existing data set, based on work done during the Stardust-NExT mission. Changes in the calibration of the NAVCAM instrument, between these prime mission data and those of the Stardust-NExT mission, are a possibility and are addressed in [KLAASENETAL2011B].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-3-rdr-wild2-v3.0_5r5b-yt4h",
+            "issued": "2021-05-21",
+            "keyword": [
+                "81p/wild 2 (1978 a2)",
+                "stardust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-3-RDR-WILD2-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-3-rdr-wild2-v3.0_5r5b-yt4h",
-            "description": "This data set contains RDR (calibrated) pre-encounter and encounter images taken by the Stardust Navigation Camera of comet 81P/Wild 2 (1978 A2). This is a new version of a subset of an existing data set, based on work done during the Stardust-NExT mission. Changes in the calibration of the NAVCAM instrument, between these prime mission data and those of the Stardust-NExT mission, are a possibility and are addressed in [KLAASENETAL2011B].",
-            "title": "STARDUST NAVCAM CALIBRATED IMAGES OF\n                                81P/WILD 2 - VERS 3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STARDUST NAVCAM CALIBRATED IMAGES OF\n                                81P/WILD 2 - VERS 3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.hq.nasa.gov/pao/FOIA/err.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1999-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.hq.nasa.gov/pao/FOIA/agency/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Josephine Sibley",
+                "hasEmail": "mailto:foia@hq.nasa.gov"
+            },
+            "description": "NASA makes annual reports of progress made on Freedom of Information Act (FOIA) requests. This database contains PDF and XML versions of reports from 1999 to the present.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hq.nasa.gov/pao/FOIA/err.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "NASA-0000011",
+            "issued": "2018-06-25",
             "keyword": [
                 "grin",
                 "history",
@@ -206190,63 +206198,34 @@
                 "wise",
                 "photography"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Josephine Sibley",
-                "hasEmail": "mailto:foia@hq.nasa.gov"
-            },
+            "landingPage": "http://www.hq.nasa.gov/pao/FOIA/err.htm",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000011",
-            "description": "NASA makes annual reports of progress made on Freedom of Information Act (FOIA) requests. This database contains PDF and XML versions of reports from 1999 to the present.",
-            "title": "Annual Freedom of Information Act (FOIA) Reports",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.hq.nasa.gov/pao/FOIA/err.htm",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "http://www.hq.nasa.gov/pao/FOIA/agency/index.html"
             ],
-            "accrualPeriodicity": "irregular"
+            "temporal": "1999-01-01/2014-01-01",
+            "title": "Annual Freedom of Information Act (FOIA) Reports"
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
-                "knowledge",
-                "sharing",
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
-            "identifier": "NASA-862__44",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -206254,460 +206233,460 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__44",
+            "issued": "2018-06-25",
+            "keyword": [
+                "appel",
+                "knowledge",
+                "sharing",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROMAP-2-FSS-SPM-V1.0",
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
+            "description": "This archive contains edited data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the FSS (First Science Sequence) phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-romap-2-fss-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROMAP-2-FSS-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-romap-2-fss-spm-v1.0",
-            "description": "This archive contains edited data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the FSS (First Science Sequence) phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P ROMAP 2 FSS SPM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P ROMAP 2 FSS SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-PROFILE-V1.2",
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
+            "description": "All PROFILE accelerometer data are packaged by periapsis number for each aerobraking orbit. Each orbit is identified by a folder with name Pyyyy where 'yyyy' is the four digit periapsis number. PROFILE data are provided in a table labeled Pyyyy.tab located in its respective orbit folder. PROFILE data are provided at one second resolution.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-profile-v1.2_5rbj-tq6t",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-PROFILE-V1.2",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-profile-v1.2_5rbj-tq6t",
-            "description": "All PROFILE accelerometer data are packaged by periapsis number for each aerobraking orbit. Each orbit is identified by a folder with name Pyyyy where 'yyyy' is the four digit periapsis number. PROFILE data are provided in a table labeled Pyyyy.tab located in its respective orbit folder. PROFILE data are provided at one second resolution.",
-            "title": "MGS PROFILE DATA RECORDS V1.2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS PROFILE DATA RECORDS V1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/W4JHZBCRCNLX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Weather Research and Forecasting (WRF) North American Mountain Snow Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/W4JHZBCRCNLX.",
-            "issued": "2004-10-01",
-            "temporal": "2004-10-01T00:00:00Z/2013-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-06-30",
-            "keyword": [
-                "snow/ice",
-                "earth science",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Melissa Wrzesien",
                 "hasEmail": "mailto:wrzesien@unc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1559336694-NSIDCV0",
             "description": "This data set consists of modeled snow water equivalent (SWE) data for 10 mountain ranges in North America, simulated by the Weather Research and Forecasting (WRF) regional climate model.",
-            "title": "Weather Research and Forecasting (WRF) North American Mountain Snow Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW4JHZBCRCNLX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW4JHZBCRCNLX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0736_WRF_swe_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0736_WRF_swe_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W4JHZBCRCNLX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/W4JHZBCRCNLX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W4JHZBCRCNLX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/W4JHZBCRCNLX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1559336694-NSIDCV0",
+            "issued": "2004-10-01",
+            "keyword": [
+                "snow/ice",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/W4JHZBCRCNLX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-168.2 31.9 -56.8 69.7",
+            "temporal": "2004-10-01T00:00:00Z/2013-06-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Weather Research and Forecasting (WRF) North American Mountain Snow Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0014-V1.0",
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
-                "unknown",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Checkout measurement covering the time 2005-09-29T04:13:18.500 to 2005-09-29T06:37:37.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0014-v1.0_5rhi-9jhj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "unknown",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0014-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0014-v1.0_5rhi-9jhj",
-            "description": "This is a Checkout measurement covering the time 2005-09-29T04:13:18.500 to 2005-09-29T06:37:37.500.",
-            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 CRUISE 2 0014 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 CRUISE 2 0014 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0737-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-28T21:12:50.000 to 2015-04-29T00:13:24.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0737-v1.0_5rhy-vz98",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0737-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0737-v1.0_5rhy-vz98",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-28T21:12:50.000 to 2015-04-29T00:13:24.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0737 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0737 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475747-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2012-01-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
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
-                "name": "OB.DAAC"
-            },
-            "identifier": "C1658475747-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Suomi-NPP VIIRS Global Binned 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Data, version 2016.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L3BIN",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L3BIN",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NPP/VIIRS/L3B/NSST/2016.2",
-                    "description": "VIIRS-Suomi-NPP L3B 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3B 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NPP/VIIRS/L3B/NSST/2016.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1658475747-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ocean temperature",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475747-OB_DAAC.html",
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
+            "temporal": "2012-01-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suomi-NPP VIIRS Global Binned 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Data, version 2016.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/C0RELPJG8BYW",
             "citation": "Chris Barnet. 2019-12-15. SNDRSNIML3SMCCPN. Version 2. Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS Normal Spectral Resolution V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/C0RELPJG8BYW. https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3SMCCPN_2.html. Digital Science Data.",
-            "issued": "2012-04-01",
-            "temporal": "2012-04-01T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-01",
-            "references": [
-                "https://doi.org/10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "air quality",
-                "clouds",
-                "surface thermal properties",
-                "atmospheric chemistry",
-                "atmosphere",
-                "surface radiative properties",
-                "precipitation",
-                "altitude",
-                "oceans",
-                "ocean temperature",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "land surface",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Chris Barnet",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1692982082-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "WARNING: To users of the derived product \u201cco_mmr_midtrop\u201d (carbon monoxide mass mixing ratio to dry air [kg/kg] at ~500 hPa). This variable has a significant bias due to a conversion error: the molecular weight of carbon dioxide (CO2, 44.01 g/mol) was used instead of carbon monoxide (CO, 28.01 g/mol). To correct, simply multiply \u201cco_mmr_midtrop\u201d by 28.01/44.01. Alternatively, derive a profile of mass mixing ratio from scratch using the retrieved column density values (\u201cmol_lay/co_mol_lay\u201d) in the Level 2 files. For further questions or concerns please contact the Sounder SIPS at: sounder.sips@jpl.nasa.gov\n\nThe CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the Cross-track Infrared Sounder/Advanced Technology Microwave Sounder (CrIS/ATMS) instruments, also known as CrIMSS (Cross-track Infrared and Microwave Sounding Suite). The CrIS/ATMS instruments used for this product are on board the Suomi National Polar-orbiting Partnership (SNPP) platform and use the Normal Spectral Resolution (NSR) data. The CrIS instrument is a Fourier transform spectrometer with a total of 1305 NSR infrared sounding channels covering the longwave (655-1095 cm-1), midwave (1210-1750 cm-1), and shortwave (2155-2550 cm-1) spectral regions. The ATMS instrument  is a cross-track scanner with 22 channels in spectral bands from 23 GHz through 183 GHz.\n \nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n\nThis monthly one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products with QC values of 0 (best), 1 (good), and 2 (don't use) which are provided for each variable and applying specific QC methodology. Specific QC accepts profile level from the top of the atmosphere down to the level where the QC determines that it is still good. Below this level, the data is rejected.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRSNIML3SMCCPN",
-            "creator": "Chris Barnet",
-            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
-            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS Normal Spectral Resolution V2 (SNDRSNIML3SMCCPN) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SMCCPN_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC0RELPJG8BYW",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC0RELPJG8BYW",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SMCCPN_2.png",
-                    "description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SMCCPN_2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3SMCCPN_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3SMCCPN_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level3/SNDRSNIML3SMCCPN.2",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level3/SNDRSNIML3SMCCPN.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level3/SNDRSNIML3SMCCPN.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level3/SNDRSNIML3SMCCPN.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML3SMCCPN+2",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML3SMCCPN+2",
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
+            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SMCCPN_2.png",
+            "identifier": "C1692982082-GES_DISC",
+            "issued": "2012-04-01",
+            "keyword": [
+                "air quality",
+                "clouds",
+                "surface thermal properties",
+                "atmospheric chemistry",
+                "atmosphere",
+                "surface radiative properties",
+                "precipitation",
+                "altitude",
+                "oceans",
+                "ocean temperature",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "land surface",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/C0RELPJG8BYW",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-06-01",
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
+            "series-name": "SNDRSNIML3SMCCPN",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-04-01T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS Normal Spectral Resolution V2 (SNDRSNIML3SMCCPN) at GES DISC"
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
-                "grs",
-                "spice",
-                "themis",
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
-            "identifier": "NASA-553",
             "description": "CGRS, SPICE, THEMIS",
-            "title": "PDS Odyssey Data Release 34",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -206715,20 +206694,55 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-553",
+            "issued": "2018-06-25",
+            "keyword": [
+                "grs",
+                "spice",
+                "themis",
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
+            "title": "PDS Odyssey Data Release 34"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/5rt9-fftx",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "In recent times long-term stay has become a common occurrence in the International Space Station (ISS). However adaptation to the space environment can sometimes pose physiological problems to the astronauts after their return. Therefore it is important to develop healthcare technologies for astronauts. In this study hair an easy-to-obtain sample was identified as the candidate. In order to investigate the genetic changes in human hair during space flight the hair follicles of 10 astronauts were analyzed by DNA microarray and real time q-PCR analyses. Space environment induced gene expression of hair follicles of astronaut was measured 6 differnent times included 2 in flight on orbit. Ten independent experiments were performed on differing astronauts. and the sampling day was differed for each astronaut because of their schedules.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-174",
+                    "mediaType": "text/html",
+                    "title": "Effects of a Closed Space Environment on Gene Expression in Hair Follicles of Astronauts in the International Space Station"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-174_5rt9-fftx",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "treatment protocol",
                 "data collection",
@@ -206740,470 +206754,465 @@
                 "spaceflight",
                 "sex"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/5rt9-fftx",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-174_5rt9-fftx",
-            "description": "In recent times long-term stay has become a common occurrence in the International Space Station (ISS). However adaptation to the space environment can sometimes pose physiological problems to the astronauts after their return. Therefore it is important to develop healthcare technologies for astronauts. In this study hair an easy-to-obtain sample was identified as the candidate. In order to investigate the genetic changes in human hair during space flight the hair follicles of 10 astronauts were analyzed by DNA microarray and real time q-PCR analyses. Space environment induced gene expression of hair follicles of astronaut was measured 6 differnent times included 2 in flight on orbit. Ten independent experiments were performed on differing astronauts. and the sampling day was differed for each astronaut because of their schedules.",
-            "title": "Effects of a Closed Space Environment on Gene Expression in Hair Follicles of Astronauts in the International Space Station",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-174",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Effects of a Closed Space Environment on Gene Expression in Hair Follicles of Astronauts in the International Space Station"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Effects of a Closed Space Environment on Gene Expression in Hair Follicles of Astronauts in the International Space Station"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-CDR-ALT%2FRAD-V1.0",
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
+            "description": "This data set contains the Magellan Altimetry/Radiometry Composite Data Record (ARCDR). Along track estimates of elevation, Fresnel Reflectivity, surface roughness, brightness temperature, emissivity derived from Magellan altimeter and radiometer data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-cdr-alt-rad-v1.0_5ruy-i8gg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-CDR-ALT%2FRAD-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-cdr-alt-rad-v1.0_5ruy-i8gg",
-            "description": "This data set contains the Magellan Altimetry/Radiometry Composite Data Record (ARCDR). Along track estimates of elevation, Fresnel Reflectivity, surface roughness, brightness temperature, emissivity derived from Magellan altimeter and radiometer data.",
-            "title": "MGN V RDRS 5 COMPOSITE DATA RECORD ALT/RAD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGN V RDRS 5 COMPOSITE DATA RECORD ALT/RAD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-2-EDR-CRUISE2-V1.0",
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
-                "solar system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-2-edr-cruise2-v1.0_5rw5-8prd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-2-EDR-CRUISE2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-2-edr-cruise2-v1.0_5rw5-8prd",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR MSI IMAGES FOR CRUISE2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR MSI IMAGES FOR CRUISE2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA204",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-01-15. AIRI2CCF. Version 006. AIRS/Aqua L2 Cloud-Cleared Infrared Radiances (AIRS+AMSU) V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA204. https://disc.gsfc.nasa.gov/datacollection/AIRI2CCF_006.html. Digital Science Data.",
-            "issued": "2002-08-30",
-            "temporal": "2002-08-30T00:00:00Z/2016-09-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-24",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1117/1.JRS.8.084994"
-            ],
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1243477378-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. Cloud-Cleared Radiances contain calibrated, geolocated channel-by-channel AIRS infrared radiances (milliWatts/m2/cm-1/steradian) that would have been observed within each AMSU footprint if there were no clouds in the FOV and produced along with the AIRS Standard Product, as they are the radiances used to retrieve the Standard Product. Nevertheless, they are an order of magnitude larger in data volume than the remainder of the Standard Products and, many Standard Product users are expected to have little interest in the Cloud Cleared Radiance. For these reasons they are a separate output file, but like the Standard Product, are generated at all locations.\n\nAn AIRS granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track for each of the approximate 2378 channels. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRI2CCF",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 2 Cloud-Cleared Infrared (IR) Radiances Product \".",
-            "title": "AIRS/Aqua L2 Cloud-Cleared Infrared Radiances (AIRS+AMSU) V006 (AIRI2CCF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRI2CCF_006.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA204",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA204",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRI2CCF_006.jpeg",
-                    "description": "Sample data of the \"AIRS/Aqua Level 2 Cloud-Cleared Infrared (IR) Radiances Product \".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 2 Cloud-Cleared Infrared (IR) Radiances Product \".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRI2CCF_006.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRI2CCF_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRI2CCF_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRI2CCF.006/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRI2CCF.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRI2CCF.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRI2CCF.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRI2CCF+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRI2CCF+006",
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
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 2 Cloud-Cleared Infrared (IR) Radiances Product \".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRI2CCF_006.jpeg",
+            "identifier": "C1243477378-GES_DISC",
+            "issued": "2002-08-30",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA204",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-09-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1117/1.JRS.8.084994"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRI2CCF",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2016-09-24T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L2 Cloud-Cleared Infrared Radiances (AIRS+AMSU) V006 (AIRI2CCF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XRS-2-EDR-EROS%2FORBIT-V1.0",
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
+            "description": "This data set contains Level 1b X-Ray Spectrometer (XRS) observations made during the Eros orbit phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xrs-2-edr-eros-orbit-v1.0_5ryp-bidd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XRS-2-EDR-EROS%2FORBIT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xrs-2-edr-eros-orbit-v1.0_5ryp-bidd",
-            "description": "This data set contains Level 1b X-Ray Spectrometer (XRS) observations made during the Eros orbit phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
-            "title": "NEAR XRS SPECTRA FOR EROS ORBIT PHASE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR XRS SPECTRA FOR EROS ORBIT PHASE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331332198-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "ngda",
-                "oceans",
-                "earth science",
-                "ocean optics",
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
-            "identifier": "C2331332198-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Global Mapped Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/PAR/2022",
-                    "description": "MODIS-Aqua L3M Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3M Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/PAR/2022",
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
+            "identifier": "C2331332198-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ngda",
+                "oceans",
+                "earth science",
+                "ocean optics",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331332198-OB_DAAC.html",
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
+            "temporal": "2002-07-04T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua MODIS Global Mapped Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475743-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2012-01-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-08",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "earth science"
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
-            "identifier": "C1658475743-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Regional 11\u00b5m Day/Night Sea Surface Temperature (SST) Data, version 2016.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L2",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L2",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L2/SST/2016.2",
-                    "description": "VIIRS-Suomi-NPP L2 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L2 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L2/SST/2016.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1658475743-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475743-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "OB.DAAC"
+            },
             "spatial": "-180.0 90.0 -180.0 90.0",
+            "temporal": "2012-01-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suomi-NPP VIIRS Regional 11\u00b5m Day/Night Sea Surface Temperature (SST) Data, version 2016.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-2-PLUTO-V3.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons                Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains PEPSSI observations taken during the              the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for PEPSSI.                               This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and the end of October, 2016, completing the delivery of all data covering the   Pluto Encounter and subsequent Calibration Campaign.                     Also, updates were made to the calibration files, documentation, and     catalog files.                                                           Significant changes were made to the PEPSSI packet processing and        calibration, too extensive to go into here.  Data from all previous      data sets should be discarded.  Refer to the data set documentation      for details about processing of PEPSSI data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-2-pluto-v3.0_5s5m-4es3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-2-PLUTO-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-2-pluto-v3.0_5s5m-4es3",
-            "description": "This data set contains Raw data taken by the New Horizons                Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains PEPSSI observations taken during the              the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for PEPSSI.                               This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and the end of October, 2016, completing the delivery of all data covering the   Pluto Encounter and subsequent Calibration Campaign.                     Also, updates were made to the calibration files, documentation, and     catalog files.                                                           Significant changes were made to the PEPSSI packet processing and        calibration, too extensive to go into here.  Data from all previous      data sets should be discarded.  Refer to the data set documentation      for details about processing of PEPSSI data.",
-            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/tdrs-2808",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://tdrs.gsfc.nasa.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Beth Beck",
+                "hasEmail": "mailto:beth.beck@nasa.gov"
+            },
+            "description": "Polygons: 2808 Vertices: 1977",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/tdrs-2808/TDRS1.fbx.zip",
+                    "mediaType": "application/octet-stream"
+                }
             ],
+            "identifier": "NASA-411",
+            "issued": "2018-06-25",
             "keyword": [
                 "tracking and data relay satellite",
                 "tdrss",
@@ -207212,67 +207221,37 @@
                 "spacecraft",
                 "satellite"
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
-            "identifier": "NASA-411",
-            "description": "Polygons: 2808 Vertices: 1977",
-            "title": "NASA 3D Models: TDRS",
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/tdrs-2808",
+            "modified": "2020-01-29",
             "programCode": [
                 "026:045",
                 "026:046"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/tdrs-2808/TDRS1.fbx.zip",
-                    "mediaType": "application/octet-stream"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://tdrs.gsfc.nasa.gov/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: TDRS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://turbmodels.larc.nasa.gov/spalart.html",
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
-                "spalart",
-                "allmaras",
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
-            "identifier": "NASA-829",
             "description": "This web page gives detailed information on the equations for various forms of the Spalart-Allmaras turbulence model.",
-            "title": "Spalart-Allmaras Turbulence Model",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -207280,349 +207259,346 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-829",
+            "issued": "2018-06-25",
+            "keyword": [
+                "turbulence",
+                "spalart",
+                "allmaras",
+                "models"
+            ],
+            "landingPage": "http://turbmodels.larc.nasa.gov/spalart.html",
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
+            "title": "Spalart-Allmaras Turbulence Model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NON9395MQ9TK",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Greenland Ice Sheet Melt Characteristics Derived from Passive Microwave Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NON9395MQ9TK.",
-            "issued": "1979-04-02",
-            "temporal": "1979-04-02T00:00:00Z/2007-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-12-31",
-            "keyword": [
-                "snow/ice",
-                "cryosphere",
-                "earth science",
-                "terrestrial hydrosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Waleed Abdalati",
                 "hasEmail": "mailto:waleed.abdalati@colorado.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386250243-NSIDCV0",
             "description": "The Greenland ice sheet melt extent data, acquired as part of the NASA Program for Arctic Regional Climate Assessment (PARCA), is a daily (or every other day, prior to August 1987) estimate of the spatial extent of wet snow on the Greenland ice sheet since 1979. It is derived from passive microwave satellite brightness temperature characteristics using the Cross-Polarized Gradient Ratio (XPGR) of Abdalati and Steffen (1997). It is physically based on the changes in microwave emission characteristics observable in data from the Scanning Multi-channel Microwave Radiometer (SMMR) and the Special Sensor Microwave/Imager (SSM/I) instruments when surface snow melts. It is not a direct measure of the snow wetness but rather is a binary indicator of the state of melt of each SMMR and SSM/I pixel on the ice sheet for each day of observation. It is, however, a useful proxy for the amount of melt that occurs on the Greenland ice sheet. The data are provided in a variety of formats including raw data in ASCII format, gridded daily data in binary format, and annual and complete time series climatologies in gridded binary and GeoTIFF format. All data are in a 60 x 109 pixel subset of the standard Northern Hemisphere polar stereographic grid with a 25 km resolution and are available via FTP.",
-            "title": "Greenland Ice Sheet Melt Characteristics Derived from Passive Microwave Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNON9395MQ9TK",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNON9395MQ9TK",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/parca/nsidc0218_melt/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/parca/nsidc0218_melt/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/parca/nsidc0218_melt/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/parca/nsidc0218_melt/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/parca/nsidc0218_melt/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/parca/nsidc0218_melt/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NON9395MQ9TK",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NON9395MQ9TK",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NON9395MQ9TK",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NON9395MQ9TK",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250243-NSIDCV0",
+            "issued": "1979-04-02",
+            "keyword": [
+                "snow/ice",
+                "cryosphere",
+                "earth science",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/NON9395MQ9TK",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-73.0 60.0 -10.0 84.0",
+            "temporal": "1979-04-02T00:00:00Z/2007-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Greenland Ice Sheet Melt Characteristics Derived from Passive Microwave Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0866-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-29T16:23:30.000 to 2015-06-29T17:56:15.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0866-v1.0_5sf5-h8a8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0866-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0866-v1.0_5sf5-h8a8",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-29T16:23:30.000 to 2015-06-29T17:56:15.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0866 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0866 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/8YTYSV6JGBK2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L2 Radar/Radiometer Half-Orbit 9 km EASE-Grid Soil Moisture V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/8YTYSV6JGBK2.",
-            "issued": "2015-04-13",
-            "temporal": "2015-04-13T00:00:00Z/2015-07-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-07",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "spectral/engineering",
-                "radar",
-                "soils",
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
-            "identifier": "C1236303829-NSIDC_ECS",
             "description": "This Level-2 (L2) soil moisture product provides estimates of global land surface conditions retrieved by both the Soil Moisture Active Passive (SMAP) radar and radiometer during 6:00 a.m. descending half-orbit passes. SMAP L-band backscatter and brightness temperatures are used to derive soil moisture data, which are then resampled to an Earth-fixed, global, cylindrical 9 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0).",
-            "title": "SMAP L2 Radar/Radiometer Half-Orbit 9 km EASE-Grid Soil Moisture V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8YTYSV6JGBK2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8YTYSV6JGBK2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL2SMAP.003/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL2SMAP.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1236303829-NSIDC_ECS&m=-31.640625%21-0.5625%211%211%210%210%2C2&q=SPL2SMAP",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1236303829-NSIDC_ECS&m=-31.640625%21-0.5625%211%211%210%210%2C2&q=SPL2SMAP",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL2SMAP/versions/3/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL2SMAP/versions/3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL2SMAP.003/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL2SMAP.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1236303829-NSIDC_ECS&m=-31.640625%21-0.5625%211%211%210%210%2C2&q=SPL2SMAP",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1236303829-NSIDC_ECS&m=-31.640625%21-0.5625%211%211%210%210%2C2&q=SPL2SMAP",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL2SMAP/versions/3/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL2SMAP/versions/3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8YTYSV6JGBK2",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/8YTYSV6JGBK2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8YTYSV6JGBK2",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/8YTYSV6JGBK2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1236303829-NSIDC_ECS",
+            "issued": "2015-04-13",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "spectral/engineering",
+                "radar",
+                "soils",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/8YTYSV6JGBK2",
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
+            "title": "SMAP L2 Radar/Radiometer Half-Orbit 9 km EASE-Grid Soil Moisture V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0254-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-29T06:38:05.000 to 2014-08-29T18:00:00.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0254-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0254-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0254-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-29T06:38:05.000 to 2014-08-29T18:00:00.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0254 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0254 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-1-MOI-V1.0",
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
+            "description": ";This data set contains archival raw, partially processed, and ancillary/supporting radio science data acquired during the Mars Orbit Insertion (MOI) phase of the Mars Global Surveyor (MGS) mission. The radio observations were carried out using the MGS spacecraft and Earth-based receiving stations of the NASA Deep Space Network (DSN). The observations were designed to test the spacecraft radio system, the DSN ground system, and MGS operations procedures; to be used in generating high-resolution gravity field models of Mars; and for estimating density and structure of the Mars atmosphere. Of most interest are likely to be the Orbit Data File and Original Data Record files, in the ODF and ODR directories, respectively, which provided the raw input to gravity and atmospheric investigations. The MOI phase extended from September 1997 to March 1999. On orbits 203-266 and 343-571 (approximately April and June-September 1998, respectively) the spacecraft periapsis was especially low giving the highest per-orbit sensitivity to gravity anomalies during the entire mission. Data were organized in approximately chronological order and delivered on a set of 159 CD volumes at the rate of 2-3 CD's per week. Typical volume of a one-day ODF was 300-400 kB. Typical volume of an ODR was 5-10 MB, and there could be multiple ODR's per day depending on DSN schedules and observing geometry.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-1-moi-v1.0_5sj3-baag",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-1-MOI-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-1-moi-v1.0_5sj3-baag",
-            "description": ";This data set contains archival raw, partially processed, and ancillary/supporting radio science data acquired during the Mars Orbit Insertion (MOI) phase of the Mars Global Surveyor (MGS) mission. The radio observations were carried out using the MGS spacecraft and Earth-based receiving stations of the NASA Deep Space Network (DSN). The observations were designed to test the spacecraft radio system, the DSN ground system, and MGS operations procedures; to be used in generating high-resolution gravity field models of Mars; and for estimating density and structure of the Mars atmosphere. Of most interest are likely to be the Orbit Data File and Original Data Record files, in the ODF and ODR directories, respectively, which provided the raw input to gravity and atmospheric investigations. The MOI phase extended from September 1997 to March 1999. On orbits 203-266 and 343-571 (approximately April and June-September 1998, respectively) the spacecraft periapsis was especially low giving the highest per-orbit sensitivity to gravity anomalies during the entire mission. Data were organized in approximately chronological order and delivered on a set of 159 CD volumes at the rate of 2-3 CD's per week. Typical volume of a one-day ODF was 300-400 kB. Typical volume of an ODR was 5-10 MB, and there could be multiple ODR's per day depending on DSN schedules and observing geometry.",
-            "title": "MARS GLOBAL SURVEYOR RAW DATA SET - MOI V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARS GLOBAL SURVEYOR RAW DATA SET - MOI V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-11-27",
-            "temporal": "2021-11-27T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "space",
-                "location",
-                "iss",
-                "international",
-                "coords",
-                "coordinates",
-                "ephemeris",
-                "topo",
-                "trajectory",
-                "station"
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
-            "identifier": "nasa-iss-data_2021-11-27_5skk-j2s7",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-11-27",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -207745,519 +207721,545 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-11-27_5skk-j2s7",
+            "issued": "2021-11-27",
+            "keyword": [
+                "space",
+                "location",
+                "iss",
+                "international",
+                "coords",
+                "coordinates",
+                "ephemeris",
+                "topo",
+                "trajectory",
+                "station"
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
+            "temporal": "2021-11-27T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-11-27"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3271-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-04-29T12:06:29.000 to 2012-04-29T14:31:00.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3271-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3271-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3271-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-04-29T12:06:29.000 to 2012-04-29T14:31:00.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3271 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3271 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67P-M31-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67p-m31-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67P-M31-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67p-m31-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP031 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP031 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHG18-3CO29",
             "citation": "NOAA/NESDIS/STAR. 2023-07-28. GHRSST L3C ACSPO America Region SST from GOES ABI. Version 2.90. GHRSST L3C NOAA/ACSPO GOES-18/ABI  America Region Sea Surface Temperature v2.90 dataset\r\n. Camp Springs, MD (USA). Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHG18-3CO29\r\n. https://www.star.nesdis.noaa.gov/star/index.php.",
-            "issued": "2020-03-31",
-            "temporal": "2022-06-07T00:00:00Z/2023-07-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-31",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.11.032405"
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
-            "identifier": "C2731041317-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The G18-ABI-L3C-ACSPO-v2.90 dataset produced by the NOAA Advanced Clear Sky Processor for Ocean (ACSPO) system is used to derive Sea Surface Skin Temperature (SST) from he Advanced Baseline Imager (ABI) onboard the GOES-18 satellite. NOAA\u2019s GOES-18 (aka, GOES-T) was launched on March 1, 2022, replacing GOES-17 as GOES West in January 2023. It is the third satellite in the geostationary GOES\u2013R Series, the Western Hemisphere\u2019s most sophisticated weather-observing and environmental-monitoring system. The Advanced Baseline Imager (ABI) is the primary instrument on the GOES-R Series for imaging Earth\u2019s weather, oceans, and environment. <br><br>\r\nThe G18-ABI-L3C-ACSPO-v2.90 dataset is a gridded version of the G18-ABI-L2P-ACSPO-v2.90 dataset (https://podaac.jpl.nasa.gov/dataset/G18-ABI-L2P-ACSPO-v2.90).  The L3C (Level 3 Collated) output files reported hourly, 24 granules per day, with a daily volume of 1.2 GB/day.  Valid SSTs are found over oceans, sea, lakes or rivers, with fill values reported elsewhere. All valid SSTs in L3C are recommended for users, although data over internal waters may not have enough in situ data to be adequately validated. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (bias and standard deviation) are reported in each pixel with valid SST. <br><br>\r\nThe ACSPO G18/ABI L3C product is continuously monitored and validated against iQuam in situ data (Xu and Ignatov, 2014) in SQUAM (Dash et al, 2010). The NRT files are replaced with Delayed Mode (DM) files, with a latency of ~2-months. File names remain unchanged, and DM vs NRT can be identified by different time stamps and global attributes inside the files (MERRA instead of GFS for atmospheric profiles, and same day CMC L4 analyses in DM instead of one-day delayed in NRT processing).",
-            "release-place": "Camp Springs, MD (USA)",
-            "series-name": "GHRSST L3C ACSPO America Region SST from GOES ABI",
             "creator": "NOAA/NESDIS/STAR",
-            "title": "GHRSST L3C NOAA/ACSPO GOES-18/ABI  America Region Sea Surface Temperature v2.90 dataset",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/G18-ABI-L3C-ACSPO-v2.90.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The G18-ABI-L3C-ACSPO-v2.90 dataset produced by the NOAA Advanced Clear Sky Processor for Ocean (ACSPO) system is used to derive Sea Surface Skin Temperature (SST) from he Advanced Baseline Imager (ABI) onboard the GOES-18 satellite. NOAA\u2019s GOES-18 (aka, GOES-T) was launched on March 1, 2022, replacing GOES-17 as GOES West in January 2023. It is the third satellite in the geostationary GOES\u2013R Series, the Western Hemisphere\u2019s most sophisticated weather-observing and environmental-monitoring system. The Advanced Baseline Imager (ABI) is the primary instrument on the GOES-R Series for imaging Earth\u2019s weather, oceans, and environment. <br><br>\r\nThe G18-ABI-L3C-ACSPO-v2.90 dataset is a gridded version of the G18-ABI-L2P-ACSPO-v2.90 dataset (https://podaac.jpl.nasa.gov/dataset/G18-ABI-L2P-ACSPO-v2.90).  The L3C (Level 3 Collated) output files reported hourly, 24 granules per day, with a daily volume of 1.2 GB/day.  Valid SSTs are found over oceans, sea, lakes or rivers, with fill values reported elsewhere. All valid SSTs in L3C are recommended for users, although data over internal waters may not have enough in situ data to be adequately validated. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (bias and standard deviation) are reported in each pixel with valid SST. <br><br>\r\nThe ACSPO G18/ABI L3C product is continuously monitored and validated against iQuam in situ data (Xu and Ignatov, 2014) in SQUAM (Dash et al, 2010). The NRT files are replaced with Delayed Mode (DM) files, with a latency of ~2-months. File names remain unchanged, and DM vs NRT can be identified by different time stamps and global attributes inside the files (MERRA instead of GFS for atmospheric profiles, and same day CMC L4 analyses in DM instead of one-day delayed in NRT processing).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHG18-3CO29%0D%0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHG18-3CO29%0D%0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/ghrsst",
-                    "description": "GHRSST Global Data Assembly Center",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Global Data Assembly Center",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/ghrsst",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/G18-ABI-L3C-ACSPO-v2.90.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/G18-ABI-L3C-ACSPO-v2.90.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ghrsst.org/",
-                    "description": "GHRSST Project",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project",
+                    "downloadURL": "https://www.ghrsst.org/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2731041317-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2731041317-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2731041317-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2731041317-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/G18-ABI-L3C-ACSPO-v2.90.jpg",
+            "identifier": "C2731041317-POCLOUD",
+            "issued": "2020-03-31",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHG18-3CO29",
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
+                "https://doi.org/10.1117/1.JRS.11.032405"
+            ],
+            "release-place": "Camp Springs, MD (USA)",
+            "series-name": "GHRSST L3C ACSPO America Region SST from GOES ABI",
             "spatial": "163.0 -60.0 -77.0 60.0",
+            "temporal": "2022-06-07T00:00:00Z/2023-07-31T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST L3C NOAA/ACSPO GOES-18/ABI  America Region Sea Surface Temperature v2.90 dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/9T4EPQXTJYW9",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs Annual Antarctic Ice Velocity Maps V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/9T4EPQXTJYW9.",
-            "issued": "2000-07-01",
-            "temporal": "2000-07-01T00:00:00Z/2020-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-30",
-            "keyword": [
-                "earth science",
-                "snow/ice",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Rignot",
                 "hasEmail": "mailto:erignot@uci.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C2245171699-NSIDC_ECS",
             "description": "This data set, part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, provides annual maps of Antarctic ice velocity. The maps are assembled using SAR data from the Japanese Space Agency's (JAXA) ALOS PALSAR, the European Space Agency's (ESA) ENVISAT ASAR and Copernicus Sentinel-1, the Canadian Space  Agency's (CSA) RADARSAT-1, RADARSAT-2, the German Aerospace Agency's (DLR) TerraSAR-X (TSX) and TanDEM \u2013X (TDX), and the U.S. Geological Survey's (USGS) Landsat-8 optical imagery..\n\nSee <a href=\"https://nsidc.org/data/measures/aiv\">Antarctic Ice Sheet Velocity and Mapping Data</a> for related data.",
-            "title": "MEaSUREs Annual Antarctic Ice Velocity Maps V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9T4EPQXTJYW9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9T4EPQXTJYW9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0720.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0720.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0720+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0720+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0720/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0720/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9T4EPQXTJYW9",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/9T4EPQXTJYW9",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9T4EPQXTJYW9",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/9T4EPQXTJYW9",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2245171699-NSIDC_ECS",
+            "issued": "2000-07-01",
+            "keyword": [
+                "earth science",
+                "snow/ice",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/9T4EPQXTJYW9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -60.0",
+            "temporal": "2000-07-01T00:00:00Z/2020-06-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs Annual Antarctic Ice Velocity Maps V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V11.0",
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
+            "description": "Absolute magnitudes and slopes, mostly IAU-adopted with exceptions noted, for all asteroids numbered as of the 2007 April 2 batch of Minor Planet Circulars.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v11.0_5srt-ku8d",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V11.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v11.0_5srt-ku8d",
-            "description": "Absolute magnitudes and slopes, mostly IAU-adopted with exceptions noted, for all asteroids numbered as of the 2007 April 2 batch of Minor Planet Circulars.",
-            "title": "ASTEROID ABSOLUTE MAGNITUDES V11.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID ABSOLUTE MAGNITUDES V11.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2378",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Madani, N., N.C. Parazoo, M. Manizza, A. Chatterjee, D. Carroll, D. Menemenlis, V. Le Fouest, A. Matsuoka, K.M. Luis, C. Serra-Pompei, and C.E. Miller. 2024. Monthly SIF Estimates from TROPOMI over the Arctic Ocean, 2004-2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2378",
-            "issued": "2024-10-31",
-            "temporal": "2004-01-01T00:00:00Z/2020-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
-            "keyword": [
-                "ecosystems",
-                "ecological dynamics",
-                "earth science",
-                "ocean optics",
-                "biosphere",
-                "oceans"
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
-            "identifier": "C3282002388-ORNL_CLOUD",
             "description": "This dataset provides solar-induced chlorophyll fluorescence (SIF) estimates over the Arctic Ocean at a 0.05-degree resolution for each month from January 2004 through December 2020. Red SIF data from TROPOspheric Monitoring Instrument (TROPOMI) (2018 to 2021) were extended over the study period using a random forest machine learning model trained using TROPOMI SIF climatological records. These data are useful for monitoring the physiological responses of phytoplankton to ongoing climate change over this ocean region. The data are provided in cloud optimized GeoTIFF format.",
-            "graphic-preview-description": "Monthly average solar-induced fluorescence (SIF) for Arctic Ocean for June 2004.  Source: TROPOMI_ArcticOcean_SIF_2004_06.tif",
-            "title": "Monthly SIF Estimates from TROPOMI over the Arctic Ocean, 2004-2020",
-            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/TROPOMI_SIF_Arctic_Ocean_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2378",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2378",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/sif-esdr/17-MEASURES-0032/TROPOMI_SIF_Arctic_Ocean/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/sif-esdr/17-MEASURES-0032/TROPOMI_SIF_Arctic_Ocean/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/TROPOMI_SIF_Arctic_Ocean.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/TROPOMI_SIF_Arctic_Ocean.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2378",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2378",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/TROPOMI_SIF_Arctic_Ocean/comp/TROPOMI_SIF_Arctic_Ocean.pdf",
-                    "description": "Monthly SIF Estimates from TROPOMI over the Arctic Ocean, 2004-2020: TROPOMI_SIF_Arctic_Ocean.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Monthly SIF Estimates from TROPOMI over the Arctic Ocean, 2004-2020: TROPOMI_SIF_Arctic_Ocean.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/TROPOMI_SIF_Arctic_Ocean/comp/TROPOMI_SIF_Arctic_Ocean.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/TROPOMI_SIF_Arctic_Ocean_Fig1.jpg",
-                    "description": "Monthly average solar-induced fluorescence (SIF) for Arctic Ocean for June 2004.  Source: TROPOMI_ArcticOcean_SIF_2004_06.tif",
                     "@type": "dcat:Distribution",
+                    "description": "Monthly average solar-induced fluorescence (SIF) for Arctic Ocean for June 2004.  Source: TROPOMI_ArcticOcean_SIF_2004_06.tif",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/TROPOMI_SIF_Arctic_Ocean_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science.jpl.nasa.gov/projects/measures/",
-                    "description": "Project site",
                     "@type": "dcat:Distribution",
+                    "description": "Project site",
+                    "downloadURL": "https://science.jpl.nasa.gov/projects/measures/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Monthly average solar-induced fluorescence (SIF) for Arctic Ocean for June 2004.  Source: TROPOMI_ArcticOcean_SIF_2004_06.tif",
+            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/TROPOMI_SIF_Arctic_Ocean_Fig1.jpg",
+            "identifier": "C3282002388-ORNL_CLOUD",
+            "issued": "2024-10-31",
+            "keyword": [
+                "ecosystems",
+                "ecological dynamics",
+                "earth science",
+                "ocean optics",
+                "biosphere",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2378",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 50.0 180.0 90.0",
+            "temporal": "2004-01-01T00:00:00Z/2020-12-31T23:59:59Z",
             "theme": [
                 "SIF-ESDR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly SIF Estimates from TROPOMI over the Arctic Ocean, 2004-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M27-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-03-08T23:25:00.000 to 2016-04-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m27-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M27-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m27-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-03-08T23:25:00.000 to 2016-04-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP027 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP027 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0258-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-30T15:22:05.000 to 2014-08-30T17:55:48.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0258-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0258-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0258-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-30T15:22:05.000 to 2014-08-30T17:55:48.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0258 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0258 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alab.hydrocarbon_spectra&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "________",
+            "identifier": "urn:nasa:pds:lab.hydrocarbon_spectra",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "hydrocarbon infrared spectra; gas giants and titan",
                 "laboratory analog saturn",
@@ -208265,337 +208267,311 @@
                 "cross section ir spectroscopy of hydrocarbons in planetary atmospheres",
                 "laboratory analog jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alab.hydrocarbon_spectra&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:lab.hydrocarbon_spectra",
-            "description": "________",
-            "title": "Laboratory Study of Hydrocarbon IR Spectra Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Laboratory Study of Hydrocarbon IR Spectra Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1296-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-29T22:09:40.000 to 2015-12-30T00:16:04.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1296-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1296-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1296-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-29T22:09:40.000 to 2015-12-30T00:16:04.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1296 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1296 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-RASTER-1.1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2023-11-30. SWOT Level 2 Water Mask Raster Image Data Product. Version 1.1. SWOT Level 2 Water Mask Raster Image Data Product, Version 1.1. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.5067/SWOT-RASTER-1.1. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-06-28",
-            "temporal": "2022-12-16T00:00:00Z/2023-12-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-28",
-            "keyword": [
-                "ocean waves",
-                "earth science",
-                "oceans",
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
-            "identifier": "C2765423410-POCLOUD",
-            "description": "Rasterized water surface elevation and inundation extent in geographically fixed tiles at resolutions of 100 m and 250 m in a Universal Transverse Mercator projection grid. Provides rasters with water surface elevation, area, water fraction, backscatter, geophysical information. On-demand processing available to users for different resolutions, sampling grids, scene sizes, and file formats. Gridded scene (approx 128x128 km2, georeferenced); full swath. Available in netCDF-4 file format.",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 Water Mask Raster Image Data Product",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Water Mask Raster Image Data Product, Version 1.1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_DEFAULT_THUMBNAIL.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Rasterized water surface elevation and inundation extent in geographically fixed tiles at resolutions of 100 m and 250 m in a Universal Transverse Mercator projection grid. Provides rasters with water surface elevation, area, water fraction, backscatter, geophysical information. On-demand processing available to users for different resolutions, sampling grids, scene sizes, and file formats. Gridded scene (approx 128x128 km2, georeferenced); full swath. Available in netCDF-4 file format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-RASTER-1.1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-RASTER-1.1",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2765423410-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2765423410-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2765423410-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2765423410-POCLOUD",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56416_SWOT_Product_Description_L2_HR_Raster_20220919_RevA.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56416_SWOT_Product_Description_L2_HR_Raster_20220919_RevA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_DEFAULT_THUMBNAIL.jpg",
+            "identifier": "C2765423410-POCLOUD",
+            "issued": "2022-06-28",
+            "keyword": [
+                "ocean waves",
+                "earth science",
+                "oceans",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-RASTER-1.1",
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
+            "release-place": "Jet Propulsion Laboratory",
+            "series-name": "SWOT Level 2 Water Mask Raster Image Data Product",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2023-12-04T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Water Mask Raster Image Data Product, Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-2-JUPITER-V3.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 3.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-2-jupiter-v3.0_5syy-7e7w",
+            "issued": "2018-09-05",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-2-JUPITER-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-2-jupiter-v3.0_5syy-7e7w",
-            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 3.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SWAP JUPITER ENCOUNTER                                                  \n      RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      SWAP JUPITER ENCOUNTER                                                  \n      RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/GMI/GPROFCLIM/3A-DAY/07",
             "citation": "Christian Kummerow. 2022-05-09. GPM_3GPROFGPMGMI_DAY_CLIM. Version 07. GPM GMI (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/GMI/GPROFCLIM/3A-DAY/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGPMGMI_DAY_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-03-04T00:00:00Z/2023-03-01T00:00:00Z",
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
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "Christian Kummerow",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2259345664-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3GPROFGPMGMI_DAY_CLIM",
-            "creator": "Christian Kummerow",
-            "title": "GPM GMI (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree  V07 (GPM_3GPROFGPMGMI_DAY_CLIM) at GES DISC",
-            "graphic-preview-description": "GMI GPROF Precipitation Estimate (GPM_3GPROFGPMGMI_DAY)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGPMGMI_DAY_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FGMI%2FGPROFCLIM%2F3A-DAY%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FGMI%2FGPROFCLIM%2F3A-DAY%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGPMGMI_DAY_CLIM_07.png",
-                    "description": "GMI GPROF Precipitation Estimate (GPM_3GPROFGPMGMI_DAY)",
                     "@type": "dcat:Distribution",
+                    "description": "GMI GPROF Precipitation Estimate (GPM_3GPROFGPMGMI_DAY)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGPMGMI_DAY_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGPMGMI_DAY_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGPMGMI_DAY_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFGPMGMI_DAY_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFGPMGMI_DAY_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFGPMGMI_DAY_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFGPMGMI_DAY_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFGPMGMI_DAY_CLIM_07.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFGPMGMI_DAY_CLIM_07.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFGPMGMI_DAY_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFGPMGMI_DAY_CLIM_07",
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
@@ -208605,273 +208581,298 @@
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
-                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "GMI GPROF Precipitation Estimate (GPM_3GPROFGPMGMI_DAY)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGPMGMI_DAY_CLIM_07.png",
+            "identifier": "C2259345664-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/GMI/GPROFCLIM/3A-DAY/07",
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
+            "series-name": "GPM_3GPROFGPMGMI_DAY_CLIM",
             "spatial": "-180.0 -70.0 180.0 70.0",
+            "temporal": "2014-03-04T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GMI (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree  V07 (GPM_3GPROFGPMGMI_DAY_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LEISA-2-LAUNCH-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-leisa-2-launch-v1.1_5t3p-yk7q",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "new horizons",
                 "132524 apl"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LEISA-2-LAUNCH-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-leisa-2-launch-v1.1_5t3p-yk7q",
-            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS LEISA POST-LAUNCH CHECKOUT V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS LEISA POST-LAUNCH CHECKOUT V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3354-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-19T05:22:40.000 to 2012-07-19T07:48:00.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3354-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3354-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3354-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-19T05:22:40.000 to 2012-07-19T07:48:00.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3354 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3354 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-CR4B-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft.  These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the CRUISE 4B mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-cr4b-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-CR4B-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-cr4b-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft.  These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the CRUISE 4B mission phase.",
-            "title": "ROSETTA-ORBITER X SREM 5 CRUISE 4B\n    V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER X SREM 5 CRUISE 4B\n    V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/R3TN4LOIKDMC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge DMS L3 Ames Stereo Pipeline Orthorectified Images V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/R3TN4LOIKDMC.",
-            "issued": "2009-10-16",
-            "temporal": "2009-10-16T00:00:00Z/2017-07-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-25",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Oleg Alexandrov",
                 "hasEmail": "mailto:oleg.alexandrov@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1552255037-NSIDC_ECS",
             "description": "This data set represents a collection of orthorectified images obtained by processing Operation IceBridge DMS stereo images and lidar data using the NASA Ames Stereo Pipeline.",
-            "title": "IceBridge DMS L3 Ames Stereo Pipeline Orthorectified Images V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FR3TN4LOIKDMC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FR3TN4LOIKDMC",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODIM3.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODIM3.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1552255037-NSIDC_ECS&m=-50.34375%212.25%211%211%210%210%2C2&tl=1522851215%214%21%21&q=IODIM3&ok=IODIM3",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1552255037-NSIDC_ECS&m=-50.34375%212.25%211%211%210%210%2C2&tl=1522851215%214%21%21&q=IODIM3&ok=IODIM3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODIM3/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODIM3/versions/1/",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODIM3.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODIM3.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1552255037-NSIDC_ECS&m=-50.34375%212.25%211%211%210%210%2C2&tl=1522851215%214%21%21&q=IODIM3&ok=IODIM3",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1552255037-NSIDC_ECS&m=-50.34375%212.25%211%211%210%210%2C2&tl=1522851215%214%21%21&q=IODIM3&ok=IODIM3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODIM3/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODIM3/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/R3TN4LOIKDMC",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/R3TN4LOIKDMC",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/R3TN4LOIKDMC",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/R3TN4LOIKDMC",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1552255037-NSIDC_ECS",
+            "issued": "2009-10-16",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/R3TN4LOIKDMC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-07-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2009-10-16T00:00:00Z/2017-07-25T23:59:59.999Z",
             "theme": [
                 "2009_AK_NASA",
                 "2009_AN_NASA",
@@ -208900,449 +208901,474 @@
                 "2017_GR_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge DMS L3 Ames Stereo Pipeline Orthorectified Images V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_SAFARI_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-12-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/AIRMISR_SAFARI_1.",
-            "issued": "2001-05-21",
-            "temporal": "2000-09-06T00:00:00Z/2000-09-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CAROL BRUEGGE",
                 "hasEmail": "mailto:carol.j.bruegge@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000726-LARC_ASDC",
             "description": "The AIRMISR_SAFARI data were acquired on September 6, 7, 13 and 14, 2000 during the SAFARI 2000 campaign. The Southern African Fire Atmosphere Research Initiative (SAFARI) 2000 field campaign focused on the smoke and gases released into the environment of southern Africa by industrial, biological and man-made sources such as biomass burning. The area of study included Botswana, Lesotho, Malawi, Mozambique, Namibia, South Africa, Swaziland, Zambia, and Zimbabwe. The Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) is an airborne instrument for obtaining multi-angle imagery similar to that of the satellite-borne Multi-angle Imaging SpectroRadiometer (MISR) instrument, which is designed to contribute to studies of the Earth's ecology and climate. AirMISR flies on the NASA ER-2 aircraft. The Jet Propulsion Laboratory in Pasadena, California built the instrument for NASA.Unlike the satellite-borne MISR instrument, which has nine cameras oriented at various angles, AirMISR uses a single camera in a pivoting gimbal mount. A data run by the ER-2 aircraft is divided into nine segments, each with the camera positioned to a MISR look angle. The gimbal rotates between successive segments, such that each segment acquires data over the same area on the ground as the previous segment. This process is repeated until all nine angles of the target area are collected. The swath width, which varies from 11 km in the nadir to 32 km at the most oblique angle, is governed by the camera's instantaneous field-of-view of 7 meters cross-track x 6 meters along-track in the nadir view and 21 meters x 55 meters at the most oblique angle. The along-track image length at each angle is dictated by the timing required to obtain overlap imagery at all angles, and varies from about 9 km in the nadir to 26 km at the most oblique angle. Thus, the nadir image dictates the area of overlap that is obtained from all nine angles. A complete flight run takes approximately 13 minutes.The 9 camera viewing angles are:0 degrees or nadir26.1 degrees, fore and aft45.6 degrees, fore and aft60.0 degrees, fore and aft70.5 degrees, fore and aftFor each of the camera angles, images are obtained at 4 spectral bands. The spectral bands can be used to identify vegetation and aerosols, estimate surface reflectance and ocean color studies. The center wavelengths of the 4 spectral bands are:443 nanometers, blue555 nanometers, green670 nanometers, red865 nanometers, near-infraredTwo types of AirMISR data products are available - the Level 1 Radiometric product (L1B1) and the Level 1 Georectified radiance product (L1B2).",
-            "graphic-preview-description": "AirMISR Campaign Imagery: AirMISR Red Band Browse Images from the SAFARI 2000 Field Campaign, September 6, 2000",
-            "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the Southern African Fire Atmosphere Research Initiative 2000 Field Campaign",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_SAFARI_images.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_SAFARI_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_SAFARI_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMISR",
-                    "description": "ASDC Data and Information for AirMISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for AirMISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMISR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/Mission/airMISR/",
-                    "description": "AirMISR project home page",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR project home page",
+                    "downloadURL": "https://misr.jpl.nasa.gov/Mission/airMISR/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000726-LARC_ASDC",
-                    "description": "Earthdata Search for AIRMISR_SAFARI_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for AIRMISR_SAFARI_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000726-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/content/SAFARI_2000",
-                    "description": "ESPO home page for SAFARI 2000",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO home page for SAFARI 2000",
+                    "downloadURL": "https://espo.nasa.gov/content/SAFARI_2000",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_read_software.pdf",
-                    "description": "AirMISR Read Software Document Readme",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Read Software Document Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_read_software.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/read_software/read_airmisr.pro",
-                    "description": "Readme to open and read AIRMISR L1B2 GP (Georectified Radiance Product) HDF-EOS data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to open and read AIRMISR L1B2 GP (Georectified Radiance Product) HDF-EOS data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/read_software/read_airmisr.pro",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_safari",
-                    "description": "AirMISR_SAFARI Data Set Readme",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR_SAFARI Data Set Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_safari",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/quality_summaries/airmisr_safari.pdf",
-                    "description": "Quality Summary: AirMISR SAFARI",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: AirMISR SAFARI",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/quality_summaries/airmisr_safari.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_SAFARI_1",
-                    "description": "DOI data set landing page for AIRMISR_SAFARI_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for AIRMISR_SAFARI_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_SAFARI_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_F01.pdf",
-                    "description": "AirMISR Data Products Specifications, December 21, 2000",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Data Products Specifications, December 21, 2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_F01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS.pdf",
-                    "description": "AirMISR Data Products Specifications, Rev. A, December 21,2000",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Data Products Specifications, Rev. A, December 21,2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_RevC.pdf",
-                    "description": "AirMISR Data Products Specifications, Rev. C, December 21,2000",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Data Products Specifications, Rev. C, December 21,2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_RevC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.tar",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/using_airmisr_data.pdf",
-                    "description": "ASDC Documents for Using AirMISR Data",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Documents for Using AirMISR Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/using_airmisr_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
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
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/FieryTemperament",
-                    "description": "NASA Earth ObservatoryArticle: \"Fiery Temperament\" By Michon Scott, May 14, 2002",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth ObservatoryArticle: \"Fiery Temperament\" By Michon Scott, May 14, 2002",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/FieryTemperament",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolMonterey.pdf",
-                    "description": "Journal of Geophysical Research Article: \"Aerosol properties derived from aircraft multiangle imagingover Monterey Bay\" by Ralph Kahn, Pranab Banerjee, Duncan McDonald, and John Martonchik, June 16, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "Journal of Geophysical Research Article: \"Aerosol properties derived from aircraft multiangle imagingover Monterey Bay\" by Ralph Kahn, Pranab Banerjee, Duncan McDonald, and John Martonchik, June 16, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolMonterey.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolRetrieval.pdf",
-                    "description": "Journal of Geophysical Research Article: \"Sensitivity of multiangle imaging to natural mixturesof aerosols over ocean\" by Ralph Kahn, Pranab Banerjee, and Duncan McDonald, August 27, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "Journal of Geophysical Research Article: \"Sensitivity of multiangle imaging to natural mixturesof aerosols over ocean\" by Ralph Kahn, Pranab Banerjee, and Duncan McDonald, August 27, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolRetrieval.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://misr.jpl.nasa.gov/",
-                    "description": "MISR project home page",
                     "@type": "dcat:Distribution",
+                    "description": "MISR project home page",
+                    "downloadURL": "https://misr.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "mediaType": "text/html",
```

