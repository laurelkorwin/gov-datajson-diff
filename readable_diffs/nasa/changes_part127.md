# Change History for nasa.json (Part 127)

### Changes from 31606f9 to dd2190f (Part 116/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "title": "SMAPVEX16 Iowa Temporary Network Soil Moisture and Temperature V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCP6MNQ7I7ZRC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCP6MNQ7I7ZRC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16I_TNET.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16I_TNET.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990799792-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&m=37.93418934207473%21-110.109375%214%211%210%210%2C2&tl=1594227826%214",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990799792-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&m=37.93418934207473%21-110.109375%214%211%210%210%2C2&tl=1594227826%214",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16I_TNET/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16I_TNET/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CP6MNQ7I7ZRC",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CP6MNQ7I7ZRC",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CP6MNQ7I7ZRC",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CP6MNQ7I7ZRC",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2011917195-NSIDC_ECS",
+            "issued": "2016-05-18",
+            "keyword": [
+                "soils",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/CP6MNQ7I7ZRC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-08-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-93.57 42.29 -93.22 42.64",
+            "temporal": "2016-05-18T00:00:00Z/2016-08-17T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX16 Iowa Temporary Network Soil Moisture and Temperature V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-2-EDR-CRUISE4-V1.0",
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
-                "solar system",
-                "near earth asteroid rendezvous"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-2-edr-cruise4-v1.0_pygc-xh6b",
+            "issued": "2018-06-26",
+            "keyword": [
+                "solar system",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-2-EDR-CRUISE4-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-2-edr-cruise4-v1.0_pygc-xh6b",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR NLR DATA FOR CRUISE4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR NLR DATA FOR CRUISE4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCMAG-3-RVM1-CALIBRATED-V3.0",
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
+            "description": "This dataset contains CALIBRATED DATA of  the mission phase\nRENDEZVOUS MANOEUVRE 1 (RVM1) of the ROSETTA\norbiter magnetometer RPCMAG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcmag-3-rvm1-calibrated-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCMAG-3-RVM1-CALIBRATED-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcmag-3-rvm1-calibrated-v3.0",
-            "description": "This dataset contains CALIBRATED DATA of  the mission phase\nRENDEZVOUS MANOEUVRE 1 (RVM1) of the ROSETTA\norbiter magnetometer RPCMAG.",
-            "title": "ROSETTA-ORBITER SW RPCMAG 3 RVM1 CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SW RPCMAG 3 RVM1 CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-NALT-OGDR-1.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2023-06-01. SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA. Version 1.0. SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA Version 1.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWOT-NALT-OGDR-1.0.",
-            "issued": "2022-06-28",
-            "temporal": "2022-12-16T00:00:00Z/2023-08-14T00:00:00Z",
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
-            "identifier": "C2628593693-POCLOUD",
-            "description": "Same as L2_NALT_GDR using predicted values for some auxiliary data, and does not have GIM ionosphere model values. Uses the onboard DORIS orbit ephemeris. Available with latency of < 7 hours. Discrete measurements at nadir for each data downlink, along the ground track. Available in netCDF-4 file format.",
-            "series-name": "SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA Version 1.0",
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
+            "identifier": "C2628593693-POCLOUD",
+            "issued": "2022-06-28",
+            "keyword": [
+                "ocean waves",
+                "earth science",
+                "oceans",
+                "sea surface topography"
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
+            "temporal": "2022-12-16T00:00:00Z/2023-08-14T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCICA-2-ESC3-RAW-V2.0",
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
+            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during Comet escort 3.\nData contains measurements of solar wind interaction\nwith the atmosphere of target comet 67P.\nData set version 2 replaces a previously delivered data set.\nImportant changes are the ordering of the energy levels which now\ngo from low to high and that the quality flag in the labels is\nupdated.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcica-2-esc3-raw-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCICA-2-ESC3-RAW-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcica-2-esc3-raw-v2.0",
-            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during Comet escort 3.\nData contains measurements of solar wind interaction\nwith the atmosphere of target comet 67P.\nData set version 2 replaces a previously delivered data set.\nImportant changes are the ordering of the energy levels which now\ngo from low to high and that the quality flag in the labels is\nupdated.",
-            "title": "ROSETTA-ORBITER 67P RPCICA 2 ESC3 UNCALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCICA 2 ESC3 UNCALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC3-MTP021-V1.0",
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
+            "description": "This dataset contains EDITED data from Rosetta RPC-LAP, acquired during MTP21, part of the COMET ESCORT 3 mission phase. The primary target was comet 67P/C-G.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc3-mtp021-v1.0_pyu4-mh2t",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC3-MTP021-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc3-mtp021-v1.0_pyu4-mh2t",
-            "description": "This dataset contains EDITED data from Rosetta RPC-LAP, acquired during MTP21, part of the COMET ESCORT 3 mission phase. The primary target was comet 67P/C-G.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2 ESC3\n        MTP021 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2 ESC3\n        MTP021 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0028-4-SBN0001%2FSMASSII-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains visible-wavelength (0.435-0.925 micron) spectra for 1341 main-belt asteroids observed during the second phase of the Small Main-belt Asteroid Spectroscopic Survey (SMASSII) between August 1993 and March 1999. The purpose of the SMASSII survey was to provide a new basis for studying the compositional diversity and structure of the asteroid belt. Based on experiences gained from the earlier SMASS survey, SMASSII focused on producing an even larger, internally consistent set of CCD spectra for small (D < 20 km) main-belt asteroids. The observing strategies and procedures used during SMASSII roughly parallel those used in the first survey (Xu et al. Icarus 115 1-35, 1995 [XUETAL1995]), though several minor changes were made in instrumentation and in portions of the data reduction process.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0028-4-sbn0001-smassii-v1.0_pyuc-ea53",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "571 dulcinea",
                 "570 kythera",
@@ -1217051,228 +1217053,240 @@
                 "1181 lilith",
                 "2029 binomi"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0028-4-SBN0001%2FSMASSII-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0028-4-sbn0001-smassii-v1.0_pyuc-ea53",
-            "description": "This data set contains visible-wavelength (0.435-0.925 micron) spectra for 1341 main-belt asteroids observed during the second phase of the Small Main-belt Asteroid Spectroscopic Survey (SMASSII) between August 1993 and March 1999. The purpose of the SMASSII survey was to provide a new basis for studying the compositional diversity and structure of the asteroid belt. Based on experiences gained from the earlier SMASS survey, SMASSII focused on producing an even larger, internally consistent set of CCD spectra for small (D < 20 km) main-belt asteroids. The observing strategies and procedures used during SMASSII roughly parallel those used in the first survey (Xu et al. Icarus 115 1-35, 1995 [XUETAL1995]), though several minor changes were made in instrumentation and in portions of the data reduction process.",
-            "title": "SMALL MAIN-BELT ASTEROID SPECTROSCOPIC SURVEY, PHASE II",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SMALL MAIN-BELT ASTEROID SPECTROSCOPIC SURVEY, PHASE II"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V2.0",
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
+            "description": "This is a compilation of published lightcurve results up through 23 January, 1996. This compilation is maintained by Alan Harris, JPL.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v2.0_pyus-egzt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v2.0_pyus-egzt",
-            "description": "This is a compilation of published lightcurve results up through 23 January, 1996. This compilation is maintained by Alan Harris, JPL.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-2-PLUTO-V2.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons                Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains PEPSSI observations taken during the              the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-2-pluto-v2.0_pyzs-tez5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-2-PLUTO-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-2-pluto-v2.0_pyzs-tez5",
-            "description": "This data set contains Raw data taken by the New Horizons                Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains PEPSSI observations taken during the              the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
-            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2561589530-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-13",
-            "keyword": [
-                "marine environment monitoring",
-                "oceans",
-                "surface water",
-                "environmental advisories",
-                "ecosystems",
-                "terrestrial hydrosphere",
-                "water quality/water chemistry",
-                "earth science services",
-                "earth science",
-                "coastal processes",
-                "biosphere",
-                "biological classification",
-                "bacteria/archaea",
-                "hydrological advisories",
-                "aquatic sciences",
-                "human dimensions",
-                "environmental governance/management"
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
-            "identifier": "C2561589530-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of\nancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than\noptimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Merged Sentinel-3A and Sentinel-3B OLCI Global Mapped Cyanobacteria Index (CI) - Near Real-time (NRT) Data, version 5.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/MERGED_S3/OLCI/L3M/CYAN/CI/5",
-                    "description": "Merged Sentinel-3A and Sentinel-3B OLCI L3M Cyanobacteria Index (CI) - Near Real-time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Merged Sentinel-3A and Sentinel-3B OLCI L3M Cyanobacteria Index (CI) - Near Real-time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/MERGED_S3/OLCI/L3M/CYAN/CI/5",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2561589530-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "marine environment monitoring",
+                "oceans",
+                "surface water",
+                "environmental advisories",
+                "ecosystems",
+                "terrestrial hydrosphere",
+                "water quality/water chemistry",
+                "earth science services",
+                "earth science",
+                "coastal processes",
+                "biosphere",
+                "biological classification",
+                "bacteria/archaea",
+                "hydrological advisories",
+                "aquatic sciences",
+                "human dimensions",
+                "environmental governance/management"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2561589530-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-04-25T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Merged Sentinel-3A and Sentinel-3B OLCI Global Mapped Cyanobacteria Index (CI) - Near Real-time (NRT) Data, version 5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67P-M29-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67p-m29-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67P-M29-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67p-m29-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP029 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP029 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/pz4b-5uyd",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "RR-1 is a validation flight to evaluate the hardware operational and science capabilities of the Rodent Research Project on the ISS. RNA DNA and protein were purified from liver tissues from RR-1 mice (female C57BL/6J 16wk old at time of launch). From each group two liver samples were collected and frozen immediately after euthanasia. The rest of the liver samples from each group were collected from frozen carcasses dissected post-flight. RNA-Seq whole genome and RNA BS-Seq (bisulfite sequencing) and proteomic expression profiling were performed.  xc2 xa0RNA extracted from these tissues was re-sequenced; these data are available as part of GLDS-168 (https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-168). xc2 xa0",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-48",
+                    "mediaType": "text/html",
+                    "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse liver transcriptomic proteomic and epigenomic data"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-48_pz4b-5uyd",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "library construction",
                 "5mc total rna methylation analysis",
@@ -1217294,931 +1217308,926 @@
                 "dna library construction",
                 "mouse habitation protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/pz4b-5uyd",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-48_pz4b-5uyd",
-            "description": "RR-1 is a validation flight to evaluate the hardware operational and science capabilities of the Rodent Research Project on the ISS. RNA DNA and protein were purified from liver tissues from RR-1 mice (female C57BL/6J 16wk old at time of launch). From each group two liver samples were collected and frozen immediately after euthanasia. The rest of the liver samples from each group were collected from frozen carcasses dissected post-flight. RNA-Seq whole genome and RNA BS-Seq (bisulfite sequencing) and proteomic expression profiling were performed.  xc2 xa0RNA extracted from these tissues was re-sequenced; these data are available as part of GLDS-168 (https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-168). xc2 xa0",
-            "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse liver transcriptomic proteomic and epigenomic data",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-48",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse liver transcriptomic proteomic and epigenomic data"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse liver transcriptomic proteomic and epigenomic data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrly_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrly_1.",
-            "issued": "2020-10-05",
-            "temporal": "1988-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-05",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
-                "clouds",
-                "atmosphere"
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
-            "identifier": "C2058673000-LARC_ASDC",
             "description": "GEWEXSRB_Rel4-IP_Longwave_3hrly is the Global Energy and Water Exchanges (GEWEX) Surface Radiation Budget (SRB) Integrated Product (Rel-4) Longwave 3-hourly data product. It contains global fields of 26 longwave surface, Top of Atmosphere (TOA), and atmospheric profile radiative parameters derived with the Longwave algorithm of the NASA World Climate Research Programme/Global Energy and Water-Cycle Experiment (WCRP/GEWEX) Surface Radiation Budget (SRB) Project. This version is known as Release 4-Integrated Product. The fluxes include all-sky, clear-sky and pristine-sky TOA upward fluxes (outgoing longwave radiation, OLR), all-sky, clear-sky and pristine-sky upward and downward fluxes at: tropopause, 200hPa, 500hPa and surface. In addition to the fluxes a day/night flag and a status flag of filled cloud properties are also included. Inputs to the longwave algorithm are cloud information based on ISCCP HXS, meteorology from ISCCP nnHIRS, SeaFlux SST and surface, LandFlux meteorology, and MERRA-2 conditionally. The temporal range is January 1988 through December 2009, with the ends bound by input constraints. Data collection for this product is complete.",
-            "title": "GEWEX SRB Integrated Product (Rel-4) Longwave 3-Hourly  Fluxes",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Longwave_3hrly_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Longwave_3hrly_1",
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
-                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrly_1",
-                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_3hrly_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_3hrly_1",
+                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrly_1",
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
-                    "description": "SRB Rel4-IP Announcement",
                     "@type": "dcat:Distribution",
+                    "description": "SRB Rel4-IP Announcement",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_Public_Release_Announcement.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_ATBD.pdf",
-                    "description": "SRB Release 4 Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "SRB Release 4 Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2058673000-LARC_ASDC",
-                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Longwave_3hrly_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Longwave_3hrly_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2058673000-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Longwave_3hrly_1/",
-                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Longwave_3hrly_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Longwave_3hrly_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Longwave_3hrly_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Longwave_3hrly_1/contents.html",
-                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Longwave_3hrly_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Longwave_3hrly_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Longwave_3hrly_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2058673000-LARC_ASDC",
+            "issued": "2020-10-05",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrly_1",
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
+            "title": "GEWEX SRB Integrated Product (Rel-4) Longwave 3-Hourly  Fluxes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-EAR1-PC0-V1.0",
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
-                "unknown",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the ROSETTA Orbiter that will provide 3D images and statistical parameters of pristine cometary particles hitting the detector. This data set includes all data from the EARTH SWING-BY 1 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-ear1-pc0-v1.0_pz5b-bnha",
+            "issued": "2021-05-21",
+            "keyword": [
+                "unknown",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-EAR1-PC0-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-ear1-pc0-v1.0_pz5b-bnha",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the ROSETTA Orbiter that will provide 3D images and statistical parameters of pristine cometary particles hitting the detector. This data set includes all data from the EARTH SWING-BY 1 mission phase.",
-            "title": "ROSETTA-ORBITER CHECK MIDAS 3 EAR1 PC0 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK MIDAS 3 EAR1 PC0 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_RTC-S1_V1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OPERA. OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 validated product (Version 1). Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Alaska Satellite Facility Distributed Active Archive Center. https://doi.org/10.5067/SNWG/OPERA_L2_RTC-S1_V1.",
-            "issued": "2021-01-01",
-            "temporal": "2021-01-01T00:00:00Z/2024-12-02T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-27",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2022.3147472"
-            ],
-            "keyword": [
-                "geomorphic landforms/processes",
-                "tectonics",
-                "solid earth",
-                "land surface",
-                "oceans",
-                "glaciers/ice sheets",
-                "coastal processes",
-                "cryosphere",
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
-            "identifier": "C2777436413-ASF",
-            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Radiometric Terrain Corrected (RTC) SAR Backscatter from Sentinel-1 (S1) validated product consists of radar backscatter normalized with respect to the topography. The product maps signals related to the physical properties of ground scattering objects, such as surface roughness and soil moisture and/or vegetation. The OPERA RTC-S1 product is derived from the original Copernicus Sentinel-1 Interferometric Wide (IW) Single Look Complex (SLC) data, provided by the European Space Agency, with a near global scope and temporal sampling coincident with the availability of S1 SLC data. Each OPERA RTC-S1 product corresponds to a single S1 burst projected onto a pre-defined UTM/Polar stereographic map projection system map grid with a 30-meter spacing. The Copernicus global 30 m (GLO-30) Digital Elevation Model (DEM) is the reference DEM used to correct for the impacts of topography and to geocode the product.  The OPERA RTC-S1 product is normalized to the backscatter coefficient gamma-naught, \u02630,  obtained from the original radar brightness beta-naught, \u03b20,  through radiometric terrain correction.  The RTC-S1 product is distributed as cloud optimized GeoTIFFs with one GeoTIFF file per processed polarization. The RTC-S1 product metadata is provided in the Hierarchical Data Format version 5 (HDF5) format. Due to the S1 mission\u2019s narrow orbital tube, radar-geometry layers such as incidence angle, local incidence angle, number of looks, and RTC Area Normalization Factor (ANF) vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA RTC-S1 product, as they are produced only once or a limited number of times, to account for changes in the DEM, in the S1 orbit, or in the static-layers generation algorithm. The static layers are available in the associated OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 Static Layers validated product (Version 1) dataset.",
-            "graphic-preview-description": "Image to represent the collection",
             "creator": "OPERA",
-            "title": "OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 validated product (Version 1)",
-            "graphic-preview-file": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_RTC-S1_T124-264306-IW2_20231027T043121Z_20231027T184651Z_S1A_30_v1.0_BROWSE.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Radiometric Terrain Corrected (RTC) SAR Backscatter from Sentinel-1 (S1) validated product consists of radar backscatter normalized with respect to the topography. The product maps signals related to the physical properties of ground scattering objects, such as surface roughness and soil moisture and/or vegetation. The OPERA RTC-S1 product is derived from the original Copernicus Sentinel-1 Interferometric Wide (IW) Single Look Complex (SLC) data, provided by the European Space Agency, with a near global scope and temporal sampling coincident with the availability of S1 SLC data. Each OPERA RTC-S1 product corresponds to a single S1 burst projected onto a pre-defined UTM/Polar stereographic map projection system map grid with a 30-meter spacing. The Copernicus global 30 m (GLO-30) Digital Elevation Model (DEM) is the reference DEM used to correct for the impacts of topography and to geocode the product.  The OPERA RTC-S1 product is normalized to the backscatter coefficient gamma-naught, \u02630,  obtained from the original radar brightness beta-naught, \u03b20,  through radiometric terrain correction.  The RTC-S1 product is distributed as cloud optimized GeoTIFFs with one GeoTIFF file per processed polarization. The RTC-S1 product metadata is provided in the Hierarchical Data Format version 5 (HDF5) format. Due to the S1 mission\u2019s narrow orbital tube, radar-geometry layers such as incidence angle, local incidence angle, number of looks, and RTC Area Normalization Factor (ANF) vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA RTC-S1 product, as they are produced only once or a limited number of times, to account for changes in the DEM, in the S1 orbit, or in the static-layers generation algorithm. The static layers are available in the associated OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 Static Layers validated product (Version 1) dataset.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSNWG%2FOPERA_L2_RTC-S1_V1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSNWG%2FOPERA_L2_RTC-S1_V1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
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
-                    "downloadURL": "https://www.jpl.nasa.gov/go/opera/",
-                    "description": "OPERA Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OPERA Project Home Page",
+                    "downloadURL": "https://www.jpl.nasa.gov/go/opera/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asf.alaska.edu/datasets/daac/opera/",
-                    "description": "Landing page for OPERA products",
                     "@type": "dcat:Distribution",
+                    "description": "Landing page for OPERA products",
+                    "downloadURL": "https://asf.alaska.edu/datasets/daac/opera/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_RTC-S1_T124-264306-IW2_20231027T043121Z_20231027T184651Z_S1A_30_v1.0_BROWSE.png",
-                    "description": "Image to represent the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Image to represent the collection",
+                    "downloadURL": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_RTC-S1_T124-264306-IW2_20231027T043121Z_20231027T184651Z_S1A_30_v1.0_BROWSE.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Image to represent the collection",
+            "graphic-preview-file": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_RTC-S1_T124-264306-IW2_20231027T043121Z_20231027T184651Z_S1A_30_v1.0_BROWSE.png",
+            "identifier": "C2777436413-ASF",
+            "issued": "2021-01-01",
+            "keyword": [
+                "geomorphic landforms/processes",
+                "tectonics",
+                "solid earth",
+                "land surface",
+                "oceans",
+                "glaciers/ice sheets",
+                "coastal processes",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_RTC-S1_V1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
+            "references": [
+                "https://doi.org/10.1109/TGRS.2022.3147472"
+            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-01-01T00:00:00Z/2024-12-02T00:00:00Z",
             "theme": [
                 "SNWG/OPERA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 validated product (Version 1)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/REMSENSPOC/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/REMSENSPOC/DATA001.",
-            "issued": "2013-08-26",
-            "temporal": "2013-08-26T10:50:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "ocean temperature",
-                "ocean chemistry",
-                "ocean optics",
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
-            "identifier": "C1633360629-OB_DAAC",
             "description": "Measurements taken for the purpose of validating remote-sensing-derived particulate organic carbon.",
-            "title": "Remote-sensing-derived particulate organic carbon (POC) validation",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FREMSENSPOC%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FREMSENSPOC%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/RemSensPOC/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/RemSensPOC/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360629-OB_DAAC",
+            "issued": "2013-08-26",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "ocean temperature",
+                "ocean chemistry",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/REMSENSPOC/DATA001",
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
+            "temporal": "2013-08-26T10:50:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Remote-sensing-derived particulate organic carbon (POC) validation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566586-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "USGS. 1997-11-01. Global Land Cover Characterization Program. Version 1.2. Archived by National Aeronautics and Space Administration, U.S. Government, USGS. http://landcover.usgs.gov/glcc/.",
-            "issued": "1992-04-01",
-            "temporal": "1992-04-01T00:00:00Z/1993-03-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1993-03-01",
-            "keyword": [
-                "spectral/engineering",
-                "land use/land cover",
-                "land surface",
-                "human dimensions",
-                "environmental governance/management",
-                "ecological dynamics",
-                "earth science",
-                "biosphere",
-                "aquatic ecosystems",
-                "terrestrial ecosystems",
-                "terrestrial hydrosphere",
-                "topography",
-                "vegetation",
-                "visible wavelengths",
-                "surface water"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TYLER STEVENS",
                 "hasEmail": "mailto:Tyler.B.Stevens@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220566586-USGS_LTA",
-            "description": "The Global Land Cover Characterization Project was established to meet science data requirements identified by the International Geosphere and Biosphere Programme (IGBP), and the U. S. Global Change Research Program. The overall goal is to produce flexible large-area land cover databases to meet evolving  requirements of the earth science research community.      \n\nThe project was implemented by the United States Geological Survey/EROS Data Center (EDC), the University of Nebraska-Lincoln (UNL), and the Joint Research (JRC) of European Commission. This effort is part of the National Aeronautic's and Space Administration (NASA) Earth Observing System Pathfinder Program.\n\nFunding for the project was provided by the USGS, NASA, the U.S. Environmental Protection Agency (EPA), National Oceanic and Atmospheric Administration (NOAA), U.S. Forest Service (USFS) , and the United Nations Environment Programme. \n\nThe data base has been adopted by the International Geosphere-Biosphere Programme Data and Information System office (IGBP-DIS) to fill its requirement  for a global 1-km land cover data set.\n      \n[Summary provided by the USGS.]",
             "creator": "USGS",
-            "title": "Global Land Cover Characterization Program",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Land Cover Characterization Project was established to meet science data requirements identified by the International Geosphere and Biosphere Programme (IGBP), and the U. S. Global Change Research Program. The overall goal is to produce flexible large-area land cover databases to meet evolving  requirements of the earth science research community.      \n\nThe project was implemented by the United States Geological Survey/EROS Data Center (EDC), the University of Nebraska-Lincoln (UNL), and the Joint Research (JRC) of European Commission. This effort is part of the National Aeronautic's and Space Administration (NASA) Earth Observing System Pathfinder Program.\n\nFunding for the project was provided by the USGS, NASA, the U.S. Environmental Protection Agency (EPA), National Oceanic and Atmospheric Administration (NOAA), U.S. Forest Service (USFS) , and the United Nations Environment Programme. \n\nThe data base has been adopted by the International Geosphere-Biosphere Programme Data and Information System office (IGBP-DIS) to fill its requirement  for a global 1-km land cover data set.\n      \n[Summary provided by the USGS.]",
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
-                    "downloadURL": "http://mercury.ornl.gov/clearinghouse/send/xsltText2?fileURL=d%3A%5Cmercury_instances%5Cusgs%5Cma%5Charvested%5Cwww.nbii.gov_metadata_mdata_Millennium_nbii_wdc_ma_d_GLCCD.xml&full_datasource=Millennium+Assessment&full_queryString=+text+%3A+Global+text+%3A+Land+text+%3A+Cover+text+%3A+Characterization+text+%3A+Program&ds_id=",
-                    "description": "\n         Metadata in Biological Data Profile format.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Metadata in Biological Data Profile format.\n      ",
+                    "downloadURL": "http://mercury.ornl.gov/clearinghouse/send/xsltText2?fileURL=d%3A%5Cmercury_instances%5Cusgs%5Cma%5Charvested%5Cwww.nbii.gov_metadata_mdata_Millennium_nbii_wdc_ma_d_GLCCD.xml&full_datasource=Millennium+Assessment&full_queryString=+text+%3A+Global+text+%3A+Land+text+%3A+Cover+text+%3A+Characterization+text+%3A+Program&ds_id=",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lpdaac.usgs.gov/glcc/globdoc1_2.asp",
-                    "description": "\n         Global Land Cover Characterization Documentation.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Global Land Cover Characterization Documentation.\n      ",
+                    "downloadURL": "http://lpdaac.usgs.gov/glcc/globdoc1_2.asp",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://landcover.usgs.gov/glcc/",
-                    "description": "\n         Global Land Cover Characterization Program - Links.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Global Land Cover Characterization Program - Links.\n      ",
+                    "downloadURL": "http://landcover.usgs.gov/glcc/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 }
             ],
+            "identifier": "C1220566586-USGS_LTA",
+            "issued": "1992-04-01",
+            "keyword": [
+                "spectral/engineering",
+                "land use/land cover",
+                "land surface",
+                "human dimensions",
+                "environmental governance/management",
+                "ecological dynamics",
+                "earth science",
+                "biosphere",
+                "aquatic ecosystems",
+                "terrestrial ecosystems",
+                "terrestrial hydrosphere",
+                "topography",
+                "vegetation",
+                "visible wavelengths",
+                "surface water"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566586-USGS_LTA.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1993-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOI/USGS/EROS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-04-01T00:00:00Z/1993-03-01T23:59:59.999Z",
             "theme": [
                 "LCCP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Land Cover Characterization Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IFLOODS/NEXRAD/DATA204",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "National Weather Service .2015. GPM GROUND VALIDATION NEXRAD LEVEL II KMPX IFLOODS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IFLOODS/NEXRAD/DATA204",
-            "issued": "2015-03-03",
-            "temporal": "2013-03-29T20:51:00Z/2013-06-18T15:15:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
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
-            "identifier": "C1982568561-GHRC_DAAC",
             "description": "The GPM Ground Validation Next Generation Weather Radar (NEXRAD) Level II IFloodS datasets were collected from four sites (see Table 1) from March 29, 2013 to June 18, 2013 for the GPM Ground Validation Iowa Flood Studies (IFloodS) field campaign in central-northeastern Iowa. Officially, the IFloodS campaign ran from May 1 to June 15, 2013 but the NEXRAD data was collected prior to the start, allowing for the wider period of record. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and select overseas locations. The resulting data includes the base data (Level-II) and the derived products (Level-III). These Level-II datasets include three meteorological base data quantities: reflectivity, mean radial velocity, and spectrum width. The GPM Ground Validation NEXRAD Level II IFloodS data files are in a custom binary format; the visualization and decoding of the data requires specialized software. Browse imagery is available in PNG file format.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "GPM GROUND VALIDATION NEXRAD LEVEL II KMPX IFLOODS V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD2/KMPX/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIFLOODS%2FNEXRAD%2FDATA204",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIFLOODS%2FNEXRAD%2FDATA204",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkmpx2ifld",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkmpx2ifld",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD2/KMPX/browse/2013-06-04/Level2_KMPX_20130604_0851_ELEV_01.png",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD2/KMPX/browse/2013-06-04/Level2_KMPX_20130604_0851_ELEV_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IFLOODS/DATA101",
-                    "description": "IFloodS Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IFloodS Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IFLOODS/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncdc.noaa.gov/data-access/radar-data/nexrad",
-                    "description": "NEXRAD",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD",
+                    "downloadURL": "https://www.ncdc.noaa.gov/data-access/radar-data/nexrad",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://catalog.data.gov/dataset/noaa-next-generation-radar-nexrad-products",
-                    "description": "NOAA NEXt-Generation RADar (NEXRAD) Products",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA NEXt-Generation RADar (NEXRAD) Products",
+                    "downloadURL": "https://catalog.data.gov/dataset/noaa-next-generation-radar-nexrad-products",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ofcm.gov/publications/fmh/allfmh2.htm",
-                    "description": "Federal Meteorological Handbooks",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbooks",
+                    "downloadURL": "https://www.ofcm.gov/publications/fmh/allfmh2.htm",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://link.galegroup.com/apps/doc/A9215749/AONE?u=naal_athens&sid=AONE&xid=c3266bae",
-                    "description": "Nexrad: next generation weather radar (WSR-88D)",
                     "@type": "dcat:Distribution",
+                    "description": "Nexrad: next generation weather radar (WSR-88D)",
+                    "downloadURL": "https://link.galegroup.com/apps/doc/A9215749/AONE?u=naal_athens&sid=AONE&xid=c3266bae",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docs.lib.purdue.edu/jto/vol1/iss2/art4",
-                    "description": "A Review of NEXRAD Level II: Data, Distribution, and Applications",
                     "@type": "dcat:Distribution",
+                    "description": "A Review of NEXRAD Level II: Data, Distribution, and Applications",
+                    "downloadURL": "https://docs.lib.purdue.edu/jto/vol1/iss2/art4",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
-                    "description": "IFloodS Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "IFloodS Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD2/KMPX/browse/",
-                    "description": "Browse images illustrate the nature and coverage of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Browse images illustrate the nature and coverage of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD2/KMPX/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD2/KMPX/browse/",
+            "identifier": "C1982568561-GHRC_DAAC",
+            "issued": "2015-03-03",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/IFLOODS/NEXRAD/DATA204",
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
             "spatial": "-99.4 40.71 -87.74 48.99",
+            "temporal": "2013-03-29T20:51:00Z/2013-06-18T15:15:59Z",
             "theme": [
                 "IFloodS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION NEXRAD LEVEL II KMPX IFLOODS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECL5M-3MT44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Ocean Three-Dimensional Momentum Tendency - Monthly Mean llc90 Grid (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECL5M-3MT44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Ocean Three-Dimensional Momentum Tendency - Monthly Mean llc90 Grid (Version 4 Release 4); 10.5067/ECL5M-3MT44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "earth science reanalyses/assimilation models",
-                "earth science services",
-                "models"
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
-            "identifier": "C1991543702-POCLOUD",
-            "description": "This dataset provides monthly-averaged ocean three-dimensional momentum tendency on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean Three-Dimensional Momentum Tendency - Monthly Mean llc90 Grid (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_MONTHLY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides monthly-averaged ocean three-dimensional momentum tendency on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-3MT44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-3MT44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_MONTHLY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_MONTHLY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECL5M-3MT44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECL5M-3MT44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543702-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543702-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543702-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543702-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_MONTHLY_V4R4.jpg",
+            "identifier": "C1991543702-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "earth science reanalyses/assimilation models",
+                "earth science services",
+                "models"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECL5M-3MT44",
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
+            "title": "ECCO Ocean Three-Dimensional Momentum Tendency - Monthly Mean llc90 Grid (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D58.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D58. Version 001. VIIRS/NPP BRDF/Albedo BSA at Solar Noon Band M5 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D58.001. https://doi.org/10.5067/VIIRS/VNP43D58.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "surface radiative properties",
-                "earth science",
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
-            "identifier": "C1607333988-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Black-Sky Albedo for Band M5 (VNP43D58) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the  VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D58 is the BSA for VIIRS band M5 (0.672 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D58",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo BSA at Solar Noon Band M5 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Black-Sky Albedo for Band M5 (VNP43D58) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the  VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D58 is the BSA for VIIRS band M5 (0.672 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D58.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D58.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D58.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D58.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D58.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D58.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607333988-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607333988-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D58.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D58.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D58",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D58",
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
+            "identifier": "C1607333988-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D58.001",
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
+            "series-name": "VNP43D58",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo BSA at Solar Noon Band M5 Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD10C2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS/Terra Snow Cover 8-Day L3 Global 0.05Deg CMG V061. Version 61. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD10C2.061.",
-            "issued": "2000-02-18",
-            "temporal": "2000-02-18T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "snow/ice",
-                "ngda",
-                "national geospatial data asset"
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
-            "identifier": "C1646609799-NSIDC_ECS",
             "description": "This global level-3 (L3) data set provides the maximum percentage of snow-covered land and persistent cloud-covered land observed over eight-days, within 0.05\u00b0 (approx. 5 km) MODIS climate modeling grid (CMG) cells. Percentages are computed from snow cover observations in the 'MODIS/Terra Snow Cover 8-Day L3 Global 500m SIN Grid' data set (DOI:10.5067/MODIS/MOD10A2.061).\n\nThe terms \"Version 61\" and \"Collection 6.1\" are used interchangeably in reference to this release of MODIS data.",
-            "title": "MODIS/Terra Snow Cover 8-Day L3 Global 0.05Deg CMG V061",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD10C2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD10C2.061",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOST/MOD10C2.061",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOST/MOD10C2.061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD10C2+V061",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD10C2+V061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/MOD10C2/versions/61/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/MOD10C2/versions/61/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10C2.061",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10C2.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10C2.061",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10C2.061",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1646609799-NSIDC_ECS",
+            "issued": "2000-02-18",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "snow/ice",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD10C2.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-18T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Snow Cover 8-Day L3 Global 0.05Deg CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/sites/default/files/atoms/files/n_pd_2200_001c_main.pdf",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-12-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/content/it-policies-and-standards/#.VkZLTKTvesE"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lori Parker",
+                "hasEmail": "mailto:lori.parker-1@nasa.gov"
+            },
+            "description": "NASA Policy Directive: NASA IT Policy on the management of NASA scientific and technical information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nasa.gov/sites/default/files/atoms/files/n_pd_2200_001c_main.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "OCIO-Fitara-101",
+            "issued": "2014-12-09",
             "keyword": [
                 "chief information officer",
                 "it policy",
@@ -1218227,64 +1218236,37 @@
                 "ocio",
                 "nodis"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lori Parker",
-                "hasEmail": "mailto:lori.parker-1@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/sites/default/files/atoms/files/n_pd_2200_001c_main.pdf",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:006"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "OCIO-Fitara-101",
-            "description": "NASA Policy Directive: NASA IT Policy on the management of NASA scientific and technical information.",
-            "title": "IT Policy NPD 2201.1C Management of NASA Scientific and Technical Information",
-            "programCode": [
-                "026:006"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nasa.gov/sites/default/files/atoms/files/n_pd_2200_001c_main.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://www.nasa.gov/content/it-policies-and-standards/#.VkZLTKTvesE"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Applied Science"
-            ]
+            ],
+            "title": "IT Policy NPD 2201.1C Management of NASA Scientific and Technical Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/pzdi-paqc",
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
-                "nen",
-                "space science",
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
-            "identifier": "NASA-0000038__32",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1218292,428 +1218274,425 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__32",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "nen",
+                "space science",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/pzdi-paqc",
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
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567654-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "surface radiative properties",
-                "topography",
-                "earth science",
-                "land surface"
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
-            "identifier": "C1220567654-USGS_LTA",
             "description": "The Aerial Photography Single Frame Records collection is a large and diverse group of imagery acquired by Federal organizations from 1937 to the present. Over 6.4 million frames of photographic images are available for download as medium and high resolution digital products. The high resolution data provide access to photogrammetric quality scans of aerial photographs with sufficient resolution to reveal landscape detail and to facilitate the interpretability of landscape features. Coverage is predominantly over the United States and includes portions of Central America and Puerto Rico. Individual photographs vary in scale, size, film type, quality, and coverage.",
-            "title": "Aerial Photo Single Frames",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n         \n         EarthExplorer offers two digital download options for the Aerial Photography Single Frame Records collection. The files are stored in Tagged Image File Format (TIFF).   Medium Resolution Digital Aerial Products were created with a digital single-lens reflex camera at a resolution of 63 microns, or 400 dots per inch (dpi). The file size for a nine inch photograph is approximately 15 megabytes (MB) for a black-and-white image and 45 MB for a color image.  High Resolution Digital Aerial Products were created with a digital scanning back at a resolution of 25 microns, or 1,000 dpi. A geometric calibration is applied to each image to correct for distortions caused by the scanning process. The high resolution scans provide access to high precision data for photogrammetric applications. The file size for a nine inch photograph is approximately 110 MB for a black-and-white image and 330 MB for a color image.  The USGS has a records schedule that transfers film sources to the National Archives and Records Administration (NARA) for permanent storage. Aerial photographs that meet the records schedule criteria become the responsibility of NARA and are retrievable for reproductions through NARA or its vendor companies. The USGS will maintain medium and high resolution data for film sources that are no longer stored at EROS.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n         \n         EarthExplorer offers two digital download options for the Aerial Photography Single Frame Records collection. The files are stored in Tagged Image File Format (TIFF).   Medium Resolution Digital Aerial Products were created with a digital single-lens reflex camera at a resolution of 63 microns, or 400 dots per inch (dpi). The file size for a nine inch photograph is approximately 15 megabytes (MB) for a black-and-white image and 45 MB for a color image.  High Resolution Digital Aerial Products were created with a digital scanning back at a resolution of 25 microns, or 1,000 dpi. A geometric calibration is applied to each image to correct for distortions caused by the scanning process. The high resolution scans provide access to high precision data for photogrammetric applications. The file size for a nine inch photograph is approximately 110 MB for a black-and-white image and 330 MB for a color image.  The USGS has a records schedule that transfers film sources to the National Archives and Records Administration (NARA) for permanent storage. Aerial photographs that meet the records schedule criteria become the responsibility of NARA and are retrievable for reproductions through NARA or its vendor companies. The USGS will maintain medium and high resolution data for film sources that are no longer stored at EROS.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1220567654-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "surface radiative properties",
+                "topography",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567654-USGS_LTA.html",
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
+            "title": "Aerial Photo Single Frames"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/HS3/SHIPS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cione, Joe , Mark  DeMaria, Jim  Gross, John  Kaplan, John  Knaff, Michelle  Mainelli, Buck  Sampson, Andrea  Schumacher, Nick  Shay and Chris A Sisko.2018. Hurricane and Severe Storm Sentinel (HS3) Statistical Hurricane Intensity Prediction Scheme (SHIPS) Intensity [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/HS3/SHIPS/DATA101",
-            "issued": "2018-08-17",
-            "temporal": "2014-03-18T00:00:00Z/2014-09-30T18:00:01Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "ocean winds",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "earth science",
-                "oceans",
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
-            "identifier": "C1979870260-GHRC_DAAC",
             "description": "The Hurricane and Severe Storm Sentinel (HS3) Statistical Hurricane Intensity Prediction Scheme (SHIPS) Intensity dataset was obtained from March 18, 2014 through September 30, 2014 during the Hurricane and Severe Storm Sentinel (HS3) field campaign. Goals for the HS3 field campaign included assessing the relative roles of large-scale environment and storm-scale internal processes, addressing the controversial role of the Saharan Air Layer (SAL) in tropical storm formation and intensification, and the role of deep convection in the inner-core region of storms. The SHIPS model provides tropical storm intensity forecasts for the Atlantic Ocean and the eastern and central North Pacific Ocean storms and invest areas.  SHIPS uses GOES infrared imagery as input to the systems.  These SHIPS data are available in ASCII format.",
-            "title": "Hurricane and Severe Storm Sentinel (HS3) Statistical Hurricane Intensity Prediction Scheme (SHIPS) Intensity V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHS3%2FSHIPS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHS3%2FSHIPS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=hs3ships",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=hs3ships",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/HS3/DATA101",
-                    "description": "HS3 Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "HS3 Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/HS3/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/SHIPS/doc/hs3ships_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/SHIPS/doc/hs3ships_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-15-00186.1",
-                    "description": "NASA\u2019s Hurricane and Severe Storm Sentinel (HS3) Investigation",
                     "@type": "dcat:Distribution",
+                    "description": "NASA\u2019s Hurricane and Severe Storm Sentinel (HS3) Investigation",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-15-00186.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0434(1994)009%3C0209:ASHIPS%3E2.0.CO;2",
-                    "description": "A Statistical Hurricane Intensity Prediction Scheme (SHIPS) for the Atlantic Basin",
                     "@type": "dcat:Distribution",
+                    "description": "A Statistical Hurricane Intensity Prediction Scheme (SHIPS) for the Atlantic Basin",
+                    "downloadURL": "https://doi.org/10.1175/1520-0434(1994)009%3C0209:ASHIPS%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0434(1999)014%3C0326:AUSHIP%3E2.0.CO;2",
-                    "description": "An Updated Statistical Hurricane Intensity Prediction Scheme (SHIPS) for the Atlantic and Eastern North Pacific Basins",
                     "@type": "dcat:Distribution",
+                    "description": "An Updated Statistical Hurricane Intensity Prediction Scheme (SHIPS) for the Atlantic and Eastern North Pacific Basins",
+                    "downloadURL": "https://doi.org/10.1175/1520-0434(1999)014%3C0326:AUSHIP%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/WAF862.1",
-                    "description": "Further Improvements to the Statistical Hurricane Intensity Prediction Scheme (SHIPS)",
                     "@type": "dcat:Distribution",
+                    "description": "Further Improvements to the Statistical Hurricane Intensity Prediction Scheme (SHIPS)",
+                    "downloadURL": "https://doi.org/10.1175/WAF862.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/projects/HS3",
-                    "description": "HS3 Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "HS3 Project Home Page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/projects/HS3",
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
+            "identifier": "C1979870260-GHRC_DAAC",
+            "issued": "2018-08-17",
+            "keyword": [
+                "ocean winds",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "earth science",
+                "oceans",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/HS3/SHIPS/DATA101",
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
             "spatial": "-179.11 7.19 -14.99 44.51",
+            "temporal": "2014-03-18T00:00:00Z/2014-09-30T18:00:01Z",
             "theme": [
                 "HS3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hurricane and Severe Storm Sentinel (HS3) Statistical Hurricane Intensity Prediction Scheme (SHIPS) Intensity V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0043",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2003-10-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0043.",
-            "issued": "2003-11-17",
-            "temporal": "2000-08-12T00:00:00Z/2002-11-05T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols"
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
-            "identifier": "C1000000087-LARC_ASDC",
             "description": "The NARSTO_EPA_SS_HOUSTON_NO3_SO4_C_DATA files contain continuous measurements of PM2.5 nitrate, PM2.5 sulfate, and PM2.5 carbon collected during August 12, 2000 through November 5, 2001 at the Aldine, Deer Park, and LaPorte Houston Supersite monitoring locations. Nitrate measurements were collected using the R&P 8400N Method. Sulfate and carbon measurements were collected using the Prototype ADI Particulate Sulfate and Carbon Monitor Method.The Houston Supersite is one of several Supersites that was established in urban areas within the United States by the U.S. Environmental Protection Agency (EPA) to better understand the measurement, sources, and health effects of suspended particulate matter (PM). The overall goals were to characterize the composition and identify the sources of particulate matter in Southeastern Texas, to develop and test new methods for characterizing fine particulate matter, and to collect data on the physical and chemical characterization of fine particulate matter that can be used to support exposure and health effects studies.NARSTO (formerly North American Research Strategy for Tropospheric Ozone) is a public/private partnership, whose membership spans government, the utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission is to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are available.",
-            "title": "NARSTO EPA_SS_HOUSTON PM2.5 Nitrate, Sulfate, and Carbon Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0043",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0043",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000087-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_HOUSTON_NO3_SO4_C_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_HOUSTON_NO3_SO4_C_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000087-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0043",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_HOUSTON_NO3_SO4_C_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_HOUSTON_NO3_SO4_C_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0043",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_houston_no3_so4_c_v1.pdf",
-                    "description": "Guide for NARSTO EPA_SS_HOUSTON PM2.5 Nitrate, Sulfate, and Carbon Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_HOUSTON PM2.5 Nitrate, Sulfate, and Carbon Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_houston_no3_so4_c_v1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Houston_Final_Report.pdf",
-                    "description": "Gulf Coast Aerosol Research and Characterization Program (Houston Supersite) FINAL REPORT - April 2005",
                     "@type": "dcat:Distribution",
+                    "description": "Gulf Coast Aerosol Research and Characterization Program (Houston Supersite) FINAL REPORT - April 2005",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Houston_Final_Report.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_HOUSTON_NO3_SO4_C_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_HOUSTON_NO3_SO4_C_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_HOUSTON_NO3_SO4_C_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_HOUSTON_NO3_SO4_C_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000087-LARC_ASDC",
+            "issued": "2003-11-17",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0043",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>29.66 -95.32 29.66 -95.06 29.9 -95.06 29.9 -95.32 29.66 -95.32</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-08-12T00:00:00Z/2002-11-05T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA_SS_HOUSTON PM2.5 Nitrate, Sulfate, and Carbon Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M03-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m03-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M03-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m03-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP003 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP003 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-EPA-3-RDR-GRIGG-SKJELL-V1.0",
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
-                "26p/grigg-skjellerup 1 (1922 k1)",
-                "giotto extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains count rates from the Energetic Particle Analyser (EPA) experiment aboard the Giotto spacecraft during its flyby of comet P/Grigg-Skjellerup during July of 1992. These data were not formally reviewed by the PDS.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-epa-3-rdr-grigg-skjell-v1.0_pzh4-dyur",
+            "issued": "2021-05-21",
+            "keyword": [
+                "26p/grigg-skjellerup 1 (1922 k1)",
+                "giotto extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-EPA-3-RDR-GRIGG-SKJELL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-epa-3-rdr-grigg-skjell-v1.0_pzh4-dyur",
-            "description": "This dataset contains count rates from the Energetic Particle Analyser (EPA) experiment aboard the Giotto spacecraft during its flyby of comet P/Grigg-Skjellerup during July of 1992. These data were not formally reviewed by the PDS.",
-            "title": "GIOTTO EXTENDED MISSION ELECTRON PARTICLE ANALYSER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GIOTTO EXTENDED MISSION ELECTRON PARTICLE ANALYSER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://appel.nasa.gov/knowledge-sharing/annual-publications/",
+            "accrualPeriodicity": "R/P2Y",
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
-                "annual report",
-                "appel",
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
-            "identifier": "NASA-861__1",
             "description": "Academy of Program/Project & Engineering Leadership's Annual Report highlights the Academy's efforts to serve the NASA workforce's needs in adapting to the challenges of today and the future.",
-            "title": "Academy of Program/Project & Engineering Leadership Annual Publications",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1218721,91 +1218700,124 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P2Y",
+            "identifier": "NASA-861__1",
+            "issued": "2018-06-25",
+            "keyword": [
+                "knowledge",
+                "annual report",
+                "appel",
+                "sharing"
+            ],
+            "landingPage": "http://appel.nasa.gov/knowledge-sharing/annual-publications/",
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
+            "title": "Academy of Program/Project & Engineering Leadership Annual Publications"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5ZW1HV4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Arctic Landfast Sea Ice 1953-1998, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5ZW1HV4.",
-            "issued": "1953-01-01",
-            "temporal": "1953-01-01T00:00:00Z/1998-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-12-31",
-            "keyword": [
-                "earth science",
-                "sea ice",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Christof Beatty",
                 "hasEmail": "mailto:Christof.KonigBeatty@uclouvain.be"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206527-NSIDCV0",
             "description": "The files in this data set contain landfast sea ice data (monthly means) gathered from both Russian Arctic and Antarctic Research Institute (AARI) and Canadian Ice Service (CIS) sources. Details on processing and treatment are given in the contributor's PhD thesis (Konig 2007).   The data are provided in netCDF format. \n\nThe time span over which data are available is split into 3 ranges: for 1953-1967 there are only AARI data, for 1968-1990 both AARI and CIS data are available, and from 1991-1998 only CIS data are available. There are a total of six files: two for the 1953-1967 data, two for the 1968-1990 data, and two for the 1991-1998 data. There are two files for each range because the files with \"_noNaN\" in their names contain \"-1000\" as the missing value, and the other files use \"nan\" as the missing value. Otherwise the data in those files are identical. \n\nAARI data were obtained from NSIDC retired data set AARI 10-Day Arctic Ocean EASE-Grid Sea Ice Observations that was later replaced by Sea Ice Charts of the Russian Arctic in Gridded Format, 1933-2006 (AARI, 2007).\n\nArctic and Antarctic Research Institute. 2007. Sea ice charts of the Russian Arctic in gridded format, 1933-2006. Edited and compiled by V. Smolyanitsky, V. Borodachev, A. Mahoney, F. Fetterer, and R. Barry. Boulder, Colorado USA: National Snow and Ice Data Center. https://nsidc.org/data/g02176.\n\nNotice to Data Users: The documentation for this data set was provided solely by the contributor and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.",
-            "title": "Arctic Landfast Sea Ice 1953-1998, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5ZW1HV4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5ZW1HV4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02195_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02195_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5ZW1HV4",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5ZW1HV4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5ZW1HV4",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5ZW1HV4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206527-NSIDCV0",
+            "issued": "1953-01-01",
+            "keyword": [
+                "earth science",
+                "sea ice",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5ZW1HV4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1998-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 55.0 180.0 90.0",
+            "temporal": "1953-01-01T00:00:00Z/1998-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic Landfast Sea Ice 1953-1998, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1210197768-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "ERS-1 Standard Beam Level 0 Frame",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1210197768-ASF",
             "issued": "2010-10-05",
-            "temporal": "1991-08-08T03:18:11Z/1997-09-29T15:20:44Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-12-03",
             "keyword": [
                 "geomorphic landforms/processes",
                 "land surface",
@@ -1218828,390 +1218840,387 @@
                 "glaciers/ice sheets",
                 "landscape"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1210197768-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-12-03",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1210197768-ASF",
-            "description": "ERS-1 Standard Beam Level 0 Frame",
-            "title": "ERS-1_LEVEL0",
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
+            "temporal": "1991-08-08T03:18:11Z/1997-09-29T15:20:44Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ERS-1_LEVEL0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E%2FL%2FCAL-PPR-3-RDR-EARTH2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "B. Harris, 2006-07-14, added ARCHIVE_STATUS, ,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Venus encounter observations in February 1990.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-l-cal-ppr-3-rdr-earth2-v1.0_pzki-ze5h",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "moon",
                 "earth",
                 "galileo"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E%2FL%2FCAL-PPR-3-RDR-EARTH2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-l-cal-ppr-3-rdr-earth2-v1.0_pzki-ze5h",
-            "description": "B. Harris, 2006-07-14, added ARCHIVE_STATUS, ,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Venus encounter observations in February 1990.",
-            "title": "GLL PPR EARTH-2 ENCOUNTER RDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GLL PPR EARTH-2 ENCOUNTER RDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1333-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-11T17:05:00.000 to 2016-01-12T00:50:21.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1333-v1.0_pzkp-udgb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1333-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1333-v1.0_pzkp-udgb",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-11T17:05:00.000 to 2016-01-12T00:50:21.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1333 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1333 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1145",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Helmer, E.H., M.A. Lefsky, and D.A. Roberts. 2013. LBA-ECO CD-37 Secondary Forest Biomass and Age Class, Rondonia, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1145",
-            "issued": "2023-10-03",
-            "temporal": "1975-06-19T00:00:00Z/2003-05-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
-            "keyword": [
-                "earth science",
-                "vegetation",
-                "ecosystems",
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
-            "identifier": "C2781386619-ORNL_CLOUD",
             "description": "This data set provides tree age, forest formation, and  land cover classification maps, and estimates of landscape-level above-ground live woody biomass (AGLB) for secondary forests in Rondonia, Brazil. The Threshold Age Mapping Algorithm (TAMA) was applied to a densely spaced time series of Landsat images (1975 to 2003) to derive forest type and age classification maps. The AGLB of the secondary forest was estimated by combining the forest classification map with coincident biomass estimates from the Geoscience Laser Altimeter System (GLAS). There are five raster images and three comma-delimited data files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-37 Secondary Forest Biomass and Age Class, Rondonia, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1145",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1145",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD37_Biomass_Landsat_Glas/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD37_Biomass_Landsat_Glas/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD37_Biomass_Landsat_GLAS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD37_Biomass_Landsat_GLAS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1145",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1145",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD37_Biomass_Landsat_Glas/comp/CD37_Biomass_Landsat_GLAS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD37_Biomass_Landsat_Glas/comp/CD37_Biomass_Landsat_GLAS.pdf",
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
+            "identifier": "C2781386619-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "ecosystems",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1145",
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
             "spatial": "-64.39 -10.78 -62.89 -9.34",
+            "temporal": "1975-06-19T00:00:00Z/2003-05-20T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-37 Secondary Forest Biomass and Age Class, Rondonia, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-CRS-4-SUMM-D2-96SEC-V1.0",
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
+            "description": "Counting rate from the D2 detector in the Cosmic Ray System (CRS) electron telescope (TET) on Voyager 2 during the Neptune encounter. The D2 detector nominally responds to electrons with kinetic energies above approximately 2.5 MeV (see detector description for details).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-crs-4-summ-d2-96sec-v1.0_pzqh-z7h4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "neptune"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-CRS-4-SUMM-D2-96SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-crs-4-summ-d2-96sec-v1.0_pzqh-z7h4",
-            "description": "Counting rate from the D2 detector in the Cosmic Ray System (CRS) electron telescope (TET) on Voyager 2 during the Neptune encounter. The D2 detector nominally responds to electrons with kinetic energies above approximately 2.5 MeV (see detector description for details).",
-            "title": "VG2 NEP CRS RESAMPLED SUMMARY D2 RATE ELEC 96SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 NEP CRS RESAMPLED SUMMARY D2 RATE ELEC 96SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-PUMA-3-RDR-HALLEY-PROCESSED-V1.0",
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
+            "description": "The data from MPI for this dataset were received as text files each containing spectra of a single instrument mode (there were several files for most modes). These spectra were reformatted into binary tables, and all spectra from each mode were combined into a single file. The original order of the spectra has been preserved. Spacecraft time, relative to switch-on of the instrument is specified as 1 clock tick = 0.11852 seconds. The exact equation is:",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-puma-3-rdr-halley-processed-v1.0_pzqn-392y",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "vega 1"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-PUMA-3-RDR-HALLEY-PROCESSED-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-puma-3-rdr-halley-processed-v1.0_pzqn-392y",
-            "description": "The data from MPI for this dataset were received as text files each containing spectra of a single instrument mode (there were several files for most modes). These spectra were reformatted into binary tables, and all spectra from each mode were combined into a single file. The original order of the spectra has been preserved. Spacecraft time, relative to switch-on of the instrument is specified as 1 clock tick = 0.11852 seconds. The exact equation is:",
-            "title": "VEGA1 DUST MASS SPECTROMETER MODAL DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VEGA1 DUST MASS SPECTROMETER MODAL DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/2J1BEWBUKC3M",
             "citation": "NOAA NESDIS. 2022-08-22. VISSRSMS1IMIR. Version 001. VISSR/SMS-1 Infrared Imagery on 70mm Film V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/2J1BEWBUKC3M. https://disc.gsfc.nasa.gov/datacollection/VISSRSMS1IMIR_001.html. Digital Science Data.",
-            "issued": "2018-03-13",
-            "temporal": "1974-07-28T00:00:00Z/1979-04-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-13",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
-            "data-presentation-form": "Digital Science Data",
-            "identifier": "C2386924897-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "description": "VISSRSMS1IMIR is the Visible Infrared Spin-Scan Radiometer (VISSR) Infrared Imagery on 70mm Film data product from the first Synchronous Meteorological Satellite (SMS-1). This set of IR imagery (10.5 to 12.5 micrometer) was originally produced on commercial image-generation equipment from digital tapes and was made available on 70-mm film, from which they were later scanned to digital TIFF image files. Each TIFF scan contains 2 or 3 pictures, and there are several hundred scans from an original 70 mm film roll which are combined into a ZIP file. Each picture contains a title on the top boundary and a 33-level gray scale on the right boundary that represents brightness temperatures. It may have a combination of the following options: 1) contrast enhancement, 2) image sectorization, and 3) 1/16-size imagery. The maximum effective size covers 500 sq km, represented by 4000 by 3904 pixels. Each element has a maximum resolution of 3.7 km. The title contains the satellite identification, picture number, picture type, coordinate numbers of the top left pixel relative to the visible sensor, start time of sectorized image, and pixel scaling and sector size identification.\n\nThe SMS-1 satellite was initially parked over the equator at longitude 45W on June 7, 1974 viewing the hemisphere below the satellite to support the GARP Atlantic Tropical Experiment (GATE). It was moved to its operational position at 75W on Nov 15, 1974 where it remained until GOES-1 was launched, after which SMS-1 was moved to 105W and placed in stand-by-mode as a backup to GOES-1 or SMS-2. The VISSR experiment was operated by the NOAA National Environmental Satellite Data and Information Service (NESDIS), as well as scientists from NASA Goddard Space Flight Center.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00068 (old ID 74-033A-01C).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "VISSRSMS1IMIR",
             "creator": "NOAA NESDIS",
-            "title": "VISSR/SMS-1 Infrared Imagery on 70mm Film V001 (VISSRSMS1IMIR) at GES DISC",
-            "graphic-preview-description": "Typical SMS-1 VISSR visible 70mm film image.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS1IMIR_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "VISSRSMS1IMIR is the Visible Infrared Spin-Scan Radiometer (VISSR) Infrared Imagery on 70mm Film data product from the first Synchronous Meteorological Satellite (SMS-1). This set of IR imagery (10.5 to 12.5 micrometer) was originally produced on commercial image-generation equipment from digital tapes and was made available on 70-mm film, from which they were later scanned to digital TIFF image files. Each TIFF scan contains 2 or 3 pictures, and there are several hundred scans from an original 70 mm film roll which are combined into a ZIP file. Each picture contains a title on the top boundary and a 33-level gray scale on the right boundary that represents brightness temperatures. It may have a combination of the following options: 1) contrast enhancement, 2) image sectorization, and 3) 1/16-size imagery. The maximum effective size covers 500 sq km, represented by 4000 by 3904 pixels. Each element has a maximum resolution of 3.7 km. The title contains the satellite identification, picture number, picture type, coordinate numbers of the top left pixel relative to the visible sensor, start time of sectorized image, and pixel scaling and sector size identification.\n\nThe SMS-1 satellite was initially parked over the equator at longitude 45W on June 7, 1974 viewing the hemisphere below the satellite to support the GARP Atlantic Tropical Experiment (GATE). It was moved to its operational position at 75W on Nov 15, 1974 where it remained until GOES-1 was launched, after which SMS-1 was moved to 105W and placed in stand-by-mode as a backup to GOES-1 or SMS-2. The VISSR experiment was operated by the NOAA National Environmental Satellite Data and Information Service (NESDIS), as well as scientists from NASA Goddard Space Flight Center.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00068 (old ID 74-033A-01C).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2J1BEWBUKC3M",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2J1BEWBUKC3M",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS1IMIR_001.png",
-                    "description": "Typical SMS-1 VISSR visible 70mm film image.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical SMS-1 VISSR visible 70mm film image.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS1IMIR_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRSMS1IMIR_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRSMS1IMIR_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS1IMIR.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS1IMIR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRSMS1IMIR",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRSMS1IMIR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS1IMIR.001/doc/README.VISSRSMSGOESIM.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS1IMIR.001/doc/README.VISSRSMSGOESIM.001.pdf",
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
+            "graphic-preview-description": "Typical SMS-1 VISSR visible 70mm film image.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS1IMIR_001.png",
+            "identifier": "C2386924897-GES_DISC",
+            "issued": "2018-03-13",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/2J1BEWBUKC3M",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "VISSRSMS1IMIR",
             "spatial": "165.0 -90.0 45.0 90.0",
+            "temporal": "1974-07-28T00:00:00Z/1979-04-19T23:59:59.999Z",
             "theme": [
                 "GOES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VISSR/SMS-1 Infrared Imagery on 70mm Film V001 (VISSRSMS1IMIR) at GES DISC"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20091208.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-593",
+            "issued": "2018-06-25",
             "keyword": [
                 "rss",
                 "spice",
@@ -1219223,45 +1219232,38 @@
                 "sharad",
                 "hirise"
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
-            "identifier": "NASA-593",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 11",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20091208.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67PCHURYUMOV-M18-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67pchuryumov-m18-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega",
@@ -1219269,630 +1219271,609 @@
                 "zeta cas",
                 "pluto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67PCHURYUMOV-M18-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67pchuryumov-m18-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP018 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP018 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-LECP-3-STEP-6.4MIN-V1.0",
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
+            "description": "Voyager 2 Energetic Particle (LECP) data from the Saturn far encounter\nperiod between 1981-08-23T06:34:23 and 1981-08-29T06:30:54.  The data\nset provides 6.4 minute counting rate and flux measurements during the\ninstrument stepping operation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-lecp-3-step-6.4min-v1.0_pzsn-zj3k",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-LECP-3-STEP-6.4MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-lecp-3-step-6.4min-v1.0_pzsn-zj3k",
-            "description": "Voyager 2 Energetic Particle (LECP) data from the Saturn far encounter\nperiod between 1981-08-23T06:34:23 and 1981-08-29T06:30:54.  The data\nset provides 6.4 minute counting rate and flux measurements during the\ninstrument stepping operation.",
-            "title": "VG2 LECP 6.4 MINUTE SATURN\n                                      FAR ENCOUNTER STEP DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 LECP 6.4 MINUTE SATURN\n                                      FAR ENCOUNTER STEP DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9%2FVO1%2FVO2-M-RSS-5-GRAVITY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This archive contains maps of the Bouguer anomalies, free-gravity accelerations, and geoid anomalies of Mars, along with spherical harmonic gravity and topography models and occultation data acquired with Mariner 9 and the Viking Orbiter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-vo1-vo2-m-rss-5-gravity-v1.0_pzv6-5pt6",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "mariner71",
                 "viking"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9%2FVO1%2FVO2-M-RSS-5-GRAVITY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-vo1-vo2-m-rss-5-gravity-v1.0_pzv6-5pt6",
-            "description": "This archive contains maps of the Bouguer anomalies, free-gravity accelerations, and geoid anomalies of Mars, along with spherical harmonic gravity and topography models and occultation data acquired with Mariner 9 and the Viking Orbiter.",
-            "title": "unk",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "unk"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-MCDIDS-3-RDR-MCDNLD-V1.0",
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
-                "comet"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The McDonald Observatory Faint Comet Survey data set presents spectral data from 152 observations of 17 comets taken using the Intensified Dissector Scanner spectrograph.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-mcdids-3-rdr-mcdnld-v1.0_pzwf-v5mt",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "comet"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-MCDIDS-3-RDR-MCDNLD-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-mcdids-3-rdr-mcdnld-v1.0_pzwf-v5mt",
-            "description": "The McDonald Observatory Faint Comet Survey data set presents spectral data from 152 observations of 17 comets taken using the Intensified Dissector Scanner spectrograph.",
-            "title": "MCDONALD OBSERVATORY FAINT COMET SPECTRO-PHOTOMETRIC SURVEY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MCDONALD OBSERVATORY FAINT COMET SPECTRO-PHOTOMETRIC SURVEY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4GH9FVG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2002-12-31. Last of the Wild Project, Version 1, 2002 (LWP-1): Top One Percent Wild Areas Dataset (IGHP). Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4GH9FVG. https://doi.org/10.7927/H4QV3JG4.",
-            "issued": "2002-12-31",
-            "temporal": "1992-01-01T00:00:00Z/1995-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4CN71V6",
-                "https://doi.org/10.7927/H4VM496V",
-                "https://doi.org/10.7927/H47W694W",
-                "https://doi.org/10.7927/H4445JDG",
-                "https://doi.org/10.7927/H40C4SPR"
-            ],
-            "keyword": [
-                "biosphere",
-                "land use/land cover",
-                "land surface",
-                "earth science",
-                "ecosystems"
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
-            "identifier": "C179001939-SEDAC",
-            "description": "The Top One Percent Wild Areas Dataset of the Last of the Wild Project, Version 1, 2002 (LWP-1) is derived from the LWP-1 Human Footprint Dataset. The gridded data are classified according to their raster value (wild = 0-1; not wild >1). The top 1% of the wild areas within each biome by realm are selected and identified. The dataset  in Interrupted Goode Homolosine Projection (IGHP) is produced by the Wildlife Conservation Society (WCS) and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Last of the Wild Project, Version 1, 2002 (LWP-1): Top One Percent Wild Areas Dataset (IGHP)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-top-one-percent-wild-areas-ighp/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Top One Percent Wild Areas Dataset of the Last of the Wild Project, Version 1, 2002 (LWP-1) is derived from the LWP-1 Human Footprint Dataset. The gridded data are classified according to their raster value (wild = 0-1; not wild >1). The top 1% of the wild areas within each biome by realm are selected and identified. The dataset  in Interrupted Goode Homolosine Projection (IGHP) is produced by the Wildlife Conservation Society (WCS) and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4GH9FVG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4GH9FVG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-top-one-percent-wild-areas-ighp/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-top-one-percent-wild-areas-ighp/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v1-top-one-percent-wild-areas-ighp/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v1-top-one-percent-wild-areas-ighp/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v1-top-one-percent-wild-areas-ighp",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v1-top-one-percent-wild-areas-ighp",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-top-one-percent-wild-areas-ighp/sedac-logo.jpg",
+            "identifier": "C179001939-SEDAC",
+            "issued": "2002-12-31",
+            "keyword": [
+                "biosphere",
+                "land use/land cover",
+                "land surface",
+                "earth science",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4GH9FVG",
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
+                "https://doi.org/10.7927/H4CN71V6",
+                "https://doi.org/10.7927/H4VM496V",
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
+            "title": "Last of the Wild Project, Version 1, 2002 (LWP-1): Top One Percent Wild Areas Dataset (IGHP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D81.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D81. Version 001. VIIRS/NPP BRDF/Albedo NBAR at Solar Noon Band M2 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D81.001. https://doi.org/10.5067/VIIRS/VNP43D81.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
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
-            "identifier": "C1607356177-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Nadir BRDF-Adjusted Reflectance (NBAR) for Band M2 (VNP43D81) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D80 through VNP43D89 are the NBAR products of the VNP43D BRDF/Albedo product suite. NBAR values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) included in the VNP43MA4 (https://doi.org/10.5067/VIIRS/VNP43MA4.001) product. In addition to the bands included in VNP43MA4, this product suite includes NBAR values for the VIIRS Day/Night Band (DNB). The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon. Details regarding methodology are available on the VNP43MA4 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D81 is the NBAR for VIIRS band M2 (0.445 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D81",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo NBAR at Solar Noon Band M2 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Nadir BRDF-Adjusted Reflectance (NBAR) for Band M2 (VNP43D81) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D80 through VNP43D89 are the NBAR products of the VNP43D BRDF/Albedo product suite. NBAR values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) included in the VNP43MA4 (https://doi.org/10.5067/VIIRS/VNP43MA4.001) product. In addition to the bands included in VNP43MA4, this product suite includes NBAR values for the VIIRS Day/Night Band (DNB). The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon. Details regarding methodology are available on the VNP43MA4 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D81 is the NBAR for VIIRS band M2 (0.445 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D81.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D81.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D81.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D81.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D81.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D81.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607356177-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607356177-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D81.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D81.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D81",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D81",
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
+            "identifier": "C1607356177-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D81.001",
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
+            "series-name": "VNP43D81",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo NBAR at Solar Noon Band M2 Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566868-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "1973-01-15",
-            "temporal": "1973-01-15T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-27",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
-                "spectral/engineering",
-                "ngda",
-                "national geospatial data asset",
-                "land use/land cover",
-                "earth science",
-                "surface thermal properties",
-                "sensor characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GREG STENSAAS",
                 "hasEmail": "mailto:stensaas@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220566868-USGS_LTA",
             "description": "On the background of these requirements for sensor calibration, intercalibration and product validation, the subgroup on Calibration and Validation of the Committee on Earth Observing System (CEOS) formulated the following recommendation during the plenary session held in China at the end of 2004, with the goal of setting-up and operating an internet based system to provide sensor data, protocols and guidelines for these purposes:\n\nBackground:\n\nReference Datasets are required to support the understanding of climate change and quality assure operational services by Earth Observing satellites. The data from different sensors and the resulting synergistic data products require a high level of accuracy that can only be obtained through continuous traceable calibration and validation activities.\nRequirement:\n\nInitiate an activity to document a reference methodology to predict Top of Atmosphere (TOA) radiance for which currently flying and planned wide swath sensors can be intercompared, i.e. define a standard for traceability. Also create and maintain a fully accessible web page containing, on an instrument basis, links to all instrument characteristics needed for intercomparisons as specified above, ideally in a common format. In addition, create and maintain a database (e.g. SADE) of instrument data for specific vicarious calibration sites, including site characteristics, in a common format. Each agency is responsible for providing data for their instruments in this common format. Recommendation : The required activities described above should be supported for an implementation period of two years and a maintenance period over two subsequent years. The CEOS should encourage a member agency to accept the lead role in supporting this activity. CEOS should request all member agencies to support this activity by providing appropriate information and data in a timely manner.\n\nPseudo-Invariant Calibration Sites (PICS):\nLibya 4 is one of six CEOS reference Pseudo-Invariant Calibration Sites (PICS) that are CEOS Reference Test Sites. Besides the nominally good site characteristics (temporal stability, uniformity, homogeneity, etc.), these six PICS were selected by also taking into account their heritage and the large number of datasets from multiple instruments that already existed in the EO archives and the long history of characterization performed over these sites. The PICS have high reflectance and are usually made up of sand dunes with climatologically low aerosol loading and practically no vegetation. Consequently, these PICS can be used to evaluate the long-term stability of instrument and facilitate inter-comparison of multiple instruments.",
-            "title": "CEOS Cal Val Test Site - Libya 1 - Pseudo-Invariant Calibration Site (PICS)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://calvalportal.ceos.org/web/guest/home",
-                    "description": "Committee on Earth Observation Satellites (CEOS) Working Group on Calibration and Validation (WGCV) Test Sites.",
                     "@type": "dcat:Distribution",
+                    "description": "Committee on Earth Observation Satellites (CEOS) Working Group on Calibration and Validation (WGCV) Test Sites.",
+                    "downloadURL": "http://calvalportal.ceos.org/web/guest/home",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/opensearchdescription+xml",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/opensearch/granules/descriptor_document.xml?collectionConceptId=C1220566868-USGS_LTA",
-                    "description": "Collection-specific granule Open Search Descriptor Document",
                     "@type": "dcat:Distribution",
+                    "description": "Collection-specific granule Open Search Descriptor Document",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/opensearch/granules/descriptor_document.xml?collectionConceptId=C1220566868-USGS_LTA",
+                    "mediaType": "application/opensearchdescription+xml",
                     "title": "Retrieve the OpenSearch Get Capabilities document"
                 }
             ],
+            "identifier": "C1220566868-USGS_LTA",
+            "issued": "1973-01-15",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "spectral/engineering",
+                "ngda",
+                "national geospatial data asset",
+                "land use/land cover",
+                "earth science",
+                "surface thermal properties",
+                "sensor characteristics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566868-USGS_LTA.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOI/USGS/EROS"
+            },
             "spatial": "12.19 23.44 14.83 25.76",
+            "temporal": "1973-01-15T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CEOS Cal Val Test Site - Libya 1 - Pseudo-Invariant Calibration Site (PICS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P12-V-ORAD-5-RADAR-IMAGE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of five VICAR2 format images of Venus derived from Pioneer Venus radar altimeter measurements. Data are presented in simple cylindrical projection format. The radius image contains 1440 lines (latitude) and 2880 samples (longitude), and the others contain 1024 lines and 2048 samples.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p12-v-orad-5-radar-image-v1.0_pzzg-rr4g",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "pioneer",
                 "venus",
                 "pre-magellan"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P12-V-ORAD-5-RADAR-IMAGE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p12-v-orad-5-radar-image-v1.0_pzzg-rr4g",
-            "description": "This data set consists of five VICAR2 format images of Venus derived from Pioneer Venus radar altimeter measurements. Data are presented in simple cylindrical projection format. The radius image contains 1440 lines (latitude) and 2880 samples (longitude), and the others contain 1024 lines and 2048 samples.",
-            "title": "PIONEER 12 VENUS ORBITING RADAR DERIVED RADAR IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PIONEER 12 VENUS ORBITING RADAR DERIVED RADAR IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-FGM-4-SUMM-5MIN-V1.0",
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
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 11 Fluxgate Magnetometer (FGM) data from the Jupiter encounter\nperiod between 1974-12-02T23:31:40.000 and 1974-12-03T11:12:16.000.\nThe data set provides 5 minute magnetic field averages in both Inertial\nHeliocentric and System III (1957.0) coordinates, and spacecraft\ntrajectory data in System I and System III (1957.0) coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-fgm-4-summ-5min-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pioneer 11",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-FGM-4-SUMM-5MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-fgm-4-summ-5min-v1.0",
-            "description": "Pioneer 11 Fluxgate Magnetometer (FGM) data from the Jupiter encounter\nperiod between 1974-12-02T23:31:40.000 and 1974-12-03T11:12:16.000.\nThe data set provides 5 minute magnetic field averages in both Inertial\nHeliocentric and System III (1957.0) coordinates, and spacecraft\ntrajectory data in System I and System III (1957.0) coordinates.",
-            "title": "P11 FLUXGATE MAGMETOMETER 5 MINUTE\n                                      JUPITER SUMMARY DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P11 FLUXGATE MAGMETOMETER 5 MINUTE\n                                      JUPITER SUMMARY DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/622",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Raich, J.W., and W.H. Schlesinger. 2001. Global Annual Soil Respiration Data (Raich and Schlesinger 1992). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/622",
-            "issued": "2022-02-12",
-            "temporal": "1963-01-01T00:00:00Z/1992-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "atmospheric chemistry",
-                "atmospheric temperature",
-                "atmosphere",
-                "soils",
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
-            "identifier": "C2216863171-ORNL_CLOUD",
             "description": "This data set is a compilation of soil respiration rates (g C m-2 yr-1) from terrestrial and wetland ecosystems reported in the literature prior to 1992. These rates were measured in a variety of ecosystems to examine rates of microbial activity, nutrient turnover, carbon cycling, root dynamics, and a variety of other soil processes. Also included in the data set are biome type, vegetation type, locality, and geographic coordinates.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Global Annual Soil Respiration Data (Raich and Schlesinger 1992)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/soil_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F622",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F622",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_soil/Respiration/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_soil/Respiration/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Respiration.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Respiration.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/622",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/622",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Respiration/comp/Global_Soil_Respiration_Comp_Doc.PDF",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Respiration/comp/Global_Soil_Respiration_Comp_Doc.PDF",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Respiration/comp/Global_Soil_Respiration_Comp_Doc.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Respiration/comp/Global_Soil_Respiration_Comp_Doc.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Respiration/comp/RAICH_abstract.htm",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Respiration/comp/RAICH_abstract.htm",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Respiration/comp/Respiration.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Respiration/comp/Respiration.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/soil_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/soil_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/soil_logo_square.png",
+            "identifier": "C2216863171-ORNL_CLOUD",
+            "issued": "2022-02-12",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmospheric chemistry",
+                "atmospheric temperature",
+                "atmosphere",
+                "soils",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/622",
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
             "spatial": "-156.4 -37.5 146.5 71.18",
+            "temporal": "1963-01-01T00:00:00Z/1992-01-01T23:59:59Z",
             "theme": [
                 "Soil",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Annual Soil Respiration Data (Raich and Schlesinger 1992)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/e-standards-mass-properties-engineering/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-07-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "code ti",
-                "mass properties engineering",
-                "java",
-                "api",
-                "application programming interface"
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
-            "identifier": "OCIO-Fitara-117",
             "description": "The purpose of this Opensource forum is to promote the development of a JAVA based Application Programming Interface for the field of Mass Properties Engineering.",
-            "title": "ARC Code TI: E-Standards for Mass Properties Engineering",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1219900,60 +1219881,81 @@
                     "mediaType": "application/x-zip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-117",
+            "issued": "2015-07-21",
+            "keyword": [
+                "code ti",
+                "mass properties engineering",
+                "java",
+                "api",
+                "application programming interface"
+            ],
+            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/e-standards-mass-properties-engineering/",
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
+            "title": "ARC Code TI: E-Standards for Mass Properties Engineering"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1325-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-09T09:41:50.000 to 2016-01-09T14:34:21.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1325-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1325-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1325-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-09T09:41:50.000 to 2016-01-09T14:34:21.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1325 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1325 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-MIR2-2-RAW-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Raw, uncalibrated image data from the Mid Infrared Camera 2 (MIR2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-mir2-2-raw-v1.0_q2fk-2u3h",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "lunar crater observation and sensing satellite",
@@ -1219961,213 +1219963,190 @@
                 "test image",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-MIR2-2-RAW-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-mir2-2-raw-v1.0_q2fk-2u3h",
-            "description": "Raw, uncalibrated image data from the Mid Infrared Camera 2 (MIR2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS EARTH/MOON 2ND MID IR CAMERA 2 RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LCROSS EARTH/MOON 2ND MID IR CAMERA 2 RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/487/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-11-03",
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
-            "identifier": "DASHLINK_487",
             "description": "This documents the modal results for the final HIRENASD Finite element models TET model with instrumentation, modelcart, balance and OML modified. \r\n\r\nPost your comments below\r\n\r\nFrequency comparisons\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/image001_2.png\">\r\n<BR>\t\t\t\t\r\n\r\nMode shapes showing only the wing for the last column of mode shapes\r\n\r\n<TABLE>\r\n<TR><TD>\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_1.jpg\" width=200> <br>Mode 1\r\n</TD><TD>\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_2.jpg\" width=200> \r\n<br>Mode 2</TD><TD>\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_3.jpg\" width=200> \r\n<br>Mode 3</TD></TR>\r\n<TR><TD>\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_4.jpg\" width=200> \r\n<br>Mode 4</TD><TD>\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_5.jpg\" width=200> \r\n<br>Mode 5\r\n</TD><TD><img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_6.jpg\" width=200> \r\n<br>Mode 6\r\n</TD>\r\n</TR>\r\n<TR><TD>\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_7.jpg\" width=200> \r\n<br>Mode 7\r\n</TD><TD><img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_8.jpg\" width=200> \r\n<br>Mode 8\r\n</TD><TD><img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_9.jpg\" width=200> \r\n<br>Mode 9\r\n</TD></TR>\r\n<TR><TD>\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_10.jpg\" width=200> \r\n<br>Mode 10\r\n</TD><TD>\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_11.jpg\" width=200> \r\n<br>Mode 11\r\n</TD><TD>\r\n<img src=\"https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_12.jpg\" width=200> \r\n<br>Mode 12\r\n</TD></TR>\r\n</TABLE>",
-            "title": "HIRENASD Modeshapes Nov 2011 model",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_1.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_1.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_1.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_1.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_2.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_2.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_3.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_3.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_3.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_3.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_3.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_4.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_4.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_4.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_4.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_5.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_5.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_5.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_5.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_6.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_6.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_6.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_6.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_6.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_7.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_7.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_7.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_7.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_7.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_8.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_8.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_8.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_8.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_8.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_9.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_9.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_9.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_9.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_9.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_10.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_10.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_10.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_10.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_10.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_11.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_11.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_11.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_11.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_11.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_12.jpg",
-                    "description": "hirenasd_aepw_nov2011_mode_12.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "hirenasd_aepw_nov2011_mode_12.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/hirenasd_aepw_nov2011_mode_12.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "hirenasd_aepw_nov2011_mode_12.jpg"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_487",
+            "issued": "2011-11-03",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/487/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "HIRENASD Modeshapes Nov 2011 model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1331-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-11T09:01:25.000 to 2016-01-11T11:16:37.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1331-v1.0_q2hp-cscv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1331-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1331-v1.0_q2hp-cscv",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-11T09:01:25.000 to 2016-01-11T11:16:37.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1331 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1331 V1.0"
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
-                "knowledge",
-                "appel"
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
-            "identifier": "NASA-862__12",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1220175,22 +1220154,55 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__12",
+            "issued": "2018-06-25",
+            "keyword": [
+                "sharing",
+                "ask the academy",
+                "knowledge",
+                "appel"
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
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214474435-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SMAP Level 1C Sigma Naught High Res Data Quality Info",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1214474435-ASF",
             "issued": "2015-07-31",
-            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-24",
             "keyword": [
                 "platform characteristics",
                 "land surface",
@@ -1220199,138 +1220211,128 @@
                 "spectral/engineering",
                 "radar"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214474435-ASF.html",
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
-            "identifier": "C1214474435-ASF",
-            "description": "SMAP Level 1C Sigma Naught High Res Data Quality Info",
-            "title": "SMAP_L1C_SIGMA_NAUGHT_HIGH_RES_QA_V001",
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
+            "title": "SMAP_L1C_SIGMA_NAUGHT_HIGH_RES_QA_V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL17.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3B Monthly Gridded Atmosphere V005. Version 005. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL17.005.",
-            "issued": "2018-10-14",
-            "temporal": "2018-10-13T00:00:00Z/2024-09-02T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-10",
-            "keyword": [
-                "atmosphere",
-                "lidar",
-                "cryosphere",
-                "snow/ice",
-                "earth science",
-                "spectral/engineering",
-                "aerosols",
-                "clouds"
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
-            "identifier": "C2737997483-NSIDC_ECS",
             "description": "This data set contains a gridded summary of monthly global cloud fraction, total column optical depth over the oceans, polar cloud fraction, blowing snow frequency, apparent surface reflectivity, and ground detection frequency.",
-            "title": "ATLAS/ICESat-2 L3B Monthly Gridded Atmosphere V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL17.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL17.005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL17.005/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL17.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL17+V005",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL17+V005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL17/versions/5/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL17/versions/5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL17.005",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL17.005",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL17.005",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL17.005",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2737997483-NSIDC_ECS",
+            "issued": "2018-10-14",
+            "keyword": [
+                "atmosphere",
+                "lidar",
+                "cryosphere",
+                "snow/ice",
+                "earth science",
+                "spectral/engineering",
+                "aerosols",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL17.005",
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
+            "title": "ATLAS/ICESat-2 L3B Monthly Gridded Atmosphere V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A%2FE-SSI-2-REDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set has been generated by NASA's Galileo Project in order to distribute the images acquired by the Solid State Imaging (SSI) camera to the scientists and later to the Planetary Data System (PDS). The collection resides on volumes GO_0007 thru GO_0015 and consists of all images acquired by the Galileo spacecraft during the Gaspra and the second encounter with the Earth (Earth2). Included are images of Gaspra, the Earth's Moon and the Earth taken during the 1991 and 1992 encounters (SCLK 99757945 through 166324700), as well as additional star and calibration data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-e-ssi-2-redr-v1.0_q2rm-p8td",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "gaspra",
                 "jupiter",
@@ -1220341,63 +1220343,37 @@
                 "galileo",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A%2FE-SSI-2-REDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-e-ssi-2-redr-v1.0_q2rm-p8td",
-            "description": "This data set has been generated by NASA's Galileo Project in order to distribute the images acquired by the Solid State Imaging (SSI) camera to the scientists and later to the Planetary Data System (PDS). The collection resides on volumes GO_0007 thru GO_0015 and consists of all images acquired by the Galileo spacecraft during the Gaspra and the second encounter with the Earth (Earth2). Included are images of Gaspra, the Earth's Moon and the Earth taken during the 1991 and 1992 encounters (SCLK 99757945 through 166324700), as well as additional star and calibration data.",
-            "title": "GALILEO ORBITER ASTEROID AND EARTH 2 SOLID STATE IMAGING 2 R",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO ORBITER ASTEROID AND EARTH 2 SOLID STATE IMAGING 2 R"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-07-09",
-            "temporal": "2021-07-09T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "ephemeris",
-                "location",
-                "iss",
-                "coordinates",
-                "topo",
-                "space",
-                "trajectory",
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
-            "identifier": "nasa-iss-data_2021-07-09_q2u8-7xxw",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-07-09",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1220520,614 +1220496,619 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-07-09_q2u8-7xxw",
+            "issued": "2021-07-09",
+            "keyword": [
+                "ephemeris",
+                "location",
+                "iss",
+                "coordinates",
+                "topo",
+                "space",
+                "trajectory",
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
+            "temporal": "2021-07-09T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-07-09"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-3-RDR-VIS-CERES-SPECTRA-V1.0",
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
-                "1 ceres",
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the spectral      radiance (W/(m**2*sr*micron)) data from the Dawn VIR instrument          visible channel for all Ceres encounter mission phases. The data        cover the time period between 2014-12-26 and 2016-06-01.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-3-rdr-vis-ceres-spectra-v1.0_q2ug-u7xt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-3-RDR-VIS-CERES-SPECTRA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-3-rdr-vis-ceres-spectra-v1.0_q2ug-u7xt",
-            "description": "This data set contains the spectral      radiance (W/(m**2*sr*micron)) data from the Dawn VIR instrument          visible channel for all Ceres encounter mission phases. The data        cover the time period between 2014-12-26 and 2016-06-01.",
-            "title": "DAWN VIR CAL (RDR) CERES VISIBLE SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN VIR CAL (RDR) CERES VISIBLE SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-EXT1-RAW-V6.0",
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
+            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nEXTENDED MISSION PHASE 1 (EXT1) from January 13 until April 6, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first being archived.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-ext1-raw-v6.0_q2ui-2vmu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-EXT1-RAW-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-ext1-raw-v6.0_q2ui-2vmu",
-            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nEXTENDED MISSION PHASE 1 (EXT1) from January 13 until April 6, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first being archived.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 2 EXT1 RAW V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 2 EXT1 RAW V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0368-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-18T15:17:40.000 to 2014-10-18T21:30:09.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0368-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0368-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0368-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-18T15:17:40.000 to 2014-10-18T21:30:09.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0368 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0368 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/504",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Mickle, R.E., and A.J. Arnold. 2000. BOREAS TF-02 SSA-OA Tethersonde Meteorological and Ozone Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/504",
-            "issued": "2023-11-22",
-            "temporal": "1993-10-17T00:00:00Z/1994-09-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "air quality",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "atmospheric chemistry",
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
-            "identifier": "C2808092322-ORNL_CLOUD",
             "description": "The BOREAS TF-02 team collected various trace gas and energy flux data along with meteorological parameters at the SSA-OA site. This data set contains meteorological and ozone measurements from instruments mounted below a tethered balloon. These data were collected at the SSA-OA site to extend meteorological and ozone measurements made from the flux tower to heights of 300 m.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-02 SSA-OA Tethersonde Meteorological and Ozone Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F504",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F504",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf2met/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf2met/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF02_Tethersonde.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF02_Tethersonde.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/504",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/504",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf2met/comp/TF02_Tethersonde.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf2met/comp/TF02_Tethersonde.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf2met/comp/TF02_Tethersonde.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf2met/comp/TF02_Tethersonde.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf2met/comp/TF02_Tethersonde.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf2met/comp/TF02_Tethersonde.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf2met/comp/tf2met.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf2met/comp/tf2met.def",
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
+            "identifier": "C2808092322-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "air quality",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/504",
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
             "spatial": "53.63 -106.2",
+            "temporal": "1993-10-17T00:00:00Z/1994-09-19T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-02 SSA-OA Tethersonde Meteorological and Ozone Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/176/",
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
                 "fn": "Kanishka Bhaduri",
                 "hasEmail": "mailto:kanishka.bhaduri-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_176",
             "description": "This paper offers a local distributed algorithm for multivariate regression in large peer-to-peer environments. The algorithm is designed for distributed inferencing, data compaction, data modeling and classification tasks in many emerging peer-to-peer applications for bioinformatics, astronomy, social networking, sensor networks and web mining. Computing a global regression model from data available at the different peer-nodes using a traditional centralized algorithm for regression can be very costly and impractical because of the large number of data sources, the asynchronous nature of the peer-to-peer networks, and dynamic nature of the data/network. This paper proposes a two-step approach to deal with this problem. First, it offers an efficient local distributed algorithm that monitors the \u201cquality \u201d of the current regression model. If the model is outdated, it uses this algorithm as a feedback mechanism for rebuilding the model. The local nature of the monitoring algorithm guarantees low monitoring cost. Experimental results presented in this paper strongly support the theoretical claims.",
-            "title": "An Efficient Local Algorithm for Distributed Multivariate Regression",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Regression.pdf",
-                    "description": "Paper",
                     "@type": "dcat:Distribution",
+                    "description": "Paper",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Regression.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Regression.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_176",
+            "issued": "2010-09-22",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/176/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "An Efficient Local Algorithm for Distributed Multivariate Regression"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/PROBES/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Heymsfield, Andrew J and Aaron  Bansemer.2011. GPM GROUND VALIDATION CLOUD SPECTROMETER AND IMPACTOR (CIP) LPVEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/LPVEX/PROBES/DATA201",
-            "issued": "2011-02-25",
-            "temporal": "2010-08-06T00:00:00Z/2010-10-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds",
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
-            "identifier": "C1979130601-GHRC_DAAC",
             "description": "The GPM Ground Validation Cloud Spectrometer and Impactor (CIP) LPVEx dataset provides particle size spectra for the Global Precipitation Measurement (GPM) Misson Ground Validation Experiment. Data was collected by the Cloud spectrometer and impactor (CIP) and 2D-S (2-dimensional stereo probe) aboard the University of Wyoming King Air flown in Finland during the Light Precipitation Validation Experiment (LPVEx) from August to October 2010. Lat, lon, altitude, pressure, and temperature are provided with the total concentration of particles with diameter greater than 100 microns.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION CLOUD SPECTROMETER AND IMPACTOR (CIP) LPVEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/cip-2dp/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FPROBES%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FPROBES%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmcilpvex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmcilpvex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/cip-2dp/browse/2010-09-16/09162010_075400_CIPG.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/cip-2dp/browse/2010-09-16/09162010_075400_CIPG.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/lpvex/gpmcilpvex/gpmcilpvex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/lpvex/gpmcilpvex/gpmcilpvex_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/cip-2dp/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/cip-2dp/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/cip-2dp/browse/",
+            "identifier": "C1979130601-GHRC_DAAC",
+            "issued": "2011-02-25",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/PROBES/DATA201",
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
             "spatial": "25.04 60.06 25.37 61.36",
+            "temporal": "2010-08-06T00:00:00Z/2010-10-20T23:59:59Z",
             "theme": [
                 "LPVEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION CLOUD SPECTROMETER AND IMPACTOR (CIP) LPVEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109GA_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2023-10-10.  VIIRS/JPSS1 Surface Reflectance Daily L2G Global 1km and 500m SIN Grid NRT. Version 2. NASA GSFC LANCE. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ109GA_NRT.002. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt.",
-            "issued": "2023-10-10",
-            "temporal": "2023-10-10T00:00:00Z/2023-10-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
-                "earth science",
-                "surface thermal properties"
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
-            "identifier": "C2781246545-LANCEMODIS",
-            "description": "The VJ109GA_NRT is a Near Real Time (NRT) VIIRS/JPSS1 Surface Reflectance Daily L2G Global 1km and 500m SIN Grid product. The VIIRS surface reflectance products are estimates of surface reflectance in each of the VIIRS reflective bands I1-I3, M1-M5, M7, M8, M10, and M11. VJ109GA is a Level-2G surface reflectance product produced on a 10km x 10km grid. The VNP09GA surface reflectance product is composed of all available surface reflectance observations for a given day over a set of tiles with global coverage. The tile numbering scheme and boundaries are the same as for MODIS. The first set of observations for each data set and grid cell are projected onto a two-dimensional grid and stored as 10km square tiles at 500m and 1 km resolution.\r\n\r\nSurface reflectance is obtained by adjusting top-of-atmosphere reflectance to compensate for atmospheric effects. Corrections are made for the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. The inputs to the surface reflectance algorithm include top-of-atmosphere reflectance for the VIIRS visible bands (VJ102MOD, VJ102IMG), the VIIRS cloud mask and aerosol product , aerosol optical thickness, and atmospheric data obtained from a reanalysis (surface pressure, atmospheric precipitable water, and ozone concentration).\r\n\r\nAll surface reflectance products are produced for daytime conditions only. The product is produced under all atmospheric conditions except for night and oceans. Pixels when not produced are replaced by fill values in the Level-2 and Level-2G products.\r\n\r\n\r\nFor more information read Suomi-NPP VIIRS Surface Reflectance User's Guide at https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf\r\nor \r\n\r\nvisit VIIRS Land website at https://viirsland.gsfc.nasa.gov/Products/NASA/ReflectanceESDR.html",
-            "release-place": "NASA GSFC LANCE",
             "creator": "LANCEMODIS",
-            "title": "VIIRS/JPSS1 Surface Reflectance Daily L2G Global 1km and 500m SIN Grid NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VJ109GA_NRT is a Near Real Time (NRT) VIIRS/JPSS1 Surface Reflectance Daily L2G Global 1km and 500m SIN Grid product. The VIIRS surface reflectance products are estimates of surface reflectance in each of the VIIRS reflective bands I1-I3, M1-M5, M7, M8, M10, and M11. VJ109GA is a Level-2G surface reflectance product produced on a 10km x 10km grid. The VNP09GA surface reflectance product is composed of all available surface reflectance observations for a given day over a set of tiles with global coverage. The tile numbering scheme and boundaries are the same as for MODIS. The first set of observations for each data set and grid cell are projected onto a two-dimensional grid and stored as 10km square tiles at 500m and 1 km resolution.\r\n\r\nSurface reflectance is obtained by adjusting top-of-atmosphere reflectance to compensate for atmospheric effects. Corrections are made for the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. The inputs to the surface reflectance algorithm include top-of-atmosphere reflectance for the VIIRS visible bands (VJ102MOD, VJ102IMG), the VIIRS cloud mask and aerosol product , aerosol optical thickness, and atmospheric data obtained from a reanalysis (surface pressure, atmospheric precipitable water, and ozone concentration).\r\n\r\nAll surface reflectance products are produced for daytime conditions only. The product is produced under all atmospheric conditions except for night and oceans. Pixels when not produced are replaced by fill values in the Level-2 and Level-2G products.\r\n\r\n\r\nFor more information read Suomi-NPP VIIRS Surface Reflectance User's Guide at https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf\r\nor \r\n\r\nvisit VIIRS Land website at https://viirsland.gsfc.nasa.gov/Products/NASA/ReflectanceESDR.html",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109GA_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109GA_NRT.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ109GA_NRT",
-                    "description": "Direct access to the download site and directory hosting the VJ109GA_NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the VJ109GA_NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ109GA_NRT",
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
-                    "description": "Surface Reflectance Products' User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Reflectance Products' User Guide",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C2781246545-LANCEMODIS",
+            "issued": "2023-10-10",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109GA_NRT.002",
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
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "2023-10-10T00:00:00Z/2023-10-16T00:00:00Z",
             "theme": [
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Surface Reflectance Daily L2G Global 1km and 500m SIN Grid NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OETP-3-HIRESELECTRONS-V1.0",
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
-                "pioneer venus",
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The High Resolution Ne File. These data are based on measurements of the electron saturation current or the ion saturation current taken from as many voltampere curves as the telemetry data rate permitted. Since Ne is assumed equal to Ni everywhere in the ionosphere, either can be used as a measure of Ne. The ion current is used at high densities (Ni > 4x104cm-3) and the electron current is used at lower densities. Typically, 4 to 8 high resolution density samples are obtained in the interval between recovered voltampere curves, although this ratio is bit rate dependent. This provides Ne and Ni measurements at much smaller intervals than is possible from the voltampere curves themselves. High resolution measurements are typically available at 2 to 8 second intervals depending upon the telemetry rate available to the OETP at the time.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oetp-3-hireselectrons-v1.0_q37m-ib47",
+            "issued": "2018-06-26",
+            "keyword": [
+                "pioneer venus",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OETP-3-HIRESELECTRONS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oetp-3-hireselectrons-v1.0_q37m-ib47",
-            "description": "The High Resolution Ne File. These data are based on measurements of the electron saturation current or the ion saturation current taken from as many voltampere curves as the telemetry data rate permitted. Since Ne is assumed equal to Ni everywhere in the ionosphere, either can be used as a measure of Ne. The ion current is used at high densities (Ni > 4x104cm-3) and the electron current is used at lower densities. Typically, 4 to 8 high resolution density samples are obtained in the interval between recovered voltampere curves, although this ratio is bit rate dependent. This provides Ne and Ni measurements at much smaller intervals than is possible from the voltampere curves themselves. High resolution measurements are typically available at 2 to 8 second intervals depending upon the telemetry rate available to the OETP at the time.",
-            "title": "PVO VENUS ELECT TEMP PROBE CALIB HIGH RES ELECTRONS VER 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PVO VENUS ELECT TEMP PROBE CALIB HIGH RES ELECTRONS VER 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1808",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wang, J., M.K. Farina, A. Baccini, and M.A. Friedl. 2021. ABoVE: Annual Aboveground Biomass for Boreal Forests of ABoVE Core Domain, 1984-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1808",
-            "issued": "2021-02-27",
-            "temporal": "1984-01-01T00:00:00Z/2014-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "earth science",
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
-            "identifier": "C2111720412-ORNL_CLOUD",
             "description": "This dataset provides estimated annual aboveground biomass (AGB) density for live woody (tree and shrub) species and corresponding standard errors at a 30 m spatial resolution for the boreal forest biome portion of the Core Study Domain of NASA's Arctic-Boreal Vulnerability Experiment (ABoVE) Project (Alaska and Canada) over the time period 1984-2014. The data were derived from a time series of Landsat-5 and Landsat-7 surface reflectance imagery and full-waveform lidar returns from the Geoscience Laser Altimeter System (GLAS) flown onboard IceSAT from 2004 to 2008. The Change Detection and Classification (CCDC) model-fitting algorithm was used to estimate the seasonal variability in surface reflectance, and AGB density data were produced by applying allometric equations to the GLAS lidar data. A Gradient Boosted Machines machine learning algorithm was used to predict annual AGB density across the study domain given the seasonal variability in surface reflectance and other predictors. The data received statistical smoothing to reduce noise and uncertainty was estimated at the pixel level. These data contribute to the characterization of how biomass stocks are responding to climate and disturbance in boreal forests.",
-            "graphic-preview-description": "Spatial distribution of predicted aboveground biomass (AGB) density averaged over 1984-2014 for the ABoVE Core Study Domain. Solid black lines indicate the EPA Level 2 Ecoregion boundaries. Source: Wang et al. (2021)",
-            "title": "ABoVE: Annual Aboveground Biomass for Boreal Forests of ABoVE Core Domain, 1984-2014",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Annual_30m_AGB_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1808",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1808",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Annual_30m_AGB/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Annual_30m_AGB/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Annual_30m_AGB.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Annual_30m_AGB.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1808",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1808",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Annual_30m_AGB/comp/Annual_30m_AGB.pdf",
-                    "description": "ABoVE: Annual Aboveground Biomass for Boreal Forests of ABoVE Core Domain, 1984-2014: Annual_30m_AGB.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Annual Aboveground Biomass for Boreal Forests of ABoVE Core Domain, 1984-2014: Annual_30m_AGB.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Annual_30m_AGB/comp/Annual_30m_AGB.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Annual_30m_AGB_Fig1.png",
-                    "description": "Spatial distribution of predicted aboveground biomass (AGB) density averaged over 1984-2014 for the ABoVE Core Study Domain. Solid black lines indicate the EPA Level 2 Ecoregion boundaries. Source: Wang et al. (2021)",
                     "@type": "dcat:Distribution",
+                    "description": "Spatial distribution of predicted aboveground biomass (AGB) density averaged over 1984-2014 for the ABoVE Core Study Domain. Solid black lines indicate the EPA Level 2 Ecoregion boundaries. Source: Wang et al. (2021)",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Annual_30m_AGB_Fig1.png",
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
+            "graphic-preview-description": "Spatial distribution of predicted aboveground biomass (AGB) density averaged over 1984-2014 for the ABoVE Core Study Domain. Solid black lines indicate the EPA Level 2 Ecoregion boundaries. Source: Wang et al. (2021)",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Annual_30m_AGB_Fig1.png",
+            "identifier": "C2111720412-ORNL_CLOUD",
+            "issued": "2021-02-27",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "ecosystems",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1808",
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
             "spatial": "-165.41 51.78 -101.74 69.73",
+            "temporal": "1984-01-01T00:00:00Z/2014-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Annual Aboveground Biomass for Boreal Forests of ABoVE Core Domain, 1984-2014"
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
-                "aerosols",
-                "satellite",
-                "radiation",
-                "eos",
-                "clouds",
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
-            "identifier": "NASA-0000027__2",
+            "describedBy": "https://eosweb.larc.nasa.gov/project/calipso/calipso_table",
             "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international 'A-Train' (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO)",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1221135,257 +1221116,249 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "https://eosweb.larc.nasa.gov/project/calipso/calipso_table",
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-0000027__2",
+            "issued": "2018-06-25",
+            "keyword": [
+                "aerosols",
+                "satellite",
+                "radiation",
+                "eos",
+                "clouds",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67PCHURYUMOV-M31-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67pchuryumov-m31-v2.0_q39m-k97y",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67PCHURYUMOV-M31-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67pchuryumov-m31-v2.0_q39m-k97y",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP031 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP031 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-PROFILE-V1.1",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-profile-v1.1_q3ah-fiqn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-PROFILE-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-profile-v1.1_q3ah-fiqn",
-            "description": "not applicable",
-            "title": "MGS PROFILE DATA RECORDS V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS PROFILE DATA RECORDS V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-2-EDR-EROS%2FSURFACE-V1.0",
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
+            "description": "This data set contains the NEAR magnetometer (MAG) data for the EROS/SURFACE phase. The data set begins on 2001-02-13T00:00:00.000 and ends 2001-02-28T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw magnetometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-2-edr-eros-surface-v1.0_q3bc-3vur",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-2-EDR-EROS%2FSURFACE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-2-edr-eros-surface-v1.0_q3bc-3vur",
-            "description": "This data set contains the NEAR magnetometer (MAG) data for the EROS/SURFACE phase. The data set begins on 2001-02-13T00:00:00.000 and ends 2001-02-28T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw magnetometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
-            "title": "NEAR MAG DATA FOR EROS/SURFACE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR MAG DATA FOR EROS/SURFACE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0299-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-17T06:07:02.000 to 2014-09-17T15:08:07.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0299-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0299-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0299-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-17T06:07:02.000 to 2014-09-17T15:08:07.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0299 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0299 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1411142646-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR L1B2 Ellipsoid Product subset for the RICO region;See ProductionDateTime for published date.",
-            "issued": "2017-08-07",
-            "temporal": "2000-11-01T00:00:00Z/2005-02-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-08-08",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths"
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
-            "identifier": "C1411142646-LARC",
             "description": "This file contains the ellipsoid projected TOA Radiance over the RICO region,resampled to WGS84 ellipsoid corrected",
-            "title": "MISR L1B2 Ellipsoid Product subset for the RICO region V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1411142646-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1411142646-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1411142646-LARC",
+            "issued": "2017-08-07",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1411142646-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-08-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-11-01T00:00:00Z/2005-02-01T23:59:59Z",
             "theme": [
                 "RICO_2004",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR L1B2 Ellipsoid Product subset for the RICO region V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2012",
             "citation": "Pepijn Veefkind. 2006-06-26. OMDOAO3. Version 003. OMI/Aura Ozone (O3) DOAS Total Column 1-Orbit L2 Swath 13x24 km V003. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA2012. https://disc.gsfc.nasa.gov/datacollection/OMDOAO3_003.html. Digital Science Data.",
-            "issued": "2006-06-26",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-03-13",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2006.869987",
-                "https://doi.org/10.1109/TGRS.2006.872935",
-                "https://doi.org/10.1117/12.627013"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JENNIFER WEI, PH. D",
                 "hasEmail": "mailto:jennifer.c.wei@nasa.gov"
             },
+            "creator": "Pepijn Veefkind",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239966794-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The second release of Aura Ozone Monitoring Instrument (OMI) Version 003 OMI/Aura Level-2 Total Column Ozone Data Product OMDOAO3 is now available from the NASA Goddard Earth Sciences Data and Information Services Center (GES DISC) for the public access. The data were processed in late 2011 using Algorithm or PGE version 1.2.3 and released in March 2012. OMI provides two total column ozone products based on two different algorithms. This level-2 global total column ozone product at the pixel resolution (13x24 km at nadir), is based on the Differential Absorption Spectroscopy (DOAS) fitting technique that essentially uses the OMI UV radiance values between 331.1 and 336.1 nm. In addition to the total ozone column this product also contains auxiliary , derived and ancillary input parameters e.g. ozone slant column density, ozone ghost column density, air mass factor, scene reflectivity, radiance over the DOAS fit window, root mean square of DAOS fit, cloud fraction, cloud radiance, cloud pressure, terrain height, geolocation, viewing angles and quality flags. The shortname for this Level-2 OMI total column ozone product is OMDOAO3. The lead scientist for this product is Dr. J. Pepijn Veefkind.\n\nThe OMDOAO3 product files are stored in the version 5 Hierarchical Data Format (HDF-EOS5). Each file contains data from the day lit portion of an orbit (approximately 53 minutes) and is approximately 11 MB in size. There are approximately 14 orbits per day.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMDOAO3",
-            "creator": "Pepijn Veefkind",
-            "title": "OMI/Aura DOAS Total Column Ozone 1-Orbit L2 Swath 13x24 km V003 (OMDOAO3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMDOAO3_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2012",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2012",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1221394,74 +1221367,74 @@
                     "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMDOAO3_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMDOAO3_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMDOAO3.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMDOAO3.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMDOAO3_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMDOAO3_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Level2/OMDOAO3.003/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Level2/OMDOAO3.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMDOAO3.003/doc/README.OMDOAO3.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMDOAO3.003/doc/README.OMDOAO3.pdf",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-02.pdf",
-                    "description": "OMI Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-02.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMDOAO3_FileSpec_V003.pdf",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMDOAO3_FileSpec_V003.pdf",
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
@@ -1221471,27 +1221444,63 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMDOAO3_003.png",
+            "identifier": "C1239966794-GES_DISC",
+            "issued": "2006-06-26",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2012",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-03-13",
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
+            "series-name": "OMDOAO3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura DOAS Total Column Ozone 1-Orbit L2 Swath 13x24 km V003 (OMDOAO3) at GES DISC"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140303.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-455",
+            "issued": "2018-06-25",
             "keyword": [
                 "ctx",
                 "pds",
@@ -1221502,389 +1221511,358 @@
                 "hirise",
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
-            "identifier": "NASA-455",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 28",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140303.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 28"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/GAUGE/DATA202",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A, David  Wolff, Jianxin  Wang and Ali  Tokay.2016. GPM GROUND VALIDATION MET ONE RAIN GAUGE PAIRS IFLOODS V2 [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IFLOODS/GAUGE/DATA202",
-            "issued": "2016-07-26",
-            "temporal": "2013-04-06T22:34:00Z/2013-12-27T20:56:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "precipitation",
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
-            "identifier": "C1979699547-GHRC_DAAC",
             "description": "The GPM Ground Validation Met One Rain Gauge Pairs IFloodS V2 data measures the amount of fallen precipitation collected by a Model 380 tipping bucket rain gauge made by Met One Instruments, Inc. The gauge has a 30.5 cm diameter catchment funnel. Precipitation is collected to a resolution of 0.254 mm of liquid water for each bucket tip. These gauges measure rainfall over a 1 second interval. This data set has two types of files, the 1 second rainfall data and a 1-minute cubic-spline interpolated rain rate produced using the method described in Wang, 2008. There are two rain gauges located on each station (A or B), each with their own set of data files. Data were collected from April 2013 through December 2013 as part of the GPM Ground Validation Iowa Flood Studies (IFloodS) Field Experiment. More detailed information about the Met One Model 380 Precipitation Gauge is available at http://www.metone.com/docs/370_380_precipitation_gauge.pdf",
-            "title": "GPM GROUND VALIDATION MET ONE RAIN GAUGE PAIRS IFLOODS V2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FGAUGE%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FGAUGE%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmrgnaifld2",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmrgnaifld2",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauge_NASA/doc/gpmrgnaifld2_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauge_NASA/doc/gpmrgnaifld2_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauge_NASA/doc/README_IFloodS_APU-NASA_GMIN_v2.txt",
-                    "description": "Quality-controlled and Cubic Spline interpolated rain rates from IFloodS NASA gauges NASA0008",
                     "@type": "dcat:Distribution",
+                    "description": "Quality-controlled and Cubic Spline interpolated rain rates from IFloodS NASA gauges NASA0008",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauge_NASA/doc/README_IFloodS_APU-NASA_GMIN_v2.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauge_NASA/doc/README_IFloodS_APU-NASA_GAG_v2.txt",
-                    "description": "Quality-controlled and reformatted rainfall data taken from IFloodS NASA gauges  NASA00008",
                     "@type": "dcat:Distribution",
+                    "description": "Quality-controlled and reformatted rainfall data taken from IFloodS NASA gauges  NASA00008",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauge_NASA/doc/README_IFloodS_APU-NASA_GAG_v2.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
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
+            "identifier": "C1979699547-GHRC_DAAC",
+            "issued": "2016-07-26",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/GAUGE/DATA202",
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
             "spatial": "-93.5207 41.8471 -91.1898 43.3706",
+            "temporal": "2013-04-06T22:34:00Z/2013-12-27T20:56:00Z",
             "theme": [
                 "IFloodS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION MET ONE RAIN GAUGE PAIRS IFLOODS V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0852-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-21T21:02:00.000 to 2015-06-21T22:40:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0852-v1.0_q3nd-u844",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0852-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0852-v1.0_q3nd-u844",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-21T21:02:00.000 to 2015-06-21T22:40:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0852 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0852 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2N2ONS.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-08-22. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2N2ONS.008. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "clouds",
-                "earth science",
-                "atmosphere",
-                "air quality"
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
-            "identifier": "C1618042985-LARC",
             "description": "TL2N2ONS_8 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Nitrous Oxide Nadir Special Observation Version 8 data product. It consists of information for one molecular species for an entire Global Survey or Special Observation. TTES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object represented one of these",
-            "title": "TES/Aura L2 Nitrous Oxide Nadir Special Observation V008",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2N2ONS.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2N2ONS.008",
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2N2ONS.008",
-                    "description": "DOI data set landing page for TL2N2ONS_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2N2ONS_8",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2N2ONS.008",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2N2ONS.008/contents.html",
-                    "description": "OPeNDAP data access for TL2N2ONS_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2N2ONS_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2N2ONS.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1618042985-LARC",
-                    "description": "Earthdata Search for TL2N2ONS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2N2ONS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1618042985-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2N2ONS.008/",
-                    "description": "ASDC Direct Data Download for TL2N2ONS_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2N2ONS_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2N2ONS.008/",
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
+            "identifier": "C1618042985-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "clouds",
+                "earth science",
+                "atmosphere",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2N2ONS.008",
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
+            "title": "TES/Aura L2 Nitrous Oxide Nadir Special Observation V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC8-V1.0",
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
+            "description": "The Cassini Radio Science Titan Bistatic and Occultation experiments (TBOC8) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 6, 2016, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc8-v1.0_q3nx-ipy6",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC8-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc8-v1.0_q3nx-ipy6",
-            "description": "The Cassini Radio Science Titan Bistatic and Occultation experiments (TBOC8) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 6, 2016, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TBOC8 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TBOC8 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/3LTYEL5PPMWB",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee. 2024-06-01. OCO2_L2_Diagnostic. Version 11.2r. OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information V11.2r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/3LTYEL5PPMWB. https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Diagnostic_11.2r.html. Digital Science Data.",
-            "issued": "2024-04-01",
-            "temporal": "2019-11-30T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-01",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
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
-            "identifier": "C3090472506-GES_DISC",
-            "description": "Version 11.2r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection encompass various data fields used for diagnostic and pre-processing, including aerosol optical depth, albedo, absorption coefficients, fluorescence, XCO2 uncertainties, averaging kernel, surface type, etc.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_Diagnostic",
             "creator": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee",
-            "title": "OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information Retrospective Processing V11.2r (OCO2_L2_Diagnostic) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Dia_10__10132021.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11.2r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection encompass various data fields used for diagnostic and pre-processing, including aerosol optical depth, albedo, absorption coefficients, fluorescence, XCO2 uncertainties, averaging kernel, surface type, etc.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3LTYEL5PPMWB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3LTYEL5PPMWB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1221894,247 +1221872,246 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Diagnostic_11.2r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Diagnostic_11.2r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Diagnostic.11.2r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Diagnostic.11.2r/",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Diagnostic.11.2r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Diagnostic.11.2r/contents.html",
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
+            "identifier": "C3090472506-GES_DISC",
+            "issued": "2024-04-01",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/3LTYEL5PPMWB",
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
+            "temporal": "2019-11-30T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information Retrospective Processing V11.2r (OCO2_L2_Diagnostic) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT2-MTP029-V1.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 2 MTP029 mission phase. Comet C-G/67P was the primary target.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext2-mtp029-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT2-MTP029-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext2-mtp029-v1.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 2 MTP029 mission phase. Comet C-G/67P was the primary target.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT2 MTP029 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT2 MTP029 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/8esq-w553",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Glacier Covered Area for the State of Alaska, 1985-2020, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/8esq-w553.",
-            "issued": "1985-01-01",
-            "temporal": "1985-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-31",
-            "keyword": [
-                "cryosphere",
-                "earth science",
-                "glaciers/ice sheets"
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
-            "identifier": "C2245266323-NSIDCV0",
             "description": "This data set captures changes in glacier covered area across the state of Alaska for the period 1985 to 2020.The data set includes 18 biannual shapefiles each for overall glacier covered area, supraglacial debris area, and debris-free glacier covered area.",
-            "title": "Glacier Covered Area for the State of Alaska, 1985-2020, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F8esq-w553",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F8esq-w553",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G10040_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G10040_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/8esq-w553",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/8esq-w553",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/8esq-w553",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/8esq-w553",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2245266323-NSIDCV0",
+            "issued": "1985-01-01",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "glaciers/ice sheets"
+            ],
+            "landingPage": "https://doi.org/10.7265/8esq-w553",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-167.0 53.0 -130.0 69.0",
+            "temporal": "1985-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Glacier Covered Area for the State of Alaska, 1985-2020, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/canadarm",
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
-                "remote manipulator system",
-                "shuttle",
-                "international space station",
-                "canadarm",
-                "3d model"
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
-            "identifier": "NASA-324",
             "description": "Polygons: 663 Vertices: 1080",
-            "title": "NASA 3D Models: Canadarm",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1222142,23 +1222119,48 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-324",
+            "issued": "2018-06-25",
+            "keyword": [
+                "remote manipulator system",
+                "shuttle",
+                "international space station",
+                "canadarm",
+                "3d model"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/canadarm",
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
+            "title": "NASA 3D Models: Canadarm"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT2-MTP030-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Extension 2 phase from 31st May 2016 to 28th June 2016 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext2-mtp030-v1.0_q3xb-ehye",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "zeta cas",
@@ -1222166,94 +1222168,73 @@
                 "calibration",
                 "alpha lyr"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT2-MTP030-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext2-mtp030-v1.0_q3xb-ehye",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Extension 2 phase from 31st May 2016 to 28th June 2016 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 2 MTP030 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 2 MTP030 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-RSS-5-LOS-V1.0",
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
-                "lunar prospector",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation. For information on Lunar Prospector (LP) gravity investigations see [KONOPLIVETAL1998 CARRANZAETAL1999].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-rss-5-los-v1.0_q3xc-5d3q",
+            "issued": "2018-06-26",
+            "keyword": [
+                "lunar prospector",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-RSS-5-LOS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-rss-5-los-v1.0_q3xc-5d3q",
-            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation. For information on Lunar Prospector (LP) gravity investigations see [KONOPLIVETAL1998 CARRANZAETAL1999].",
-            "title": "LP L RSS LINE OF SIGHT ACCELERATION PROFILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LP L RSS LINE OF SIGHT ACCELERATION PROFILES V1.0"
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
-            "identifier": "NASA-773",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (18)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1222261,59 +1222242,80 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-773",
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
+            "title": "PDS Odyssey Radio Science Data (18)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04B-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-06-18 to 2014-07-02.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m04b-v1.0_q3xw-dbpe",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04B-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m04b-v1.0_q3xw-dbpe",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-06-18 to 2014-07-02.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 004B V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 004B V1.0"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mdis-2-edr-rawdata-v1.0_q3z6-xpue",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "neptune",
                 "venus",
@@ -1222346,233 +1222348,240 @@
                 "alioth",
                 "2p/encke 1 (1818 w1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MDIS-2-EDR-RAWDATA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mdis-2-edr-rawdata-v1.0_q3z6-xpue",
-            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes the Experiment Data Record (EDR) version of all available images acquired during the cruise phase to Mercury and includes post- launch checkout images, flyby images of Earth, Venus, Mercury, and the Moon, images acquired from Mercury orbit, and inflight calibration images. In addition to the imagery, anciliary information (including calibration files needed to process the data further) is included.",
-            "title": "MESSENGER MDIS EXPERIMENT DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESSENGER MDIS EXPERIMENT DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2003-06-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0008.",
-            "issued": "2003-06-04",
-            "temporal": "1998-04-27T00:00:00Z/1998-05-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-02",
-            "keyword": [
-                "earth science",
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation"
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
-            "identifier": "C1000000942-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.",
-            "title": "First ISCCP Regional Experiment - Arctic Cloud Experiment Utrecht University Tower",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0008",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000942-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_ACE_UTRECHT_TOWER_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_ACE_UTRECHT_TOWER_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000942-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0008",
-                    "description": "DOI data set landing page for FIRE_ACE_UTRECHT_TOWER_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_ACE_UTRECHT_TOWER_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0008",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_UTRECHT_TOWER/",
-                    "description": "ASDC Direct Data Download for FIRE_ACE_UTRECHT_TOWER_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_ACE_UTRECHT_TOWER_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_UTRECHT_TOWER/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_UTRECHT_TOWER/contents.html",
-                    "description": "OPeNDAP data access for FIRE_ACE_UTRECHT_TOWER_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_ACE_UTRECHT_TOWER_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_UTRECHT_TOWER/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000942-LARC_ASDC",
+            "issued": "2003-06-04",
+            "keyword": [
+                "earth science",
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0008",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>76.0 -167.85 76.0 -164.84 76.52 -164.84 76.52 -167.85 76.0 -167.85</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1998-04-27T00:00:00Z/1998-05-27T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment - Arctic Cloud Experiment Utrecht University Tower"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-IONFBR-96SEC-V1.0",
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
+            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 1 ENCOUNTER.  RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IN SOME REGIONS.  DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY.  THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY.  THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ionfbr-96sec-v1.0_q42z-p86b",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-IONFBR-96SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ionfbr-96sec-v1.0_q42z-p86b",
-            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 1 ENCOUNTER.  RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IN SOME REGIONS.  DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY.  THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY.  THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983).",
-            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION\n                                      FITS BROWSE 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION\n                                      FITS BROWSE 96 SEC"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-28-Jul-06.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-623",
+            "issued": "2018-06-25",
             "keyword": [
                 "apxs",
                 "hazcam",
@@ -1222584,192 +1222593,161 @@
                 "pds",
                 "spice"
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
-            "identifier": "NASA-623",
-            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 9",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-28-Jul-06.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 9"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3Q7CS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Yueh. 2018-10-01. Aquarius CAP Sea Surface Salinity and Wind Products. Version 5.0. Aquarius CAP Sea Surface Salinity and Wind Products. Jet Propulsion Laboratory, 4800 Oak Grove Drive, Pasadena, CA91109, USA. Archived by National Aeronautics and Space Administration, U.S. Government, JPL - Simon Yueh. https://doi.org/10.5067/AQR50-3Q7CS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. Simon Yueh, JPL - Simon Yueh, 2018-10-01, Aquarius CAP Level 3 Sea Surface Salinity Rain Corrected Standard Mapped Image 7-Day Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2018-08-23",
-            "temporal": "2011-08-26T00:00:00Z/2015-06-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-23",
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
-            "identifier": "C2491756351-POCLOUD",
-            "description": "Version 5.0 Aquarius CAP Level 3 products are the fourth release of the AQUARIUS/SAC-D mapped salinity and wind speed data based on the Combined Active Passive (CAP) algorithm. CAP Level 3 standard mapped image products contain gridded 1 degree spatial resolution salinity and wind speed data averaged over 7 day and monthly time scales.  This particular dataset is the 7-Day running mean sea surface salinity (SSS) rain corrected V5.0 Aquarius CAP product. CAP is a P.I. produced dataset developed and provided by JPL.  The CAP algorithm utilizes data from both the onboard radiometer and scatterometer to simultaneously retrieve salinity, wind speed and direction by minimizing the sum of squared differences between model and observations. The main improvements in CAP V5.0 relative to the previous version include: updates to the Geophysical Model Functions to 4th order harmonics with the inclusion of sea surface temperature (SST) and stability at air-sea interface effects; use of the Canadian Meteorological Center (CMC) SST product as the new source ancillary sea surface temperature data in place of NOAA OI SST. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Jet Propulsion Laboratory, 4800 Oak Grove Drive, Pasadena, CA91109, USA",
-            "series-name": "Aquarius CAP Sea Surface Salinity and Wind Products",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Simon Yueh",
-            "title": "Aquarius CAP Level 3 Sea Surface Salinity Rain Corrected Standard Mapped Image 7-Day Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_RAINCORRECTED_CAP_7DAY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Version 5.0 Aquarius CAP Level 3 products are the fourth release of the AQUARIUS/SAC-D mapped salinity and wind speed data based on the Combined Active Passive (CAP) algorithm. CAP Level 3 standard mapped image products contain gridded 1 degree spatial resolution salinity and wind speed data averaged over 7 day and monthly time scales.  This particular dataset is the 7-Day running mean sea surface salinity (SSS) rain corrected V5.0 Aquarius CAP product. CAP is a P.I. produced dataset developed and provided by JPL.  The CAP algorithm utilizes data from both the onboard radiometer and scatterometer to simultaneously retrieve salinity, wind speed and direction by minimizing the sum of squared differences between model and observations. The main improvements in CAP V5.0 relative to the previous version include: updates to the Geophysical Model Functions to 4th order harmonics with the inclusion of sea surface temperature (SST) and stability at air-sea interface effects; use of the Canadian Meteorological Center (CMC) SST product as the new source ancillary sea surface temperature data in place of NOAA OI SST. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Q7CS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Q7CS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_RAINCORRECTED_CAP_7DAY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_RAINCORRECTED_CAP_7DAY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/CAPv5/Aquarius-CAP-User-Guide-v5.0.pdf",
-                    "description": "Aquarius CAP V5.0 Algorithm and Data Users Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aquarius CAP V5.0 Algorithm and Data Users Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/CAPv5/Aquarius-CAP-User-Guide-v5.0.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756351-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756351-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756351-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756351-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/CAPv5/Aquarius-CAP-User-Guide-v5.0.pdf",
-                    "description": "ATBD, Validation & Uncertainty Analyses, Publications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation & Uncertainty Analyses, Publications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/CAPv5/Aquarius-CAP-User-Guide-v5.0.pdf",
+                    "mediaType": "application/pdf",
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
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_RAINCORRECTED_CAP_7DAY_V5.jpg",
+            "identifier": "C2491756351-POCLOUD",
+            "issued": "2018-08-23",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3Q7CS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-08-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Jet Propulsion Laboratory, 4800 Oak Grove Drive, Pasadena, CA91109, USA",
+            "series-name": "Aquarius CAP Sea Surface Salinity and Wind Products",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-26T00:00:00Z/2015-06-08T00:00:00Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius CAP Level 3 Sea Surface Salinity Rain Corrected Standard Mapped Image 7-Day Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Santee, M., Livesey, N. and Read, W.. 2015-02-19. ML2CLO. Version 004. MLS/Aura Level 2 Chlorine Monoxide (ClO) Mixing Ratio V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2004. https://disc.gsfc.nasa.gov/datacollection/ML2CLO_004.html. Digital Science Data.",
-            "issued": "2015-02-19",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-02-19",
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
-            "identifier": "C1251101234-GES_DISC",
-            "description": "ML2CLO is the EOS Aura Microwave Limb Sounder (MLS) standard product for chlorine monoxide derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 147 and 1.0 hPa, and the vertical resolution varies between 3 and 4.5 km. Users of the ML2CLO data product should read section 3.6 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2CLO",
             "creator": "Santee, M., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Chlorine Monoxide (ClO) Mixing Ratio V004 (ML2CLO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2CLO_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2CLO is the EOS Aura Microwave Limb Sounder (MLS) standard product for chlorine monoxide derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 147 and 1.0 hPa, and the vertical resolution varies between 3 and 4.5 km. Users of the ML2CLO data product should read section 3.6 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1222779,313 +1222757,310 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2CLO_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2CLO_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2CLO.004/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2CLO.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2CLO.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2CLO.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2CLO_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2CLO_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2CLO_004.png",
+            "identifier": "C1251101234-GES_DISC",
+            "issued": "2015-02-19",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2004",
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
+            "series-name": "ML2CLO",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Chlorine Monoxide (ClO) Mixing Ratio V004 (ML2CLO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M06-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m06-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "16 cyg b",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M06-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m06-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP006 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP006 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1661710604-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
-            "issued": "2019-11-27",
-            "temporal": "1994-09-30T00:00:00Z/1994-10-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-24",
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
-            "identifier": "C1661710604-ASF",
             "description": "STS-68 SIR-C Slant Range Product",
-            "title": "STS-68_SLC",
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
+            "identifier": "C1661710604-ASF",
+            "issued": "2019-11-27",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1661710604-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>60.5933 -167.484 60.5933 173.996 -58.2098 173.996 -58.2098 -167.484 60.5933 -167.484</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1994-09-30T00:00:00Z/1994-10-12T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "STS-68_SLC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-URAP-4-SUMM-RAR-AVG-E-10MIN-V1.0",
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
+            "description": "C USER&apos;S GUIDE TO RAR 144 SECOND AVERAGED DATA FILES ------------------ This document describes the contents and format of the RAR 144 second averaged data files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-urap-4-summ-rar-avg-e-10min-v1.0_q4fu-zn3m",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-URAP-4-SUMM-RAR-AVG-E-10MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-urap-4-summ-rar-avg-e-10min-v1.0_q4fu-zn3m",
-            "description": "C USER&apos;S GUIDE TO RAR 144 SECOND AVERAGED DATA FILES ------------------ This document describes the contents and format of the RAR 144 second averaged data files.",
-            "title": "ULY JUP URAP RADIO ASTRONOMY REC AVERAGE E-FIELD 10 MIN",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULY JUP URAP RADIO ASTRONOMY REC AVERAGE E-FIELD 10 MIN"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ZF4OXSD2NS7W",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L1B Polarimetric GNSS Reflectometry, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ZF4OXSD2NS7W.",
-            "issued": "2015-10-01",
-            "temporal": "2015-10-01T00:00:00Z/2024-11-18T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
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
-            "identifier": "C3236702461-NSIDCV0",
             "description": "This product represents the first full polarimetric Global Navigation Satellite System Reflectometry (GNSS-R) dataset, derived from the Soil Moisture Active Passive (SMAP) mission radar. The main parameters are the normalized Stokes parameters, total power normalized bistatic radar cross section, and reflectivity. The SMAP radar receiver, in bistatic radar configuration, measures the horizontal and vertical components of the Global Positioning System (GPS) signal as it is reflected and scatters from the Earth\u2019s surface. Stokes parameters are computed with these horizontal and vertical polarization measurements. The dataset comprises a full reconstruction of the Earth' surface polarimetric values, with approximately 3,200 observations per day and about 1,200,000 per year.",
-            "title": "SMAP L1B Polarimetric GNSS Reflectometry, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZF4OXSD2NS7W",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZF4OXSD2NS7W",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0795_SMAP_Reflectometry_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0795_SMAP_Reflectometry_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ZF4OXSD2NS7W",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ZF4OXSD2NS7W",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ZF4OXSD2NS7W",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ZF4OXSD2NS7W",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3236702461-NSIDCV0",
+            "issued": "2015-10-01",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ZF4OXSD2NS7W",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-10-01T00:00:00Z/2024-11-18T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP L1B Polarimetric GNSS Reflectometry, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CBM5W8T7HHL6",
             "citation": "William J. Blackwell, MIT Lincoln Laboratory. 2023-03-01. TROPICS01ANTTL1A. Version 1.0. TROPICS01\u00a0Pathfinder\u00a0L1A Orbital Geolocated Native-Resolution Antenna Temperatures V1.0. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/CBM5W8T7HHL6. https://disc.gsfc.nasa.gov/datacollection/TROPICS01ANTTL1A_1.0.html. Digital Science Data.",
-            "issued": "2021-07-19",
-            "temporal": "2021-07-19T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "references": [
-                "https://doi.org/10.5067/CBM5W8T7HHL6"
-            ],
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "microwave"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kristan Morgan",
                 "hasEmail": "mailto:kristan.l.morgan@nasa.gov"
             },
+            "creator": "William J. Blackwell, MIT Lincoln Laboratory",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2622842528-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The \"Time-Resolved Observations of Precipitation structure and storm Intensity with a Constellation of Smallsats\" (TROPICS) mission has a goal of providing nearly all-weather observations of three-dimensional temperature and humidity, as well as cloud ice and precipitation horizontal structure, at high temporal resolution to conduct high-value science investigations of tropical cyclones.  The mission comprises a constellation of six identical Space Vehicles (SVs) conforming to the 3U form factor and hosting a passive microwave spectrometer payload.  This dataset is produced from the Pathfinder satellite, a single 3U small satellite, which has launched previous to the constellation, on a sun-synchronous orbital plane.\n\nEach SV hosts an identical high-performance spectrometer named the TROPICS Millimeter-wave Sounder (TMS) that will provide temperature profiles using seven channels near the 118.75-GHz oxygen absorption line, water vapor profiles using three channels near the 183-GHz water vapor absorption line, imagery in a single channel near 90 GHz for precipitation measurements (when combined with higher resolution water vapor channels), and a single channel near 205 GHz that is more sensitive to cloud-sized ice particles.\n\nEach TROPICS netCDF file contains a granule of data with 81 spots and approximately 2880 scans, where a granule is defined as an orbit's worth of data.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TROPICS01ANTTL1A",
-            "creator": "William J. Blackwell, MIT Lincoln Laboratory",
-            "title": "TROPICS01\u00a0Pathfinder\u00a0L1A Orbital Geolocated Native-Resolution Antenna Temperatures V1.0",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TROPICS01ANTTL1A_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCBM5W8T7HHL6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCBM5W8T7HHL6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1223095,139 +1223070,145 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS01ANTTL1A_1.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS01ANTTL1A_1.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/.Twp5FGhb5T/TROPICS_L1A/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/.Twp5FGhb5T/TROPICS_L1A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/.Twp5FGhb5T/TROPICS_L1A/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/.Twp5FGhb5T/TROPICS_L1A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICS01ANTTL1A_1.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICS01ANTTL1A_1.0",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS.UserGuide.pdf",
-                    "description": "TROPICS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS User Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS.UserGuide.pdf",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/README.TROPICS01L1.pdf",
-                    "description": "TROPICS01L1 README",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS01L1 README",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/README.TROPICS01L1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TROPICS01ANTTL1A_01.png",
+            "identifier": "C2622842528-GES_DISC",
+            "issued": "2021-07-19",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/CBM5W8T7HHL6",
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
+            "series-name": "TROPICS01ANTTL1A",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-07-19T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPICS (EVI-3)",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPICS01\u00a0Pathfinder\u00a0L1A Orbital Geolocated Native-Resolution Antenna Temperatures V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0944-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-05T10:09:25.000 to 2015-08-05T17:26:49.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0944-v1.0_q4rd-87uy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0944-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0944-v1.0_q4rd-87uy",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-05T10:09:25.000 to 2015-08-05T17:26:49.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0944 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0944 V1.0"
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
-            "identifier": "NASA-767",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (24)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1223235,401 +1223216,398 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-767",
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
+            "title": "PDS Odyssey Radio Science Data (24)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1271-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-20T07:00:25.000 to 2015-12-20T12:55:09.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1271-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1271-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1271-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-20T07:00:25.000 to 2015-12-20T12:55:09.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1271 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1271 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-S3COORDS-48.0SEC-V1.1",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-s3coords-48.0sec-v1.1_q4vk-535g",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-S3COORDS-48.0SEC-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-s3coords-48.0sec-v1.1_q4vk-535g",
-            "description": "not applicable",
-            "title": "VG1 JUP MAG RESAMPLED SYSTEM III (1965) COORDS 48.0SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 JUP MAG RESAMPLED SYSTEM III (1965) COORDS 48.0SEC V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/ZOG6BCSE26HV",
             "citation": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL. 2020-01-30. GLDAS_VIC10_3H. Version 2.1. GLDAS VIC Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.1. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ZOG6BCSE26HV. https://disc.gsfc.nasa.gov/datacollection/GLDAS_VIC10_3H_2.1.html. Digital Science Data.",
-            "issued": "2020-01-30",
-            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-30",
-            "references": [
-                "https://doi.org/10.1175/BAMS-85-3-381"
-            ],
-            "keyword": [
-                "atmospheric pressure",
-                "terrestrial hydrosphere",
-                "atmospheric winds",
-                "surface water",
-                "surface thermal properties",
-                "soils",
-                "atmospheric water vapor",
-                "snow/ice",
-                "precipitation",
-                "land surface",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hualan Rui",
                 "hasEmail": "mailto:Hualan.Rui@nasa.gov"
             },
+            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1690022329-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "NASA Global Land Data Assimilation System Version 2 (GLDAS-2) has three components: GLDAS-2.0, GLDAS-2.1, and GLDAS-2.2.  GLDAS-2.0 is forced entirely with the Princeton meteorological forcing input data and provides a temporally consistent series from 1948 through 2014.  GLDAS-2.1 is forced with a combination of model and observation data from 2000 to present.  GLDAS-2.2 product suites use data assimilation (DA), whereas the GLDAS-2.0 and GLDAS-2.1 products are \"open-loop\" (i.e., no data assimilation).  The choice of forcing data, as well as DA observation source, variable, and scheme, vary for different GLDAS-2.2 products.\n\nGLDAS-2.1 data products are now available in two production streams: one stream is forced with combined forcing data including GPCP version 1.3 (the main production stream), and the other stream is processed without this forcing data (the early production stream). Since the GPCP Version 1.3 data have a 3-4 month latency, the GLDAS-2.1 data products are first created without it, and are designated as Early Products (EPs), with about 1.5 month latency. Once the GPCP Version 1.3 data become available, the GLDAS-2.1 data products are processed in the main production stream and are removed from the Early Products archive. \n\nThis data product is for GLDAS-2.1 VIC 3-hourly 1.0 degree data from the main production stream. It was simulated with the VIC 4.1.2 Land Surface Model in Land Information System (LIS) Version 7.  The data product contains 34 land surface fields from January 2000 to present.  The GLDAS-2.1 data are archived and distributed in NetCDF format. The GLDAS-2.1 products supersede their corresponding GLDAS-1 products.\n\nThe GLDAS-2.1 simulation started on January 1, 2000 using the conditions from the GLDAS-2.0 simulation. This simulation was forced with National Oceanic and Atmospheric Administration (NOAA)/Global Data Assimilation System (GDAS) atmospheric analysis fields (Derber et al., 1991), the disaggregated Global Precipitation Climatology Project (GPCP) V1.3 Daily Analysis precipitation fields (Adler et al., 2003; Huffman et al., 2001), and the Air Force Weather Agency's AGRicultural METeorological modeling system (AGRMET) radiation fields.  The simulation used with GDAS and GPCP only from 2000 to February 2001, followed by addition of AGRMET for March 1, 2001 onwards.\n\nIn October 2020, all 3-hourly and monthly GLDAS-2 data were post-processed with the MOD44W MODIS land mask.  Previously, some grid boxes over inland water were considered as over land and, thus, had non-missing values.  The post-processing corrected this issue and masked out all model output data over inland water; the post-processing did not affect the meteorological forcing variables. More information can be found in the GLDAS-2 README.  The MOD44W MODIS land mask is available on the GLDAS Project site.\n\nIf you had downloaded the GLDAS data prior to November 2020, please download the data again to receive the post-processed data.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GLDAS_VIC10_3H",
-            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
-            "graphic-preview-description": "GLDAS-2.1 VIC 3-hourly 1.0 degree soil moisture of surface layer (0-30 cm) [kg/m2] 03Z Jan 01, 2000.",
-            "title": "GLDAS VIC Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.1 (GLDAS_VIC10_3H) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_VIC10_3H_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZOG6BCSE26HV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZOG6BCSE26HV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_VIC10_3H_2.1.png",
-                    "description": "GLDAS-2.1 VIC 3-hourly 1.0 degree soil moisture of surface layer (0-30 cm) [kg/m2] 03Z Jan 01, 2000.",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS-2.1 VIC 3-hourly 1.0 degree soil moisture of surface layer (0-30 cm) [kg/m2] 03Z Jan 01, 2000.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_VIC10_3H_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_VIC10_3H_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_VIC10_3H_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_VIC10_3H.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_VIC10_3H.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_VIC10_3H_2.1",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_VIC10_3H_2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_VIC10_3H.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_VIC10_3H.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/README_GLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/README_GLDAS2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ldas.gsfc.nasa.gov/gldas/",
-                    "description": "GLDAS Project Web Site",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS Project Web Site",
+                    "downloadURL": "https://ldas.gsfc.nasa.gov/gldas/",
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
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_VIC10_3H.2.1",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_VIC10_3H.2.1",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_VIC10_3H.2.1/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_VIC10_3H.2.1/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "GLDAS-2.1 VIC 3-hourly 1.0 degree soil moisture of surface layer (0-30 cm) [kg/m2] 03Z Jan 01, 2000.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_VIC10_3H_2.1.png",
+            "identifier": "C1690022329-GES_DISC",
+            "issued": "2020-01-30",
+            "keyword": [
+                "atmospheric pressure",
+                "terrestrial hydrosphere",
+                "atmospheric winds",
+                "surface water",
+                "surface thermal properties",
+                "soils",
+                "atmospheric water vapor",
+                "snow/ice",
+                "precipitation",
+                "land surface",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ZOG6BCSE26HV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-01-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1175/BAMS-85-3-381"
+            ],
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "GLDAS_VIC10_3H",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "GLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLDAS VIC Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.1 (GLDAS_VIC10_3H) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/LIS/LIS/DATA305",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Albrecht, Rachel I, Steve  Goodman, Dennis  Buechler, Richard J. Blakeslee and Hugh  Christian.2016. LIS 0.1 DEGREE VERY HIGH RESOLUTION GRIDDED LIGHTNING SEASONAL CLIMATOLOGY (VHRSC) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/LIS/LIS/DATA305",
-            "issued": "2016-03-02",
-            "temporal": "1998-01-01T00:00:00Z/2013-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "weather events",
-                "atmospheric electricity"
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
-            "identifier": "C1979883491-GHRC_DAAC",
             "description": "The LIS 0.1 Degree Very High Resolution Gridded Lightning Seasonal Climatology (VHRSC) dataset consists of gridded seasonal climatologies of total lightning flash rates seen by the Lightning Imaging Sensor (LIS) from January 1, 1998 through December 31, 2013. LIS is an instrument on the Tropical Rainfall Measurement Mission satellite (TRMM) used to detect the distribution and variability of total lightning occurring in the Earth's tropical and subtropical regions. This information can be used for severe storm detection and analysis, and also for lightning-atmosphere interaction studies. The gridded climatologies include annual mean flash rate, mean diurnal cycle of flash rate with 24 hour resolution, and mean annual cycle of flash rate with daily, monthly, or seasonal resolution. All datasets are in 0.1 degree spatial resolution. The mean annual cycle of flash rate datasets (i.e., daily, monthly or seasonal) have both 49-day and 1 degree boxcar moving averages to remove diurnal cycle and smooth regions with low flash rate, making the results more robust.",
-            "graphic-preview-description": "N/A",
-            "title": "LIS 0.1 DEGREE VERY HIGH RESOLUTION GRIDDED LIGHTNING SEASONAL CLIMATOLOGY (VHRSC) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRSC/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLIS%2FDATA305",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLIS%2FDATA305",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=lisvhrsc",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=lisvhrsc",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRSC/browse/lis_vhrsc_1998_2013_v01.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRSC/browse/lis_vhrsc_1998_2013_v01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/LIS/LIS/DATA306",
-                    "description": "Collection DOI for set of related datasets",
                     "@type": "dcat:Distribution",
+                    "description": "Collection DOI for set of related datasets",
+                    "downloadURL": "http://dx.doi.org/10.5067/LIS/LIS/DATA306",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/doc/LIS_VHRES_Guide.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/doc/LIS_VHRES_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/BAMS-D-14-00193.1",
-                    "description": "Where are the lightning hotspots on Earth?",
                     "@type": "dcat:Distribution",
+                    "description": "Where are the lightning hotspots on Earth?",
+                    "downloadURL": "http://dx.doi.org/10.1175/BAMS-D-14-00193.1",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/doc/read_example-LIS_VHRC.R",
-                    "description": "LIS Very  High Resolution Climatology Data Reader Code",
                     "@type": "dcat:Distribution",
+                    "description": "LIS Very  High Resolution Climatology Data Reader Code",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/doc/read_example-LIS_VHRC.R",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/data/data_lis_vhr-climatology.html",
-                    "description": "Google Earth Tool",
                     "@type": "dcat:Distribution",
+                    "description": "Google Earth Tool",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/data/data_lis_vhr-climatology.html",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/highlights-albrecht-et-als-where-are-lightning-hotspots-earth%E2%80%99-publication",
-                    "description": "Highlights from Albrecht et. al's 'Where Are the Lightning Hotspots on Earth?' publication",
                     "@type": "dcat:Distribution",
+                    "description": "Highlights from Albrecht et. al's 'Where Are the Lightning Hotspots on Earth?' publication",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/highlights-albrecht-et-als-where-are-lightning-hotspots-earth%E2%80%99-publication",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRSC/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRSC/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRSC/browse/",
+            "identifier": "C1979883491-GHRC_DAAC",
+            "issued": "2016-03-02",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "weather events",
+                "atmospheric electricity"
+            ],
+            "landingPage": "https://doi.org/10.5067/LIS/LIS/DATA305",
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
             "spatial": "-180.0 -38.0 180.0 38.0",
+            "temporal": "1998-01-01T00:00:00Z/2013-12-31T23:59:59Z",
             "theme": [
                 "LIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LIS 0.1 DEGREE VERY HIGH RESOLUTION GRIDDED LIGHTNING SEASONAL CLIMATOLOGY (VHRSC) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gille, John and Gray, Lesley J.. 2013-08-19. H3ZFC8MEXT. Version 007. HIRDLS/Aura Level 3 Extinction at 8.3 Microns 1deg Lat Zonal Fourier Coefficients V007. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/HIRDLS/DATA301. https://disc.gsfc.nasa.gov/datacollection/H3ZFC8MEXT_007.html. Digital Science Data.",
-            "issued": "2013-05-31",
-            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-31",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
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
-            "identifier": "C1251100820-GES_DISC",
-            "description": "The \"HIRDLS/Aura Level 3 Extinction at 8.3 Microns Zonal Fourier Coefficients\" version 7 data product (H3ZFC8MEXT) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 215 to 20 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "H3ZFC8MEXT",
             "creator": "Gille, John and Gray, Lesley J.",
-            "title": "HIRDLS/Aura Level 3 Extinction at 8.3 Microns 1deg Lat Zonal Fourier Coefficients V007 (H3ZFC8MEXT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFC8MEXT_007.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The \"HIRDLS/Aura Level 3 Extinction at 8.3 Microns Zonal Fourier Coefficients\" version 7 data product (H3ZFC8MEXT) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 215 to 20 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1223639,469 +1223617,469 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFC8MEXT_007.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFC8MEXT_007.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFC8MEXT.007/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFC8MEXT.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFC8MEXT.007/HIRDLS-Aura_L3ZFC8MEXT_v07-00-20-c02_2005d022-2008d077.he5.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFC8MEXT.007/HIRDLS-Aura_L3ZFC8MEXT_v07-00-20-c02_2005d022-2008d077.he5.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFC8MEXT_007",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFC8MEXT_007",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFC8MEXT_007.png",
+            "identifier": "C1251100820-GES_DISC",
+            "issued": "2013-05-31",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA301",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "H3ZFC8MEXT",
             "spatial": "-180.0 -64.0 180.0 80.0",
+            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HIRDLS/Aura Level 3 Extinction at 8.3 Microns 1deg Lat Zonal Fourier Coefficients V007 (H3ZFC8MEXT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L2/ERR/OC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3B/OLCI/L2/ERR/OC/2022.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere"
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
-            "identifier": "C2250852708-OB_DAAC",
             "description": "The Ocean and Land Colour Instrument (OLCI) is the successor to ENVISAT's Medium Resolution Imaging Spectrometer (MERIS) having additional spectral channels, different camera arrangements and simplified on-board processing. The OLCI is a push-broom instrument with five camera modules sharing the field of view. The field of view of the five cameras is arranged in a fan-shaped configuration in the vertical plane, perpendicular to the platform velocity. Each camera has an individual field of view of 14.2\u00b0 and a 0.6\u00b0 overlap with its neighbors. The whole field of view is shifted across track by 12.6\u00b0 away from the sun to minimize the impact of sun glint. OLCI is equipped with on-board calibration hardware based on sun diffusers. There are three sun diffusers--two 'white' diffusers dedicated to radiometric calibration and one dedicated to spectral calibration, with spectral reflectance features. The native resolution is approximately 300m, refered to as Full Resolution (FR). A Reduced Resolution (RR) processing mode provides Level-1B data at sampling rates decreased by a factor of four in both spatial dimensions resulting to resolution of approximately 1.2 km.",
-            "title": "Sentinel-3B OLCI Level-2 Earth-observation Reduced Resolution (ERR) Ocean Color (OC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL2%2FERR%2FOC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL2%2FERR%2FOC%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/S3B-OLCI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/S3B-OLCI/",
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
                 }
             ],
+            "identifier": "C2250852708-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L2/ERR/OC/2022",
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
+            "title": "Sentinel-3B OLCI Level-2 Earth-observation Reduced Resolution (ERR) Ocean Color (OC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5C24TC5",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Soil Temperature Station Data from Permafrost Regions of Russia (Selection of Five Stations), 1915 - 2000, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5C24TC5.",
-            "issued": "1915-01-01",
-            "temporal": "1915-01-01T00:00:00Z/2000-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2000-12-31",
-            "keyword": [
-                "land surface",
-                "cryosphere",
-                "surface thermal properties",
-                "frozen ground",
-                "earth science"
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
-            "identifier": "C2170960160-NSIDCV0",
             "description": "This data set includes soil temperature data from boreholes located at five stations in Russia: Yakutsk, Verkhoyansk, Pokrovsk, Isit', and Churapcha. The data have been compiled into five Microsoft Excel files, one for each station. Air temperature measured at these five stations was also included when available. \n\nThis data set was compiled to go with a classroom learning activity called \"How Permanent is Permafrost.\" To view the activity, see the PDF file of the same name under the Technical References tab.\n\nThere are two different versions of the Excel files: a complete version and a subsetted version. Both versions exist for each of the five stations for a total of 10 files. The complete versions of the files contain borehole temperature data at all available standard depths: 0.2 m, 0.4 m, 0.6 m, 0.8 m, 1.2 m, 1.6 m, 2.0 m, 2.4 m, and 3.2 m. The subsetted versions of the files contain data from the 0.8 m and 3.2 m depths only. The complete version is more applicable to scientific investigation. The subset version is provided for K-12 teachers and is featured in the \"How Permanent is Permafrost?\" classroom activity.",
-            "title": "Soil Temperature Station Data from Permafrost Regions of Russia (Selection of Five Stations), 1915 - 2000, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5C24TC5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5C24TC5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02189_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02189_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5C24TC5",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5C24TC5",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5C24TC5",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5C24TC5",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2170960160-NSIDCV0",
+            "issued": "1915-01-01",
+            "keyword": [
+                "land surface",
+                "cryosphere",
+                "surface thermal properties",
+                "frozen ground",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5C24TC5",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2000-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "125.3 60.8 133.4 67.6",
+            "temporal": "1915-01-01T00:00:00Z/2000-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Temperature Station Data from Permafrost Regions of Russia (Selection of Five Stations), 1915 - 2000, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC11-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC11) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 26-27, 2010, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc11-v1.0_q538-wkc2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC11-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc11-v1.0_q538-wkc2",
-            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC11) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 26-27, 2010, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC11 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SROC11 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-DRIFT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "L. Centurioni, V. Hormann, G. Reverdin, A. Hasson, A. Supply, D. Volkov. 2019-10-24. SPURS-2 Drifter data for the E. Tropical Pacific field campaign. Version 1.0. SPURS Field Campaign Drifter Data Products. Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-DRIFT. http://podaac.jpl.nasa.gov/SPURS. L. Centurioni, V. Hormann, G. Reverdin, A. Hasson, A. Supply, D. Volkov, SPURS Data Management PI, Fred Bingham, 2019-10-24, SPURS-2 Drifter data for the E. Tropical Pacific field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-05-30",
-            "temporal": "2016-06-20T05:57:00Z/2019-03-14T12:04:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
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
-            "identifier": "C2491772335-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. A drifter is a passive Lagrangian sensor platform consisting of a surface buoy and tethered subsurface drogue. Drifter buoys contain GPS/ARGOS and satellite data transmitters, with sensors measuring temperature and other properties. For SPURS-2, a range of drifters were deployed during both Revelle SPURS-2 cruises. These included: standard Surface Velocity Program (SVP) drifters with salinity sensors added (SVP/S), Surface Contact Salinity drifters, CODE, SADOS, AOML and CARTHE-SUPRACT drifters.  For each series, drifter data have been aggregrated within single netCDF data files with their corresponding drifter-IDs and associated near-surface salinity, temperature georeferenced (GPS and ARGOS) trajectory series data.",
-            "release-place": "Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA",
-            "series-name": "SPURS-2 Drifter data for the E. Tropical Pacific field campaign",
-            "graphic-preview-description": "Thumbnail",
             "creator": "L. Centurioni, V. Hormann, G. Reverdin, A. Hasson, A. Supply, D. Volkov",
-            "title": "SPURS-2 Drifter data for the E. Tropical Pacific field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_DRIFTER.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. A drifter is a passive Lagrangian sensor platform consisting of a surface buoy and tethered subsurface drogue. Drifter buoys contain GPS/ARGOS and satellite data transmitters, with sensors measuring temperature and other properties. For SPURS-2, a range of drifters were deployed during both Revelle SPURS-2 cruises. These included: standard Surface Velocity Program (SVP) drifters with salinity sensors added (SVP/S), Surface Contact Salinity drifters, CODE, SADOS, AOML and CARTHE-SUPRACT drifters.  For each series, drifter data have been aggregrated within single netCDF data files with their corresponding drifter-IDs and associated near-surface salinity, temperature georeferenced (GPS and ARGOS) trajectory series data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-DRIFT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-DRIFT",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_DRIFTER.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_DRIFTER.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772335-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772335-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772335-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772335-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_DRIFTER.jpg",
+            "identifier": "C2491772335-POCLOUD",
+            "issued": "2019-05-30",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-DRIFT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-05-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA",
+            "series-name": "SPURS-2 Drifter data for the E. Tropical Pacific field campaign",
             "spatial": "-179.999 -10.074 -124.78 32.283",
+            "temporal": "2016-06-20T05:57:00Z/2019-03-14T12:04:00Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 Drifter data for the E. Tropical Pacific field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-S-IRIS-3-RDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The data set contains measurements from both the infrared interferometer spectrometer and the broadband reflected solar radiometer and ancillary data. The data set is ordered by time as measured by the Flight Data System Count (FDSC). This represents the data frame number, modulo 60. Also included is pointing and other information on the geometry associated with a given data record.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-s-iris-3-rdr-v1.0_q57i-h5ch",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "comet sl9/jupiter collision",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-S-IRIS-3-RDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-s-iris-3-rdr-v1.0_q57i-h5ch",
-            "description": "The data set contains measurements from both the infrared interferometer spectrometer and the broadband reflected solar radiometer and ancillary data. The data set is ordered by time as measured by the Flight Data System Count (FDSC). This represents the data frame number, modulo 60. Also included is pointing and other information on the geometry associated with a given data record.",
-            "title": "VG1/VG2 SATURN IRIS 3 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1/VG2 SATURN IRIS 3 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0669-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-24T10:08:30.000 to 2015-03-24T12:21:25.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0669-v1.0_q598-s6sf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0669-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0669-v1.0_q598-s6sf",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-24T10:08:30.000 to 2015-03-24T12:21:25.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0669 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0669 V1.0"
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
-                "flow",
-                "cases",
-                "compressible",
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
-            "identifier": "NASA-843__16",
             "description": "This grouping contains the compressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Compressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1224109,111 +1224087,109 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-843__16",
+            "issued": "2018-06-25",
+            "keyword": [
+                "flow",
+                "cases",
+                "compressible",
+                "models",
+                "turbulence"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP1-0002-V1.0",
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
-                "unknown",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Commissioning measurement covering the time 2004-03-27T21:51:39.500 to 2004-03-28T07:17:42.950.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp1-0002-v1.0_q5b5-dtzs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "unknown",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP1-0002-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp1-0002-v1.0_q5b5-dtzs",
-            "description": "This is a Commissioning measurement covering the time 2004-03-27T21:51:39.500 to 2004-03-28T07:17:42.950.",
-            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 1 0002 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 1 0002 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1354",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Walker, D.A. 2018. Arctic Vegetation Plots at Happy Valley, Alaska, 1994. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1354",
-            "issued": "2018-12-31",
-            "temporal": "1994-07-18T00:00:00Z/1994-07-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "biosphere",
-                "soils",
-                "vegetation",
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
-            "identifier": "C2170968750-ORNL_CLOUD",
             "description": "This dataset provides environmental, soil, and vegetation data collected in July 1994 from 56 study plots at the Happy Valley research site, located along the Sagavanirktok River in a glaciated valley of the northern Arctic Foothills of the Brooks Range. Data includes the baseline plot information for vegetation, soils, and site factors for the study plots subjectively located in 17 plant communities that occur in 5 broad habitat types across the glaciated landscape. Specific attributes include: dominant vegetation species, cover, indices, and biomass pools, soil chemistry, physical characteristics, moisture, and organic matter. This product brings together for easy reference all the available information collected from the plots that has been used for the classification, mapping, and analysis of geo-botanical factors in the Happy Valley region and across Alaska.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Arctic Vegetation Plots at Happy Valley, Alaska, 1994",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Happy_Valley_Veg_Plots_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1354",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1354",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Happy_Valley_Veg_Plots/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Happy_Valley_Veg_Plots/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Happy_Valley_Veg_Plots.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Happy_Valley_Veg_Plots.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1354",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1354",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -1224247,74 +1224223,72 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Happy_Valley_Veg_Plots_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Happy_Valley_Veg_Plots_Fig1.png",
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
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Happy_Valley_Veg_Plots_Fig1.png",
+            "identifier": "C2170968750-ORNL_CLOUD",
+            "issued": "2018-12-31",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "biosphere",
+                "soils",
+                "vegetation",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1354",
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
             "spatial": "-148.87 69.12 -148.82 69.17",
+            "temporal": "1994-07-18T00:00:00Z/1994-07-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic Vegetation Plots at Happy Valley, Alaska, 1994"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAR/DATA102",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2018-09-20. CAR_DISCOVERAQ_L1C. Version 1. CAR Discover AQ Air Quality L1 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/CAR/DATA102. https://disc.gsfc.nasa.gov/datacollection/CAR_DISCOVERAQ_L1C_1.html.",
-            "issued": "2017-12-02",
-            "temporal": "2014-07-08T00:00:00Z/2014-08-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-02",
-            "keyword": [
-                "aerosols",
-                "atmospheric radiation",
-                "land surface",
-                "clouds",
-                "surface radiative properties",
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
-            "identifier": "C1442068291-GES_DISC",
-            "description": "DISCOVER-AQ, a NASA Earth Venture program funded mission, stands for Deriving Information on Surface Conditions from Column and Vertically Resolved Observations Relevant to Air Quality.\nIn recent years, progress in reaching air quality goals has begun to plateau for many locations. Furthermore, near-surface pollution is one of the most challenging problems for Earth observations from space. However, with an improved ability to monitor pollution from satellites from DISCOVER-AQ, scientists could make better air quality forecasts, more accurately determine the sources of pollutants in the air and more closely determine the fluctuations in emissions levels. In short, the more accurate data scientists have at hand, the better society is able to deal effectively with lingering pollution problems.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_DISCOVERAQ_L1C",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR Discover AQ Air Quality L1 V1 (CAR_DISCOVERAQ_L1C) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_DISCOVERAQ_L1C_1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "DISCOVER-AQ, a NASA Earth Venture program funded mission, stands for Deriving Information on Surface Conditions from Column and Vertically Resolved Observations Relevant to Air Quality.\nIn recent years, progress in reaching air quality goals has begun to plateau for many locations. Furthermore, near-surface pollution is one of the most challenging problems for Earth observations from space. However, with an improved ability to monitor pollution from satellites from DISCOVER-AQ, scientists could make better air quality forecasts, more accurately determine the sources of pollutants in the air and more closely determine the fluctuations in emissions levels. In short, the more accurate data scientists have at hand, the better society is able to deal effectively with lingering pollution problems.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAR%2FDATA102",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAR%2FDATA102",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1224324,692 +1224298,727 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_DISCOVERAQ_L1C_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_DISCOVERAQ_L1C_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_DISCOVERAQ_L1C.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_DISCOVERAQ_L1C.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CAR/CAR_DISCOVERAQ_L1C.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CAR/CAR_DISCOVERAQ_L1C.1/contents.html",
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
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_DISCOVERAQ_L1C.1/doc/CAR_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_DISCOVERAQ_L1C.1/doc/CAR_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_DISCOVERAQ_L1C_1.jpg",
+            "identifier": "C1442068291-GES_DISC",
+            "issued": "2017-12-02",
+            "keyword": [
+                "aerosols",
+                "atmospheric radiation",
+                "land surface",
+                "clouds",
+                "surface radiative properties",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAR/DATA102",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CAR_DISCOVERAQ_L1C",
             "spatial": "-105.247 37.1656 -75.0814 42.0232",
+            "temporal": "2014-07-08T00:00:00Z/2014-08-12T23:59:59.999Z",
             "theme": [
                 "CAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAR Discover AQ Air Quality L1 V1 (CAR_DISCOVERAQ_L1C) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1797",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fiore, N., S. Pedron, M. Tayo, C.I. Czimczik, and M.L. Goulden. 2021. NDVI, Species Cover, and LAI, Burned and Unburned sites, Interior Alaska, 2017-2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1797",
-            "issued": "2021-10-28",
-            "temporal": "2017-08-29T00:00:00Z/2018-08-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "ecosystems",
-                "ngda",
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
-            "identifier": "C2162189202-ORNL_CLOUD",
             "description": "This dataset provides leaf area index (LAI), tree species and canopy cover, normalized difference vegetation index (NDVI), and NDVI trends for boreal forests in interior Alaska, U.S. These data were collected to investigate NDVI trends with forest structure and composition as influenced by disturbance and succession. The data are from 102 sites surveyed in 2017 and 2018 and include locations with and without a fire since 1940. A time series of NDVI was developed from Landsat (1999-2018) to measure NDVI trends. The field data cover the period 2017-08-29 to 2018-08-20. The surveyed forest stands spanned a distance of over 425 km across interior Alaska. The sites were selected before visiting the field to include locations with and without a fire since 1940. Recently burned sites were selected to span a range of years since fire, while sites without a recent fire were selected to include a range of Landsat NDVI trends. For each year, the median NDVI during the growing season was calculated. Then, a simple linear regression trend was calculated for years 1999-2018.",
-            "graphic-preview-description": "Locations of boreal forest stands in interior Alaska where forest structure and composition were measured and compared to remotely-sensed NDVI trends (Fiore et al., 2020). The locations are available as a companion file. Source: Google Earth",
-            "title": "NDVI, Species Cover, and LAI, Burned and Unburned sites, Interior Alaska, 2017-2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/NDVI_Forest_Structure_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1797",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1797",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/NDVI_Forest_Structure/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/NDVI_Forest_Structure/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/NDVI_Forest_Structure.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/NDVI_Forest_Structure.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1797",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1797",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/NDVI_Forest_Structure/comp/NDVI_Forest_Structure.pdf",
-                    "description": "NDVI, Species Cover, and LAI, Burned and Unburned sites, Interior Alaska, 2017-2018: NDVI_Forest_Structure.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "NDVI, Species Cover, and LAI, Burned and Unburned sites, Interior Alaska, 2017-2018: NDVI_Forest_Structure.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/NDVI_Forest_Structure/comp/NDVI_Forest_Structure.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/NDVI_Forest_Structure/comp/survey_sites.kml",
-                    "description": "NDVI, Species Cover, and LAI, Burned and Unburned sites, Interior Alaska, 2017-2018: survey_sites.kml",
                     "@type": "dcat:Distribution",
+                    "description": "NDVI, Species Cover, and LAI, Burned and Unburned sites, Interior Alaska, 2017-2018: survey_sites.kml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/NDVI_Forest_Structure/comp/survey_sites.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/NDVI_Forest_Structure_Fig1.jpg",
-                    "description": "Locations of boreal forest stands in interior Alaska where forest structure and composition were measured and compared to remotely-sensed NDVI trends (Fiore et al., 2020). The locations are available as a companion file. Source: Google Earth",
                     "@type": "dcat:Distribution",
+                    "description": "Locations of boreal forest stands in interior Alaska where forest structure and composition were measured and compared to remotely-sensed NDVI trends (Fiore et al., 2020). The locations are available as a companion file. Source: Google Earth",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/NDVI_Forest_Structure_Fig1.jpg",
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
+            "graphic-preview-description": "Locations of boreal forest stands in interior Alaska where forest structure and composition were measured and compared to remotely-sensed NDVI trends (Fiore et al., 2020). The locations are available as a companion file. Source: Google Earth",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/NDVI_Forest_Structure_Fig1.jpg",
+            "identifier": "C2162189202-ORNL_CLOUD",
+            "issued": "2021-10-28",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "ecosystems",
+                "ngda",
+                "vegetation",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1797",
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
             "spatial": "-149.96 63.82 -144.96 65.96",
+            "temporal": "2017-08-29T00:00:00Z/2018-08-20T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NDVI, Species Cover, and LAI, Burned and Unburned sites, Interior Alaska, 2017-2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MODST-MO4N9",
             "citation": "NASA OBPG. 2020-01-15. MODIS Terra Level 3 SST Thermal IR Monthly 4km Nighttime. Version 2019.0. MODIS Terra Global Level 3 Mapped SST. OBPG, Goddard Space Flight Center  Greenbelt, MD,US. Archived by National Aeronautics and Space Administration, U.S. Government, OBPG. https://doi.org/10.5067/MODST-MO4N9. https://podaac-tools.jpl.nasa.gov/drive/files/allData/modis/L3/docs/modis_sst.html. NASA OBPG, OBPG, 2020-01-15, MODIS Terra Level 3 SST Thermal IR Monthly 4km Nighttime V2019.0, https://podaac-tools.jpl.nasa.gov/drive/files/allData/modis/L3/docs/modis_sst.html.",
-            "issued": "2019-12-14",
-            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-14",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2015.04.023",
-                "https://doi.org/10.1175/JTECH-D-18-0103.1"
-            ],
-            "keyword": [
-                "earth science",
-                "ocean temperature",
-                "oceans",
-                "ngda",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036882337-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "Day and night spatially gridded global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODST-MO4N4",
-            "release-place": "OBPG, Goddard Space Flight Center  Greenbelt, MD,US",
-            "series-name": "MODIS Terra Level 3 SST Thermal IR Monthly 4km Nighttime",
             "creator": "NASA OBPG",
-            "title": "MODIS Terra Level 3 SST Thermal IR Monthly 4km Nighttime V2019.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V2019.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Day and night spatially gridded global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODST-MO4N4",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODST-MO4N9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODST-MO4N9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V2019.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V2019.0.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882337-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882337-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882337-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882337-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V2019.0.jpg",
+            "identifier": "C2036882337-POCLOUD",
+            "issued": "2019-12-14",
+            "keyword": [
+                "earth science",
+                "ocean temperature",
+                "oceans",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODST-MO4N9",
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
+            "series-name": "MODIS Terra Level 3 SST Thermal IR Monthly 4km Nighttime",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "EOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS Terra Level 3 SST Thermal IR Monthly 4km Nighttime V2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-PEPSSI-3-JUPITER-V1.1",
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
-                "solar wind"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-pepssi-3-jupiter-v1.1_q5fe-yev9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-PEPSSI-3-JUPITER-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-pepssi-3-jupiter-v1.1_q5fe-yev9",
-            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS PEPSSI JUPITER ENCOUNTER V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS PEPSSI JUPITER ENCOUNTER V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD10CM.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS/Terra Snow Cover Monthly L3 Global 0.05Deg CMG V061. Version 61. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD10CM.061.",
-            "issued": "2000-03-01",
-            "temporal": "2000-03-01T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-31",
-            "keyword": [
-                "national geospatial data asset",
-                "cryosphere",
-                "earth science",
-                "snow/ice",
-                "ngda"
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
-            "identifier": "C1646609754-NSIDC_ECS",
             "description": "This global Level-3 (L3) data set provides monthly mean snow cover extent within 0.05\u00b0 (approx. 5 km) MODIS Climate Modeling Grid (CMG) cells. This data set is derived from snow cover observations in the 'MODIS/Terra Snow Cover Daily L3 Global 0.05Deg CMG\u2019 data set (DOI:10.5067/MODIS/MOD10C1.061).\n\nThe terms \"Version 61\" and \"Collection 6.1\" are used interchangeably in reference to this release of MODIS data.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "MODIS/Terra Snow Cover Monthly L3 Global 0.05Deg CMG V061",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-224,-103,170,79&l=MODIS_Terra_L3_Snow_Cover_Monthly_Average_Pct,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2000-03-01",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD10CM.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD10CM.061",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOST/MOD10CM.061",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOST/MOD10CM.061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD10CM+V061",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD10CM+V061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/MOD10CM/versions/61/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/MOD10CM/versions/61/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-224%2C-103%2C170%2C79&l=MODIS_Terra_L3_Snow_Cover_Monthly_Average_Pct%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2000-03-01",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-224%2C-103%2C170%2C79&l=MODIS_Terra_L3_Snow_Cover_Monthly_Average_Pct%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2000-03-01",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10CM.061",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10CM.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10CM.061",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10CM.061",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-224,-103,170,79&l=MODIS_Terra_L3_Snow_Cover_Monthly_Average_Pct,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2000-03-01",
+            "identifier": "C1646609754-NSIDC_ECS",
+            "issued": "2000-03-01",
+            "keyword": [
+                "national geospatial data asset",
+                "cryosphere",
+                "earth science",
+                "snow/ice",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD10CM.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-01T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Snow Cover Monthly L3 Global 0.05Deg CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-CR4B-PC9-V3.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCRUISE 4-2 mission phase. This release supersedes version 1.0. Version 2.0 was never generated\nfor pre-comet phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-cr4b-pc9-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-CR4B-PC9-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-cr4b-pc9-v3.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCRUISE 4-2 mission phase. This release supersedes version 1.0. Version 2.0 was never generated\nfor pre-comet phases.",
-            "title": "ROSETTA-ORBITER CHECK MIDAS 3 CR4B PC9 V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK MIDAS 3 CR4B PC9 V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M01-V3.0",
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
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m01-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M01-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m01-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 3 PRL-MTP001 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 3 PRL-MTP001 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-09-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1.",
-            "issued": "2021-03-19",
-            "temporal": "2013-08-01T00:00:00Z/2013-09-23T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-20",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "aerosols",
-                "earth science"
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
-            "identifier": "C2119341663-LARC_ASDC",
             "description": "SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data are remotely sensed data collected by the Research Scanning Polarimeter (RSP) onboard the ER-2 aircraft during the Studies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEA4CRS) airborne field study. Data collection for this product is complete.\r\n\r\nStudies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEAC4RS) airborne field study was conducted in August and September of 2013. The field operation was based in Houston, Texas. The primary SEAC4RS science objectives are: to determine how pollutant emissions are redistributed via deep convection throughout the troposphere; to determine the evolution of gases and aerosols in deep convective outflow and the implications for UT/LS chemistry; to identify the influences and feedbacks of aerosol particles from anthropogenic pollution and biomass burning on meteorology and climate through changes in the atmospheric heat budget (i.e., semi-direct effect) or through microphysical changes in clouds (i.e., indirect effects); and lastly, to serve as a calibration and validation test bed for future satellite instruments and missions.\r\n\r\nThe airborne observational data were collected from three aircraft platforms: the NASA DC-8, ER-2, and SPEC LearJet. Both the NASA DC-8 and ER-2 aircraft were instrumented for comprehensive in-situ and remote sensing measurements of the trace gas, aerosol properties, and cloud properties. In addition, radiative fluxes and meteorological parameters were also recorded. The NASA DC-8 was mostly responsible for tropospheric sampling, while the NASA ER-2 was operating in the lower stratospheric regime. The SPEC LearJet was dedicated to in-situ cloud characterizations. To accomplish the science objectives, the flight plans were designed to investigate the influence of biomass burning and pollution, their temporal evolution, and ultimately, impacts on meteorological processes which can, in turn, feedback on regional air quality. With respect to meteorological feedbacks, the opportunity to examine the impact of polluting aerosols on cloud properties and dynamics was of particular interest.",
-            "title": "SEAC4RS ER-2 Aircraft Remotely Sensed Research Scanning Polarimeter Aerosol and Cloud Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
-                    "description": "DOI data set landing page for SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341663-LARC_ASDC",
-                    "description": "Earthdata Search for SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341663-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/AircraftRemoteSensing_RSP_ER2_Data_1/",
-                    "description": "ASDC Direct Data Download for SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/AircraftRemoteSensing_RSP_ER2_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SEAC4RS/AircraftRemoteSensing_RSP_ER2_Data_1/contents.html",
-                    "description": "OPeNDAP data access for SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SEAC4RS/AircraftRemoteSensing_RSP_ER2_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2119341663-LARC_ASDC",
+            "issued": "2021-03-19",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "aerosols",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_AircraftRemoteSensing_RSP_ER2_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>15.0 -128.0 15.0 -82.0 53.0 -82.0 53.0 -128.0 15.0 -128.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-08-01T00:00:00Z/2013-09-23T23:59:59.999Z",
             "theme": [
                 "SEAC4RS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEAC4RS ER-2 Aircraft Remotely Sensed Research Scanning Polarimeter Aerosol and Cloud Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/doi:10.5067/VIIRS/VJ114_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCE MODIS. 2024-03-05. VIIRS/JPSS1 Thermal Anomalies/Fire 6-Min L2 Swath 750m NRT. Version 2. NASA GSFC LANCE. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/doi:10.5067/VIIRS/VJ114_NRT.002. https://doi.org/10.5067/VIIRS/VJ114_NRT.002.",
-            "issued": "2024-03-05",
-            "temporal": "2024-03-05T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-07",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2013.12.008"
-            ],
-            "keyword": [
-                "ecological dynamics",
-                "land surface",
-                "surface radiative properties",
-                "surface thermal properties",
-                "earth science",
-                "biosphere"
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
-            "identifier": "C2888590350-LANCEMODIS",
-            "description": "The VIIRS/JPSS1 Thermal Anomalies/Fire 6-Min L2 Swath 750m NRT product, short-name VJ114_NRT is based on the MODIS Fire algorithm. The input to the Active Fires production are Level-1B moderate-resolution reflective band M7, and emissive bands M13 and M15. The fire algorithm first calculates bands M13, M15 brightness temperature (BT) statistics for a group of background pixels adjacent to each potential fire pixel. These statistics are used to set thresholds for several contextual fire detection tests. There is also an absolute fire detection test based on a pre-set M13 BT threshold. If the results of the absolute and relative fire detection tests meet certain criteria, the pixel is labeled as fire. The designation of a pixel as fire from the results of the BT threshold tests may be overridden under sun glint conditions or if too few pixels were used to calculate the background statistics.\r\n\r\nThe VJ114_NRT product contains several pieces of information for each fire pixel: pixel coordinates, latitude and longitude, pixel M7 reflectance, background M7 reflectance, pixel M13 and M15 BT, background M13 and M15 BT, mean background BT difference, background M13, M15, and BT difference mean absolute deviation, fire radiative power, number of adjacent cloud pixels, number of adjacent water pixels, background window size, number of valid background pixels, detection confidence, land pixel flag, background M7 reflectance, and reflectance mean absolute deviation.\r\n\r\nThe product provides day and nighttime active fire detection over land and water (from gas flares). The VJ114 product provides fire data continuity with NASA's EOS MODIS 1 km fire product. \r\n\r\nFor more information visit University of Maryland VIIRS Active Fire Web page at http://viirsfire.geog.umd.edu/",
-            "release-place": "NASA GSFC LANCE",
             "creator": "LANCE MODIS",
-            "title": "VIIRS/JPSS1 Thermal Anomalies/Fire 6-Min L2 Swath 750m NRT - V2",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/JPSS1 Thermal Anomalies/Fire 6-Min L2 Swath 750m NRT product, short-name VJ114_NRT is based on the MODIS Fire algorithm. The input to the Active Fires production are Level-1B moderate-resolution reflective band M7, and emissive bands M13 and M15. The fire algorithm first calculates bands M13, M15 brightness temperature (BT) statistics for a group of background pixels adjacent to each potential fire pixel. These statistics are used to set thresholds for several contextual fire detection tests. There is also an absolute fire detection test based on a pre-set M13 BT threshold. If the results of the absolute and relative fire detection tests meet certain criteria, the pixel is labeled as fire. The designation of a pixel as fire from the results of the BT threshold tests may be overridden under sun glint conditions or if too few pixels were used to calculate the background statistics.\r\n\r\nThe VJ114_NRT product contains several pieces of information for each fire pixel: pixel coordinates, latitude and longitude, pixel M7 reflectance, background M7 reflectance, pixel M13 and M15 BT, background M13 and M15 BT, mean background BT difference, background M13, M15, and BT difference mean absolute deviation, fire radiative power, number of adjacent cloud pixels, number of adjacent water pixels, background window size, number of valid background pixels, detection confidence, land pixel flag, background M7 reflectance, and reflectance mean absolute deviation.\r\n\r\nThe product provides day and nighttime active fire detection over land and water (from gas flares). The VJ114 product provides fire data continuity with NASA's EOS MODIS 1 km fire product. \r\n\r\nFor more information visit University of Maryland VIIRS Active Fire Web page at http://viirsfire.geog.umd.edu/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ114_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ114_NRT.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/5200/VJ114_NRT/",
-                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
                     "@type": "dcat:Distribution",
+                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/5200/VJ114_NRT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
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
                 }
             ],
+            "identifier": "C2888590350-LANCEMODIS",
+            "issued": "2024-03-05",
+            "keyword": [
+                "ecological dynamics",
+                "land surface",
+                "surface radiative properties",
+                "surface thermal properties",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/doi:10.5067/VIIRS/VJ114_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.rse.2013.12.008"
+            ],
+            "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "2024-03-05T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "LANCE",
                 "FIRMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Thermal Anomalies/Fire 6-Min L2 Swath 750m NRT - V2"
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
+            "description": "CAPS, CDA, INMS, ISS, MAG, MIMI, RPWS, RSS, SPICE, UVIS, VIMS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20111006.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-526",
+            "issued": "2018-06-25",
             "keyword": [
                 "cda",
                 "caps",
@@ -1225024,45 +1225033,38 @@
                 "iss",
                 "inms"
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
-            "identifier": "NASA-526",
-            "description": "CAPS, CDA, INMS, ISS, MAG, MIMI, RPWS, RSS, SPICE, UVIS, VIMS",
-            "title": "PDS Cassini Data Release 27",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20111006.shtml",
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
+            "title": "PDS Cassini Data Release 27"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-MAG-3-RDR-MAGSPHERIC-SURVEY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains magnetic field vectors acquired by the Galileo Orbiter magnetometer during the magnetospheric survey portion of the mission. These data were acquired in the optimal averager (opt/avg) and real-time survey (RTS) modes beginning during the Jupiter approach and continuing throughout Jupiter orbital operations. The data set covers the time period from 1995-11-06T00:21:30 UT (Jupiter approach) until the end of mission (September 2003). Sampling rates are variable and depended upon the downlink capabilities. With few exceptions, the data are provided at the full downlink resolution. The data are provided in five coordinate systems (IRC, System III [1965], JSE, JSO, and JSM).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-mag-3-rdr-magspheric-survey-v1.0_q5qr-538j",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "io plasma torus",
@@ -1225073,142 +1225075,116 @@
                 "callisto",
                 "amalthea"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-MAG-3-RDR-MAGSPHERIC-SURVEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-mag-3-rdr-magspheric-survey-v1.0_q5qr-538j",
-            "description": "This data set contains magnetic field vectors acquired by the Galileo Orbiter magnetometer during the magnetospheric survey portion of the mission. These data were acquired in the optimal averager (opt/avg) and real-time survey (RTS) modes beginning during the Jupiter approach and continuing throughout Jupiter orbital operations. The data set covers the time period from 1995-11-06T00:21:30 UT (Jupiter approach) until the end of mission (September 2003). Sampling rates are variable and depended upon the downlink capabilities. With few exceptions, the data are provided at the full downlink resolution. The data are provided in five coordinate systems (IRC, System III [1965], JSE, JSO, and JSM).",
-            "title": "GO JUPITER MAG MAGNETOSPHERIC SURVEY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GO JUPITER MAG MAGNETOSPHERIC SURVEY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675299-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2023-04-04",
-            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
-            "keyword": [
-                "oceans",
-                "biosphere",
-                "earth science",
-                "ecosystems",
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
-            "identifier": "C2652675299-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-21 VIIRS Regional Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/NOAA21-VIIRS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/NOAA21-VIIRS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L2/IOP/2022",
-                    "description": "VIIRS-NOAA-21 L2 Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L2 Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L2/IOP/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2652675299-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "oceans",
+                "biosphere",
+                "earth science",
+                "ecosystems",
+                "ocean optics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675299-OB_DAAC.html",
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
+            "title": "NOAA-21 VIIRS Regional Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1685783979-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2020-03-17. OCO2_L1aIn_Sample. Version 10. OCO-2 Level 1A collated, parsed, science or calibration data V10. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Sample_10.html. Digital Science Data.",
-            "issued": "2020-01-17",
-            "temporal": "2019-11-30T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-17",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1685783979-GES_DISC",
-            "description": "Version 10 is the current version of the data set. Older versions will no longer be available and are superseded by Version 10.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Sample Mode of operation.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L1aIn_Sample",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 1A collated, parsed, science or calibration data V10 (OCO2_L1aIn_Sample) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 10 is the current version of the data set. Older versions will no longer be available and are superseded by Version 10.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Sample Mode of operation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1225217,270 +1225193,274 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Sample_10.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Sample_10.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Sample.10/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Sample.10/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Sample.10/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Sample.10/",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
+            "identifier": "C1685783979-GES_DISC",
+            "issued": "2020-01-17",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1685783979-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-01-17",
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
+            "temporal": "2019-11-30T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 1A collated, parsed, science or calibration data V10 (OCO2_L1aIn_Sample) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD09CMG.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eric Vermote. 2021-02-02. MODIS/Terra Surface Reflectance Daily L3 Global 0.05Deg CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD09CMG.061. https://doi.org/10.5067/MODIS/MOD09CMG.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-02",
-            "temporal": "2000-02-24T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-02",
-            "keyword": [
-                "national geospatial data asset",
-                "surface radiative properties",
-                "land surface",
-                "ngda",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Vermote",
                 "hasEmail": "mailto:eric.f.vermote@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2565788876-LPCLOUD",
-            "description": "The MOD09CMG Version 6.1 product provides an estimate of the surface spectral reflectance of Terra Moderate Resolution Imaging Spectroradiometer (MODIS) Bands 1 through 7, resampled to 5600 meter (m) pixel resolution and corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. The MOD09CMG data product provides 25 layers including MODIS bands 1 through 7; Brightness Temperature data from thermal bands 20, 21, 31, and 32; along with Quality Assurance (QA) and observation bands. This product is based on a Climate Modeling Grid (CMG) for use in climate simulation models. \n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Reflectance products. Further details regarding MODIS land product validation for the MOD09 data product is available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD09).\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Eric Vermote",
-            "title": "MODIS/Terra Surface Reflectance Daily L3 Global 0.05Deg CMG V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2602479339-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MOD09CMG Version 6.1 product provides an estimate of the surface spectral reflectance of Terra Moderate Resolution Imaging Spectroradiometer (MODIS) Bands 1 through 7, resampled to 5600 meter (m) pixel resolution and corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. The MOD09CMG data product provides 25 layers including MODIS bands 1 through 7; Brightness Temperature data from thermal bands 20, 21, 31, and 32; along with Quality Assurance (QA) and observation bands. This product is based on a Climate Modeling Grid (CMG) for use in climate simulation models. \n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Reflectance products. Further details regarding MODIS land product validation for the MOD09 data product is available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD09).\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09CMG.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09CMG.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD09CMG.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD09CMG.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565788876-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565788876-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD09CMG.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD09CMG.061",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/925/MOD09_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/925/MOD09_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD09CMG",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD09CMG",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 3 has been achieved for all MODIS Surface Reflectance products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for all MODIS Surface Reflectance products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD09",
-                    "description": "Further details regarding MODIS land product validation for the MOD09 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MOD09 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD09",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD09CMG.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD09CMG.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2602479339-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2602479339-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2602479339-LPCLOUD?h=85&w=85",
+            "identifier": "C2565788876-LPCLOUD",
+            "issued": "2021-02-02",
+            "keyword": [
+                "national geospatial data asset",
+                "surface radiative properties",
+                "land surface",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD09CMG.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Surface Reflectance Daily L3 Global 0.05Deg CMG V061"
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
-            "identifier": "NASA-650",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r61)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1225488,120 +1225468,117 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-650",
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
+            "title": "PDS Data Dictionary (1r61)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-MUPUS-3-FSS-V1.0",
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
+            "description": "This archive contains calibrated data from the MUPUS instrument onboard ROSETTA Lander, acquired during the FSS phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the MUPUS experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-mupus-3-fss-v1.0_q5yi-5znm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-MUPUS-3-FSS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-mupus-3-fss-v1.0_q5yi-5znm",
-            "description": "This archive contains calibrated data from the MUPUS instrument onboard ROSETTA Lander, acquired during the FSS phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the MUPUS experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P MUPUS 3 FSS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P MUPUS 3 FSS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-CRT-4-SUMM-FLUX-15MIN-V1.0",
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
-                "pioneer 11",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 11 Cosmic-Ray Telescope (CRT) data from the Jupiter encounter period from 1974-11-26 and 1974-12-09. The data set provides 15.0 minute flux averages from 18 electron, proton, and heavy ion channels.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-crt-4-summ-flux-15min-v1.0_q62j-9aee",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pioneer 11",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-CRT-4-SUMM-FLUX-15MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-crt-4-summ-flux-15min-v1.0_q62j-9aee",
-            "description": "Pioneer 11 Cosmic-Ray Telescope (CRT) data from the Jupiter encounter period from 1974-11-26 and 1974-12-09. The data set provides 15.0 minute flux averages from 18 electron, proton, and heavy ion channels.",
-            "title": "P11 JUPITER CRT ELECTRON/PROTON/ION\n                                      FLUX 15 MIN AVGS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P11 JUPITER CRT ELECTRON/PROTON/ION\n                                      FLUX 15 MIN AVGS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/aces",
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
-                "spacesuit",
-                "suit",
-                "aces",
-                "3d model",
-                "astronaut"
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
-            "identifier": "NASA-304__1",
             "description": "The Advanced Crew Escape Suit (ACES) is a full pressure vessel providing an atmosphere of protection. Polygons: 44656 Vertices: 44684",
-            "title": "NASA 3D Models: Advanced Crew Escape Suit",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1225609,184 +1225586,183 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-304__1",
+            "issued": "2018-06-25",
+            "keyword": [
+                "spacesuit",
+                "suit",
+                "aces",
+                "3d model",
+                "astronaut"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/aces",
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
+            "title": "NASA 3D Models: Advanced Crew Escape Suit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/63",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wrigley, R. C. 1994. Optical Thickness Data: C-130 (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/63",
-            "issued": "2024-05-06",
-            "temporal": "1987-06-04T00:00:00Z/1989-08-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation"
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
-            "identifier": "C2980497351-ORNL_CLOUD",
             "description": "Airborne sun photometer data taken from C-130",
-            "graphic-preview-description": "Browse Image",
-            "title": "Optical Thickness Data: C-130 (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F63",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F63",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_optical_ot_c130/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_optical_ot_c130/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/optical_thick_c130.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/optical_thick_c130.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/63",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/63",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_optical_ot_c130/comp/optical_thick_c130.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_optical_ot_c130/comp/optical_thick_c130.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_optical_ot_c130/comp/ot_c130.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_optical_ot_c130/comp/ot_c130.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_optical_ot_c130/comp/ot_c130.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_optical_ot_c130/comp/ot_c130.tdf",
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
+            "identifier": "C2980497351-ORNL_CLOUD",
+            "issued": "2024-05-06",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/63",
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
+            "temporal": "1987-06-04T00:00:00Z/1989-08-11T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Optical Thickness Data: C-130 (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-CAL-ITS-2-NAV-9P-CRUISE-V1.1",
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
+            "description": "This data set contains raw calibration and test images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the cruise phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the impactor spacecraft. These data were collected from 7 April to 30 April 2005. The comet was not imaged during cruise. In this version 1.1 of the data set, the values for the INTEGRATION_DURATION keyword in the PDS data labels were corrected. This revised data set supersedes version 1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-cal-its-2-nav-9p-cruise-v1.1_q645-6ghh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "deep impact",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-CAL-ITS-2-NAV-9P-CRUISE-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-cal-its-2-nav-9p-cruise-v1.1_q645-6ghh",
-            "description": "This data set contains raw calibration and test images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the cruise phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the impactor spacecraft. These data were collected from 7 April to 30 April 2005. The comet was not imaged during cruise. In this version 1.1 of the data set, the values for the INTEGRATION_DURATION keyword in the PDS data labels were corrected. This revised data set supersedes version 1.0.",
-            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW ITS NAV IMAGES V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW ITS NAV IMAGES V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1332654211-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2007-01-01. TRMM_2A52. TRMM Ground Validation Rain Existence L2 1 month V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_2A52_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1995-08-02T00:00:00Z/2012-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-09",
-            "keyword": [
-                "atmosphere",
-                "spectral/engineering",
-                "earth science",
-                "precipitation",
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
-            "identifier": "C1332654211-GES_DISC",
-            "description": "The TRMM_2A52 product displays the existence of rain in the radar volume scan. 'Existence' is the fraction of the radar FOV which has measurable precipitation. The GV radar FOV is defined as a base scan (i.e., the lowest level sweep).  Each product file has the Existence data of one site (not one radar) for one month. \n\nA key component of the TRMM project is the Ground Validation (GV) effort which consists of collecting data from ground-based radar, rain gauges and disdrometers. The data is quality-controlled, and then validation products are produced for comparison with TRMM satellite products.\n\nThe four primary GV sites are:\n\n+ Darwin, Australia; \n+ Houston, Texas; \n+ Kwajalein, Republic of the Marshall Islands;\n+ Melbourne, Florida. \n\nA significant effort is also being supported at NASA Wallops Flight Facility (WFF) and vicinity to provide high quality, long-term measurements of rain rates (via a network of rain gauges collocated with National Weather Service gauges), as well as drop size distributions (DSD) using a variety of instruments, including impact-type Joss Waldvogel, laser-optical Parsivel, as well as two-dimensional video disdrometers.  DSD measurements are also being collected at Melbourne and Kwajalein using Joss-Waldvogel disdrometers.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_2A52",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Ground Validation Rain Existence L2 1 month V7 (TRMM_2A52) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/TRMM.logo.PNG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The TRMM_2A52 product displays the existence of rain in the radar volume scan. 'Existence' is the fraction of the radar FOV which has measurable precipitation. The GV radar FOV is defined as a base scan (i.e., the lowest level sweep).  Each product file has the Existence data of one site (not one radar) for one month. \n\nA key component of the TRMM project is the Ground Validation (GV) effort which consists of collecting data from ground-based radar, rain gauges and disdrometers. The data is quality-controlled, and then validation products are produced for comparison with TRMM satellite products.\n\nThe four primary GV sites are:\n\n+ Darwin, Australia; \n+ Houston, Texas; \n+ Kwajalein, Republic of the Marshall Islands;\n+ Melbourne, Florida. \n\nA significant effort is also being supported at NASA Wallops Flight Facility (WFF) and vicinity to provide high quality, long-term measurements of rain rates (via a network of rain gauges collocated with National Weather Service gauges), as well as drop size distributions (DSD) using a variety of instruments, including impact-type Joss Waldvogel, laser-optical Parsivel, as well as two-dimensional video disdrometers.  DSD measurements are also being collected at Melbourne and Kwajalein using Joss-Waldvogel disdrometers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1225795,1493 +1225771,1495 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_2A52_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_2A52_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L2/TRMM_2A52.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L2/TRMM_2A52.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_2A52",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_2A52",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://trmm-fc.gsfc.nasa.gov/trmm_gv/",
-                    "description": "TRMM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Project Home Page",
+                    "downloadURL": "https://trmm-fc.gsfc.nasa.gov/trmm_gv/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/ICSVol4.pdf",
-                    "description": "File specification document",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "File specification document",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/ICSVol4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://trmm-fc.gsfc.nasa.gov/",
-                    "description": "TRMM Field Campaign Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Field Campaign Project Page",
+                    "downloadURL": "https://trmm-fc.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "ftp://gpmweb2.pps.eosdis.nasa.gov/tsdis/AB/docs/anomalous.html",
-                    "description": "TRMM Data Gaps",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Data Gaps",
+                    "downloadURL": "ftp://gpmweb2.pps.eosdis.nasa.gov/tsdis/AB/docs/anomalous.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/TRMM.logo.PNG",
+            "identifier": "C1332654211-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "atmosphere",
+                "spectral/engineering",
+                "earth science",
+                "precipitation",
+                "radar"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1332654211-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-05-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "TRMM_2A52",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "1995-08-02T00:00:00Z/2012-12-31T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Ground Validation Rain Existence L2 1 month V7 (TRMM_2A52) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-01_L1B-003.01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2010-12-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-01_L1B-003.01. https://asdc.larc.nasa.gov/project/CALIPSO.",
-            "issued": "2007-09-06",
-            "temporal": "2006-06-13T00:00:00Z/2011-11-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-11",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "spectral/engineering",
-                "aerosols",
-                "visible wavelengths",
-                "infrared wavelengths",
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
-            "identifier": "C5862867-LARC_ASDC",
             "description": "CAL_WFC_L1_IIR-ValStage1-V3-01 data are Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) Wide Field Camera (WFC) Level 1B 1 km Registered Science data, Validated Stage 1 Version 3-01. Data collection for this product is complete. Version 3.01 includes new metadata parameters and corrections to several minor software bugs. Specifically, the Orbit Number and Path Number metadata parameters are now included to facilitate improved subsetting capabilities. The primary WFC Level 1B data products are calibrated radiance and bidirectional reflectance registered to an Earth-based grid centered on the Lidar ground track. During the normal operation, the WFC acquires science data only during the daylight portions of the CALIPSO orbits. The WFC Level 1B 1 Imaging Infrared Radiometer (IIR) Registered Science grid provides WFC data on the identical grid as the CALIPSO IIR data and is produced to facilitate the use of the WFC data in the IIR retrievals. Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite is comprised of three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), IIR, and WFC. CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Wide Field Camera Level 1B 1 km Registered Science data, Validated Stage 1 V3-01",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWFC%2FCALIPSO%2FCAL_WFC_L1_IIR-VALSTAGE1-V3-01_L1B-003.01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWFC%2FCALIPSO%2FCAL_WFC_L1_IIR-VALSTAGE1-V3-01_L1B-003.01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-01_L1B-003.01",
-                    "description": "DOI data set landing page for CAL_WFC_L1_IIR-ValStage1-V3-01_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_WFC_L1_IIR-ValStage1-V3-01_V3-01",
+                    "downloadURL": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-01_L1B-003.01",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C5862867-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_WFC_L1_IIR-ValStage1-V3-01_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_WFC_L1_IIR-ValStage1-V3-01_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C5862867-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/WFC_L1_IIR-ValStage1-V3-01/contents.html",
-                    "description": "OPeNDAP data access for CAL_WFC_L1_IIR-ValStage1-V3-01_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_WFC_L1_IIR-ValStage1-V3-01_V3-01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/WFC_L1_IIR-ValStage1-V3-01/contents.html",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/quality_summaries/WFC_L1BScansProducts_3-01.pdf",
-                    "description": "CALIPSO Quality Statement: Wide Field Camera Level 1B Scans Data Release Versions: 3.01, 3.02",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Quality Statement: Wide Field Camera Level 1B Scans Data Release Versions: 3.01, 3.02",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/quality_summaries/WFC_L1BScansProducts_3-01.pdf",
+                    "mediaType": "application/pdf",
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
-                    "description": "CALIPSO Tilt Mode Geometry Anomaly Anomalies",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Tilt Mode Geometry Anomaly Anomalies",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/WFC_L1_IIR-ValStage1-V3-01/",
-                    "description": "ASDC Direct Data Download for CAL_WFC_L1_IIR-ValStage1-V3-01_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_WFC_L1_IIR-ValStage1-V3-01_V3-01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/WFC_L1_IIR-ValStage1-V3-01/",
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
+            "identifier": "C5862867-LARC_ASDC",
+            "issued": "2007-09-06",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "spectral/engineering",
+                "aerosols",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-01_L1B-003.01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-06-13T00:00:00Z/2011-11-01T23:59:59Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Wide Field Camera Level 1B 1 km Registered Science data, Validated Stage 1 V3-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1269-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-19T17:50:40.000 to 2015-12-20T01:19:34.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1269-v1.0_q66j-wtxr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1269-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1269-v1.0_q66j-wtxr",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-19T17:50:40.000 to 2015-12-20T01:19:34.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1269 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1269 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-ICI-3-RDR-GIACOBINI-ZIN-V1.0",
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
-                "international cometary explorer",
-                "giacobini-zinner"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Mass spectrometric measurements of ions in the coma of comet Giacobini-Zinner made during the encounter of the International Cometary Explorer (ICE) on 11 September 1985, when the spacecraft passed within 7800 km of the nucleus on its antisunward side.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-ici-3-rdr-giacobini-zin-v1.0_q66s-4qah",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international cometary explorer",
+                "giacobini-zinner"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-ICI-3-RDR-GIACOBINI-ZIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-ici-3-rdr-giacobini-zin-v1.0_q66s-4qah",
-            "description": "Mass spectrometric measurements of ions in the coma of comet Giacobini-Zinner made during the encounter of the International Cometary Explorer (ICE) on 11 September 1985, when the spacecraft passed within 7800 km of the nucleus on its antisunward side.",
-            "title": "ARRAY OF ICI COUNTS FOR STEPPED M/Q,V",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ARRAY OF ICI COUNTS FOR STEPPED M/Q,V"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA-20/VIIRS/L1/GEO/2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-20/VIIRS/L1/GEO/2.",
-            "issued": "2022-09-28",
-            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-28",
-            "keyword": [
-                "sensor characteristics",
-                "spectral/engineering",
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
-            "identifier": "C1940926976-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) Geolocation (GEO) Products are data containing terrain corrected solar zenith and azimuth angles, satellite zenith and azimuth angles, as well as latitudes and longitudes for each VIIRS grid point for each of the three VIIRS resolutions. (375m, 750m, and DNB).",
-            "title": "NOAA-20 VIIRS Geolocation Product Data, version 2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-20%2FVIIRS%2FL1%2FGEO%2F2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-20%2FVIIRS%2FL1%2FGEO%2F2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Geo-Location/NOAA20-VIIRS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Geo-Location/NOAA20-VIIRS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-20/VIIRS/L1/GEO/2",
-                    "description": "VIIRS-NOAA-20 L1 Geolocation Product Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-20 L1 Geolocation Product Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-20/VIIRS/L1/GEO/2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1940926976-OB_DAAC",
+            "issued": "2022-09-28",
+            "keyword": [
+                "sensor characteristics",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-20/VIIRS/L1/GEO/2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-28",
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
+            "title": "NOAA-20 VIIRS Geolocation Product Data, version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-2-KEM1-V1.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach field where MU69 was expected to reside during the MU69 encounter on Jan. 1, 2019.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-2-kem1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-2-KEM1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-2-kem1-v1.0",
-            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach field where MU69 was expected to reside during the MU69 encounter on Jan. 1, 2019.",
-            "title": "NEW HORIZONS\n      LORRI KEM1\n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      LORRI KEM1\n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESO3LS_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2015-01-05. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TESO3LS_L2.006. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2013-01-18",
-            "temporal": "2006-01-31T00:00:00Z/2006-05-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality",
-                "earth science"
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
-            "identifier": "C191856330-LARC",
             "description": "TL2O3LS_6 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 O3 Limb Special Observation Version 6 data product. It consists of information for one molecular species for an entire Global Survey or Special Observation. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits. \r\rNadir observations, which point directly to the surface of the Earth are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations\u201d\r\rThe organization of data within the Swath object was based on a superset of the Upper Atmosphere Research Satellite (UARS) pressure levels used to report concentrations of trace atmospheric gases. The reporting grid was the same pressure grid used for modeling. There were 67 reporting levels from 1211.53 hPa, which allowed for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products reported values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files, each observation could potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels were not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresp",
-            "title": "TES/Aura L2 O3 Limb Special Observation V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESO3LS_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESO3LS_L2.006",
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
-                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_products_V006.pdf",
-                    "description": "Aura-TES L2 Products: Version 6 Data Quality Description",
                     "@type": "dcat:Distribution",
+                    "description": "Aura-TES L2 Products: Version 6 Data Quality Description",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_products_V006.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TESDataUsersGuideV6_0_Nov5_2013_FV-dhs.pdf",
-                    "description": "TES Level 2 (L2) Data User\u2019s Guide (Up to & including Version 6 data)",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 2 (L2) Data User\u2019s Guide (Up to & including Version 6 data)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TESDataUsersGuideV6_0_Nov5_2013_FV-dhs.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C191856330-LARC",
-                    "description": "Earthdata Search for TL2O3LS_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2O3LS_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C191856330-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TESO3LS_L2.006",
-                    "description": "DOI data set landing page for TL2O3LS_6",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2O3LS_6",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TESO3LS_L2.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2O3LS.006/contents.html",
-                    "description": "OPeNDAP data access for TL2O3LS_6",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2O3LS_6",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2O3LS.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2O3LS.006/",
-                    "description": "ASDC Direct Data Download for TL2O3LS_6",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2O3LS_6",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2O3LS.006/",
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
-                    "downloadURL": "https://tes.jpl.nasa.gov/science/publications/",
-                    "description": "TES Publications",
                     "@type": "dcat:Distribution",
+                    "description": "TES Publications",
+                    "downloadURL": "https://tes.jpl.nasa.gov/science/publications/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "identifier": "C191856330-LARC",
+            "issued": "2013-01-18",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TESO3LS_L2.006",
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
+            "temporal": "2006-01-31T00:00:00Z/2006-05-20T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L2 O3 Limb Special Observation V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0793-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-19T21:02:05.000 to 2015-05-20T00:35:44.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0793-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0793-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0793-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-19T21:02:05.000 to 2015-05-20T00:35:44.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0793 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0793 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2254303783-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-11-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "ocean optics",
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
-            "identifier": "C2254303783-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Sentinel-3A OLCI Level-2 Regional Earth-observation Full Resolution (EFR) Ocean Color (OC) - Near Realtime Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/S3A-OLCI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/S3A-OLCI/",
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
                 }
             ],
+            "identifier": "C2254303783-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "ocean optics",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2254303783-OB_DAAC.html",
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
+            "temporal": "2016-04-25T00:00:00Z/2024-11-04T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-3A OLCI Level-2 Regional Earth-observation Full Resolution (EFR) Ocean Color (OC) - Near Realtime Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/908",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Saatchi, S.S., R.A. Houghton, D.S. Alves, and B. Nelson. 2009. LBA-ECO LC-15 Amazon Basin Aboveground Live Biomass Distribution Map: 1990-2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/908",
-            "issued": "2023-10-03",
-            "temporal": "1990-01-01T00:00:00Z/2000-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "biosphere",
-                "soils",
-                "vegetation",
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
-            "identifier": "C2768932524-ORNL_CLOUD",
             "description": "This data set provides a single raster image containing the spatial distribution of aboveground live forest biomass of the Amazon basin. This product was derived using a methodology based on a combination of land cover map, remote sensing derived metrics, and more than 500 forest plots distributed over the basin (Saatchi, et al., 2007).The distributed map was produced in ENVI, in Tiff format and it contains forest biomass divided among 11 classes at 1 km spatial resolution with reasonable accuracy (better than 70%). Remote sensing and ground data used in this product were collected from 1990-2000. The Biomass map represents average biomass distribution over the Amazon basin over this period and was used to estimate the total carbon stock of the basin, including the dead and belowground biomass.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-15 Amazon Basin Aboveground Live Biomass Distribution Map: 1990-2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/908_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F908",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F908",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC15_AGLB_Distribution_Map/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC15_AGLB_Distribution_Map/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC15_AGLB.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC15_AGLB.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/908",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/908",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC15_AGLB_Distribution_Map/comp/LC15_AGLB.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC15_AGLB_Distribution_Map/comp/LC15_AGLB.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/908_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/908_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=908",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=908",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/908_1_fit.png",
+            "identifier": "C2768932524-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "biosphere",
+                "soils",
+                "vegetation",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/908",
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
             "spatial": "-82.72 -21.13 -33.57 13.86",
+            "temporal": "1990-01-01T00:00:00Z/2000-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-15 Amazon Basin Aboveground Live Biomass Distribution Map: 1990-2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amess_xrs_raw&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The MESSENGER XRS Raw (EDR) data consist of x-ray spectra and instrument data collected by the XRS instrument during cruise, fly-by and orbital operations at Mercury, along with observations of Venus, and observations taken of Cassiopeia-A for calibration.",
+            "identifier": "urn:nasa:pds:mess_xrs_raw",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "messenger",
                 "earth",
                 "mercury",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amess_xrs_raw&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mess_xrs_raw",
-            "description": "The MESSENGER XRS Raw (EDR) data consist of x-ray spectra and instrument data collected by the XRS instrument during cruise, fly-by and orbital operations at Mercury, along with observations of Venus, and observations taken of Cassiopeia-A for calibration.",
-            "title": "MESSENGER XRS Raw (EDR) Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESSENGER XRS Raw (EDR) Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/0QPQFIXDET1X",
             "citation": "Kevin W. Bowman. 2023-02-28. TRPSDL2ALLCRSMGLOS. Version 1. TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/0QPQFIXDET1X. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGLOS_1.html. Digital Science Data.",
-            "issued": "2023-02-17",
-            "temporal": "2016-01-02T00:00:00Z/2023-03-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-17",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2569838553-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Standard Product contains the vertical distribution of seven retrieved atmospheric gases (CH4, CO, H2O, HDO, NH3, O3 and PAN) and temperature, along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is centered on a 3x3 degree region over Los Angeles for the time period from 2016-01-02 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2ALLCRSMGLOS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Standard Product V1 (TRPSDL2ALLCRSMGLOS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGLOS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0QPQFIXDET1X",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0QPQFIXDET1X",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGLOS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGLOS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGLOS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGLOS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLOS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLOS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGLOS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGLOS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLOS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLOS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLOS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLOS.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGLOS_Sample.png",
+            "identifier": "C2569838553-GES_DISC",
+            "issued": "2023-02-17",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/0QPQFIXDET1X",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-17",
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
+            "series-name": "TRPSDL2ALLCRSMGLOS",
             "spatial": "-120.0 33.0 -117.0 36.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-03-06T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Standard Product V1 (TRPSDL2ALLCRSMGLOS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2G_CLOUD.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Glynn Hulley. 2023-04-25. ECOSTRESS Gridded Cloud Mask Instantaneous L2 Global 70 m v002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L2G_CLOUD.002. https://doi.org/10.5067/ECOSTRESS/ECO_L2G_CLOUD.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2023-04-25",
-            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-25",
-            "keyword": [
-                "atmosphere",
-                "clouds",
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
-            "identifier": "C2076113561-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\nThe ECOSTRESS Gridded Cloud Mask Instantaneous L2 Global 70 m (ECO_L2G_CLOUD) Version 2 data product is derived using a single-channel Bayesian cloud threshold with a look-up-table (LUT) approach. The ECO_L2G_CLOUD product provides a cloud mask that can be used to determine cloud cover for accurate land surface temperature and evapotranspiration estimation. This data product is a gridded version of the ECO_L2_CLOUD Version 2 product that was resampled using nearest neighbor, projected to a globally snapped 0.0006\u00b0 grid, and repackaged as the ECO_L2G_CLOUD Version 2 data product.\r\nThe ECO_L2G_CLOUD Version 2 data product contains two cloud mask layers: cloud confidence and final cloud mask. Information on how to interpret the cloud confidence and cloud mask layers is provided in Table 7 of the ECO_L2_CLOUD Version 2 User Guide. \r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse from Earthdata Search",
             "creator": "Simon Hook, Glynn Hulley",
-            "title": "ECOSTRESS Gridded Cloud Mask Instantaneous L2 Global 70 m V002",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2G_CLOUD.002/ECOv002_L2G_CLOUD_26815_001_20230329T224841_0710_01/ECOv002_L2G_CLOUD_26815_001_20230329T224841_0710_01.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\nThe ECOSTRESS Gridded Cloud Mask Instantaneous L2 Global 70 m (ECO_L2G_CLOUD) Version 2 data product is derived using a single-channel Bayesian cloud threshold with a look-up-table (LUT) approach. The ECO_L2G_CLOUD product provides a cloud mask that can be used to determine cloud cover for accurate land surface temperature and evapotranspiration estimation. This data product is a gridded version of the ECO_L2_CLOUD Version 2 product that was resampled using nearest neighbor, projected to a globally snapped 0.0006\u00b0 grid, and repackaged as the ECO_L2G_CLOUD Version 2 data product.\r\nThe ECO_L2G_CLOUD Version 2 data product contains two cloud mask layers: cloud confidence and final cloud mask. Information on how to interpret the cloud confidence and cloud mask layers is provided in Table 7 of the ECO_L2_CLOUD Version 2 User Guide. \r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2G_CLOUD.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2G_CLOUD.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076113561-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076113561-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2G_CLOUD.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2G_CLOUD.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1655/ECO_L1C-4_Grid_Tile_User_Guide_V2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1655/ECO_L1C-4_Grid_Tile_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1575/ECOL2_ATBD_V2.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1575/ECOL2_ATBD_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2G_CLOUD.002/ECOv002_L2G_CLOUD_26815_001_20230329T224841_0710_01/ECOv002_L2G_CLOUD_26815_001_20230329T224841_0710_01.png",
-                    "description": "Browse from Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse from Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2G_CLOUD.002/ECOv002_L2G_CLOUD_26815_001_20230329T224841_0710_01/ECOv002_L2G_CLOUD_26815_001_20230329T224841_0710_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf",
-                    "description": "The technical information in the ECO_L2_CLOUD User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the ECO_L2_CLOUD User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
-                    "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
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
                 }
             ],
+            "graphic-preview-description": "Browse from Earthdata Search",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2G_CLOUD.002/ECOv002_L2G_CLOUD_26815_001_20230329T224841_0710_01/ECOv002_L2G_CLOUD_26815_001_20230329T224841_0710_01.png",
+            "identifier": "C2076113561-LPCLOUD",
+            "issued": "2023-04-25",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2G_CLOUD.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-25",
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
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Gridded Cloud Mask Instantaneous L2 Global 70 m V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-USPS0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Asher, W., E. Thompson and K. Drushka. 2019-08-15. SPURS-2 research vessel Underway Salinity Profiling System (USPS) data for the E. Tropical Pacific R/V Revelle cruises. Version 1.0. SPURS Field Campaign USPS Products. Applied Physics Laboratory, University of Washington, Seattle, WA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-USPS0. http://podaac.jpl.nasa.gov/SPURS. Asher, W., E. Thompson and K. Drushka, SPURS Data Management PI, Fred Bingham, 2019-08-15, SPURS-2 research vessel Underway Salinity Profiling System (USPS) data for the E. Tropical Pacific R/V Revelle cruises, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-07-22",
-            "temporal": "2016-08-15T00:00:00Z/2017-11-15T23:59:55Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-22",
-            "keyword": [
-                "salinity/density",
-                "ocean temperature",
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
-            "identifier": "C2491772360-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. Underway surface profiling systems (USPS) are automated measurement systems coupled to a research vessels water intake and GPS systems. They provide continuous, along-track surface temperature and salinity measurements at depths of 2, 3 and 5 m using through-hull ports in the bow of the ship. Both SPURS-2 cruises had USPS and associated thermosalinograph (TSG) instrumentation, with measurements calibrated against onboard salinometers. There is one USPS netCDF containing the complete series for each of the 2 cruises.",
-            "release-place": "Applied Physics Laboratory, University of Washington, Seattle, WA, USA",
-            "series-name": "SPURS-2 research vessel Underway Salinity Profiling System (USPS) data for the E. Tropical Pacific R/V Revelle cruises",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Asher, W., E. Thompson and K. Drushka",
-            "title": "SPURS-2 research vessel Underway Salinity Profiling System (USPS) data for the E. Tropical Pacific R/V Revelle cruises",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_USPS.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. Underway surface profiling systems (USPS) are automated measurement systems coupled to a research vessels water intake and GPS systems. They provide continuous, along-track surface temperature and salinity measurements at depths of 2, 3 and 5 m using through-hull ports in the bow of the ship. Both SPURS-2 cruises had USPS and associated thermosalinograph (TSG) instrumentation, with measurements calibrated against onboard salinometers. There is one USPS netCDF containing the complete series for each of the 2 cruises.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-USPS0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-USPS0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_USPS.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_USPS.jpg",
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
-                    "downloadURL": "http://spurs.jpl.nasa.gov/",
-                    "description": "Project Website for SPURS",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for SPURS",
+                    "downloadURL": "http://spurs.jpl.nasa.gov/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772360-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772360-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772360-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772360-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_USPS.jpg",
+            "identifier": "C2491772360-POCLOUD",
+            "issued": "2019-07-22",
+            "keyword": [
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-USPS0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-07-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Applied Physics Laboratory, University of Washington, Seattle, WA, USA",
+            "series-name": "SPURS-2 research vessel Underway Salinity Profiling System (USPS) data for the E. Tropical Pacific R/V Revelle cruises",
             "spatial": "-157.0 5.06 -119.5 25.84",
+            "temporal": "2016-08-15T00:00:00Z/2017-11-15T23:59:55Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 research vessel Underway Salinity Profiling System (USPS) data for the E. Tropical Pacific R/V Revelle cruises"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/9K96YRHCV5A5",
             "citation": "Miyazaki, Kazuyuki. 2024-01-08. TRPSCRAERSO42H2D. Version 1. TROPESS Chemical Reanalysis Surface Aerosol SO4 2-Hourly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/9K96YRHCV5A5. https://disc.gsfc.nasa.gov/datacollection/TRPSCRAERSO42H2D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-17",
-            "references": [
-                "https://doi.org/10.5194/essd-12-2223-2020"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2816184410-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Surface Aerosol SO4 2-Hourly 2-dimensional Product contains the surface concentrations of sulfate aerosol particles. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at 2-hourly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRAERSO42H2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TCR-2 01 April 2005.",
-            "title": "TROPESS Chemical Reanalysis Surface Aerosol SO4 2-Hourly 2-dimensional Product V1 (TRPSCRAERSO42H2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO42H2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9K96YRHCV5A5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9K96YRHCV5A5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO42H2D_Sample.png",
-                    "description": "TCR-2 01 April 2005.",
                     "@type": "dcat:Distribution",
+                    "description": "TCR-2 01 April 2005.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO42H2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRAERSO42H2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRAERSO42H2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRAERSO42H2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRAERSO42H2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRAERSO42H2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRAERSO42H2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_SURFCONCS/TRPSCRAERSO42H2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_SURFCONCS/TRPSCRAERSO42H2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRAERSO42H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRAERSO42H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TCR-2 01 April 2005.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO42H2D_Sample.png",
+            "identifier": "C2816184410-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/9K96YRHCV5A5",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5194/essd-12-2223-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSCRAERSO42H2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Surface Aerosol SO4 2-Hourly 2-dimensional Product V1 (TRPSCRAERSO42H2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC3-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 3 mission phase, which took place between 2015-07-01 and 2015-10-21.  The current V2.0 data set supersedes the previous V1.0 data set with improved documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc3-v2.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC3-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc3-v2.0",
-            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 3 mission phase, which took place between 2015-07-01 and 2015-10-21.  The current V2.0 data set supersedes the previous V1.0 data set with improved documentation.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC3 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC3 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2513",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Froidevaux, L., Livesey, N. and Read, W.. 2020-06-11. ML2HOCL. Version 005. MLS/Aura Level 2 Hypochlorous Acid (HOCl) Mixing Ratio V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2513. https://disc.gsfc.nasa.gov/datacollection/ML2HOCL_005.html. Digital Science Data.",
-            "issued": "2020-02-04",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
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
-            "identifier": "C1729925474-GES_DISC",
-            "description": "ML2HOCL is the EOS Aura Microwave Limb Sounder (MLS) standard product for  hypochlorous acid derived from radiances measured primarily by the 640 GHz radiometer. The data version is 5.0. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 10 to 2.15 hPa, and the vertical resolution is about 6 km. Users of the ML2OHCL data product should read section 3.14 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2HOCL",
             "creator": "Froidevaux, L., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Hypochlorous Acid (HOCl) Mixing Ratio V005 (ML2HOCL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2HOCL_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
```

