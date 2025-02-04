# Change History for nasa.json (Part 92)

### Changes from 31606f9 to dd2190f (Part 81/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02186/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/data/masie",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "http://nsidc.org/data/masie",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02186/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02186/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/data/masie",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "http://nsidc.org/data/masie",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5GT5K3K",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5GT5K3K",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5GT5K3K",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5GT5K3K",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246275-NSIDCV0",
+            "issued": "2006-01-01",
+            "keyword": [
+                "oceans",
+                "national geospatial data asset",
+                "earth science",
+                "sea ice",
+                "ngda",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5GT5K3K",
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
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "2006-01-01T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Multisensor Analyzed Sea Ice Extent  - Northern Hemisphere (MASIE-NH), Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-3-IRBTR-V1.0",
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
-                "2001 mars odyssey",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The THEMIS IR-BTR data set contains the brightness temperature records, derived from the calibrated thermal infrared observations. Each image header includes basic parameters describing the observation and geometric parameters for the center of the observation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-3-irbtr-v1.0_h5nf-bmdu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "2001 mars odyssey",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-3-IRBTR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-3-irbtr-v1.0_h5nf-bmdu",
-            "description": "The THEMIS IR-BTR data set contains the brightness temperature records, derived from the calibrated thermal infrared observations. Each image header includes basic parameters describing the observation and geometric parameters for the center of the observation.",
-            "title": "ODYSSEY THEMIS IR BTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ODYSSEY THEMIS IR BTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/EYXLPVGTSWFF",
             "citation": "Kevin W. Bowman. 2021-05-27. TRPSDL2NH3AIRSFS. Version 1. TROPESS AIRS-Aqua L2 Ammonia for Forward Stream, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/EYXLPVGTSWFF. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2NH3AIRSFS_1.html. Digital Science Data.",
-            "issued": "2021-05-22",
-            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-22",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1109/TGRS.2006.871234",
-                "https://doi.org/10.5194/amt-8-1323-2015",
-                "https://doi.org/10.5194/acp-11-10743-2011"
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
-            "identifier": "C2041965834-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS AIRS-Aqua L2 Ammonia for Forward Stream, Standard Product contains the vertical distribution of the retrieved atmospheric state of ammonia (NH3), formal uncertainties, and diagnostic information measured by the AIRS instrument on the EOS Aqua satellite. The forward stream standard product is global for the time period from 2021-02-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 13.5 km (AIRS nadir FOV), and are reported at 15 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2NH3AIRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS AIRS-Aqua NH3 (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS AIRS-Aqua L2 Ammonia for Forward Stream, Standard Product V1 (TRPSDL2NH3AIRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2NH3AIRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEYXLPVGTSWFF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEYXLPVGTSWFF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2NH3AIRSFS_Sample.png",
-                    "description": "TROPESS AIRS-Aqua NH3 (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS AIRS-Aqua NH3 (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2NH3AIRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2NH3AIRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2NH3AIRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2NH3AIRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2NH3AIRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2NH3AIRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2NH3AIRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2NH3AIRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2NH3AIRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2NH3AIRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2NH3AIRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_NH3_L2_Product_User_Guide_2-22-21.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_NH3_L2_Product_User_Guide_2-22-21.pdf",
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
+            "graphic-preview-description": "TROPESS AIRS-Aqua NH3 (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2NH3AIRSFS_Sample.png",
+            "identifier": "C2041965834-GES_DISC",
+            "issued": "2021-05-22",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/EYXLPVGTSWFF",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.1109/TGRS.2006.871234",
+                "https://doi.org/10.5194/amt-8-1323-2015",
+                "https://doi.org/10.5194/acp-11-10743-2011"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2NH3AIRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS AIRS-Aqua L2 Ammonia for Forward Stream, Standard Product V1 (TRPSDL2NH3AIRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/h5pe-bcfp",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2022-07-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "imerg",
-                "precipitation",
-                "modis",
-                "cloud",
-                "cloud-precipitation hybrid regime"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daeho Jin",
                 "hasEmail": "mailto:Daeho.Jin@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Daeho Jin (Code613 in NASA GSFC)"
-            },
-            "identifier": "https://data.nasa.gov/api/views/h5pe-bcfp",
             "description": "Cloud-Precipitation Hybrid Regimes with MODIS C6.1 2D joint histogram of CTP and COT (total 42 bins) and IMERG v06B precipitation histogram (total 6 bins) derived in 15S-15N domain.\nThis version is for precip weight=1, so cloud:precip = 7:1 ratio. (See details in Jin et al. 2021, https://doi.org/10.1175/JAMC-D-20-0253.1)\n\nThe dataset is composed of one netCDF file, which includes centroids, CPR-numbers-on-map for Terra, Aqua, and TAmean, and UTC info for Terra and Aqua observations (2002.07.16 to 2021.09.29).",
-            "title": "Tropical Cloud-Precip (hybrid) Regime, Pr6x1 set",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -846732,41 +846712,43 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/h5pe-bcfp",
+            "issued": "2022-07-04",
+            "keyword": [
+                "imerg",
+                "precipitation",
+                "modis",
+                "cloud",
+                "cloud-precipitation hybrid regime"
+            ],
+            "landingPage": "https://data.nasa.gov/d/h5pe-bcfp",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Daeho Jin (Code613 in NASA GSFC)"
+            },
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Tropical Cloud-Precip (hybrid) Regime, Pr6x1 set"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/h5pw-8kxj",
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
-            "identifier": "NASA-0000038__41",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -846774,243 +846756,239 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__41",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "space science",
+                "nen",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/h5pw-8kxj",
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
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1758",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Joiner, J., Y. Yoshida, P. Koehler, C. Frankenberg, and N.C. Parazoo. 2019. L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1758",
-            "issued": "2022-01-09",
-            "temporal": "1995-07-01T00:00:00Z/2003-06-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "surface radiative properties",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
-                "vegetation",
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
-            "identifier": "C2207946101-ORNL_CLOUD",
             "description": "This dataset provides Level 2 Solar-Induced Fluorescence (SIF) of Chlorophyll estimates derived from the Global Ozone Monitoring Experiment (GOME) instrument on the European Space Agency's (ESA's) European Remote-Sensing 2 (ERS-2) satellite. Each file contains daily raw and bias-adjusted solar-induced fluorescence on an orbital basis (land pixels only), at a resolution of 40 km x 320 km, along with quality control information and ancillary data. Data is provided for the period from 19950701 to 20030622. The GOME SIF product is inherently noisy due to low signal levels and has undergone only a limited amount of validation.",
-            "graphic-preview-description": "Figure 1: Solar-Induced Fluorescence derived along ERS2 GOME orbital tracks on 1 July 1995.",
-            "title": "L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003",
-            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1758",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1758",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1758",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1758",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/comp/ERS2_GOME_SIF.pdf",
-                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003: ERS2_GOME_SIF.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003: ERS2_GOME_SIF.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/comp/ERS2_GOME_SIF.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/comp/README_ERSGOME-F_v28.pdf",
-                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003: README_ERSGOME-F_v28.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003: README_ERSGOME-F_v28.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/comp/README_ERSGOME-F_v28.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF_Fig1.png",
-                    "description": "Figure 1: Solar-Induced Fluorescence derived along ERS2 GOME orbital tracks on 1 July 1995.",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: Solar-Induced Fluorescence derived along ERS2 GOME orbital tracks on 1 July 1995.",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF_Fig1.png",
+                    "mediaType": "image/png",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1758/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1758/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Figure 1: Solar-Induced Fluorescence derived along ERS2 GOME orbital tracks on 1 July 1995.",
+            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF_Fig1.png",
+            "identifier": "C2207946101-ORNL_CLOUD",
+            "issued": "2022-01-09",
+            "keyword": [
+                "surface radiative properties",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "vegetation",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1758",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1995-07-01T00:00:00Z/2003-06-22T23:59:59Z",
             "theme": [
                 "SIF-ESDR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67PCHURYUMOV-M22-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67pchuryumov-m22-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67PCHURYUMOV-M22-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67pchuryumov-m22-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP022 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP022 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-RSS-1-ROCC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-rss-1-rocc-v1.0_h5tb-z8j2",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "comet sl9/jupiter collision",
                 "saturn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-RSS-1-ROCC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-rss-1-rocc-v1.0_h5tb-z8j2",
-            "description": "not applicable",
-            "title": "VOYAGER 2 SATURN RADIO OCCULTATION RAW DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 2 SATURN RADIO OCCULTATION RAW DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3219",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Read, W., Livesey, N., and Fuller, R.. 2020-04-20. ML3MBRHI. Version 004. MLS/Aura Level 3 Monthly Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3219. https://disc.gsfc.nasa.gov/datacollection/ML3MBRHI_004.html. Digital Science Data.",
-            "issued": "2020-03-06",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-06",
-            "keyword": [
-                "atmospheric water vapor",
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
-            "identifier": "C1725339717-GES_DISC",
-            "description": "ML3MBRHI is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for relative humidity with respect to ice (RHI) derived from radiances measured by the 118 and 190 GHz radiometers. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 316 to 0.0215 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3MBRHI data product should read chapter 4 and section 3.20 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3MBRHI",
             "creator": "Read, W., Livesey, N., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Monthly Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V004 (ML3MBRHI) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBRHI_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3MBRHI is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for relative humidity with respect to ice (RHI) derived from radiances measured by the 118 and 190 GHz radiometers. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 316 to 0.0215 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3MBRHI data product should read chapter 4 and section 3.20 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3219",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3219",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -847020,713 +846998,713 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBRHI_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBRHI_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBRHI.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBRHI.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBRHI.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBRHI.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBRHI_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBRHI_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBRHI_004.png",
+            "identifier": "C1725339717-GES_DISC",
+            "issued": "2020-03-06",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3219",
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
+            "series-name": "ML3MBRHI",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Monthly Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V004 (ML3MBRHI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1703",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bourgeau-Chavez, L.L., M. Battaglia, E.S. Kane, L.M. Cohen, and D. Tanzer. 2019. ABoVE: Post-Fire and Unburned Vegetation Community and Field Data, NWT, Canada, 2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1703",
-            "issued": "2019-08-30",
-            "temporal": "2018-08-12T00:00:00Z/2018-08-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
-                "vegetation",
-                "soils",
-                "natural hazards",
-                "human dimensions",
-                "ecological dynamics",
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
-            "identifier": "C2143403376-ORNL_CLOUD",
             "description": "This dataset provides vegetation community characteristics and biophysical data collected in 2018 from areas that were burned by wildfire in 2014 and 2015, and from nine unburned validation sites in the Northwest Territories, Canada. The data include vegetation inventories, ground cover, regrowth, tree diameter and height, and woody seedling/sprouting data at burned sites, and similar vegetation community characterization at unburned validation sites. Additional measurements included soil moisture, collected for validation of the UAVSAR airborne collection, and depth to frozen ground at the nine unburned sites. This 2018 fieldwork completes four years of field sampling at the wildfire areas.",
-            "graphic-preview-description": "Investigators collected field data and inventoried plots for vegetation species and growth in 2018 at a post-burn site (image provided by Laura Bourgeau-Chavez).",
-            "title": "ABoVE: Post-Fire and Unburned Vegetation Community and Field Data, NWT, Canada, 2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Wildfires_NWT_Canada_2018_Fig1.JPG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1703",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1703",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Wildfires_NWT_Canada_2018/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Wildfires_NWT_Canada_2018/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wildfires_NWT_Canada_2018.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wildfires_NWT_Canada_2018.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1703",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1703",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Wildfires_NWT_Canada_2018/comp/Wildfires_NWT_Canada_2018.pdf",
-                    "description": "ABoVE: Post-Fire Vegetation, Soil Moisture, and Biophysical Data, NWT, Canada, 2018: Wildfires_NWT_Canada_2018.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Post-Fire Vegetation, Soil Moisture, and Biophysical Data, NWT, Canada, 2018: Wildfires_NWT_Canada_2018.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Wildfires_NWT_Canada_2018/comp/Wildfires_NWT_Canada_2018.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wildfires_NWT_Canada_2018_Fig1.JPG",
-                    "description": "Investigators collected field data and inventoried plots for vegetation species and growth in 2018 at a post-burn site (image provided by Laura Bourgeau-Chavez).",
                     "@type": "dcat:Distribution",
+                    "description": "Investigators collected field data and inventoried plots for vegetation species and growth in 2018 at a post-burn site (image provided by Laura Bourgeau-Chavez).",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wildfires_NWT_Canada_2018_Fig1.JPG",
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
+            "graphic-preview-description": "Investigators collected field data and inventoried plots for vegetation species and growth in 2018 at a post-burn site (image provided by Laura Bourgeau-Chavez).",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Wildfires_NWT_Canada_2018_Fig1.JPG",
+            "identifier": "C2143403376-ORNL_CLOUD",
+            "issued": "2019-08-30",
+            "keyword": [
+                "land surface",
+                "vegetation",
+                "soils",
+                "natural hazards",
+                "human dimensions",
+                "ecological dynamics",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1703",
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
             "spatial": "-117.43 60.45 -113.42 62.57",
+            "temporal": "2018-08-12T00:00:00Z/2018-08-22T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Post-Fire and Unburned Vegetation Community and Field Data, NWT, Canada, 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHVRS-2PN02",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Naval Oceanographic Office. 2012-04-11. GHRSST Level 2P 1 m Depth Global Sea Surface Temperature from VIIRS on Suomi NPP (GDS2) V1. Version 1.0. Stennis Space Center, MS, USA. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHVRS-2PN02.",
-            "issued": "2013-04-02",
-            "temporal": "2013-05-20T17:28:00Z/2016-02-25T23:45:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bruce McKenzie",
                 "hasEmail": "mailto:bruce.mckenzie@navy.mil"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C1996881807-POCLOUD",
-            "description": "A global Group for High Resolution Sea Surface Temperature (GHRSST) Level 2P dataset based on retrievals from the Visible Infrared Imaging Radiometer Suite (VIIRS). This sensor resides on the Suomi National Polar-orbiting Operational Environmental Satellite System (NPOESS) Preparatory Project (NPP) satellite launched on 28 October 2011.\r\nThe VIIRS instrument is a a 22-band, multi-spectral scanning radiometer with a 3040-km swath width that builds on the heritage of the MODIS , AVHRR and SeaWIFS sensors for sea surface temperature (SST) and ocean color. For the infrared bands for SST the effective pixel size is 740 meters at nadir and the pixel size variation across the swath is constrained to no more than 1600 meters at the edge of the swath.  However, the processing of this dataset aggregates two pixels into one so the resolution is 1500 meters at nadir. This dataset adheres to the GHRSST Data Processing Specification (GDS) version 2 format specifications.",
-            "release-place": "Stennis Space Center, MS, USA",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Naval Oceanographic Office",
-            "title": "GHRSST Level 2P 1 m Depth Global Sea Surface Temperature from VIIRS on Suomi NPP (GDS2) V1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-NAVO-L2P-v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A global Group for High Resolution Sea Surface Temperature (GHRSST) Level 2P dataset based on retrievals from the Visible Infrared Imaging Radiometer Suite (VIIRS). This sensor resides on the Suomi National Polar-orbiting Operational Environmental Satellite System (NPOESS) Preparatory Project (NPP) satellite launched on 28 October 2011.\r\nThe VIIRS instrument is a a 22-band, multi-spectral scanning radiometer with a 3040-km swath width that builds on the heritage of the MODIS , AVHRR and SeaWIFS sensors for sea surface temperature (SST) and ocean color. For the infrared bands for SST the effective pixel size is 740 meters at nadir and the pixel size variation across the swath is constrained to no more than 1600 meters at the edge of the swath.  However, the processing of this dataset aggregates two pixels into one so the resolution is 1500 meters at nadir. This dataset adheres to the GHRSST Data Processing Specification (GDS) version 2 format specifications.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHVRS-2PN02",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHVRS-2PN02",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-NAVO-L2P-v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-NAVO-L2P-v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
-                    "description": "GHRSST Data User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Data User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "GHRSST Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project Page",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1996881807-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1996881807-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1996881807-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1996881807-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-NAVO-L2P-v1.0.jpg",
+            "identifier": "C1996881807-POCLOUD",
+            "issued": "2013-04-02",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHVRS-2PN02",
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
+            "release-place": "Stennis Space Center, MS, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2013-05-20T17:28:00Z/2016-02-25T23:45:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 2P 1 m Depth Global Sea Surface Temperature from VIIRS on Suomi NPP (GDS2) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD09CMA.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2021-02-07. MODIS/Aqua Aerosol Optical Thickness Daily L3 Global 0.05-Deg CMA NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MYD09CMA.NRT.061.",
-            "issued": "2021-02-07",
-            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "earth science",
-                "national geospatial data asset",
-                "ngda"
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
-            "identifier": "C2007652084-LANCEMODIS",
-            "description": "The MODIS/Aqua Aerosol Optical Thickness Daily L3 Global 0.05-Deg CMA Near Real Time (NRT), short name MYD09CMA, is a daily level 3 global product. It is in linear latitude and longitude (Plate Carre) projection with a 0.05Deg spatial resolution. This product is derived from MYD09IDN, MYD09IDT and MYD09IDS for each orbit by compositing the data on the basis of minimum band 3 (459 - 479 nm band) values (after excluding pixels flagged for clouds and high solar zenith angles).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Aqua Aerosol Optical Thickness Daily L3 Global 0.05-Deg CMA NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Aerosol Optical Thickness Daily L3 Global 0.05-Deg CMA Near Real Time (NRT), short name MYD09CMA, is a daily level 3 global product. It is in linear latitude and longitude (Plate Carre) projection with a 0.05Deg spatial resolution. This product is derived from MYD09IDN, MYD09IDT and MYD09IDS for each orbit by compositing the data on the basis of minimum band 3 (459 - 479 nm band) values (after excluding pixels flagged for clouds and high solar zenith angles).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09CMA.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09CMA.NRT.061",
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
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MYD09CMA",
-                    "description": "Direct access to the download site and directory hosting the MYD09CMA 6.1NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MYD09CMA 6.1NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MYD09CMA",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2007652084-LANCEMODIS",
+            "issued": "2021-02-07",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD09CMA.NRT.061",
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
             "spatial": "-180.0 -81.0 180.0 81.0",
+            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "Aqua",
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Aerosol Optical Thickness Daily L3 Global 0.05-Deg CMA NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A15A-L-HFE-3-THERMAL-CONDUCTIVITY-V1.0",
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
-                "moon",
-                "apollo 15"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set comprises a reduced, subsampled set of the data returned from the Apollo 15 Heat Flow Experiment from 31 July 1971 through 31 December 1974. The experiment consisted of two probes placed by the Apollo 15 astronauts in holes drilled in the lunar surface near the Apollo 15 Lunar Surface Experiments Package site to measure the thermal conductivity. The data consist of a set of ten ASCII tables with time, temperature differences, and average temperatures readings measured by the thermocouples in the heat flow probes and probe cables. The data have been restored and reformatted from binary data held on magnetic tapes at the NASA National Space Science Data Center (NSSDC) under NSSDC ID of PSPG-00093 (old NSSDC ID 71-063C-06A).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a15a-l-hfe-3-thermal-conductivity-v1.0_h5vu-3bxs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "apollo 15"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A15A-L-HFE-3-THERMAL-CONDUCTIVITY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a15a-l-hfe-3-thermal-conductivity-v1.0_h5vu-3bxs",
-            "description": "This data set comprises a reduced, subsampled set of the data returned from the Apollo 15 Heat Flow Experiment from 31 July 1971 through 31 December 1974. The experiment consisted of two probes placed by the Apollo 15 astronauts in holes drilled in the lunar surface near the Apollo 15 Lunar Surface Experiments Package site to measure the thermal conductivity. The data consist of a set of ten ASCII tables with time, temperature differences, and average temperatures readings measured by the thermocouples in the heat flow probes and probe cables. The data have been restored and reformatted from binary data held on magnetic tapes at the NASA National Space Science Data Center (NSSDC) under NSSDC ID of PSPG-00093 (old NSSDC ID 71-063C-06A).",
-            "title": "APOLLO 15 HEAT FLOW THERMAL CONDUCTIVITY RDR SUBSAMPLED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "APOLLO 15 HEAT FLOW THERMAL CONDUCTIVITY RDR SUBSAMPLED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/970",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sietse, O.L., F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2010. ISLSCP II FASIR-adjusted NDVI Biophysical Parameter Fields, 1982-1998. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/970",
-            "issued": "2023-10-15",
-            "temporal": "1982-01-01T00:00:00Z/1998-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
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
-            "identifier": "C2784891689-ORNL_CLOUD",
             "description": "The Fourier-Adjusted, Sensor and Solar zenith angle corrected, Interpolated, Reconstructed (FASIR) adjusted Normalized Difference Vegetation Index (NDVI) data set and derived biophysical parameter fields were generated to provide a 17-year, satellite record of monthly changes in the photosynthetic activity of terrestrial vegetation. This multiple resolution (1/4, 1/2 and 1 degree in latitude and longitude) biophysical parameter data set contains essential variables for the calculation of photosynthesis, and the energy and water exchange between the Earth's surface (in particular of vegetation) and the lower boundary layer of the atmosphere. The Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is related to the light absorption and the photosynthetic capacity of vegetation. It also serves as an intermediate variable to calculate vegetation cover fraction (Vcover), total Leaf Area Index (LAI_T), green leaf area index (LAI_G), roughness length (z0), zero plane displacement (d), and snow-free albedo. The biophysical parameters were derived assuming one canopy layer. The production of the FASIR NDVI data set and its associated biophysical parameters was funded by NASA's Land Surface Hydrology program and the Higher Education Funding Council for Wales (HEFCW) as a core component of the International Satellite Land Surface Climatology Project (ISLSCP) Initiative II Data Collection.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II FASIR-adjusted NDVI Biophysical Parameter Fields, 1982-1998",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/970_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F970",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F970",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/vegetation/fasir_biophys_monthly_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/vegetation/fasir_biophys_monthly_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/fasir_biophys_monthly_xdeg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/fasir_biophys_monthly_xdeg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/970",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/970",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/fasir_biophys_monthly_xdeg/comp/0_fasir_biophys_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/fasir_biophys_monthly_xdeg/comp/0_fasir_biophys_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/fasir_biophys_monthly_xdeg/comp/1_fasir_biophys_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/fasir_biophys_monthly_xdeg/comp/1_fasir_biophys_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/970_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/970_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=970",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=970",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/970/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/970/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/970_1_fit.png",
+            "identifier": "C2784891689-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/970",
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
+            "temporal": "1982-01-01T00:00:00Z/1998-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II FASIR-adjusted NDVI Biophysical Parameter Fields, 1982-1998"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1321-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-08T02:41:00.000 to 2016-01-08T08:41:43.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1321-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1321-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1321-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-08T02:41:00.000 to 2016-01-08T08:41:43.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1321 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1321 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SMODE-DSCT2-V2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "E. Rodriguez, A. Wineteer, T. Gal, D. Perkovic-Martin, H. Torres, G. Gunther. 2023-05-30. S-MODE DopplerScatt Level 2 Ocean Winds Currents Version 2. Version 2. S-MODE DopplerScatt Level 2 Ocean Winds Currents Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, S-MODE Project Data Manager, Frederick Bingham. https://doi.org/10.5067/SMODE-DSCT2-V2. http://podaac.jpl.nasa.gov/S-MODE.",
-            "issued": "2021-10-20",
-            "temporal": "2021-10-20T00:00:00Z/2023-04-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-29",
-            "references": [
-                "https://doi.org/10.3390/rs10040576"
-            ],
-            "keyword": [
-                "atmosphere",
-                "spectral/engineering",
-                "radar",
-                "oceans",
-                "ocean circulation",
-                "earth science",
-                "atmospheric winds"
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
-            "identifier": "C2639507467-POCLOUD",
-            "description": "This dataset contains concurrent airborne DopplerScatt radar retrievals of surface vector winds and ocean currents from the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE). S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. Data were collected approximately 300 km offshore of San Fransisco during a pilot campaign in October 2021, and two intensive operating periods (IOPs) in Fall 2022 and Spring 2023.  DopplerScatt is a Ka-band (35.75 GHz) scatterometer with a swath width of 24 km that records Doppler measurements of the relative velocity between the platform and the surface. It is mounted on a B200 aircraft which flies daily surveys of the field domain during deployments, and data is used to give larger scale context, and also to compare with in-situ measurements of velocities and divergence. Level 2 data includes estimates of surface winds and currents. The V2 data have been cross-calibrated against ADCPs, surface drifters, and the SIO-DopVis instrument collected during the Pilot and IOP1 campaigns. Additional DopVis data collected during IOP1 and IOP2, in addition to IOP2 ADCP and surface drifter data will lead to a reprocessing of this dataset, and it should be regarded as provisional. Data are available in netCDF format.",
-            "series-name": "S-MODE DopplerScatt Level 2 Ocean Winds Currents Version 2",
-            "graphic-preview-description": "Thumbnail",
             "creator": "E. Rodriguez, A. Wineteer, T. Gal, D. Perkovic-Martin, H. Torres, G. Gunther",
-            "title": "S-MODE DopplerScatt Level 2 Ocean Winds and Currents Version 2",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L2_DOPPLERSCATT_WIND_CURRENT_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains concurrent airborne DopplerScatt radar retrievals of surface vector winds and ocean currents from the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE). S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. Data were collected approximately 300 km offshore of San Fransisco during a pilot campaign in October 2021, and two intensive operating periods (IOPs) in Fall 2022 and Spring 2023.  DopplerScatt is a Ka-band (35.75 GHz) scatterometer with a swath width of 24 km that records Doppler measurements of the relative velocity between the platform and the surface. It is mounted on a B200 aircraft which flies daily surveys of the field domain during deployments, and data is used to give larger scale context, and also to compare with in-situ measurements of velocities and divergence. Level 2 data includes estimates of surface winds and currents. The V2 data have been cross-calibrated against ADCPs, surface drifters, and the SIO-DopVis instrument collected during the Pilot and IOP1 campaigns. Additional DopVis data collected during IOP1 and IOP2, in addition to IOP2 ADCP and surface drifter data will lead to a reprocessing of this dataset, and it should be regarded as provisional. Data are available in netCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-DSCT2-V2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-DSCT2-V2",
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
-                    "description": "Field Campaign and Instrument Overview for S-MODE",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview for S-MODE",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/s-mode",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L2_DOPPLERSCATT_WIND_CURRENT_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L2_DOPPLERSCATT_WIND_CURRENT_V1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2639507467-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2639507467-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2639507467-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2639507467-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L2_DOPPLERSCATT_WIND_CURRENT_V1.jpg",
+            "identifier": "C2639507467-POCLOUD",
+            "issued": "2021-10-20",
+            "keyword": [
+                "atmosphere",
+                "spectral/engineering",
+                "radar",
+                "oceans",
+                "ocean circulation",
+                "earth science",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMODE-DSCT2-V2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.3390/rs10040576"
+            ],
+            "series-name": "S-MODE DopplerScatt Level 2 Ocean Winds Currents Version 2",
             "spatial": "-126.5 36.0 -122.0 38.4",
+            "temporal": "2021-10-20T00:00:00Z/2023-04-30T00:00:00Z",
             "theme": [
                 "S-MODE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "S-MODE DopplerScatt Level 2 Ocean Winds and Currents Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA302",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gille, John and Gray, Lesley J.. 2013-08-19. H3ZFC12MEXT. Version 007. HIRDLS/Aura Level 3 Extinction at 12.1 Microns 1deg Lat Zonal Fourier Coefficients V007. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/HIRDLS/DATA302. https://disc.gsfc.nasa.gov/datacollection/H3ZFC12MEXT_007.html. Digital Science Data.",
-            "issued": "2013-05-31",
-            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-31",
-            "keyword": [
-                "aerosols",
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
-            "identifier": "C1251100759-GES_DISC",
-            "description": "The \"HIRDLS/Aura Level 3 Extinction at 12.1 Microns Zonal Fourier Coefficients\" version 7 data product (H3ZFC12MEXT) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 215 to 20 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "H3ZFC12MEXT",
             "creator": "Gille, John and Gray, Lesley J.",
-            "title": "HIRDLS/Aura Level 3 Extinction at 12.1 Microns 1deg Lat Zonal Fourier Coefficients V007 (H3ZFC12MEXT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFC12MEXT_007.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The \"HIRDLS/Aura Level 3 Extinction at 12.1 Microns Zonal Fourier Coefficients\" version 7 data product (H3ZFC12MEXT) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 215 to 20 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA302",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA302",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -847736,210 +847714,246 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFC12MEXT_007.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFC12MEXT_007.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFC12MEXT.007/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFC12MEXT.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFC12MEXT.007/HIRDLS-Aura_L3ZFC12MEXT_v07-00-20-c02_2005d022-2008d077.he5.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFC12MEXT.007/HIRDLS-Aura_L3ZFC12MEXT_v07-00-20-c02_2005d022-2008d077.he5.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFC12MEXT_007",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFC12MEXT_007",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFC12MEXT_007.png",
+            "identifier": "C1251100759-GES_DISC",
+            "issued": "2013-05-31",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA302",
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
+            "series-name": "H3ZFC12MEXT",
             "spatial": "-180.0 -64.0 180.0 80.0",
+            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HIRDLS/Aura Level 3 Extinction at 12.1 Microns 1deg Lat Zonal Fourier Coefficients V007 (H3ZFC12MEXT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1222-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-29T18:48:50.000 to 2015-11-30T04:12:56.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1222-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1222-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1222-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-29T18:48:50.000 to 2015-11-30T04:12:56.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1222 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1222 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/83",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Johnson, L.F. 1994. SE-590 Lab-Measured Reflectances (OTTER). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/83",
-            "issued": "2023-11-19",
-            "temporal": "1990-08-17T00:00:00Z/1990-12-04T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
-            "keyword": [
-                "atmospheric radiation",
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
-            "identifier": "C2804776618-ORNL_CLOUD",
             "description": "Laboratory hemispherical reflectance spectra measurements taken to eliminate the effects of atmosphere, understory, exposed soils, mixed species and canopy architecture",
-            "graphic-preview-description": "Browse Image",
-            "title": "SE-590 Lab-Measured Reflectances (OTTER)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/otter_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F83",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F83",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/otter/spectra_se590_lab/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/otter/spectra_se590_lab/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/OTTER/guides/SE590_Laboratory_Reflectance_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/OTTER/guides/SE590_Laboratory_Reflectance_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/83",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/83",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_lab/comp/aug90.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_lab/comp/aug90.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_lab/comp/dec90.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_lab/comp/dec90.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_lab/comp/se590.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_lab/comp/se590.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_lab/comp/SE590_Laboratory_Reflectance_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_lab/comp/SE590_Laboratory_Reflectance_Data.pdf",
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
+            "identifier": "C2804776618-ORNL_CLOUD",
+            "issued": "2023-11-19",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/83",
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
+            "temporal": "1990-08-17T00:00:00Z/1990-12-04T23:59:59Z",
             "theme": [
                 "OTTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SE-590 Lab-Measured Reflectances (OTTER)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/h67r-htky",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Understanding the possible impact of potential confounding factors is necessary for any approach to radiation biodosimetry. Potential confounding factors have not been fully addressed for gene expression-based biodosimetry approaches such as we are developing. To begin addressing this need we have used an ex vivo irradiated peripheral blood cell model to investigate the potential effect of smoking on the global radiation gene expression response and looked for genes that respond to radiation differently in smokers and non-smokers and also in males and females. The results indicate that only a small number of genes may be significantly confounded by either factor supporting the idea of developing peripheral blood gene expression strategies for radiation biodosimetry. Blood from each of 24 different donors was exposed to four doses of ionizing radiation (0 0.1 0.5 or 2 Gy) and analyzed using single-color microarray hybridization. The donors represented equal numbers of male and female smokers (1 or more packs a day) and non-smokers. There are 95 data sets in the study as the sample from one of the female smokers exposed to 2 Gy was lost.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-155",
+                    "mediaType": "text/html",
+                    "title": "Radiation responses in peripheral white blood cells of smokers and non-smokers"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-155_h67r-htky",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "hybridization",
                 "age",
@@ -847964,207 +847978,205 @@
                 "image_aquisition",
                 "grow"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/h67r-htky",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-155_h67r-htky",
-            "description": "Understanding the possible impact of potential confounding factors is necessary for any approach to radiation biodosimetry. Potential confounding factors have not been fully addressed for gene expression-based biodosimetry approaches such as we are developing. To begin addressing this need we have used an ex vivo irradiated peripheral blood cell model to investigate the potential effect of smoking on the global radiation gene expression response and looked for genes that respond to radiation differently in smokers and non-smokers and also in males and females. The results indicate that only a small number of genes may be significantly confounded by either factor supporting the idea of developing peripheral blood gene expression strategies for radiation biodosimetry. Blood from each of 24 different donors was exposed to four doses of ionizing radiation (0 0.1 0.5 or 2 Gy) and analyzed using single-color microarray hybridization. The donors represented equal numbers of male and female smokers (1 or more packs a day) and non-smokers. There are 95 data sets in the study as the sample from one of the female smokers exposed to 2 Gy was lost.",
-            "title": "Radiation responses in peripheral white blood cells of smokers and non-smokers",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-155",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Radiation responses in peripheral white blood cells of smokers and non-smokers"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Radiation responses in peripheral white blood cells of smokers and non-smokers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/483",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ranson, K.J., R. Lang, and G. Sun. 1999. BOREAS RSS-15 SIR-C and TM Biomass and Landcover Maps of the NSA and SSA. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/483",
-            "issued": "2023-11-22",
-            "temporal": "1994-04-13T00:00:00Z/1995-09-02T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "land surface",
-                "land use/land cover",
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
-            "identifier": "C2929140955-ORNL_CLOUD",
             "description": "The RSS-15 team conducted an investigation using SIR-C , X-SAR and Landsat TM data for estimating total above-ground dry biomass for the SSA and NSA modeling grids and component biomass for the SSA. Relationships of backscatter to total biomass and total biomass to foliage, branch, and bole biomass were used to estimate biomass density across the landscape.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS RSS-15 SIR-C and TM Biomass and Landcover Maps of the NSA and SSA",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F483",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F483",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rs15bmlc/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rs15bmlc/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS15_SIRC_Biomass.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS15_SIRC_Biomass.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/483",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/483",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/nsa_data.lst",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/nsa_data.lst",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/RSS15_SIRC_Biomass.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/RSS15_SIRC_Biomass.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/RSS15_SIRC_Biomass.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/RSS15_SIRC_Biomass.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/RSS15_SIRC_Biomass.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/RSS15_SIRC_Biomass.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/ssa_data.lst",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs15bmlc/comp/ssa_data.lst",
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
+            "identifier": "C2929140955-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "land surface",
+                "land use/land cover",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/483",
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
             "spatial": "-105.61 53.63 -97.75 56.21",
+            "temporal": "1994-04-13T00:00:00Z/1995-09-02T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS RSS-15 SIR-C and TM Biomass and Landcover Maps of the NSA and SSA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V8.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through January 2011. It includes some comets with Centaur orbits. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v8.0_h6as-4svm",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid",
                 "comet",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V8.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v8.0_h6as-4svm",
-            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through January 2011. It includes some comets with Centaur orbits. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
-            "title": "TNO AND CENTAUR COLORS V8.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TNO AND CENTAUR COLORS V8.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985661-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "Sentinel-1B slant-range product",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1327985661-ASF",
             "issued": "2016-08-20",
-            "temporal": "2016-04-25T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
             "keyword": [
                 "sea ice",
                 "terrestrial ecosystems",
@@ -848191,614 +848203,614 @@
                 "land use/land cover",
                 "ocean winds"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985661-ASF.html",
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
-            "identifier": "C1327985661-ASF",
-            "description": "Sentinel-1B slant-range product",
-            "title": "SENTINEL-1B_SLC",
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
+            "temporal": "2016-04-25T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SENTINEL-1B_SLC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SPEC-V1.0",
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
+            "description": "Spectroscopy of Jupiter, Saturnian rings, atmospheres and satellites for determining chemical abundance, compositional albedo, aerosol profiling, ring reflected spectra and diffraction patterns.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-spec-v1.0_h6bf-xf35",
+            "issued": "2018-06-26",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SPEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-spec-v1.0_h6bf-xf35",
-            "description": "Spectroscopy of Jupiter, Saturnian rings, atmospheres and satellites for determining chemical abundance, compositional albedo, aerosol profiling, ring reflected spectra and diffraction patterns.",
-            "title": "CASSINI ORBITER SATURN UVIS EDITED SPECTRA 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER SATURN UVIS EDITED SPECTRA 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V9.0",
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
+            "description": "The data set lists orbital and physical properties for well-observed or suspected binary/multiple minor planets including the Pluto system, compiled from the published literature as inspired by Richardson and Walsh (2006) and similar reviews (Merline et al., 2003; Noll, 2006; Pravec et al., 2006; Pravec and Harris, 2007; Descamps and Marchis, 2008; Noll et al., 2008; Walsh, 2009).  In total 297 companions in 282 systems are included. Data are presented in three tables:  one for orbital and physical properties; one for companion designations, discovery information, and reference codes for data values; and one giving full references for each reference code.  This data set is complete for binary/multiple components reported through 31 March 2016.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v9.0_h6bv-4tig",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V9.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v9.0_h6bv-4tig",
-            "description": "The data set lists orbital and physical properties for well-observed or suspected binary/multiple minor planets including the Pluto system, compiled from the published literature as inspired by Richardson and Walsh (2006) and similar reviews (Merline et al., 2003; Noll, 2006; Pravec et al., 2006; Pravec and Harris, 2007; Descamps and Marchis, 2008; Noll et al., 2008; Walsh, 2009).  In total 297 companions in 282 systems are included. Data are presented in three tables:  one for orbital and physical properties; one for companion designations, discovery information, and reference codes for data values; and one giving full references for each reference code.  This data set is complete for binary/multiple components reported through 31 March 2016.",
-            "title": "BINARY MINOR PLANETS V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "BINARY MINOR PLANETS V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RADAR-3-ABDR-V1.0",
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
+            "description": "N/A",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-radar-3-abdr-v1.0_h6e2-ifwj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RADAR-3-ABDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-radar-3-abdr-v1.0_h6e2-ifwj",
-            "description": "N/A",
-            "title": "CASSINI ORBITER RADAR ALTIMETER BURST DATA RECORD",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER RADAR ALTIMETER BURST DATA RECORD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP21C3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Glynn Hulley, Simon Hook. 2023-06-26. VIIRS/NPP Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP21C3.002. https://doi.org/10.5067/VIIRS/VNP21C3.002. This data set was provided by the NASA/NOAA NPP Project..",
-            "issued": "2023-06-26",
-            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-26",
-            "keyword": [
-                "earth science",
-                "surface thermal properties",
-                "surface radiative properties",
-                "land surface"
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
-            "identifier": "C2545314573-LPCLOUD",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Land Surface Temperature and Emissivity (LST&E) monthly Climate Modeling Grid Version 2 product (VNP21C3) provides LST&E by a process of selecting the best available pixel over a monthly acquisition period at 0.05 degree (~5,600 meter) resolution. The VNP21C3 dataset is a monthly composite LST&E product that uses an algorithm based on a simple averaging method and is formatted as a CMG for use in climate simulation models. The algorithm calculates the average from all the cloud free VNP21A1D (http://doi.org/10.5067/VIIRS/VNP21A1D.002) and VNP21A1N (http://doi.org/10.5067/VIIRS/VNP21A1N.002) daily acquisitions from the monthly period. Unlike the VNP21A1 data sets where the daytime and nighttime acquisitions are separate products, the VNP21C3 contains both daytime and nighttime acquisitions as separate Science Dataset (SDS) layers within a single Hierarchical Data Format (HDF) file. Additional details regarding the method used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Glynn Hulley, Simon Hook",
-            "title": "VIIRS/NPP Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V002",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2917659759-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Land Surface Temperature and Emissivity (LST&E) monthly Climate Modeling Grid Version 2 product (VNP21C3) provides LST&E by a process of selecting the best available pixel over a monthly acquisition period at 0.05 degree (~5,600 meter) resolution. The VNP21C3 dataset is a monthly composite LST&E product that uses an algorithm based on a simple averaging method and is formatted as a CMG for use in climate simulation models. The algorithm calculates the average from all the cloud free VNP21A1D (http://doi.org/10.5067/VIIRS/VNP21A1D.002) and VNP21A1N (http://doi.org/10.5067/VIIRS/VNP21A1N.002) daily acquisitions from the monthly period. Unlike the VNP21A1 data sets where the daytime and nighttime acquisitions are separate products, the VNP21C3 contains both daytime and nighttime acquisitions as separate Science Dataset (SDS) layers within a single Hierarchical Data Format (HDF) file. Additional details regarding the method used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP21C3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP21C3.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314573-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314573-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QS/new/index.cgi",
-                    "description": "The LDOPE Land Product Quality Assessment website provides known issues, maneuvers, and product quality of the land products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LDOPE Land Product Quality Assessment website provides known issues, maneuvers, and product quality of the land products.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QS/new/index.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP21C3.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP21C3.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1662/VNP21_User_Guide_V2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1662/VNP21_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2917659759-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2917659759-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LST_Val.html",
-                    "description": "Validation at stage 1 has been achieved for the VIIRS Land Surface Temperature and Emissivity product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the VIIRS Land Surface Temperature and Emissivity product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LST_Val.html",
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
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2917659759-LPCLOUD?h=85&w=85",
+            "identifier": "C2545314573-LPCLOUD",
+            "issued": "2023-06-26",
+            "keyword": [
+                "earth science",
+                "surface thermal properties",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP21C3.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0023-V1.0",
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
+            "description": "This is a Solar Conjunction measurement covering the time 2006-03-30T00:27:04.500 to 2006-03-30T03:37:16.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0023-v1.0_h6kk-bk45",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0023-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0023-v1.0_h6kk-bk45",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-03-30T00:27:04.500 to 2006-03-30T03:37:16.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0023 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0023 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://data.nasa.gov/d/h6kq-qbn7",
-            "issued": "2022-06-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-15",
-            "keyword": [
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Parker Case",
                 "hasEmail": "mailto:parker.a.case@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Parker Case"
-            },
-            "identifier": "https://data.nasa.gov/api/views/h6kq-qbn7",
             "description": "pinatubo_james",
-            "title": "pinatubo_james",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.nasa.gov/download/h6kq-qbn7/application/zip",
                     "mediaType": "application/zip"
                 }
-            ]
+            ],
+            "identifier": "https://data.nasa.gov/api/views/h6kq-qbn7",
+            "issued": "2022-06-28",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://data.nasa.gov/d/h6kq-qbn7",
+            "modified": "2024-05-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Parker Case"
+            },
+            "title": "pinatubo_james"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/8DQKWY03KJWT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Global Glacier Debris Thickness Estimates and Sub-Debris Melt Factors V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA NSIDC DAAC. https://doi.org/10.5067/8DQKWY03KJWT.",
-            "issued": "2000-01-01",
-            "temporal": "2000-01-01T00:00:00Z/2018-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-31",
-            "keyword": [
-                "earth science",
-                "glaciers/ice sheets",
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
-            "identifier": "C2048907945-NSIDC_ECS",
             "description": "This data set includes spatially distributed estimates of the debris thickness and sub-debris melt enhancement factors for every debris-covered glacier in the Randolph Glacier Inventory\nVersion 6, excluding the ice sheets and Antarctic Periphery. The debris thickness estimates are derived using a novel approach that uses a combination of sub-debris melt inversion and surface temperature inversion methods. The sub-debris melt enhancement factors are estimated from the debris thickness using debris thickness-melt curves normalized by estimates of the clean-ice melt.",
-            "title": "Global Glacier Debris Thickness Estimates and Sub-Debris Melt Factors V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8DQKWY03KJWT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8DQKWY03KJWT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DTE.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DTE.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2028568967-NSIDC_ECS&tl=1602012627%214%21%21&m=24.884853055007127%2118.480051040649414%212%211%210%210%2C2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2028568967-NSIDC_ECS&tl=1602012627%214%21%21&m=24.884853055007127%2118.480051040649414%212%211%210%210%2C2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DTE/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DTE/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DTE.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DTE.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2028568967-NSIDC_ECS&tl=1602012627%214%21%21&m=24.884853055007127%2118.480051040649414%212%211%210%210%2C2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2028568967-NSIDC_ECS&tl=1602012627%214%21%21&m=24.884853055007127%2118.480051040649414%212%211%210%210%2C2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DTE/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DTE/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DTE.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DTE.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2028568967-NSIDC_ECS&tl=1602012627%214%21%21&m=24.884853055007127%2118.480051040649414%212%211%210%210%2C2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2028568967-NSIDC_ECS&tl=1602012627%214%21%21&m=24.884853055007127%2118.480051040649414%212%211%210%210%2C2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DTE/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DTE/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8DQKWY03KJWT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/8DQKWY03KJWT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8DQKWY03KJWT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/8DQKWY03KJWT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2048907945-NSIDC_ECS",
+            "issued": "2000-01-01",
+            "keyword": [
+                "earth science",
+                "glaciers/ice sheets",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/8DQKWY03KJWT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -56.0 180.0 84.0",
+            "temporal": "2000-01-01T00:00:00Z/2018-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Glacier Debris Thickness Estimates and Sub-Debris Melt Factors V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/102",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Betts, A.K. 1994. Site Averaged Neutron Soil Moisture: 1988 (Betts) . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/102",
-            "issued": "2023-11-21",
-            "temporal": "1988-04-11T00:00:00Z/1988-10-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-02",
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
-            "identifier": "C2810664362-ORNL_CLOUD",
             "description": "Site averaged product of the neutron probe soil moisture collected during the 1987-1989 FIFE experiment. Samples were averaged for each site, then averaged for each day. Includes only 1988 data.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Site Averaged Neutron Soil Moisture: 1988 (Betts)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F102",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F102",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/ffo_Betts_1988_nsm/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/ffo_Betts_1988_nsm/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/Follow_On/guides/Betts_neut_soil_mstr_88.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/Follow_On/guides/Betts_neut_soil_mstr_88.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/102",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/102",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_nsm/comp/Betts_neut_soil_mstr_88.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_nsm/comp/Betts_neut_soil_mstr_88.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_nsm/comp/Betts_neut_soil_mstr_88.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_nsm/comp/Betts_neut_soil_mstr_88.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_nsm/comp/ffoneu88.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_nsm/comp/ffoneu88.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_nsm/comp/ffo_sm.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_nsm/comp/ffo_sm.txt",
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
+            "identifier": "C2810664362-ORNL_CLOUD",
+            "issued": "2023-11-21",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/102",
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
             "spatial": "-96.61 38.98 -96.45 39.12",
+            "temporal": "1988-04-11T00:00:00Z/1988-10-21T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Site Averaged Neutron Soil Moisture: 1988 (Betts)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0319-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-26T16:29:20.000 to 2014-09-27T01:10:08.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0319-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0319-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0319-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-26T16:29:20.000 to 2014-09-27T01:10:08.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0319 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0319 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://earthobservatory.nasa.gov/Images/?eocn=topnav&eoci=images",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Ichoku",
+                "hasEmail": "mailto:charles.m.ichoku@nasa.gov"
+            },
+            "description": "The Earth Observatory is part of the EOS Project Science Office located at NASA Goddard Space Flight Center.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://earthobservatory.nasa.gov/Images/?eocn=topnav&eoci=images",
+                    "mediaType": "application/html"
+                }
+            ],
+            "identifier": "NASA-908",
             "issued": "2015-08-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "image of the day",
                 "photos of earth",
@@ -848818,114 +848830,80 @@
                 "astronomy",
                 "life"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Ichoku",
-                "hasEmail": "mailto:charles.m.ichoku@nasa.gov"
-            },
+            "landingPage": "http://earthobservatory.nasa.gov/Images/?eocn=topnav&eoci=images",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-908",
-            "description": "The Earth Observatory is part of the EOS Project Science Office located at NASA Goddard Space Flight Center.",
-            "title": "NASA Earth Observatory Images",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://earthobservatory.nasa.gov/Images/?eocn=topnav&eoci=images",
-                    "mediaType": "application/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NASA Earth Observatory Images"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67P-M26-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67p-m26-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "zeta cas",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67P-M26-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67p-m26-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP026 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP026 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA3020",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Millan, L., Livesey, N. and Read, W.. 2016-06-30. ML3DZMBRO. Version 004. MLS/Aura Level 3 Bromine Monoxide (BrO) Daily 10degrees Lat Zonal Mean V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA3020. https://disc.gsfc.nasa.gov/datacollection/ML3DZMBRO_004.html. Digital Science Data.",
-            "issued": "2016-06-30",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-06-30",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
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
-            "identifier": "C1281455546-GES_DISC",
-            "description": "ML3DZMBRO is the EOS Aura Microwave Limb Sounder (MLS) daily zonal mean product for bromine monoxide derived from radiances measured by the 640 GHz radiometer. The data version is 4.2. Data coverage is from August 2, 2004 to current. Spatial coverage is near-global (-85 degrees to  85 degrees latitude) spaced every 10 degrees in latitude. The recommended useful vertical range is between 10 and 4.64 hPa, and the vertical resolution is about 5 km. Users of the ML3DZMBRO data product should read the MLS Radiance Average Retrievals (RAR) BrO Product Guideline document, as well as section 3.2 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 4 network Common Data Form (netCDF4), which is built on the version 5 Hierarchical Data Format, or HDF5. The netCDF4 files follow the Climate and Forecast (CF) metadata conventions. Each file contains two zonal means objects or groups, one with data from the ascending part of the MLS orbit, the other with the descending data. Each zonal means object contains the average, error (precision), solar zenith angle, and local solar time for each latitude band and pressure level. Files also contain metadata attributes describing the data and product.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DZMBRO",
             "creator": "Millan, L., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 3 Bromine Monoxide (BrO) Daily 10degrees Lat Zonal Mean V004 (ML3DZMBRO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZMBRO_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DZMBRO is the EOS Aura Microwave Limb Sounder (MLS) daily zonal mean product for bromine monoxide derived from radiances measured by the 640 GHz radiometer. The data version is 4.2. Data coverage is from August 2, 2004 to current. Spatial coverage is near-global (-85 degrees to  85 degrees latitude) spaced every 10 degrees in latitude. The recommended useful vertical range is between 10 and 4.64 hPa, and the vertical resolution is about 5 km. Users of the ML3DZMBRO data product should read the MLS Radiance Average Retrievals (RAR) BrO Product Guideline document, as well as section 3.2 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 4 network Common Data Form (netCDF4), which is built on the version 5 Hierarchical Data Format, or HDF5. The netCDF4 files follow the Climate and Forecast (CF) metadata conventions. Each file contains two zonal means objects or groups, one with data from the ascending part of the MLS orbit, the other with the descending data. Each zonal means object contains the average, error (precision), solar zenith angle, and local solar time for each latitude band and pressure level. Files also contain metadata attributes describing the data and product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA3020",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA3020",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -848935,137 +848913,126 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZMBRO_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZMBRO_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZMBRO.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZMBRO.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZMBRO.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZMBRO.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZMBRO_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZMBRO_004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZMBRO.004/doc/Aura-MLS_L3-BrORAR_v4_guidelines.pdf",
-                    "description": "Product Guideline",
                     "@type": "dcat:Distribution",
+                    "description": "Product Guideline",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZMBRO.004/doc/Aura-MLS_L3-BrORAR_v4_guidelines.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/eos_l3_atbd.pdf",
-                    "description": "EOS MLS Level 3 Algorithm Theoretical Basis",
                     "@type": "dcat:Distribution",
+                    "description": "EOS MLS Level 3 Algorithm Theoretical Basis",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/eos_l3_atbd.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZMBRO_004.png",
+            "identifier": "C1281455546-GES_DISC",
+            "issued": "2016-06-30",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA3020",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML3DZMBRO",
             "spatial": "-180.0 -85.0 180.0 85.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Bromine Monoxide (BrO) Daily 10degrees Lat Zonal Mean V004 (ML3DZMBRO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MXL0MFDHWP07",
             "citation": "Vrije Universiteit Amsterdam (Richard de Jeu) and NASA GSFC (Manfred Owe). Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng). 2011-10-28. LPRM_AMSRE_D_SOILM3. Version 002. AMSR-E/Aqua surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V002. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MXL0MFDHWP07. https://disc.gsfc.nasa.gov/datacollection/LPRM_AMSRE_D_SOILM3_002.html.",
-            "issued": "2013-05-22",
-            "temporal": "2002-06-19T00:29:47Z/2011-10-03T21:49:11Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-06-11",
-            "references": [
-                "https://doi.org/10.1029/2007JF000769",
-                "https://doi.org/10.1007/s10712-008-9044-0",
-                "https://doi.org/10.1029/2008JD010257",
-                "https://doi.org/10.1109/LGRS.2011.2114872"
-            ],
-            "keyword": [
-                "soils",
-                "vegetation",
-                "surface thermal properties",
-                "land surface",
-                "earth science",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RICHARD DE JEU",
                 "hasEmail": "mailto:Richard.de.jeu@falw.vu.nl"
             },
-            "identifier": "C1235316221-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "description": "AMSR-E/Aqua surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V002 is a Level 3 (gridded) data set. Its land surface parameters, surface soil moisture, land surface (skin) temperature, and vegetation water content, are derived from passive microwave remote sensing data from the Advanced Microwave Scanning Radiometer-Earth Observing System (AMSR-E), using the Land Parameter Retrieval Model (LPRM). There are two files per day, one ascending (daytime) and one descending (nighttime), archived as two different products. This document is for the nighttime product. The data set covers the period from June 2002 to October 2011 (when the AMSR-E on the NASA EOS Aqua satellite stopped producing data due to a problem with the rotation of its antenna).\n                         \nThe LPRM is based on a forward radiative transfer model to retrieve surface soil moisture and vegetation optical depth. The land surface temperature is derived separately from the AMSR-E's Ka-band (36.5 GHz). A unique feature of this method is that it can be applied at any microwave frequency, making it very suitable to exploit all the available passive microwave data from various satellites.\n                         \nInput data are from the AMSR-E resampled brightness temperatures (AE_L2A) product, nighttime passes, as processed using LPRM (i.e., LPRM/AMSR-E/Aqua L2B product, LPRM_AMSRE_SOILM2_V002).",
-            "editor": "Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng)",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "LPRM_AMSRE_D_SOILM3",
             "creator": "Vrije Universiteit Amsterdam (Richard de Jeu) and NASA GSFC (Manfred Owe)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface\n(Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "AMSR-E/Aqua surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V002 (LPRM_AMSRE_D_SOILM3) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=&endtime=&dataKeyword=LPRM_AMSRE_D_SOILM3",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "AMSR-E/Aqua surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V002 is a Level 3 (gridded) data set. Its land surface parameters, surface soil moisture, land surface (skin) temperature, and vegetation water content, are derived from passive microwave remote sensing data from the Advanced Microwave Scanning Radiometer-Earth Observing System (AMSR-E), using the Land Parameter Retrieval Model (LPRM). There are two files per day, one ascending (daytime) and one descending (nighttime), archived as two different products. This document is for the nighttime product. The data set covers the period from June 2002 to October 2011 (when the AMSR-E on the NASA EOS Aqua satellite stopped producing data due to a problem with the rotation of its antenna).\n                         \nThe LPRM is based on a forward radiative transfer model to retrieve surface soil moisture and vegetation optical depth. The land surface temperature is derived separately from the AMSR-E's Ka-band (36.5 GHz). A unique feature of this method is that it can be applied at any microwave frequency, making it very suitable to exploit all the available passive microwave data from various satellites.\n                         \nInput data are from the AMSR-E resampled brightness temperatures (AE_L2A) product, nighttime passes, as processed using LPRM (i.e., LPRM/AMSR-E/Aqua L2B product, LPRM_AMSRE_SOILM2_V002).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMXL0MFDHWP07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMXL0MFDHWP07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -849075,409 +849042,453 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LPRM_AMSRE_D_SOILM3_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LPRM_AMSRE_D_SOILM3_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSRE_D_SOILM3.002/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSRE_D_SOILM3.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=&endtime=&dataKeyword=LPRM_AMSRE_D_SOILM3",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface\n(Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface\n(Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=&endtime=&dataKeyword=LPRM_AMSRE_D_SOILM3",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LPRM_AMSRE_D_SOILM3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LPRM_AMSRE_D_SOILM3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/LPRM_AMSRE_D_SOILM3.002/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/LPRM_AMSRE_D_SOILM3.002/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSRE_D_SOILM3.002/doc/README_LPRM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSRE_D_SOILM3.002/doc/README_LPRM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/tools?title=Hydrology+Data+Rods",
-                    "description": "GES DISC Data Rods Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "GES DISC Data Rods Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/tools?title=Hydrology+Data+Rods",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "editor": "Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng)",
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface\n(Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=&endtime=&dataKeyword=LPRM_AMSRE_D_SOILM3",
+            "identifier": "C1235316221-GES_DISC",
+            "issued": "2013-05-22",
+            "keyword": [
+                "soils",
+                "vegetation",
+                "surface thermal properties",
+                "land surface",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MXL0MFDHWP07",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-06-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2007JF000769",
+                "https://doi.org/10.1007/s10712-008-9044-0",
+                "https://doi.org/10.1029/2008JD010257",
+                "https://doi.org/10.1109/LGRS.2011.2114872"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "LPRM_AMSRE_D_SOILM3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-06-19T00:29:47Z/2011-10-03T21:49:11Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/Aqua surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V002 (LPRM_AMSRE_D_SOILM3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/401",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Harden, J.W., S.E. Trumbore, E. Sundquist, and G.C. Winston. 1998. BOREAS TGB-12 Radon-222 Flux Data: NSA. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/401",
-            "issued": "2023-11-22",
-            "temporal": "1993-11-15T00:00:00Z/1994-08-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "land surface",
-                "soils",
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
-            "identifier": "C2808089765-ORNL_CLOUD",
             "description": "Contains RADON-222 flux data data collected by TGB-12 in the northern study area.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-12 Radon-222 Flux Data: NSA",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F401",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F401",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb12rfd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb12rfd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB12_RadonFlux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB12_RadonFlux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/401",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/401",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12rfd/comp/tgb12rfd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12rfd/comp/tgb12rfd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12rfd/comp/TGB12_RadonFlux.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12rfd/comp/TGB12_RadonFlux.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12rfd/comp/TGB12_RadonFlux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12rfd/comp/TGB12_RadonFlux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12rfd/comp/TGB12_RadonFlux.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12rfd/comp/TGB12_RadonFlux.txt",
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
+            "identifier": "C2808089765-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "land surface",
+                "soils",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/401",
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
             "spatial": "-98.62 55.88 -97.71 55.93",
+            "temporal": "1993-11-15T00:00:00Z/1994-08-16T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-12 Radon-222 Flux Data: NSA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MULTI-5-67P-SHAPE-V1.0",
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
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-multi-5-67p-shape-v1.0_h749-qnzq",
             "description": "This data set contains a collection of shape models and their associated reference frame(s) for the Rosetta target 67P/Churyumov-Gerasimenko 1 (1969 R1).  These were produced by Rosetta mission teams, based on OSIRIS and NAVCAM image data obtained at the comet.",
-            "title": "SHAPE MODELS OF 67P/CHURYUMOV-GERASIMENKO V1.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-multi-5-67p-shape-v1.0_h749-qnzq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MULTI-5-67P-SHAPE-V1.0",
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
-            "landingPage": "https://doi.org/10.7927/H44F1NNF",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Cyclone Proportional Economic Loss Risk Deciles. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H44F1NNF. https://doi.org/10.7927/H44F1NNF.",
-            "issued": "2005-12-31",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
             "references": [
-                "https://doi.org/10.7927/H4CZ353K",
-                "https://doi.org/10.7927/H40P0WXQ",
-                "https://doi.org/10.7927/H4862DC5"
+                "https://pds.nasa.gov"
+            ],
+            "theme": [
+                "Earth Science"
             ],
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "natural hazards",
-                "socioeconomics"
+            "title": "SHAPE MODELS OF 67P/CHURYUMOV-GERASIMENKO V1.0"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Cyclone Proportional Economic Loss Risk Deciles. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H44F1NNF. https://doi.org/10.7927/H44F1NNF.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:metadata@ciesin.columbia.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "SEDAC"
-            },
-            "identifier": "C179001767-SEDAC",
-            "description": "The Global Cyclone Proportional Economic Loss Risk Deciles is a 2.5 minute grid of cyclone hazard economic loss as proportions of Gross Domestic Product (GDP) per analytical Unit. Estimates of GDP at risk are based on regional economic loss rates derived from historical records of the Emergency Events Database (EM-DAT). Loss rates are weighted by the hazard's frequency and distribution. The methodology of Sachs et al. (2003) is followed to determine baseline estimates of GDP per grid cell. To better reflect the confidence surrounding the data and procedures, the range of proportionalities is classified into deciles, 10 class of an approximately equal number of grid cells of increasing risk. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank",
-            "title": "Global Cyclone Proportional Economic Loss Risk Deciles",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Cyclone Proportional Economic Loss Risk Deciles is a 2.5 minute grid of cyclone hazard economic loss as proportions of Gross Domestic Product (GDP) per analytical Unit. Estimates of GDP at risk are based on regional economic loss rates derived from historical records of the Emergency Events Database (EM-DAT). Loss rates are weighted by the hazard's frequency and distribution. The methodology of Sachs et al. (2003) is followed to determine baseline estimates of GDP per grid cell. To better reflect the confidence surrounding the data and procedures, the range of proportionalities is classified into deciles, 10 class of an approximately equal number of grid cells of increasing risk. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH44F1NNF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH44F1NNF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-cyclone-proportional-economic-loss-risk-deciles/cyclone-proportional-economic-loss-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-cyclone-proportional-economic-loss-risk-deciles/cyclone-proportional-economic-loss-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-proportional-economic-loss-risk-deciles/maps",
+            "identifier": "C179001767-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "natural hazards",
+                "socioeconomics"
+            ],
+            "landingPage": "https://doi.org/10.7927/H44F1NNF",
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
+                "https://doi.org/10.7927/H4CZ353K",
+                "https://doi.org/10.7927/H40P0WXQ",
+                "https://doi.org/10.7927/H4862DC5"
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
+            "title": "Global Cyclone Proportional Economic Loss Risk Deciles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1976",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, R.O. Green, T.H. Painter, R. Iacovazzi, R. Pollock, and S.L. Ustin. 2022. MASTER: Airborne Science, Southwest US, June, 2011. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1976",
-            "issued": "2023-06-19",
-            "temporal": "2011-06-08T21:59:17Z/2011-06-20T23:05:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "land surface",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "surface radiative properties",
-                "earth science",
-                "visible wavelengths",
-                "surface thermal properties"
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
-            "identifier": "C2731698585-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during 6 flights aboard a NASA ER-2 aircraft over southwestern U.S. and northern Mexico, from 2011-06-08 to 2011-06-20. The purposes of these flights include collecting data for wildfire mapping, airborne science initiatives, and calibration data for AVIRIS. This deployment was coordinated by NASA's Dryden Flight Research Center (DRFC), renamed Armstrong Flight Research Center in 2014, located in Edwards, California. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes the flight path, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single band images and an RGB composite image from flight track 7 acquired on 09 June 2011 over Black Bear Pass east of Telluride, Colorado, U.S. Source: MASTERL1B_1165200_07_20110609_1906_1911_V01.jpg",
-            "title": "MASTER: Airborne Science, Southwest US, June, 2011",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_June_2011_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1976",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1976",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_DFRC_June_2011/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_DFRC_June_2011/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_June_2011.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_June_2011.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1976",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1976",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_DFRC_June_2011/comp/MASTER_DFRC_June_2011.pdf",
-                    "description": "MASTER: Airborne Science, Southwest US, June, 2011: MASTER_DFRC_June_2011.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, Southwest US, June, 2011: MASTER_DFRC_June_2011.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_DFRC_June_2011/comp/MASTER_DFRC_June_2011.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_June_2011_Fig1.jpg",
-                    "description": "Single band images and an RGB composite image from flight track 7 acquired on 09 June 2011 over Black Bear Pass east of Telluride, Colorado, U.S. Source: MASTERL1B_1165200_07_20110609_1906_1911_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single band images and an RGB composite image from flight track 7 acquired on 09 June 2011 over Black Bear Pass east of Telluride, Colorado, U.S. Source: MASTERL1B_1165200_07_20110609_1906_1911_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_June_2011_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single band images and an RGB composite image from flight track 7 acquired on 09 June 2011 over Black Bear Pass east of Telluride, Colorado, U.S. Source: MASTERL1B_1165200_07_20110609_1906_1911_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_June_2011_Fig1.jpg",
+            "identifier": "C2731698585-ORNL_CLOUD",
+            "issued": "2023-06-19",
+            "keyword": [
+                "land surface",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "surface radiative properties",
+                "earth science",
+                "visible wavelengths",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1976",
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
             "spatial": "-122.55 31.62 -105.47 40.98",
+            "temporal": "2011-06-08T21:59:17Z/2011-06-20T23:05:21Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, Southwest US, June, 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://aeronet.gsfc.nasa.gov/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brent Holben",
+                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
+            },
+            "description": "Sun photometer measurements of the direct (collimated) solar radiation provide information to calculate the columnar aerosol optical depth (AOD). AOD can be used to compute columnar water vapor (Precipitable Water) and estimate the aerosol size using the Angstrom parameter relationship. Two data versions (Versions 1 and 2) and three quality levels (Levels 1.0, 1.5, 2.0) exist for each product. While Levels 1.0 and 1.5 are provided in near real-time, the 12-month or longer delay (due to final calibration and manual inspection) ensures that the highest quality data can be found in Version 2, Level 2.0 data products. Level 2: pre- and post-field calibration applied, automatically cloud cleared and manually inspected.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aeronet.gsfc.nasa.gov/cgi-bin/type_piece_of_map_opera_v2_newtar.gz",
+                    "mediaType": "application/x-tar"
+                }
+            ],
+            "identifier": "NASA-0000001",
             "issued": "2018-06-25",
-            "temporal": "1993-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "satellite",
                 "aerosols",
@@ -849487,490 +849498,445 @@
                 "precipitable water",
                 "radiation"
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
-            "identifier": "NASA-0000001",
-            "description": "Sun photometer measurements of the direct (collimated) solar radiation provide information to calculate the columnar aerosol optical depth (AOD). AOD can be used to compute columnar water vapor (Precipitable Water) and estimate the aerosol size using the Angstrom parameter relationship. Two data versions (Versions 1 and 2) and three quality levels (Levels 1.0, 1.5, 2.0) exist for each product. While Levels 1.0 and 1.5 are provided in near real-time, the 12-month or longer delay (due to final calibration and manual inspection) ensures that the highest quality data can be found in Version 2, Level 2.0 data products. Level 2: pre- and post-field calibration applied, automatically cloud cleared and manually inspected.",
-            "title": "Aeronet AOD",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aeronet.gsfc.nasa.gov/cgi-bin/type_piece_of_map_opera_v2_newtar.gz",
-                    "mediaType": "application/x-tar"
-                }
-            ],
             "spatial": "Global",
-            "accrualPeriodicity": "irregular",
+            "temporal": "1993-01-01/2014-01-01",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Aeronet AOD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast-bennu.radar.shape-model&version=1.0",
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
-                "(101955) bennu"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "We present the three-dimensional shape of near-Earth asteroid (101955) Bennu\n(provisional designation 1999 RQ36) based on radar images and optical lightcurves\n(Nolan et al., 2013). Bennu was observed both in 1999 at its discovery apparition,\nand in 2005 using the 12.6-cm radar at the Arecibo Observatory and the 3.5-cm radar\nat the Goldstone tracking station. Data obtained in both apparitions were used to\nconstruct a shape model of this object.      \nObservations were also obtained at many other wavelengths to characterize this\nobject, some of which were used to further constrain the shape modeling (Clark et\nal., 2011; Hergenrother et al., 2013; Krugly et al., 1999).",
+            "identifier": "urn:nasa:pds:ast-bennu.radar.shape-model",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none",
+                "(101955) bennu"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast-bennu.radar.shape-model&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ast-bennu.radar.shape-model",
-            "description": "We present the three-dimensional shape of near-Earth asteroid (101955) Bennu\n(provisional designation 1999 RQ36) based on radar images and optical lightcurves\n(Nolan et al., 2013). Bennu was observed both in 1999 at its discovery apparition,\nand in 2005 using the 12.6-cm radar at the Arecibo Observatory and the 3.5-cm radar\nat the Goldstone tracking station. Data obtained in both apparitions were used to\nconstruct a shape model of this object.      \nObservations were also obtained at many other wavelengths to characterize this\nobject, some of which were used to further constrain the shape modeling (Clark et\nal., 2011; Hergenrother et al., 2013; Krugly et al., 1999).",
-            "title": "Asteroid (101955) Bennu Radar Shape Model V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Asteroid (101955) Bennu Radar Shape Model V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-W-V1.0",
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
+            "description": "This data set consists of HISCALE W ion counts from the Ulysses Jupiter encounter 1991-Dec-31 to 1992-Feb-16. This includes 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-w-v1.0_h76d-pvam",
+            "issued": "2018-06-26",
+            "keyword": [
+                "ulysses",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-W-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-w-v1.0_h76d-pvam",
-            "description": "This data set consists of HISCALE W ion counts from the Ulysses Jupiter encounter 1991-Dec-31 to 1992-Feb-16. This includes 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
-            "title": "ULYSSES JUPITER HISCALE W ION COUNTS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULYSSES JUPITER HISCALE W ION COUNTS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0236-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-24T06:49:35.000 to 2014-08-24T08:15:37.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0236-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0236-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0236-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-24T06:49:35.000 to 2014-08-24T08:15:37.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0236 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0236 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/LZB54MLNK98U",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VIIRS/JPSS1 Sea Ice Cover 6-Min L2 Swath 375m V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/LZB54MLNK98U.",
-            "issued": "2018-01-05",
-            "temporal": "2018-01-05T00:00:00Z/2024-11-25T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
-            "keyword": [
-                "sea ice",
-                "earth science",
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
-            "identifier": "C2317029310-NSIDC_ECS",
             "description": "This data set reports the location of sea ice cover derived from radiance data acquired by the Visible Infrared Imager Radiometer Suite (VIIRS) onboard the Joint Polar Satellite System's first satellite (JPSS-1). Following the approach used by MODIS, sea ice is detected using the Normalized Difference Snow Index.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "VIIRS/JPSS1 Sea Ice Cover 6-Min L2 Swath 375m V002",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-239,-87,129,97&l=,Coastlines_15m,VIIRS_NOAA20_Sea_Ice,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLZB54MLNK98U",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLZB54MLNK98U",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VJ129.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VJ129.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VJ129+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VJ129+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/VJ129/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/VJ129/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-239%2C-87%2C129%2C97&l=%2CCoastlines_15m%2CVIIRS_NOAA20_Sea_Ice%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-239%2C-87%2C129%2C97&l=%2CCoastlines_15m%2CVIIRS_NOAA20_Sea_Ice%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/LZB54MLNK98U",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/LZB54MLNK98U",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/LZB54MLNK98U",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/LZB54MLNK98U",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-239,-87,129,97&l=,Coastlines_15m,VIIRS_NOAA20_Sea_Ice,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C2317029310-NSIDC_ECS",
+            "issued": "2018-01-05",
+            "keyword": [
+                "sea ice",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/LZB54MLNK98U",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-05T00:00:00Z/2024-11-25T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Sea Ice Cover 6-Min L2 Swath 375m V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1973",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, R.O. Green, T.H. Painter, F.A. Kruse, D. Riano, and R. Iacovazzi. 2022. MASTER: Airborne Science, Southwest US, November, 2011. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1973",
-            "issued": "2023-06-19",
-            "temporal": "2011-11-02T17:27:45Z/2011-11-16T20:53:34Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
-                "visible wavelengths",
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
-            "identifier": "C2731696704-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during seven flights aboard a NASA ER-2 aircraft over southwestern U.S. from 2011-11-02 to 2011-11-16. This deployment was coordinated by NASA's Dryden Flight Research Center (DRFC), renamed Armstrong Flight Research Center in 2014, located in Edwards, California. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. The L1B file formats are HDF-4 and KMZ. In addition, the dataset includes the flight path, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single band images and an RGB composite image from flight track 06 acquired on 03 November 2011 east of Canyonlands National Park, south of Moab, Utah, U.S. Source: MASTERL1B_1260700_06_20111103_1859_1902_V01.jpg",
-            "title": "MASTER: Airborne Science, Southwest US, November, 2011",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_November_2011_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1973",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1973",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_DFRC_November_2011/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_DFRC_November_2011/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_November_2011.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_November_2011.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1973",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1973",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_DFRC_November_2011/comp/MASTER_DFRC_November_2011.pdf",
-                    "description": "MASTER: Airborne Science, Southwest US, November, 2011: MASTER_DFRC_November_2011.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, Southwest US, November, 2011: MASTER_DFRC_November_2011.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_DFRC_November_2011/comp/MASTER_DFRC_November_2011.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_November_2011_Fig1.jpg",
-                    "description": "Single band images and an RGB composite image from flight track 06 acquired on 03 November 2011 east of Canyonlands National Park, south of Moab, Utah, U.S. Source: MASTERL1B_1260700_06_20111103_1859_1902_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single band images and an RGB composite image from flight track 06 acquired on 03 November 2011 east of Canyonlands National Park, south of Moab, Utah, U.S. Source: MASTERL1B_1260700_06_20111103_1859_1902_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_November_2011_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single band images and an RGB composite image from flight track 06 acquired on 03 November 2011 east of Canyonlands National Park, south of Moab, Utah, U.S. Source: MASTERL1B_1260700_06_20111103_1859_1902_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_November_2011_Fig1.jpg",
+            "identifier": "C2731696704-ORNL_CLOUD",
+            "issued": "2023-06-19",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1973",
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
             "spatial": "-120.56 31.95 -108.28 39.37",
+            "temporal": "2011-11-02T17:27:45Z/2011-11-16T20:53:34Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, Southwest US, November, 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206714-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rock glacier inventory, Hautes Alpes Calcaires, Switzerland, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/1997-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-12-31",
-            "keyword": [
-                "snow/ice",
-                "frozen ground",
-                "cryosphere",
-                "earth science",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Marcia Phillips",
                 "hasEmail": "mailto:phillips@slf.ch"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206714-NSIDCV0",
             "description": "The Hautes Alpes Calcaires is a limestone range in the northern part of the Rhone Valley (Switzerland). It is characterized by a transitional climate between the wet Prealpes (precipitations = 1500 mm per year at 1000 m asl) and the central part of Valais (750 mm per year at 1000 m asl) and a contrasted morphology, with high limestone cliffs alternating with schists. For each rock glacier a file exists with different characteristics such as orientation, width, length, elevation of the spring and the front, type of form, type of material, activity, lithology, etc.   Measurements of spring temperatures and BTS (Bottom temperature under snow cover) exist for some rock glaciers, especially for the Cabane des Diablerets Rock Glacier, on which several temperature measurements (under the snow cover (BTS) and in the soil (mini-loggers)) and snow profiles have been carried out. A modelled map of the permafrost distribution has also been prepared for this sector (see map). The inventory is not complete. Data provided on the CAPS Version 1.0 CD-ROM, June 1998, are for Morcles and Chavalard Range, Diablerets Range, Wildhorn Range. Data collected during 1992 and 1997.",
-            "title": "Rock glacier inventory, Hautes Alpes Calcaires, Switzerland, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD289_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD289_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD289/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD289/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD289/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD289/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206714-NSIDCV0",
+            "issued": "1992-01-01",
+            "keyword": [
+                "snow/ice",
+                "frozen ground",
+                "cryosphere",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206714-NSIDCV0.html",
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
             "spatial": "7.033 46.133 7.6 46.417",
+            "temporal": "1992-01-01T00:00:00Z/1997-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Rock glacier inventory, Hautes Alpes Calcaires, Switzerland, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "GSSTFYC_3",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA311",
             "citation": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, J. Ardizzone, and S. Gao. Andrey Savtchenko. 2012-08-14. GSSTFYC. Version 3. Goddard Satellite-Based Surface Turbulent Fluxes Climatology, 0.25 x 0.25 deg, Yearly Grid V3. Greenbelt, MD, USA. GSSTFYC_3. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/GSSTF/DATA311. https://disc.gsfc.nasa.gov/datacollection/GSSTFYC_3.html. Digital Science Data.",
-            "issued": "2012-08-14",
-            "temporal": "1988-01-01T00:00:00Z/2008-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-08-14",
-            "keyword": [
-                "ocean heat budget",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "ocean winds",
-                "ocean temperature",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "oceans",
-                "ocean pressure",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SILBERSTEIN",
                 "hasEmail": "mailto:david.s.silberstein@nasa.gov"
             },
+            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, J. Ardizzone, and S. Gao",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1237113477-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "These data are the Goddard Satellite-based Surface Turbulent Fluxes Version-3 Dataset recently produced through a MEaSUREs funded project led by Dr. Chung-Lin Shie (UMBC/GEST, NASA/GSFC), converted to HDF-EOS5 format. The stewardship of this HDF-EOS5 dataset is part of the MEaSUREs project. \n\nThis is the fine resolution version of the previously released GSSTFYC.2c. \n\nThis is the Yearly Climatology product; data are projected to equidistant Grid that covers the globe at 0.25x00.25 degree cell size, resulting in data arrays of 1440x720 size. \n\nStarting from previous Version 2c, these data have only one set of Combined data, \"Set1\". The Yearly Climatology HDF-EOS5 file also contains one extra grid of NCEP Climatology, \"NCEP\". \n\nStarting with this Version 3, the \"WB\" variable, \"lowest 500-m precipitable water\" has been discontinued.  \n      \nThe short name for this product is GSSTFYC.",
-            "editor": "Andrey Savtchenko",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GSSTFYC",
-            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, J. Ardizzone, and S. Gao",
-            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Precipitable Water Yearly Climatology 1 x 1 degree (1988-2008) [g/cm2]",
-            "title": "Goddard Satellite-Based Surface Turbulent Fluxes Climatology, 0.25 x 0.25 deg, Yearly Grid V3 (GSSTFYC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFYC_3.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA311",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA311",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFYC_3.png",
-                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Precipitable Water Yearly Climatology 1 x 1 degree (1988-2008) [g/cm2]\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Precipitable Water Yearly Climatology 1 x 1 degree (1988-2008) [g/cm2]\n      ",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFYC_3.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTFYC_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTFYC_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFYC.3/",
-                    "description": "Access the data via HTTP.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.\n      ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFYC.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTFYC_3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.\n      ",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTFYC_3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTFYC.3",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTFYC.3",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFYC.3/doc/Readme.GSSTF3.pdf",
-                    "description": "README Document\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "README Document\n      ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFYC.3/doc/Readme.GSSTF3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects",
-                    "description": "MEaSUREs Project Home Page\n",
                     "@type": "dcat:Distribution",
+                    "description": "MEaSUREs Project Home Page\n",
+                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
@@ -849980,160 +849946,196 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "editor": "Andrey Savtchenko",
+            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Precipitable Water Yearly Climatology 1 x 1 degree (1988-2008) [g/cm2]",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFYC_3.png",
+            "identifier": "C1237113477-GES_DISC",
+            "issue-identification": "GSSTFYC_3",
+            "issued": "2012-08-14",
+            "keyword": [
+                "ocean heat budget",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "ocean winds",
+                "ocean temperature",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "oceans",
+                "ocean pressure",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA311",
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
+            "series-name": "GSSTFYC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1988-01-01T00:00:00Z/2008-12-31T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Goddard Satellite-Based Surface Turbulent Fluxes Climatology, 0.25 x 0.25 deg, Yearly Grid V3 (GSSTFYC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/687",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wilson, M.F., and A. Henderson-Sellers. 2003. LBA Regional Vegetation and Soils, 1-Degree (Wilson and Henderson-Sellers). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/687",
-            "issued": "2023-10-03",
-            "temporal": "1900-01-01T00:00:00Z/1999-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "soils",
-                "biosphere",
-                "earth science",
-                "land surface",
-                "land use/land cover",
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
-            "identifier": "C2777328977-ORNL_CLOUD",
             "description": "This data set is a subset of a global vegetation and soils data set by Wilson and Henderson-Sellers (1985a). The subset was created for the study area of the Large Scale Biosphere-Atmosphere Experiment in Amazonia (LBA) in South America (i.e., 10 N to 25 S, 30 to 85 W). The data are in ASCII GRID format.The original global data set (Wilson and Henderson-Sellers 1985a) is an archive of soil type and land cover data derived for use in general circulation models (GCMs). The data were collated from maps depicting natural vegetation, forestry, agriculture, land use, and soil, and they were archived at a resolution of 1 latitude by 1 longitude. The data set indicates soil type, soil data reliability, primary vegetation, secondary vegetation, and land cover data reliability. Approximately 50 land cover classifications are used, including categories for agricultural and urban uses. The inclusion of secondary vegetation type is particularly useful in areas with cover types that may have a fragmented distribution, such as in areas of urban development. The soil type data are classified according to climatically important properties for GCMs, and they indicate color (light, medium, or dark), texture, and drainage quality of the soil. The land cover data are compatible with the soils data, forming a coherent and consistent data set. The reliability of the land cover data is ranked on a scale of 1 to 5 (high to low). The reliability of the soil data is ranked as high, good, moderate, fair, or poor.Recommendations for the use of these data, as well as more detailed information can be found in Wilson and Henderson-Sellers (1985b).Further data set information can be found at ftp://daac.ornl.gov/data/lba/land_use_land_cover_change/wilhend/comp/wilhend_readme.pdf.LBA was a cooperative international research initiative led by Brazil. NASA was a lead sponsor for several experiments. LBA was designed to create the new knowledge needed to understand the climatological, ecological, biogeochemical, and hydrological functioning of Amazonia; the impact of land use change on these functions; and the interactions between Amazonia and the Earth system. More information about LBA can be found at http://www.daac.ornl.gov/LBA/misc_amazon.html.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA Regional Vegetation and Soils, 1-Degree (Wilson and Henderson-Sellers)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/687_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F687",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F687",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/wilhend/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/wilhend/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_wilhend.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_wilhend.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/687",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/687",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/wilhend/comp//wilhend_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/wilhend/comp//wilhend_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/687_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/687_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=687",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=687",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/687_1_fit.png",
+            "identifier": "C2777328977-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "soils",
+                "biosphere",
+                "earth science",
+                "land surface",
+                "land use/land cover",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/687",
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
             "spatial": "-85.0 -25.0 -30.0 10.0",
+            "temporal": "1900-01-01T00:00:00Z/1999-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA Regional Vegetation and Soils, 1-Degree (Wilson and Henderson-Sellers)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M02-V3.0",
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
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m02-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M02-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m02-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 3 PRL-MTP002 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 3 PRL-MTP002 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSIWAC-2-EAR2-EARTHSWINGBY2-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the EARTH SWING-BY 2 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osiwac-2-ear2-earthswingby2-v1.4_h7jh-sbqk",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "jupiter",
@@ -850144,63 +850146,39 @@
                 "16 cyg b",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSIWAC-2-EAR2-EARTHSWINGBY2-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osiwac-2-ear2-earthswingby2-v1.4_h7jh-sbqk",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the EARTH SWING-BY 2 mission phase",
-            "title": "ROSETTA-ORBITER EARTH SWING-BY 2 OSIWAC\n                                      2 EDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH SWING-BY 2 OSIWAC\n                                      2 EDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114199-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOMS Science Team. 1996-07-25. TOMSEPL3maer. Version 008. TOMS Earth Probe UV Aerosol Index Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3maer_008.html. Digital Science Data.",
-            "issued": "2004-04-30",
-            "temporal": "1996-08-01T00:00:00Z/2005-03-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-04-30",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere"
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
-            "identifier": "C1237114199-GES_DISC",
-            "description": "This Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 monthly averaged global gridded data product contains UV aerosol index values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TOMSEPL3maer",
             "creator": "TOMS Science Team",
-            "title": "TOMS Earth Probe UV Aerosol Index Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3maer) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPL3maer_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 monthly averaged global gridded data product contains UV aerosol index values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -850209,161 +850187,184 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3maer_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3maer_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPL3maer.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPL3maer.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPL3maer",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPL3maer",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPL3maer_008.png",
+            "identifier": "C1237114199-GES_DISC",
+            "issued": "2004-04-30",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114199-GES_DISC.html",
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
+            "series-name": "TOMSEPL3maer",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-08-01T00:00:00Z/2005-03-31T23:59:59.999Z",
             "theme": [
                 "TOMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS Earth Probe UV Aerosol Index Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3maer) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M16-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m16-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "vega",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M16-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m16-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSIWAC 3 RDR MTP016 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSIWAC 3 RDR MTP016 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD04_L2.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-10-20. MODIS/Terra Aerosol 5-Min L2 Swath 10km - NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MOD04_L2.NRT.061. https://modis-atmos.gsfc.nasa.gov/products/aerosol.",
-            "issued": "2017-10-11",
-            "temporal": "2017-10-11T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "earth science",
-                "national geospatial data asset",
-                "aerosols",
-                "ngda"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MODAPS USER SUPPORT TEAM",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCEMODIS"
-            },
-            "identifier": "C1426436561-LANCEMODIS",
             "description": "The new Collection 6.1 (C61) MOD04_L2 product is an improved version based on algorithm changes in Dark Target (DT) Aerosol retrieval over urban areas and uncertainty estimates for Deep Blue (DB) Aerosol retrievals.\n\nThe MODIS level-2 atmospheric aerosol product provides retrieved ambient aerosol optical properties, quality assurance, and other parameters, globally over ocean and land. In Collection 5, and earlier collections, there was only one aerosol product (MOD04_L2) at 10km (at nadir) spatial resolution. Starting from C6, the Dark Target (DT) Aerosol algorithm team provided a new 3 km spatial resolution product (MOD04_3k) intended for the air quality community.\n\nFor more information visit the MODIS Atmosphere website at:\nhttps://modis-atmos.gsfc.nasa.gov/products/aerosol\n\nAnd, for C6.1 changes and updates, visit:\nhttps://modis-atmosphere.gsfc.nasa.gov/documentation/collection-61",
-            "release-place": "MODAPS at NASA/GSFC",
-            "title": "MODIS/Terra Aerosol 5-Min L2 Swath 10km - NRT",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD04_L2.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD04_L2.NRT.061",
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
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page(download server).",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page(download server).",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD04_L2/",
-                    "description": "Direct access to the download site and directory hosting the MOD04_L2 C6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MOD04_L2 C6.1 NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD04_L2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C1426436561-LANCEMODIS",
+            "issued": "2017-10-11",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science",
+                "national geospatial data asset",
+                "aerosols",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD04_L2.NRT.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCEMODIS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-10-11T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "DODS",
                 "EOSDIS",
@@ -850372,92 +850373,66 @@
                 "OPENDAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Aerosol 5-Min L2 Swath 10km - NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-EPD-4-SUMM-EARTH2-15MIN-V1.0",
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
-                "galileo",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains fifteen minute averaged rate data for all 64 EPD channels.  The browse set covers the Earth 2 encounnter data from 1992 Day 311 through day 353.  All available motor positions except zero are included in the averages.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-epd-4-summ-earth2-15min-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-EPD-4-SUMM-EARTH2-15MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-epd-4-summ-earth2-15min-v1.0",
-            "description": "This data set contains fifteen minute averaged rate data for all 64 EPD channels.  The browse set covers the Earth 2 encounnter data from 1992 Day 311 through day 353.  All available motor positions except zero are included in the averages.",
-            "title": "GO EARTH EPD RESAMPLED SUMMARY EARTH2 15.0 MIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO EARTH EPD RESAMPLED SUMMARY EARTH2 15.0 MIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/PRTMI/TRMM/CSH/3B-MONTH/07",
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2021-07-29. GPM_3HCSH_TRMM. GPM PR and TMI on TRMM Combined Convective-Stratiform Latent Heating Profiles L3 1 month 0.25x0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/PRTMI/TRMM/CSH/3B-MONTH/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3HCSH_TRMM_07.html. Digital Science Data.",
-            "issued": "2021-07-21",
-            "temporal": "1997-12-01T00:00:00Z/2015-04-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-21",
-            "references": [
-                "https://doi.org/10.1175/AMSMONOGRAPHS-D-15-0013.1"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "Tropical Rainfall Measuring Mission (TRMM)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264132528-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is the new (GPM-formated) TRMM product. It replaces the old TRMM legacy TRMM_3H31\n\nVersion 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nEstimating vertical profiles of latent heating released by precipitating cloud systems is one of the key objectives of TRMM, together with accurately measuring the horizontal distribution of tropical rainfall.\n\nThe method uses TRMM PR information [precipitation-top height (PTH), precipitation rates at the surface and melting level, and rain type] to select heating profiles from lookup tables. Heating-profile lookup tables for the three rain types\u2014convective, shallow stratiform, and anvil rain (deep stratiform with a melting level)\u2014were derived from numerical simulations of tropical cloud systems from the Tropical Ocean and Global Atmosphere Coupled Ocean\u2013Atmosphere Response Experiment (TOGA COARE) utilizing a cloud-resolving model (CRM). The CSH algorithm is severely limited by the inherent sensitivity of the TRMM PR. For latent heating, the quantity required is actually cloud top, but the PR can detect only precipitation-sized particles.\n\nBecause observed information on precipitation depth is used in addition to precipitation type and intensity, differences between shallow and deep convection are more distinct in the CSH algorithm in comparison with the CSH algorithm.\n\nMonthly Spectral Latent Heating produces 0.25x0.25 degree grid of latent heating profiles from the TRMM PR rain. The grids are in the Planetary Grid 2 structure matching the Dual-frequency PR on the core GPM observatory that covers 67S to 67N degrees of latitudes.  Areas beyond the \u00b140 degrees of latitudes are padded with empty grid cells.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3HCSH_TRMM",
-            "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "GPM PR and TMI on TRMM Combined Convective-Stratiform Latent Heating Profiles L3 1 month 0.25x0.25 degree V07 (GPM_3HCSH_TRMM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3HCSH_TRMM.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FPRTMI%2FTRMM%2FCSH%2F3B-MONTH%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FPRTMI%2FTRMM%2FCSH%2F3B-MONTH%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -850467,295 +850442,329 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3HCSH_TRMM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3HCSH_TRMM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/GPM_3HCSH_TRMM.07",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/GPM_3HCSH_TRMM.07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/GPM_3HCSH_TRMM.07/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/GPM_3HCSH_TRMM.07/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3HCSH_TRMM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3HCSH_TRMM",
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
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/stout/helpdesk/filespec.GPM.V7.pdf",
-                    "description": "FILE SPECIFICATION DOCUMENT",
                     "@type": "dcat:Distribution",
+                    "description": "FILE SPECIFICATION DOCUMENT",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/stout/helpdesk/filespec.GPM.V7.pdf",
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
-                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/Release_Notes_CSH_V7.pdf",
-                    "description": "Details of the caveats to consider in this product.",
                     "@type": "dcat:Distribution",
+                    "description": "Details of the caveats to consider in this product.",
+                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/Release_Notes_CSH_V7.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3HCSH_TRMM.png",
+            "identifier": "C2264132528-GES_DISC",
+            "issued": "2021-07-21",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/PRTMI/TRMM/CSH/3B-MONTH/07",
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
+            "series-name": "GPM_3HCSH_TRMM",
             "spatial": "-180.0 -67.0 180.0 67.0",
+            "temporal": "1997-12-01T00:00:00Z/2015-04-30T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM PR and TMI on TRMM Combined Convective-Stratiform Latent Heating Profiles L3 1 month 0.25x0.25 degree V07 (GPM_3HCSH_TRMM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0204-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-13T13:51:05.000 to 2014-08-13T19:10:41.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0204-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0204-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0204-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-13T13:51:05.000 to 2014-08-13T19:10:41.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0204 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0204 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1857",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nault, B.A., P. Campuzano-Jost, D.A. Day, D.S. Jo, J.C. Schroder, H.M. Allen, R. Bahreini, H. Bian, D.R. Blake, M. Chin, S.L. Clegg, P.R. Colarco, J.D. Crounse, M.J. Cubison, P.F. Decarlo, J.E. Dibb, G.S. Diskin, A. Hodzic, W. Hu, J.M. Katich, J.K. Kodros, A. Kupc, F.D. Lopez-Hilfiker, E.A. Marais, A.M. Middlebrook, J.A. Neuman, J.B. Nowak, B.B. Palm, F. Paulot, J.R. Pierce, G.P. Schill, E. Scheuer, J.A. Thornton, K. Tsigaridis, P.O. Wennberg, C.J. Williamson, and J.L. Jimenez. 2022. Airborne Observations and Modeling Comparison of Global Inorganic Aerosol Acidity. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1857",
-            "issued": "2022-03-17",
-            "temporal": "2006-01-01T00:00:00Z/2017-08-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "air quality",
-                "aerosols",
-                "earth science",
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
-            "identifier": "C2698474800-ORNL_CLOUD",
             "description": "This dataset provides observations collected during eleven airborne campaigns from 2006&ndash;2017 and associated input and output from nine widely used chemical transport models (CTMs). The airborne campaigns include ARCTAS-A, ARCTAS-B, ATom-1 and ATom-2, CalNex, DC3, INTEX-B, KORUS-AQ, MILAGRO, SEAC4RS, and WINTER, and they sampled mainly tropospheric air over the conterminous U.S. and the state of Alaska, Mexico, Canada, Greenland, and South Korea and remote areas over the Arctic, Pacific, Southern, and Atlantic Oceans. The CTMs are the AM4.1, CCSM4, GEOS-5, GEOS-Chem TOMAS, GEOS-Chem v10, GEOS-Chem v12, GISS-MATRIX, GISS-ModelE, and TM4-ECPL-F, and the output includes sulfate, nitrate, temperature, specific humidity, mixing ratio of ammonium, the volume mixing ratio of nitric acid, surface pressure, gas-phase ammonia, gas-phase nitric acid, pressure, total ammonium, etc. The observations were collected in-situ from a variety of instruments, including the Aerosol Microphysical Properties (AMP), HR Aerodyne Aerosol Mass Spectrometer (AMS), CIT Chemical Ionization Mass Spectrometer (CIMS), diode laser hygrometer (DLH), a mist chamber/ion chromatography system (MC/IC), Particle Analysis by Laser Mass Spectrometer (PALMS), Single Particle Soot Photometer (SP2), and UCI Whole Air Sampler (WAS). In-situ data also include latitude, longitude, and pressure. These observations were used to investigate how aerosol pH and ammonium balance change from polluted to remote regions, such as over oceans, and were compared to predictions from the CTMs.",
-            "graphic-preview-description": "Flight tracks for airborne campaigns in this dataset.",
-            "title": "Airborne Observations and Modeling Comparison of Global Inorganic Aerosol Acidity",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Modeled_Observed_Data_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1857",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1857",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Modeled_Observed_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Modeled_Observed_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Modeled_Observed_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Modeled_Observed_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1857",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1857",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Modeled_Observed_Data/comp/ATom_Modeled_Observed_Data.pdf",
-                    "description": "Airborne Observations and Modeling Comparison of Global Inorganic Aerosol Acidity: ATom_Modeled_Observed_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Airborne Observations and Modeling Comparison of Global Inorganic Aerosol Acidity: ATom_Modeled_Observed_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Modeled_Observed_Data/comp/ATom_Modeled_Observed_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Modeled_Observed_Data/comp/file_groupings.pdf",
-                    "description": "Airborne Observations and Modeling Comparison of Global Inorganic Aerosol Acidity: file_groupings.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Airborne Observations and Modeling Comparison of Global Inorganic Aerosol Acidity: file_groupings.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Modeled_Observed_Data/comp/file_groupings.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Modeled_Observed_Data_Fig1.png",
-                    "description": "Flight tracks for airborne campaigns in this dataset.",
                     "@type": "dcat:Distribution",
+                    "description": "Flight tracks for airborne campaigns in this dataset.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Modeled_Observed_Data_Fig1.png",
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
+            "graphic-preview-description": "Flight tracks for airborne campaigns in this dataset.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Modeled_Observed_Data_Fig1.png",
+            "identifier": "C2698474800-ORNL_CLOUD",
+            "issued": "2022-03-17",
+            "keyword": [
+                "air quality",
+                "aerosols",
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1857",
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
+            "temporal": "2006-01-01T00:00:00Z/2017-08-01T23:59:59Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airborne Observations and Modeling Comparison of Global Inorganic Aerosol Acidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL2TCAL_L2.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2015), Terra/MISR Level 2, TOA/Cloud Albedo, version 2, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/Terra/MISR/MIL2TCAL_L2.002",
-            "issued": "2003-03-24",
-            "temporal": "2000-02-24T16:33:37Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-15",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "clouds",
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
-            "identifier": "C43677709-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 2 TOA/Cloud Albedo parameters V002 contains local, restrictive, and expansive albedo, with associated data.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 2 TOA/Cloud Albedo parameters V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL2TCAL_L2.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL2TCAL_L2.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/PRODOCS/misr/Quality_Summaries/L2_Cloud_Products.html",
-                    "description": "The product quality assessment may be downloaded directly from this link",
                     "@type": "dcat:Distribution",
+                    "description": "The product quality assessment may be downloaded directly from this link",
+                    "downloadURL": "http://eosweb.larc.nasa.gov/PRODOCS/misr/Quality_Summaries/L2_Cloud_Products.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C43677709-LARC",
+            "issued": "2003-03-24",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL2TCAL_L2.002",
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
+            "temporal": "2000-02-24T16:33:37Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 2 TOA/Cloud Albedo parameters V002"
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
+                    "downloadURL": "http://cfdval2004.larc.nasa.gov/Presentations/case3figsonly.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-848__6",
+            "issued": "2018-06-25",
             "keyword": [
                 "control",
                 "validation",
@@ -850766,166 +850775,159 @@
                 "synthetic",
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
-            "identifier": "NASA-848__6",
-            "description": "CFD Validation of Synthetic Jets and Turbulent Separation Control. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: CFD Validation of Synthetic Jets and Turbulent Separation Control",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://cfdval2004.larc.nasa.gov/Presentations/case3figsonly.pdf",
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
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GAAB1GIBBQKU",
             "citation": "Kevin W. Bowman. 2021-05-27. TRPSDL2H2OAIRSFS. Version 1. TROPESS AIRS-Aqua L2 Water for Forward Stream, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GAAB1GIBBQKU. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2H2OAIRSFS_1.html. Digital Science Data.",
-            "issued": "2021-05-22",
-            "temporal": "2021-02-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-22",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
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
-            "identifier": "C2041964582-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS AIRS-Aqua L2 Water for Forward Stream, Standard Product contains the vertical distribution of the retrieved atmospheric state of water vapor (H2O), formal uncertainties, and diagnostic information measured by the AIRS instrument on the EOS Aqua satellite. The forward stream standard product is global for the time period from 2021-02-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 13.5 km (AIRS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2H2OAIRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS AIRS-Aqua H2O (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS AIRS-Aqua L2 Water for Forward Stream, Standard Product V1 (TRPSDL2H2OAIRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2H2OAIRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGAAB1GIBBQKU",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGAAB1GIBBQKU",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2H2OAIRSFS_Sample.png",
-                    "description": "TROPESS AIRS-Aqua H2O (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS AIRS-Aqua H2O (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2H2OAIRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2H2OAIRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2H2OAIRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2H2OAIRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2H2OAIRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2H2OAIRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2H2OAIRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2H2OAIRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2H2OAIRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2H2OAIRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2H2OAIRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS AIRS-Aqua H2O (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2H2OAIRSFS_Sample.png",
+            "identifier": "C2041964582-GES_DISC",
+            "issued": "2021-05-22",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GAAB1GIBBQKU",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-22",
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
+            "series-name": "TRPSDL2H2OAIRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS AIRS-Aqua L2 Water for Forward Stream, Standard Product V1 (TRPSDL2H2OAIRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M04-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m04-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "beta car",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
@@ -850936,171 +850938,145 @@
                 "fomalhaut",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M04-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m04-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP004 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP004 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0035-5-SDSSTAX-V1.1",
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
+            "description": "The Sloan Digital Sky Survey Moving Object Catalog (SDSS-MOC) is a large data set that provides five-filter magnitudes and astrometric information for all moving objects identified in the SDSS images (Izevic et al., 2010). The photometric observations were classified by Carvano et al. (2010) into nine taxonomic classes: Vp, Op, Qp, Sp, Ap, Lp, Dp, Xp and Cp, which are related to the classes and complexes of Bus Taxonomy (Bus & Binzel, 2002b). This data set is contains the taxonomic classification of each SDSS detections and its compilation for each observed asteroid.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0035-5-sdsstax-v1.1_h829-v8ag",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0035-5-SDSSTAX-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0035-5-sdsstax-v1.1_h829-v8ag",
-            "description": "The Sloan Digital Sky Survey Moving Object Catalog (SDSS-MOC) is a large data set that provides five-filter magnitudes and astrometric information for all moving objects identified in the SDSS images (Izevic et al., 2010). The photometric observations were classified by Carvano et al. (2010) into nine taxonomic classes: Vp, Op, Qp, Sp, Ap, Lp, Dp, Xp and Cp, which are related to the classes and complexes of Bus Taxonomy (Bus & Binzel, 2002b). This data set is contains the taxonomic classification of each SDSS detections and its compilation for each observed asteroid.",
-            "title": "SDSS-BASED ASTEROID TAXONOMY V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SDSS-BASED ASTEROID TAXONOMY V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPC/3A-MONTH/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFMETOPCMHS. Version 07. GPM MHS on METOP-C (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/MHS/METOPC/3A-MONTH/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFMETOPCMHS_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2019-07-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "precipitation",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHRISTIAN KUMMEROW",
                 "hasEmail": "mailto:kummerow@atmos.colostate.edu"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264134803-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set.  \n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_3GPROFMETOPCMHS",
-            "creator": "GPM Science Team",
-            "title": "GPM MHS on METOP-C (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPCMHS) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from GPM MHS on METOP-B GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFMETOPBMHS)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFMETOPCMHS_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPC%2F3A-MONTH%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPC%2F3A-MONTH%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFMETOPCMHS_07.png",
-                    "description": "Surface Precipitation from GPM MHS on METOP-B GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFMETOPBMHS)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from GPM MHS on METOP-B GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFMETOPBMHS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFMETOPCMHS_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFMETOPCMHS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFMETOPCMHS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFMETOPCMHS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFMETOPCMHS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFMETOPCMHS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFMETOPCMHS.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFMETOPCMHS_07.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFMETOPCMHS_07.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFMETOPCMHS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFMETOPCMHS_07",
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
@@ -851110,460 +851086,496 @@
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
+            "graphic-preview-description": "Surface Precipitation from GPM MHS on METOP-B GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFMETOPBMHS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFMETOPCMHS_07.png",
+            "identifier": "C2264134803-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPC/3A-MONTH/07",
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
+            "series-name": "GPM_3GPROFMETOPCMHS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-07-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM MHS on METOP-C (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPCMHS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2G_LSTE.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Glynn Hulley. 2023-04-25. ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L2G_LSTE.002. https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2023-04-25",
-            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-25",
-            "keyword": [
-                "surface thermal properties",
-                "earth science",
-                "land surface"
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
-            "identifier": "C2076113037-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\nThe ECOSTRESS Gridded Land Surface Temperature and Emissivity Instantaneous Level 2 Global 70 m (ECO_L2G_LSTE) Version 2 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO_L2G_LSTE data product was derived using a physics-based Temperature and Emissivity Separation (TES) algorithm. This data product is a gridded version of the ECO_L2_LSTE (https://doi.org/10.5067/ECOSTRESS/ECO_L2_LSTE.002) Version 2 data product that was resampled using nearest neighbor, projected to a globally snapped 0.0006\u00b0 grid, and repackaged as the ECO_L2G_LSTE data product. The ECO_L2G_LSTE product is provided as gridded data and has a spatial resolution of 70 meters (m). The ECO_L2G_LSTE Version 2 data product contains 8 layers distributed in an HDF5 format file including LST, LST error, wideband emissivity, height, view zenith angle, quality flags, and cloud and water masks.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Glynn Hulley",
-            "title": "ECOSTRESS Gridded Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2G_LSTE.002/ECOv002_L2G_LSTE_21265_028_20220406T174138_0700_01/ECOv002_L2G_LSTE_21265_028_20220406T174138_0700_01.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\nThe ECOSTRESS Gridded Land Surface Temperature and Emissivity Instantaneous Level 2 Global 70 m (ECO_L2G_LSTE) Version 2 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO_L2G_LSTE data product was derived using a physics-based Temperature and Emissivity Separation (TES) algorithm. This data product is a gridded version of the ECO_L2_LSTE (https://doi.org/10.5067/ECOSTRESS/ECO_L2_LSTE.002) Version 2 data product that was resampled using nearest neighbor, projected to a globally snapped 0.0006\u00b0 grid, and repackaged as the ECO_L2G_LSTE data product. The ECO_L2G_LSTE product is provided as gridded data and has a spatial resolution of 70 meters (m). The ECO_L2G_LSTE Version 2 data product contains 8 layers distributed in an HDF5 format file including LST, LST error, wideband emissivity, height, view zenith angle, quality flags, and cloud and water masks.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2G_LSTE.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2G_LSTE.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076090826-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076090826-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2G_LSTE.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2G_LSTE.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1324/ECO2_LSTE_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1324/ECO2_LSTE_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2G_LSTE.002/ECOv002_L2G_LSTE_21265_028_20220406T174138_0700_01/ECOv002_L2G_LSTE_21265_028_20220406T174138_0700_01.png",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2G_LSTE.002/ECOv002_L2G_LSTE_21265_028_20220406T174138_0700_01/ECOv002_L2G_LSTE_21265_028_20220406T174138_0700_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac-ops.cr.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf",
-                    "description": "The quality information in the ECO_L2_LSTE User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The quality information in the ECO_L2_LSTE User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac-ops.cr.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2G_LSTE.002/ECOv002_L2G_LSTE_21265_028_20220406T174138_0700_01/ECOv002_L2G_LSTE_21265_028_20220406T174138_0700_01.png",
+            "identifier": "C2076113037-LPCLOUD",
+            "issued": "2023-04-25",
+            "keyword": [
+                "surface thermal properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2G_LSTE.002",
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
+            "title": "ECOSTRESS Gridded Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2254303790-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
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
-            "identifier": "C2254303790-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Sentinel-3A OLCI Level-2 Earth-observation Reduced-Resolution (ERR) Inherent Optical Properties (IOP), Near Real-time (NRT) Data, version R2022.0",
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
+            "identifier": "C2254303790-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere",
+                "ocean optics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2254303790-OB_DAAC.html",
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
+            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-3A OLCI Level-2 Earth-observation Reduced-Resolution (ERR) Inherent Optical Properties (IOP), Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566678-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "1972-11-16",
-            "temporal": "1972-11-16T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-27",
-            "keyword": [
-                "national geospatial data asset",
-                "spectral/engineering",
-                "sensor characteristics",
-                "land use/land cover",
-                "ngda",
-                "land surface",
-                "earth science",
-                "surface thermal properties",
-                "surface radiative properties"
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
-            "identifier": "C1220566678-USGS_LTA",
             "description": "On the background of these requirements for sensor calibration, intercalibration and product validation, the subgroup on Calibration and Validation of the Committee on Earth Observing System (CEOS) formulated the following recommendation during the plenary session held in China at the end of 2004, with the goal of setting-up and operating an internet based system to provide sensor data, protocols and guidelines for these purposes:\n\nBackground:\n\nReference Datasets are required to support the understanding of climate change and quality assure operational services by Earth Observing satellites. The data from different sensors and the resulting synergistic data products require a high level of accuracy that can only be obtained through continuous traceable calibration and validation activities.\nRequirement:\n\nInitiate an activity to document a reference methodology to predict Top of Atmosphere (TOA) radiance for which currently flying and planned wide swath sensors can be intercompared, i.e. define a standard for traceability. Also create and maintain a fully accessible web page containing, on an instrument basis, links to all instrument characteristics needed for intercomparisons as specified above, ideally in a common format. In addition, create and maintain a database (e.g. SADE) of instrument data for specific vicarious calibration sites, including site characteristics, in a common format. Each agency is responsible for providing data for their instruments in this common format. Recommendation : The required activities described above should be supported for an implementation period of two years and a maintenance period over two subsequent years. The CEOS should encourage a member agency to accept the lead role in supporting this activity. CEOS should request all member agencies to support this activity by providing appropriate information and data in a timely manner.\n\nPseudo-Invariant Calibration Sites (PICS):\nLibya 4 is one of six CEOS reference Pseudo-Invariant Calibration Sites (PICS) that are CEOS Reference Test Sites. Besides the nominally good site characteristics (temporal stability, uniformity, homogeneity, etc.), these six PICS were selected by also taking into account their heritage and the large number of datasets from multiple instruments that already existed in the EO archives and the long history of characterization performed over these sites. The PICS have high reflectance and are usually made up of sand dunes with climatologically low aerosol loading and practically no vegetation. Consequently, these PICS can be used to evaluate the long-term stability of instrument and facilitate inter-comparison of multiple instruments.",
-            "title": "CEOS Cal Val Test Site - Libya 4 - Pseudo-Invariant Calibration Site (PICS)",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/opensearch/granules/descriptor_document.xml?collectionConceptId=C1220566678-USGS_LTA",
-                    "description": "Collection-specific granule Open Search Descriptor Document",
                     "@type": "dcat:Distribution",
+                    "description": "Collection-specific granule Open Search Descriptor Document",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/opensearch/granules/descriptor_document.xml?collectionConceptId=C1220566678-USGS_LTA",
+                    "mediaType": "application/opensearchdescription+xml",
                     "title": "Retrieve the OpenSearch Get Capabilities document"
                 }
             ],
+            "identifier": "C1220566678-USGS_LTA",
+            "issued": "1972-11-16",
+            "keyword": [
+                "national geospatial data asset",
+                "spectral/engineering",
+                "sensor characteristics",
+                "land use/land cover",
+                "ngda",
+                "land surface",
+                "earth science",
+                "surface thermal properties",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566678-USGS_LTA.html",
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
             "spatial": "23.3 28.45 23.5 28.65",
+            "temporal": "1972-11-16T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CEOS Cal Val Test Site - Libya 4 - Pseudo-Invariant Calibration Site (PICS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-ROTATION-V1.0",
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
-                "comet"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set presents Table 1 of Samarasinha, et al. (2004): 'Information on spin states of specific comets', as published in 'Comets II' (Festou, Keller and Weaver, eds.).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-rotation-v1.0_h888-xzh9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "comet"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-ROTATION-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-rotation-v1.0_h888-xzh9",
-            "description": "This data set presents Table 1 of Samarasinha, et al. (2004): 'Information on spin states of specific comets', as published in 'Comets II' (Festou, Keller and Weaver, eds.).",
-            "title": "ROTATION OF COMET NUCLEI: TABLE 1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROTATION OF COMET NUCLEI: TABLE 1"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/580",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "Tieszen, L.L. 2013. NPP Tundra: Point Barrow, Alaska, 1970-1972, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/580",
-            "issued": "2013-08-28",
-            "temporal": "1921-01-01T00:00:00Z/1990-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "vegetation",
-                "ecological dynamics"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "Tieszen, L.L. 2013. NPP Tundra: Point Barrow, Alaska, 1970-1972, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/580",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2751947951-ORNL_CLOUD",
             "description": "This data set contains three data files. One file (.csv format) provides above- and below-ground biomass and leaf area index (LAI) data for a wet arctic tundra meadow (Biome research site 2, Dupontia meadow, vegetation type V) studied from 1970 to 1971 at Point Barrow, Alaska, USA, (71.30 N -156.67 W Elevation 5 m). The second file, also in .csv format, provides net primary productivity (NPP) estimates for different plant growth forms for eight vegetation types recognized in the coastal tundra at Barrow. The third file (.txt format) provides climate data from the weather station at Barrow, Alaska (71.30 N -156.78 W Elevation 31 m). Measurements of above- and below-ground living and dead biomass were made at 10-day intervals during the growing season (mid June to end of August) by harvest methods in 6 x 6 m study plots of undisturbed vegetation. LAI was estimated at 10-day intervals with inclined point quadrats and other methods. NPP estimates are based on harvest at the period of peak above-ground vascular biomass and seasonal CO2 gas exchange estimates in 1972. The studies were conducted as part of the International Biological Program (IBP) U.S. Tundra Biome program. Average total NPP for the eight vegetation communities recognized for the coastal tundra at Barrow was 230 g/m2/year (110 g/m2/year ANPP plus 120 g/m2/year BNPP). Values varied by vegetation community type. Revision Notes: This data set has been revised to correct several values of average below-ground plant standing crop. A second NPP data file has been added to provide NPP estimates for the different vegetation types at the coastal tundra study site from measurements made in 1972. Please see the Data Set Revisions section of this document for detailed information.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Tundra: Point Barrow, Alaska, 1970-1972, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F580",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F580",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/tundra/NPP_BRW/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/tundra/NPP_BRW/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BRW.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BRW.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/580",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/580",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tundra/NPP_BRW/comp/NPP_BRW.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tundra/NPP_BRW/comp/NPP_BRW.pdf",
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
+            "identifier": "C2751947951-ORNL_CLOUD",
+            "issued": "2013-08-28",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/580",
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
             "spatial": "71.3 -156.67",
+            "temporal": "1921-01-01T00:00:00Z/1990-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Tundra: Point Barrow, Alaska, 1970-1972, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-SOLAR-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-solar-ops-v1.0_h8dq-wjn8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-SOLAR-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-solar-ops-v1.0_h8dq-wjn8",
-            "description": "not applicable",
-            "title": "MER 1 MARS NAVIGATION CAMERA SOLAR RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS NAVIGATION CAMERA SOLAR RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ssd.jpl.nasa.gov/sbdb_query.cgi",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Watskins",
+                "hasEmail": "mailto:michael.m.watkins@jpl.nasa.gov"
+            },
+            "description": "Use this search engine to generate custom tables of orbital and/or physical parameters for all asteroids and comets (or a specified sub-set) in our small-body database. If this is your first time here, you may find it helpful to read our tutorial. Otherwise, simply follow the steps in each section: 'Search Constraints', 'Output Fields', and finally 'Format Options'. If you want details for a single object, use the Small Body Browser instead.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ssd.jpl.nasa.gov/sbdb_query.cgi",
+                    "mediaType": "application/html"
+                }
+            ],
+            "identifier": "NASA-903",
             "issued": "1998-03-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "comet",
                 "asteroid",
@@ -851577,42 +851589,44 @@
                 "solar system",
                 "discovery"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Watskins",
-                "hasEmail": "mailto:michael.m.watkins@jpl.nasa.gov"
-            },
+            "landingPage": "http://ssd.jpl.nasa.gov/sbdb_query.cgi",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-903",
-            "description": "Use this search engine to generate custom tables of orbital and/or physical parameters for all asteroids and comets (or a specified sub-set) in our small-body database. If this is your first time here, you may find it helpful to read our tutorial. Otherwise, simply follow the steps in each section: 'Search Constraints', 'Output Fields', and finally 'Format Options'. If you want details for a single object, use the Small Body Browser instead.",
-            "title": "JPL Small Body Database Search Engine",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ssd.jpl.nasa.gov/sbdb_query.cgi",
-                    "mediaType": "application/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "JPL Small Body Database Search Engine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/h8gv-j777",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The JAXA MHU-2 mission had two objectives: 1) To increase understanding of effects of spaceflight on the gut environment (microbiota and metabolites) and immune system using multi-omics based analysis; 2) To evaluate whether fructo-oligosaccharides added to the diet as prebiotics improve the gut environment and immune function during spaceflight. Twelve 16-18 week old male C57BL/6J mice were singly housed in the JAXA Habitat Cage Units (HCUs) on the ISS for 30 days. Six flight mice were housed in microgravity while six were exposed to simulated 1g by centrifugation. These two flight groups were further divided in half so that three mice in each group received standard JAXA chow while the other three were fed chow supplemented with fructooligosaccharides (FOS). Mice were returned live and euthanized and dissected <1 day after splashdown. Ground controls (n=6) were asynchronous and housed in HCUs. Vivarium controls (n=6) were asynchronous and housed in standard habitats. Three ground control and three vivarium animals received standard chow while the other three each ground control and vivarium animals received FOS-supplemented chow. Ground and vivarium samples were dissected by a separate dissection team than flight samples. Femoral skin was dissected 30 minutes after euthanasia and snap frozen in liquid nitrogen. Total RNA was extracted and sequenced at a target depth of 60 M clusters per sample (ribodepleted paired end 150). Study Factor Levels: 1)Spaceflight ug Std. Chow: 3; 2)Spaceflight ug FOS: 3; 3) Spaceflight Artificial 1g Std. Chow: 3; 4)Spaceflight Artificial 1g FOS: 3; 5)Ground 1g Std. Chow: 3; 6)Ground 1g FOS: 3; 7)Vivarium 1g Std. Chow: 3; 8)Vivarium 1g FOS: 3",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-239",
+                    "mediaType": "text/html",
+                    "title": "Transcriptomic analysis of femoral skin from mice flown on the MHU-2 mission"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-239_h8gv-j777",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "altered gravity",
                 "nucleic acid extraction",
@@ -851627,324 +851641,319 @@
                 "diet",
                 "spike-in protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/h8gv-j777",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-239_h8gv-j777",
-            "description": "The JAXA MHU-2 mission had two objectives: 1) To increase understanding of effects of spaceflight on the gut environment (microbiota and metabolites) and immune system using multi-omics based analysis; 2) To evaluate whether fructo-oligosaccharides added to the diet as prebiotics improve the gut environment and immune function during spaceflight. Twelve 16-18 week old male C57BL/6J mice were singly housed in the JAXA Habitat Cage Units (HCUs) on the ISS for 30 days. Six flight mice were housed in microgravity while six were exposed to simulated 1g by centrifugation. These two flight groups were further divided in half so that three mice in each group received standard JAXA chow while the other three were fed chow supplemented with fructooligosaccharides (FOS). Mice were returned live and euthanized and dissected <1 day after splashdown. Ground controls (n=6) were asynchronous and housed in HCUs. Vivarium controls (n=6) were asynchronous and housed in standard habitats. Three ground control and three vivarium animals received standard chow while the other three each ground control and vivarium animals received FOS-supplemented chow. Ground and vivarium samples were dissected by a separate dissection team than flight samples. Femoral skin was dissected 30 minutes after euthanasia and snap frozen in liquid nitrogen. Total RNA was extracted and sequenced at a target depth of 60 M clusters per sample (ribodepleted paired end 150). Study Factor Levels: 1)Spaceflight ug Std. Chow: 3; 2)Spaceflight ug FOS: 3; 3) Spaceflight Artificial 1g Std. Chow: 3; 4)Spaceflight Artificial 1g FOS: 3; 5)Ground 1g Std. Chow: 3; 6)Ground 1g FOS: 3; 7)Vivarium 1g Std. Chow: 3; 8)Vivarium 1g FOS: 3",
-            "title": "Transcriptomic analysis of femoral skin from mice flown on the MHU-2 mission",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-239",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcriptomic analysis of femoral skin from mice flown on the MHU-2 mission"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcriptomic analysis of femoral skin from mice flown on the MHU-2 mission"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/O72K7GAES72W",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx17 SnowSAR Raw FMCW Waveforms V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/O72K7GAES72W.",
-            "issued": "2017-02-16",
-            "temporal": "2017-02-16T00:00:00Z/2017-02-22T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-02-22",
-            "keyword": [
-                "radar",
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
-            "identifier": "C1722859882-NSIDC_ECS",
             "description": "This data set, part of the SnowEx 2017 campaign, contains raw data captured from the SnowSAR instrument. The processed SnowSAR data are also archived at NSIDC (DOI: 10.5067/TWRTXCYBCBB8).\n\nThe SnowSAR instrument flew on the NP-3C Orion aircraft and collected data at the X (9.6 GHz) and Ku (17.25 GHz) bands. Data were captured across Colorado, including near the SnowEx 2017 Grand Mesa, Colorado study site and Vail, Colorado. Data were acquired between 16 February 2017 and 22 February 2017.",
-            "title": "SnowEx17 SnowSAR Raw FMCW Waveforms V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FO72K7GAES72W",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FO72K7GAES72W",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_SnowSAR_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_SnowSAR_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1722859882-NSIDC_ECS&q=SNEX17_SnowSAR_Raw&m=38.01043806447779%21-112.38629150390625%215%211%210%210%2C2&tl=1571783818%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1722859882-NSIDC_ECS&q=SNEX17_SnowSAR_Raw&m=38.01043806447779%21-112.38629150390625%215%211%210%210%2C2&tl=1571783818%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_SnowSAR_Raw/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_SnowSAR_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/O72K7GAES72W",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/O72K7GAES72W",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/O72K7GAES72W",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/O72K7GAES72W",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1722859882-NSIDC_ECS",
+            "issued": "2017-02-16",
+            "keyword": [
+                "radar",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/O72K7GAES72W",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-02-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-109.05 37.0 -102.05 41.0",
+            "temporal": "2017-02-16T00:00:00Z/2017-02-22T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx17 SnowSAR Raw FMCW Waveforms V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/7KKNQ5UURM2W",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L3 Radar/Radiometer Global Daily 9 km EASE-Grid Soil Moisture V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/7KKNQ5UURM2W.",
-            "issued": "2015-04-13",
-            "temporal": "2015-04-13T00:00:00Z/2015-07-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-07",
-            "keyword": [
-                "earth science",
-                "radar",
-                "land surface",
-                "microwave",
-                "spectral/engineering",
-                "soils"
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
-            "identifier": "C1236303847-NSIDC_ECS",
             "description": "This Level-3 (L3) soil moisture product provides a daily composite of global land surface conditions retrieved by both the Soil Moisture Active Passive (SMAP) radar and radiometer. SMAP L-band soil moisture data are resampled to an Earth-fixed, global, cylindrical 9 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0).",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP L3 Radar/Radiometer Global Daily 9 km EASE-Grid Soil Moisture V003",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?p=geographic&l=BlueMarble_NextGeneration,SMAP_L3_Active_Passive_Soil_Moisture,SMAP_L3_Active_Passive_Brightness_Temp_H,SMAP_L3_Active_Passive_Brightness_Temp_V,Coastlines&t=2015-04-13",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7KKNQ5UURM2W",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7KKNQ5UURM2W",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL3SMAP.003/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL3SMAP.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1236303847-NSIDC_ECS&m=-33.328125%210.28125%211%211%210%210%2C2&q=SPL3SMAP",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1236303847-NSIDC_ECS&m=-33.328125%210.28125%211%211%210%210%2C2&q=SPL3SMAP",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL3SMAP/versions/3/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL3SMAP/versions/3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL3SMAP.003/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL3SMAP.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1236303847-NSIDC_ECS&m=-33.328125%210.28125%211%211%210%210%2C2&q=SPL3SMAP",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1236303847-NSIDC_ECS&m=-33.328125%210.28125%211%211%210%210%2C2&q=SPL3SMAP",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL3SMAP/versions/3/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL3SMAP/versions/3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?p=geographic&l=BlueMarble_NextGeneration%2CSMAP_L3_Active_Passive_Soil_Moisture%2CSMAP_L3_Active_Passive_Brightness_Temp_H%2CSMAP_L3_Active_Passive_Brightness_Temp_V%2CCoastlines&t=2015-04-13",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?p=geographic&l=BlueMarble_NextGeneration%2CSMAP_L3_Active_Passive_Soil_Moisture%2CSMAP_L3_Active_Passive_Brightness_Temp_H%2CSMAP_L3_Active_Passive_Brightness_Temp_V%2CCoastlines&t=2015-04-13",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7KKNQ5UURM2W",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/7KKNQ5UURM2W",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7KKNQ5UURM2W",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/7KKNQ5UURM2W",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?p=geographic&l=BlueMarble_NextGeneration,SMAP_L3_Active_Passive_Soil_Moisture,SMAP_L3_Active_Passive_Brightness_Temp_H,SMAP_L3_Active_Passive_Brightness_Temp_V,Coastlines&t=2015-04-13",
+            "identifier": "C1236303847-NSIDC_ECS",
+            "issued": "2015-04-13",
+            "keyword": [
+                "earth science",
+                "radar",
+                "land surface",
+                "microwave",
+                "spectral/engineering",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/7KKNQ5UURM2W",
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
+            "title": "SMAP L3 Radar/Radiometer Global Daily 9 km EASE-Grid Soil Moisture V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/789/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
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
-            "identifier": "DASHLINK_789",
             "description": "This article discusses several aspects of uncertainty represen- tation and management for model-based prognostics method- ologies based on our experience with Kalman Filters when applied to prognostics for electronics components. In par- ticular, it explores the implications of modeling remaining useful life prediction as a stochastic process and how it re- lates to uncertainty representation, management, and the role of prognostics in decision-making. A distinction between the interpretations of estimated remaining useful life probability density function and the true remaining useful life probabil- ity density function is explained and a cautionary argument is provided against mixing interpretations for the two while considering prognostics in making critical decisions.",
-            "title": "Uncertainty Representation and Interpretation in Model-based Prognostics Algorithms based on Kalman Filter Estimation",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_PHM_Uncertainty_KF.pdf",
-                    "description": "2012_PHM_Uncertainty_KF.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2012_PHM_Uncertainty_KF.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_PHM_Uncertainty_KF.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2012_PHM_Uncertainty_KF.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_789",
+            "issued": "2013-06-19",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/789/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Uncertainty Representation and Interpretation in Model-based Prognostics Algorithms based on Kalman Filter Estimation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-IRON-COUNTS_V1.0",
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
+            "description": "A global map of gamma ray                counting rates binned on twenty-degree quasi-equal-area                 pixels is provided. The map was determined from a time series           of net counting rates for the 7.6 MeV gamma ray peak produced by        neutron capture with Fe within Ceres' regolith. The data were           acquired by Dawn's Gamma Ray and Neutron Detector (GRaND) while         in low altitude mapping orbit, about 385 km from Ceres' surface         (about 0.8 body radii altitude). Prior to mapping, the time             series counting data were subjected to corrections for variations       in the flux of galactic cosmic rays and measurement geometry,           as described by PRETTYMANETAL2017.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-iron-counts_v1.0_h8jd-mmnw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-IRON-COUNTS_V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-iron-counts_v1.0_h8jd-mmnw",
-            "description": "A global map of gamma ray                counting rates binned on twenty-degree quasi-equal-area                 pixels is provided. The map was determined from a time series           of net counting rates for the 7.6 MeV gamma ray peak produced by        neutron capture with Fe within Ceres' regolith. The data were           acquired by Dawn's Gamma Ray and Neutron Detector (GRaND) while         in low altitude mapping orbit, about 385 km from Ceres' surface         (about 0.8 body radii altitude). Prior to mapping, the time             series counting data were subjected to corrections for variations       in the flux of galactic cosmic rays and measurement geometry,           as described by PRETTYMANETAL2017.",
-            "title": "DAWN GRAND MAP CERES IRON               \n                                      7.6MEV GAMMA COUNTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN GRAND MAP CERES IRON               \n                                      7.6MEV GAMMA COUNTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mro-1232",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/MRO/main/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Beth Beck",
+                "hasEmail": "mailto:beth.beck@nasa.gov"
+            },
+            "description": "Mars Reconnaissance Orbiter Polygons: 1232 Vertices: 1478",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/models/mro-1232/MRO1.fbx.zip",
+                    "mediaType": "application/octet-stream"
+                }
             ],
+            "identifier": "NASA-388",
+            "issued": "2018-06-25",
             "keyword": [
                 "spacecraft",
                 "mro",
@@ -851953,46 +851962,39 @@
                 "satellite",
                 "shuttle"
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
-            "identifier": "NASA-388",
-            "description": "Mars Reconnaissance Orbiter Polygons: 1232 Vertices: 1478",
-            "title": "NASA 3D Models: MRO",
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mro-1232",
+            "modified": "2020-01-29",
             "programCode": [
                 "026:045",
                 "026:046"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/models/mro-1232/MRO1.fbx.zip",
-                    "mediaType": "application/octet-stream"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/MRO/main/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: MRO"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC4-67PCHURYUMOV-M23-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc4-67pchuryumov-m23-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "zeta cas",
@@ -852001,75 +852003,82 @@
                 "international rosetta mission",
                 "dark"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC4-67PCHURYUMOV-M23-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc4-67pchuryumov-m23-v1.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSINAC 2 EDR MTP023 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSINAC 2 EDR MTP023 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RA-4-RDR-SCI-V1.0",
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
+            "description": "The Phoenix Robotic Arm Derived Data consists of Robotic Arm (RA) Scoop Tip position data and components of force exerted by the RA. Data are included for both the spacecraft RA and the Payload Interoperability Testbed (PIT) RA. These data are derived from raw RA telemetry data that are not archived in PDS due to ITAR restrictions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ra-4-rdr-sci-v1.0_h8t8-2cdd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RA-4-RDR-SCI-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ra-4-rdr-sci-v1.0_h8t8-2cdd",
-            "description": "The Phoenix Robotic Arm Derived Data consists of Robotic Arm (RA) Scoop Tip position data and components of force exerted by the RA. Data are included for both the spacecraft RA and the Payload Interoperability Testbed (PIT) RA. These data are derived from raw RA telemetry data that are not archived in PDS due to ITAR restrictions.",
-            "title": "PHOENIX MARS ROBOTIC ARM 4 RDR DERIVED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS ROBOTIC ARM 4 RDR DERIVED V1.0"
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
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_lower_xc_0.8_cm_0.115.dat",
+                    "mediaType": "application/dat"
+                }
             ],
+            "identifier": "NASA-851__11",
+            "issued": "2018-06-25",
             "keyword": [
                 "models",
                 "synthetic",
@@ -852081,42 +852090,47 @@
                 "experiment",
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
-            "identifier": "NASA-851__11",
-            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_lower_xc_0.8_cm_0.115.dat",
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
-            "landingPage": "https://data.nasa.gov/d/h8un-259y",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "To investigate DNA methylation patterns in rat mammary carcinomas induced by ionizing radiation. DNA methylation patterns were analyzed in radiation-induced rat mammary carcinomas and normal mammary gland tissues using CpG island microarray.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-275",
+                    "mediaType": "text/html",
+                    "title": "Global DNA methylation profiling of radiation-induced rat mammary carcinomas"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-275_h8un-259y",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "treatment protocol",
                 "tissue",
@@ -852129,305 +852143,305 @@
                 "dna extraction",
                 "normalization data transformation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/h8un-259y",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-275_h8un-259y",
-            "description": "To investigate DNA methylation patterns in rat mammary carcinomas induced by ionizing radiation. DNA methylation patterns were analyzed in radiation-induced rat mammary carcinomas and normal mammary gland tissues using CpG island microarray.",
-            "title": "Global DNA methylation profiling of radiation-induced rat mammary carcinomas",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-275",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Global DNA methylation profiling of radiation-induced rat mammary carcinomas"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Global DNA methylation profiling of radiation-induced rat mammary carcinomas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NSMGD-SIGW2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/JPL/PO.DAAC. 2006-02-20. NSCAT High-Resolution MGDR, Sigma-0 and Ocean Wind Vectors. Version 2. NSCAT High-Resolution MGDR, Sigma-0 and Ocean Wind Vectors (Dunbar). PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/NSMGD-SIGW2. https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/nscat/doc/l25_usersguide.pdf. NASA/JPL/PO.DAAC, PO.DAAC, 2006-02-20, NSCAT High-Resolution MGDR, Sigma-0 and Ocean Wind Vectors (Dunbar), https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/nscat/doc/l25_usersguide.pdf.",
-            "issued": "2009-06-15",
-            "temporal": "1996-09-15T00:00:00Z/1997-06-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-01-21",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "oceans",
-                "radar",
-                "ocean winds",
-                "sea ice",
-                "spectral/engineering"
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
-            "identifier": "C2617226431-POCLOUD",
-            "description": "The NASA Scatterometer (NSCAT) Level 2.5 high-resolution merged ocean wind vectors and sigma-0 in 25 km wind vector cell (WVC) swaths contain daily data from ascending and descending passes. Wind vectors are accurate to within 2 m/s (vector speed) and 20 degrees (vector direction). Wind vectors are not considered valid in rain contaminated regions; rain flags and precipitation information are not provided. Data is flagged where measurements are either missing or ambiguous. In the presence of land or sea ice winds values are set to 0, and sigma-0 values are preserved where measurements are available. This is the most up-to-date version, which designates the final phase of calibration, validation and science data processing, which was completed in November of 1998, on behalf of the JPL NSCAT Project; wind vectors are processed using the NSCAT-2 geophysical model function.",
-            "release-place": "PO.DAAC",
-            "series-name": "NSCAT High-Resolution MGDR, Sigma-0 and Ocean Wind Vectors",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA/JPL/PO.DAAC",
-            "title": "NSCAT High-Resolution MGDR, Sigma-0 and Ocean Wind Vectors (Dunbar)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_25KM_MGDR_V2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NASA Scatterometer (NSCAT) Level 2.5 high-resolution merged ocean wind vectors and sigma-0 in 25 km wind vector cell (WVC) swaths contain daily data from ascending and descending passes. Wind vectors are accurate to within 2 m/s (vector speed) and 20 degrees (vector direction). Wind vectors are not considered valid in rain contaminated regions; rain flags and precipitation information are not provided. Data is flagged where measurements are either missing or ambiguous. In the presence of land or sea ice winds values are set to 0, and sigma-0 values are preserved where measurements are available. This is the most up-to-date version, which designates the final phase of calibration, validation and science data processing, which was completed in November of 1998, on behalf of the JPL NSCAT Project; wind vectors are processed using the NSCAT-2 geophysical model function.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNSMGD-SIGW2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNSMGD-SIGW2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_25KM_MGDR_V2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_25KM_MGDR_V2.jpg",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/nscat/open/L25/v2/README.txt",
-                    "description": "PO.DAAC Drive",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Drive",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/nscat/open/L25/v2/README.txt",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226431-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226431-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226431-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226431-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_25KM_MGDR_V2.jpg",
+            "identifier": "C2617226431-POCLOUD",
+            "issued": "2009-06-15",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "oceans",
+                "radar",
+                "ocean winds",
+                "sea ice",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/NSMGD-SIGW2",
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
+            "series-name": "NSCAT High-Resolution MGDR, Sigma-0 and Ocean Wind Vectors",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-09-15T00:00:00Z/1997-06-29T23:59:59.999Z",
             "theme": [
                 "NSCAT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NSCAT High-Resolution MGDR, Sigma-0 and Ocean Wind Vectors (Dunbar)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Scholes, R.J., E. Brown de Colstoun, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, and D.R. Landis. 2011. ISLSCP II Global Gridded Soil Characteristics. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1004",
-            "issued": "2023-10-15",
-            "temporal": "1995-01-01T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
-            "keyword": [
-                "earth science",
-                "ecological dynamics",
-                "erosion/sedimentation",
-                "land surface",
-                "soils",
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
-            "identifier": "C2785271209-ORNL_CLOUD",
             "description": "This data set provides gridded data for selected soil parameters derived from data and methods developed by the Global Soil Data Task, an international collaborative project with the objective of making accurate and appropriate data relating to soil properties accessible to the global change research community. The task was coordinated by the International Geosphere-Biosphere Programme (IGBP-DIS). The data in this data set were produced by the International Satellite Land-Surface Climatology Project, Initiative II (ISLSCP II) staff from data obtained from the Oak Ridge National Laboratory Distributed Active Archive Center (ORNL DAAC, http://daac.ornl.gov/). See the related data sets section below. Two-dimensional gridded maps of selected soil parameters, including soil texture, at a 1.0 by 1.0 degree spatial resolution and for two soil depths are provided. All data layers have been adjusted to match the ISLSCP II land/water mask. There are 36 data files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Global Gridded Soil Characteristics",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1004_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/hydrology_soils/islscp2_soils_1deg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/hydrology_soils/islscp2_soils_1deg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/islscp2_soils_1deg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/islscp2_soils_1deg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1004",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1004",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/islscp2_soils_1deg/comp/0_islscp2_soils_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/islscp2_soils_1deg/comp/0_islscp2_soils_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/islscp2_soils_1deg/comp/1_islscp2_soils_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/islscp2_soils_1deg/comp/1_islscp2_soils_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/islscp2_soils_1deg/comp/islscp2_soils_1deg.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/islscp2_soils_1deg/comp/islscp2_soils_1deg.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1004_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1004_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1004",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1004",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1004/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1004/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1004_1_fit.png",
+            "identifier": "C2785271209-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "earth science",
+                "ecological dynamics",
+                "erosion/sedimentation",
+                "land surface",
+                "soils",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1004",
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
+            "temporal": "1995-01-01T00:00:00Z/1996-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II Global Gridded Soil Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/h8xc-7fv2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "treatment protocol   nucleic acid extraction   library construction   nucleic acid sequencing",
-                "spaceflight   altered gravity   light"
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
-            "identifier": "nasa_genelab_GLDS-314_h8xc-7fv2",
             "description": "The response of plants to the spaceflight environment and microgravity is still not well understood although there has been an increased emphasis on this topic. Even less is known about plants  response to partial or reduced gravity levels. In the absence of the directional cues provided by the gravity vector the plant is especially perceptive to other cues such as light. Here we investigate the response of Arabidopsis thaliana 6-day-old seedlings to microgravity and the Mars partial gravity level during spaceflight as well as the effects of red light photostimulation by determining meristematic cell growth and proliferation. These experiments involve microscopic techniques together with transcriptomic studies. We demonstrate that microgravity and partial gravity trigger differential responses. The microgravity environment activates hormonal routes responsible for proliferation/growth and upregulates plastid/mitochondrial-encoded transcripts even in the dark. In contrast the Mars gravity level inhibits these routes and activates responses to stress factors to restore cell growth parameters only when red photostimulation is provided. This response is accompanied by upregulation of numerous transcription factors such as the environmental acclimation-related WRKY family. In the long term these discoveries can be applied in the design of bioregenerative life support systems and space farming.",
-            "title": "Adaptive response of Arabidopsis seedlings in microgravity and Mars reduced gravity environment is enhanced by red light photostimulation",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-314",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-314",
+                    "mediaType": "text/html",
                     "title": "Adaptive response of Arabidopsis seedlings in microgravity and Mars reduced gravity environment is enhanced by red light photostimulation"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-314_h8xc-7fv2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "treatment protocol   nucleic acid extraction   library construction   nucleic acid sequencing",
+                "spaceflight   altered gravity   light"
+            ],
+            "landingPage": "https://data.nasa.gov/d/h8xc-7fv2",
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
+            "title": "Adaptive response of Arabidopsis seedlings in microgravity and Mars reduced gravity environment is enhanced by red light photostimulation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/h8y7-i98w",
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
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-98",
+                    "mediaType": "text/html",
+                    "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse adrenal gland transcriptomic proteomic and epigenomic data"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-98_h8y7-i98w",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "mass spectrometry",
                 "labeling",
@@ -852442,71 +852456,35 @@
                 "microgravity",
                 "library construction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/h8y7-i98w",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-98_h8y7-i98w",
-            "description": "NASA  s Rodent Research (RR) project is playing a critical role in advancing biomedical research on the physiological effects of space environments. Due to the limited resources for conducting biological experiments aboard the International Space Station (ISS) it is imperative to use crew time efficiently while maximizing high-quality science return. NASA  s GeneLab project has as its primary objectives to 1) further increase the value of these experiments using a multi-omics systems biology-based approach and 2) disseminate these data without restrictions to the scientific community. The current investigation assessed viability of RNA DNA and protein extracted from archived RR-1 tissue samples for epigenomic transcriptomic and proteomic assays. During the first RR spaceflight experiment a variety of tissue types were harvested from subjects snap-frozen or RNAlater-preserved and then stored at least a year at -80C after return to Earth. They were then prioritized for this investigation based on likelihood of significant scientific value for spaceflight research. All tissues were made available to GeneLab through the bio-specimen sharing program managed by the Ames Life Science Data Archive and included mouse adrenal glands quadriceps gastrocnemius tibialis anterior extensor digitorum longus soleus eye and kidney. We report here protocols for and results of these tissue extractions and thus the feasibility and value of these kinds of omics analyses. In addition to providing additional opportunities for investigation of spaceflight effects on the mouse transcriptome and proteome in new kinds of tissues our results may also be of value to program managers for the prioritization of ISS crew time for rodent research activities.",
-            "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse adrenal gland transcriptomic proteomic and epigenomic data",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-98",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse adrenal gland transcriptomic proteomic and epigenomic data"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse adrenal gland transcriptomic proteomic and epigenomic data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274246684-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Goddard Space Flight Center (GSFC). 2016-05-31. ESMRN5L1. Version 001. ESMR/Nimbus-5 Level 1 Calibrated Brightness Temperature V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/ESMRN5L1_001.html. Digital Science Data.",
-            "issued": "2014-05-12",
-            "temporal": "1972-12-11T00:00:00Z/1977-05-16T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-05-12",
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
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
-            "identifier": "C1274246684-GES_DISC",
-            "description": "ESMRN5L1 is the Nimbus-5 Electrically Scanning Microwave Radiometer (ESMR) Level 1 Calibrated Brightness Temperature product and contains calibrated radiances expressed in units of brightness temperature measured at 19.35 GHz. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as the Calibrated Brightness Temperature Tapes (CBTT). The data are archived in their original IBM binary proprietary format, also referred to as a binary TAP file.\n\nThe Nimbus-5 satellite was successfully launched on December 11, 1972. The ESMR experiment on Nimbus-5 continued the measurements made by its predecessor flown on Nimbus-4. The ESMR instrument objectives were (1) to derive the liquid water content of clouds from brightness temperatures over oceans, (2) to observe differences between sea ice and the open sea over the polar caps, and (3) to test the feasibility of inferring surface composition and soil moisture.\n\nThe ESMR Principal Investigator was Dr. Thomas T. Wilheit, Jr. from NASA Goddard Space Flight Center. The Nimbus-5 ESMR data are available from December 11, 1972 (day of year 346) through May 16, 1977 (day of year 136)\n\nThis product was previously available from the NSSDC with the identifier ESAD-00219 (old ID 72-097A-04A).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ESMRN5L1",
             "creator": "NASA Goddard Space Flight Center (GSFC)",
-            "title": "ESMR/Nimbus-5 Level 1 Calibrated Brightness Temperature V001 (ESMRN5L1) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ESMRN5L1_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ESMRN5L1 is the Nimbus-5 Electrically Scanning Microwave Radiometer (ESMR) Level 1 Calibrated Brightness Temperature product and contains calibrated radiances expressed in units of brightness temperature measured at 19.35 GHz. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as the Calibrated Brightness Temperature Tapes (CBTT). The data are archived in their original IBM binary proprietary format, also referred to as a binary TAP file.\n\nThe Nimbus-5 satellite was successfully launched on December 11, 1972. The ESMR experiment on Nimbus-5 continued the measurements made by its predecessor flown on Nimbus-4. The ESMR instrument objectives were (1) to derive the liquid water content of clouds from brightness temperatures over oceans, (2) to observe differences between sea ice and the open sea over the polar caps, and (3) to test the feasibility of inferring surface composition and soil moisture.\n\nThe ESMR Principal Investigator was Dr. Thomas T. Wilheit, Jr. from NASA Goddard Space Flight Center. The Nimbus-5 ESMR data are available from December 11, 1972 (day of year 346) through May 16, 1977 (day of year 136)\n\nThis product was previously available from the NSSDC with the identifier ESAD-00219 (old ID 72-097A-04A).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -852515,83 +852493,107 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ESMRN5L1_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ESMRN5L1_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/s4pa/Nimbus5_ESMR_Level1/ESMRN5L1.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/s4pa/Nimbus5_ESMR_Level1/ESMRN5L1.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ESMRN5L1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ESMRN5L1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_ESMR_Level1/ESMRN5L1.001/doc/README.ESMRN5L1.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_ESMR_Level1/ESMRN5L1.001/doc/README.ESMRN5L1.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N5_Users_Guide.pdf",
-                    "description": "Nimbus 5 User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 5 User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N5_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.7_Validation/ESMR_NimbusE_19730023610.pdf",
-                    "description": "Nimbus 5 ESMR Report",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 5 ESMR Report",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.7_Validation/ESMR_NimbusE_19730023610.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus5.tar.gz",
-                    "description": "Nimbus 5 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 5 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus5.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N5_ESMR_Inventory.xlsx",
-                    "description": "N5 ESMR Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N5 ESMR Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N5_ESMR_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ESMRN5L1_001.png",
+            "identifier": "C1274246684-GES_DISC",
+            "issued": "2014-05-12",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274246684-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-05-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ESMRN5L1",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1972-12-11T00:00:00Z/1977-05-16T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ESMR/Nimbus-5 Level 1 Calibrated Brightness Temperature V001 (ESMRN5L1) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acassini_vims_saturn&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains Cassini VIMS data, metadata, and associated documentation for the Saturn tour--January 2004 through end of mission in September 2017.",
+            "identifier": "urn:nasa:pds:cassini_vims_saturn",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "rx leporis",
                 "hyperion",
@@ -852711,685 +852713,685 @@
                 "ymir",
                 "zeta orionis"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acassini_vims_saturn&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:cassini_vims_saturn",
-            "description": "This bundle contains Cassini VIMS data, metadata, and associated documentation for the Saturn tour--January 2004 through end of mission in September 2017.",
-            "title": "VIMS Observations from the Cassini Tour of the Saturn System",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VIMS Observations from the Cassini Tour of the Saturn System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ORACLES/RADIANCE/TERRAIN_V006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-07-05. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ORACLES/RADIANCE/TERRAIN_V006.",
-            "issued": "2017-07-18",
-            "temporal": "2016-07-28T00:00:00Z/2016-10-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-11",
-            "keyword": [
-                "visible wavelengths",
-                "ultraviolet wavelengths",
-                "spectral/engineering",
-                "earth science"
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
-            "identifier": "C1459296627-LARC_ASDC",
             "description": "AirMSPI_ORACLES_Terrain-projected_Georegistered_Radiance_Data are AirMSPI Terrain-projected georegistered radiance product acquired during the NASA ObseRvations of Aerosols above CLouds and their intEractionS (ORACLES) flight campaign.\r\n\r\nAirMSPI Level 1B2 products contain radiometric and polarimetric images of clouds, aerosols, and the surface of the Earth. In particular, products contain map-projected data at 8 wavelengths: 355, 380, 445, 470, 555, 660, 865, and 935 nm. The data products include radiance, time, solar zenith, solar azimuth, view zenith, and view azimuth for all spectral bands. Wavelengths for which polarization information is available (470, 660, and 865 nm) also include the Stokes parameters Q and U, as well as degree of linear polarization (DOLP) and angle of linear polarization (AOLP). Q, U, and AOLP are reported relative to both the scattering and view meridional planes. Files are distributed in HDF-EOS-5 format.\r\n\r\nThis release of AirMPSI data contains all targets acquired during the ObseRvations of Aerosols above CLouds and their intEractionS (ORACLES) flight campaign, including the check-out and transit flights. ORACLES was based out of Walvis Bay, Namibia and focused on the South Atlantic Ocean off the coast of Namibia and Angola. AirMSPI was acquired from July 28 to October 6, 2016. More details about the ORACLES campaign and AirMSPI participation can be found at https://espo.nasa.gov/oracles (link is external).",
-            "title": "AirMSPI verison 6 terrain-projected georegistered radiance product acquired during the NASA ORACLES flight campaign Jul-Oct 2016",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FORACLES%2FRADIANCE%2FTERRAIN_V006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FORACLES%2FRADIANCE%2FTERRAIN_V006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMSPI",
-                    "description": "ASDC Data and Information for AirMSPI",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for AirMSPI",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMSPI",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1459296627-LARC_ASDC",
-                    "description": "Earthdata Search for AirMSPI_ORACLES_Terrain-projected_Georegistered_Radiance_Data_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for AirMSPI_ORACLES_Terrain-projected_Georegistered_Radiance_Data_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1459296627-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/oracles",
-                    "description": "ESPO home page for ORACLES",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO home page for ORACLES",
+                    "downloadURL": "https://espo.nasa.gov/oracles",
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
-                    "downloadURL": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ORACLES/RADIANCE/TERRAIN_V006",
-                    "description": "DOI data set landing page for AirMSPI_ORACLES_Terrain-projected_Georegistered_Radiance_Data_6",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for AirMSPI_ORACLES_Terrain-projected_Georegistered_Radiance_Data_6",
+                    "downloadURL": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ORACLES/RADIANCE/TERRAIN_V006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/AirMSPI_L1B2_DPS.RevC.20180223.pdf",
-                    "description": "Data Product Specification for the AirMSPI Level 1B2 Products (V006)",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for the AirMSPI Level 1B2 Products (V006)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/AirMSPI_L1B2_DPS.RevC.20180223.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.jpl.nasa.gov/instruments/airmspi",
-                    "description": "NASA JPL Airborne Instrument AirMSPI Overview",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Airborne Instrument AirMSPI Overview",
+                    "downloadURL": "https://airbornescience.jpl.nasa.gov/instruments/airmspi",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://airbornescience.nasa.gov/instrument/AirMSPI",
-                    "description": "NASA Airborne Science Program Instrumentation page for AirMSPI",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Airborne Science Program Instrumentation page for AirMSPI",
+                    "downloadURL": "https://airbornescience.nasa.gov/instrument/AirMSPI",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/quality_summaries/AirMSPI-Data_Quality-V006_ORACLES.pdf",
-                    "description": "AirMSPI Data Quality Statement: ORACLES Campaign (September - October 2016)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMSPI Data Quality Statement: ORACLES Campaign (September - October 2016)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/quality_summaries/AirMSPI-Data_Quality-V006_ORACLES.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMSPI/ORACLES/ER2_GRP_TERRAIN/V006/",
-                    "description": "ASDC Direct Data Download for AirMSPI_ORACLES_Terrain-projected_Georegistered_Radiance_Data_6",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for AirMSPI_ORACLES_Terrain-projected_Georegistered_Radiance_Data_6",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMSPI/ORACLES/ER2_GRP_TERRAIN/V006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMSPI/ORACLES/ER2_GRP_TERRAIN/V006/contents.html",
-                    "description": "OPeNDAP data access for AirMSPI_ORACLES_Terrain-projected_Georegistered_Radiance_Data_6",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for AirMSPI_ORACLES_Terrain-projected_Georegistered_Radiance_Data_6",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMSPI/ORACLES/ER2_GRP_TERRAIN/V006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1459296627-LARC_ASDC",
+            "issued": "2017-07-18",
+            "keyword": [
+                "visible wavelengths",
+                "ultraviolet wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ORACLES/RADIANCE/TERRAIN_V006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-24.0 -126.0 -24.0 15.0 40.0 15.0 40.0 -126.0 -24.0 -126.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2016-07-28T00:00:00Z/2016-10-06T23:59:59.999Z",
             "theme": [
                 "AIRMSPI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMSPI verison 6 terrain-projected georegistered radiance product acquired during the NASA ORACLES flight campaign Jul-Oct 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H47D2S2F",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center of China Studies - CCS - University of Michigan, China in Time and Space - CITAS - University of Washington, and Center for International Earth Science Information Network - CIESIN. 1996-12-31. China Dimensions Data Collection: China County-Level Data from Provincial Economic Yearbooks, Keyed to 1:1M GIS Map. Version 1.00. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H47D2S2F. https://doi.org/10.7927/H47D2S2F.",
-            "issued": "1996-12-31",
-            "temporal": "1990-01-01T00:00:00Z/1991-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4RB72JW",
-                "https://doi.org/10.7927/H4QC01D2",
-                "https://doi.org/10.7927/H4C24TCF",
-                "https://doi.org/10.7927/H4GT5K3V",
-                "https://doi.org/10.7927/H4KK98PS",
-                "https://doi.org/10.7927/H4MK69T5",
-                "https://doi.org/10.7927/H4ZW1HVD",
-                "https://doi.org/10.7927/H43N21B3",
-                "https://doi.org/10.7927/H4V40S4D",
-                "https://doi.org/10.7927/H4FT8HZ2"
-            ],
-            "keyword": [
-                "boundaries",
-                "human dimensions",
-                "economic resources",
-                "earth science",
-                "socioeconomics"
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
-            "identifier": "C179001904-SEDAC",
-            "description": "The China County-Level Data on Provincial Economic Yearbooks, Keyed To 1:1M GIS Map consists of socioeconomic and boundary data for the administrative regions of China for 1990 and 1991. The socioeconomic data includes natural resources, population, employment, investment, wage, public finance, price, people's livelihood, agriculture, industry, energy, production, transportation, telecommunication, construction, trade, tourism, environmental protection, education, science, patents, culture, sports, health care, and social welfare. The boundary data are at a scale of one to one million (1:1M) at the county level. This data set is produced in collaboration with the University of Washington as part of the China in Time and Space (CITAS) project, University of Michigan Center of China Studies (CCS), and the Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center of China Studies - CCS - University of Michigan, China in Time and Space - CITAS - University of Washington, and Center for International Earth Science Information Network - CIESIN",
-            "title": "China Dimensions Data Collection: China County-Level Data from Provincial Economic Yearbooks, Keyed to 1:1M GIS Map",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-provincial-economic-yearbooks/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The China County-Level Data on Provincial Economic Yearbooks, Keyed To 1:1M GIS Map consists of socioeconomic and boundary data for the administrative regions of China for 1990 and 1991. The socioeconomic data includes natural resources, population, employment, investment, wage, public finance, price, people's livelihood, agriculture, industry, energy, production, transportation, telecommunication, construction, trade, tourism, environmental protection, education, science, patents, culture, sports, health care, and social welfare. The boundary data are at a scale of one to one million (1:1M) at the county level. This data set is produced in collaboration with the University of Washington as part of the China in Time and Space (CITAS) project, University of Michigan Center of China Studies (CCS), and the Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH47D2S2F",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH47D2S2F",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-provincial-economic-yearbooks/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-provincial-economic-yearbooks/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-provincial-economic-yearbooks/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-provincial-economic-yearbooks/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cddc-china-provincial-economic-yearbooks/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cddc-china-provincial-economic-yearbooks/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-provincial-economic-yearbooks",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-provincial-economic-yearbooks",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-provincial-economic-yearbooks/sedac-logo.jpg",
+            "identifier": "C179001904-SEDAC",
+            "issued": "1996-12-31",
+            "keyword": [
+                "boundaries",
+                "human dimensions",
+                "economic resources",
+                "earth science",
+                "socioeconomics"
+            ],
+            "landingPage": "https://doi.org/10.7927/H47D2S2F",
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
+                "https://doi.org/10.7927/H4RB72JW",
+                "https://doi.org/10.7927/H4QC01D2",
+                "https://doi.org/10.7927/H4C24TCF",
+                "https://doi.org/10.7927/H4GT5K3V",
+                "https://doi.org/10.7927/H4KK98PS",
+                "https://doi.org/10.7927/H4MK69T5",
+                "https://doi.org/10.7927/H4ZW1HVD",
+                "https://doi.org/10.7927/H43N21B3",
+                "https://doi.org/10.7927/H4V40S4D",
+                "https://doi.org/10.7927/H4FT8HZ2"
+            ],
+            "release-place": "Saginaw, MI",
             "spatial": "73.0 18.0 135.0 54.0",
+            "temporal": "1990-01-01T00:00:00Z/1991-12-31T00:00:00Z",
             "theme": [
                 "CDDC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "China Dimensions Data Collection: China County-Level Data from Provincial Economic Yearbooks, Keyed to 1:1M GIS Map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-SUMM-ION-SOLARWIND-96S-V1.0",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-summ-ion-solarwind-96s-v1.0_h97j-mcap",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-SUMM-ION-SOLARWIND-96S-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-summ-ion-solarwind-96s-v1.0_h97j-mcap",
-            "description": "not applicable",
-            "title": "VG2 SAT PLS DERIVED ION SOLAR WIND BROWSE 96SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SAT PLS DERIVED ION SOLAR WIND BROWSE 96SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/O0XI8PPYEZJ6",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Quicklook Arctic Weekly EASE-Grid Sea Ice Motion Vectors, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/O0XI8PPYEZJ6.",
-            "issued": "2024-01-01",
-            "temporal": "2024-01-01T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "keyword": [
-                "sea ice",
-                "earth science",
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
-            "identifier": "C1613624767-NSIDCV0",
             "description": "This data set is the quicklook version of the Polar Pathfinder Daily 25 km EASE-Grid Sea Ice Motion Vectors product (https://nsidc.org/data/nsidc-0116). It contains weekly sea ice motion vectors, as well as browse images representing the weekly data. Weekly sea ice motion vectors are derived from near-real-time SSMI/S data sets, IABP buoys, and NCEP/NCAR Reanalysis forecasts.",
-            "title": "Quicklook Arctic Weekly EASE-Grid Sea Ice Motion Vectors, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FO0XI8PPYEZJ6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FO0XI8PPYEZJ6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0748_ql_icemotion/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0748_ql_icemotion/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0748_ql_icemotion/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0748_ql_icemotion/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/O0XI8PPYEZJ6",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/O0XI8PPYEZJ6",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/O0XI8PPYEZJ6",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/O0XI8PPYEZJ6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1613624767-NSIDCV0",
+            "issued": "2024-01-01",
+            "keyword": [
+                "sea ice",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/O0XI8PPYEZJ6",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 29.7 180.0 90.0",
+            "temporal": "2024-01-01T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Quicklook Arctic Weekly EASE-Grid Sea Ice Motion Vectors, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-IOF-SCI-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Science RDR data set contains Incidence Over Flux (IOF) data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-iof-sci-v1.0_h9ac-zfvc",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-IOF-SCI-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-iof-sci-v1.0_h9ac-zfvc",
-            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Science RDR data set contains Incidence Over Flux (IOF) data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 INCID OVER FLX SCI V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 INCID OVER FLX SCI V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESCH4LN_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "issued": "2014-08-20",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-10-28",
-            "keyword": [
-                "atmosphere",
-                "air quality",
-                "earth science",
-                "atmospheric chemistry/carbon and hydrocarbon compounds"
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
-            "identifier": "C1000000320-LARC",
             "description": "Atmospheric vertical profile estimates and associated errors including the mapping matrix to relate the reduced-size retrieval vectors, covariances, and averaging kernels back to the TES forward model pressure grid.",
-            "title": "TES/Aura L2 Methane Lite Nadir V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESCH4LN_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESCH4LN_L2.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C1000000320-LARC",
+            "issued": "2014-08-20",
+            "keyword": [
+                "atmosphere",
+                "air quality",
+                "earth science",
+                "atmospheric chemistry/carbon and hydrocarbon compounds"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TESCH4LN_L2.006",
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
+            "title": "TES/Aura L2 Methane Lite Nadir V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625667016-LAADS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "European Space Agency. 2019-08-01. SLSTR/Sentinel-3B L1 Full Resolution Top of Atmosphere Radiances and Brightness Temperature. Version 1.",
-            "issued": "2019-08-01",
-            "temporal": "2018-04-25T18:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "keyword": [
-                "platform characteristics",
-                "infrared wavelengths",
-                "sensor characteristics",
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LAADS USER SUPPORT TEAM",
                 "hasEmail": "mailto:ops@eumetsat.int"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1625667016-LAADS",
-            "description": "The SLSTR/Sentinel-3B L1 Full Resolution Top of Atmosphere Radiances and Brightness Temperature product with shortname S3B_SL_1_RBT, is generated from the data acquired by the Sea and Land Surface Temperature Radiometer (SLSTR), on-board SENTINEL-3, is a dual scan temperature radiometer. The principal aim of the SLSTR instrument is to maintain continuity with the AATSR series of instruments. The SLSTR instrument design incorporates the basic functionality of AATSR in addition to new, more advanced features including a wider swath, new channels (including two channels dedicated to fire detection), and higher resolution in some channels. The principal objective of SLSTR products is to provide global and regional Sea and Land Surface Temperature (SST, LST) to a very high level of accuracy (better than 0.3 K) for both climatological and meteorological applications.\r\n\r\nFor more information about the instrument and the mission, visit \"Sentinel Online\" at https://sentinel.esa.int/web/sentinel/home. \r\n\r\nThe S3B_SL_1_RBT is a Level 1B product which consist of full resolution, geolocated, co-located nadir and along track view, Top of Atmosphere (TOA) brightness temperatures (in the case of thermal IR channels) or radiances (in the case of visible, NIR and SWIR channels) from all SLSTR channels. It also contains quality flags, pixel classification information and meteorological annotations. Based on components activated by configuration which are not part of the operational production baseline, the S3B_SL_1_RBT may contain 77 or 111 files. Out of the these files, 22 or 34 files contain the actual measurements, where the other 54 or 76 files contain the annotations data.\r\n\r\nFor more information about the product, read the SENTINEL-3 SLSTR User Guide at https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-slstr",
             "creator": "European Space Agency",
-            "title": "SLSTR/Sentinel-3B L1 Full Resolution Top of Atmosphere Radiances and Brightness Temperature",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SLSTR/Sentinel-3B L1 Full Resolution Top of Atmosphere Radiances and Brightness Temperature product with shortname S3B_SL_1_RBT, is generated from the data acquired by the Sea and Land Surface Temperature Radiometer (SLSTR), on-board SENTINEL-3, is a dual scan temperature radiometer. The principal aim of the SLSTR instrument is to maintain continuity with the AATSR series of instruments. The SLSTR instrument design incorporates the basic functionality of AATSR in addition to new, more advanced features including a wider swath, new channels (including two channels dedicated to fire detection), and higher resolution in some channels. The principal objective of SLSTR products is to provide global and regional Sea and Land Surface Temperature (SST, LST) to a very high level of accuracy (better than 0.3 K) for both climatological and meteorological applications.\r\n\r\nFor more information about the instrument and the mission, visit \"Sentinel Online\" at https://sentinel.esa.int/web/sentinel/home. \r\n\r\nThe S3B_SL_1_RBT is a Level 1B product which consist of full resolution, geolocated, co-located nadir and along track view, Top of Atmosphere (TOA) brightness temperatures (in the case of thermal IR channels) or radiances (in the case of visible, NIR and SWIR channels) from all SLSTR channels. It also contains quality flags, pixel classification information and meteorological annotations. Based on components activated by configuration which are not part of the operational production baseline, the S3B_SL_1_RBT may contain 77 or 111 files. Out of the these files, 22 or 34 files contain the actual measurements, where the other 54 or 76 files contain the annotations data.\r\n\r\nFor more information about the product, read the SENTINEL-3 SLSTR User Guide at https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-slstr",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/450/S3B_SL_1_RBT/",
-                    "description": "Direct access to S3B_SL_1_RBT C1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to S3B_SL_1_RBT C1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/450/S3B_SL_1_RBT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-olci/processing-levels/level-1",
-                    "description": "The product User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "The product User\u2019s Guide",
+                    "downloadURL": "https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-olci/processing-levels/level-1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C1625667016-LAADS",
+            "issued": "2019-08-01",
+            "keyword": [
+                "platform characteristics",
+                "infrared wavelengths",
+                "sensor characteristics",
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625667016-LAADS.html",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-04-25T18:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "Sentinel-3B",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SLSTR/Sentinel-3B L1 Full Resolution Top of Atmosphere Radiances and Brightness Temperature"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/26",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Matson, P.A. 1994. Canopy Chemistry (OTTER) . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/26",
-            "issued": "2023-11-19",
-            "temporal": "1989-08-23T00:00:00Z/1991-06-04T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
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
-            "identifier": "C2804747736-ORNL_CLOUD",
             "description": "Canopy characteristics: leaf chemistry, specific leaf area, LAI, PAR, IPAR, NPP, standing biomass--see also: Meteorology (OTTER) for associated meteorological conditions",
-            "graphic-preview-description": "Browse Image",
-            "title": "Canopy Chemistry (OTTER)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/otter_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F26",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F26",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/otter/chem/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/otter/chem/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/OTTER/guides/Canopy_Characteristics.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/OTTER/guides/Canopy_Characteristics.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/26",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/26",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/chem/comp/Canopy_Characteristics.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/chem/comp/Canopy_Characteristics.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/chem/comp/metchem.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/chem/comp/metchem.txt",
+                    "mediaType": "text/html",
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
+            "identifier": "C2804747736-ORNL_CLOUD",
+            "issued": "2023-11-19",
+            "keyword": [
+                "ecological dynamics",
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/26",
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
             "spatial": "-123.94 44.29 -121.33 45.06",
+            "temporal": "1989-08-23T00:00:00Z/1991-06-04T23:59:59Z",
             "theme": [
                 "OTTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Canopy Chemistry (OTTER)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-ESC3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 3 mission phase, which took place between 2015-07-01 and 2015-10-21.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-esc3-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "calibration",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-ESC3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-esc3-v1.0",
-            "description": "This data set contains CODMAC Level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 3 mission phase, which took place between 2015-07-01 and 2015-10-21.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 ESC3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 ESC3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH%2FSW-EPPS-3-EPS-CDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER Energetic Particle and Plasma Spectrometer (EPPS) calibrated observations, also known as CDRs. The system encompasses 2 instrument subsystems - the Energetic Particle Spectrometer (EPS) and the Fast Imaging Plasma Spectrometer (FIPS). This data set contains EPS instrument data. EPS covers the energy range of 25 to > 500 keV for electrons, and 10 keV/nucleon to ~3 MeV total energy for ions. There are seven CDR data products for EPS",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-sw-epps-3-eps-cdr-v1.0_h9i7-vmp6",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "mercury",
@@ -853397,129 +853399,103 @@
                 "messenger",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH%2FSW-EPPS-3-EPS-CDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-sw-epps-3-eps-cdr-v1.0_h9i7-vmp6",
-            "description": "Abstract ======== This data set consists of the MESSENGER Energetic Particle and Plasma Spectrometer (EPPS) calibrated observations, also known as CDRs. The system encompasses 2 instrument subsystems - the Energetic Particle Spectrometer (EPS) and the Fast Imaging Plasma Spectrometer (FIPS). This data set contains EPS instrument data. EPS covers the energy range of 25 to > 500 keV for electrons, and 10 keV/nucleon to ~3 MeV total energy for ions. There are seven CDR data products for EPS",
-            "title": "MESSENGER E/V/H/SW EPPS CALIBRATED EPS CDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER E/V/H/SW EPPS CALIBRATED EPS CDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206874-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Land Resources of Russia -- Maps of Permafrost and Ground Ice, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1996-01-01",
-            "temporal": "1996-01-01T00:00:00Z/1996-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-31",
-            "keyword": [
-                "cryosphere",
-                "soils",
-                "agriculture",
-                "frozen ground",
-                "land surface",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vladamir Kotlyakov",
                 "hasEmail": "mailto:kun@mikun.msk.su"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206874-NSIDCV0",
             "description": "This data set includes maps of permafrost extent, permafrost temperature, the permafrost boundary, and ground ice thickness for all of Russia. The maps are ESRI Shapefiles, which were digitized from paper maps taken from the World Atlas of Snow and Ice Resources, 1997, Institute of Geography, Russian Academy of Sciences, Moscow, Russia. The scale of the source maps range from 1:20,000,000 to 1:40,000,000. Polygons were assigned attributes based on the classes used in the legends of the paper map.\n\nThese data were extracted from a larger collection entitled Land Resources of Russia. Data and documentation &copy; 2002 copyright International Institute for Applied Systems Analysis and the Russian Academy of Sciences.",
-            "title": "Land Resources of Russia -- Maps of Permafrost and Ground Ice, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD600_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD600_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD600/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD600/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD600/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD600/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206874-NSIDCV0",
+            "issued": "1996-01-01",
+            "keyword": [
+                "cryosphere",
+                "soils",
+                "agriculture",
+                "frozen ground",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206874-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "27.3 41.2 180.0 77.7",
+            "temporal": "1996-01-01T00:00:00Z/1996-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Land Resources of Russia -- Maps of Permafrost and Ground Ice, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273348581-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Swinbank, Richard, et al.. 1994-03-22. UARZCUKM. Version 001. UARS Correlative UKMO Daily Gridded Stratospheric Assimilated Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/UARZCUKM_001.html. Digital Science Data.",
-            "issued": "1991-10-17",
-            "temporal": "1991-10-17T00:00:00Z/2001-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1991-10-17",
-            "keyword": [
-                "atmosphere",
-                "altitude",
-                "atmospheric temperature",
-                "atmospheric winds",
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
-            "identifier": "C1273348581-GES_DISC",
-            "description": "The UARS Correlative assimilation data from the U.K. Meteorological Office (UKMO) consists of daily model runs at 12:00 GMT as a means of providing an independent analysis for comparison with data from the UARS instruments. The UKMO product includes temperature (Kelvin), geopotential height (m), zonal and meridional wind components (m/s), and vertical velocity (Pa/s). Note: vertical velocity (omega) data are available from 26 August 1992 forward.\n\nThe numerical Unified Model used in the assimilation system is a global primitive equation model, with a split-explicit time integration scheme. It incorporates a comprehensive range of physical parameterization schemes. It uses a hybrid vertical coordinate system, with terrain-following model levels at low levels, gradually changing to pressure levels in the stratosphere. The input to the assimilation system are from the World Weather Watch network of surface and upper air observations and satellite data.\n\nThe UKMO correlative product consists of a single granule per day containing all the geophysical parameters. Data coverage is global for where the horizontal resolution is 2.5 degrees latitude by 3.75 degrees longitude, using a staggered grid system. For parameters other than wind components, each horizontal field consists of 73 rows of 96 points, starting at 90N, 0E. The wind data are staggered by half a grid, starting at 88.75N, 1.875E (with 72 rows).\n\nThe UKMO correlative assimilation data are on the UARS standard pressure levels (in mbars) given by:\n\nP(i) = 1000 * 10**(-i/6)  for i = 0, 1, 2, ...\n\nThe data files are available in a binary record oriented format.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "UARZCUKM",
             "creator": "Swinbank, Richard, et al.",
-            "title": "UARS Correlative UKMO Daily Gridded Stratospheric Assimilated Data V001 (UARZCUKM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/UARZCUKM_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The UARS Correlative assimilation data from the U.K. Meteorological Office (UKMO) consists of daily model runs at 12:00 GMT as a means of providing an independent analysis for comparison with data from the UARS instruments. The UKMO product includes temperature (Kelvin), geopotential height (m), zonal and meridional wind components (m/s), and vertical velocity (Pa/s). Note: vertical velocity (omega) data are available from 26 August 1992 forward.\n\nThe numerical Unified Model used in the assimilation system is a global primitive equation model, with a split-explicit time integration scheme. It incorporates a comprehensive range of physical parameterization schemes. It uses a hybrid vertical coordinate system, with terrain-following model levels at low levels, gradually changing to pressure levels in the stratosphere. The input to the assimilation system are from the World Weather Watch network of surface and upper air observations and satellite data.\n\nThe UKMO correlative product consists of a single granule per day containing all the geophysical parameters. Data coverage is global for where the horizontal resolution is 2.5 degrees latitude by 3.75 degrees longitude, using a staggered grid system. For parameters other than wind components, each horizontal field consists of 73 rows of 96 points, starting at 90N, 0E. The wind data are staggered by half a grid, starting at 88.75N, 1.875E (with 72 rows).\n\nThe UKMO correlative assimilation data are on the UARS standard pressure levels (in mbars) given by:\n\nP(i) = 1000 * 10**(-i/6)  for i = 0, 1, 2, ...\n\nThe data files are available in a binary record oriented format.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -853528,303 +853504,306 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/UARZCUKM_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/UARZCUKM_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_Correlative_Level4/UARZCUKM/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_Correlative_Level4/UARZCUKM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=UARZCUKM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=UARZCUKM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://uars.gsfc.nasa.gov/",
-                    "description": "The UARS Project Homepage.",
                     "@type": "dcat:Distribution",
+                    "description": "The UARS Project Homepage.",
+                    "downloadURL": "https://uars.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_Correlative_Level4/UARZCUKM/doc/README.UARCorr.doc",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_Correlative_Level4/UARZCUKM/doc/README.UARCorr.doc",
+                    "mediaType": "application/msword",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/UARZCUKM_001.png",
+            "identifier": "C1273348581-GES_DISC",
+            "issued": "1991-10-17",
+            "keyword": [
+                "atmosphere",
+                "altitude",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273348581-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1991-10-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "UARZCUKM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1991-10-17T00:00:00Z/2001-09-30T23:59:59.999Z",
             "theme": [
                 "UARS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "UARS Correlative UKMO Daily Gridded Stratospheric Assimilated Data V001 (UARZCUKM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2182",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Joiner, J., Y. Yoshida, P. Koehler, C. Frankenberg, and N.C. Parazoo. 2023. L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-B GOME-2, 2013-2021. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2182",
-            "issued": "2024-01-18",
-            "temporal": "2013-04-01T00:02:57Z/2021-06-07T22:56:12Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-22",
-            "keyword": [
-                "land surface",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
-                "surface radiative properties",
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
-            "identifier": "C2840822442-ORNL_CLOUD",
             "description": "This dataset provides Level 2 (L2) Solar-Induced Fluorescence (SIF) of chlorophyll estimates derived from the Global Ozone Monitoring Experiment 2 (GOME-2) instrument on the European Meteorological Satellite (EUMETSAT) MetOp-B with ~0.5 nm spectral resolution and wavelengths between 734 and 758 nm. GOME-2 covers global land (observations up to 75-degree solar zenith angle) at a resolution of approximately 40 km x 80. Data are provided for the period from 2013-04-01 to 2021-06-07. Each file contains daily raw and bias-adjusted solar-induced fluorescence along with quality control information and ancillary data. SIF measurements can provide information on the functional status of vegetation including light-use efficiency and global primary productivity that can be used for global carbon cycle modeling and agricultural applications. The GOME-2 SIF product is inherently noisy owing to low signal levels and has undergone only a limited amount of validation. The data are provided in netCDF (*.nc) format.",
-            "graphic-preview-description": "Monthly mean solar-induced fluorescence (SIF) values (mW m-2 nm-1 sr-1) at 740 nm and gridded at 0.5-degree spatial resolution, derived from this L2 dataset.",
-            "title": "L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-B GOME-2, 2013-2021",
-            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpB_GOME2_SIF_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2182",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2182",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/sif-esdr/17-MEASURES-0032/MetOpB_GOME2_SIF/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/sif-esdr/17-MEASURES-0032/MetOpB_GOME2_SIF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpB_GOME2_SIF.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpB_GOME2_SIF.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2182",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2182",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/MetOpB_GOME2_SIF/comp/MetOpB_GOME2_SIF.pdf",
-                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-B GOME-2, 2013-2021: MetOpB_GOME2_SIF.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-B GOME-2, 2013-2021: MetOpB_GOME2_SIF.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/MetOpB_GOME2_SIF/comp/MetOpB_GOME2_SIF.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpB_GOME2_SIF_Fig1.png",
-                    "description": "Monthly mean solar-induced fluorescence (SIF) values (mW m-2 nm-1 sr-1) at 740 nm and gridded at 0.5-degree spatial resolution, derived from this L2 dataset.",
                     "@type": "dcat:Distribution",
+                    "description": "Monthly mean solar-induced fluorescence (SIF) values (mW m-2 nm-1 sr-1) at 740 nm and gridded at 0.5-degree spatial resolution, derived from this L2 dataset.",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpB_GOME2_SIF_Fig1.png",
+                    "mediaType": "image/png",
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
+            "graphic-preview-description": "Monthly mean solar-induced fluorescence (SIF) values (mW m-2 nm-1 sr-1) at 740 nm and gridded at 0.5-degree spatial resolution, derived from this L2 dataset.",
+            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpB_GOME2_SIF_Fig1.png",
+            "identifier": "C2840822442-ORNL_CLOUD",
+            "issued": "2024-01-18",
+            "keyword": [
+                "land surface",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "surface radiative properties",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2182",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -89.77 180.0 89.59",
+            "temporal": "2013-04-01T00:02:57Z/2021-06-07T22:56:12Z",
             "theme": [
                 "SIF-ESDR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-B GOME-2, 2013-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/h9tj-6ene",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "treatment protocol   sample collection   nucleic acid extraction   spike-in protocol   library construction   nucleic acid sequencing   genelab rnaseq data processing protocol",
-                "dissection condition   preservation method   order of preservation"
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
-            "identifier": "nasa_genelab_GLDS-273_h9tj-6ene",
             "description": "Data from the NASA Rodent Research-1 (RR-1) mission showed that gene-expression levels in mouse livers are different depending on what tissue preservation protocol is used and that slow freezing is not an effective method for preserving signals in gene-expression data. In response to these and other observations the Rapid Freeze hardware was built for use on the International Space Station. The Rapid Freeze hardware freezes mouse tissues (Glovebox freezer) and whole carcasses (Cryochiller) at rates closely mimicking those attained with immersion in liquid nitrogen. Because this hardware will be used extensively on future rodent research missions it is crucial to understand whether or not it preserves signals in gene expression data in order to maximize the value of these rare and expensive spaceflight experiments. Therefore this study was designed with three goals: 1) To evaluate the temperature profile of the Cryochiller and Glovebox freezer cartridges (Rapid Freeze hardware) over time during mock on-orbit procedures; 2) To determine the freezing profiles of tissues and carcasses using Rapid Freeze hardware at both optimal and sub-optimal temperatures (to mimic on-orbit operations) compared with those frozen in liquid nitrogen (the laboratory gold standard) or frozen at -80 C (the current standard method); 3) To identify gene expression changes in a) tissues that were frozen via the Glovebox freezer and b) tissues dissected from whole or partial carcasses that were frozen via the Cryochiller versus tissues that were frozen via control methods (liquid nitrogen or -80C slow freeze) to assess how the Rapid Freeze hardware compares with laboratory gold standard practices and our current standard methods.",
-            "title": "Transcriptional analysis of livers from mice preserved with the Rapid Freeze hardware",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-273",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-273",
+                    "mediaType": "text/html",
                     "title": "Transcriptional analysis of livers from mice preserved with the Rapid Freeze hardware"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-273_h9tj-6ene",
+            "issued": "2021-05-21",
+            "keyword": [
+                "treatment protocol   sample collection   nucleic acid extraction   spike-in protocol   library construction   nucleic acid sequencing   genelab rnaseq data processing protocol",
+                "dissection condition   preservation method   order of preservation"
+            ],
+            "landingPage": "https://data.nasa.gov/d/h9tj-6ene",
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
+            "title": "Transcriptional analysis of livers from mice preserved with the Rapid Freeze hardware"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD19A3DN.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-01-01. MODIS/Terra+Aqua BRDF Model Parameters Daily NRT L3 Global 1km SIN Grid. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MCD19A3DN.NRT.061. http://dx.doi.org/10.5067/MODIS/MCD19A3DN.NRT.061.",
-            "issued": "2023-09-10",
-            "temporal": "2023-09-10T00:00:00Z/2023-09-25T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "keyword": [
-                "surface radiative properties",
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "land surface"
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
-            "identifier": "C2407808961-LANCEMODIS",
             "description": "The MODIS Near Real Time (NRT) Combined Terra and Aqua combined Multi-Angle Implementation of Atmospheric Correction (MAIAC) Bidirectional Reflectance Distribution Function (BRDF) Model Parameters gridded Level 3 product (MCD19A3DN) produced daily at 1 kilometer (km) pixel resolutions. The MCD19A3DN product provides three coefficients (weights) of the RossThick/Li-Sparse (RTLS) BRDF model that can be used to describe the anisotropy of each pixel. The retrievals represent cloud-free and low aerosol conditions.\r\n\r\nThe Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017. A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "MODAPS at NASA/GSFC",
-            "title": "MODIS/Terra+Aqua BRDF Model Parameters Daily NRT L3 Global 1km SIN Grid",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD19A3DN.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD19A3DN.NRT.061",
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
-                    "downloadURL": "https://lance.modaps.eosdis.nasa.gov/modis/",
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
+                    "downloadURL": "https://lance.modaps.eosdis.nasa.gov/modis/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MCD19A3DN",
-                    "description": "Direct access to the download site and directory hosting the MCD19A2DN C6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MCD19A2DN C6.1 NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MCD19A3DN",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C2407808961-LANCEMODIS",
+            "issued": "2023-09-10",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD19A3DN.NRT.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-09-10T00:00:00Z/2023-09-25T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra+Aqua BRDF Model Parameters Daily NRT L3 Global 1km SIN Grid"
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
-                "grs",
-                "themis",
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
-            "identifier": "NASA-570",
             "description": "GRS, SPICE, THEMIS",
-            "title": "PDS Odyssey Data Release 32",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -853832,23 +853811,46 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-570",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "grs",
+                "themis",
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
+            "title": "PDS Odyssey Data Release 32"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M03-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m03-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "zeta cas",
@@ -853858,199 +853860,167 @@
                 "starfield",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M03-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m03-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP003 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP003 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-D-HRD-3-COHRD-V4.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The High Rate Detector (HRD) from the University of Chicago is an independent part of the CDA instrument on the Cassini Orbiter that measures the dust flux and particle mass distribution of dust particles hitting the HRD detectors. This data set includes all data from the HRD through July 28, 2008. Please refer to Srama et al. (2004) for a detailed HRD description.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-d-hrd-3-cohrd-v4.0_h9yc-susk",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "cassini-huygens",
                 "dust",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-D-HRD-3-COHRD-V4.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-d-hrd-3-cohrd-v4.0_h9yc-susk",
-            "description": "The High Rate Detector (HRD) from the University of Chicago is an independent part of the CDA instrument on the Cassini Orbiter that measures the dust flux and particle mass distribution of dust particles hitting the HRD detectors. This data set includes all data from the HRD through July 28, 2008. Please refer to Srama et al. (2004) for a detailed HRD description.",
-            "title": "CASSINI HIGH RATE DETECTOR V4.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI HIGH RATE DETECTOR V4.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-OPE-3-RDR-HALLEY-V1.0",
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
-                "giotto"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The OPE photopolarimeter was designed to measure the polarized components of the light in seven bandpasses or channels, ranging from the near ultraviolet to the near infrared. Three channels (so- called blue, green and red) were devoted to the observation of the scattering of solar light by cometary dust grains, in emission-free countinuum bands. Four other channels (so called OH, CN, CO+, C2) were devoted to the observation of light emitted by cometary gases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-ope-3-rdr-halley-v1.0_ha2c-6fq8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "giotto"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-OPE-3-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-ope-3-rdr-halley-v1.0_ha2c-6fq8",
-            "description": "The OPE photopolarimeter was designed to measure the polarized components of the light in seven bandpasses or channels, ranging from the near ultraviolet to the near infrared. Three channels (so- called blue, green and red) were devoted to the observation of the scattering of solar light by cometary dust grains, in emission-free countinuum bands. Four other channels (so called OH, CN, CO+, C2) were devoted to the observation of light emitted by cometary gases.",
-            "title": "GIOTTO OPTICAL PROBE PHASE MEASUREMENTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GIOTTO OPTICAL PROBE PHASE MEASUREMENTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SSMIS/F16/1C/07",
             "citation": "Wesley Berg. 2021-07-29. GPM_1CF16SSMIS. GPM SSMIS on F16 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SSMIS/F16/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CF16SSMIS_07.html. Digital Science Data.",
-            "issued": "2021-07-21",
-            "temporal": "2005-11-20T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-21",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "atmosphere",
-                "microwave",
-                "precipitation",
-                "spectral/engineering",
-                "atmospheric water vapor",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264132881-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nAll 1C products have a common L1C data structure, simple and generic. Each L1C swath includes scan time, latitude and longitude, scan status, quality, incidence angle, Sun glint angle, and the intercalibrated brightness temperature (Tc). One or more swaths are included in a product. The radiometer data are recalibrated to a common basis so that precipitation products derived from them are consistent. 1CSSMIS contains common calibrated brightness temperature from the SSMIS passive microwave instruments flown on the DMSP satellites. Swath S1 has 3 low frequency channels (19V 19H 22V). Swath S2 has 2 low frequency channels (37V 37H). Swath S3 has 4 high frequency channels (150H 183+/-1H 183+/-3H 183+/-7H). S4 has 2 high frequency channels (91V 91H). All the above frequencies are in GHz. Earth observations for all four swaths are taken during a 144o segment of the instrument rotation when SSMIS scans in the direction of foreward satellite motion. We define the spacecraft vector (v) at the center of this segment.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_1CF16SSMIS",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from F16 SSMIS (GPM_1CF16SSMIS)",
-            "title": "GPM SSMIS on F16 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07 (GPM_1CF16SSMIS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.F16.SSMIS.XCAL2016-V.20150101-S012641-E030835.057809.V05A.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMIS%2FF16%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMIS%2FF16%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.F16.SSMIS.XCAL2016-V.20150101-S012641-E030835.057809.V05A.PNG",
-                    "description": "Common Calibrated Brightness Temperature from F16 SSMIS (GPM_1CF16SSMIS)",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from F16 SSMIS (GPM_1CF16SSMIS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.F16.SSMIS.XCAL2016-V.20150101-S012641-E030835.057809.V05A.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CF16SSMIS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CF16SSMIS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CF16SSMIS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CF16SSMIS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CF16SSMIS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CF16SSMIS_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CF16SSMIS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CF16SSMIS.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
@@ -854060,416 +854030,460 @@
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/ssmis.php",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/ssmis.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Common Calibrated Brightness Temperature from F16 SSMIS (GPM_1CF16SSMIS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.F16.SSMIS.XCAL2016-V.20150101-S012641-E030835.057809.V05A.PNG",
+            "identifier": "C2264132881-GES_DISC",
+            "issued": "2021-07-21",
+            "keyword": [
+                "atmosphere",
+                "microwave",
+                "precipitation",
+                "spectral/engineering",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SSMIS/F16/1C/07",
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
+            "series-name": "GPM_1CF16SSMIS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-11-20T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SSMIS on F16 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07 (GPM_1CF16SSMIS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-GRE-3-RDR-GRIGG-SKJELL-V1.0",
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
-                "giotto extended mission",
-                "26p/grigg-skjellerup 1 (1922 k1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset includes open- and closed-loop data from the Giotto Radio Experiment (GRE) during the time range +/- 3 minutes around close approach. In both cases the data were received by station 63 in Madrid. These data were never formally reviewed by PDS.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-gre-3-rdr-grigg-skjell-v1.0_ha62-mz48",
+            "issued": "2018-06-26",
+            "keyword": [
+                "giotto extended mission",
+                "26p/grigg-skjellerup 1 (1922 k1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-GRE-3-RDR-GRIGG-SKJELL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-gre-3-rdr-grigg-skjell-v1.0_ha62-mz48",
-            "description": "This dataset includes open- and closed-loop data from the Giotto Radio Experiment (GRE) during the time range +/- 3 minutes around close approach. In both cases the data were received by station 63 in Madrid. These data were never formally reviewed by PDS.",
-            "title": "GIOTTO EXTENDED MISSION, RADIO SCIENCE EXPERIMENT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GIOTTO EXTENDED MISSION, RADIO SCIENCE EXPERIMENT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASB0EQO2LYJV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP/Sentinel-1 L2 Radiometer/Radar 30-Second Scene 3 km EASE-Grid Soil Moisture V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ASB0EQO2LYJV.",
-            "issued": "2015-03-31",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-19",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "microwave",
-                "radar",
-                "land surface",
-                "soils"
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
-            "identifier": "C1931663473-NSIDC_ECS",
             "description": "This Level-2 (L2) soil moisture product provides estimates of land surface conditions retrieved by both the Soil Moisture Active Passive (SMAP) radiometer during 6:00 a.m. descending and 6:00 p.m. ascending half-orbit passes and the Sentinel-1A and -1B radar. SMAP L-band brightness temperatures and Copernicus Sentinel-1 C-band backscatter coefficients are used to derive soil moisture data, which are then resampled to an Earth-fixed, cylindrical 3 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0). While the 3 km data product has undergone validation, the 1 km product has not and should be used with caution.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP/Sentinel-1 L2 Radiometer/Radar 30-Second Scene 3 km EASE-Grid Soil Moisture V003",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-198,-80,167,89&l=SMAP_Sentinel-1_L2_Active_Passive_Soil_Moisture,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASB0EQO2LYJV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASB0EQO2LYJV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL2SMAP_S.003/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL2SMAP_S.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL2SMAP_S+V003",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL2SMAP_S+V003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL2SMAP_S/versions/3/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL2SMAP_S/versions/3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-198%2C-80%2C167%2C89&l=SMAP_Sentinel-1_L2_Active_Passive_Soil_Moisture%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-198%2C-80%2C167%2C89&l=SMAP_Sentinel-1_L2_Active_Passive_Soil_Moisture%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASB0EQO2LYJV",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ASB0EQO2LYJV",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASB0EQO2LYJV",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASB0EQO2LYJV",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-198,-80,167,89&l=SMAP_Sentinel-1_L2_Active_Passive_Soil_Moisture,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C1931663473-NSIDC_ECS",
+            "issued": "2015-03-31",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave",
+                "radar",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASB0EQO2LYJV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -60.0 180.0 60.0",
+            "temporal": "2015-03-31T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP/Sentinel-1 L2 Radiometer/Radar 30-Second Scene 3 km EASE-Grid Soil Moisture V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1406-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-07T19:37:10.000 to 2016-02-07T21:43:03.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1406-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1406-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1406-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-07T19:37:10.000 to 2016-02-07T21:43:03.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1406 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1406 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/504/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-12-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Arnab Chatterjee",
                 "hasEmail": "mailto:rnb.chatterjee@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_504",
             "description": "A brief self composed research article on Amphibious Aircrafts discussing their use, origin and modern day applications along with their advantages and disadvantages over conventional land-based aircrafts.",
-            "title": "Amphibious Aircraft",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AMPHIBIOUS_AIRCRAFT.pdf",
-                    "description": "AMPHIBIOUS AIRCRAFT.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "AMPHIBIOUS AIRCRAFT.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AMPHIBIOUS_AIRCRAFT.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AMPHIBIOUS AIRCRAFT.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_504",
+            "issued": "2011-12-13",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/504/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Amphibious Aircraft"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "New, M., P.D. Jones, M. Hulme, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2011. ISLSCP II CRU05 Climate Time Series for Global Land Areas, 1986-1995. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1014",
-            "issued": "2023-10-15",
-            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
-            "keyword": [
-                "land surface",
-                "precipitation",
-                "topography",
-                "earth science",
-                "atmospheric temperature",
-                "clouds",
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
-            "identifier": "C2785289548-ORNL_CLOUD",
             "description": "This data set contains monthly climate time series data created by the Climatic Research Unit (CRU) at the University of East Anglia, U.K.,for every year covering the period 1986 to 1995. This time series is a subset of a larger CRU monthly data set that covers the period of 1901 to 1996.  The data comprise a suite of six climate elements: precipitation, mean temperature, diurnal temperature range, wet-day frequency, vapor pressure, and cloud cover. There are 13 files in this data set provided at 0.5 and 1.0 degree spatial resolutions.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II CRU05 Climate Time Series for Global Land Areas, 1986-1995",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1014_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1014",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/near-surface_met/cru_monthly_climate_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/near-surface_met/cru_monthly_climate_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/cru_monthly_climate_xdeg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/cru_monthly_climate_xdeg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1014",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1014",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/near-surface_met/cru_monthly_climate_xdeg/comp/0_cru_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/near-surface_met/cru_monthly_climate_xdeg/comp/0_cru_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/near-surface_met/cru_monthly_climate_xdeg/comp/1_cru_monthly_climate_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/near-surface_met/cru_monthly_climate_xdeg/comp/1_cru_monthly_climate_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1014_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1014_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1014",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1014",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1014/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1014/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1014_1_fit.png",
+            "identifier": "C2785289548-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "land surface",
+                "precipitation",
+                "topography",
+                "earth science",
+                "atmospheric temperature",
+                "clouds",
+                "atmosphere",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1014",
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
+            "title": "ISLSCP II CRU05 Climate Time Series for Global Land Areas, 1986-1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-SHAPE-MODELS-V1.0",
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
+            "description": "This data set contains the Peter Thomas shape models for small solar system bodies, as well as image mosaics constructed from these models. The current version of the data set contains the following: 243 Ida, 951 Gaspra, M1 Phobos, M2 Deimos, S7 Hyperion, S10 Janus, S11 Epimetheus.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-shape-models-v1.0_habw-jpek",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-SHAPE-MODELS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-shape-models-v1.0_habw-jpek",
-            "description": "This data set contains the Peter Thomas shape models for small solar system bodies, as well as image mosaics constructed from these models. The current version of the data set contains the following: 243 Ida, 951 Gaspra, M1 Phobos, M2 Deimos, S7 Hyperion, S10 Janus, S11 Epimetheus.",
-            "title": "SMALL BODY SHAPE MODELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SMALL BODY SHAPE MODELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/hac2-mmp8",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The Space Algae Experiment Verification Test completed a competitive growth selection on mutagenized microalgae in a series of batch cultures that were passaged for three growth cycles. The experiment was conducted with ground control conditions similar to those actually used in spaceflight. Cultures were limited in growth rate due to gas permeable membranes to provide oxygen and carbon dioxide exchange and a lack of agitation to mix the cells throughout the liquid media. Two strains were grown and three biological replicates were completed for each strain. Specific variables (factors) tested were: 1) The effect of UVC mutagenesis was tested by sampling the algae cultures prior to mutagenesis. 2) The sensitivity of different strains was tested by conducting the experiment with a wild-type and cell wall mutant (cw15) strain. 3) The effect of competitive growth was tested by sampling each biological replicate experiment at the end of each growth cycle. 4) The effect of live culture storage in the dark was tested by sampling each growth cycle twice. At the time of passage a sample of cells was pelleted and frozen. The cultures were then stored in the dark in a Cargo Transport Bag (CTB) to simulate storage on the ISS and return of cultures. This factor tested whether cultures could be stored alive in the dark or if samples needed to be fixed at the time of passage in order to get an accurate representation of the genetic variation in each cycle of growth. Paired-end whole genome sequencing was completed for 38 samples: 2 strains pre mutagenesis and 2 strains X 3 biological replicates X 3 growth cycles X 2 storage conditions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-265",
+                    "mediaType": "text/html",
+                    "title": "Selecting for Chlamydomonas reinhardtii fitness in the KSC Veggie Unit"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-265_hac2-mmp8",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "library construction",
                 "nucleic acid extraction",
@@ -854481,629 +854495,593 @@
                 "sample collection",
                 "nucleic acid sequencing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/hac2-mmp8",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-265_hac2-mmp8",
-            "description": "The Space Algae Experiment Verification Test completed a competitive growth selection on mutagenized microalgae in a series of batch cultures that were passaged for three growth cycles. The experiment was conducted with ground control conditions similar to those actually used in spaceflight. Cultures were limited in growth rate due to gas permeable membranes to provide oxygen and carbon dioxide exchange and a lack of agitation to mix the cells throughout the liquid media. Two strains were grown and three biological replicates were completed for each strain. Specific variables (factors) tested were: 1) The effect of UVC mutagenesis was tested by sampling the algae cultures prior to mutagenesis. 2) The sensitivity of different strains was tested by conducting the experiment with a wild-type and cell wall mutant (cw15) strain. 3) The effect of competitive growth was tested by sampling each biological replicate experiment at the end of each growth cycle. 4) The effect of live culture storage in the dark was tested by sampling each growth cycle twice. At the time of passage a sample of cells was pelleted and frozen. The cultures were then stored in the dark in a Cargo Transport Bag (CTB) to simulate storage on the ISS and return of cultures. This factor tested whether cultures could be stored alive in the dark or if samples needed to be fixed at the time of passage in order to get an accurate representation of the genetic variation in each cycle of growth. Paired-end whole genome sequencing was completed for 38 samples: 2 strains pre mutagenesis and 2 strains X 3 biological replicates X 3 growth cycles X 2 storage conditions.",
-            "title": "Selecting for Chlamydomonas reinhardtii fitness in the KSC Veggie Unit",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-265",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Selecting for Chlamydomonas reinhardtii fitness in the KSC Veggie Unit"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Selecting for Chlamydomonas reinhardtii fitness in the KSC Veggie Unit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Huffman, G.J., D.T. Bolvin,  R.F. Adler, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2011. ISLSCP II Global Precipitation Climatology Project Version 2, Monthly Precipitation. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1003",
-            "issued": "2023-10-15",
-            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
-            "keyword": [
-                "earth science",
-                "precipitation",
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
-            "identifier": "C2785267282-ORNL_CLOUD",
             "description": "The Global Precipitation Climatology Project (GPCP) Version 2 data set includes global, monthly precipitation rates and associated random errors (RMSE), and a monthly precipitation climatology derived as an average from all GPCP data sets from January 1979 to December 1999. The data are derived from measured gauge data and merged with satellite estimates of rainfall. This is a portion of the version 2 GPCP data and covers the ISLSCP II period from 1986 to 1995. There are six data files included with this data set:  the original precipitation rates, errors and climatology at 2.5 degrees spatial resolution, and the same data  re-gridded to a 1 degree spatial resolution by the ISLSCP II staff.and merged with satellite estimates of rainfall. This is a portion of the version 2 GPCP data sets and covers the ISLSCP II period from 1986 to 1995. There are six data files included with this data set:  the original precipitation rates, errors and climatology at 2.5 degrees spatial resolution, and the same data  re-gridded to a 1 degree spatial resolution by the ISLSCP II staff.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Global Precipitation Climatology Project Version 2, Monthly Precipitation",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1003_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/hydrology_soils/gpcp_precip_monthly_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/hydrology_soils/gpcp_precip_monthly_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/gpcp_precip_monthly_xdeg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/gpcp_precip_monthly_xdeg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1003",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/gpcp_precip_monthly_xdeg/comp/0_gpcp_precip_month_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/gpcp_precip_monthly_xdeg/comp/0_gpcp_precip_month_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/gpcp_precip_monthly_xdeg/comp/1_gpcp_precip_monthly_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/gpcp_precip_monthly_xdeg/comp/1_gpcp_precip_monthly_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1003_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1003_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1003",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1003",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1003/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1003/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1003_1_fit.png",
+            "identifier": "C2785267282-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1003",
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
+            "title": "ISLSCP II Global Precipitation Climatology Project Version 2, Monthly Precipitation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ELE-PAR-96.0SEC",
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
+            "description": "THIS DATA SET CONTAINS ELECTRON PARAMETERS IN THE PLS ENERGY RANGE (10-5950 EV) AT SATURN DURING THE VOYAGER 1 ENCOUNTER. PARAMETERS ARE CALCULATED IN SEVERAL WAYS. TOTAL MOMENT DENSITY AND TEMPERATURE ARE GIVEN. EACH ELECTRON SPECTRUM IS ALSO FIT WITH A THERMAL COMPONENT AND 1-3 HOT COMPONENTS DEPENDING ON HOW MANY MAXWELLIANS ARE NEEDED TO FIT THE ENTIRE DISTRIBUTION. THE MOMENT DENSITY AND TEMPERATURE OF THE HOT COMPONENT IS CALCULATED AFTER THE THERMAL COMPONENT IS SUBTRACTED FROM THE SPECTRUM. THE CHI-SQUARE VALUE FOR EACH FIT IS GIVEN. THE SPACECRAFT CHARGE IS NOT TAKEN INTO ACCOUNT, AND MAY RESULT IN FACTOR OF 2-3 ERRORS IN THE THERMAL ELECTRON DENSITY. DATA IS UNRELIABLE INSIDE 6 RS AND IN THE OCCULTATION REGIONS. A COMPLETE DESCRIPTION OF THIS DATA SET IS IN SITTLER ET AL. (1983). DATA FORMAT: THE DATA SET IS IN ASC FORMAT AND CAN BE READ USING THE FOLLOWING FORTRAN STATEMENT:\\n",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ele-par-96.0sec_hacx-652d",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ELE-PAR-96.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ele-par-96.0sec_hacx-652d",
-            "description": "THIS DATA SET CONTAINS ELECTRON PARAMETERS IN THE PLS ENERGY RANGE (10-5950 EV) AT SATURN DURING THE VOYAGER 1 ENCOUNTER. PARAMETERS ARE CALCULATED IN SEVERAL WAYS. TOTAL MOMENT DENSITY AND TEMPERATURE ARE GIVEN. EACH ELECTRON SPECTRUM IS ALSO FIT WITH A THERMAL COMPONENT AND 1-3 HOT COMPONENTS DEPENDING ON HOW MANY MAXWELLIANS ARE NEEDED TO FIT THE ENTIRE DISTRIBUTION. THE MOMENT DENSITY AND TEMPERATURE OF THE HOT COMPONENT IS CALCULATED AFTER THE THERMAL COMPONENT IS SUBTRACTED FROM THE SPECTRUM. THE CHI-SQUARE VALUE FOR EACH FIT IS GIVEN. THE SPACECRAFT CHARGE IS NOT TAKEN INTO ACCOUNT, AND MAY RESULT IN FACTOR OF 2-3 ERRORS IN THE THERMAL ELECTRON DENSITY. DATA IS UNRELIABLE INSIDE 6 RS AND IN THE OCCULTATION REGIONS. A COMPLETE DESCRIPTION OF THIS DATA SET IS IN SITTLER ET AL. (1983). DATA FORMAT: THE DATA SET IS IN ASC FORMAT AND CAN BE READ USING THE FOLLOWING FORTRAN STATEMENT:\\n",
-            "title": "VOYAGER 1 SATURN PLASMA DERIVED ELECTRON PARAMETERS 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 SATURN PLASMA DERIVED ELECTRON PARAMETERS 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1754",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Guevara, M., and R. Vargas. 2020. Soil Organic Carbon Estimates and Uncertainty at 1-m Depth across Mexico, 1999-2009. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1754",
-            "issued": "2020-03-26",
-            "temporal": "1999-01-01T00:00:00Z/2009-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "soils",
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
-            "identifier": "C2389083479-ORNL_CLOUD",
             "description": "This dataset provides an estimate of soil organic carbon (SOC) in the top one meter of soil across Mexico at a 90-m resolution for the period 1999-2009. Carbon estimates (kg/m2) are based on a field data collection of 2852 soil profiles by the National Institute for Statistics and Geography (INEGI). The profile data were used for the development of a predictive model along with a set of environmental covariates that were harmonized in a regular grid of 90x90 m2 across all Mexican states. The base of reference was the digital elevation model (DEM) of the INEGI at 90-m spatial resolution. A model ensemble of regression trees with a recursive elimination of variables explained 54% of the total variability using a cross-validation technique of independent samples. The error associated with the predictive model estimates of SOC is provided. A summary of the total estimated SOC per state, statistical description of the modeled SOC data, and the number of pixels modeled for each state are also provided.",
-            "graphic-preview-description": "(a) Digital map of soil organic carbon (kg m2) at 1m depth and 90m spatial resolution, the black line represents country borders. The black and blue colored areas are urban areas and water bodies. (b) Zoom in, to an area in northern Mexico to visualize an example of the level of detail achieved by mapping across 90m grids. (c) Percentage of errors in the predictive model (uncertainty map). (d) Zoom in to the error map across an area in northern\nMexico to visualize the prediction error with higher spatial detail.",
-            "title": "Soil Organic Carbon Estimates and Uncertainty at 1-m Depth across Mexico, 1999-2009",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1754",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1754",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_SOC_Mexico/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_SOC_Mexico/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1754",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1754",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_SOC_Mexico/comp/CMS_SOC_Mexico.pdf",
-                    "description": "Soil Organic Carbon Estimates for Mexico at 1-m Depth and 90-m Resolution,1999-2009: CMS_SOC_Mexico.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Soil Organic Carbon Estimates for Mexico at 1-m Depth and 90-m Resolution,1999-2009: CMS_SOC_Mexico.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_SOC_Mexico/comp/CMS_SOC_Mexico.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_Fig1.png",
-                    "description": "(a) Digital map of soil organic carbon (kg m2) at 1m depth and 90m spatial resolution, the black line represents country borders. The black and blue colored areas are urban areas and water bodies. (b) Zoom in, to an area in northern Mexico to visualize an example of the level of detail achieved by mapping across 90m grids. (c) Percentage of errors in the predictive model (uncertainty map). (d) Zoom in to the error map across an area in northern\nMexico to visualize the prediction error with higher spatial detail.",
                     "@type": "dcat:Distribution",
+                    "description": "(a) Digital map of soil organic carbon (kg m2) at 1m depth and 90m spatial resolution, the black line represents country borders. The black and blue colored areas are urban areas and water bodies. (b) Zoom in, to an area in northern Mexico to visualize an example of the level of detail achieved by mapping across 90m grids. (c) Percentage of errors in the predictive model (uncertainty map). (d) Zoom in to the error map across an area in northern\nMexico to visualize the prediction error with higher spatial detail.",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "(a) Digital map of soil organic carbon (kg m2) at 1m depth and 90m spatial resolution, the black line represents country borders. The black and blue colored areas are urban areas and water bodies. (b) Zoom in, to an area in northern Mexico to visualize an example of the level of detail achieved by mapping across 90m grids. (c) Percentage of errors in the predictive model (uncertainty map). (d) Zoom in to the error map across an area in northern\nMexico to visualize the prediction error with higher spatial detail.",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_Fig1.png",
+            "identifier": "C2389083479-ORNL_CLOUD",
+            "issued": "2020-03-26",
+            "keyword": [
+                "soils",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1754",
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
             "spatial": "-117.12 14.53 -86.74 32.72",
+            "temporal": "1999-01-01T00:00:00Z/2009-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Organic Carbon Estimates and Uncertainty at 1-m Depth across Mexico, 1999-2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SEAGRASS_MAPPING_FLORIDA/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SEAGRASS_MAPPING_FLORIDA/DATA001.",
-            "issued": "2010-05-17",
-            "temporal": "2010-05-17T14:37:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean optics",
-                "salinity/density",
-                "ocean temperature",
-                "oceans",
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
-            "identifier": "C1633360643-OB_DAAC",
             "description": "Water quality measurements taken near the Big Bend Seagrasses Aquatic Preserve in Florida.",
-            "title": "Water quality measurements near the Big Bend Seagrasses Aquatic Preserve, Florida",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSEAGRASS_MAPPING_FLORIDA%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSEAGRASS_MAPPING_FLORIDA%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Seagrass_Mapping_Florida/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Seagrass_Mapping_Florida/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360643-OB_DAAC",
+            "issued": "2010-05-17",
+            "keyword": [
+                "ocean chemistry",
+                "ocean optics",
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SEAGRASS_MAPPING_FLORIDA/DATA001",
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
+            "temporal": "2010-05-17T14:37:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Water quality measurements near the Big Bend Seagrasses Aquatic Preserve, Florida"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO1BMAPRAD.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Mike Smyth, Tom Logan, William Johnson. 2019-03-27. ECO1BMAPRAD.001.  ECOSTRESS Resampled Radiance Daily L1B Global 70 m V001. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO1BMAPRAD.001. https://doi.org/10.5067/ECOSTRESS/ECO1BMAPRAD.001. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2019-03-27",
-            "temporal": "2018-07-09T00:00:00Z/2024-09-02T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
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
-            "identifier": "C1545228916-LPDAAC_ECS",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO1BMAPRAD Version 1 data product combines the at-sensor calibrated radiance values retrieved for the ECO1BRAD (https://doi.org/10.5067/ECOSTRESS/ECO1BRAD.001) data product and the geolocation information provided in the ECO1BGEO (https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001) data product to produce a geotagged, resampled radiance product.  The ECO1BMAPRAD data product is produced as a map registered product that is in a rotated geographic projection with a spatial resolution of 70 m. The ECO1BMAPRAD data product accounts for the overlap and variable pixel size in the ECO1BRAD data product.\r\n\r\nThe ECO1BMAPRAD Version 1 data product contains data layers including the radiance values for the five thermal infrared (TIR) bands, digital number (DN) values for the shortwave infrared (SWIR) band, associated data quality indicators, latitude and longitude values, solar and view geometry information, and surface height.\r\n\r\nThe ECO1BMAPRAD Version 1 data product contains data layers including the radiance values for the five thermal infrared (TIR) bands, digital number (DN) values for the shortwave infrared (SWIR) band, associated data quality indicators, latitude and longitude values, solar and view geometry information, and surface height.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Resampled data: The data has been resampled, so users interested in working with data closest to that acquired by the instrument may want to work with the swath products. \r\n*Missing scan data: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see section 3.3.2 of the User Guide.\r\n*Cold bias: ECOSTRESS Level-1 Radiance data shows high correlation with in-situ ground measurements (R2 = 0.99 in all bands). Currently, ECOSTRESS has a cold bias of approximately 0.7 Kelvin (K), which will be corrected through calibration in future data releases.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmwar",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "ECO1BMAPRAD.001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "title": "ECOSTRESS Resampled Radiance Daily L1B Global 70m V001",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.12.31/ECOSTRESS_L1B_MAP_RAD_08422_001_20191231T002428_0601_01.1.jpg?_ga=2.210053781.1882281295.1577729098-2066674673.1574795892",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO1BMAPRAD Version 1 data product combines the at-sensor calibrated radiance values retrieved for the ECO1BRAD (https://doi.org/10.5067/ECOSTRESS/ECO1BRAD.001) data product and the geolocation information provided in the ECO1BGEO (https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001) data product to produce a geotagged, resampled radiance product.  The ECO1BMAPRAD data product is produced as a map registered product that is in a rotated geographic projection with a spatial resolution of 70 m. The ECO1BMAPRAD data product accounts for the overlap and variable pixel size in the ECO1BRAD data product.\r\n\r\nThe ECO1BMAPRAD Version 1 data product contains data layers including the radiance values for the five thermal infrared (TIR) bands, digital number (DN) values for the shortwave infrared (SWIR) band, associated data quality indicators, latitude and longitude values, solar and view geometry information, and surface height.\r\n\r\nThe ECO1BMAPRAD Version 1 data product contains data layers including the radiance values for the five thermal infrared (TIR) bands, digital number (DN) values for the shortwave infrared (SWIR) band, associated data quality indicators, latitude and longitude values, solar and view geometry information, and surface height.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Resampled data: The data has been resampled, so users interested in working with data closest to that acquired by the instrument may want to work with the swath products. \r\n*Missing scan data: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see section 3.3.2 of the User Guide.\r\n*Cold bias: ECOSTRESS Level-1 Radiance data shows high correlation with in-situ ground measurements (R2 = 0.99 in all bands). Currently, ECOSTRESS has a cold bias of approximately 0.7 Kelvin (K), which will be corrected through calibration in future data releases.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmwar",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO1BMAPRAD.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO1BMAPRAD.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1545228916-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1545228916-LPDAAC_ECS",
+                    "mediaType": "application/xhdf5",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO1BMAPRAD.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO1BMAPRAD.001/",
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
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO1BMAPRAD.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO1BMAPRAD.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1323/ECO1B_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1323/ECO1B_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
-                    "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
-                    "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
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
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.12.31/ECOSTRESS_L1B_MAP_RAD_08422_001_20191231T002428_0601_01.1.jpg?_ga=2.210053781.1882281295.1577729098-2066674673.1574795892",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.12.31/ECOSTRESS_L1B_MAP_RAD_08422_001_20191231T002428_0601_01.1.jpg?_ga=2.210053781.1882281295.1577729098-2066674673.1574795892",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOD/ECOSTRESS/ECO1BMAPRAD.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOD/ECOSTRESS/ECO1BMAPRAD.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.12.31/ECOSTRESS_L1B_MAP_RAD_08422_001_20191231T002428_0601_01.1.jpg?_ga=2.210053781.1882281295.1577729098-2066674673.1574795892",
+            "identifier": "C1545228916-LPDAAC_ECS",
+            "issued": "2019-03-27",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO1BMAPRAD.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-08-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "ECO1BMAPRAD.001",
             "spatial": "-180.0 -54.0 180.0 54.0",
+            "temporal": "2018-07-09T00:00:00Z/2024-09-02T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Resampled Radiance Daily L1B Global 70m V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GH19L-2PN02",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Naval Oceanographic Office. 2014-10-27. GHRSST Level 2P Regional 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 satellite produced by NAVO. Version 1. N-19 AVHRR LAC L2P swath SST data set. Stennis Space Center, MS, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Naval Oceanographic Office. https://doi.org/10.5067/GH19L-2PN02. Naval Oceanographic Office, Naval Oceanographic Office, 2014-10-27, GHRSST Level 2P Regional 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 satellite produced by NAVO, none.",
-            "issued": "2013-09-25",
-            "temporal": "2013-05-05T15:07:20Z/2021-01-16T23:59:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "ocean temperature",
-                "oceans",
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
-            "identifier": "C2036877716-POCLOUD",
-            "description": "A regional Group for High Resolution Sea Surface Temperature (GHRSST) Level 2P dataset based on multi-channel sea surface temperature (SST) retrievals generated in real-time from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 platform (launched 6 Feb 2009) produced and used operationally in  oceanographic analyses and forecasts by the US Naval Oceanographic Office (NAVO). The AVHRR is a space-borne scanning sensor on the National Oceanic and Atmospheric Administration (NOAA) family of Polar Orbiting Environmental Satellites (POES) having a operational legacy that traces back to the Television Infrared Observation Satellite-N (TIROS-N) launched in 1978. AVHRR instruments measure the radiance of the Earth in 5 (or 6) relatively wide spectral bands. The first two are centered around the red (0.6 micrometer) and near-infrared (0.9 micrometer) regions, the third one is located around 3.5 micrometer, and the last two sample the emitted thermal radiation, around 11 and 12 micrometers, respectively. The legacy 5 band instrument is known as AVHRR/2 while the more recent version, the AVHRR/3 (first carried on the NOAA-15 platform),  acquires data in a 6th channel located at 1.6 micrometer. Typically the 11 and 12 micron channels are used to derive SST sometimes in combination with the 3.5 micron channel. The NOAA platforms are sun synchronous generally viewing the same earth location twice a day (latitude dependent) due to the relatively large AVHRR swath of approximately 2400 km. The highest ground resolution that can be obtained from the current AVHRR instruments is 1.1 km at nadir. AVHRR data are acquired in three formats: High Resolution Picture Transmission (HRPT), Local Area Coverage (LAC), and Global Area Coverage (GAC).  HRPT data are full resolution image data transmitted to a ground stations as they are collected. LAC are also full resolution data, but the acquisition is prescheduled and recorded with an on-board tape recorder for subsequent transmission during a station overpass. GAC data provide daily subsampled global coverage recorded on tape recorders and then transmitted to a ground station. This particular dataset is derived from LAC data. Further binning and averaging of the 1.1 km  LAC pixels results in a final dataset resolution of 2.2 km. The coverage of the LAC data can vary but generally contains scenes over the oceans adjacent to Australia and the North Indian Ocean.",
-            "release-place": "Stennis Space Center, MS, USA",
-            "series-name": "GHRSST Level 2P Regional 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 satellite produced by NAVO",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Naval Oceanographic Office",
-            "title": "GHRSST Level 2P Regional 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 satellite produced by NAVO",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR19_L-NAVO-L2P-v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A regional Group for High Resolution Sea Surface Temperature (GHRSST) Level 2P dataset based on multi-channel sea surface temperature (SST) retrievals generated in real-time from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 platform (launched 6 Feb 2009) produced and used operationally in  oceanographic analyses and forecasts by the US Naval Oceanographic Office (NAVO). The AVHRR is a space-borne scanning sensor on the National Oceanic and Atmospheric Administration (NOAA) family of Polar Orbiting Environmental Satellites (POES) having a operational legacy that traces back to the Television Infrared Observation Satellite-N (TIROS-N) launched in 1978. AVHRR instruments measure the radiance of the Earth in 5 (or 6) relatively wide spectral bands. The first two are centered around the red (0.6 micrometer) and near-infrared (0.9 micrometer) regions, the third one is located around 3.5 micrometer, and the last two sample the emitted thermal radiation, around 11 and 12 micrometers, respectively. The legacy 5 band instrument is known as AVHRR/2 while the more recent version, the AVHRR/3 (first carried on the NOAA-15 platform),  acquires data in a 6th channel located at 1.6 micrometer. Typically the 11 and 12 micron channels are used to derive SST sometimes in combination with the 3.5 micron channel. The NOAA platforms are sun synchronous generally viewing the same earth location twice a day (latitude dependent) due to the relatively large AVHRR swath of approximately 2400 km. The highest ground resolution that can be obtained from the current AVHRR instruments is 1.1 km at nadir. AVHRR data are acquired in three formats: High Resolution Picture Transmission (HRPT), Local Area Coverage (LAC), and Global Area Coverage (GAC).  HRPT data are full resolution image data transmitted to a ground stations as they are collected. LAC are also full resolution data, but the acquisition is prescheduled and recorded with an on-board tape recorder for subsequent transmission during a station overpass. GAC data provide daily subsampled global coverage recorded on tape recorders and then transmitted to a ground station. This particular dataset is derived from LAC data. Further binning and averaging of the 1.1 km  LAC pixels results in a final dataset resolution of 2.2 km. The coverage of the LAC data can vary but generally contains scenes over the oceans adjacent to Australia and the North Indian Ocean.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGH19L-2PN02",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGH19L-2PN02",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/sea_surface_temperature/avhrr/navoceano_hrpt_lac/doc/avhrr_hrpt_lac_13.html",
-                    "description": "Product documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Product documentation",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/sea_surface_temperature/avhrr/navoceano_hrpt_lac/doc/avhrr_hrpt_lac_13.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR19_L-NAVO-L2P-v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR19_L-NAVO-L2P-v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877716-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877716-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877716-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877716-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
-                    "description": "Documentation on the GDS version 2 format specification",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation on the GDS version 2 format specification",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR19_L-NAVO-L2P-v1.0.jpg",
+            "identifier": "C2036877716-POCLOUD",
+            "issued": "2013-09-25",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GH19L-2PN02",
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
+            "release-place": "Stennis Space Center, MS, USA",
+            "series-name": "GHRSST Level 2P Regional 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 satellite produced by NAVO",
             "spatial": "-180.0 -70.0 180.0 80.0",
+            "temporal": "2013-05-05T15:07:20Z/2021-01-16T23:59:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 2P Regional 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 satellite produced by NAVO"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2248663206-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, AnnmarieEldering. 2019-07-01. OCO2_Att. Version 11r. OCO-2 Level 0 spacecraft attitude data, Retrospective Processing V11r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_Att_11r.html. Digital Science Data.",
-            "issued": "2019-06-27",
-            "temporal": "2014-07-02T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-17",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "platform characteristics"
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
-            "identifier": "C2248663206-GES_DISC",
-            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA missiondesigned to collect space-based measurements of atmospheric carbon dioxidewith the precision, resolution, and coverage needed to characterize theprocesses controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements ofreflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and inmolecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectralelements.This product contains pointing angles of the spacecraft for each orbit.It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_Att",
             "creator": "OCO-2 Science Team/Michael Gunson, AnnmarieEldering",
-            "title": "OCO-2 Level 0 spacecraft attitude data, Retrospective Processing V11r (OCO2_Att) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_Att_8r.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA missiondesigned to collect space-based measurements of atmospheric carbon dioxidewith the precision, resolution, and coverage needed to characterize theprocesses controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements ofreflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and inmolecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectralelements.This product contains pointing angles of the spacecraft for each orbit.It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -855112,111 +855090,135 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Att_11r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Att_11r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_Att",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_Att",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Att.11r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Att.11r/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Att.11r/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Att.11r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_Attde.V5.pdf",
-                    "description": "Software interface specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software interface specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_Attde.V5.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_Att_8r.jpeg",
+            "identifier": "C2248663206-GES_DISC",
+            "issued": "2019-06-27",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "platform characteristics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2248663206-GES_DISC.html",
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
+            "series-name": "OCO2_Att",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-07-02T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 0 spacecraft attitude data, Retrospective Processing V11r (OCO2_Att) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-RDR-3-52COLOR-V2.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains 52-color IR data of asteroids, taken using a double circularly variable filter. The short wavelength portion of the CVF covered the octave from 0.8 to 1.6 microns with 3 percent resolution, while the long wavelength portion covered 1.5 to 2.6 microns with 5 percent resolution. Most of the data are unpublished other than in this PDS data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-rdr-3-52color-v2.1_hakw-nr4s",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "1056 azalea",
                 "68 leto",
@@ -855340,352 +855342,328 @@
                 "10 hygiea",
                 "18 melpomene"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-RDR-3-52COLOR-V2.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-rdr-3-52color-v2.1_hakw-nr4s",
-            "description": "This data set contains 52-color IR data of asteroids, taken using a double circularly variable filter. The short wavelength portion of the CVF covered the octave from 0.8 to 1.6 microns with 3 percent resolution, while the long wavelength portion covered 1.5 to 2.6 microns with 5 percent resolution. Most of the data are unpublished other than in this PDS data set.",
-            "title": "52-COLOR ASTEROID SURVEY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "52-COLOR ASTEROID SURVEY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67PCHURYUMOV-M30-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67pchuryumov-m30-v2.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67PCHURYUMOV-M30-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67pchuryumov-m30-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP030 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP030 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/DNC2SNXE6HJB",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VIIRS/JPSS1 Snow Cover Daily L3 Global 0.05Deg CMG V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/DNC2SNXE6HJB.",
-            "issued": "2018-01-05",
-            "temporal": "2018-01-05T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds",
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
-            "identifier": "C2317027844-NSIDC_ECS",
             "description": "This global Level-3 data set provides the percentage of snow-covered land and cloud-covered land observed daily, within 0.05\u00b0 (approx. 5 km at the equator) MODIS/VIIRS Climate Modeling Grid (CMG) cells. Percentages are computed from snow cover observations in the 'VIIRS/JPSS1 Snow Cover Daily L3 Global 375m SIN Grid' data set (DOI:10.5067/UAJGR7WVWDDI).",
-            "title": "VIIRS/JPSS1 Snow Cover Daily L3 Global 0.05Deg CMG V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDNC2SNXE6HJB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDNC2SNXE6HJB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VJ110C1.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VJ110C1.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VJ110C1+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VJ110C1+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/VJ110C1/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/VJ110C1/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DNC2SNXE6HJB",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/DNC2SNXE6HJB",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DNC2SNXE6HJB",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/DNC2SNXE6HJB",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2317027844-NSIDC_ECS",
+            "issued": "2018-01-05",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds",
+                "cryosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/DNC2SNXE6HJB",
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
+            "temporal": "2018-01-05T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Snow Cover Daily L3 Global 0.05Deg CMG V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/951/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2016-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chetan Kulkarni",
                 "hasEmail": "mailto:chetan.s.kulkarni@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_951",
             "description": "Studying and analyzing the ageing mechanisms of electronic components avionics in systems such as the GPS and INAV are of critical importance. In DC-DC power converter systems electrolytic capacitors and MOSFET\u2019s have higher failure rates among the components. Degradation in the capacitors under varying operating conditions leads to high ripples output voltages and currents affecting downstream components leading to cascading faults. For example, in avionics systems where the power supply drives a GPS unit, ripple currents can cause glitches in the GPS position and velocity output, and this may cause errors in the Inertial Navigation (INAV) system, causing the aircraft to fly off course The work in this paper proposes a detail experimental and systematic study on analyzing the degradation phenomenon is electrolytic capacitors under high stress operating conditions. The output degradation is typically measured by an increase in ESR (Equivalent Series Resistance) and decrease in the capacitance value. We present the details of our accelerated ageing methodology along with analysis and comparison of the results.",
-            "title": "DIAGNOSTIC/PROGNOSTIC EXPERIMENTS FOR CAPACITOR DEGRADATION AND HEALTH MONITORING IN DC-DC CONVERTERS",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/SMASIS2010-3862_Vanderbilt_University.pdf",
-                    "description": "KulkarniEtAl_SMASIS_2010",
                     "@type": "dcat:Distribution",
+                    "description": "KulkarniEtAl_SMASIS_2010",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/SMASIS2010-3862_Vanderbilt_University.pdf",
+                    "mediaType": "application/pdf",
                     "title": "SMASIS2010-3862_Vanderbilt_University.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_951",
+            "issued": "2016-02-23",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/951/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "DIAGNOSTIC/PROGNOSTIC EXPERIMENTS FOR CAPACITOR DEGRADATION AND HEALTH MONITORING IN DC-DC CONVERTERS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_NPT_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_NPT_001.",
-            "issued": "1976-01-01",
-            "temporal": "1982-01-01T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "earth science",
-                "solid earth",
-                "tectonics",
-                "gravity/gravitational field",
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
-            "identifier": "C1602535597-CDDIS",
             "description": "This dataset consists of ground-based Satellite Laser Ranging observation data summary (normal points, monthly files) from the NASA Crustal Dynamics Data Information System (CDDIS). SLR provides unambiguous range measurements to mm precision that can be aggregated over the global network to provide very accurate satellite orbits, time histories of station position and motion, and many other geophysical parameters. SLR operates in the optical region and is the only space geodetic technique that measures unambiguous range directly. Analysis of SLR data contributes to the terrestrial reference frame, modeling of the spatial and temporal variations of the Earth's gravitational field, and monitoring of millimeter-level variations in the location of the center of mass of the total Earth system (solid Earth-atmosphere-oceans). In addition, SLR provides precise orbit determination for spaceborne radar altimeter missions. It provides a means for sub-nanosecond global time transfer, and a basis for special tests of the Theory of General Relativity. Analysis Centers (ACs) of the International Laser Ranging Service (ILRS) retrieve SLR data on regular schedules to produce precise station positions and velocities for stations in the ILRS network. The monthly SLR normal point observation summary files report on one month of SLR data from a global network of stations ranging to satellites equipped with retroreflectors. Data are available in ILRS data format (older data sets) and/or the Consolidated Ranging Data (CRD) format. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/SLR/Normal_point_data.html.",
-            "title": "Ground-Based Satellite Laser Ranging (SLR) Observation Data Summary (normal points, monthly files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSLR%2FSLR_DATA_MONTHLYSUM_NPT_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSLR%2FSLR_DATA_MONTHLYSUM_NPT_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/slr/data",
-                    "description": "URL for retrieval of SLR derived products through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of SLR derived products through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/slr/data",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/Normal_point_data.html",
-                    "description": "URL for more information about SLR data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about SLR data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/Normal_point_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_NPT_001",
-                    "description": "URL for more information about SLR data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about SLR data",
+                    "downloadURL": "http://dx.doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_NPT_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1602535597-CDDIS",
+            "issued": "1976-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "tectonics",
+                "gravity/gravitational field",
+                "geodetics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_NPT_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1982-01-01T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Satellite Laser Ranging (SLR) Observation Data Summary (normal points, monthly files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567768-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "surface radiative properties",
-                "topography"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EROS CENTER",
                 "hasEmail": "mailto:lta@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220567768-USGS_LTA",
             "description": "Global Land Survey 1975 images were acquired from 1972 to 1987 by Landsat 1-5 MSS.  Landsat 4-5 data were used to fill gaps in the Landsat 1-3 data.\n \nThe U.S. Geological Survey (USGS) and the National Aeronautics and Space Administration (NASA) collaborated on the creation of the global land datasets using Landsat data from 1972 through 2008. Each of these global datasets was created from the primary Landsat sensor in use at the time: the Multispectral Scanner (MSS) in the 1970s, the Thematic Mapper (TM) in 1990, the Enhanced Thematic Mapper Plus (ETM+) in 2000, and a combination of TM and ETM+, as well as EO-1 ALI data, in 2005.",
-            "title": "Global Land Survey 1975",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n         \n         Typically, all data available from USGS/EROS are downloadable at no cost  to the user.  There are some cases when a service fee is required to  convert the analog film record to a digital file. This non-refundable fee  is $30 per scene/frame.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n         \n         Typically, all data available from USGS/EROS are downloadable at no cost  to the user.  There are some cases when a service fee is required to  convert the analog film record to a digital file. This non-refundable fee  is $30 per scene/frame.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://landsat.usgs.gov/band_designations_landsat_satellites.php",
-                    "description": "\n         Band designations for the Landsat satellites.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Band designations for the Landsat satellites.\n      ",
+                    "downloadURL": "http://landsat.usgs.gov/band_designations_landsat_satellites.php",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 }
             ],
+            "identifier": "C1220567768-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface radiative properties",
+                "topography"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567768-USGS_LTA.html",
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
+            "title": "Global Land Survey 1975"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://epic.gsfc.nasa.gov/about.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-06-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://epic.gsfc.nasa.gov/"
-            ],
-            "keyword": [
-                "imagery",
-                "earth science",
-                "api",
-                "space",
-                "imaging"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alexander Marshak",
                 "hasEmail": "mailto:alexander.marshak-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "API-106",
             "description": "This is an API for the Earth Polychromatic Imaging Camera.",
-            "title": "EPIC Daily Blue Marble API",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -855693,20 +855671,56 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "API-106",
+            "issued": "2015-06-13",
+            "keyword": [
+                "imagery",
+                "earth science",
+                "api",
+                "space",
+                "imaging"
+            ],
+            "landingPage": "http://epic.gsfc.nasa.gov/about.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://epic.gsfc.nasa.gov/"
+            ],
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPIC Daily Blue Marble API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/hav7-nc8e",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "These investigations studied the fundamentals of how plants perceive gravity and develop in microgravity. It informs how gene regulation is altered by spaceflight conditions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-121",
+                    "mediaType": "text/html",
+                    "title": "Biological Research in Canisters-16 (BRIC-16): Investigations of the plant cytoskeleton in microgravity with gene profiling and cytochemistry"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-121_hav7-nc8e",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample collection",
                 "rna extraction",
@@ -855716,211 +855730,174 @@
                 "data collection",
                 "labeling"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/hav7-nc8e",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-121_hav7-nc8e",
-            "description": "These investigations studied the fundamentals of how plants perceive gravity and develop in microgravity. It informs how gene regulation is altered by spaceflight conditions.",
-            "title": "Biological Research in Canisters-16 (BRIC-16): Investigations of the plant cytoskeleton in microgravity with gene profiling and cytochemistry",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-121",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Biological Research in Canisters-16 (BRIC-16): Investigations of the plant cytoskeleton in microgravity with gene profiling and cytochemistry"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Biological Research in Canisters-16 (BRIC-16): Investigations of the plant cytoskeleton in microgravity with gene profiling and cytochemistry"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD11C3.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Zhengming Wan, Simon Hook, Glynn Hulley. 2021-02-04. MODIS/Aqua Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MYD11C3.061. https://doi.org/10.5067/MODIS/MYD11C3.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-04",
-            "temporal": "2002-07-01T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-04",
-            "keyword": [
-                "earth science",
-                "surface thermal properties",
-                "ngda",
-                "surface radiative properties",
-                "land surface",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Zhengming Wan",
                 "hasEmail": "mailto:sadashiva.devadiga-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2565794044-LPCLOUD",
-            "description": "The MYD11C3 Version 6.1 product provides monthly Land Surface Temperature and Emissivity (LST&E) values in a 0.05  degree (5,600 meters at the equator) latitude/longitude Climate Modeling Grid (CMG). A CMG granule is a geographic grid with 7,200 columns and 3,600 rows representing the entire globe. The LST&E values in the MYD11C3 product are derived by compositing and averaging the values from the corresponding month of MYD11C1 (https://doi.org/10.5067/MODIS/MYD11C1.061) daily files. Each MYD11C3 product consists of the following layers for daytime and nighttime observations: LSTs, quality control assessments, observation times, view zenith angles, and number of clear-sky observations along with percentage of land in the grid and emissivities from bands 20, 22, 23, 29, 31, and 32. \n\nValidation at stage 2 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for all MODIS Land Surface Temperature and Emissivity products. Further details regarding MODIS land product validation for the MYD11 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD11).\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Zhengming Wan, Simon Hook, Glynn Hulley",
-            "title": "MODIS/Aqua Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2618671574-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MYD11C3 Version 6.1 product provides monthly Land Surface Temperature and Emissivity (LST&E) values in a 0.05  degree (5,600 meters at the equator) latitude/longitude Climate Modeling Grid (CMG). A CMG granule is a geographic grid with 7,200 columns and 3,600 rows representing the entire globe. The LST&E values in the MYD11C3 product are derived by compositing and averaging the values from the corresponding month of MYD11C1 (https://doi.org/10.5067/MODIS/MYD11C1.061) daily files. Each MYD11C3 product consists of the following layers for daytime and nighttime observations: LSTs, quality control assessments, observation times, view zenith angles, and number of clear-sky observations along with percentage of land in the grid and emissivities from bands 20, 22, 23, 29, 31, and 32. \n\nValidation at stage 2 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for all MODIS Land Surface Temperature and Emissivity products. Further details regarding MODIS land product validation for the MYD11 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD11).\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD11C3.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD11C3.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD11C3.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD11C3.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565794044-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565794044-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD11C3.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD11C3.061",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD11C3",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD11C3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 2 has been achieved for all MODIS Land Surface Temperature and Emissivity products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 2 has been achieved for all MODIS Land Surface Temperature and Emissivity products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD11",
-                    "description": "Further details regarding MODIS land product validation for the MYD11 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MYD11 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD11",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOLA/MYD11C3.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOLA/MYD11C3.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2618671574-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2618671574-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2618671574-LPCLOUD?h=85&w=85",
+            "identifier": "C2565794044-LPCLOUD",
+            "issued": "2021-02-04",
+            "keyword": [
+                "earth science",
+                "surface thermal properties",
+                "ngda",
+                "surface radiative properties",
+                "land surface",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD11C3.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-01T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPM/DPRGMI/CMB/3B-MONTH/07",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "William Olson. 2022-05-09. GPM_3CMB. GPM DPR and GMI (Combined Precipitation) L3 1 month 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/DPRGMI/CMB/3B-MONTH/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3CMB_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-03-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "atmospheric water vapor",
-                "precipitation",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C2179081668-GES_DISC",
-            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n.\n\nThis is a precipitation product created from the combination of the Global Precipitation Measurement (GPM) Microwave Imager (GMI) and Dual-frequency Precipitation Radar (DPR) instruments.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3CMB",
             "creator": "William Olson",
-            "title": "GPM DPR and GMI (Combined Precipitation) L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3CMB) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3CMB_07.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n.\n\nThis is a precipitation product created from the combination of the Global Precipitation Measurement (GPM) Microwave Imager (GMI) and Dual-frequency Precipitation Radar (DPR) instruments.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPRGMI%2FCMB%2F3B-MONTH%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPRGMI%2FCMB%2F3B-MONTH%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -855930,45 +855907,45 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3CMB_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3CMB_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3CMB.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3CMB.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3CMB.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3CMB.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3CMB_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3CMB_07",
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
@@ -855978,85 +855955,110 @@
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3CMB_07.png",
+            "identifier": "C2179081668-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "precipitation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/DPRGMI/CMB/3B-MONTH/07",
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
+            "series-name": "GPM_3CMB",
             "spatial": "-180.0 -67.0 180.0 67.0",
+            "temporal": "2014-03-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM DPR and GMI (Combined Precipitation) L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3CMB) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LEISA-2-LAUNCH-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-leisa-2-launch-v1.0_hb78-xq9q",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LEISA-2-LAUNCH-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-leisa-2-launch-v1.0_hb78-xq9q",
-            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS LEISA POST-LAUNCH CHECKOUT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS LEISA POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.lebofsky-etal.3-micron-spectra&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "3-micron spectrophotometric data on      asteroids collected from several papers by Lebofsky, Jones, and        Feierberg and their collaborators, published 1980-1990.",
+            "identifier": "urn:nasa:pds:gbo.ast.lebofsky-etal.3-micron-spectra",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "(19) fortuna",
                 "(18) melpomene",
@@ -856113,426 +856115,437 @@
                 "(111) ate",
                 "(1172) aneas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.lebofsky-etal.3-micron-spectra&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast.lebofsky-etal.3-micron-spectra",
-            "description": "3-micron spectrophotometric data on      asteroids collected from several papers by Lebofsky, Jones, and        Feierberg and their collaborators, published 1980-1990.",
-            "title": "LEBOFSKY ET AL. 3-MICRON ASTEROID DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LEBOFSKY ET AL. 3-MICRON ASTEROID DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2177",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chen, D., X. Zhu, M. Kogure, E.E. Hoy, X. Xu, N.H.F. French, L.T. Berner, A.L. Breen, S. Bret-Harte, S.J. Davidson, J.J. Ebersole, G.V. Frost, S.J. Goetz, R.E. Hewitt, J.K.Y. Hung, C.M. Iversen, G. Iwahana, R. Jandt, L.K. Jenkins, A.N. Kade, I. Klupar, T.V. Loboda, S. Ludwig, M.J. Macander, M.C. Mack, C.R. Meyers, R.J. Michaelides, E.A. Miller, S. Natali, T.W. Nawrocki, P.R. Nelson, A.D. Parsekian, E. Rastetter, M.K. Raynolds, A.V. Rocha, K. Schaefer, U. Schickhoff, E.A.G. Schuur, S. Tsuyuzaki, C.E. Tweedie, S.V. Zesati, D.A. Walker, P.J. Webber, M. Williams, and D. Zona. 2023. Field Data on Soils, Vegetation, and Fire History for Alaska Tundra Sites, 1972-2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2177",
-            "issued": "2023-10-18",
-            "temporal": "1972-08-01T00:00:00Z/2020-08-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "biosphere",
-                "cryosphere",
-                "frozen ground",
-                "vegetation",
-                "ecosystems",
-                "soils",
-                "ecological dynamics",
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
-            "identifier": "C2756289636-ORNL_CLOUD",
             "description": "This dataset, titled the Synthesized Alaskan Tundra Field Database (SATFiD), provides a comprehensive collection of in-situ field data compiled from 37 existing datasets resulting from field surveys conducted at Alaska tundra sites between 1972 to 2020. The data were harmonized prior to being included in this dataset. The variables include active layer thickness, vegetation cover (by plant functional types), soil moisture and temperatures, as well as the wildfire history. SATFiD provides a unique lens into various long-term ecological processes within the tundra (such as the fire-permafrost-vegetation interactions) under a rapidly changing climate.",
-            "graphic-preview-description": "Locations (blue dots) of field sites in the Alaskan tundra that contributed data to this synthesis database.",
-            "title": "Field Data on Soils, Vegetation, and Fire History for Alaska Tundra Sites, 1972-2020",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/FieldData_Alaska_Tundra_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2177",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2177",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/FieldData_Alaska_Tundra/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/FieldData_Alaska_Tundra/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/FieldData_Alaska_Tundra.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/FieldData_Alaska_Tundra.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2177",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2177",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/FieldData_Alaska_Tundra/comp/FieldData_Alaska_Tundra.pdf",
-                    "description": "Field Data on Soils, Vegetation, and Fire History for Alaska Tundra Sites, 1972-2020: FieldData_Alaska_Tundra.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Field Data on Soils, Vegetation, and Fire History for Alaska Tundra Sites, 1972-2020: FieldData_Alaska_Tundra.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/FieldData_Alaska_Tundra/comp/FieldData_Alaska_Tundra.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/FieldData_Alaska_Tundra_Fig1.jpg",
-                    "description": "Locations (blue dots) of field sites in the Alaskan tundra that contributed data to this synthesis database.",
                     "@type": "dcat:Distribution",
+                    "description": "Locations (blue dots) of field sites in the Alaskan tundra that contributed data to this synthesis database.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/FieldData_Alaska_Tundra_Fig1.jpg",
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
+            "graphic-preview-description": "Locations (blue dots) of field sites in the Alaskan tundra that contributed data to this synthesis database.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/FieldData_Alaska_Tundra_Fig1.jpg",
+            "identifier": "C2756289636-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "biosphere",
+                "cryosphere",
+                "frozen ground",
+                "vegetation",
+                "ecosystems",
+                "soils",
+                "ecological dynamics",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2177",
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
             "spatial": "-166.41 61.14 -141.68 71.33",
+            "temporal": "1972-08-01T00:00:00Z/2020-08-15T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Field Data on Soils, Vegetation, and Fire History for Alaska Tundra Sites, 1972-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECL5D-ISP44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Sea-Ice Salt Plume Fluxes - Daily Mean llc90 Grid (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECL5D-ISP44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Sea-Ice Salt Plume Fluxes - Daily Mean llc90 Grid (Version 4 Release 4); 10.5067/ECL5D-ISP44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "salinity/density",
-                "earth science reanalyses/assimilation models",
-                "earth science",
-                "models",
-                "earth science services",
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
-            "identifier": "C1991543807-POCLOUD",
-            "description": "This dataset provides daily-averaged sea-ice salt plume fluxes on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Sea-Ice Salt Plume Fluxes - Daily Mean llc90 Grid (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_DAILY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides daily-averaged sea-ice salt plume fluxes on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5D-ISP44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5D-ISP44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_DAILY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_DAILY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECL5D-ISP44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECL5D-ISP44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543807-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543807-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543807-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543807-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_DAILY_V4R4.jpg",
+            "identifier": "C1991543807-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "salinity/density",
+                "earth science reanalyses/assimilation models",
+                "earth science",
+                "models",
+                "earth science services",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECL5D-ISP44",
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
+            "title": "ECCO Sea-Ice Salt Plume Fluxes - Daily Mean llc90 Grid (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43IA3N.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2023-11-20. VIIRS/NPP Albedo Daily L3 Global 500m SIN Grid NRT. Version 2. NASA GSFC LANCE. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VNP43IA3N.002. https://doi.org/10.5067/VIIRS/VNP43IA3N.002.",
-            "issued": "2023-11-20",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-11",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LANCEMODIS",
                 "hasEmail": "mailto:support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/TISL/MODAPS"
-            },
-            "identifier": "C2807588708-LANCEMODIS",
-            "description": "The VIIRS/NPP Albedo Daily L3 Global 500 m SIN Grid Near Real Time (NRT), short-name VNP43IA3N product provides albedo values at 500 m resolution for the bi-hemispherical reflectance white-sky albedos (WSA) and directional hemispherical reflectance black-sky albedos (BSA) at local solar noon. The VNP43IA3N product is produced daily using 16-day VIIRS data (i.e., the current day and the previous 15 days). \r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from VNP43IA1N to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43IA4N), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43IA3N). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD) at https://www.umb.edu/editor_uploads/images/school_for_the_environment_cs/Viirs/VIIRS_ATBD_Apr_Jul2017.pdf\r\n\r\nThe VNP43IA3N product provides a total of 9 SDS layers including: BSA, WSA, and mandatory quality layers for VIIRS imagery bands I1, I2, and I3.",
-            "release-place": "NASA GSFC LANCE",
             "creator": "LANCEMODIS",
-            "title": "VIIRS/NPP Albedo Daily L3 Global 500m SIN Grid NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/NPP Albedo Daily L3 Global 500 m SIN Grid Near Real Time (NRT), short-name VNP43IA3N product provides albedo values at 500 m resolution for the bi-hemispherical reflectance white-sky albedos (WSA) and directional hemispherical reflectance black-sky albedos (BSA) at local solar noon. The VNP43IA3N product is produced daily using 16-day VIIRS data (i.e., the current day and the previous 15 days). \r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from VNP43IA1N to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43IA4N), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43IA3N). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD) at https://www.umb.edu/editor_uploads/images/school_for_the_environment_cs/Viirs/VIIRS_ATBD_Apr_Jul2017.pdf\r\n\r\nThe VNP43IA3N product provides a total of 9 SDS layers including: BSA, WSA, and mandatory quality layers for VIIRS imagery bands I1, I2, and I3.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43IA3N.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43IA3N.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP43IA3N/",
-                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
                     "@type": "dcat:Distribution",
+                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP43IA3N/",
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
                 }
             ],
+            "identifier": "C2807588708-LANCEMODIS",
+            "issued": "2023-11-20",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43IA3N.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-02-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/TISL/MODAPS"
+            },
+            "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Albedo Daily L3 Global 500m SIN Grid NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/190/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ashok Srivastava",
+                "hasEmail": "mailto:ashok.n.srivastava@gmail.com"
+            },
+            "description": "In this study we use long-term satellite, climate, and crop observations to document the spatial distribution of the recent stagnation in food grain production affecting the water-limited tropics (WLT), a region where 1.5 billion people live and depend on local agriculture that is constrained by chronic water shortages. Overall, our analysis shows that the recent stagnation in food production is corroborated by satellite data. The growth rate in annually integrated vegetation greenness, a measure of crop growth, has declined significantly (p < 0.10) in 23% of the WLT cropland area during the last decade, while statistically significant increases in the growth rates account for less than 2%. In most countries, the decade-long declines appear to be primarily due to unsustainable crop management practices rather than climate alone. One quarter of the statistically significant declines are observed in India, which with the world\u2019s largest population of food-insecure people and largest WLT croplands, is a leading example of the observed declines. Here we show geographically matching patterns of enhanced crop production and irrigation expansion with groundwater that have leveled off in the past decade. We estimate that, in the absence of irrigation, the enhancement in dry-season food grain production in India, during 1982\u20132002, would have required an increase in annual rainfall of at least 30% over almost half of the cropland area. This suggests that the past expansion of use of irrigation has not been sustainable. We expect that improved surface and groundwater management practices will be required to reverse the recent food grain production declines.\r\n\r\n \r\n**MDPI and ACS Style**\r\n\r\nMilesi, C.; Samanta, A.; Hashimoto, H.; Kumar, K.K.; Ganguly, S.; Thenkabail, P.S.; Srivastava, A.N.; Nemani, R.R.; Myneni, R.B. Decadal Variations in NDVI and Food Production in India. Remote Sens. 2010, 2, 758-776.\r\n\r\n**AMA Style**\r\n\r\nMilesi C., Samanta A., Hashimoto H., Kumar K.K., Ganguly S., Thenkabail P.S., Srivastava A.N., Nemani R.R., Myneni R.B. Decadal Variations in NDVI and Food Production in India. Remote Sensing. 2010; 2(3):758-776.\r\n\r\n**Chicago/Turabian Style**\r\n\r\nMilesi, Cristina; Samanta, Arindam; Hashimoto, Hirofumi; Kumar, K. Krishna; Ganguly, Sangram; Thenkabail, Prasad S.; Srivastava, Ashok N.; Nemani, Ramakrishna R.; Myneni, Ranga B. 2010. \"Decadal Variations in NDVI and Food Production in India.\" Remote Sens. 2, no. 3: 758-776.",
+            "identifier": "DASHLINK_190",
             "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ames",
                 "dashlink",
                 "nasa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ashok Srivastava",
-                "hasEmail": "mailto:ashok.n.srivastava@gmail.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/190/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_190",
-            "description": "In this study we use long-term satellite, climate, and crop observations to document the spatial distribution of the recent stagnation in food grain production affecting the water-limited tropics (WLT), a region where 1.5 billion people live and depend on local agriculture that is constrained by chronic water shortages. Overall, our analysis shows that the recent stagnation in food production is corroborated by satellite data. The growth rate in annually integrated vegetation greenness, a measure of crop growth, has declined significantly (p < 0.10) in 23% of the WLT cropland area during the last decade, while statistically significant increases in the growth rates account for less than 2%. In most countries, the decade-long declines appear to be primarily due to unsustainable crop management practices rather than climate alone. One quarter of the statistically significant declines are observed in India, which with the world\u2019s largest population of food-insecure people and largest WLT croplands, is a leading example of the observed declines. Here we show geographically matching patterns of enhanced crop production and irrigation expansion with groundwater that have leveled off in the past decade. We estimate that, in the absence of irrigation, the enhancement in dry-season food grain production in India, during 1982\u20132002, would have required an increase in annual rainfall of at least 30% over almost half of the cropland area. This suggests that the past expansion of use of irrigation has not been sustainable. We expect that improved surface and groundwater management practices will be required to reverse the recent food grain production declines.\r\n\r\n \r\n**MDPI and ACS Style**\r\n\r\nMilesi, C.; Samanta, A.; Hashimoto, H.; Kumar, K.K.; Ganguly, S.; Thenkabail, P.S.; Srivastava, A.N.; Nemani, R.R.; Myneni, R.B. Decadal Variations in NDVI and Food Production in India. Remote Sens. 2010, 2, 758-776.\r\n\r\n**AMA Style**\r\n\r\nMilesi C., Samanta A., Hashimoto H., Kumar K.K., Ganguly S., Thenkabail P.S., Srivastava A.N., Nemani R.R., Myneni R.B. Decadal Variations in NDVI and Food Production in India. Remote Sensing. 2010; 2(3):758-776.\r\n\r\n**Chicago/Turabian Style**\r\n\r\nMilesi, Cristina; Samanta, Arindam; Hashimoto, Hirofumi; Kumar, K. Krishna; Ganguly, Sangram; Thenkabail, Prasad S.; Srivastava, Ashok N.; Nemani, Ramakrishna R.; Myneni, Ranga B. 2010. \"Decadal Variations in NDVI and Food Production in India.\" Remote Sens. 2, no. 3: 758-776.",
-            "title": "Decadal Variations in NDVI and Food Production in India",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Decadal Variations in NDVI and Food Production in India"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aasteroid_polarimetric_database&version=1.0",
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
+            "description": "The Asteroid Polarimetric Database (APD) is a collection of asteroid polarimetry\nresults compiled by D.F. Lupishko of Karazin Kharkiv National University, Ukraine. It\nis intended to include most asteroid polarimetry available through February 15, 2019.",
+            "identifier": "urn:nasa:pds:asteroid_polarimetric_database",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aasteroid_polarimetric_database&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:asteroid_polarimetric_database",
-            "description": "The Asteroid Polarimetric Database (APD) is a collection of asteroid polarimetry\nresults compiled by D.F. Lupishko of Karazin Kharkiv National University, Ukraine. It\nis intended to include most asteroid polarimetry available through February 15, 2019.",
-            "title": "Asteroid Polarimetric Database V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Asteroid Polarimetric Database V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567941-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 2013-01-01. Global Forest Observations Initiative - Burma. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://lsiexplorer.cr.usgs.gov.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EUGENE FOSNIGHT",
+                "hasEmail": "mailto:fosnight@usgs.gov"
+            },
+            "creator": "U.S. Geological Survey",
+            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilising observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         Group on Earth Observations (GEO) Global Forest Observations Initiative (GFOI)\n      ",
+                    "downloadURL": "http://www.gfoi.org/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                }
+            ],
+            "identifier": "C1220567941-USGS_LTA",
             "issued": "1972-01-01",
-            "temporal": "1972-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
             "keyword": [
                 "vegetation",
                 "agriculture",
@@ -856543,145 +856556,135 @@
                 "human dimensions",
                 "earth science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EUGENE FOSNIGHT",
-                "hasEmail": "mailto:fosnight@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567941-USGS_LTA.html",
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
-            "identifier": "C1220567941-USGS_LTA",
-            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilising observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
-            "creator": "U.S. Geological Survey",
-            "title": "USGS Global Forest Observations Initiative (GFOI) Burma",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.gfoi.org/",
-                    "description": "\n         Group on Earth Observations (GEO) Global Forest Observations Initiative (GFOI)\n      ",
-                    "@type": "dcat:Distribution",
-                    "title": "The dataset's project home page"
-                }
-            ],
             "spatial": "92.0 10.0 102.0 28.0",
+            "temporal": "1972-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Global Forest Observations Initiative (GFOI) Burma"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567925-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 2013-01-01. Global Forest Observations Initiative - Nicaragua. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://lsiexplorer.cr.usgs.gov.",
-            "issued": "1972-01-01",
-            "temporal": "1972-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "agriculture",
-                "forest science",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EUGENE FOSNIGHT",
                 "hasEmail": "mailto:fosnight@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220567925-USGS_LTA",
-            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilising observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
             "creator": "U.S. Geological Survey",
-            "title": "USGS Global Forest Observations Initiative (GFOI) Nicaragua",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilising observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.gfoi.org/",
-                    "description": "\n         Group on Earth Observations (GEO) Global Forest Observations Initiative (GFOI)\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Group on Earth Observations (GEO) Global Forest Observations Initiative (GFOI)\n      ",
+                    "downloadURL": "http://www.gfoi.org/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "identifier": "C1220567925-USGS_LTA",
+            "issued": "1972-01-01",
+            "keyword": [
+                "agriculture",
+                "forest science",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567925-USGS_LTA.html",
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
             "spatial": "-87.5 10.75 -83.0 16.0",
+            "temporal": "1972-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Global Forest Observations Initiative (GFOI) Nicaragua"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-2-CR4A-V1.0",
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
+            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 4A mission phase, which occurred during July 2008.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-2-cr4a-v1.0_hbeh-6ai8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-2-CR4A-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-2-cr4a-v1.0_hbeh-6ai8",
-            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 4A mission phase, which occurred during July 2008.",
-            "title": "ROSETTA-ORBITER CAL ALICE 2 CR4A V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL ALICE 2 CR4A V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.lpi.usra.edu/resources/apollopanoramas/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1967-01-01/1973-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.lpi.usra.edu/resources/apollopanoramas/",
-                "http://www.lpi.usra.edu/resources/cla/",
-                "http://www.lpi.usra.edu/resources/lunarorbiter/",
-                "http://www.lpi.usra.edu/resources/lunar_orbiter/",
-                "http://www.lpi.usra.edu/resources/ranger/",
-                "http://planetarynames.wr.usgs.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Paul Schenk",
+                "hasEmail": "mailto:rpif@lpi.usra.edu"
+            },
+            "description": "Apollo Surface Panoramas is a digital library of photographic panoramas that the Apollo astronauts took while exploring the Moon's surface. These images provide a spectacular boots-on-the-ground view of the lunar landscape. Lunar surface features captured in the panoramas can be studied using zoom and pan tools. An annotated version of each panorama is also available to assist users with the identification of major geographic features around each Apollo landing site.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.lpi.usra.edu/resources/apollopanoramas/",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "NASA-0000020",
+            "issued": "2018-06-25",
             "keyword": [
                 "venus",
                 "circulation",
@@ -856690,67 +856693,43 @@
                 "modeling",
                 "space science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Paul Schenk",
-                "hasEmail": "mailto:rpif@lpi.usra.edu"
-            },
+            "landingPage": "http://www.lpi.usra.edu/resources/apollopanoramas/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000020",
-            "description": "Apollo Surface Panoramas is a digital library of photographic panoramas that the Apollo astronauts took while exploring the Moon's surface. These images provide a spectacular boots-on-the-ground view of the lunar landscape. Lunar surface features captured in the panoramas can be studied using zoom and pan tools. An annotated version of each panorama is also available to assist users with the identification of major geographic features around each Apollo landing site.",
-            "title": "Apollo Surface Panoramas",
-            "programCode": [
-                "026:009"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.lpi.usra.edu/resources/apollopanoramas/",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "http://www.lpi.usra.edu/resources/apollopanoramas/",
+                "http://www.lpi.usra.edu/resources/cla/",
+                "http://www.lpi.usra.edu/resources/lunarorbiter/",
+                "http://www.lpi.usra.edu/resources/lunar_orbiter/",
+                "http://www.lpi.usra.edu/resources/ranger/",
+                "http://planetarynames.wr.usgs.gov/"
             ],
             "spatial": "Lunar",
-            "accrualPeriodicity": "irregular",
+            "temporal": "1967-01-01/1973-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Apollo Surface Panoramas"
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
-                "spice",
-                "pds",
-                "grs"
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
-            "identifier": "NASA-691",
             "description": "GRS, SPICE, RSS",
-            "title": "PDS Odyssey Data Delivery 10",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -856758,499 +856737,501 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-691",
+            "issued": "2018-06-25",
+            "keyword": [
+                "rss",
+                "spice",
+                "pds",
+                "grs"
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
+            "title": "PDS Odyssey Data Delivery 10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD09A1.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD09A1.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-01",
-            "temporal": "2000-02-18T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-01",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "surface radiative properties"
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
-            "identifier": "C2343111356-LPCLOUD",
             "description": "The  Moderate Resolution Imaging Spectroradiometer (MODIS) Terra MOD09A1 Version 6.1 product provides an estimate of the surface spectral reflectance of Terra MODIS Bands 1 through 7 corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. Along with the seven 500 meter (m) reflectance bands are two quality layers and four observation bands. For each pixel, a value is selected from all the acquisitions within the 8-day composite period. The criteria for the pixel choice include cloud and solar zenith. When several acquisitions meet the criteria the pixel with the minimum channel 3 (blue) value is used. \n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Reflectance products. Further details regarding MODIS land product validation for the MOD09 data product is available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD09).\n\nImprovements/Changes from Previous Versions \n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "title": "MODIS/Terra Surface Reflectance 8-Day L3 Global 500m SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2508869786-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09A1.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09A1.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD09A1.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD09A1.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2343111356-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2343111356-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD09A1.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD09A1.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD09A1",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD09A1",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD09A1.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD09A1.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2508869786-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2508869786-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2508869786-LPCLOUD?h=85&w=85",
+            "identifier": "C2343111356-LPCLOUD",
+            "issued": "2021-02-01",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD09A1.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-18T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Surface Reflectance 8-Day L3 Global 500m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67PCHURYUMOV-M17-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67pchuryumov-m17-v2.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67PCHURYUMOV-M17-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67pchuryumov-m17-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP017 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP017 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1838",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Vetrita, Y., and M.A. Cochrane. 2021. Land Use and Cover Maps from Landsat, Mawas, Central Kalimantan, Indonesia, 1994-2019. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1838",
-            "issued": "2021-03-15",
-            "temporal": "1994-01-01T00:00:00Z/2019-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "land use/land cover",
-                "land surface",
-                "human dimensions",
-                "environmental governance/management",
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
-            "identifier": "C2345896026-ORNL_CLOUD",
             "description": "This dataset contains annual land use/cover (LUC) maps at 30 m resolution across Mawas, Central Kalimantan, Indonesia. There are six files, each representing a five-year interval over the period 1994-2019. An additional file for 2015 was created for accuracy assessment. A high-quality and low-cloud coverage image from Landsat 5 or Landsat 8 over each 5-year period was selected or composited for the January-August timeframe. Investigators used their knowledge to manually identify training polygons in these images for five LUC classes: peat swamp forest, tall shrubs/ secondary forest, low shrubs/ferns/grass, urban/bare land/open flooded areas, and river. Pixel values of Landsat Tier 1 surface reflectance products and selected indices were extracted for each LUC and used to predict LUC classes across the Mawas study area using the Classification and Regression Trees (CART) method. These data can be used to evaluate the relationship between fire occurrence and land cover type in the study site.",
-            "graphic-preview-description": "Land cover maps at 30 m resolution across Mawas, Central Kalimantan, Indonesia in 1994 (left) and 2004 (right).",
-            "title": "Land Use and Cover Maps from Landsat, Mawas, Central Kalimantan, Indonesia, 1994-2019",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Landcover_Indonesia_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1838",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1838",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Landcover_Indonesia/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Landcover_Indonesia/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Landcover_Indonesia.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Landcover_Indonesia.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1838",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1838",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Landcover_Indonesia/comp/CMS_Landcover_Indonesia.pdf",
-                    "description": "Land Use and Cover Maps from Landsat, Mawas, Central Kalimantan, Indonesia, 1994-2019: CMS_Landcover_Indonesia.pdf",
                     "@type": "dcat:Distribution",
```

