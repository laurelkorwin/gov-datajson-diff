# Change History for nasa.json (Part 161)

### Changes from 31606f9 to dd2190f (Part 150/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_L4_Daily_NEE/comp/AirMOSS_L4NEE_ATBD_V2.0_160928.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_L4_Daily_NEE/comp/AirMOSS_L4NEE_ATBD_V2.0_160928.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_L4_Daily_NEE/comp/AirMOSS_L4_Daily_NEE.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_L4_Daily_NEE/comp/AirMOSS_L4_Daily_NEE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1422_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1422_1_fit.png",
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
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1422/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1422/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1422_1_fit.png",
+            "identifier": "C2262413649-ORNL_CLOUD",
+            "issued": "2016-11-22",
+            "keyword": [
+                "land surface",
+                "soils",
+                "biosphere",
+                "ecosystems",
+                "ecological dynamics",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1422",
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
             "spatial": "-122.88 31.49 -68.34 45.79",
+            "temporal": "2012-01-01T00:00:00Z/2014-10-30T23:59:59Z",
             "theme": [
                 "AirMOSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMOSS: L4 Daily Modeled Net Ecosystem Exchange (NEE), AirMOSS sites, 2012-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/643/",
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
-            "identifier": "DASHLINK_643",
             "description": "The following zip files contain individual flight recorded data in Matlab file format. There are 186 parameters each with a data structure that contains the following:\r\n\r\n<pre>\r\n-sensor recordings\r\n-sampling rate\r\n-units\r\n-parameter description\r\n-parameter ID\r\n</pre>",
-            "title": "Flight Data For Tail 665",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_1.zip",
-                    "description": "Tail 665 Set 1",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 665 Set 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_1.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_665_1.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_2.zip",
-                    "description": "Tail 665 Set 2",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 665 Set 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_2.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_665_2.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_3.zip",
-                    "description": "Tail 665 Set 3",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 665 Set 3",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_3.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_665_3.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_4.zip",
-                    "description": "Tail 665 Set 4",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 665 Set 4",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_4.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_665_4.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_5.zip",
-                    "description": "Tail 665 Set 5",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 665 Set 5",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_5.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_665_5.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_6.zip",
-                    "description": "Tail 665 Set 6",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 665 Set 6",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_6.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_665_6.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_7.zip",
-                    "description": "Tail 665 Set 7",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 665 Set 7",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_7.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_665_7.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_8.zip",
-                    "description": "Tail_665 Set 8\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_665 Set 8\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_665_8.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_665_8.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_643",
+            "issued": "2012-12-04",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/643/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Flight Data For Tail 665"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67P-M26-INF-REFL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67p-m26-inf-refl-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67P-M26-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67p-m26-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP026 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP026 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2SUMS_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-03-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2SUMS_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "air quality",
-                "atmosphere",
-                "atmospheric water vapor",
-                "clouds",
-                "surface radiative properties",
-                "earth science",
-                "land surface",
-                "atmospheric pressure",
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
-            "identifier": "C1331182612-LARC",
             "description": "TL2SUMS_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Atmospheric Temperatures Limb Version 7 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. The satellite flew at an altitude of 705 km in an orbit that took it near Earth's North and South Poles. Each orbit, the spacecraft advanced 22\u00b0 westward and, after 233 orbits (16 days) it was back to its starting point. This product contains atmospheric vertical profile estimates, along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, and a priori constraint vectors.",
-            "title": "TES/Aura L2 Summary Profiles Special Observation V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2SUMS_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2SUMS_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182612-LARC",
-                    "description": "Earthdata Search for TL2SUMS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2SUMS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182612-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2SUMS_L2.007",
-                    "description": "DOI data set landing page for TL2SUMS_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2SUMS_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2SUMS_L2.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2SUMS.007/contents.html",
-                    "description": "OPeNDAP data access for TL2SUMS_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2SUMS_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2SUMS.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2SUMS.007/",
-                    "description": "ASDC Direct Data Download for TL2SUMS_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2SUMS_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2SUMS.007/",
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
+            "identifier": "C1331182612-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "air quality",
+                "atmosphere",
+                "atmospheric water vapor",
+                "clouds",
+                "surface radiative properties",
+                "earth science",
+                "land surface",
+                "atmospheric pressure",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2SUMS_L2.007",
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
+            "title": "TES/Aura L2 Summary Profiles Special Observation V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1.",
-            "issued": "2020-07-07",
-            "temporal": "2019-08-15T00:00:00Z/2019-11-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-07-24",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science",
-                "aerosols"
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
-            "identifier": "C1917875750-LARC_ASDC",
             "description": "FIREXAQ_SurfaceMobile_MACH2_InSitu_Data are in-situ measurements collected via the California Air Resources Board (CARB) mobile lab during FIREX-AQ. Data collection for this product is complete.\r\n\r\nCompleted during summer 2019, FIREX-AQ utilized a combination of instrumented airplanes, satellites, and ground-based instrumentation. Detailed fire plume sampling was carried out by the NASA DC-8 aircraft, which had a comprehensive instrument payload capable of measuring over 200 trace gas species, as well as aerosol microphysical, optical, and chemical properties. The DC-8 aircraft completed 23 science flights, including 15 flights from Boise, Idaho and 8 flights from Salina, Kansas. NASA\u2019s ER-2 completed 11 flights, partially in support of the FIREX-AQ effort. The ER-2 payload was made up of 8 satellite analog instruments and provided critical fire information, including fire temperature, fire plume heights, and vegetation/soil albedo information. NOAA provided the NOAA-CHEM Twin Otter and the NOAA-MET Twin Otter aircraft to measure chemical processing in the lofted plumes of Western wildfires. The NOAA-CHEM Twin Otter focused on nighttime plume chemistry, from which data is archived at the NASA Atmospheric Science Data Center (ASDC). The NOAA-MET Twin Otter collected measurements of air movements at fire boundaries with the goal of understanding the local weather impacts of fires and the movement patterns of fires. NOAA-MET Twin Otter data will be archived at the ASDC in the future. Additionally, a ground-based station in McCall, Idaho and several mobile laboratories provided in-situ measurements of aerosol microphysical and optical properties, aerosol chemical compositions, and trace gas species. \r\n\r\nThe Fire Influence on Regional to Global Environments and Air Quality (FIREX-AQ) campaign was a NOAA/NASA interagency intensive study of North American fires to gain an understanding on the integrated impact of the fire emissions on the tropospheric chemistry and composition and to assess the satellite\u2019s capability for detecting fires and estimating fire emissions. The overarching goal of FIREX-AQ was to provide measurements of trace gas and aerosol emissions for wildfires and prescribed fires in great detail, relate them to fuel and fire conditions at the point of emission, characterize the conditions relating to plume rise, and follow plumes downwind to understand chemical transformation and air quality impacts.",
-            "title": "FIREX-AQ California Air Resources Board (CARB) Surface Mobile In-Situ Measurements",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
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
-                    "downloadURL": "https://espo.nasa.gov/firex-aq/",
-                    "description": "ESPO home page for FIREX-AQ",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO home page for FIREX-AQ",
+                    "downloadURL": "https://espo.nasa.gov/firex-aq/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
-                    "description": "DOI data set landing page for FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1917875750-LARC_ASDC",
-                    "description": "Earthdata Search for FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1917875750-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://esrl.noaa.gov/csl/projects/firex-aq/",
-                    "description": "NOAA Chemical Sciences Laboratory (CSL) Overview of FIREX-AQ",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA Chemical Sciences Laboratory (CSL) Overview of FIREX-AQ",
+                    "downloadURL": "https://esrl.noaa.gov/csl/projects/firex-aq/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/whitepaper.pdf",
-                    "description": "FIREX-AQ Mission Overview/White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "FIREX-AQ Mission Overview/White Paper",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/whitepaper.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/DMT_FIREXAQ_v02.pptx",
-                    "description": "Data Management Plan for FIREX-AQ",
                     "@type": "dcat:Distribution",
+                    "description": "Data Management Plan for FIREX-AQ",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/DMT_FIREXAQ_v02.pptx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/FIREX-AQ_ER-2_Instrument_data_archive_pointer.docx",
-                    "description": "ER-2 instrument suite for the Summer 2019 FIREX-AQ field campaign",
                     "@type": "dcat:Distribution",
+                    "description": "ER-2 instrument suite for the Summer 2019 FIREX-AQ field campaign",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/FIREX-AQ_ER-2_Instrument_data_archive_pointer.docx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/",
-                    "description": "FIREX-AQ Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "FIREX-AQ Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/2019/07/30/plumes-go-the-distance/",
-                    "description": "NASA Earth Expeditions Article \u201cPlumes Go The Distance\u201d (July 30, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions Article \u201cPlumes Go The Distance\u201d (July 30, 2019)",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/2019/07/30/plumes-go-the-distance/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/145494/sampling-the-castle-fire/",
-                    "description": "NASA Earth Observatory Article \u201cSampling the Castle Fire\u201d (August 13, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article \u201cSampling the Castle Fire\u201d (August 13, 2019)",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/145494/sampling-the-castle-fire/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/145446/flying-through-a-fire-cloud/",
-                    "description": "NASA Earth Observatory Article \u201cFlying through a Fire Cloud\u201d (August 7, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article \u201cFlying through a Fire Cloud\u201d (August 7, 2019)",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/145446/flying-through-a-fire-cloud/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/2019/07/29/fire-weather-pyro-weather/",
-                    "description": "NASA Earth Expeditions Article \u201cFire Weather, Pyro Weather\u201d (July 29, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions Article \u201cFire Weather, Pyro Weather\u201d (July 29, 2019)",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/2019/07/29/fire-weather-pyro-weather/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/FIREXAQ/2019",
-                    "description": "FIREX-AQ Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "FIREX-AQ Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/FIREXAQ/2019",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aeronet.gsfc.nasa.gov/new_web/DRAGON-FIREX-AQ_2019.html",
-                    "description": "AERONET Data for FIREX-AQ",
                     "@type": "dcat:Distribution",
+                    "description": "AERONET Data for FIREX-AQ",
+                    "downloadURL": "https://aeronet.gsfc.nasa.gov/new_web/DRAGON-FIREX-AQ_2019.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/SurfaceMobile_CARB_InSitu_Data_1/",
-                    "description": "ASDC Direct Data Download for FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/SurfaceMobile_CARB_InSitu_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1917875750-LARC_ASDC",
+            "issued": "2020-07-07",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_SurfaceMobile_CARB_InSitu_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-07-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>15.0 -135.0 15.0 -75.0 60.0 -75.0 60.0 -135.0 15.0 -135.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-08-15T00:00:00Z/2019-11-04T23:59:59.999Z",
             "theme": [
                 "FIREX-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FIREX-AQ California Air Resources Board (CARB) Surface Mobile In-Situ Measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SMODE-RVCTD",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "S-MODE Team. 2022-09-01. S-MODE Shipboard Conductivity, Temperature, and Depth Measurements Version 1. Version 1. S-MODE Shipboard Conductivity, Temperature, and Depth Measurements Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, S-MODE Project Data Manager, Fred Bingham. https://doi.org/10.5067/SMODE-RVCTD. http://podaac.jpl.nasa.gov/S-MODE.",
-            "issued": "2021-10-29",
-            "temporal": "2021-08-01T00:00:00Z/2023-05-05T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-01",
-            "keyword": [
-                "earth science",
-                "salinity/density",
-                "ocean temperature",
-                "ocean chemistry",
-                "oceans",
-                "ocean optics"
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
-            "identifier": "C2834159558-POCLOUD",
-            "description": "This dataset contains shipboard conductivity, temperature, and depth (CTD) measurements taken during the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) field campaign. The experiment was conducted approximately 300 km offshore of San Francisco, during a pilot campaign that spanned two weeks in October 2021, and two intensive operating periods in Fall 2022 and Spring 2023. S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. The shipboard CTD rosette is cast from the R/V Oceanus where it records ocean temperature, conductivity, and pressure as it descends to depth and then returns to the surface. IOP1 and IOP2 measurements also contain biological data. Data are available in netCDF format.",
-            "series-name": "S-MODE Shipboard Conductivity, Temperature, and Depth Measurements Version 1",
-            "graphic-preview-description": "Thumbnail",
             "creator": "S-MODE Team",
-            "title": "S-MODE L2 Shipboard Conductivity, Temperature, and Depth Measurements Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_LX_SHIPBOARD_CTD_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains shipboard conductivity, temperature, and depth (CTD) measurements taken during the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) field campaign. The experiment was conducted approximately 300 km offshore of San Francisco, during a pilot campaign that spanned two weeks in October 2021, and two intensive operating periods in Fall 2022 and Spring 2023. S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. The shipboard CTD rosette is cast from the R/V Oceanus where it records ocean temperature, conductivity, and pressure as it descends to depth and then returns to the surface. IOP1 and IOP2 measurements also contain biological data. Data are available in netCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-RVCTD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-RVCTD",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://smode.whoi.edu/",
-                    "description": "Project Website for S-MODE hosted by Woods Hole Oceanographic Institute (WHOI)",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for S-MODE hosted by Woods Hole Oceanographic Institute (WHOI)",
+                    "downloadURL": "http://smode.whoi.edu/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/s-mode",
-                    "description": "Project Landing Page for S-MODE on the PO.DAAC Website",
                     "@type": "dcat:Distribution",
+                    "description": "Project Landing Page for S-MODE on the PO.DAAC Website",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/s-mode",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_LX_SHIPBOARD_CTD_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_LX_SHIPBOARD_CTD_V1.jpg",
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
-                    "downloadURL": "https://github.com/NASA-SMODE",
-                    "description": "S-MODE GitHub Organization",
                     "@type": "dcat:Distribution",
+                    "description": "S-MODE GitHub Organization",
+                    "downloadURL": "https://github.com/NASA-SMODE",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2110184927-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2110184927-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2110184927-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2110184927-POCLOUD",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/s-mode/content/S-MODE_2022_Open_Data_Workshop",
-                    "description": "2022 S-MODE Open Data Workshop Information",
                     "@type": "dcat:Distribution",
+                    "description": "2022 S-MODE Open Data Workshop Information",
+                    "downloadURL": "https://espo.nasa.gov/s-mode/content/S-MODE_2022_Open_Data_Workshop",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/s-mode/content/S-MODE_2022_ODW_Recording_and_Presentations",
-                    "description": "2022 S-MODE Open Data Workshop Presentations and Recordings",
                     "@type": "dcat:Distribution",
+                    "description": "2022 S-MODE Open Data Workshop Presentations and Recordings",
+                    "downloadURL": "https://espo.nasa.gov/s-mode/content/S-MODE_2022_ODW_Recording_and_Presentations",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/2022-SMODE-Open-Data-Workshop",
-                    "description": "2022 S-MODE Open Data Workshop Code and Tutorials",
                     "@type": "dcat:Distribution",
+                    "description": "2022 S-MODE Open Data Workshop Code and Tutorials",
+                    "downloadURL": "https://github.com/podaac/2022-SMODE-Open-Data-Workshop",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/S-MODE_Pilot-Campaign_Field-Report.pdf",
-                    "description": "S-MODE Pilot Campaign Field Report",
                     "@type": "dcat:Distribution",
+                    "description": "S-MODE Pilot Campaign Field Report",
+                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/S-MODE_Pilot-Campaign_Field-Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_LX_SHIPBOARD_CTD_V1.jpg",
+            "identifier": "C2834159558-POCLOUD",
+            "issued": "2021-10-29",
+            "keyword": [
+                "earth science",
+                "salinity/density",
+                "ocean temperature",
+                "ocean chemistry",
+                "oceans",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMODE-RVCTD",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-05-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "series-name": "S-MODE Shipboard Conductivity, Temperature, and Depth Measurements Version 1",
             "spatial": "-125.4 36.3 -122.9 38.1",
+            "temporal": "2021-08-01T00:00:00Z/2023-05-05T00:00:00Z",
             "theme": [
                 "S-MODE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "S-MODE L2 Shipboard Conductivity, Temperature, and Depth Measurements Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD13Q1.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kamel Didan. 2021-02-16. MODIS/Aqua Vegetation Indices 16-Day L3 Global 250m SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MYD13Q1.061. https://doi.org/10.5067/MODIS/MYD13Q1.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-16",
-            "temporal": "2002-07-04T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-16",
-            "keyword": [
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "biosphere",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kamel Didan",
                 "hasEmail": "mailto:didan@email.arizona.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2307290656-LPCLOUD",
-            "description": "The Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) Vegetation Indices (MYD13Q1) Version 6.1 data are generated every 16 days at 250 meter (m) spatial resolution as a Level 3 product. The MYD13Q1 product provides two primary vegetation layers. The first is the Normalized Difference Vegetation Index (NDVI) which is referred to as the continuity index to the existing National Oceanic and Atmospheric Administration-Advanced Very High Resolution Radiometer (NOAA-AVHRR) derived NDVI. The second vegetation layer is the Enhanced Vegetation Index (EVI), which has improved sensitivity over high biomass regions. The algorithm chooses the best available pixel value from all the acquisitions from the 16 day period. The criteria used is low clouds, low view angle, and the highest NDVI/EVI value.\n\nAlong with the vegetation layers and the two quality layers, the HDF file will have MODIS reflectance bands 1 (red), 2 (near-infrared), 3 (blue), and 7 (mid-infrared), as well as four observation layers. \n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Vegetation Index product suite. Further details regarding MODIS land product validation for the MOD13 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD13).\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search.",
             "creator": "Kamel Didan",
-            "title": "MODIS/Aqua Vegetation Indices 16-Day L3 Global 250m SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2357617012-LPCLOUD?h=500&w=500",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) Vegetation Indices (MYD13Q1) Version 6.1 data are generated every 16 days at 250 meter (m) spatial resolution as a Level 3 product. The MYD13Q1 product provides two primary vegetation layers. The first is the Normalized Difference Vegetation Index (NDVI) which is referred to as the continuity index to the existing National Oceanic and Atmospheric Administration-Advanced Very High Resolution Radiometer (NOAA-AVHRR) derived NDVI. The second vegetation layer is the Enhanced Vegetation Index (EVI), which has improved sensitivity over high biomass regions. The algorithm chooses the best available pixel value from all the acquisitions from the 16 day period. The criteria used is low clouds, low view angle, and the highest NDVI/EVI value.\n\nAlong with the vegetation layers and the two quality layers, the HDF file will have MODIS reflectance bands 1 (red), 2 (near-infrared), 3 (blue), and 7 (mid-infrared), as well as four observation layers. \n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Vegetation Index product suite. Further details regarding MODIS land product validation for the MOD13 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD13).\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD13Q1.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD13Q1.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD13Q1.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD13Q1.061",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD13Q1.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD13Q1.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2307290656-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2307290656-LPCLOUD",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MYD13Q1.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MYD13Q1.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/104/MOD13_ATBD.pdf",
-                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/104/MOD13_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD13Q1",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD13Q1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MYD13Q1",
-                    "description": "Further details regarding MODIS land product validation for the MYD13 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MYD13 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MYD13Q1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 3 has been achieved for the MODIS Vegetation Index product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the MODIS Vegetation Index product suite.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aqua&ver=C6",
-                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aqua&ver=C6",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2357617012-LPCLOUD?h=500&w=500",
-                    "description": "Browse image for Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2357617012-LPCLOUD?h=500&w=500",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search.",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2357617012-LPCLOUD?h=500&w=500",
+            "identifier": "C2307290656-LPCLOUD",
+            "issued": "2021-02-16",
+            "keyword": [
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD13Q1.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Vegetation Indices 16-Day L3 Global 250m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0466-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-30T01:13:15.000 to 2014-11-30T13:06:21.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0466-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0466-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0466-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-30T01:13:15.000 to 2014-11-30T13:06:21.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0466 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0466 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1721",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chini, L.P., G.C. Hurtt, R. Sahajpal, S. Frolking, K. Frieler, A. Popp, B. Bodirsky, F. Humpenoeder, M. Stevanovic, K. Calvin, S. Ostberg, L. Warszawski, and J. Volkholz. 2020. LUH2-ISIMIP2b Harmonized Global Land Use for the Years 2015-2100. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1721",
-            "issued": "2020-05-20",
-            "temporal": "2015-01-01T00:00:00Z/2100-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "vegetation",
-                "ecosystems",
-                "land surface",
-                "earth science",
-                "land use/land cover",
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
-            "identifier": "C2764728966-ORNL_CLOUD",
             "description": "This dataset provides 0.25-degree gridded, global, annual estimates of fractional land use and land cover patterns for the period 2015-2100, designed to support the ISIMIP2b effort to assess the impacts of 1.5 Deg Celcius global warming. Land use types, land use transitions, and cropland estimates of area fraction are provided and include detailed separation of primary and secondary natural vegetation into forest and non-forest sub-types, pasture into managed pasture and rangeland, and cropland into multiple crop functional types; all transitions between land use states per grid cell per year, including crop rotations, shifting cultivation, and wood harvest; and agriculture management including irrigation, synthetic nitrogen fertilizer, and biofuel management. The LUH2-ISIMIP2b datasets were derived using Land Use Harmonization 2 (LUH2) methodology and are based on land-use scenarios provided by the REMIND-MAgPIE Integrated Assessment Model using an SSP2 storyline along with RCP2.6 and RCP6.0 emissions scenarios. In contrast to the standard SSP scenarios, these land use changes additionally account for climate and atmospheric CO2 fertilization effects on the underlying patterns of potential crop yields, water availability, and terrestrial carbon content. This is achieved by using the LPJmL (Lund-Potsdam-Jena managed land) model forced with atmospheric CO2 concentrations and patterns of climate change generated from 4 different climate models (GFDL, HADGEM, IPSL, and MIROC) consistent with the 2 different RCP scenarios, resulting in a set of 8 different LUH2-ISIMIP2b datasets.",
-            "graphic-preview-description": "The area fraction within a 0.25-degree grid cell that has transitioned from C3 annual crops in 2015 to secondary vegetation in 2016 on LUH2 potential forest land. The variable displayed is c3ann_to_secdf from the file RCP60_IPSL_transitions.nc4.",
-            "title": "LUH2-ISIMIP2b Harmonized Global Land Use for the Years 2015-2100",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Land_Use_Harmonization_V2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1721",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1721",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Land_Use_Harmonization_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Land_Use_Harmonization_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Land_Use_Harmonization_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Land_Use_Harmonization_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1721",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1721",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Land_Use_Harmonization_V2/comp/LUH2-ISIMIP2b_Land_Use_Harmonization.pdf",
-                    "description": "LUH2-ISIMIP2b Harmonized Global Land Use for the Years 2015-2100: LUH2-ISIMIP2b_Land_Use_Harmonization.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "LUH2-ISIMIP2b Harmonized Global Land Use for the Years 2015-2100: LUH2-ISIMIP2b_Land_Use_Harmonization.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Land_Use_Harmonization_V2/comp/LUH2-ISIMIP2b_Land_Use_Harmonization.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Land_Use_Harmonization_V2_Fig1.png",
-                    "description": "The area fraction within a 0.25-degree grid cell that has transitioned from C3 annual crops in 2015 to secondary vegetation in 2016 on LUH2 potential forest land. The variable displayed is c3ann_to_secdf from the file RCP60_IPSL_transitions.nc4.",
                     "@type": "dcat:Distribution",
+                    "description": "The area fraction within a 0.25-degree grid cell that has transitioned from C3 annual crops in 2015 to secondary vegetation in 2016 on LUH2 potential forest land. The variable displayed is c3ann_to_secdf from the file RCP60_IPSL_transitions.nc4.",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Land_Use_Harmonization_V2_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "The area fraction within a 0.25-degree grid cell that has transitioned from C3 annual crops in 2015 to secondary vegetation in 2016 on LUH2 potential forest land. The variable displayed is c3ann_to_secdf from the file RCP60_IPSL_transitions.nc4.",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Land_Use_Harmonization_V2_Fig1.png",
+            "identifier": "C2764728966-ORNL_CLOUD",
+            "issued": "2020-05-20",
+            "keyword": [
+                "vegetation",
+                "ecosystems",
+                "land surface",
+                "earth science",
+                "land use/land cover",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1721",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-01-01T00:00:00Z/2100-01-01T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LUH2-ISIMIP2b Harmonized Global Land Use for the Years 2015-2100"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/wmcd-d5pu",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "['\"spaceflight\"' '\"time\"']",
-                "['\"sample collection\"' '\"extraction\"' '\"mass spectrometry\"' '\"data transformation\"']"
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
-            "identifier": "nasa_genelab_GLDS-359_wmcd-d5pu",
             "description": "['\"The aim of the study was to analyze exhaled breath condensate (EBC) proteome changes due to the effects of spaceflight factors. All the protocols were approved at the Institute of Biomedical Problems \u2013 Russian Federation State Scientific Research Center in the frame of Protocon experiment. EBC samples were collected by commercial devices RTube one month before flight (background) at the Yu. A. Gagarin Research and Test Cosmonaut Training Center, immediately after landing of the landing modules in the field (R0), and on the seventh day after landing as a part of medical examination (R+7). Semi-quantitative label-free proteomic analysis of 13 EBC samples collected from 5 Russian cosmonauts before and after long-term (169\u2013199 days) spaceflights were performed and resulted in 164 different proteins. The highest number of proteins was detected in EBC after landing (R0). Pathways enrichment analysis via GO database large group of proteins that take part in keratinization processes (CASP14, DSG1, DSP, JUP, and etc). Nine proteins were KRT2, KRT9, KRT1, KRT10, KRT14, DCD, KRT6C, KRT6A, KRT5 were detected in all groups (background, R0, R+1). A two-sample Welch\u2019s t-test identified the significant changing of KRT2 and KRT9 levels after landing. Enrichment analysis via KEGG database revealed significant participation (2,07E-06) of detected proteins in pathogenic E. coli infection (ACTG1, TUBA1C, TUBA4A, TUBB, TUBB8, YWHAZ). Presumably, presents of this proteins can associated with changing of cosmonauts\u2019 microbial composition. Thus EBC can be used for noninvasive monitoring of health status and respiratory tract pathologies during the spaceflight. The obtained data are important for the development of medicine in extreme situations.\"']",
-            "title": "['\"Proteome profiling of the exhaled breath condensate after long-term spaceflights\"']",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-359",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-359",
+                    "mediaType": "text/html",
                     "title": "['\"Proteome profiling of the exhaled breath condensate after long-term spaceflights\"']"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-359_wmcd-d5pu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "['\"spaceflight\"' '\"time\"']",
+                "['\"sample collection\"' '\"extraction\"' '\"mass spectrometry\"' '\"data transformation\"']"
+            ],
+            "landingPage": "https://data.nasa.gov/d/wmcd-d5pu",
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
+            "title": "['\"Proteome profiling of the exhaled breath condensate after long-term spaceflights\"']"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M09-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m09-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M09-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m09-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP009 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP009 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/175",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. NWS Daily Climatology Data: 1988 (SNF). [National Weather Service Daily Climatology Data: 1988 (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/175",
-            "issued": "2024-03-01",
-            "temporal": "1988-01-01T00:00:00Z/1988-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "precipitation",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
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
-            "identifier": "C2884978490-ORNL_CLOUD",
             "description": "Daily min, max, average temperature (F), precipitation (water equivalent in inches), and daily insolation (Langleys) for the Superior National Forest area as collected by NWS and U. of Minnesota",
-            "graphic-preview-description": "Browse Image",
-            "title": "NWS Daily Climatology Data: 1988 (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F175",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F175",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1988/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1988/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_daily_climate_1988.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_daily_climate_1988.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/175",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/175",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1988/comp/met_1988.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1988/comp/met_1988.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1988/comp/met_1988.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1988/comp/met_1988.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1988/comp/nws_daily_climate_1988.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1988/comp/nws_daily_climate_1988.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1988/comp/nws_daily_climate_1988.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1988/comp/nws_daily_climate_1988.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
+            "identifier": "C2884978490-ORNL_CLOUD",
+            "issued": "2024-03-01",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/175",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-92.51 47.66 -91.77 48.17",
+            "temporal": "1988-01-01T00:00:00Z/1988-12-31T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NWS Daily Climatology Data: 1988 (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1124",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kozovits, A.R., L.T. Viana, D.M. Sousa, A.S. Pinto, M.M.C. Bustamante, and R.G. Zepp. 2012. LBA-ECO ND-07 Nitric Oxide Flux from Cerrado Soils, Brasilia, Brazil: 2004. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1124",
-            "issued": "2023-10-03",
-            "temporal": "2004-03-22T00:00:00Z/2004-11-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "soils",
-                "atmospheric chemistry",
-                "earth science",
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
-            "identifier": "C2780948560-ORNL_CLOUD",
             "description": "This data set reports the results of soil nitric oxide (NO) flux, soil moisture, and soil nitrate (NO3) and ammonium (NH4) concentration measurements on Cerrado soils receiving nitrogen fertilization. Measurements and samples were collected from control and fertillized experimental plots on Cerrado soils within the Ecological Reserve of the Brazilian Institute of Geography and Statistic (IBGE), Brasilia, Brazil. Sampling dates were from March 26, 2004 to November 25, 2004. The soils had received nitrogen and phosphorus fertilization treatments which began in 1998. The objective of this project was to determine the long-term effects of nutrient addition (N and N+P) in native Cerrado area on N oxide fluxes from soil to the atmosphere. There is one comma delimited (.csv) ASCII file with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-07 Nitric Oxide Flux from Cerrado Soils, Brasilia, Brazil: 2004",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1124",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1124",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND07_NO_Flux_Cerrado/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND07_NO_Flux_Cerrado/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND07_NO_Flux_Cerrado.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND07_NO_Flux_Cerrado.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1124",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1124",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND07_NO_Flux_Cerrado/comp/ND07_NO_Flux_Cerrado.PDF",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND07_NO_Flux_Cerrado/comp/ND07_NO_Flux_Cerrado.PDF",
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
+            "identifier": "C2780948560-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "soils",
+                "atmospheric chemistry",
+                "earth science",
+                "land surface",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1124",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-15.93 -47.85",
+            "temporal": "2004-03-22T00:00:00Z/2004-11-25T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-07 Nitric Oxide Flux from Cerrado Soils, Brasilia, Brazil: 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-NIMS-3-TUBE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The natural form of imaging spectrometer data is the spectral image cube. It is normally in band sequential format, but has a dual nature. It is a series of 'images' of the target, each in a different wavelength, in ascending order. It is also a set of spectra, each at a particular line and sample, over the target area. Each spectrum describes a small portion of the area. When transformed into cubes, the data may be analyzed spatially, an image at a time, or spectrally, a spectrum at a time, or in more complex spatial-spectral fashion.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-nims-3-tube-v1.0_wmhi-adbr",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "sky",
                 "callisto",
@@ -1582532,759 +1582534,738 @@
                 "j rings",
                 "unknown"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-NIMS-3-TUBE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-nims-3-tube-v1.0_wmhi-adbr",
-            "description": "The natural form of imaging spectrometer data is the spectral image cube. It is normally in band sequential format, but has a dual nature. It is a series of 'images' of the target, each in a different wavelength, in ascending order. It is also a set of spectra, each at a particular line and sample, over the target area. Each spectrum describes a small portion of the area. When transformed into cubes, the data may be analyzed spatially, an image at a time, or spectrally, a spectrum at a time, or in more complex spatial-spectral fashion.",
-            "title": "GALILEO NIMS SPECTRAL IMAGE TUBES: JUPITER OPERATIONS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO NIMS SPECTRAL IMAGE TUBES: JUPITER OPERATIONS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_DC8_Data_1.",
-            "issued": "2022-09-06",
-            "temporal": "1999-11-16T00:00:00Z/2000-03-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-06",
-            "keyword": [
-                "atmosphere",
-                "atmospheric winds",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric temperature"
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
-            "identifier": "C2569836865-LARC_ASDC",
             "description": "SOLVE1_Miscellaneous_DC8_Data is the supplementary miscellaneous data for the DC-8 aircraft collected during the SAGE III Ozone Loss and Validation Experiment (SOLVE). Data collection for this product is complete.\r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE I Miscellaneous DC-8 Aircraft Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_Miscellaneous_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_Miscellaneous_DC8_Data_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836865-LARC_ASDC",
-                    "description": "Earthdata Search client for SOLVE1_Miscellaneous_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for SOLVE1_Miscellaneous_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836865-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_DC8_Data_1",
-                    "description": "DOI for SOLVE1_Miscellaneous_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for SOLVE1_Miscellaneous_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Miscellaneous_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE1_Miscellaneous_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE1_Miscellaneous_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Miscellaneous_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836865-LARC_ASDC",
+            "issued": "2022-09-06",
+            "keyword": [
+                "atmosphere",
+                "atmospheric winds",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>12.0 -122.5 12.0 126.1 89.5 126.1 89.5 -122.5 12.0 -122.5</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1999-11-16T00:00:00Z/2000-03-15T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE I Miscellaneous DC-8 Aircraft Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-03-30. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1.",
-            "issued": "2021-08-17",
-            "temporal": "2013-01-12T00:00:00Z/2013-02-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols"
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
-            "identifier": "C2245997379-LARC_ASDC",
             "description": "DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL_Data contains remotely sensed data collected by the High Spectral Resolution Lidar (HSRL-2) onboard NASA's B-200 aircraft during the California (San Joaquin Valley) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Maryland deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ California Deployment B-200 Aircraft Remotely Sensed High Spectral Resolution Lidar (HSRL-2) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
-                    "description": "DOI Data Set Landing Page for DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2245997379-LARC_ASDC",
-                    "description": "Earthdata Search for DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2245997379-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_AircraftRemoteSensing_B200_HSRL2_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_AircraftRemoteSensing_B200_HSRL2_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/California_AircraftRemoteSensing_B200_HSRL2_Data_1/contents.html",
-                    "description": "OPeNDAP data access for DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/California_AircraftRemoteSensing_B200_HSRL2_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2245997379-LARC_ASDC",
+            "issued": "2021-08-17",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_AircraftRemoteSensing_B200_HSRL2_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -130.0 25.0 -65.0 45.0 -65.0 45.0 -130.0 25.0 -130.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-01-12T00:00:00Z/2013-02-10T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ California Deployment B-200 Aircraft Remotely Sensed High Spectral Resolution Lidar (HSRL-2) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/ACADNS5UBWPQ",
             "citation": "Dan Goldberg at George Washington University. 2024-03-15. HAQ_TROPOMI_NO2_CONUS_A_L3. Version 2.4 . HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) CONUS Annual Level 3 0.01 x 0.01 Degree Gridded Data V2.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ACADNS5UBWPQ. https://disc.gsfc.nasa.gov/datacollection/HAQ_TROPOMI_NO2_CONUS_A_L3_2.4.html. Digital Science Data.",
-            "issued": "2024-01-26",
-            "temporal": "2019-01-01T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
-            "references": [
-                "https://doi.org/10.1029/2020EF001665"
-            ],
-            "keyword": [
-                "atmosphere",
-                "air quality",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Xiaohua Pan",
                 "hasEmail": "mailto:xiaohua.pan@nasa.gov"
             },
+            "creator": "Dan Goldberg at George Washington University",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2839237129-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This product provides level 3 annual averages of tropospheric Nitrogen dioxide (NO2) vertical column density derived from the level 2 Tropospheric Monitoring Instrument (TROPOMI) across the Continental United States oversampled to a spatial resolution of 0.01\u02da x 0.01\u02da (~1 km2) using a consistent algorithm from the European Space Agency (ESA) version 2.4 that can be used for trend analysis of air pollution. The dataset record began in 2019 and continues to the present. \n\nThis L3 product was developed by the George Washington University Air, Climate and Health Laboratory as part of the NASA Health Air Quality Applied Science Team (HAQAST) using Level 2 version 2.4 TROPOMI NO2 files from the ESA. The TROPOMI instrument on Sentinel-5 Precursor acquires tropospheric NO2 column contents from low Earth orbit (~824 km above ground level) once per day globally at approximately 13:30 local time.\n\nNO2 is an air pollutant that adversely affects the human respiratory system and leads to premature mortality. NO2 is also an important precursor for ozone and fine particulates, which also have severe health impacts. In urban areas, the majority of NO2 originates from anthropogenic NOx (=NO+NO2; most NOx is emitted as NO, which rapidly cycles to NO2) emissions during high-temperature fossil fuel combustion. Tropospheric NO2 vertical column contents are qualitatively representative of near-surface NO2 concentrations and NOx emissions in urban/polluted locations.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HAQ_TROPOMI_NO2_CONUS_A_L3",
-            "creator": "Dan Goldberg at George Washington University",
-            "graphic-preview-description": "Sample image: The level 3 TROPOMI Tropospheric vertical column NO2 density for 2023",
-            "title": "HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) CONUS Annual Level 3 0.01 x 0.01 Degree Gridded Data V2.4 (HAQ_TROPOMI_NO2_CONUS_A_L3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FACADNS5UBWPQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FACADNS5UBWPQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4.png",
-                    "description": "Sample image: The level 3 TROPOMI Tropospheric vertical column NO2 density for 2023",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image: The level 3 TROPOMI Tropospheric vertical column NO2 density for 2023",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4/doc/README_TROPOMI_Level3_TropNO2_DG_20240222.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4/doc/README_TROPOMI_Level3_TropNO2_DG_20240222.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQ_TROPOMI_NO2_CONUS_A_L3_2.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQ_TROPOMI_NO2_CONUS_A_L3_2.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQ_TROPOMI_NO2_CONUS_A_L3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQ_TROPOMI_NO2_CONUS_A_L3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4/contents.html",
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
+            "graphic-preview-description": "Sample image: The level 3 TROPOMI Tropospheric vertical column NO2 density for 2023",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_CONUS_A_L3.2.4.png",
+            "identifier": "C2839237129-GES_DISC",
+            "issued": "2024-01-26",
+            "keyword": [
+                "atmosphere",
+                "air quality",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ACADNS5UBWPQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2020EF001665"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "HAQ_TROPOMI_NO2_CONUS_A_L3",
             "spatial": "-124.75 24.5 -66.76 49.49",
+            "temporal": "2019-01-01T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "HAQAST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) CONUS Annual Level 3 0.01 x 0.01 Degree Gridded Data V2.4 (HAQ_TROPOMI_NO2_CONUS_A_L3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amars_cave_catalog&version=1.0",
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
-                "mars reconaissance orbiter",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Mars Global Cave Candidate Catalog Archive Bundle",
+            "identifier": "urn:nasa:pds:mars_cave_catalog_wmma-qc4u",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars reconaissance orbiter",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amars_cave_catalog&version=1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mars_cave_catalog_wmma-qc4u",
-            "description": "Mars Global Cave Candidate Catalog Archive Bundle",
-            "title": "Mars Global Cave Candidate Catalog Archive Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "Mars Global Cave Candidate Catalog Archive Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1193-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-18T19:17:50.000 to 2015-11-19T04:34:03.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1193-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1193-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1193-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-18T19:17:50.000 to 2015-11-19T04:34:03.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1193 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1193 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MODST-8D9N9",
             "citation": "NASA OBPG. 2020-01-15. MODIS Terra Level 3 SST Thermal IR 8 Day 9km Nighttime. Version 2019.0. MODIS Terra Global Level 3 Mapped SST. OBPG, Goddard Space Flight Center  Greenbelt, MD,US. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/MODST-8D9N9. https://podaac-tools.jpl.nasa.gov/drive/files/allData/modis/L3/docs/modis_sst.html.",
-            "issued": "2019-12-14",
-            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-14",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2015.04.023",
-                "https://doi.org/10.1175/JTECH-D-18-0103.1"
-            ],
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "ngda",
-                "national geospatial data asset",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036877986-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "Day and night spatially gridded (L3) global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODST-8D9N4",
-            "release-place": "OBPG, Goddard Space Flight Center  Greenbelt, MD,US",
-            "series-name": "MODIS Terra Level 3 SST Thermal IR 8 Day 9km Nighttime",
             "creator": "NASA OBPG",
-            "title": "MODIS Terra Level 3 SST Thermal IR 8 Day 9km Nighttime V2019.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V2019.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Day and night spatially gridded (L3) global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODST-8D9N4",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODST-8D9N9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODST-8D9N9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/r2019/sst/",
-                    "description": "OBPG SST Reprocessing v2019.0 summary",
                     "@type": "dcat:Distribution",
+                    "description": "OBPG SST Reprocessing v2019.0 summary",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/r2019/sst/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V2019.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V2019.0.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877986-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877986-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877986-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877986-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V2019.0.jpg",
+            "identifier": "C2036877986-POCLOUD",
+            "issued": "2019-12-14",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "ngda",
+                "national geospatial data asset",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODST-8D9N9",
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
+            "series-name": "MODIS Terra Level 3 SST Thermal IR 8 Day 9km Nighttime",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "EOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS Terra Level 3 SST Thermal IR 8 Day 9km Nighttime V2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1195",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yokelson, R.J., T.R. Karl, P.E. Artaxo, D.R. Blake, T.J. Christian, D.W.T. Griffith, A.B. Guenther, and W.M. Hao. 2013. LBA-ECO TG-10 Fire Emission Factors in Mato Grosso, Para, and Amazonas, Brazil: 2004. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1195",
-            "issued": "2022-05-10",
-            "temporal": "2004-08-29T00:00:00Z/2004-09-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-26",
-            "keyword": [
-                "air quality",
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
-            "identifier": "C2773193196-ORNL_CLOUD",
             "description": "This data set provides derived emission factors (EFs), reported in grams of compound emitted per kilogram of dry fuel (g/kg), for PM10 (particulate matter up to 10 micrometers in size), O3, CO2, CO, NO, NO2, HONO, HCN, NH3, OCS, DMS, CH4, and up to 48 non-methane organic compounds (NMOC) from the Tropical Forest and Fire Emissions Experiment (TROFFEE). TROFFEE used laboratory measurements followed by airborne and ground based field campaigns in Mato Grosso, Para, and Amazonas, Brazil during the 2004 Amazon dry season to quantify the emissions from pristine tropical forest and several plantations as well as the emissions, fuel consumption, and fire ecology of tropical deforestation fires. EFs were determined for 19 tropical deforestation fires in August and September, 2004. The combined output of these fires created a massive megaplume more than 500-km wide and covered a large area in Brazil, Bolivia, and Paraguay for about one month. For the megaplume, the EFs (reported in grams of compound emitted per kilogram of dry fuel (g/kg)) represented the effective emissions factor measured downwind from the source.There are two comma-delimited data files (.csv) and one text file (.txt) with this data set. The text file contains information regarding the fuel/fire sources, latitude and longitudes (also provided in the data files).",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO TG-10 Fire Emission Factors in Mato Grosso, Para, and Amazonas, Brazil: 2004",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1195",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1195",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/trace_gases/TG10_TROFFEE/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/trace_gases/TG10_TROFFEE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/TG10_TROFFEE.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/TG10_TROFFEE.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1195",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1195",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/trace_gases/TG10_TROFFEE/comp/TG10_TROFFEE.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/trace_gases/TG10_TROFFEE/comp/TG10_TROFFEE.pdf",
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
+            "identifier": "C2773193196-ORNL_CLOUD",
+            "issued": "2022-05-10",
+            "keyword": [
+                "air quality",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1195",
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
             "spatial": "-54.19 -11.49 -51.8 -3.01",
+            "temporal": "2004-08-29T00:00:00Z/2004-09-08T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO TG-10 Fire Emission Factors in Mato Grosso, Para, and Amazonas, Brazil: 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-6-DDR-V1.0",
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
-                "mars reconnaissance orbiter",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset is intended to include information on observation conditions, physical properties and coordinates of IR and VNIR data cubes from the CRISM instrument on MRO when the data cubes are pointed at Mars' surface. The information is mapped to the sensor space of non-map-projected data, EDRs and TRDRs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-6-ddr-v1.0_wmqz-6mqm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars reconnaissance orbiter",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-6-DDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-6-ddr-v1.0_wmqz-6mqm",
-            "description": "This dataset is intended to include information on observation conditions, physical properties and coordinates of IR and VNIR data cubes from the CRISM instrument on MRO when the data cubes are pointed at Mars' surface. The information is mapped to the sensor space of non-map-projected data, EDRs and TRDRs.",
-            "title": "MRO CRISM DERIVED DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MRO CRISM DERIVED DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-LAUNCH-V3.0",
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
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-launch-v3.0_wmrc-pfps",
             "description": "This data set contains Raw data taken by the New Horizons                Student Dust Counter                                                   instrument during the                                                    post-launch checkout                                                   mission phase.  This is VERSION 3.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SDC POST-LAUNCH CHECKOUT                                                \n      RAW V3.0",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1583292,44 +1583273,42 @@
                     "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-launch-v3.0_wmrc-pfps",
+            "issued": "2018-09-05",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-LAUNCH-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
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
+            "title": "NEW HORIZONS                            \n      SDC POST-LAUNCH CHECKOUT                                                \n      RAW V3.0"
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
-                "ask magazine",
-                "appel",
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
-            "identifier": "NASA-860__48",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1583337,1206 +1583316,1204 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__48",
+            "issued": "2018-06-25",
+            "keyword": [
+                "ask magazine",
+                "appel",
+                "sharing",
+                "knowledge"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0656-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-18T10:15:30.000 to 2015-03-18T12:22:32.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0656-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0656-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0656-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-18T10:15:30.000 to 2015-03-18T12:22:32.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0656 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0656 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP009-V2.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP009 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nthe MTP009 part of it.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp009-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP009-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp009-v2.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP009 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nthe MTP009 part of it.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP009 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP009 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://power.larc.nasa.gov/",
             "bureauCode": [
                 "026:00"
             ],
-            "rights": "Please reference the acknowledgments on https://power.larc.nasa.gov/.",
             "citation": "This data was obtained from the NASA Langley Research Center (LaRC) POWER Project funded through the NASA Earth Science/Applied Science Program.",
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-02",
-            "keyword": [
-                "climate",
-                "near real time (nrt)",
-                "nrt",
-                "google earth",
-                "renewable energy",
-                "solar",
-                "temperature",
-                "time series",
-                "wind",
-                "power",
-                "geospatial",
-                "energy",
-                "irradiance",
-                "meteorology"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dr. Paul Stackhouse",
                 "hasEmail": "mailto:larc-power-project@mail.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000112",
+            "dataQuality": true,
             "description": "The POWER Project contains over 380 satellite-derived meteorology and solar energy Analysis Ready Data (ARD) at four temporal levels: hourly, daily, monthly (by year 12 months + annual averages), and climatology. The POWER Data Archive provides data at the native resolution of the source data products. The data is updated nightly to maintain Near Real Time (NRT) availability (2-3 days for meteorological parameters and 5-7 days for solar).\n\nThe POWER Project targets three specific user communities: Renewable Energy (RE), Sustainable Buildings (SB), and Agroclimatology (AG). The POWER Projects provides community specific parameters, output formats, naming conventions, and units that are commonly employed by each user community.\n\nThe POWER Services Catalog consists of a series of RESTful Application Programming Interfaces (API), geospatial enabled image services, and a web mapping Data Access Viewer (DAV). These three different service offerings support data discovery, access, and distribution to our user base as ARD and as direct application inputs to decision support tools.",
-            "title": "Prediction Of Worldwide Energy Resources (POWER)",
-            "programCode": [
-                "026:006"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://power.larc.nasa.gov/dashboard/",
-                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
                     "@type": "dcat:Distribution",
+                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
+                    "downloadURL": "https://power.larc.nasa.gov/dashboard/",
+                    "mediaType": "text/html",
                     "title": "Prediction Of Worldwide Energy Resources (POWER)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://power.larc.nasa.gov/docs/services/",
-                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
                     "@type": "dcat:Distribution",
+                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
+                    "downloadURL": "https://power.larc.nasa.gov/docs/services/",
+                    "mediaType": "text/html",
                     "title": "Prediction Of Worldwide Energy Resources (POWER)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nasa.maps.arcgis.com/home/group.html?id=4b75def515df430980faebca6a007465",
-                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
                     "@type": "dcat:Distribution",
+                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
+                    "downloadURL": "https://nasa.maps.arcgis.com/home/group.html?id=4b75def515df430980faebca6a007465",
+                    "mediaType": "text/html",
                     "title": "Prediction Of Worldwide Energy Resources (POWER)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://power.larc.nasa.gov/beta/data-access-viewer/",
-                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
                     "@type": "dcat:Distribution",
+                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
+                    "downloadURL": "https://power.larc.nasa.gov/beta/data-access-viewer/",
+                    "mediaType": "text/html",
                     "title": "Prediction Of Worldwide Energy Resources (POWER)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://power.larc.nasa.gov/docs/tutorials/",
-                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
                     "@type": "dcat:Distribution",
+                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
+                    "downloadURL": "https://power.larc.nasa.gov/docs/tutorials/",
+                    "mediaType": "text/html",
                     "title": "Prediction Of Worldwide Energy Resources (POWER)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://power.larc.nasa.gov/docs/methodology/",
-                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
                     "@type": "dcat:Distribution",
+                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
+                    "downloadURL": "https://power.larc.nasa.gov/docs/methodology/",
+                    "mediaType": "text/html",
                     "title": "Prediction Of Worldwide Energy Resources (POWER)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://power.larc.nasa.gov/api/pages/",
-                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
                     "@type": "dcat:Distribution",
+                    "description": "Solar and meteorological data sets from NASA research for the support of renewable energy, building energy efficiency and agricultural needs.",
+                    "downloadURL": "https://power.larc.nasa.gov/api/pages/",
+                    "mediaType": "text/html",
                     "title": "Prediction Of Worldwide Energy Resources (POWER)"
                 }
             ],
+            "identifier": "NASA-0000112",
+            "issued": "2018-06-25",
+            "keyword": [
+                "climate",
+                "near real time (nrt)",
+                "nrt",
+                "google earth",
+                "renewable energy",
+                "solar",
+                "temperature",
+                "time series",
+                "wind",
+                "power",
+                "geospatial",
+                "energy",
+                "irradiance",
+                "meteorology"
+            ],
+            "landingPage": "https://power.larc.nasa.gov/",
+            "modified": "2024-02-02",
+            "programCode": [
+                "026:006"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "rights": "Please reference the acknowledgments on https://power.larc.nasa.gov/.",
             "spatial": "Global",
-            "dataQuality": true,
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Prediction Of Worldwide Energy Resources (POWER)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1181-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-14T10:17:50.000 to 2015-11-14T16:54:49.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1181-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1181-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1181-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-14T10:17:50.000 to 2015-11-14T16:54:49.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1181 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1181 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/RKPHT8KC1Y1T",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2T1NXLND. Version 5.12.4. MERRA-2 tavg1_2d_lnd_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Land Surface Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/RKPHT8KC1Y1T. https://disc.gsfc.nasa.gov/datacollection/M2T1NXLND_5.12.4.html. Digital Science Data.",
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
-                "earth science",
-                "ground water",
-                "snow/ice",
-                "terrestrial hydrosphere",
-                "soils",
-                "vegetation",
-                "precipitation",
-                "agriculture",
-                "land surface",
-                "surface water",
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812861-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2T1NXLND (or  tavg1_2d_lnd_Nx) is an hourly time-averaged 2-dimensional data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of land surface diagnostics, such as baseflow flux, runoff, surface soil wetness,  root zone soil wetness, water at surface layer, water at root zone layer, and soil temperature at six layers.  The data field is time-stamped with the central time of an hour starting from 00:30 UTC, e.g.: 00:30, 01:30, \u2026 , 23:30 UTC.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2T1NXLND",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 tavg1_2d_lnd_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Land Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXLND) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2T1NXLND",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRKPHT8KC1Y1T",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRKPHT8KC1Y1T",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXLND_5.12.4.png",
-                    "description": "M2T1NXLND variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2T1NXLND variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXLND_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T1NXLND_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T1NXLND_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXLND.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXLND.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2T1NXLND",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2T1NXLND",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T1NXLND",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T1NXLND",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXLND.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXLND.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXLND.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXLND.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T1NXLND.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T1NXLND.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXLND.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXLND.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2T1NXLND",
+            "identifier": "C1276812861-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "earth science",
+                "ground water",
+                "snow/ice",
+                "terrestrial hydrosphere",
+                "soils",
+                "vegetation",
+                "precipitation",
+                "agriculture",
+                "land surface",
+                "surface water",
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/RKPHT8KC1Y1T",
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
+            "series-name": "M2T1NXLND",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavg1_2d_lnd_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Land Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXLND) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4HD7SKJ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Intergovernmental Panel on Climate Change - IPCC. 2000-07-31. IPCC Special Report on Emissions Scenarios (SRES) Fluor-Gases Emissions Dataset. Version 1.00. New York, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Cambridge University Press. https://doi.org/10.7927/H4HD7SKJ. https://doi.org/10.7927/H4HD7SKJ.",
-            "issued": "2000-07-31",
-            "temporal": "1990-01-01T00:00:00Z/2100-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2000-07-31",
-            "references": [
-                "https://doi.org/10.7927/H4N29TWJ",
-                "https://doi.org/10.7927/H4RV0KMH",
-                "https://doi.org/10.7927/H41C1TT4",
-                "https://doi.org/10.7927/H4WM1BB7",
-                "https://doi.org/10.7927/H4XG9P2R",
-                "https://doi.org/10.7927/H4542KJV",
-                "https://doi.org/10.7927/H4FT8J0X"
-            ],
-            "keyword": [
-                "air quality",
-                "atmosphere",
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
-            "identifier": "C179001933-SEDAC",
-            "description": "The Intergovernmental Panel on Climate Change (IPCC) Special Report Emissions Scenarios (SRES) Fluor-Gases Emissions Dataset consists of global and regional emissions of Hydrofluorocarbons (HFCs), Perfluorocarbons (PFCs), Sulfur Hexafluoride (SF6), Cholorfluorocarbons (CFCs) and Hydrochlorofluorocarbons (HCFCs) projected every 10 years beginning in 1990 through 2100. This data set is produced by the IPCC and is distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "New York, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Intergovernmental Panel on Climate Change - IPCC",
-            "title": "IPCC Special Report on Emissions Scenarios (SRES) Fluor-Gases Emissions Dataset",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-fluor-gases-emissions/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Intergovernmental Panel on Climate Change (IPCC) Special Report Emissions Scenarios (SRES) Fluor-Gases Emissions Dataset consists of global and regional emissions of Hydrofluorocarbons (HFCs), Perfluorocarbons (PFCs), Sulfur Hexafluoride (SF6), Cholorfluorocarbons (CFCs) and Hydrochlorofluorocarbons (HCFCs) projected every 10 years beginning in 1990 through 2100. This data set is produced by the IPCC and is distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4HD7SKJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4HD7SKJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-fluor-gases-emissions/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-fluor-gases-emissions/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-fluor-gases-emissions/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-fluor-gases-emissions/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-fluor-gases-emissions",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-fluor-gases-emissions",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-fluor-gases-emissions/sedac-logo.jpg",
+            "identifier": "C179001933-SEDAC",
+            "issued": "2000-07-31",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4HD7SKJ",
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
+                "https://doi.org/10.7927/H4N29TWJ",
+                "https://doi.org/10.7927/H4RV0KMH",
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
+            "title": "IPCC Special Report on Emissions Scenarios (SRES) Fluor-Gases Emissions Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/10.7927/1x94-mv38",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Amini, H., M. Danesh-Yazdi, Q. Di, W. Requia, Y. Wei, Y. AbuAwad, L. Shi, M. Franklin, C.-M. Kang, J. M. Wolfson, P. James, R. Habre, Q. Zhu, J. S. Apte, Z. J. Andersen, X. Xing, C. Hultquist, I. Kloog, F. Dominici, P. Koutrakis, and J. Schwartz. 2023-04-28. Annual Mean PM2.5 Components Trace Elements (TEs) 50m Urban and 1km Non-Urban Area Grids for Contiguous U.S., 2000-2019, v1. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/10.7927/1x94-mv38. https://doi.org/10.7927/1x94-mv38.",
-            "issued": "2023-04-28",
-            "temporal": "2000-01-01T00:00:00Z/2019-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-28",
-            "keyword": [
-                "air quality",
-                "earth science",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C2673738199-SEDAC",
-            "description": "The Annual Mean PM2.5 Components Trace Elements (TEs) 50m Urban and 1km Non-Urban Area Grids for Contiguous U.S., 2000-2019, v1 data set contains annual predictions of trace elements concentrations at a hyper resolution (50m x 50m grid cells) in urban areas and a high resolution (1km x 1km grid cells) in non-urban areas, for the years 2000 to 2019. Particulate matter with an aerodynamic diameter of less than 2.5 \u00ef\u00bf\u00bdm (PM2.5) is a human silent killer of millions worldwide, and contains many trace elements (TEs). Understanding the relative toxicity is largely limited by the lack of data. In this work, ensembles of machine learning models were used to generate approximately 163 billion predictions estimating annual mean PM2.5 TEs, namely Bromine (Br), Calcium (Ca), Copper (Cu), Iron (Fe), Potassium (K), Nickel (Ni), Lead (Pb), Silicon (Si), Vanadium (V), and Zinc (Zn). The monitored data from approximately 600 locations were integrated with more than 160 predictors, such as time and location, satellite observations, composite predictors, meteorological covariates, and many novel land use variables using several machine learning algorithms and ensemble methods. Multiple machine-learning models were developed covering urban areas and non-urban areas. Their predictions were then ensembled using either a Generalized Additive Model (GAM) Ensemble Geographically-Weighted-Averaging (GAM-ENWA), or Super-Learners. The overall best model R-squared values for the test sets ranged from 0.79 for Copper to 0.88 for Zinc in non-urban areas. In urban areas, the R-squared model values ranged from 0.80 for Copper to 0.88 for Zinc. The Coordinate Reference System (CRS) used in the predictions is the World Geodetic System 1984 (WGS84) and the Units for the PM2.5 Components TEs are ng/m^3. The data are provided in RDS tabular format, a file format native to the R programming language, but can also be opened by other languages such as Python.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Amini, H., M. Danesh-Yazdi, Q. Di, W. Requia, Y. Wei, Y. AbuAwad, L. Shi, M. Franklin, C.-M. Kang, J. M. Wolfson, P. James, R. Habre, Q. Zhu, J. S. Apte, Z. J. Andersen, X. Xing, C. Hultquist, I. Kloog, F. Dominici, P. Koutrakis, and J. Schwartz",
-            "title": "Annual Mean PM2.5 Components Trace Elements (TEs) 50m Urban and 1km Non-Urban Area Grids for Contiguous U.S., 2000-2019, v1",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-pm2-5-component-trace-elements-50m-1km-contiguous-us-2000-2019/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Annual Mean PM2.5 Components Trace Elements (TEs) 50m Urban and 1km Non-Urban Area Grids for Contiguous U.S., 2000-2019, v1 data set contains annual predictions of trace elements concentrations at a hyper resolution (50m x 50m grid cells) in urban areas and a high resolution (1km x 1km grid cells) in non-urban areas, for the years 2000 to 2019. Particulate matter with an aerodynamic diameter of less than 2.5 \u00ef\u00bf\u00bdm (PM2.5) is a human silent killer of millions worldwide, and contains many trace elements (TEs). Understanding the relative toxicity is largely limited by the lack of data. In this work, ensembles of machine learning models were used to generate approximately 163 billion predictions estimating annual mean PM2.5 TEs, namely Bromine (Br), Calcium (Ca), Copper (Cu), Iron (Fe), Potassium (K), Nickel (Ni), Lead (Pb), Silicon (Si), Vanadium (V), and Zinc (Zn). The monitored data from approximately 600 locations were integrated with more than 160 predictors, such as time and location, satellite observations, composite predictors, meteorological covariates, and many novel land use variables using several machine learning algorithms and ensemble methods. Multiple machine-learning models were developed covering urban areas and non-urban areas. Their predictions were then ensembled using either a Generalized Additive Model (GAM) Ensemble Geographically-Weighted-Averaging (GAM-ENWA), or Super-Learners. The overall best model R-squared values for the test sets ranged from 0.79 for Copper to 0.88 for Zinc in non-urban areas. In urban areas, the R-squared model values ranged from 0.80 for Copper to 0.88 for Zinc. The Coordinate Reference System (CRS) used in the predictions is the World Geodetic System 1984 (WGS84) and the Units for the PM2.5 Components TEs are ng/m^3. The data are provided in RDS tabular format, a file format native to the R programming language, but can also be opened by other languages such as Python.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2F1x94-mv38",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2F1x94-mv38",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-pm2-5-component-trace-elements-50m-1km-contiguous-us-2000-2019/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-pm2-5-component-trace-elements-50m-1km-contiguous-us-2000-2019/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-component-trace-elements-50m-1km-contiguous-us-2000-2019/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-component-trace-elements-50m-1km-contiguous-us-2000-2019/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-trace-elements-2000-2019/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-trace-elements-2000-2019/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-component-trace-elements-50m-1km-contiguous-us-2000-2019",
-                    "description": "Data Set Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-pm2-5-component-trace-elements-50m-1km-contiguous-us-2000-2019",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-pm2-5-component-trace-elements-50m-1km-contiguous-us-2000-2019/sedac-logo.jpg",
+            "identifier": "C2673738199-SEDAC",
+            "issued": "2023-04-28",
+            "keyword": [
+                "air quality",
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.7927/10.7927/1x94-mv38",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 17.0 -65.0 72.0",
+            "temporal": "2000-01-01T00:00:00Z/2019-12-31T00:00:00Z",
             "theme": [
                 "AQDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Annual Mean PM2.5 Components Trace Elements (TEs) 50m Urban and 1km Non-Urban Area Grids for Contiguous U.S., 2000-2019, v1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-VIR-2-EDR-IR-CRUISE-SPECTRA-V1.0",
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
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the digital       numbers (DN) contained in the telemetry (TM) packages of the VIR-IR     instrument on board of the spacecraft DAWN. The data are from the       cruise phase from launch to Vesta (Sep 2009-May 2011), and Vesta        to Ceres (Sep 2012-Dec 2014).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-vir-2-edr-ir-cruise-spectra-v1.0_wnji-ak76",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-VIR-2-EDR-IR-CRUISE-SPECTRA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-vir-2-edr-ir-cruise-spectra-v1.0_wnji-ak76",
-            "description": "This data set contains the digital       numbers (DN) contained in the telemetry (TM) packages of the VIR-IR     instrument on board of the spacecraft DAWN. The data are from the       cruise phase from launch to Vesta (Sep 2009-May 2011), and Vesta        to Ceres (Sep 2012-Dec 2014).",
-            "title": "DAWN VIR RAW (EDR) CRUISE CHECKOUT/CALIB IR SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN VIR RAW (EDR) CRUISE CHECKOUT/CALIB IR SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-SD2-3-PHC-V1.0",
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
+            "description": "This archive contains calibrated data and telemetry data from the SD2 instrument onboard ROSETTA Lander, acquired during the PHC (Post Hibernation Commissioning) phase. It also contains documentation which describes the SD2 experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-sd2-3-phc-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-SD2-3-PHC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-sd2-3-phc-v1.0",
-            "description": "This archive contains calibrated data and telemetry data from the SD2 instrument onboard ROSETTA Lander, acquired during the PHC (Post Hibernation Commissioning) phase. It also contains documentation which describes the SD2 experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL SD2 3 PHC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL SD2 3 PHC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/635",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stillwell-Soller, L.M., L. Klinger, D. Pollard, and S. Thompson. 2002. SAFARI 2000 Freshwater Wetlands, 1-Deg (Stillwell-Soller et al.). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/635",
-            "issued": "2023-11-20",
-            "temporal": "1995-01-01T00:00:00Z/1995-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
-            "keyword": [
-                "earth science",
-                "terrestrial hydrosphere",
-                "biosphere",
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
-            "identifier": "C2804801359-ORNL_CLOUD",
             "description": "This data set consists of a southern Africa subset of the Global Distribution of Freshwater Wetlands database 1-degree data and is available in ASCII GRID and binary image file formats.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Freshwater Wetlands, 1-Deg (Stillwell-Soller et al.)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F635",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F635",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/vegetation_wetlands/s2k_soller_wetlands/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/vegetation_wetlands/s2k_soller_wetlands/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/sollerwetlands.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/sollerwetlands.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/635",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/635",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/vegetation_wetlands/s2k_soller_wetlands/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/vegetation_wetlands/s2k_soller_wetlands/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/vegetation_wetlands/s2k_soller_wetlands/comp/sollerwetlands_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/vegetation_wetlands/s2k_soller_wetlands/comp/sollerwetlands_readme.pdf",
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
+            "identifier": "C2804801359-ORNL_CLOUD",
+            "issued": "2023-11-20",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "biosphere",
+                "surface water",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/635",
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
             "spatial": "5.0 -35.0 60.0 5.0",
+            "temporal": "1995-01-01T00:00:00Z/1995-09-30T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Freshwater Wetlands, 1-Deg (Stillwell-Soller et al.)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/368",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "McCaughey, J.H., P.M. Lafleur, and D.E. Jelinski. 1999. BOREAS TF-10 NSA-Fen Tower Flux and Meteorological Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/368",
-            "issued": "2023-11-22",
-            "temporal": "1993-08-15T00:00:00Z/1996-11-10T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "soils",
-                "precipitation",
-                "land surface",
-                "atmospheric radiation",
-                "frozen ground",
-                "atmospheric temperature",
-                "terrestrial hydrosphere",
-                "vegetation",
-                "earth science",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmospheric winds",
-                "biosphere",
-                "atmospheric water vapor",
-                "surface water",
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
-            "identifier": "C2808130902-ORNL_CLOUD",
             "description": "The flux and ancillary data collected at the NSA-Fen tower flux site by the TF-10 group.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-10 NSA-Fen Tower Flux and Meteorological Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F368",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F368",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf10fxmt/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf10fxmt/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF10_NSA-Fen_Flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF10_NSA-Fen_Flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/368",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/368",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf10fxmt/comp/tf10fxmt.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf10fxmt/comp/tf10fxmt.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf10fxmt/comp/TF10_NSA-Fen_Flux.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf10fxmt/comp/TF10_NSA-Fen_Flux.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf10fxmt/comp/TF10_NSA-Fen_Flux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf10fxmt/comp/TF10_NSA-Fen_Flux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf10fxmt/comp/TF10_NSA-Fen_Flux.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf10fxmt/comp/TF10_NSA-Fen_Flux.txt",
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
+            "identifier": "C2808130902-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "soils",
+                "precipitation",
+                "land surface",
+                "atmospheric radiation",
+                "frozen ground",
+                "atmospheric temperature",
+                "terrestrial hydrosphere",
+                "vegetation",
+                "earth science",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric winds",
+                "biosphere",
+                "atmospheric water vapor",
+                "surface water",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/368",
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
             "spatial": "55.91 -98.42",
+            "temporal": "1993-08-15T00:00:00Z/1996-11-10T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-10 NSA-Fen Tower Flux and Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/7X0YS69Q188Q",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX19-22 Massachusetts UAVSAR Mosaics V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/7X0YS69Q188Q.",
-            "issued": "2022-04-25",
-            "temporal": "2022-04-25T00:00:00Z/2022-07-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-25",
-            "keyword": [
-                "earth science",
-                "radar",
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
-            "identifier": "C3306692478-NSIDC_ECS",
             "description": "This data set consists of mosaicked Uninhabited Aerial Vehicle Synthetic Aperture Radar (UAVSAR) images corrected for terrain-flattened gamma. Data image files at three different polarization configurations were composited daily between April to July 2022 in the vicinity of Petersham, Massachusetts during the SMAPVEX19-22 (Soil Moisture Active Passive Validation Experiment 2019-2022) field campaign. The location was chosen due to its forested land cover, as SMAPVEX19-22 aims to validate satellite derived soil moisture estimates in forested areas.",
-            "title": "SMAPVEX19-22 Massachusetts UAVSAR Mosaics V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7X0YS69Q188Q",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7X0YS69Q188Q",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV19MA_SAR.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV19MA_SAR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SV19MA_SAR+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SV19MA_SAR+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV19MA_SAR/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV19MA_SAR/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7X0YS69Q188Q",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/7X0YS69Q188Q",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7X0YS69Q188Q",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/7X0YS69Q188Q",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3306692478-NSIDC_ECS",
+            "issued": "2022-04-25",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/7X0YS69Q188Q",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-72.33 42.32 -71.91 42.72",
+            "temporal": "2022-04-25T00:00:00Z/2022-07-25T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX19-22 Massachusetts UAVSAR Mosaics V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOC-NA%2FWA-2-SDP-L0-V1.0",
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
+            "description": "This data set contains portions of the MOC Standard Data Product (SDP) Archive, a collection of compressed image data from the Mars Orbiter Camera on the Mars Global Surveyor spacecraft. Image data are stored with PDS labels, but are otherwise unprocessed and uncalibrated.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-moc-na-wa-2-sdp-l0-v1.0_wnsm-ubj8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOC-NA%2FWA-2-SDP-L0-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-moc-na-wa-2-sdp-l0-v1.0_wnsm-ubj8",
-            "description": "This data set contains portions of the MOC Standard Data Product (SDP) Archive, a collection of compressed image data from the Mars Orbiter Camera on the Mars Global Surveyor spacecraft. Image data are stored with PDS labels, but are otherwise unprocessed and uncalibrated.",
-            "title": "MOC SDP ARCHIVE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MOC SDP ARCHIVE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TCLQAIQ7Y5GS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX04 Two-Dimensional Synthetic Aperture Radiometer (2D-STAR) Brightness Temperatures, Arizona, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/TCLQAIQ7Y5GS.",
-            "issued": "2004-08-08",
-            "temporal": "2004-08-08T00:00:00Z/2004-08-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-08-26",
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
-            "identifier": "C1386205151-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set includes dual-polarized L-band brightness temperature and soil moisture data measured by the Two-Dimensional Synthetic Aperture Radiometer (2D-STAR) instrument.",
-            "title": "SMEX04 Two-Dimensional Synthetic Aperture Radiometer (2D-STAR) Brightness Temperatures, Arizona, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCLQAIQ7Y5GS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCLQAIQ7Y5GS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/2DSTAR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/2DSTAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/2DSTAR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/2DSTAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TCLQAIQ7Y5GS",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/TCLQAIQ7Y5GS",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TCLQAIQ7Y5GS",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/TCLQAIQ7Y5GS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205151-NSIDCV0",
+            "issued": "2004-08-08",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TCLQAIQ7Y5GS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-08-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-110.2 29.6 -109.6 32.1",
+            "temporal": "2004-08-08T00:00:00Z/2004-08-26T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX04 Two-Dimensional Synthetic Aperture Radiometer (2D-STAR) Brightness Temperatures, Arizona, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_daily_utc_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_daily_utc_1.",
-            "issued": "2020-10-05",
-            "temporal": "1988-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-05",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation",
-                "clouds"
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
-            "identifier": "C2062227430-LARC_ASDC",
             "description": "GEWEXSRB_Rel4-IP_Longwave_daily_utc is the Global Energy and Water Exchanges (GEWEX) Surface Radiation Budget (SRB) Integrated Product (Rel-4) Longwave Daily Average by UTC data product. It contains global fields of 26 longwave surface, Top of Atmosphere (TOA), and atmospheric profile radiative parameters derived with the Longwave algorithm of the NASA World Climate Research Programme/Global Energy and Water-Cycle Experiment (WCRP/GEWEX) Surface Radiation Budget (SRB) Project. This version is known as Release 4-Integrated Product. The fluxes include all-sky, clear-sky and pristine-sky TOA upward fluxes (outgoing longwave radiation, OLR), all-sky, clear-sky and pristine-sky upward and downward fluxes at: tropopause, 200hPa, 500hPa and surface. A status flag of filled cloud properties is also included. Inputs to the longwave algorithm are cloud information based on ISCCP HXS, meteorology from ISCCP nnHIRS, SeaFlux SST and surface, LandFlux meteorology, and MERRA-2 conditionally. The temporal range is January 1988 through December 2009, with the ends bound by input constraints. These data are averaged by UTC from 3-hourly values. Data collection for this product is complete.",
-            "title": "GEWEX SRB Integrated Product (Rel-4) Longwave Daily Average by UTC",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Longwave_daily_utc_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Longwave_daily_utc_1",
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
-                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_daily_utc_1",
-                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_daily_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_daily_utc_1",
+                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_daily_utc_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_ATBD.pdf",
-                    "description": "SRB Rel4-IP Algorithm Theoretical Basis Document.",
                     "@type": "dcat:Distribution",
+                    "description": "SRB Rel4-IP Algorithm Theoretical Basis Document.",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2062227430-LARC_ASDC",
-                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Longwave_daily_utc_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Longwave_daily_utc_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2062227430-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Longwave_daily_utc_1/",
-                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Longwave_daily_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Longwave_daily_utc_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Longwave_daily_utc_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Longwave_daily_utc_1/contents.html",
-                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Longwave_daily_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Longwave_daily_utc_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Longwave_daily_utc_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2062227430-LARC_ASDC",
+            "issued": "2020-10-05",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_daily_utc_1",
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
+            "title": "GEWEX SRB Integrated Product (Rel-4) Longwave Daily Average by UTC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPM/DPRGMI/CMB/3B-DAY/07",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "William Olson. 2022-05-09. GPM_3CMB_DAY. GPM DPR and GMI (Combined Precipitation) L3 1 day 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/DPRGMI/CMB/3B-DAY/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3CMB_DAY_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-03-08T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "atmosphere",
-                "atmospheric water vapor",
-                "earth science",
-                "precipitation"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WILLIAM OLSON",
                 "hasEmail": "mailto:bill.olson@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2179081680-GES_DISC",
-            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n. \n\nThis is a precipitation product created from the combination of the Global Precipitation Measurement (GPM) Microwave Imager (GMI) and Dual-frequency Precipitation Radar (DPR) instruments.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3CMB_DAY",
             "creator": "William Olson",
-            "title": "GPM DPR and GMI (Combined Precipitation) L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3CMB_DAY) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3CMB_DAY_07.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n. \n\nThis is a precipitation product created from the combination of the Global Precipitation Measurement (GPM) Microwave Imager (GMI) and Dual-frequency Precipitation Radar (DPR) instruments.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPRGMI%2FCMB%2F3B-DAY%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPRGMI%2FCMB%2F3B-DAY%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1584546,45 +1584523,45 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3CMB_DAY_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3CMB_DAY_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3CMB_DAY.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3CMB_DAY.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3CMB_DAY.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3CMB_DAY.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3CMB_DAY_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3CMB_DAY_07",
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
@@ -1584594,1324 +1584571,1359 @@
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
-                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3CMB_DAY_07.png",
+            "identifier": "C2179081680-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmosphere",
+                "atmospheric water vapor",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/DPRGMI/CMB/3B-DAY/07",
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
+            "series-name": "GPM_3CMB_DAY",
             "spatial": "-180.0 -67.0 180.0 67.0",
+            "temporal": "2014-03-08T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM DPR and GMI (Combined Precipitation) L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3CMB_DAY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/YDZXY4Q79VIJ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Grand Mesa Reference GIS Data Sets V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/YDZXY4Q79VIJ.",
-            "issued": "2019-09-21",
-            "temporal": "2019-09-21T00:00:00Z/2020-02-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-14",
-            "keyword": [
-                "spectral/engineering",
-                "sensor characteristics",
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
-            "identifier": "C2107120625-NSIDC_ECS",
             "description": "This data set contains geolocation information of the infrastructure locations for the SnowEx20 Intensive Observation Period (IOP) and Time Series (TS) campaigns. Available scientific infrastructure locations in this data set are tower and sensor locations, aircraft flight lines, planned and actual snow pit locations, and time-lapse camera locations. Additionally, this data set contains areal snow depth and tree density classification matrix over the Grand Mesa, CO study area.",
-            "title": "SnowEx20 Grand Mesa Reference GIS Data Sets V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYDZXY4Q79VIJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYDZXY4Q79VIJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GIS_REF.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GIS_REF.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GIS_REF/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GIS_REF/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GIS_REF+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GIS_REF+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GIS_REF.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GIS_REF.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GIS_REF/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GIS_REF/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GIS_REF+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GIS_REF+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YDZXY4Q79VIJ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/YDZXY4Q79VIJ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YDZXY4Q79VIJ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/YDZXY4Q79VIJ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2107120625-NSIDC_ECS",
+            "issued": "2019-09-21",
+            "keyword": [
+                "spectral/engineering",
+                "sensor characteristics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/YDZXY4Q79VIJ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.225 38.993 -107.863 39.125",
+            "temporal": "2019-09-21T00:00:00Z/2020-02-14T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Grand Mesa Reference GIS Data Sets V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3817-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-11T07:10:40.000 to 2015-09-11T07:34:32.949.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3817-v1.0_wnzw-t58s",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3817-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3817-v1.0_wnzw-t58s",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-11T07:10:40.000 to 2015-09-11T07:34:32.949.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3817 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3817 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NVAP-M/NVAP_CLIMATE_LAYERED-PRECIPITABLE-WATER_L3.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2013-07-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NVAP-M/NVAP_CLIMATE_LAYERED-PRECIPITABLE-WATER_L3.001.",
-            "issued": "2013-10-30",
-            "temporal": "1988-01-01T00:00:00Z/2009-12-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "atmospheric water vapor",
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
-            "identifier": "C1595664379-LARC_ASDC",
             "description": "NVAP_CLIMATE_Layered-Precipitable-Water data set is designed to provide the most stable water vapor data set over time for use in climate applications. NVAP-M Climate only includes data from stable instruments that have undergone intercalibration efforts to ensure consistency between data from the same instrument flying on multiple satellite platforms.The new NVAP data sets are produced under the NASA Making Earth Science Data Records for Use in Research Environments (MEaSUREs) program and is named NVAP-M. It supersedes the previous NVAP data set. NVAP-M continues the legacy of providing high-quality, model-independent global estimates of total column and layered water vapor. The use of improved, intercalibrated data sets and algorithms that were not available for the heritage NVAP data set results in an improved and extended water vapor data set that is stable enough for climate research and of a resolution appropriate for studies on smaller spatial and temporal scales. The true value of NVAP-M will be seen in outcomes from applied and research users of the data set in various fields. Some initial NVAP-M findings are presented in Vonder Haar et al. (2012). In addition to the time-dependent artifacts present in the previous NVAP data set, a wealth of new data has become available since the last NVAP processing in 2003. These include an additional SSM/I instrument, additional NOAA satellites, the NASA Earth Observing System (EOS)-Aqua Satellite, which carries the Atmospheric Infrared Sounder (AIRS), as well as water vapor information from Global Positioning System (GPS) satellites. This extension and reprocessing effort increases the temporal coverage from 14 to 22 (1988-2009) years, making the data set more useful and consistent for investigation of the long-term trends which are hypothesized to occur as Earth warms. In addition to the long-standing daily, 1-degree gridded Total Precipitable Water (TPW) and layered Precipitable Water (PW) products, NVAP-M includes additional products geared towards different scientific needs. Three separate processing streams produced products directed towards specific research goals. These are NVAP-M Climate, designed to provide the most stable water vapor data set over time for use in climate applications, and NVAP-M Weather, designed to provide higher spatial and temporal resolution products for use in studies on shorter time scales as well as weather case studies. Additionally, an ocean-only (NVAP-M Ocean) version includes only data from the SSM/I and is intended to mirror other available SSM/I-only water vapor data sets.",
-            "title": "NASA Water Vapor Project MEaSUREs (NVAP-M) CLIMATE Layered Precipitable Water",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNVAP-M%2FNVAP_CLIMATE_LAYERED-PRECIPITABLE-WATER_L3.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNVAP-M%2FNVAP_CLIMATE_LAYERED-PRECIPITABLE-WATER_L3.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/NVAP-M",
-                    "description": "ASDC Data and Information for NVAP-M",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for NVAP-M",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/NVAP-M",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NVAP-M/NVAP_CLIMATE_LAYERED-PRECIPITABLE-WATER_L3.001",
-                    "description": "DOI data set landing page for NVAP_CLIMATE_Layered-Precipitable-Water_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NVAP_CLIMATE_Layered-Precipitable-Water_1",
+                    "downloadURL": "https://doi.org/10.5067/NVAP-M/NVAP_CLIMATE_LAYERED-PRECIPITABLE-WATER_L3.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1595664379-LARC_ASDC",
-                    "description": "Earthdata Search for NVAP_CLIMATE_Layered-Precipitable-Water_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NVAP_CLIMATE_Layered-Precipitable-Water_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1595664379-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/read_software/read_nvapm.pro.txt",
-                    "description": "Readme to open and read NVAP-M data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to open and read NVAP-M data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/read_software/read_nvapm.pro.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/guide/NVAPM_User_Guide.pdf",
-                    "description": "NVAP-MEaSUREs (NVAP-M) ReadMe",
                     "@type": "dcat:Distribution",
+                    "description": "NVAP-MEaSUREs (NVAP-M) ReadMe",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/guide/NVAPM_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/NVAP_M_ATBD_Feb2013.pdf",
-                    "description": "NASA Water Vapor Project \u2013 MEaSUREs (NVAP-M) Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Water Vapor Project \u2013 MEaSUREs (NVAP-M) Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/NVAP_M_ATBD_Feb2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NVAP-M/NVAP-M_Climate/NVAP_CLIMATE_Layered-Precipitable-Water/",
-                    "description": "ASDC Direct Data Download for NVAP_CLIMATE_Layered-Precipitable-Water_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NVAP_CLIMATE_Layered-Precipitable-Water_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NVAP-M/NVAP-M_Climate/NVAP_CLIMATE_Layered-Precipitable-Water/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/NVAP-M/NVAP-M_Climate/NVAP_CLIMATE_Layered-Precipitable-Water/contents.html",
-                    "description": "OPeNDAP data access for NVAP_CLIMATE_Layered-Precipitable-Water_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for NVAP_CLIMATE_Layered-Precipitable-Water_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/NVAP-M/NVAP-M_Climate/NVAP_CLIMATE_Layered-Precipitable-Water/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1595664379-LARC_ASDC",
+            "issued": "2013-10-30",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NVAP-M/NVAP_CLIMATE_LAYERED-PRECIPITABLE-WATER_L3.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -179.9 -90.0 180.0 90.0 180.0 90.0 -179.9 -90.0 -179.9</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1988-01-01T00:00:00Z/2009-12-01T23:59:59.999Z",
             "theme": [
                 "NVAP-M",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NASA Water Vapor Project MEaSUREs (NVAP-M) CLIMATE Layered Precipitable Water"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWTPR-CTD01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SWOT pre-launch field campaign. 2022-05-31. GPS sea surface height, Conductivity, Temperature and Depth (CTD) data from the 2019-2020 SWOT pre-launch field campaign. Version 1.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWTPR-CTD01. https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf .",
-            "issued": "2022-03-02",
-            "temporal": "2019-09-05T00:00:00Z/2020-01-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-18",
-            "references": [
-                "https://doi.org/10.1175/jtech-d-21-0039.1"
-            ],
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
-                "ocean pressure",
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
-            "identifier": "C2229635779-POCLOUD",
-            "description": "This dataset provides the conductivity, temperature and depth (CTD) measurements from the fixed-depth CTD sensors mounted on a full-depth mooring deployed by the SWOT prelaunch field campaign. The campaign was designed to test the performance of several instruments/platforms in meeting the SWOT Calibration/Validation (CalVal) requirement. It was conducted near the SWOT CalVal crossover location, about 300 kilometers west of Monterey, California between September, 2019 and January, 2020. These fixed-depth CTDs are below 500 m while the upper part of the mooring has a WireWalker (WW) profiler. The CTD data from WW is available here https://doi.org/10.5067/SWTPR-WW001. The campaign also deployed another two CTD moorings, a slocum glider, one bottom pressure recorder and one Pressure Inverted Echo Sounder. Details can be found in the user guide and the journal reference given in the documentation section.",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SWOT pre-launch field campaign",
-            "title": "SWOT 2019-2020 Prelaunch Oceanography Field Campaign SIO Moored Fixed-Depth CTDs",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_SIOCTD_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides the conductivity, temperature and depth (CTD) measurements from the fixed-depth CTD sensors mounted on a full-depth mooring deployed by the SWOT prelaunch field campaign. The campaign was designed to test the performance of several instruments/platforms in meeting the SWOT Calibration/Validation (CalVal) requirement. It was conducted near the SWOT CalVal crossover location, about 300 kilometers west of Monterey, California between September, 2019 and January, 2020. These fixed-depth CTDs are below 500 m while the upper part of the mooring has a WireWalker (WW) profiler. The CTD data from WW is available here https://doi.org/10.5067/SWTPR-WW001. The campaign also deployed another two CTD moorings, a slocum glider, one bottom pressure recorder and one Pressure Inverted Echo Sounder. Details can be found in the user guide and the journal reference given in the documentation section.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWTPR-CTD01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWTPR-CTD01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/swot",
-                    "description": "Field Campaign and Instrument Overview for SWOT",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview for SWOT",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/swot",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_SIOCTD_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_SIOCTD_V1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2229635779-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2229635779-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2229635779-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2229635779-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_SIOCTD_V1.jpg",
+            "identifier": "C2229635779-POCLOUD",
+            "issued": "2022-03-02",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "ocean pressure",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWTPR-CTD01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-01-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1175/jtech-d-21-0039.1"
+            ],
             "spatial": "-125.2 35.8 -125.0 36.2",
+            "temporal": "2019-09-05T00:00:00Z/2020-01-18T23:59:59.999Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT 2019-2020 Prelaunch Oceanography Field Campaign SIO Moored Fixed-Depth CTDs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1063",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Asner, G.P., M.W. Palace, M.M. Keller, M. Pereira, J. Silva, and J.C. Zweede. 2012. LBA-ECO TG-07 Tree Geometry in an Undisturbed Forest in Cauaxi, Para, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1063",
-            "issued": "2023-10-03",
-            "temporal": "2000-06-10T00:00:00Z/2000-06-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-09",
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
-            "identifier": "C2779742959-ORNL_CLOUD",
             "description": "Canopy measurements in an undisturbed eastern Amazon forest (Cauxi, Para, Brazil. See Figure 1) were derived from a one-time event in 2000 using a hand-held laser range finder, and diameter at breast height (DBH) was determined manually. Parameters reported include: Crown Width, Crown Depth, Tree Height, and DBH. There is one comma-delimited ASCII data file with this data set. In addition, these manually derived measurements were compared to the IKONOS satellite data of crown dimensions that were acquired on 2 November 2000, from an orbital altitude of 680 km. The data from a 600 x 600 m block of undisturbed forest, including the 50 ha area surveyed in the field, were analyzed in a combined image processing and geographic information system environment.DATA QUALITY STATEMENT: The Data Center has determined that there are questions about the quality of the data reported in this data set. The data set has missing or incomplete data, metadata, or other documentation that diminishes the usability of the products. KNOWN PROBLEMS: Only the general location for this study was identified -- Cauaxi, Para, Brazil. The tree measurement data are of limited use because coordinates for the study site, coordinates of the beginning and end of the transects, and coordinates of the measured trees were not provided. Also, the area that the IKONOS image captured was not provided and the IKONOS image is not available due to restricted distribution.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO TG-07 Tree Geometry in an Undisturbed Forest in Cauaxi, Para, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1063",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1063",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/grab_bag/TG07_DBH_Cauaxi/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/grab_bag/TG07_DBH_Cauaxi/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/TG07_DBH_Cauaxi.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/TG07_DBH_Cauaxi.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1063",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1063",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/grab_bag/TG07_DBH_Cauaxi/comp/TG07_DBH_Cauaxi.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/grab_bag/TG07_DBH_Cauaxi/comp/TG07_DBH_Cauaxi.pdf",
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
+            "identifier": "C2779742959-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1063",
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
             "spatial": "-3.73 -48.29",
+            "temporal": "2000-06-10T00:00:00Z/2000-06-22T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO TG-07 Tree Geometry in an Undisturbed Forest in Cauaxi, Para, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/DROJ79M0DGES",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 QuikSCAT/SeaWinds Backscatter Data, Alabama, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/DROJ79M0DGES.",
-            "issued": "2003-05-01",
-            "temporal": "2003-05-01T00:00:00Z/2003-08-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-08-31",
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
-                "radar",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Long",
                 "hasEmail": "mailto:long@et.byu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386204323-NSIDCV0",
             "description": "This data set includes data collected over the Soil Moisture Experiment 2003 (SMEX03) areas of Alabama, Georgia, and Oklahoma, USA, and Brazil. The SeaWinds scatterometer on NASA's Quick Scatterometer (QuikSCAT) satellite collected backscatter data.",
-            "title": "SMEX03 QuikSCAT/SeaWinds Backscatter Data, Alabama, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDROJ79M0DGES",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDROJ79M0DGES",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/QUIKSCAT/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/QUIKSCAT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/QUIKSCAT/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/QUIKSCAT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/QUIKSCAT/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/QUIKSCAT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/QUIKSCAT/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/QUIKSCAT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DROJ79M0DGES",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/DROJ79M0DGES",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DROJ79M0DGES",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/DROJ79M0DGES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204323-NSIDCV0",
+            "issued": "2003-05-01",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/DROJ79M0DGES",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-90.0 28.0 -80.0 38.0",
+            "temporal": "2003-05-01T00:00:00Z/2003-08-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 QuikSCAT/SeaWinds Backscatter Data, Alabama, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIANCARP_ANCILLARY.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2009-04-08. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MISR/MIANCARP_ANCILLARY.002. http://eosweb.larc.nasa.gov/project/misr/misr_table.",
-            "issued": "2000-11-10",
-            "temporal": "1999-12-28T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "sensor characteristics"
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
-            "identifier": "C179031521-LARC",
             "description": "MIANCARP_2 is the Multi-angle Imaging SpectroRadiometer (MISR) Ancillary Radiometric Product version 2. It is composed of 4 files covering instrument characterization data, pre-flight calibration data, in-flight calibration data, and configuration parameters. The MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward, and four cameras pointing aftward. It takes seven minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally Gaussian, centered at 443, 555, 670, and 865 nm.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Ancillary Radiometric Product V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIANCARP_ANCILLARY.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIANCARP_ANCILLARY.002",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MIANCARP_ANCILLARY.002",
-                    "description": "DOI data set landing page for MIANCARP_2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MIANCARP_2",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MIANCARP_ANCILLARY.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031521-LARC",
-                    "description": "Earthdata Search for MIANCARP_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MIANCARP_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031521-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MIANCARP.002/contents.html",
-                    "description": "OPeNDAP data access for MIANCARP_2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MIANCARP_2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MIANCARP.002/contents.html",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/RadCal.pdf",
-                    "description": "Quality of MISR Radiometric Calibration June13, 201",
                     "@type": "dcat:Distribution",
+                    "description": "Quality of MISR Radiometric Calibration June13, 201",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/RadCal.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's calibration documentation"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MIANCARP.002/",
-                    "description": "ASDC Direct Data Download for MIANCARP_2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MIANCARP_2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MIANCARP.002/",
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
+            "identifier": "C179031521-LARC",
+            "issued": "2000-11-10",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "sensor characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIANCARP_ANCILLARY.002",
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
+            "temporal": "1999-12-28T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Ancillary Radiometric Product V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206850-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Borehole and environmental protection descriptive and numerical data, Yamal Peninsula, Russia, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1977-01-01",
-            "temporal": "1977-01-01T00:00:00Z/1990-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1990-12-31",
-            "keyword": [
-                "landscape",
-                "snow/ice",
-                "frozen ground",
-                "soils",
-                "vegetation",
-                "agriculture",
-                "cryosphere",
-                "earth science",
-                "biosphere",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Minkin",
                 "hasEmail": "mailto:fund@fundamnt.ru"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206850-NSIDCV0",
             "description": "This database of selected borehole records from the Yamal Peninsula, Russia, contains environmental descriptions (textual and numerical) of the units on the index map, and relevant borehole data. The Index Map of Yamal Peninsula (VSEGINGEO-Earth Cryosphere Institute SB RAS; PI -  Prof.E.S.Melnikov) was originally compiled at a scale of 1 to 1,000,000, as 'The Map of Natural Complexes of West Siberia for the Purpose of Geocryological Prediction and Planning of Nature-Protection Measures for the Mass Construction, 1 to 1 mln' (1991) by E.S.Melnikov and N.G.Moskalenko (eds.). It was taken as a base map for nature-protection regionalization. Environmental 'regions', 'sub-regions', 'landscapes' and localities' shown on a landscape map are merged into the nature-protection regions. The map was compiled by interpreting more than 1000 satellite images and aerial photos as well as from analysis of field data from several institutions. Dominating components of the landscape, composition of the surface deposits, geocryological conditions and natural protection of ground water were considered while distinguishing the Nature-Protection Regions within the limits of Environmental Regions (Melnikov, 1988). The map is supplied with relevant databases, containing the following information - number of regions and landscape type; category of resiliency; category of the ground water protection; vegetation type; geological and geocryological structure to the depth of 10-15 m; ice content (of lenses and of macro-inclusions separately); thickness of seasonally frozen and seasonally thawed layers; ground temperature; contemporary exogenic geological (periglacial) processes; and the area affected by these processes.\n\nThe 55 nature-protection regions of Yamal Peninsula generalize information. To approve the ranges of geocryological and cryolithological characteristics, 160 boreholes were retrieved out of the database containing more than 4000 boreholes data obtained in 1977-1990 by Fundamentproekt Design Institute (Moscow, Russia; PI - Dr.sci.M.A.Minkin) at Kharasavey and Bovanenkovo gas fields and along the pipelines Yamal-Ukhta and Yamal-Uzhgorod. The boreholes have reference to geographical coordinates (latitude and longitude), as well as to the nature-protection region numbers shown on the Index Map. A total of 21 units are covered by borehole data, 5-8 boreholes in each unit, covering most typical conditions\n\nThe original database consisted of 3 relational tables. The first table includes category of resiliency; locality type description; landscape type description; ground-ice content, water saturation, cryogenic structure, macro-ground-ice content; vegetation types; seasonally frozen and seasonally thawed layer depths; ground temperature at 10 m; exogenic geological\n processes an their paragenesis and combinations; and degree of the surface disturbance. The second relational table contains layer-by-layer description of the lithological section types. The third table for the boreholes includes the description of topography around the borehole; types of geological profiles through the active layer and depths down to the permafrost table; ground temperature at 10-m depth (close to the depth of zero annual amplitude in the area); macro-ice content; and salinity of permafrost. These data are presented on the CAPS Version 1.0 CD-ROM, June 1998.",
-            "title": "Borehole and environmental protection descriptive and numerical data, Yamal Peninsula, Russia, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD402_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD402_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD402/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD402/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD402/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD402/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206850-NSIDCV0",
+            "issued": "1977-01-01",
+            "keyword": [
+                "landscape",
+                "snow/ice",
+                "frozen ground",
+                "soils",
+                "vegetation",
+                "agriculture",
+                "cryosphere",
+                "earth science",
+                "biosphere",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206850-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1990-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "65.5 66.0 74.0 72.5",
+            "temporal": "1977-01-01T00:00:00Z/1990-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Borehole and environmental protection descriptive and numerical data, Yamal Peninsula, Russia, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3MRD_L3.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Radiance Product for a month;See ProductionDateTime for Published date.",
-            "issued": "2003-12-03",
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
-            "identifier": "C43677725-LARC",
             "description": "This file contains the MISR Level 3 Component Global Radiance Product covering a month",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Component Global Radiance Product covering a month V005",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3MRD_L3.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3MRD_L3.005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C43677725-LARC",
+            "issued": "2003-12-03",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3MRD_L3.005",
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
+            "title": "MISR Level 3 Component Global Radiance Product covering a month V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/LMOS/Ground_Grafton_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/LMOS/Ground_Grafton_Data_1. https://asdc.larc.nasa.gov/project/SEAC4RS.",
-            "issued": "2020-09-08",
-            "temporal": "2017-05-10T00:00:00Z/2017-06-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-02",
-            "keyword": [
-                "earth science",
-                "air quality",
-                "atmosphere",
-                "atmospheric chemistry"
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
-            "identifier": "C1966365966-LARC_ASDC",
             "description": "LMOS_Ground_Grafton_Data_1 is the Lake Michigan Ozone Study (LMOS) Grafton ground site data collected during the LMOS field campaign. This product is a result of a joint effort across multiple agencies, including NASA, NOAA, the EPA, Electric Power Research Institute (EPRI), National Science Foundation (NSF), Lake Michigan Air Directors Consortium (LADCO) and its member states, and several research groups at universities. Data collection is complete.\r\rElevated spring and summertime ozone levels remain a challenge along the coast of Lake Michigan, with a number of monitors exceeding the 2015 National Ambient Air Quality Standards (NAAQS) for ozone. The production of ozone over Lake Michigan, combined with onshore daytime \u201clake breeze\u201d airflow is believed to increase ozone concentrations at locations within a few kilometers off shore. This observed lake-shore gradient motivated the Lake Michigan Ozone Study (LMOS). Conducted from May through June 2017, the goal of LMOS was to better understand ozone formation and transport around Lake Michigan; in particular, why ozone concentrations are generally highest along the lakeshore and drop off sharply inland and why ozone concentrations peak in rural areas far from major emission sources. LMOS was a collaborative, multi-agency field study that provided extensive observational air quality and meteorology datasets through a combination of airborne, ship, mobile laboratories, and fixed ground-based observational platforms. Chemical transport models (CTMs) and meteorological forecast tools assisted in planning for day-to-day measurement strategies. The long term goals of the LMOS field study were to improve modeled ozone forecasts for this region, better understand ozone formation and transport around Lake Michigan, provide a better understanding of the lakeshore gradient in ozone concentrations (which could influence how the Environmental Protection Agency (EPA) addresses future regional ozone issues), and provide improved knowledge of how emissions influence ozone formation in the region.",
-            "title": "LMOS Grafton Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLMOS%2FGround_Grafton_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLMOS%2FGround_Grafton_Data_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LMOS",
-                    "description": "ASDC Data and Information for LMOS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for LMOS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LMOS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/LMOS_FAQ_rev_jun5.pdf",
-                    "description": "Lake Michigan Ozone Study (LMOS 2017) FAQ",
                     "@type": "dcat:Distribution",
+                    "description": "Lake Michigan Ozone Study (LMOS 2017) FAQ",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/LMOS_FAQ_rev_jun5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/Great_Lakes_Ozone_Study_White_Paper_Draft_v6.pdf",
-                    "description": "White Paper: Lake Michigan Ozone Study 2017 (LMOS 2017)",
                     "@type": "dcat:Distribution",
+                    "description": "White Paper: Lake Michigan Ozone Study 2017 (LMOS 2017)",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/Great_Lakes_Ozone_Study_White_Paper_Draft_v6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/",
-                    "description": "LMOS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Suborbital/LMOS/Ground_Grafton_Data_1",
-                    "description": "DOI data set landing page for LMOS_Ground_Grafton_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for LMOS_Ground_Grafton_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Suborbital/LMOS/Ground_Grafton_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1966365966-LARC_ASDC",
-                    "description": "Earthdata Search for LMOS_Ground_Grafton_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LMOS_Ground_Grafton_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1966365966-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LMOS/Ground_Grafton_Data_1/",
-                    "description": "ASDC Direct Data Download for LMOS_Ground_Grafton_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LMOS_Ground_Grafton_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LMOS/Ground_Grafton_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1966365966-LARC_ASDC",
+            "issued": "2020-09-08",
+            "keyword": [
+                "earth science",
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/LMOS/Ground_Grafton_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-11-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-90.0 40.0 -85.0 45.0",
+            "temporal": "2017-05-10T00:00:00Z/2017-06-21T23:59:59Z",
             "theme": [
                 "LMOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LMOS Grafton Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0011",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0011.",
-            "issued": "1999-11-01",
-            "temporal": "1992-05-31T00:00:00Z/1992-07-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-05",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LAURENCE EYMARD",
                 "hasEmail": "mailto:laurence.eymard@cetp.ipsl.fr"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001000-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.These files are the calculated downward longwave flux at the surface derived from METEOSAT observations. The file naming convention is: raDDMMYYsxx.fis_tmpwhere DDMMYY is the date and xx = slot numberMean time (UT) is obtained from the slot number overthe ASTEX region by the formula: UT = (xx/2) - 0.17These files are: I2 pixels, 188 pixels/row, 163 rows. Each pixel has a spatial resolution of 0.08 degrees.The units of flux are Wm^-2.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) Centre Meteorologie Spatiale (CMS) Longwave Flux Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0011",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0011",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001000-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_CMS_LWFLUX_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_CMS_LWFLUX_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001000-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_ax_cms_cloud.c",
-                    "description": "Project Level/Data Set Level Read Software for SUN, HP, SGI, and Dec Alpha Platforms - Direct File Download (.c), HP, SGI, and Dec Alpha Platforms - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Project Level/Data Set Level Read Software for SUN, HP, SGI, and Dec Alpha Platforms - Direct File Download (.c), HP, SGI, and Dec Alpha Platforms - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_ax_cms_cloud.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fax",
-                    "description": "Makefile.fci1 Release: 1.1 Date: 7/29/94",
                     "@type": "dcat:Distribution",
+                    "description": "Makefile.fci1 Release: 1.1 Date: 7/29/94",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fax",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_cms_lwflux_info.txt",
-                    "description": "CMS Statement on satellite-based series of images as part of ASTEX Readme",
                     "@type": "dcat:Distribution",
+                    "description": "CMS Statement on satellite-based series of images as part of ASTEX Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_cms_lwflux_info.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_cms_lwflux.txt",
-                    "description": "Readme Information about the FIRE ASTEX Centre de Meteorologie Spatiale (CMS) Longwave Flux",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the FIRE ASTEX Centre de Meteorologie Spatiale (CMS) Longwave Flux",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_cms_lwflux.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0011",
-                    "description": "DOI data set landing page for FIRE_AX_CMS_LWFLUX_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_CMS_LWFLUX_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0011",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_cms_dataset.pdf",
-                    "description": "FIRE ASTEX Centre de Meteorologie Spatiale (CMS) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Centre de Meteorologie Spatiale (CMS) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_cms_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/FIRE",
-                    "description": "ASDC Data and Information for FIRE",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for FIRE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/FIRE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_CMS_LWFLUX/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_CMS_LWFLUX_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_CMS_LWFLUX_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_CMS_LWFLUX/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_CMS_LWFLUX/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_CMS_LWFLUX_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_CMS_LWFLUX_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_CMS_LWFLUX/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001000-LARC_ASDC",
+            "issued": "1999-11-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0011",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>27.03 -29.97 27.03 -15.01 39.99 -15.01 39.99 -29.97 27.03 -29.97</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-05-31T00:00:00Z/1992-07-02T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) Centre Meteorologie Spatiale (CMS) Longwave Flux Data"
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
+            "description": "These images display several of Saturn's moons approved by the International Astronomical Union (IAU).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/mimas_comp.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-185",
             "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "usgs",
                 "dione",
@@ -1585931,398 +1585943,398 @@
                 "mimas",
                 "janus"
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
-            "identifier": "OCIO-Fitara-185",
-            "description": "These images display several of Saturn's moons approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Saturnian System: Mimas",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/mimas_comp.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Saturnian System: Mimas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-02_L1B-003.02",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2011-12-13. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-02_L1B-003.02. https://asdc.larc.nasa.gov/project/CALIPSO.",
-            "issued": "2014-04-22",
-            "temporal": "2008-01-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-02",
-            "keyword": [
-                "atmosphere",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths",
-                "earth science",
-                "atmospheric radiation",
-                "aerosols"
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
-            "identifier": "C7441430-LARC_ASDC",
             "description": "CAL_WFC_L1_IIR-ValStage1-V3-02 data are Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) Wide Field Camera (WFC) Level 1B 1 km Registered Science data, Validated Stage 1 Version 3-02. Data collection for this product is ongoing. Version 3.02 represents a transition of the Lidar, Imaging Infrared Radiometer (IIR), and WFC processing and browse code to a new cluster computing system. No algorithm changes were introduced, and very minor changes were observed between V3.01 and V3.02 as a result of the compiler and computer architecture differences. The primary WFC Level 1B data products are calibrated radiance and bidirectional reflectance registered to an Earth-based grid centered on the Lidar ground track. During the normal operation, the WFC acquires science data only during the daylight portions of the CALIPSO orbits. The WFC Level 1B 1 IIR Registered Science grid provides WFC data on the identical grid as the CALIPSO IIR data and is produced to facilitate the use of the WFC data in the IIR retrievals. CALIPSO was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite is comprised of three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the WFC. CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Wide Field Camera Level 1B 1 km Registered Science data, Validated Stage 1 V3-02",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWFC%2FCALIPSO%2FCAL_WFC_L1_IIR-VALSTAGE1-V3-02_L1B-003.02",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWFC%2FCALIPSO%2FCAL_WFC_L1_IIR-VALSTAGE1-V3-02_L1B-003.02",
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
-                    "downloadURL": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-02_L1B-003.02",
-                    "description": "DOI data set landing page for CAL_WFC_L1_IIR-ValStage1-V3-02_V3-02",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_WFC_L1_IIR-ValStage1-V3-02_V3-02",
+                    "downloadURL": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-02_L1B-003.02",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7441430-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_WFC_L1_IIR-ValStage1-V3-02_V3-02 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_WFC_L1_IIR-ValStage1-V3-02_V3-02 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7441430-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/WFC_L1_IIR-ValStage1-V3-02/contents.html",
-                    "description": "OPeNDAP data access for CAL_WFC_L1_IIR-ValStage1-V3-02_V3-02",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_WFC_L1_IIR-ValStage1-V3-02_V3-02",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/WFC_L1_IIR-ValStage1-V3-02/contents.html",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/quality_summaries/WFC_L1BScansProducts_3-01_v02.pdf",
-                    "description": "CALIPSO Quality Statement: Wide Field Camera Level 1B Scans Data Release Versions: 3.01, 3.02",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Quality Statement: Wide Field Camera Level 1B Scans Data Release Versions: 3.01, 3.02",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/quality_summaries/WFC_L1BScansProducts_3-01_v02.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/WFC_L1_IIR-ValStage1-V3-02/",
-                    "description": "ASDC Direct Data Download for CAL_WFC_L1_IIR-ValStage1-V3-02_V3-02",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_WFC_L1_IIR-ValStage1-V3-02_V3-02",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/WFC_L1_IIR-ValStage1-V3-02/",
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
+            "identifier": "C7441430-LARC_ASDC",
+            "issued": "2014-04-22",
+            "keyword": [
+                "atmosphere",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science",
+                "atmospheric radiation",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-02_L1B-003.02",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2008-01-18T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Wide Field Camera Level 1B 1 km Registered Science data, Validated Stage 1 V3-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_AircraftRemoteSensing_DC8_HSRL_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_AircraftRemoteSensing_DC8_HSRL_Data_1.",
-            "issued": "2022-08-31",
-            "temporal": "1999-11-16T00:00:00Z/2000-03-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-31",
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Hostetler",
                 "hasEmail": "mailto:chris.a.hostetler@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836796-LARC_ASDC",
             "description": "SOLVE1_AircraftRemoteSensing_DC8_HSRL_Data is the remotely sensed trace gas data for the DC-8 aircraft collected during the SAGE III Ozone Loss and Validation Experiment (SOLVE) by the High Spectral Resolution Lidar (HSRL). Data collection for this product is complete.\r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE I DC-8 Aircraft High Spectral Resolution Lidar (HSRL) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_AircraftRemoteSensing_DC8_HSRL_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_AircraftRemoteSensing_DC8_HSRL_Data_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/AircraftRemoteSensing_DC8_HSRL_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE1_AircraftRemoteSensing_DC8_HSRL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE1_AircraftRemoteSensing_DC8_HSRL_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/AircraftRemoteSensing_DC8_HSRL_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836796-LARC_ASDC",
+            "issued": "2022-08-31",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_AircraftRemoteSensing_DC8_HSRL_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>12.0 -122.5 12.0 126.1 89.5 126.1 89.5 -122.5 12.0 -122.5</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1999-11-16T00:00:00Z/2000-03-15T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE I DC-8 Aircraft High Spectral Resolution Lidar (HSRL) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214473624-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SMAP Level 1C Sigma Naught High Res Product Metadata",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1214473624-ASF",
             "issued": "2015-07-31",
-            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-24",
             "keyword": [
                 "platform characteristics",
                 "land surface",
@@ -1586331,286 +1586343,286 @@
                 "soils",
                 "radar"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214473624-ASF.html",
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
-            "identifier": "C1214473624-ASF",
-            "description": "SMAP Level 1C Sigma Naught High Res Product Metadata",
-            "title": "SMAP_L1C_SIGMA_NAUGHT_HIGH_RES_METADATA_V001",
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
+            "title": "SMAP_L1C_SIGMA_NAUGHT_HIGH_RES_METADATA_V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1179",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wei, Y., D.J. Hayes, M.M. Thornton, W.M. Post, R.B. Cook, P.E. Thornton, A.R. Jacobson, D.N. Huntzinger, T.O. West, L.S. Heath, K. McKain, G. Stinson, W. Kurz, B. de Jong, I.T. Baker, J.M. Chen, F. Chevallier, F.M. Hoffman, A.K. Jain, R. Lokupitiya, D.A. McGuire, A.M. Michalak, G.G. Moisen, R.P. Neilson, P. Peylin, C.S. Potter, B. Poulter, D. Price, J.T. Randerson, C. Rodenbeck, H. Tian, E. Tomelleri, G.R. van der Werf, N. Viovy, J. Xiao, N. Zeng, and M. Zhao. 2013. NACP Regional: National Greenhouse Gas Inventories and Aggregated Gridded Model Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1179",
-            "issued": "2022-11-21",
-            "temporal": "2000-01-01T00:00:00Z/2007-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "vegetation",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
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
-            "identifier": "C2539942542-ORNL_CLOUD",
             "description": "This data set provides two products that were derived from the recently published North American Carbon Program (NACP) Regional Synthesis 1-degree terrestrial biosphere model (TBM) and inverse model (IM) outputs (Gridded 1-deg Observation Data and Biosphere and Inverse Model Outputs, Wei et al., 2013). The first product is the aggregation of the standardized gridded 1-degree TBM and IM outputs to the Greenhouse Gas (GHG) inventory zones as defined for North America (United States, Canada, and Mexico). Depending on the data availability, the monthly/yearly Net Ecosystem Exchange (NEE), Net Primary Production (NPP), Total Vegetation Carbon (VegC), Heterotrophic Respiration (Rh), and Fire Emissions (FE) outputs from the 22 TBM and 7 IM models were aggregated from the 1-degree resolution gridded format to the inventory zones and then, further divided into Forest Lands, Crop Lands, and Other Lands sectors within each inventory zone based on the 1-km resolution GLC2000 land cover map (GLC2000, 2003).The second product is the North American national GHG inventories on the scale of inventory zones which contain estimated land-atmosphere exchange of CO2 (NEE) in forest lands, crop lands, and other lands sectors. NEE estimates were synthesized from inventory-based data on productivity, ecosystem carbon stock change, and harvested product stock change, and additional information from national-level GHG inventories of the United States, Canada, and Mexico including EPA (2011) and Environment Canada (2011).An additional summary file of annual mean NEE (2000-2006)is provided for both land sectors and reporting zones in North America and was created by combining the aggregated model output and the national GHG database and is provided. The aggregated monthly and yearly model output data and the national GHG inventories data are available in comma separated value (*.csv) format files. Also provided are detailed inventory zone spatial data as an ESRI Shapefile. Included are zone names, boundaries, and zone and land cover type area attributes. For mapping convenience, the inventory zones shapefile was merged with 1-km forest, crop, and other lands masks to create a 1-km resolution reference data file that was converted to GeoTIFF format. The GeoTIFF defines to which inventory zone and land cover type each 1-km grid cell belongs.This document provides detailed information about the content, format, and processing procedures of these two data products. Detailed descriptions of the TBMs and IMs can be found in a separate companion document: NACP Regional Synthesis - Description of Observations and Models.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NACP Regional: National Greenhouse Gas Inventories and Aggregated Gridded Model Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1179",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1179",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_Regional_Model_GHG_Aggr/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_Regional_Model_GHG_Aggr/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_Regional_Model_GHG_Aggr.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_Regional_Model_GHG_Aggr.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1179",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1179",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/NACP_Model_Characteristics.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/NACP_Model_Characteristics.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/NACP_Model_Metadata_Survey_Results.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/NACP_Model_Metadata_Survey_Results.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/NACP_Regional_Model_GHG_Aggr.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/NACP_Regional_Model_GHG_Aggr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/Regional-Description_of_Observations_and_Models.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/Regional-Description_of_Observations_and_Models.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/Regional-Standardized_Inventory_Zones.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Model_GHG_Aggr/comp/Regional-Standardized_Inventory_Zones.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
+            "identifier": "C2539942542-ORNL_CLOUD",
+            "issued": "2022-11-21",
+            "keyword": [
+                "vegetation",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1179",
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
             "spatial": "-170.0 10.0 -50.0 84.0",
+            "temporal": "2000-01-01T00:00:00Z/2007-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP Regional: National Greenhouse Gas Inventories and Aggregated Gridded Model Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EMIT/EMITL3ASA.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Robert Green. 2023-09-28. EMITL3ASA.001. EMIT L3 Aggregated Mineral Spectral Abundance and Uncertainty 0.5 Deg V001. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/EMIT/EMITL3ASA.001. https://doi.org/10.5067/EMIT/EMITL3ASA.001. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2023-09-28",
-            "temporal": "2022-08-10T00:00:00Z/2023-07-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-28",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "soils"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Green",
                 "hasEmail": "mailto:robert.o.green@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2408752948-LPCLOUD",
-            "description": "The Earth Surface Mineral Dust Source Investigation (EMIT) instrument measures surface mineralogy, targeting the Earth\u2019s arid dust source regions. EMIT is installed on the International Space Station (ISS) and uses imaging spectroscopy to take measurements of the sunlit regions of interest between 52\u00b0 N latitude and 52\u00b0 S latitude. An interactive map showing the regions being investigated, current and forecasted data coverage, and additional data resources can be found on the VSWIR Imaging Spectroscopy Interface for Open Science (VISIONS) EMIT Open Data Portal.\r\nThe EMIT Level 3 Aggregated Mineral Spectral Abundance and Uncertainty (EMITL3ASA) Version 1 data product provides an aggregated mineral spectral abundance of the 10 minerals that are the focus of the EMIT mission. These minerals, referred to as the EMIT-10 minerals, are calcite, chlorite, dolomite, goethite, gypsum, hematite, illite+muscovite, kaolinite, montmorillonite, and vermiculite. The EMITL3ASA granule consists of one network Common Data Format 4 (netCDF-4) file at a spatial resolution of 0.5 degrees. The data in EMITL3ASA relies heavily on the EMIT L2B Estimated Mineral Identification and Band Depth and Uncertainty (EMITL2BMIN) data. Using the EMITL2BMIN data, aggregated spectral abundance (ASA) is calculated for each of the EMIT-10 minerals as the simple average of relevant 60 m pixels within each 0.5 degree grid cell in the EMITL3ASA product, after controlling for the estimated fractional cover of bare soil within the pixel. \r\nThe EMITL3ASA data product contains 20 Science Dataset (SDS) layers. There are two layers for each of the EMIT-10 minerals: mineral spectral abundance and mineral spectral abundance uncertainty. The latitude and longitude layers contain the coordinates for the upper left corner of each pixel.",
-            "series-name": "EMITL3ASA.001",
-            "graphic-preview-description": "Browse image for Earthdata Search.",
             "creator": "Robert Green",
-            "title": "EMIT L3 Aggregated Mineral Spectral Abundance and Uncertainty 0.5 Deg V001",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/EMITL3ASA.001/EMIT_L3_ASA_001/EMIT_L3_ASA_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Earth Surface Mineral Dust Source Investigation (EMIT) instrument measures surface mineralogy, targeting the Earth\u2019s arid dust source regions. EMIT is installed on the International Space Station (ISS) and uses imaging spectroscopy to take measurements of the sunlit regions of interest between 52\u00b0 N latitude and 52\u00b0 S latitude. An interactive map showing the regions being investigated, current and forecasted data coverage, and additional data resources can be found on the VSWIR Imaging Spectroscopy Interface for Open Science (VISIONS) EMIT Open Data Portal.\r\nThe EMIT Level 3 Aggregated Mineral Spectral Abundance and Uncertainty (EMITL3ASA) Version 1 data product provides an aggregated mineral spectral abundance of the 10 minerals that are the focus of the EMIT mission. These minerals, referred to as the EMIT-10 minerals, are calcite, chlorite, dolomite, goethite, gypsum, hematite, illite+muscovite, kaolinite, montmorillonite, and vermiculite. The EMITL3ASA granule consists of one network Common Data Format 4 (netCDF-4) file at a spatial resolution of 0.5 degrees. The data in EMITL3ASA relies heavily on the EMIT L2B Estimated Mineral Identification and Band Depth and Uncertainty (EMITL2BMIN) data. Using the EMITL2BMIN data, aggregated spectral abundance (ASA) is calculated for each of the EMIT-10 minerals as the simple average of relevant 60 m pixels within each 0.5 degree grid cell in the EMITL3ASA product, after controlling for the estimated fractional cover of bare soil within the pixel. \r\nThe EMITL3ASA data product contains 20 Science Dataset (SDS) layers. There are two layers for each of the EMIT-10 minerals: mineral spectral abundance and mineral spectral abundance uncertainty. The latitude and longitude layers contain the coordinates for the upper left corner of each pixel.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEMIT%2FEMITL3ASA.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEMIT%2FEMITL3ASA.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earth.jpl.nasa.gov/emit/",
-                    "description": "The EMIT website provides detailed information on the EMIT mission, instrument, science, applications, and data.",
                     "@type": "dcat:Distribution",
+                    "description": "The EMIT website provides detailed information on the EMIT mission, instrument, science, applications, and data.",
+                    "downloadURL": "https://earth.jpl.nasa.gov/emit/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://doi.org/10.5067/EMIT/EMITL3ASA.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/EMIT/EMITL3ASA.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2408752948-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2408752948-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1801/EMIT_L3_ATBD_V1.pdf",
-                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1801/EMIT_L3_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1800/EMITL3ASA_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1800/EMITL3ASA_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/emit-sds/emit-sds-l3",
-                    "description": "EMIT Level 3 science data system repository.",
                     "@type": "dcat:Distribution",
+                    "description": "EMIT Level 3 science data system repository.",
+                    "downloadURL": "https://github.com/emit-sds/emit-sds-l3",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/EMITL3ASA.001/EMIT_L3_ASA_001/EMIT_L3_ASA_001.png",
-                    "description": "Browse image for Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search.",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/EMITL3ASA.001/EMIT_L3_ASA_001/EMIT_L3_ASA_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/nasa/EMIT-Data-Resources",
-                    "description": "The LP DAAC GitHub repository provides guides, Python notebooks, and scripts to help users access and work with data from the EMIT mission.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC GitHub repository provides guides, Python notebooks, and scripts to help users access and work with data from the EMIT mission.",
+                    "downloadURL": "https://github.com/nasa/EMIT-Data-Resources",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/search/?query=EMIT&content_types=E-Learning&view=cards&sort=relevance",
-                    "description": "EMIT data E-Learning resources provided by NASA's LP DAAC.",
                     "@type": "dcat:Distribution",
+                    "description": "EMIT data E-Learning resources provided by NASA's LP DAAC.",
+                    "downloadURL": "https://lpdaac.usgs.gov/search/?query=EMIT&content_types=E-Learning&view=cards&sort=relevance",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search.",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/EMITL3ASA.001/EMIT_L3_ASA_001/EMIT_L3_ASA_001.png",
+            "identifier": "C2408752948-LPCLOUD",
+            "issued": "2023-09-28",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/EMIT/EMITL3ASA.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "series-name": "EMITL3ASA.001",
             "spatial": "-165.0 -54.5 179.5 55.0",
+            "temporal": "2022-08-10T00:00:00Z/2023-07-30T23:59:59Z",
             "theme": [
                 "EMIT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "EMIT L3 Aggregated Mineral Spectral Abundance and Uncertainty 0.5 Deg V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://spaceflight.nasa.gov/spacenews/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Amiko Kauderer",
+                "hasEmail": "mailto:amiko.kauderer-1@nasa.gov"
+            },
+            "description": "Walking to Olympus:  An EVA Chronology chronicles the 154 EVAs conducted from March 1965 to April 1997. It is intended to make clear the crucial role played by EVA in the history of spaceflight, as well as to chronicle the large body of EVA lessons learned.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://spaceflight.nasa.gov/spacenews/factsheets/pdfs/EVACron.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "NASA-906",
             "issued": "1997-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "space shuttle",
                 "mission",
@@ -1586622,678 +1586634,646 @@
                 "human spaceflight",
                 "extravehicular activity"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Amiko Kauderer",
-                "hasEmail": "mailto:amiko.kauderer-1@nasa.gov"
-            },
+            "landingPage": "http://spaceflight.nasa.gov/spacenews/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-906",
-            "description": "Walking to Olympus:  An EVA Chronology chronicles the 154 EVAs conducted from March 1965 to April 1997. It is intended to make clear the crucial role played by EVA in the history of spaceflight, as well as to chronicle the large body of EVA lessons learned.",
-            "title": "Extravehicular Activity Fact Sheet: An EVA Chronology",
-            "programCode": [
-                "026:035"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://spaceflight.nasa.gov/spacenews/factsheets/pdfs/EVACron.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Extravehicular Activity Fact Sheet: An EVA Chronology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MI1B2E_L1.004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MI1B2E_004. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MISR/MI1B2E_L1.004. https://asdc.larc.nasa.gov/project/MISR/MI1B2E_004.",
-            "issued": "2023-11-02",
-            "temporal": "1999-12-18T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-23",
-            "keyword": [
-                "atmosphere",
-                "spectral/engineering",
-                "visible wavelengths",
-                "atmospheric pressure",
-                "earth science",
-                "atmospheric temperature"
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
-            "identifier": "C2794373815-LARC",
             "description": "MI1B2E_004 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 1B2 Ellipsoid Data Version 4 product. It contains Ellipsoid-projected Top-of-Atmosphere (TOA) Radiance, resampled at the surface and topographically corrected, as well as geometrically corrected by PGE22. Data collection for this product is ongoing.\r\n\r\nMISR itself is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the affects of sunlight on Earth, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 1B2 Ellipsoid Data V004",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMI1B2E_L1.004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMI1B2E_L1.004",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf",
-                    "description": "Overview of MISR Data at the ASDC, 2015",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of MISR Data at the ASDC, 2015",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
-                    "description": "MISR Level 1 Production Report",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 1 Production Report",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
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
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
-                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.html",
-                    "description": "MISR Quality Statements for Current Products",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements for Current Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.html",
-                    "description": "Data Product Specification for Specific Products MISR Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for Specific Products MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://terra.nasa.gov/about/terra-instruments/misr",
-                    "description": "TERRA Overview",
                     "@type": "dcat:Distribution",
+                    "description": "TERRA Overview",
+                    "downloadURL": "https://terra.nasa.gov/about/terra-instruments/misr",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
-                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
+                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2794373815-LARC",
-                    "description": "Earthdata Search for MI1B2E_004",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MI1B2E_004",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2794373815-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MI1B2E_L1.004",
-                    "description": "DOI data set landing page for MI1B2E_004",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MI1B2E_004",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MI1B2E_L1.004",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
-                    "description": "MISR Peer-Reviewed Publications",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Peer-Reviewed Publications",
+                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.pdf",
-                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "description": "ASDC Data and Information for MISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
+                    "mediaType": "text/html",
                     "title": "Visit this dataset's data center's home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View a micro article on this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
-                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
-                    "description": "NASA EOS ATB Documents: MISR",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MISR",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
-                    "description": "MISR Level 1 Production Report",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 1 Production Report",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
-                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf",
-                    "description": "Overview of MISR Data at the ASDC, 2023",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of MISR Data at the ASDC, 2023",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR/cgi-bin/MISR/main.cgi",
-                    "description": "MISR Order and Customization Tool",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Order and Customization Tool",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR/cgi-bin/MISR/main.cgi",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
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
-                    "downloadURL": "https://terra.nasa.gov/about/terra-instruments/misr",
-                    "description": "TERRA Overview",
                     "@type": "dcat:Distribution",
+                    "description": "TERRA Overview",
+                    "downloadURL": "https://terra.nasa.gov/about/terra-instruments/misr",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.pdf",
-                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.pdf",
-                    "description": "MISR Quality Statements for Current Products",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements for Current Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.pdf",
-                    "description": "ASDC Overview of MISR Data Versioning Index",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR Data Versioning Index",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MI1B2E_L1.004",
-                    "description": "DOI data set landing page for MI1B2E_004",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MI1B2E_004",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MI1B2E_L1.004",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.pdf",
-                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.pdf",
-                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.pdf",
-                    "description": "Data Product Specification for Specific Products MISR Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for Specific Products MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents//misr/dps/misr_dps_dps.pdf",
-                    "description": "Data Product Specification for MISR Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents//misr/dps/misr_dps_dps.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI1B2E.004/",
-                    "description": "ASDC Direct Data Download for MI1B2E_004",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MI1B2E_004",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI1B2E.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "description": "ASDC Data and Information for MISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
+                    "mediaType": "text/html",
                     "title": "Visit this dataset's data center's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
-                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
+                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2794373815-LARC",
-                    "description": "Earthdata Search for MI1B2E_004",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MI1B2E_004",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2794373815-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI1B2E.004/contents.html",
-                    "description": "OPeNDAP data access for MI1B2E_004",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MI1B2E_004",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI1B2E.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
-                    "description": "MISR Paths Tool - Direct File Download (.kml)",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Paths Tool - Direct File Download (.kml)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "Downloadable software applications"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C2794373815-LARC",
+            "issued": "2023-11-02",
+            "keyword": [
+                "atmosphere",
+                "spectral/engineering",
+                "visible wavelengths",
+                "atmospheric pressure",
+                "earth science",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MI1B2E_L1.004",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
+            "temporal": "1999-12-18T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 1B2 Ellipsoid Data V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECL5D-HEA44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Ocean and Sea-Ice Surface Heat Fluxes - Daily Mean llc90 Grid (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECL5D-HEA44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Ocean and Sea-Ice Surface Heat Fluxes - Daily Mean llc90 Grid (Version 4 Release 4); 10.5067/ECL5D-HEA44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "earth science services",
-                "earth science reanalyses/assimilation models",
-                "earth science",
-                "oceans",
-                "ocean heat budget",
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
-            "identifier": "C1991543712-POCLOUD",
-            "description": "This dataset provides daily-averaged ocean and sea-ice surface heat fluxes on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean and Sea-Ice Surface Heat Fluxes - Daily Mean llc90 Grid (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_HEAT_FLUX_LLC0090GRID_DAILY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides daily-averaged ocean and sea-ice surface heat fluxes on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5D-HEA44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5D-HEA44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_HEAT_FLUX_LLC0090GRID_DAILY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_HEAT_FLUX_LLC0090GRID_DAILY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECL5D-HEA44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECL5D-HEA44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543712-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543712-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543712-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543712-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_HEAT_FLUX_LLC0090GRID_DAILY_V4R4.jpg",
+            "identifier": "C1991543712-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "earth science services",
+                "earth science reanalyses/assimilation models",
+                "earth science",
+                "oceans",
+                "ocean heat budget",
+                "models"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECL5D-HEA44",
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
+            "title": "ECCO Ocean and Sea-Ice Surface Heat Fluxes - Daily Mean llc90 Grid (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/echo/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-07-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "metadata",
-                "eos",
-                "earth science",
-                "code ti",
-                "arc",
-                "ames research center"
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
-            "identifier": "OCIO-Fitara-118",
             "description": "ECHO is a clearinghouse of Earth science Metadata under the EOS Program.",
-            "title": "ARC Code TI: EOS Clearinghouse (ECHO)",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1587301,912 +1587281,908 @@
                     "mediaType": "application/x-zip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-118",
+            "issued": "2015-07-21",
+            "keyword": [
+                "metadata",
+                "eos",
+                "earth science",
+                "code ti",
+                "arc",
+                "ames research center"
+            ],
+            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/echo/",
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
+            "title": "ARC Code TI: EOS Clearinghouse (ECHO)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC1-67PCHURYUMOV-M10-V2.0",
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
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc1-67pchuryumov-m10-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC1-67PCHURYUMOV-M10-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc1-67pchuryumov-m10-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSIWAC 2 EDR MTP010 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSIWAC 2 EDR MTP010 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-SOLARARRAY-V1.0",
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
+            "description": "This CODMAC level 3 data set contains the key parameters of the SA and   Power Housekeeping. In particular, it provides information on the SA     (mis)alignment, incidence angle & displacement errors as well as         information on the Power subsystem units which include the Master bus    voltage, currents etc.                                                   It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-solararray-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-SOLARARRAY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-solararray-v1.0",
-            "description": "This CODMAC level 3 data set contains the key parameters of the SA and   Power Housekeeping. In particular, it provides information on the SA     (mis)alignment, incidence angle & displacement errors as well as         information on the Power subsystem units which include the Master bus    voltage, currents etc.                                                   It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA SOLAR ARRAY AND POWER                    \n                            ENGINEERING DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA SOLAR ARRAY AND POWER                    \n                            ENGINEERING DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR13-V1.0",
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
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR13) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 26 and 28, 2009, during he Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr13-v1.0_wpqr-g9sg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR13-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr13-v1.0_wpqr-g9sg",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR13) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 26 and 28, 2009, during he Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR13 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TIGR13 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V4.0",
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
+            "description": "The data set lists orbital and physical properties for well-observed or suspected binary/multiple minor planets including the Pluto system, as inspired by Richardson and Walsh (2006) and similar reviews (Merline et al., 2003; Noll, 2006; Pravec et al., 2006; Pravec and Harris, 2007; Descamps and Marchis, 2008; Noll et al., 2008; Walsh, 2009). In total 202 companions in 191 systems are included. Data are presented in two tables, one for orbital and physical properties and one for companion designations, discovery information, and reference codes for data values. Data are ordered by permanent number, then provisional designation. This data set is complete for binary/multiple components reported through 31 March 2011.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v4.0_wprm-63zq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V4.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v4.0_wprm-63zq",
-            "description": "The data set lists orbital and physical properties for well-observed or suspected binary/multiple minor planets including the Pluto system, as inspired by Richardson and Walsh (2006) and similar reviews (Merline et al., 2003; Noll, 2006; Pravec et al., 2006; Pravec and Harris, 2007; Descamps and Marchis, 2008; Noll et al., 2008; Walsh, 2009). In total 202 companions in 191 systems are included. Data are presented in two tables, one for orbital and physical properties and one for companion designations, discovery information, and reference codes for data values. Data are ordered by permanent number, then provisional designation. This data set is complete for binary/multiple components reported through 31 March 2011.",
-            "title": "BINARY MINOR PLANETS V4.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "BINARY MINOR PLANETS V4.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/zzbm-2w05",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rutgers Northern Hemisphere 24 km Weekly Snow Cover Extent, September 1980 Onward, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/zzbm-2w05.",
-            "issued": "1980-08-26",
-            "temporal": "1980-08-26T00:00:00Z/2023-10-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-02",
-            "keyword": [
-                "cryosphere",
-                "earth science",
-                "snow/ice"
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
-            "identifier": "C2141102279-NSIDCV0",
             "description": "This data set provides weekly snow cover extent for the Northern Hemisphere in NetCDF format from September 1980 through most recent processing at a 24 km resolution.",
-            "title": "Rutgers Northern Hemisphere 24 km Weekly Snow Cover Extent, September 1980 Onward, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fzzbm-2w05",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fzzbm-2w05",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G10035/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G10035/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/zzbm-2w05",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/zzbm-2w05",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/zzbm-2w05",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/zzbm-2w05",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2141102279-NSIDCV0",
+            "issued": "1980-08-26",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.7265/zzbm-2w05",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "1980-08-26T00:00:00Z/2023-10-02T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Rutgers Northern Hemisphere 24 km Weekly Snow Cover Extent, September 1980 Onward, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-2-EDR-ELS-EXT3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Mars Express ASPERA-3 Electron Spectrometer (ELS) data for the second mission extension (January 1, 2010 - Dec. 31, 2012). These data are provided in raw units of counts/accumulation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-2-edr-els-ext3-v1.0_wpxs-dp8d",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "solar wind",
                 "mars express",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-2-EDR-ELS-EXT3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-2-edr-els-ext3-v1.0_wpxs-dp8d",
-            "description": "This data set contains Mars Express ASPERA-3 Electron Spectrometer (ELS) data for the second mission extension (January 1, 2010 - Dec. 31, 2012). These data are provided in raw units of counts/accumulation.",
-            "title": "MARS EXPRESS ASPERA-3 RAW EDR ELECTRON SPECTROMTR EXT3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARS EXPRESS ASPERA-3 RAW EDR ELECTRON SPECTROMTR EXT3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECL5M-OBP44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Ocean Bottom Pressure - Monthly Mean llc90 Grid (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECL5M-OBP44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Ocean Bottom Pressure - Monthly Mean llc90 Grid (Version 4 Release 4); 10.5067/ECL5M-OBP44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "earth science",
-                "earth science services",
-                "models",
-                "ocean pressure",
-                "earth science reanalyses/assimilation models",
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
-            "identifier": "C1991543806-POCLOUD",
-            "description": "This dataset provides monthly-averaged ocean bottom pressure and model ocean bottom pressure anomaly on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean Bottom Pressure - Monthly Mean llc90 Grid (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides monthly-averaged ocean bottom pressure and model ocean bottom pressure anomaly on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-OBP44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-OBP44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECL5M-OBP44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECL5M-OBP44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543806-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543806-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543806-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543806-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4.jpg",
+            "identifier": "C1991543806-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "earth science",
+                "earth science services",
+                "models",
+                "ocean pressure",
+                "earth science reanalyses/assimilation models",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECL5M-OBP44",
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
+            "title": "ECCO Ocean Bottom Pressure - Monthly Mean llc90 Grid (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MODEL-M-AMES-GCM-5-TOPOGRAPHY-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.model-m-ames-gcm-5-topography-v1.0_wq37-uyya",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MODEL-M-AMES-GCM-5-TOPOGRAPHY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.model-m-ames-gcm-5-topography-v1.0_wq37-uyya",
-            "description": "The Ames Mars General Circulation Model is a three dimensional model based on the primitive equations of meteorology. It includes the radiative effects of dust and carbon dioxide as well as other features such as large-scale topography (see [POLLACKETAL1990]",
-            "title": "AMES MARS GENERAL CIRCULATION MODEL 5 TOPOGRAPHY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "AMES MARS GENERAL CIRCULATION MODEL 5 TOPOGRAPHY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0995-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-29T21:30:30.000 to 2015-08-30T01:24:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0995-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0995-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0995-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-29T21:30:30.000 to 2015-08-30T01:24:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0995 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0995 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/BBOP/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/BBOP/DATA001.",
-            "issued": "1988-10-20",
-            "temporal": "1988-10-20T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "earth science",
-                "ocean chemistry",
-                "ocean temperature",
-                "oceans",
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
-            "identifier": "C1633360137-OB_DAAC",
             "description": "The Bermuda Bio-Optics Project (BBOP) is a long term study of the factors contributing to the regulation of the underwater light field in the open ocean and the resulting biogeochemical impact.  These studies are done, on average, once a month in conjunction with the Bermuda-Atlantic Time Series (BATS) in the Sargasso Sea.",
-            "title": "Bermuda Bio-Optics Project (BBOP)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBBOP%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBBOP%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BBOP/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BBOP/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360137-OB_DAAC",
+            "issued": "1988-10-20",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "ocean temperature",
+                "oceans",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/BBOP/DATA001",
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
+            "temporal": "1988-10-20T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Bermuda Bio-Optics Project (BBOP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/tyrt-8r32",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "PISUNA-net Local Observations Database, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/tyrt-8r32.",
-            "issued": "2019-01-01",
-            "temporal": "2019-01-01T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-25",
-            "keyword": [
-                "animals/vertebrates",
-                "social behavior",
-                "public health",
-                "human dimensions",
-                "earth science",
-                "biological classification"
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
-            "identifier": "C1728381147-NSIDCV0",
             "description": "The PISUNA-net Local Observations database was developed to record, archive, and share indigenous and local knowledge and expertise on natural resources and resource use on the western and northern coasts of Greenland.",
-            "title": "PISUNA-net Local Observations Database, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Ftyrt-8r32",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Ftyrt-8r32",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eloka-arctic.org/pisuna-net/en/",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://eloka-arctic.org/pisuna-net/en/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/tyrt-8r32",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/tyrt-8r32",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/tyrt-8r32",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/tyrt-8r32",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C1728381147-NSIDCV0",
+            "issued": "2019-01-01",
+            "keyword": [
+                "animals/vertebrates",
+                "social behavior",
+                "public health",
+                "human dimensions",
+                "earth science",
+                "biological classification"
             ],
+            "landingPage": "https://doi.org/10.7265/tyrt-8r32",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2025-01-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
+            "temporal": "2019-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "PISUNA-net Local Observations Database, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1.",
-            "issued": "2020-07-20",
-            "temporal": "2019-08-24T00:00:00Z/2019-09-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-08",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere"
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
-            "identifier": "C1954734794-LARC_ASDC",
             "description": "CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data are in-situ cloud measurements conducted onboard the SPEC Learjet aircraft during the Clouds, Aerosol and Monsoon Processes-Philippines Experiment (CAMP2Ex) NASA field study. Data collection for this product is complete.\r\n\r\nCAMP2Ex was a NASA field study, with three main science objectives: aerosol effect on cloud microphysical and optical properties, aerosol and cloud influence on radiation as well as radiative feedback, and meteorology effect on aerosol distribution and aerosol-cloud interactions. Research on these three main objectives requires a comprehensive characterization of aerosol, cloud, and precipitation properties, as well as the associated meteorological and radiative parameters. Trace gas tracers are also needed for airmass type analysis to characterize the role of anthropogenic and natural aerosols. To deliver these observations, CAMP2Ex utilized a combination of remote sensing and in-situ measurements. NASA\u2019s P-3B aircraft was equipped with a suite of in-situ instruments to conduct measurements of aerosol and cloud properties, trace gases, meteorological parameters, and radiative fluxes. The P-3B was also equipped passive remote sensors (i.e. lidar, polarimeter, radar, and radiometers). A second aircraft, the SPEC Learjet 35A, was primarily dedicated to measuring detailed cloud microphysical properties. The sampling strategy designed for CAMP2Ex coordinated flight plans for both aircraft to maximize the science return. The P-3B was used primarily to conduct remote sensing measurements of cloud and precipitation structure and aerosol layers and vertical profiles of atmospheric state variable, while the Learjet flew below the P-3B to obtain the detailed cloud microphysical properties. During the 2019 field deployment in the vicinity of the Philippines, completed from August 20-October 10, the P-3B conducted 19 science flights and the SPEC Learjet conducted 11 flights. Ground-based aerosol observations were also recorded in 2018 and 2019. CAMP2Ex was completed in partnership with Philippine research and operational weather communities. Measurements completed during CAMP2EX provide a 4-D observational view of the environment of the Philippines and its neighboring waters in terms of microphysical, hydrological, dynamical, thermodynamical and radiative properties of the environment, targeting the environment of shallow cumulus and cumulus congestus clouds.",
-            "title": "CAMP2Ex Learjet In-Situ Cloud Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FCAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FCAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/camp2ex",
-                    "description": "CAMP2EX ESPO Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "CAMP2EX ESPO Project Home Page",
+                    "downloadURL": "https://espo.nasa.gov/camp2ex",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/camp2ex/docs/CAMP2Ex-overview-27NOV2015.pdf",
-                    "description": "CAMP2Ex Mission Overview/White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "CAMP2Ex Mission Overview/White Paper",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/camp2ex/docs/CAMP2Ex-overview-27NOV2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/philippine-airborne-campaign-targets-weather-climate-science",
-                    "description": "NASA.gov CAMP2Ex Feature \u201cPhilippine Airborne Campaign Targets Weather, Climate Science\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov CAMP2Ex Feature \u201cPhilippine Airborne Campaign Targets Weather, Climate Science\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/philippine-airborne-campaign-targets-weather-climate-science",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1954734794-LARC_ASDC",
-                    "description": "Earthdata Search for CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1954734794-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
-                    "description": "DOI data set landing page for CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/camp2ex/",
-                    "description": "NASA Earth Expeditions CAMP2Ex Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions CAMP2Ex Posts",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/camp2ex/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/Cloud_AircraftInSitu_Learjet_Data_1/",
-                    "description": "ASDC Direct Data Download for CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/Cloud_AircraftInSitu_Learjet_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1954734794-LARC_ASDC",
+            "issued": "2020-07-20",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_Learjet_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-10-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>0.0 0.0 0.0 130.0 21.0 130.0 21.0 0.0 0.0 0.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-08-24T00:00:00Z/2019-09-29T23:59:59.999Z",
             "theme": [
                 "CAMP2Ex",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMP2Ex Learjet In-Situ Cloud Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/476/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-10-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PAWEL CHWALOWSKI",
                 "hasEmail": "mailto:pawel.chwalowski@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_476",
             "description": "These grids were constructed using VGRID software from NASA Langley. The grids designed for node based (labeled 'nc') and cell-centered solvers are supplied. Grids with mixed elements (labeled 'mixed') and tetrahedral elements (labeled 'tets') are supplied.\r\n\r\nEach mixed elements tar-file contains grid in aflr3 .ugrid format and the corresponding .cgns file. Each tetrahedral elements tar-file contains grid in native VGRID format (.cogsg, .bs, .mapbc) and the corresponding .cgns file.\r\n\r\nSome files were too large and had to be split into parts. To combine the parts, use cat filename_part1 filename_part2 > filename.\r\n\r\nGrids are in units of 'inch'. Information about grids, that is number of nodes, elements, etc., is provided in AePW_BSCW_Grid_Statistics_VGRID.docx\r\n\r\nPlease report any issues with these grids to Pawel.Chwalowski@nasa.gov\r\n\r\nPlease note that the final grids for Aeroelastic Prediction Workshop are due on November 1. Therefore these grids still may change based on your initial calculations.",
-            "title": "BSCW Unstructured Grids - VGRID software",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_tets_nc.tar.gz",
-                    "description": "Coarse tetrahedral node based",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse tetrahedral node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_tets_nc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_coarse_tets_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_mixed_nc.tar.gz",
-                    "description": "Coarse Mixed node based",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse Mixed node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_mixed_nc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_coarse_mixed_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_tets_cc.tar.gz",
-                    "description": "Coarse tetrahedral cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse tetrahedral cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_tets_cc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_coarse_tets_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_mixed_cc.tar.gz",
-                    "description": "Coarse Mixed cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse Mixed cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_mixed_cc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_coarse_mixed_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_tets_nc.tar.gz",
-                    "description": "Medium tetrahedral node based",
                     "@type": "dcat:Distribution",
+                    "description": "Medium tetrahedral node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_tets_nc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_medium_tets_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_mixed_nc.tar.gz",
-                    "description": "Medium Mixed node based",
                     "@type": "dcat:Distribution",
+                    "description": "Medium Mixed node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_mixed_nc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_medium_mixed_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_tets_cc.tar.gz",
-                    "description": "Medium tetrahedral cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Medium tetrahedral cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_tets_cc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_medium_tets_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_mixed_cc.tar.gz",
-                    "description": "Medium Mixed cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Medium Mixed cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_mixed_cc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_medium_mixed_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_nc.tar.gz_part1",
-                    "description": "Part1: Fine tetrahedral node based",
                     "@type": "dcat:Distribution",
+                    "description": "Part1: Fine tetrahedral node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_nc.tar.gz_part1",
+                    "mediaType": "application/octet-stream",
                     "title": "bscw_fine_tets_nc.tar.gz_part1"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_nc.tar.gz_part2",
-                    "description": "Part2: Fine tetrahedral node based",
                     "@type": "dcat:Distribution",
+                    "description": "Part2: Fine tetrahedral node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_nc.tar.gz_part2",
+                    "mediaType": "application/octet-stream",
                     "title": "bscw_fine_tets_nc.tar.gz_part2"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_nc.tar.gz_part1",
-                    "description": "Part1: Fine Mixed node based",
                     "@type": "dcat:Distribution",
+                    "description": "Part1: Fine Mixed node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_nc.tar.gz_part1",
+                    "mediaType": "application/octet-stream",
                     "title": "bscw_fine_mixed_nc.tar.gz_part1"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_nc.tar.gz_part2",
-                    "description": "Part2: Fine Mixed node based",
                     "@type": "dcat:Distribution",
+                    "description": "Part2: Fine Mixed node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_nc.tar.gz_part2",
+                    "mediaType": "application/octet-stream",
                     "title": "bscw_fine_mixed_nc.tar.gz_part2"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_cc.tar.gz",
-                    "description": "Fine tetrahedral cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Fine tetrahedral cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_cc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_fine_tets_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_cc.tar.gz",
-                    "description": "Fine Mixed cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Fine Mixed cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_cc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_fine_mixed_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.d",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AePW_BSCW_Grid_Statistics_VGRID.docx",
-                    "description": "Grid Information",
                     "@type": "dcat:Distribution",
+                    "description": "Grid Information",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AePW_BSCW_Grid_Statistics_VGRID.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.d",
                     "title": "AePW_BSCW_Grid_Statistics_VGRID.docx"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_476",
+            "issued": "2011-10-13",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/476/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "BSCW Unstructured Grids - VGRID software"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2248663248-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2019-07-01. OCO2_L1aIn_Pixel. Version 11r. OCO-2 Level 1A collated, parsed, calibration data, Retrospective Processing V11r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Pixel_11r.html. Digital Science Data.",
-            "issued": "2019-06-27",
-            "temporal": "2014-07-21T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-17",
-            "keyword": [
-                "spectral/engineering",
-                "atmospheric chemistry",
-                "earth science",
-                "infrared wavelengths",
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
-            "identifier": "C2248663248-GES_DISC",
-            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Single-pixel Mode of operation.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L1aIn_Pixel",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 1A collated, parsed, calibration data, Retrospective Processing V11r (OCO2_L1aIn_Pixel) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_L1aIn_Pixel_8r.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Single-pixel Mode of operation.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1588215,270 +1588191,274 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Pixel_11r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Pixel_11r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1aIn_Pixel",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1aIn_Pixel",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Pixel.11r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Pixel.11r/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Pixel.11r/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Pixel.11r/",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_L1aIn_Pixel_8r.jpeg",
+            "identifier": "C2248663248-GES_DISC",
+            "issued": "2019-06-27",
+            "keyword": [
+                "spectral/engineering",
+                "atmospheric chemistry",
+                "earth science",
+                "infrared wavelengths",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2248663248-GES_DISC.html",
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
+            "series-name": "OCO2_L1aIn_Pixel",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-07-21T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 1A collated, parsed, calibration data, Retrospective Processing V11r (OCO2_L1aIn_Pixel) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0193-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-09T20:42:00.000 to 2014-08-10T02:13:13.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0193-v1.0_wq8a-5tce",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0193-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0193-v1.0_wq8a-5tce",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-09T20:42:00.000 to 2014-08-10T02:13:13.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0193 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0193 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-J-UVIS-2-SPEC-V1.0",
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
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A set of spectra.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-j-uvis-2-spec-v1.0_wq93-spgf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-J-UVIS-2-SPEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-j-uvis-2-spec-v1.0_wq93-spgf",
-            "description": "A set of spectra.",
-            "title": "CASSINI ORBITER JUPITER UVIS EDITED SPECTRA 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER JUPITER UVIS EDITED SPECTRA 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/N01/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/N01/DATA001.",
-            "issued": "2011-12-03",
-            "temporal": "2011-12-03T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
-                "earth science",
-                "ocean chemistry",
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
-            "identifier": "C1633360512-OB_DAAC",
             "description": "Measurements taken along a zonal transect from Hawaii across the western Pacific Ocean in 2011.",
-            "title": "Zonal transect from Hawaii across the western Pacific Ocean in 2011",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FN01%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FN01%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/N01/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/N01/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360512-OB_DAAC",
+            "issued": "2011-12-03",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/N01/DATA001",
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
+            "temporal": "2011-12-03T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Zonal transect from Hawaii across the western Pacific Ocean in 2011"
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
-                "index",
-                "dictionary",
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
-            "identifier": "NASA-660",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r51)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1588486,666 +1588466,657 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-660",
+            "issued": "2018-06-25",
+            "keyword": [
+                "index",
+                "dictionary",
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
+            "title": "PDS Data Dictionary (1r51)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-3-LAUNCH-V2.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the post-launch checkout mission phase.  This is VERSION 2.0 of this data set. LORRI V2.0 updates include - improvements to geometry and timing in data header sections and to ancillary files (DOCUMENT/); - keywords giving the approximate target and target location have been added to the PDS labels, as well as a PDS SPREADSHEET containing potential targets in or near the instrument Field of View; - Corrections were made to some calibration file labels.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-3-launch-v2.0_wqea-7pde",
+            "issued": "2018-06-26",
+            "keyword": [
+                "new horizons",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-3-LAUNCH-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-3-launch-v2.0_wqea-7pde",
-            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the post-launch checkout mission phase.  This is VERSION 2.0 of this data set. LORRI V2.0 updates include - improvements to geometry and timing in data header sections and to ancillary files (DOCUMENT/); - keywords giving the approximate target and target location have been added to the PDS labels, as well as a PDS SPREADSHEET containing potential targets in or near the instrument Field of View; - Corrections were made to some calibration file labels.",
-            "title": "NEW HORIZONS\n      LORRI POST-LAUNCH CHECKOUT\n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS\n      LORRI POST-LAUNCH CHECKOUT\n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-09-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1.",
-            "issued": "2021-03-19",
-            "temporal": "2013-08-02T00:00:00Z/2013-11-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-20",
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C2119341676-LARC_ASDC",
             "description": "SEAC4RS_Aerosol_AircraftInSitu_DC8_Data are in-situ aerosol data collected onboard the DC8 aircraft during the Studies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEA4CRS) airborne field study. Data collection for this product is complete.\r\n\r\nStudies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEAC4RS) airborne field study was conducted in August and September of 2013. The field operation was based in Houston, Texas. The primary SEAC4RS science objectives are: to determine how pollutant emissions are redistributed via deep convection throughout the troposphere; to determine the evolution of gases and aerosols in deep convective outflow and the implications for UT/LS chemistry; to identify the influences and feedbacks of aerosol particles from anthropogenic pollution and biomass burning on meteorology and climate through changes in the atmospheric heat budget (i.e., semi-direct effect) or through microphysical changes in clouds (i.e., indirect effects); and lastly, to serve as a calibration and validation test bed for future satellite instruments and missions.\r\n\r\nThe airborne observational data were collected from three aircraft platforms: the NASA DC-8, ER-2, and SPEC LearJet. Both the NASA DC-8 and ER-2 aircraft were instrumented for comprehensive in-situ and remote sensing measurements of the trace gas, aerosol properties, and cloud properties. In addition, radiative fluxes and meteorological parameters were also recorded. The NASA DC-8 was mostly responsible for tropospheric sampling, while the NASA ER-2 was operating in the lower stratospheric regime. The SPEC LearJet was dedicated to in-situ cloud characterizations. To accomplish the science objectives, the flight plans were designed to investigate the influence of biomass burning and pollution, their temporal evolution, and ultimately, impacts on meteorological processes which can, in turn, feedback on regional air quality. With respect to meteorological feedbacks, the opportunity to examine the impact of polluting aerosols on cloud properties and dynamics was of particular interest.",
-            "title": "SEAC4RS DC-8 Aircraft In-Situ Aerosol Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341676-LARC_ASDC",
-                    "description": "Earthdata Search for SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341676-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI data set landing page of SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page of SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/Aerosol_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/Aerosol_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2119341676-LARC_ASDC",
+            "issued": "2021-03-19",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Aerosol_AircraftInSitu_DC8_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.0 -127.0 19.0 -79.0 51.0 -79.0 51.0 -127.0 19.0 -127.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-08-02T00:00:00Z/2013-11-25T23:59:59.999Z",
             "theme": [
                 "SEAC4RS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEAC4RS DC-8 Aircraft In-Situ Aerosol Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3PQCE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image 7-Day Running Mean Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3PQCE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image 7-Day Running Mean Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
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
-            "identifier": "C2491756147-POCLOUD",
-            "description": "Aquarius Level 3 sea surface spiciness standard mapped image data contains gridded 1 degree spatial resolution spice data averaged\nover daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day running mean sea surface spiciness product for version 5.0 of the Aquarius data set. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image 7-Day Running Mean Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image 7-Day Running Mean Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SPICINESS_SMI_7DAY-RUNNINGMEAN_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface spiciness standard mapped image data contains gridded 1 degree spatial resolution spice data averaged\nover daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day running mean sea surface spiciness product for version 5.0 of the Aquarius data set. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3PQCE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3PQCE",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SPICINESS_SMI_7DAY-RUNNINGMEAN_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SPICINESS_SMI_7DAY-RUNNINGMEAN_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756147-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756147-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756147-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756147-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SPICINESS_SMI_7DAY-RUNNINGMEAN_V5.jpg",
+            "identifier": "C2491756147-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3PQCE",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image 7-Day Running Mean Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image 7-Day Running Mean Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ARCB%2FGSSR-M-RTLS-5-MODEL-V1.0",
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
-                "pre-magellan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A model for Mars depolarized radar echo power that (1) matches the observed variation of total radar cross section with longitude and (2) produces model spectra that have the broad features of spectra published for Goldstone Solar System Radar and for Arecibo Observatory 1980 to 1982 observations. This model assumes that different geologic units on Mars backscatter in a uniformly bright manner, where radar echo power is A * Cosine (angle of incidence), where A varies across the planet. This model assigns depolarized radar echo power on a degree-by-degree basis in latitude and longitude.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.arcb-gssr-m-rtls-5-model-v1.0_wqhr-f7dd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "pre-magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ARCB%2FGSSR-M-RTLS-5-MODEL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.arcb-gssr-m-rtls-5-model-v1.0_wqhr-f7dd",
-            "description": "A model for Mars depolarized radar echo power that (1) matches the observed variation of total radar cross section with longitude and (2) produces model spectra that have the broad features of spectra published for Goldstone Solar System Radar and for Arecibo Observatory 1980 to 1982 observations. This model assumes that different geologic units on Mars backscatter in a uniformly bright manner, where radar echo power is A * Cosine (angle of incidence), where A varies across the planet. This model assigns depolarized radar echo power on a degree-by-degree basis in latitude and longitude.",
-            "title": "ARCB/GSSR M RADIO TELESC DERIVED RADAR MODEL UNIT MAP V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ARCB/GSSR M RADIO TELESC DERIVED RADAR MODEL UNIT MAP V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-SS-MAG-2-EDR-CRUISE-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains data acquired by the Galileo Magnetometer during the Interplanetary Cruise to Jupiter. The data are at varying resolution depending on the averaging constant applied to the instrument. The EDR files are given in IBM 370 binary representation and are stored in an extremely compact format.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-ss-mag-2-edr-cruise-v1.0_wqjy-3bn4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-SS-MAG-2-EDR-CRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-ss-mag-2-edr-cruise-v1.0_wqjy-3bn4",
-            "description": "This data set contains data acquired by the Galileo Magnetometer during the Interplanetary Cruise to Jupiter. The data are at varying resolution depending on the averaging constant applied to the instrument. The EDR files are given in IBM 370 binary representation and are stored in an extremely compact format.",
-            "title": "GALILEO MAGNETOMETER CRUISE EDR DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO MAGNETOMETER CRUISE EDR DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D51.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Shortwave Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D51.061. https://doi.org/10.5067/MODIS/MCD43D51.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "national geospatial data asset",
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
-            "identifier": "C2540273055-LPCLOUD",
-            "description": "The MCD43D51 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Black-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D51 is the black-sky albedo for the MODIS shortwave broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Shortwave Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D51 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Black-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D51 is the black-sky albedo for the MODIS shortwave broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D51.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D51.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D51.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D51.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273055-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273055-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D51.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D51.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D51",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D51",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D51.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D51.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540273055-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D51.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Shortwave Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CZ39JIR4ZAT4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gary L. Fahnenstiel, Michael J. Sayers, Robert A. Shuchman, Foad Yousef, & Steven A. Pothoven. 2019-10-31. CMSLakeHuronPPM. Version 1. Carbon Monitoring System Lake Huron Primary Production Monthly. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/CZ39JIR4ZAT4. https://disc.gsfc.nasa.gov/datacollection/CMSLakeHuronPPM_1.html.",
-            "issued": "2019-10-21",
-            "temporal": "2010-01-01T00:00:00Z/2013-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-21",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2016.02.004",
-                "https://doi.org/10.1016/j.jglr.2013.06.017",
-                "https://doi.org/10.1029/2004JC002780"
-            ],
-            "keyword": [
-                "earth science",
-                "ngda",
-                "biosphere",
-                "national geospatial data asset",
-                "ecological dynamics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1652491691-GES_DISC",
-            "description": "Monthly Average primary production/carbon fixation data for Lake Huron.  The primary production data is derived using MODIS imagery with model data.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMSLakeHuronPPM",
             "creator": "Gary L. Fahnenstiel, Michael J. Sayers, Robert A. Shuchman, Foad Yousef, & Steven A. Pothoven",
-            "title": "Carbon Monitoring System Lake Huron Primary Production Monthly V1 (CMSLakeHuronPPM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSLakeHuronPPM_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Monthly Average primary production/carbon fixation data for Lake Huron.  The primary production data is derived using MODIS imagery with model data.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCZ39JIR4ZAT4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCZ39JIR4ZAT4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1589155,45 +1589126,45 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSLakeHuronPPM_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSLakeHuronPPM_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeHuronPPM.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeHuronPPM.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeHuronPPM.1/doc/README.CMSGreatLakesPrimaryProductivity.V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeHuronPPM.1/doc/README.CMSGreatLakesPrimaryProductivity.V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSLakeHuronPPM.1",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSLakeHuronPPM.1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSLakeHuronPPM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSLakeHuronPPM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -1589203,289 +1589174,294 @@
                     "title": "This dataset's landing page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSLakeHuronPPM_1.png",
+            "identifier": "C1652491691-GES_DISC",
+            "issued": "2019-10-21",
+            "keyword": [
+                "earth science",
+                "ngda",
+                "biosphere",
+                "national geospatial data asset",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.5067/CZ39JIR4ZAT4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2016.02.004",
+                "https://doi.org/10.1016/j.jglr.2013.06.017",
+                "https://doi.org/10.1029/2004JC002780"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CMSLakeHuronPPM",
             "spatial": "-84.762 43.001 -79.652 46.591",
+            "temporal": "2010-01-01T00:00:00Z/2013-12-31T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon Monitoring System Lake Huron Primary Production Monthly V1 (CMSLakeHuronPPM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/HGLHWEO3764N",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IPAB Antarctic Drifting Buoy Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/HGLHWEO3764N.",
-            "issued": "1995-01-01",
-            "temporal": "1995-01-01T00:00:00Z/1998-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-12-31",
-            "keyword": [
-                "ocean circulation",
-                "ocean temperature",
-                "atmospheric temperature",
-                "atmosphere",
-                "atmospheric pressure",
-                "oceans",
-                "earth science",
-                "snow/ice",
-                "cryosphere",
-                "sea ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ian Allison",
                 "hasEmail": "mailto:i.allison@antdiv.gov.au"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386250149-NSIDCV0",
             "description": "Through participating research organizations in various countries, the World Climate Research Programme's (WCRP) International Programme for Antarctic Buoys (IPAB) maintains a network of drifting buoys in the Antarctic sea ice zone to support a better understanding of sea ice motion, meteorology, and oceanography. The IPAB Antarctic Drifting Buoy Data archive, spanning the years 1995 to 1998, includes measurements of buoy position, atmospheric pressure, air temperature, and sea surface temperature. Data are organized by daily and three-hour averages and are provided as raw, instantaneous, non-interpolated data values. Data were collected from buoys initially deployed in the following three study regions: East Antarctica; the Weddell Sea; and the Bellingshausen, Amundsen, and Ross Seas.",
-            "title": "IPAB Antarctic Drifting Buoy Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHGLHWEO3764N",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHGLHWEO3764N",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/IPAB_BUOYS/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/IPAB_BUOYS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/HGLHWEO3764N",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/HGLHWEO3764N",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/HGLHWEO3764N",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/HGLHWEO3764N",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250149-NSIDCV0",
+            "issued": "1995-01-01",
+            "keyword": [
+                "ocean circulation",
+                "ocean temperature",
+                "atmospheric temperature",
+                "atmosphere",
+                "atmospheric pressure",
+                "oceans",
+                "earth science",
+                "snow/ice",
+                "cryosphere",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/HGLHWEO3764N",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1998-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -76.0 180.0 -57.0",
+            "temporal": "1995-01-01T00:00:00Z/1998-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IPAB Antarctic Drifting Buoy Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1974",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, R. Kudela, and S.L. Ustin. 2022. MASTER: Student Airborne Research Program (SARP) Campaign, California, 2011. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1974",
-            "issued": "2023-07-08",
-            "temporal": "2011-06-27T19:51:44Z/2011-07-01T00:10:32Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
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
-            "identifier": "C2731697265-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument collected and developed by the Student Airborne Research Program (SARP). The spectral data were collected from flights flown on 2011-06-27 to 2011-06-30 over southern California, U.S., in a NASA DC-8 aircraft. SARP was an eight-week summer program for junior and senior undergraduate students to acquire hands-on research experience in all aspects of a scientific campaign using airborne science laboratories. The SARP 2011 deployment included five flights with 23 flight tracks. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 10-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes the flight path, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single band images and an RGB composite image from flight track 6 acquired on 28 June 2011 over California's Central Valley WNW of Bakersfield, California, U.S. Source: MASTERL1B_1100303_03_20110628_1827_1829_V01.jpg",
-            "title": "MASTER: Student Airborne Research Program (SARP) Campaign, California, 2011",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_SARP_2011_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1974",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1974",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_SARP_2011/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_SARP_2011/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_SARP_2011.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_SARP_2011.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1974",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1974",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_SARP_2011/comp/MASTER_SARP_2011.pdf",
-                    "description": "MASTER: Student Airborne Research Program (SARP) Campaign, California, 2011: MASTER_SARP_2011.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Student Airborne Research Program (SARP) Campaign, California, 2011: MASTER_SARP_2011.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_SARP_2011/comp/MASTER_SARP_2011.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_SARP_2011_Fig1.jpg",
-                    "description": "Single band images and an RGB composite image from flight track 6 acquired on 28 June 2011 over California's Central Valley WNW of Bakersfield, California, U.S. Source: MASTERL1B_1100303_03_20110628_1827_1829_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single band images and an RGB composite image from flight track 6 acquired on 28 June 2011 over California's Central Valley WNW of Bakersfield, California, U.S. Source: MASTERL1B_1100303_03_20110628_1827_1829_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_SARP_2011_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single band images and an RGB composite image from flight track 6 acquired on 28 June 2011 over California's Central Valley WNW of Bakersfield, California, U.S. Source: MASTERL1B_1100303_03_20110628_1827_1829_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_SARP_2011_Fig1.jpg",
+            "identifier": "C2731697265-ORNL_CLOUD",
+            "issued": "2023-07-08",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1974",
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
             "spatial": "-120.26 33.09 -115.31 36.03",
+            "temporal": "2011-06-27T19:51:44Z/2011-07-01T00:10:32Z",
             "theme": [
                 "MASTER",
                 "SARP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Student Airborne Research Program (SARP) Campaign, California, 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-3-EDR-MATHILDE-V1.0",
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
+            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-3-edr-mathilde-v1.0_wqp8-x3yf",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-3-EDR-MATHILDE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-3-edr-mathilde-v1.0_wqp8-x3yf",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR MSI IMAGES FOR MATHILDE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR MSI IMAGES FOR MATHILDE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-AMVIS-2-RDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Amateur Observation Network archived 11641 measurements of Halley's comet. Even though most observers adhered to guidelines established by the IHW, visual magnitudes are highly subjective depending on the technique of each observer and may vary with the quality of the instrument used (e.g., binoculars vs. telescope). These magnitude estimates cover the date range from 1985 January 23 through 1988 February 23.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-amvis-2-rdr-halley-v1.0_wqrk-rdsh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-AMVIS-2-RDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-amvis-2-rdr-halley-v1.0_wqrk-rdsh",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Amateur Observation Network archived 11641 measurements of Halley's comet. Even though most observers adhered to guidelines established by the IHW, visual magnitudes are highly subjective depending on the technique of each observer and may vary with the quality of the instrument used (e.g., binoculars vs. telescope). These magnitude estimates cover the date range from 1985 January 23 through 1988 February 23.",
-            "title": "IHW COMET HALLEY AMATEUR VISUAL MAGNITUDES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY AMATEUR VISUAL MAGNITUDES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-09-14",
-            "temporal": "2021-09-14T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "space",
-                "location",
-                "iss",
-                "station",
-                "topo",
-                "international",
-                "trajectory",
-                "ephemeris",
-                "coords",
-                "coordinates"
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
-            "identifier": "nasa-iss-data_2021-09-14_wqsv-q39a",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-09-14",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1589608,54 +1589584,54 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-09-14_wqsv-q39a",
+            "issued": "2021-09-14",
+            "keyword": [
+                "space",
+                "location",
+                "iss",
+                "station",
+                "topo",
+                "international",
+                "trajectory",
+                "ephemeris",
+                "coords",
+                "coordinates"
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
+            "temporal": "2021-09-14T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-09-14"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3268212607-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-3 Science Team/Michael Gunson, Annmarie Eldering. 2024-10-16. OCO3_L1aIn_Sample. Version 11r. OCO-3 Level 1A collated, parsed, science or calibration data, Retrospective Processing V11r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO3_L1aIn_Sample_11r.html. Digital Science Data.",
-            "issued": "2024-06-27",
-            "temporal": "2014-07-03T00:00:00Z/2024-10-21T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
-                "spectral/engineering",
-                "atmosphere",
-                "atmospheric chemistry"
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
-            "identifier": "C3268212607-GES_DISC",
-            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-3 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Sample Mode of operation.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO3_L1aIn_Sample",
             "creator": "OCO-3 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-3 Level 1A collated, parsed, science or calibration data, Retrospective Processing V11r (OCO2_L1aIn_Sample) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_L1aIn_Sample_8r.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-3 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Sample Mode of operation.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1589664,148 +1589640,150 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L1aIn_Sample_11r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L1aIn_Sample_11r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L1aIn_Sample",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L1aIn_Sample",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L1aIn_Sample.11r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L1aIn_Sample.11r/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ocov3.jpl.nasa.gov/",
-                    "description": "OCO-3 Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Project Home Page",
+                    "downloadURL": "https://ocov3.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L1aIn_Sample.11r/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L1aIn_Sample.11r/",
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
-                    "downloadURL": "https://ocov3.jpl.nasa.gov/science/publications/",
-                    "description": "Publications from the Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "Publications from the Science Team",
+                    "downloadURL": "https://ocov3.jpl.nasa.gov/science/publications/",
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
+            "identifier": "C3268212607-GES_DISC",
+            "issued": "2024-06-27",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "spectral/engineering",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3268212607-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-06-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO3_L1aIn_Sample",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-07-03T00:00:00Z/2024-10-21T00:00:00Z",
             "theme": [
                 "OCO-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-3 Level 1A collated, parsed, science or calibration data, Retrospective Processing V11r (OCO2_L1aIn_Sample) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/582L7HTJ343N",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hai Nguyen, Manju Johny, Junjie Liu, Susan Kulawik, David Baker, Jonathan Hobbs, Amy Braverman, Matthias Katzfuss, and Vineet Yadav. 2024-10-11. OCO2GriddedXCO2_SIF. Version 3. OCO-2 Gridded bias-corrected XCO2, SIF,  and other select fields aggregated as Level 3 daily files. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/582L7HTJ343N. https://disc.gsfc.nasa.gov/datacollection/OCO2GriddedXCO2_SIF_4.html. Digital Science Data.",
-            "issued": "2014-09-06",
-            "temporal": "2014-09-06T02:07:30Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-30",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
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
-            "identifier": "C3278456620-GES_DISC",
-            "description": "Gridded carbon dioxide mole fraction (XCO2) and other select variables created by applying local kriging (also known as optimal interpolation) to daily aggregates of Orbiting Carbon Observatory (OCO-2) bias corrected data.\n\nThis is the latest version of this collection. The DOIs assigned to previous versions, which are no longer available, now direct to this page.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2GriddedXCO2_SIF",
             "creator": "Hai Nguyen, Manju Johny, Junjie Liu, Susan Kulawik, David Baker, Jonathan Hobbs, Amy Braverman, Matthias Katzfuss, and Vineet Yadav",
-            "title": "OCO-2 Gridded bias-corrected XCO2, SIF, and other select fields aggregated as Level 3 daily files V4 (OCO2GriddedXCO2_SIF)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/XCO2_Data_Fusion/OCO2GriddedXCO2_3.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Gridded carbon dioxide mole fraction (XCO2) and other select variables created by applying local kriging (also known as optimal interpolation) to daily aggregates of Orbiting Carbon Observatory (OCO-2) bias corrected data.\n\nThis is the latest version of this collection. The DOIs assigned to previous versions, which are no longer available, now direct to this page.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F582L7HTJ343N",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F582L7HTJ343N",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1589815,89 +1589793,91 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2GriddedXCO2_SIF_4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2GriddedXCO2_SIF_4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/CO2/OCO2GriddedXCO2_SIF.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/CO2/OCO2GriddedXCO2_SIF.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/CO2/OCO2GriddedXCO2_SIF.4/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/CO2/OCO2GriddedXCO2_SIF.4/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2GriddedXCO2_SIF",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2GriddedXCO2_SIF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/XCO2_Data_Fusion/MEASURES_XCO2_DataUserGuide_dataVersion4.pdf",
-                    "description": "MEASURES 2017 XCO2 Data Fusion Data User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "MEASURES 2017 XCO2 Data Fusion Data User\u2019s Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/XCO2_Data_Fusion/MEASURES_XCO2_DataUserGuide_dataVersion4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/XCO2_Data_Fusion/MEASURES_XCO2_ATBDdataVersion4.pdf",
-                    "description": "MEASURES 2017 XCO2 Data Fusion Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "MEASURES 2017 XCO2 Data Fusion Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/XCO2_Data_Fusion/MEASURES_XCO2_ATBDdataVersion4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/XCO2_Data_Fusion/OCO2GriddedXCO2_3.png",
+            "identifier": "C3278456620-GES_DISC",
+            "issued": "2014-09-06",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/582L7HTJ343N",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2GriddedXCO2_SIF",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-09-06T02:07:30Z/2024-11-11T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Gridded bias-corrected XCO2, SIF, and other select fields aggregated as Level 3 daily files V4 (OCO2GriddedXCO2_SIF)"
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
-                "dictionary",
-                "pds",
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
-            "identifier": "NASA-645",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r66)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1589905,23 +1589885,45 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-645",
+            "issued": "2018-06-25",
+            "keyword": [
+                "dictionary",
+                "pds",
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
+            "title": "PDS Data Dictionary (1r66)"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-5-ddr-energetic-ion-comp-v1.0_wqww-uqiu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "io",
                 "io plasma torus",
@@ -1589932,68 +1589934,44 @@
                 "callisto",
                 "europa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-HIC-5-DDR-ENERGETIC-ION-COMP-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-5-ddr-energetic-ion-comp-v1.0_wqww-uqiu",
-            "description": "This data set provides energetic (MeV) ion fluxes for a variety of different Z values (carbon, oxygen, sulfur) derived from the Heavy Ion Counter (HIC) instrument on the Galileo spacecraft. The data set includes all recorded intervals at Jupiter.",
-            "title": "GO JUP HIC DERIVED ENERGETIC ION COMPOSITION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GO JUP HIC DERIVED ENERGETIC ION COMPOSITION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/JFLOW2CC07NG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee. 2024-04-01. OCO2_L2_Met. Version 11.2r. OCO-2 Level 2 meteorological parameters interpolated from global assimilation model for each sounding Retrospective Processing V11.2r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/JFLOW2CC07NG. https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Met_11.2r.html. Digital Science Data.",
-            "issued": "2024-04-01",
-            "temporal": "2014-06-01T00:00:00Z/2024-10-07T00:00:00Z",
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
-            "identifier": "C3090460016-GES_DISC",
-            "description": "Version 11.2r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. \n\nThis collection encompass meteorological parameters interpolated from global assimilation model for each sounding.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_Met",
             "creator": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee",
-            "title": "OCO-2 Level 2 meteorological parameters interpolated from global assimilation model for each sounding Retrospective Processing V11.2r (OCO2_L2_Met) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11.2r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. \n\nThis collection encompass meteorological parameters interpolated from global assimilation model for each sounding.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJFLOW2CC07NG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJFLOW2CC07NG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1590003,59 +1589981,59 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Met_11.2r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Met_11.2r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Met.11.2r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Met.11.2r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_Met",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_Met",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Met.11.2r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Met.11.2r/contents.html",
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
@@ -1590065,190 +1590043,188 @@
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
+            "identifier": "C3090460016-GES_DISC",
+            "issued": "2024-04-01",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/JFLOW2CC07NG",
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
+            "series-name": "OCO2_L2_Met",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-06-01T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 meteorological parameters interpolated from global assimilation model for each sounding Retrospective Processing V11.2r (OCO2_L2_Met) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/380/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-05-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Markus Ritter",
                 "hasEmail": "mailto:markus.ritter@dlr.de"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_380",
             "description": "Unstructured HIRENASD mesh:\r\n- medium size (16 million nodes, 39 million elements)\r\n- for node centered solvers\r\n- 31.05.2011\r\n- caution: dimensions in mm",
-            "title": "HIRENASD medium unstructured",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_medium_nc.cgns",
-                    "description": "HIRENASD_medium_nc",
                     "@type": "dcat:Distribution",
+                    "description": "HIRENASD_medium_nc",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_medium_nc.cgns",
+                    "mediaType": "application/octet-stream",
                     "title": "HIRENASD_medium_nc.cgns"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_medium_nc_volume.dat.gz",
-                    "description": "Tecplot ascii file",
                     "@type": "dcat:Distribution",
+                    "description": "Tecplot ascii file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_medium_nc_volume.dat.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "HIRENASD_medium_nc_volume.dat.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_medium_nc_volume.plt.gz",
-                    "description": "Tecplot binary",
                     "@type": "dcat:Distribution",
+                    "description": "Tecplot binary",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_medium_nc_volume.plt.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "HIRENASD_medium_nc_volume.plt.gz"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_380",
+            "issued": "2011-05-31",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/380/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "HIRENASD medium unstructured"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F14/GPROFCLIM/3A-DAY/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFF14SSMI_DAY_CLIM. Version 07. GPM SSMI on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SSMI/F14/GPROFCLIM/3A-DAY/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFF14SSMI_DAY_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "1997-05-01T00:00:00Z/2008-08-23T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "atmospheric water vapor",
-                "earth science",
-                "precipitation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264135246-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07. \n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3GPROFF14SSMI_DAY_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM SSMI on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF14SSMI_DAY_CLIM) at GES DISC",
-            "graphic-preview-description": "GPM SSMI on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree (GPM_3GPROFF14SSMI_DAY_CLIM)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF14SSMI_DAY_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF14%2FGPROFCLIM%2F3A-DAY%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF14%2FGPROFCLIM%2F3A-DAY%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF14SSMI_DAY_CLIM_07.png",
-                    "description": "GPM SSMI on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree (GPM_3GPROFF14SSMI_DAY_CLIM)",
                     "@type": "dcat:Distribution",
+                    "description": "GPM SSMI on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree (GPM_3GPROFF14SSMI_DAY_CLIM)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF14SSMI_DAY_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFF14SSMI_DAY_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFF14SSMI_DAY_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFF14SSMI_DAY_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFF14SSMI_DAY_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFF14SSMI_DAY_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFF14SSMI_DAY_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFF14SSMI_DAY_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFF14SSMI_DAY_CLIM_07",
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
@@ -1590258,378 +1590234,382 @@
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
+            "graphic-preview-description": "GPM SSMI on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree (GPM_3GPROFF14SSMI_DAY_CLIM)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF14SSMI_DAY_CLIM_07.png",
+            "identifier": "C2264135246-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F14/GPROFCLIM/3A-DAY/07",
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
+            "series-name": "GPM_3GPROFF14SSMI_DAY_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1997-05-01T00:00:00Z/2008-08-23T23:59:59.999Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SSMI on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF14SSMI_DAY_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M11-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m11-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M11-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m11-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP011 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP011 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1417-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-11T14:29:30.000 to 2016-02-11T22:24:17.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1417-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1417-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1417-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-11T14:29:30.000 to 2016-02-11T22:24:17.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1417 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1417 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D06.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Parameter 3 Band 2 Daily L3 Global 30 ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D06.061. https://doi.org/10.5067/MODIS/MCD43D06.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "national geospatial data asset",
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
-            "identifier": "C2532007810-LPCLOUD",
-            "description": "The MCD43D06 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter data set is a daily 16-day product. This product incorporates the Climate Modeling Grid (CMG) structure in which each file geographically covers the entire earth rather than the 10 degree x 10 degree latitude and longitude tiling system utilized by the standard MODIS land products. Unlike the standard CMG pixel resolution of 5600 meters the MCD43D products are 1000 meters, consequently, because of the large file size each product contains just one layer. The Julian date in the granule ID of each specific file represents the 9th day of the 16 day composite period, and consequently the observations are weighted to estimate the BRDF/Albedo for that day. The layer in the MCD43D06 is the Bidirectional Reflectance Distribution Function geometric parameter for MODIS band 2. This geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the Albedo and BRDF value for MODIS band 2.",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter 3 Band 2 Daily L3 Global 30 ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D06 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter data set is a daily 16-day product. This product incorporates the Climate Modeling Grid (CMG) structure in which each file geographically covers the entire earth rather than the 10 degree x 10 degree latitude and longitude tiling system utilized by the standard MODIS land products. Unlike the standard CMG pixel resolution of 5600 meters the MCD43D products are 1000 meters, consequently, because of the large file size each product contains just one layer. The Julian date in the granule ID of each specific file represents the 9th day of the 16 day composite period, and consequently the observations are weighted to estimate the BRDF/Albedo for that day. The layer in the MCD43D06 is the Bidirectional Reflectance Distribution Function geometric parameter for MODIS band 2. This geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the Albedo and BRDF value for MODIS band 2.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D06.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D06.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D06.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D06.061",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D06.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D06.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2532007810-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2532007810-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD43D06.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD43D06.061/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D06",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D06",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43D06",
-                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43D06",
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
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aquaTerra&ver=C6",
-                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aquaTerra&ver=C6",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 }
             ],
+            "identifier": "C2532007810-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D06.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter 3 Band 2 Daily L3 Global 30 ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206882-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Inventory of Rock Glaciers along the Ghunsa Valley, Kanchanjunga Himal, Eastern Nepal, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1998-01-01",
-            "temporal": "1998-01-01T00:00:00Z/1999-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1999-12-31",
-            "keyword": [
-                "frozen ground",
-                "cryosphere",
-                "earth science",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mamoru Ishikawa",
                 "hasEmail": "mailto:mishi@ees.hokudai.ac.jp"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206882-NSIDCV0",
             "description": "This dataset provides information on a number of Nepali rock glaciers distributed above 4250 m ASL along the Ghunsa valley and the Kanchanjunga glacier (originating from the summit of Mt. Kanchanjunga, 8586 m ASL). The rock glaciers were identified on the basis of air photo analysis and were visited in October and November 1999. The longitude, latitude, and elevation of each rock glacier are given. Geographic coordinates were determined using a 1:50,000 topographic map of Nepal. Two categories of rock glaciers are described: glacier-derived and talus-derived rock glaciers. The internal structure of two rock glaciers (KR4 and KR23) were investigated by DC resistivity imaging.",
-            "title": "Inventory of Rock Glaciers along the Ghunsa Valley, Kanchanjunga Himal, Eastern Nepal, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD610_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD610_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD610/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD610/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD610/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD610/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206882-NSIDCV0",
+            "issued": "1998-01-01",
+            "keyword": [
+                "frozen ground",
+                "cryosphere",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206882-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1999-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "87.833 27.667 88.167 27.833",
+            "temporal": "1998-01-01T00:00:00Z/1999-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Inventory of Rock Glaciers along the Ghunsa Valley, Kanchanjunga Himal, Eastern Nepal, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-PPR-2-EDR-EARTH2-V1.0",
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
+            "description": "ARCHIVE_STATUS, ,DATA_SET_TERSE_DESC,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Earth-2 encounter observations in November-December 1992.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-ppr-2-edr-earth2-v1.0_wr25-c79u",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-PPR-2-EDR-EARTH2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-ppr-2-edr-earth2-v1.0_wr25-c79u",
-            "description": "ARCHIVE_STATUS, ,DATA_SET_TERSE_DESC,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Earth-2 encounter observations in November-December 1992.",
-            "title": "GLL PPR EARTH-2 ENCOUNTER EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GLL PPR EARTH-2 ENCOUNTER EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/LASE/0003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2003-01-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/LASE/0003. http://eosweb.larc.nasa.gov/project/lase/lase_table.",
-            "issued": "2003-01-07",
-            "temporal": "1998-08-21T00:00:00Z/1998-09-23T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-03",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "atmospheric water vapor"
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
-            "identifier": "C1535863031-LARC_ASDC",
             "description": "LASE_CAMEX3 data are Lidar Atmospheric Sensing Experiment water vapor and aerosol data measurements taken during the 3rd Convection and Moisture Experiment (CAMEX3).LASE (Lidar Atmospheric Sensing Experiment) is an airborne autonomous DIAL system developed to measure water vapor and aerosol profiles. The Convection And Moisture EXperiment (CAMEX-3) campaign was based at Patrick Air Force Base, Florida from 6 August - 23 September, 1998. CAMEX-3 successfully studied Hurricanes Bonnie, Danielle, Earl and Georges. CAMEX-3 collected data for research in tropical cyclone development, tracking, intensification, and landfalling impacts using NASA-funded aircraft and surface remote sensing instrumentation.The CAMEX-3 study yields high spatial and temporal information of hurricane structure, dynamics, and motion. The LASE instrument's purpose in this experiment is to characterize the hurricane environment using water vapor and aerosol measurements for use as input to models and assimilation schemes and to fill in sonde data voids.",
-            "title": "Lidar Atmospheric Sensing Experiment (LASE) Data Obtained During the Convection And Moisture Experiment (CAMEX-3)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FLASE%2F0003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FLASE%2F0003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1590711,490 +1590691,488 @@
                     "title": "View this dataset's calibration documentation"
                 }
             ],
+            "identifier": "C1535863031-LARC_ASDC",
+            "issued": "2003-01-07",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/LASE/0003",
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
             "spatial": "-85.9 14.1 -63.0 39.0",
+            "temporal": "1998-08-21T00:00:00Z/1998-09-23T23:59:59Z",
             "theme": [
                 "LASE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Lidar Atmospheric Sensing Experiment (LASE) Data Obtained During the Convection And Moisture Experiment (CAMEX-3)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V3.0",
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
+            "description": "IAU-adopted magnitude parameters (absolute V magnitude and slope parameter) for all numbered asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v3.0_wr2v-z63r",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v3.0_wr2v-z63r",
-            "description": "IAU-adopted magnitude parameters (absolute V magnitude and slope parameter) for all numbered asteroids.",
-            "title": "ASTEROID ABSOLUTE MAGNITUDES V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID ABSOLUTE MAGNITUDES V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5PN93HT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Great Lakes Daily Ice Observations at NOAA Water Level Gauge Sites, 1956 - 1997, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5PN93HT.",
-            "issued": "1956-11-01",
-            "temporal": "1956-11-01T00:00:00Z/1997-04-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-04-30",
-            "keyword": [
-                "cryosphere",
-                "snow/ice",
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
-            "identifier": "C2205522271-NSIDCV0",
             "description": "This data set contains daily visual ice observations taken yearly from 1 November to 30 April at NOAA/National Ocean Service water level gauge sites in the Great Lakes Basin from 1956 to the 1997. Not all gauge sites have reported each season; a list of sites with coordinates and reporting years is included with the data set. The longest records tend to be at river stations such as St. Clair, St. Marys, Detroit, and St. Lawrence. Daily observations are coded (open water, solid ice, honeycombed ice, slush ice, windrowed ice, drifting ice, or ice gorge), as well as first and last reported ice for each season.",
-            "title": "Great Lakes Daily Ice Observations at NOAA Water Level Gauge Sites, 1956 - 1997, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5PN93HT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5PN93HT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G00945_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G00945_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5PN93HT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5PN93HT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5PN93HT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5PN93HT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2205522271-NSIDCV0",
+            "issued": "1956-11-01",
+            "keyword": [
+                "cryosphere",
+                "snow/ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5PN93HT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1997-04-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-93.0 41.0 -75.0 49.0",
+            "temporal": "1956-11-01T00:00:00Z/1997-04-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Great Lakes Daily Ice Observations at NOAA Water Level Gauge Sites, 1956 - 1997, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-ASTR-2-EDR-HALLEY-V2.0",
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
-                "1p/halley 1 (1682 q1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Astrometry Net of the International Halley Watch (IHW) compiled astrometric observations of comet 1P/Halley from observations made by professional astronomers from ground-based observatories all over the world. The data set comprises 6475 astrometric observations over the period 16 Oct 1982 through 9 Jan 1989, in addition to 158 observations from the 1835 apparition and 1696 observations from the 1910 apparition. The data from previous apparitions was re-reduced using modern star catalogs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-astr-2-edr-halley-v2.0_wr49-w5vg",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "1p/halley 1 (1682 q1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-ASTR-2-EDR-HALLEY-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-astr-2-edr-halley-v2.0_wr49-w5vg",
-            "description": "The Astrometry Net of the International Halley Watch (IHW) compiled astrometric observations of comet 1P/Halley from observations made by professional astronomers from ground-based observatories all over the world. The data set comprises 6475 astrometric observations over the period 16 Oct 1982 through 9 Jan 1989, in addition to 158 observations from the 1835 apparition and 1696 observations from the 1910 apparition. The data from previous apparitions was re-reduced using modern star catalogs.",
-            "title": "IHW COMET HALLEY ASTROMETRIC DATA, V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY ASTROMETRIC DATA, V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/OT8OC3DBY70R",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Arctic Water Vapor Characteristics from Rawinsondes, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/OT8OC3DBY70R.",
-            "issued": "1954-01-01",
-            "temporal": "1954-01-01T00:00:00Z/1991-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1991-12-31",
-            "keyword": [
-                "atmospheric pressure",
-                "altitude",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "earth science",
-                "atmospheric temperature",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Serreze",
                 "hasEmail": "mailto:serreze@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386246952-NSIDCV0",
             "description": "A gridded climatological monthly-mean data base of Arctic water vapor characteristics has been assembled by combining fixed station data with data from soundings taken over the Arctic Ocean from ships and Russian drifting stations.\n\nVariables provided include temperature, specific humidity, zonal vapor flux, meridional vapor flux, zonal wind speed, and meridional wind speed, available for 15 pressure levels extending from the surface (1,000 mb) to 300 mb. Sea level pressure and geopotential height are provided for the 850 mb, 700 mb, 500 mb and 300 mb levels. Precipitable water, vertically integrated zonal vapor flux and vertically integrated meridional vapor flux are available for five layers: surface to 850 mb, 850 to 700 mb, 700 to 500 mb, 500 to 400 mb and 400 to 300 mb.\n\nCoverage of the rawinsonde archives extends from 1954 through 1990 for data from the Russian North Pole series of drifting ice stations over the Arctic Ocean; from 1976 through 1991 for fixed-station data obtained from the National Center for Atmospheric Research; and from about 1958 through 1991 for fixed-station data obtained from the Historical Arctic Rawinsonde Archive.\n\nAll variables were obtained through interpolation of the raw sounding data, with the exception of sea level pressure and geopotential height. The files are structured in monthly data arrays over a subsection of the National Meteorological Center grid (octagonal grid format) centered over the pole, extending to approximately 65 degrees North on each side and about 55 degrees North at the corners.",
-            "title": "Arctic Water Vapor Characteristics from Rawinsondes, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOT8OC3DBY70R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOT8OC3DBY70R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/WATERVAPOR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/WATERVAPOR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/OT8OC3DBY70R",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/OT8OC3DBY70R",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/OT8OC3DBY70R",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/OT8OC3DBY70R",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246952-NSIDCV0",
+            "issued": "1954-01-01",
+            "keyword": [
+                "atmospheric pressure",
+                "altitude",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/OT8OC3DBY70R",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1991-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 65.0 180.0 90.0",
+            "temporal": "1954-01-01T00:00:00Z/1991-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic Water Vapor Characteristics from Rawinsondes, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3H2OM.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3H2OM.005. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-03T00:00:00Z/2018-01-24T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric pressure"
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
-            "identifier": "C1536988697-LARC",
             "description": "TL3H2OM_5 is the Tropospheric Emission Spectrometer (TES)/Aura Level 3 Water Vapor Monthly Gridded Version 5 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. This data product consists of monthly atmospheric temperature and volume mixing ratios (VMRs) for the Water Vapor atmospheric species, which are provided at 2 degree latitude by 4 degree longitude spatial grids and at a subset of TES standard pressure levels.\r\rThe TES Science Data Processing L3 subsystem interpolated L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products are composed of L3 HDF-EOS grid data. A separate product file was produced for each different atmospheric species. TES obtained data in two basic observation modes: Limb or Nadir; Nadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing were the terms Daily and Monthly representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey was not split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represented a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products were daily and monthly.",
-            "title": "TES/Aura L3 Water Vapor Monthly Gridded V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3H2OM.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3H2OM.005",
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3H2OM.005",
-                    "description": "DOI data set landing page for TL3H2OM_5",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3H2OM_5",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3H2OM.005",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://gs614-avdc1-pz.gsfc.nasa.gov/Overview/",
-                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena, CA, USA",
                     "@type": "dcat:Distribution",
+                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena, CA, USA",
+                    "downloadURL": "https://gs614-avdc1-pz.gsfc.nasa.gov/Overview/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://portal.hdfgroup.org/display/support",
-                    "description": "HDF Support Portal",
                     "@type": "dcat:Distribution",
+                    "description": "HDF Support Portal",
+                    "downloadURL": "https://portal.hdfgroup.org/display/support",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3H2OM.005/",
-                    "description": "ASDC Direct Data Download for TL3H2OM_5",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL3H2OM_5",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3H2OM.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3H2OM.005/contents.html",
-                    "description": "OPeNDAP data access for TL3H2OM_5",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL3H2OM_5",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3H2OM.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536988697-LARC",
-                    "description": "Earthdata Search for TL3H2OM_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL3H2OM_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536988697-LARC",
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
+            "identifier": "C1536988697-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3H2OM.005",
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
+            "title": "TES/Aura L3 Water Vapor Monthly Gridded V005"
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
-                "models",
-                "turbulence",
-                "cases",
-                "incompressible"
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
-            "identifier": "NASA-842__9",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1591202,570 +1591180,564 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__9",
+            "issued": "2018-06-25",
+            "keyword": [
+                "flow",
+                "models",
+                "turbulence",
+                "cases",
+                "incompressible"
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
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-07-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Padonia_Data_1.",
-            "issued": "2021-06-10",
-            "temporal": "2011-06-17T00:00:00Z/2011-08-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-20",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C2358890638-LARC_ASDC",
             "description": "DISCOVERAQ_Maryland_Ground_Padonia_Data contains data collected at the Padonia ground site during the Maryland (Baltimore-Washington) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Maryland deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Maryland Deployment Padonia Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Ground_Padonia_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Ground_Padonia_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
-                    "description": "DOI for DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2358890638-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2358890638-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Ground_Padonia_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Ground_Padonia_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2358890638-LARC_ASDC",
+            "issued": "2021-06-10",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Padonia_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>30.0 -85.0 30.0 -70.0 45.0 -70.0 45.0 -85.0 30.0 -85.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2011-06-17T00:00:00Z/2011-08-03T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Maryland Deployment Padonia Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_M_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, Hourly 30-second compressed meteorological data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/gnss_hourly_m_001",
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
-            "identifier": "C1419766544-CDDIS",
             "description": "This dataset consists of ground-based Meteorological Data (hourly, 24 hour files) from instruments co-located with Global Navigation Satellite System (GNSS) receivers from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The hourly meteorological data files contain one day of meteorological data (temperature, pressure, humidity, etc.) in RINEX format from a global permanent network of ground-based receivers, one file per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/hourly_30second_data.html.",
-            "title": "Ground-Based Meteorological Data (hourly files) from Co-Located Global Navigation Satellite System (GNSS) Receivers from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HOURLY_M_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HOURLY_M_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/hourly",
-                    "description": "URL for retrieval of GNSS hourly meteorological data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS hourly meteorological data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/hourly",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/hourly_30second_data.html",
-                    "description": "URL for more information about GNSS hourly meteorological data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS hourly meteorological data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/hourly_30second_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_M_001",
-                    "description": "URL for more information about GNSS hourly meteorological data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS hourly meteorological data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_M_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1419766544-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_M_001",
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
+            "title": "Ground-Based Meteorological Data (hourly files) from Co-Located Global Navigation Satellite System (GNSS) Receivers from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/CERES/NEWS_CCCM-FM3-MODIS-CAL-CS_L2.RELB1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2011-03-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AQUA/CERES/NEWS_CCCM-FM3-MODIS-CAL-CS_L2.RELB1.",
-            "issued": "2013-12-10",
-            "temporal": "2006-07-01T00:00:00Z/2011-04-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-03-07",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "surface radiative properties",
-                "ngda",
-                "national geospatial data asset",
-                "land surface",
-                "atmospheric winds",
-                "clouds"
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
-            "identifier": "C5769450-LARC_ASDC",
             "description": "CER-NEWS_CCCM_Aqua-FM3-MODIS-CAL-CS_RelB1 is the Clouds and the Earth's Radiant Energy System (CERES) NASA Energy and Water cycle Study (NEWS) A-Train Integrated Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO), loudSat Cloudsat, CERES, and Moderate-Resolution Imaging Spectroradiometer (MODIS) (CCCM) Merged Release B1 data product. Data was collected using the CALIOP on CALIPSO and CERES Flight Model 3 (FM3), CERES Scanner, MODIS, and Cloudsat on Aqua. Data collection for this product is complete. \r\n\r\nThe CER-NEWS_CCCM_Aqua-FM3-MODIS-CAL-CS_RelB1 contains the current CERES CCCM data. The CALIPSO-CloudSat-CERES-MODIS (CCCM) data set integrates measurements from the CALIPSO CALIOP instrument, CloudSat Cloud Profiling Radar (CPR), CERES, and the MODIS data. The cloud and aerosol properties from CALIOP and cloud properties from the CPR are matched to a MODIS pixel and then an Aqua CERES footprint. The product contains only the CERES footprint in each scan that has the highest CALIPSO and CloudSat ground track coverage. The product consists of all cloud and aerosol properties derived from MODIS radiances included in the Single Scanner Footprint (SSF) product and computed irradiances included in the Cloud Radiative Swath (CRS) product. Two sets of SSF variables are included in the CCCM data. One set covers the entire CERES footprint and the other set is only over CALIOP and CPR ground track. CERES derived top-of-atmosphere (TOA) shortwave (SW), longwave (LW) and window (WN) irradiances by angular distribution models are also included. In addition, irradiance profiles computed by a radiative transfer model using MODIS, CALIOP, and CPR derived aerosol, clouds, and surface properties are included in the product. Furthermore, MODIS-derived cloud properties from the algorithm that incorporates CALIOP and CPR cloud information are also included. \r\n\r\nMODIS-derived cloud properties and TOA irradiances derived from CERES radiances are produced by the same algorithm that produces CERES SSF and CRS products. However, the CCCM product should not be considered as a climate data record since various input data product versions and algorithm modifications will occur along the course of the measurement period. The scan and packet numbers unique to the CERES footprint provide the means to match the data to other CERES products, although the CCCM product contains more near nadir CERES footprints compared with SSF and CRS products. The resulting HDF granule contains 24 hours of data.CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. \r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES A-Train Integrated CALIPSO, CloudSat, CERES, and MODIS (CCCM) Merged Release B1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FNEWS_CCCM-FM3-MODIS-CAL-CS_L2.RELB1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FNEWS_CCCM-FM3-MODIS-CAL-CS_L2.RELB1",
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
-                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/NEWS_CCCM-FM3-MODIS-CAL-CS_L2.RELB1",
-                    "description": "DOI data set landing page for CER-NEWS_CCCM_Aqua-FM3-MODIS-CAL-CS_RelB1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER-NEWS_CCCM_Aqua-FM3-MODIS-CAL-CS_RelB1",
+                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/NEWS_CCCM-FM3-MODIS-CAL-CS_L2.RELB1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C5769450-LARC_ASDC",
-                    "description": "Earthdata Search for CER-NEWS_CCCM_Aqua-FM3-MODIS-CAL-CS_RelB1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER-NEWS_CCCM_Aqua-FM3-MODIS-CAL-CS_RelB1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C5769450-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_CER-NEWS_CCCM_SampleRead_RelB-v1.txt",
-                    "description": "Readme Information on the CER-NEWS_CCCM_Aqua-FM3-MODIS-CAL-CS_RelB1 Data Set",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information on the CER-NEWS_CCCM_Aqua-FM3-MODIS-CAL-CS_RelB1 Data Set",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_CER-NEWS_CCCM_SampleRead_RelB-v1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_NEWS_RelB1.pdf",
-                    "description": "Quality Summary: CERES NEWS CCCM Rel B1",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES NEWS CCCM Rel B1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_NEWS_RelB1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/c3m_variables_B1_v2.pdf",
-                    "description": "Variable Descriptions of the A-Train Integrated CALIPSO, CloudSat, CERES, and MODIS Merged Product (CCCM or C3M), CloudSat, CERES, and MODIS Merged Product (CCCM or C3M), 2/6/2014",
                     "@type": "dcat:Distribution",
+                    "description": "Variable Descriptions of the A-Train Integrated CALIPSO, CloudSat, CERES, and MODIS Merged Product (CCCM or C3M), CloudSat, CERES, and MODIS Merged Product (CCCM or C3M), 2/6/2014",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/c3m_variables_B1_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/CER-NEWS_CCCM_SampleRead_RelB-v1.zip",
-                    "description": "Read Software Package - CERES-NEWS CCCM Release B1. - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - CERES-NEWS CCCM Release B1. - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/CER-NEWS_CCCM_SampleRead_RelB-v1.zip",
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
```

