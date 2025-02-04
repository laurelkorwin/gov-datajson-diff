# Change History for nasa.json (Part 78)

### Changes from 31606f9 to dd2190f (Part 67/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
+            "title": "Sentinel-3B OLCI Level-2 Earth-observation Full Resolution (EFR) Ocean Color (OC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_RTC-S1-STATIC_V1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OPERA. 2023-12-05. OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 Static Layers validated product (Version 1). Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Alaska Satellite Facility Distributed Active Archive Center. https://doi.org/10.5067/SNWG/OPERA_L2_RTC-S1-STATIC_V1.",
-            "issued": "2014-04-03",
-            "temporal": "2014-04-03T00:00:00Z/2023-12-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-04-03",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2022.3147472"
-            ],
-            "keyword": [
-                "oceans",
-                "coastal processes",
-                "cryosphere",
-                "earth science",
-                "geomorphic landforms/processes",
-                "glaciers/ice sheets",
-                "land surface",
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
-            "identifier": "C2795135174-ASF",
-            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Radiometric Terrain Corrected (RTC) SAR Backscatter from Sentinel-1 (S1) Static Layers (RTC-S1-STATIC) validated product contains static radar geometry layers associated with the OPERA Radiometric Terrain Corrected (RTC) SAR Backscatter from Sentinel-1 (S1) (RTC-S1) validated product.  Due to the S1 mission\u2019s narrow orbital tube, radar-geometry layers such as incidence angle, local incidence angle, number of looks, and RTC Area Normalization Factor (ANF) vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA RTC-S1 product, as they are produced only once or a limited number of times, to account for changes in the DEM, in the S1 orbit, or in the static-layers generation algorithm.  Static layers are provided as single-band cloud-optimized GeoTIFF (COG) files, with map grid matching RTC-S1 products with the same burst ID.  The standard OPERA RTC-S1 product is derived from the original Copernicus Sentinel-1 (S1) interferometric wide (IW) single-look complex (SLC) data, provided by the European Space Agency, with a temporal sampling coincident with the availability of Sentinel-1A and Sentinel-1B SLC data. The OPERA RTC-S1-STATIC and RTC-S1 products are provided at a near global scope (land masses excluding Antarctica).  The RTC-S1 products are available in the associated OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 validated product (Version 1) dataset.",
-            "graphic-preview-description": "Image to represent the collection",
             "creator": "OPERA",
-            "title": "OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 Static Layers validated product (Version 1)",
-            "graphic-preview-file": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_RTC-S1-STATIC_T004-006672-IW1_20140403_S1A_30_v1.0_BROWSE.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Radiometric Terrain Corrected (RTC) SAR Backscatter from Sentinel-1 (S1) Static Layers (RTC-S1-STATIC) validated product contains static radar geometry layers associated with the OPERA Radiometric Terrain Corrected (RTC) SAR Backscatter from Sentinel-1 (S1) (RTC-S1) validated product.  Due to the S1 mission\u2019s narrow orbital tube, radar-geometry layers such as incidence angle, local incidence angle, number of looks, and RTC Area Normalization Factor (ANF) vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA RTC-S1 product, as they are produced only once or a limited number of times, to account for changes in the DEM, in the S1 orbit, or in the static-layers generation algorithm.  Static layers are provided as single-band cloud-optimized GeoTIFF (COG) files, with map grid matching RTC-S1 products with the same burst ID.  The standard OPERA RTC-S1 product is derived from the original Copernicus Sentinel-1 (S1) interferometric wide (IW) single-look complex (SLC) data, provided by the European Space Agency, with a temporal sampling coincident with the availability of Sentinel-1A and Sentinel-1B SLC data. The OPERA RTC-S1-STATIC and RTC-S1 products are provided at a near global scope (land masses excluding Antarctica).  The RTC-S1 products are available in the associated OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 validated product (Version 1) dataset.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSNWG%2FOPERA_L2_RTC-S1-STATIC_V1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSNWG%2FOPERA_L2_RTC-S1-STATIC_V1",
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
-                    "downloadURL": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_RTC-S1-STATIC_T004-006672-IW1_20140403_S1A_30_v1.0_BROWSE.png",
-                    "description": "Image to represent the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Image to represent the collection",
+                    "downloadURL": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_RTC-S1-STATIC_T004-006672-IW1_20140403_S1A_30_v1.0_BROWSE.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Image to represent the collection",
+            "graphic-preview-file": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_RTC-S1-STATIC_T004-006672-IW1_20140403_S1A_30_v1.0_BROWSE.png",
+            "identifier": "C2795135174-ASF",
+            "issued": "2014-04-03",
+            "keyword": [
+                "oceans",
+                "coastal processes",
+                "cryosphere",
+                "earth science",
+                "geomorphic landforms/processes",
+                "glaciers/ice sheets",
+                "land surface",
+                "solid earth",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_RTC-S1-STATIC_V1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-04-03",
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
+            "temporal": "2014-04-03T00:00:00Z/2023-12-11T00:00:00Z",
             "theme": [
                 "SNWG/OPERA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 Static Layers validated product (Version 1)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1145-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-31T08:38:10.000 to 2015-10-31T17:12:57.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1145-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1145-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1145-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-31T08:38:10.000 to 2015-10-31T17:12:57.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1145 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1145 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-PROPERTIES-V2.0",
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
-                "comet",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-properties-v2.0_ec8g-gvby",
+            "issued": "2018-06-26",
+            "keyword": [
+                "comet",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-PROPERTIES-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-properties-v2.0_ec8g-gvby",
-            "description": "not applicable",
-            "title": "PROPERTIES OF COMET NUCLEI",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PROPERTIES OF COMET NUCLEI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA205",
             "citation": "P.K. Bhartia, et al.. 2012-08-07. SBUV2N14L2. Version 1. SBUV2/NOAA-14 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/OZONE/DATA205. https://disc.gsfc.nasa.gov/datacollection/SBUV2N14L2_1.html. Digital Science Data.",
-            "issued": "2013-07-02",
-            "temporal": "1995-02-05T00:00:00Z/2006-09-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-07-02",
-            "references": [
-                "https://doi.org/doi:10.5194/amt-5-2951-2012",
-                "https://doi.org/doi:10.5194/amt-6-2533-2013",
-                "https://doi.org/doi:10.1002/jgrd.50597"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RICHARD MCPETERS, PH. D",
                 "hasEmail": "mailto:richard.d.mcpeters@nasa.gov"
             },
+            "creator": "P.K. Bhartia, et al.",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1251051546-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Solar Backscattered Ultraviolet (SBUV) from NOAA-14 Level-2 daily product (SBUV2N14L2) contains ozone nadir profile and total column data from retrievals generated from the v8.6 SBUV algorithm. The v8.6 SBUV algorithm estimates the ozone nadir profile and total column from SBUV measurements using 1) the Brion-Daumont-Malicet ozone cross sections, 2) an OMI-derived cloud-height climatology, 3) a revised a priori ozone climatology, and 4) inter-instrument calibration based on comparisons with no local time difference.\n\nThe SBUV2N14L2 product is written as daily files using the HDF5 format, with file sizes ranging from about 1 to 5 Mbytes. Data are available from March 1995 through September 2006. The SBUV2N14L2 data product was used as input in creating the SBUV2N14L3zm monthly zonal mean data product.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SBUV2N14L2",
-            "creator": "P.K. Bhartia, et al.",
-            "title": "SBUV2/NOAA-14 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N14L2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N14L2_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA205",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA205",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -696665,525 +696638,566 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N14L2_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N14L2_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N14L2.1/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N14L2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N14L2.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N14L2.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N14L2.1/catalog.xml",
-                    "description": "Access the data using the THREDDS Catalog.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data using the THREDDS Catalog.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N14L2.1/catalog.xml",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N14L2.1/doc/README.SBUVL2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N14L2.1/doc/README.SBUVL2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N14L2_1.png",
+            "identifier": "C1251051546-GES_DISC",
+            "issued": "2013-07-02",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA205",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-07-02",
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
+            "series-name": "SBUV2N14L2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1995-02-05T00:00:00Z/2006-09-28T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SBUV2/NOAA-14 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N14L2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ORPA-5-ELE%2FION%2FPHOTO%2FUADS-V1.0",
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
-                "pioneer venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The ORPA processed data consist of 4\nfile types: high resolution thermal electrons, high resolution superthermal\nelectrons, high resolution ions, and a key parameters file at 12 second\nsampling.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-orpa-5-ele-ion-photo-uads-v1.0_ec8y-ke47",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "pioneer venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ORPA-5-ELE%2FION%2FPHOTO%2FUADS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-orpa-5-ele-ion-photo-uads-v1.0_ec8y-ke47",
-            "description": "The ORPA processed data consist of 4\nfile types: high resolution thermal electrons, high resolution superthermal\nelectrons, high resolution ions, and a key parameters file at 12 second\nsampling.",
-            "title": "PVO RPA PROC THERM ELEC, ION,\n                                   PHOTOELEC, LOW RES. V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PVO RPA PROC THERM ELEC, ION,\n                                   PHOTOELEC, LOW RES. V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1656",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cosgrove, C.L., L.R. Prugh, A.W. Nolin, K.J. Sivy, R.L. Crumley, and M.E. Tedesche. 2019. Snow Depth, Stratigraphy, and Temperature in Wrangell St Elias NP, Alaska, 2016-2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1656",
-            "issued": "2019-04-12",
-            "temporal": "2016-09-01T00:00:00Z/2018-03-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
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
-            "identifier": "C2170971586-ORNL_CLOUD",
             "description": "This dataset includes data from late-March snow surveys and hourly digital camera images from two study areas within the Wrangell St Elias National Park, Alaska. These data comprise snow density, stratigraphy, and temperature profiles obtained by snow pits; and snow depth data obtained from transects between snow pits. Daily snow depths, adjacent to each pit, were derived from hourly camera images of snow stakes placed adjacent to each pit. These data were collected to constrain and validate a physically-based, spatially-distributed snow evolution model used to simulate snow conditions in Dall sheep habitat. The two study areas are both located within the Jacksina Park Unit (JPU). The first study area, surveyed in 2017, included the northern end of Jaeger Mesa and an area near Rambler mine in the North East of the JPU. The second study area, surveyed in 2018, was within the upper watershed of Pass Creek in the North of the JPU. The remote cameras operated from September 2016 to August 2017 on Jaeger Mesa/Rambler Mine and from September 2017 to July 2018 at Pass Creek.",
-            "graphic-preview-description": "A remote camera image showing the snow stake at plot 15 of the Jaeger Mesa/Rambler Mine study area. Snow depth can be determined using a provided image analysis script.",
-            "title": "Snow Depth, Stratigraphy, and Temperature in Wrangell St Elias NP, Alaska, 2016-2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Snow_Depth_Data_Images_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1656",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1656",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Snow_Depth_Data_Images/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Snow_Depth_Data_Images/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Snow_Depth_Data_Images.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Snow_Depth_Data_Images.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1656",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1656",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "video/mp4",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/c15_lapse.mp4",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: c15_lapse.mp4",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: c15_lapse.mp4",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/c15_lapse.mp4",
+                    "mediaType": "video/mp4",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/getCameraDepth.m",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: getCameraDepth.m",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: getCameraDepth.m",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/getCameraDepth.m",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c01.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c01.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c01.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c01.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c02.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c02.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c02.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c02.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c03.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c03.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c03.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c03.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c04.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c04.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c04.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c04.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c05.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c05.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c05.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c05.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c06.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c06.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c06.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c06.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c07.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c07.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c07.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c07.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c08.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c08.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c08.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c08.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c09.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c09.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c09.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c09.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c10.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c10.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c10.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c10.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c11.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c11.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c11.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c11.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c12.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c12.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c12.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c12.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c13.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c13.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c13.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c13.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c14.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c14.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c14.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c14.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c15.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c15.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c15.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c15.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c16.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c16.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c16.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c16.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c17.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c17.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c17.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c17.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c18.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c18.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c18.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c18.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c19.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c19.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c19.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c19.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c20.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c20.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c20.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c20.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c21.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c21.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c21.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c21.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c22.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c22.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: jaegermesa_nabesna_c22.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/jaegermesa_nabesna_c22.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c01.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c01.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c01.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c01.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c02.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c02.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c02.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c02.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c03.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c03.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c03.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c03.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c04.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c04.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c04.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c04.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c05.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c05.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c05.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c05.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c06.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c06.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c06.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c06.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c07.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c07.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c07.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c07.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c08.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c08.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c08.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c08.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c09.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c09.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c09.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c09.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c10.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c10.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c10.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c10.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c11.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c11.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c11.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c11.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c12.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c12.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c12.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c12.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c13.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c13.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c13.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c13.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c14.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c14.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c14.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c14.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c15.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c15.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c15.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c15.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c16.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c16.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c16.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c16.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c17.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c17.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c17.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c17.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c18.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c18.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c18.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c18.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c19.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c19.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c19.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c19.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c20.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c20.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c20.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c20.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c21.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c21.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c21.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c21.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c22.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c22.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: passcreek_c22.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/passcreek_c22.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/Pit_photos.zip",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: Pit_photos.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: Pit_photos.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/Pit_photos.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/pit_template_snowex.pdf",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, Temperature, Wrangell St Elias NP, Alaska, 2016-2018: pit_template_snowex.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, Temperature, Wrangell St Elias NP, Alaska, 2016-2018: pit_template_snowex.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/pit_template_snowex.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/Snow_Depth_Data_Images.pdf",
-                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: Snow_Depth_Data_Images.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Snow Depth, Stratigraphy, and Temperature Survey Data; Alaska, 2017-2018: Snow_Depth_Data_Images.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Snow_Depth_Data_Images/comp/Snow_Depth_Data_Images.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Snow_Depth_Data_Images_Fig1.jpg",
-                    "description": "A remote camera image showing the snow stake at plot 15 of the Jaeger Mesa/Rambler Mine study area. Snow depth can be determined using a provided image analysis script.",
                     "@type": "dcat:Distribution",
+                    "description": "A remote camera image showing the snow stake at plot 15 of the Jaeger Mesa/Rambler Mine study area. Snow depth can be determined using a provided image analysis script.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Snow_Depth_Data_Images_Fig1.jpg",
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
+            "graphic-preview-description": "A remote camera image showing the snow stake at plot 15 of the Jaeger Mesa/Rambler Mine study area. Snow depth can be determined using a provided image analysis script.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Snow_Depth_Data_Images_Fig1.jpg",
+            "identifier": "C2170971586-ORNL_CLOUD",
+            "issued": "2019-04-12",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1656",
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
             "spatial": "-143.32 62.26 -143.0 62.39",
+            "temporal": "2016-09-01T00:00:00Z/2018-03-20T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Snow Depth, Stratigraphy, and Temperature in Wrangell St Elias NP, Alaska, 2016-2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/eca5-kixu",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Microgravity alters the immune response to in vitro LPS assault engineered in spaceflight: A multi-omics study Microgravity can facilitate creation of a potent environment for opportunistic infection by augmenting virulence and suppressing the host defense. Presumably extraterrestrial infection may trigger potentially novel bionetworks different from the terrestrial equivalent which could only be probed by investigating the host-pathogen relationship with minimum terrestrial bias. Towards this objective we strategically engineered a cell culture module equipped with a feedback controlled semi-automated platform to expose human endothelial cells to lipopolysaccharide (LPS). The assay was carried out in the STS-135 space shuttle and a concurrent ground study constituted the baseline. Transcriptomic investigation revealed an immune blunting in microgravity; Lbp MyD88 and MD-2 failed to encode proteins responsible for early LPS uptake. Longer exposure results implied that there was a delayed response potentially ineffectual in preventing pathogens from opportunistically modulating the infection network. Lack of recruitment of growth factors and a debilitated apoptosome supported this potential explanation. Certain cytokines such as IL-6 and IL-8 surged in response to LPS insult in microgravity. Contrasting expressions of B2M TIMP-1 and VEGRs suggested impaired pro-survival adaptation and healing mechanisms. The susceptibility of oxidative stress and immune regulation to microgravity compelled further investigation of the respective microRNA modulators such as miR-200a and miR-146b. These miRNAs were expressed differently in response to LPS assaults in different gravitational limits. In conclusion despite a serious drawback attributed to the small sample size we delineated some of the important aspects of the extraterrestrial etiology; more comprehensive follow up studies are warranted. Present study though compromised by the small sample size was able to shade lights on several aspects of immunological responses to the endotoxic assault mediated by uG. Implementing the host-pathogen interactions in the spaceflight and subsequently lysing the cells onboard presented the critical distinguishing features of the present study from the past reports. We identified the CCM of Tissue Genesis Inc. HI as the suitable hardware system to carry out the experiment in the spaceflight. CCM is an automated feedback controlled module that can concurrently support 24 bioreactors following protocols exclusively programmed for individual bioreactor. For this experiment we use samples EA41 EA 47 EA45 and EA155 that were exposed to LPS for 4 hours. Samples EA123 EA165 EA127 EA126 were exposed to LPS for 8Hrs. Samples EA33 EA 125 EA79 and EA 39 were controls in this experiment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-54",
+                    "mediaType": "text/html",
+                    "title": "Immune responses to the in vitro LPS assault engineered in the spaceflight multi-omics study"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-54_eca5-kixu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "microgravity",
                 "absorbed radiation dose",
@@ -697206,66 +697220,34 @@
                 "treatment",
                 "treatment duration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/eca5-kixu",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-54_eca5-kixu",
-            "description": "Microgravity alters the immune response to in vitro LPS assault engineered in spaceflight: A multi-omics study Microgravity can facilitate creation of a potent environment for opportunistic infection by augmenting virulence and suppressing the host defense. Presumably extraterrestrial infection may trigger potentially novel bionetworks different from the terrestrial equivalent which could only be probed by investigating the host-pathogen relationship with minimum terrestrial bias. Towards this objective we strategically engineered a cell culture module equipped with a feedback controlled semi-automated platform to expose human endothelial cells to lipopolysaccharide (LPS). The assay was carried out in the STS-135 space shuttle and a concurrent ground study constituted the baseline. Transcriptomic investigation revealed an immune blunting in microgravity; Lbp MyD88 and MD-2 failed to encode proteins responsible for early LPS uptake. Longer exposure results implied that there was a delayed response potentially ineffectual in preventing pathogens from opportunistically modulating the infection network. Lack of recruitment of growth factors and a debilitated apoptosome supported this potential explanation. Certain cytokines such as IL-6 and IL-8 surged in response to LPS insult in microgravity. Contrasting expressions of B2M TIMP-1 and VEGRs suggested impaired pro-survival adaptation and healing mechanisms. The susceptibility of oxidative stress and immune regulation to microgravity compelled further investigation of the respective microRNA modulators such as miR-200a and miR-146b. These miRNAs were expressed differently in response to LPS assaults in different gravitational limits. In conclusion despite a serious drawback attributed to the small sample size we delineated some of the important aspects of the extraterrestrial etiology; more comprehensive follow up studies are warranted. Present study though compromised by the small sample size was able to shade lights on several aspects of immunological responses to the endotoxic assault mediated by uG. Implementing the host-pathogen interactions in the spaceflight and subsequently lysing the cells onboard presented the critical distinguishing features of the present study from the past reports. We identified the CCM of Tissue Genesis Inc. HI as the suitable hardware system to carry out the experiment in the spaceflight. CCM is an automated feedback controlled module that can concurrently support 24 bioreactors following protocols exclusively programmed for individual bioreactor. For this experiment we use samples EA41 EA 47 EA45 and EA155 that were exposed to LPS for 4 hours. Samples EA123 EA165 EA127 EA126 were exposed to LPS for 8Hrs. Samples EA33 EA 125 EA79 and EA 39 were controls in this experiment.",
-            "title": "Immune responses to the in vitro LPS assault engineered in the spaceflight multi-omics study",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-54",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Immune responses to the in vitro LPS assault engineered in the spaceflight multi-omics study"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Immune responses to the in vitro LPS assault engineered in the spaceflight multi-omics study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://eosweb.larc.nasa.gov/project/ceres/ceres_table",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "energy",
-                "clouds",
-                "moisture",
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
-            "identifier": "NASA-0000028",
+            "describedBy": "https://eosweb.larc.nasa.gov/project/ceres/ceres_table",
             "description": "The Clouds and the Earth's Radiant Energy System (CERES) is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999, and two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002.",
-            "title": "Clouds and the Earth's Radiant Energy System (CERES)",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -697273,89 +697255,108 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "https://eosweb.larc.nasa.gov/project/ceres/ceres_table",
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-0000028",
+            "issued": "2018-06-25",
+            "keyword": [
+                "energy",
+                "clouds",
+                "moisture",
+                "eos",
+                "climate"
+            ],
+            "landingPage": "https://eosweb.larc.nasa.gov/project/ceres/ceres_table",
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
+            "title": "Clouds and the Earth's Radiant Energy System (CERES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD07_L2.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2017-10-20. MODIS/Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MOD07_L2.NRT.061. http://modis-atmos.gsfc.nasa.gov/MOD07_L2/.",
-            "issued": "2017-10-11",
-            "temporal": "2017-10-11T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "atmospheric phenomena",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "national geospatial data asset",
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1426510452-LANCEMODIS",
-            "description": "The level-2 MODIS Temperature and Water Vapor Profile Product MOD07_L2 consists of 30 gridded parameters related to atmospheric stability, atmospheric temperature and moisture profiles, total atmospheric water vapor, and total ozone. All of these parameters are produced for both daytime and nighttime conditions at 5-km pixel resolution when at least 9 FOVs are cloud free.                        \n\nThe atmospheric profiles are produced at 20 vertical atmospheric levels (5., 10., 20., 30., 50., 70., 100., 150., 200., 250., 300., 400., 500., 620., 700., 780., 850., 920., 950., 1000. mbar) The water vapor parameter is an estimate of the total tropospheric column water vapor made from integrated MODIS infrared retrievals of atmospheric moisture profiles in clear scenes. The thermal band 9.6 micron is used for retrieving total ozone burden.                        \n\nThe shortname for this Level-2 MODIS atmospheric profile product is MOD07_L2 and the principal investigator for this product is MODIS scientist Dr. Paul Menzel ( paulm@ssec.wisc.edu).The MODIS atmospheric profile (MOD07_L2) product contains data that has a spatial resolution (pixel size) of 5 x 5 kilometers (at nadir). Each MOD07_L2 product file covers a five-minute time interval, which means the MOD07_L2 output grid is 270 5-km pixels in width and 406 5-km pixels in length for nine consecutive granules. Every tenth granule has an output grid size of 270 by 408 pixels.\n\nMOD07_L2 product files are stored in Hierarchical Data Format(HDF-EOS). Twenty eight of the 30 gridded cloud parameters(5-kilometer pixel resolution) are stored as Scientific Data Sets (SDS) within the file, the remaining two algorithmic static parameters (band number and presure level) are stored as Vdata(table arrays). Cloud Mask SDS, derived from the 1-km MOD35_L2 Cloud Mask parameter, is remapped to 5-km resolution, by using only the center 1-km pixel in the 5x5 pixel retrieval array. The remaining two (band number and static pressure levels) are stored as Vdata(table arrays) Each file is roughly 8 MB in size, and the total data volume is approximately 2 GB/day.\nMOD07_L2 Data Group and Parameters:                         Spatial &amp; Temporal Resolution:\nLatitude &amp; LongitudeScan start time\n\nSolar and Sensor Viewing Geometry:\n\nSolar zenith &amp; Solar azimuth angleSensor zenith &amp; Sensor azimuth angle\n\nStatic Algorithm Parameters:\nMODIS band number; Pressure levels Atmospheric &amp; \n\nSurface Pressure:\n\nRetrieved Geopotential Height ProfileTropopause HeightSurface Elevation, Surface Pressure                        Atmospheric &amp; Surface Temperature:Guess &amp; Retrieved Temperature ProfilesBrightness Temperature and Skin Temperature\n\nAtmospheric Moisture:\n\nGuess Mixing ratio ProfileRetrieved Dew Point Temperature Profile\nAtmospheric Stability Indices:\n\nTotal Totals, Lifted Index, and K-index                        \n\nAtmospheric Trace Gases:\n\nTotal Ozone BurdenTotal Column Precipitable Water Vapor - IR RetrievalTotal Column Precipitable Water Vapor - Direct IR RetrievalWater Vapor(Low &amp; High)Retrieved Water Vapour Mixing Ratio Profile                        Quality Assurance &amp; Statistical Parameters:Quality Assurance Parameters Run time QA flags MODIS Cloud Mask Processing Flag                        These parameters are very essential in the characterization of the atmosphere, atmospheric correction of remotely sensed surface parameters, and prediction of convective clouds and thunderstorms.                       \n\nFor more information about the MOD07_L2 product, visit the MODIS-Atmosphere site at:\n\nhttps://modis-atmos.gsfc.nasa.gov/products/atm-profile",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km - NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The level-2 MODIS Temperature and Water Vapor Profile Product MOD07_L2 consists of 30 gridded parameters related to atmospheric stability, atmospheric temperature and moisture profiles, total atmospheric water vapor, and total ozone. All of these parameters are produced for both daytime and nighttime conditions at 5-km pixel resolution when at least 9 FOVs are cloud free.                        \n\nThe atmospheric profiles are produced at 20 vertical atmospheric levels (5., 10., 20., 30., 50., 70., 100., 150., 200., 250., 300., 400., 500., 620., 700., 780., 850., 920., 950., 1000. mbar) The water vapor parameter is an estimate of the total tropospheric column water vapor made from integrated MODIS infrared retrievals of atmospheric moisture profiles in clear scenes. The thermal band 9.6 micron is used for retrieving total ozone burden.                        \n\nThe shortname for this Level-2 MODIS atmospheric profile product is MOD07_L2 and the principal investigator for this product is MODIS scientist Dr. Paul Menzel ( paulm@ssec.wisc.edu).The MODIS atmospheric profile (MOD07_L2) product contains data that has a spatial resolution (pixel size) of 5 x 5 kilometers (at nadir). Each MOD07_L2 product file covers a five-minute time interval, which means the MOD07_L2 output grid is 270 5-km pixels in width and 406 5-km pixels in length for nine consecutive granules. Every tenth granule has an output grid size of 270 by 408 pixels.\n\nMOD07_L2 product files are stored in Hierarchical Data Format(HDF-EOS). Twenty eight of the 30 gridded cloud parameters(5-kilometer pixel resolution) are stored as Scientific Data Sets (SDS) within the file, the remaining two algorithmic static parameters (band number and presure level) are stored as Vdata(table arrays). Cloud Mask SDS, derived from the 1-km MOD35_L2 Cloud Mask parameter, is remapped to 5-km resolution, by using only the center 1-km pixel in the 5x5 pixel retrieval array. The remaining two (band number and static pressure levels) are stored as Vdata(table arrays) Each file is roughly 8 MB in size, and the total data volume is approximately 2 GB/day.\nMOD07_L2 Data Group and Parameters:                         Spatial &amp; Temporal Resolution:\nLatitude &amp; LongitudeScan start time\n\nSolar and Sensor Viewing Geometry:\n\nSolar zenith &amp; Solar azimuth angleSensor zenith &amp; Sensor azimuth angle\n\nStatic Algorithm Parameters:\nMODIS band number; Pressure levels Atmospheric &amp; \n\nSurface Pressure:\n\nRetrieved Geopotential Height ProfileTropopause HeightSurface Elevation, Surface Pressure                        Atmospheric &amp; Surface Temperature:Guess &amp; Retrieved Temperature ProfilesBrightness Temperature and Skin Temperature\n\nAtmospheric Moisture:\n\nGuess Mixing ratio ProfileRetrieved Dew Point Temperature Profile\nAtmospheric Stability Indices:\n\nTotal Totals, Lifted Index, and K-index                        \n\nAtmospheric Trace Gases:\n\nTotal Ozone BurdenTotal Column Precipitable Water Vapor - IR RetrievalTotal Column Precipitable Water Vapor - Direct IR RetrievalWater Vapor(Low &amp; High)Retrieved Water Vapour Mixing Ratio Profile                        Quality Assurance &amp; Statistical Parameters:Quality Assurance Parameters Run time QA flags MODIS Cloud Mask Processing Flag                        These parameters are very essential in the characterization of the atmosphere, atmospheric correction of remotely sensed surface parameters, and prediction of convective clouds and thunderstorms.                       \n\nFor more information about the MOD07_L2 product, visit the MODIS-Atmosphere site at:\n\nhttps://modis-atmos.gsfc.nasa.gov/products/atm-profile",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD07_L2.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD07_L2.NRT.061",
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
-                    "description": "Access Collection 6 data set from the MODAPS LANCE-MODIS page(download server).",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6 data set from the MODAPS LANCE-MODIS page(download server).",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/61/MOD07_L2/",
-                    "description": "Direct access to the download site and directory hosting the MOD07_L2 6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MOD07_L2 6.1 NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/61/MOD07_L2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://modis.gsfc.nasa.gov/sci_team/",
-                    "description": "MODIS Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Science Team",
+                    "downloadURL": "http://modis.gsfc.nasa.gov/sci_team/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "identifier": "C1426510452-LANCEMODIS",
+            "issued": "2017-10-11",
+            "keyword": [
+                "atmospheric phenomena",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "national geospatial data asset",
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD07_L2.NRT.061",
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
@@ -697364,317 +697365,294 @@
                 "TERRA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km - NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-ESC1-V2.0",
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
+            "description": "This data set contains CODMAC level 4 science data acquired by the ROSINA COPS sensor between 2014-11-19 and 2015-03-10 during the Escort phase 1 of the Rosetta mission to comet 67P/CG. V2.0: Minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-esc1-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-ESC1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-esc1-v2.0",
-            "description": "This data set contains CODMAC level 4 science data acquired by the ROSINA COPS sensor between 2014-11-19 and 2015-03-10 during the Escort phase 1 of the Rosetta mission to comet 67P/CG. V2.0: Minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 4\n                                      ESC1 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 4\n                                      ESC1 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/387/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-06-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
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
-            "identifier": "DASHLINK_387",
             "description": "The Propulsion IVHM Technology Experiment (PITEX) has been an on-going research effort conducted over several\r\nyears. PITEX has developed and applied a model-based diagnostic system for the main propulsion system of the X-34\r\nreusable launch vehicle, a space-launch technology demonstrator. The application was simulation-based using detailed models of the propulsion subsystem to generate nominal and failure scenarios during captive carry, which is the most safety-critical portion of the X-34 flight. Since no system-level testing of the X-34 Main Propulsion System (MPS) was performed, these simulated data were used to verify and validate the software system. Advanced diagnostic and signal processing algorithms were developed and tested in real-time on flight-like hardware. In an attempt to expose potential performance problems, these PITEX algorithms were subject to numerous real-world effects in the simulated data including noise, sensor resolution, command/valve talkback information, and nominal build variations. The current research has demonstrated the potential benefits of model-based diagnostics, defined the performance metrics required to evaluate the diagnostic system, and studied the impact of real-world challenges encountered when monitoring\r\npropulsion subsystems.",
-            "title": "Addressing the Real-World Challenges in the Development of Propulsion IVHM Technology Experiment (PITEX)",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/AIAA_ISTC_2004.pdf",
-                    "description": "AIAA_ISTC_2004.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "AIAA_ISTC_2004.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/AIAA_ISTC_2004.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AIAA_ISTC_2004.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_387",
+            "issued": "2011-06-07",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/387/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Addressing the Real-World Challenges in the Development of Propulsion IVHM Technology Experiment (PITEX)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "S-NPP VIIRS Science Team. 2021-08-18. VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath IP 375m, 750m. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/VJ109.002. https://doi.org/10.5067/VIIRS/VJ109.002.",
-            "issued": "2022-09-09",
-            "temporal": "2018-01-05T00:00:00Z/2024-11-25T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
-            "keyword": [
-                "surface radiative properties",
-                "earth science",
-                "land surface"
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
-            "identifier": "C2849305562-LAADS",
-            "description": "The VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath 375m, 750m product, with short name VJ109, are estimates of surface reflectance in each of the Visible Infrared Imaging Radiometer Suite (VIIRS) reflective bands I1-I3, M1-M5, M7, M8, M10, and M11.  The VJ109 contains approximately 6 minutes' worth of data. Surface reflectance for each moderate-resolution (750m) or imagery-resolution (375m) pixel is retrieved separately for the Level-2 products. Surface reflectance is obtained by adjusting top-of-atmosphere reflectance to compensate for atmospheric effects. Corrections are made for the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. All surface reflectance products are produced for daytime conditions only. The product is produced under all atmospheric conditions except for night and oceans.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "S-NPP VIIRS Science Team",
-            "title": "VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath 375m, 750m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath 375m, 750m product, with short name VJ109, are estimates of surface reflectance in each of the Visible Infrared Imaging Radiometer Suite (VIIRS) reflective bands I1-I3, M1-M5, M7, M8, M10, and M11.  The VJ109 contains approximately 6 minutes' worth of data. Surface reflectance for each moderate-resolution (750m) or imagery-resolution (375m) pixel is retrieved separately for the Level-2 products. Surface reflectance is obtained by adjusting top-of-atmosphere reflectance to compensate for atmospheric effects. Corrections are made for the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. All surface reflectance products are produced for daytime conditions only. The product is produced under all atmospheric conditions except for night and oceans.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/VJ109.002",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/VJ109.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf",
-                    "description": "Suomi-NPP VIIRS Surface Reflectance User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Suomi-NPP VIIRS Surface Reflectance User's Guide",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/PDF/ATBD_VIIRS_SR_v2.pdf",
-                    "description": "Suomi-NPP VIIRS Surface Reflectance Algorithm Theoretical Basis Document (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "Suomi-NPP VIIRS Surface Reflectance Algorithm Theoretical Basis Document (ATBD)",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/PDF/ATBD_VIIRS_SR_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ109--5200",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ109--5200",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5200/VJ109/",
-                    "description": "Direct access to VNP09 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to VNP09 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5200/VJ109/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/allData/5200/VJ109/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/allData/5200/VJ109/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2849305562-LAADS",
+            "issued": "2022-09-09",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-05T00:00:00Z/2024-11-25T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath 375m, 750m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/DECKLAB/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/DECKLAB/DATA001.",
-            "issued": "1997-09-30",
-            "temporal": "1997-01-03T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "ocean temperature",
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
-            "identifier": "C1633360199-OB_DAAC",
             "description": "Measurements made off the western African coast in 1997.",
-            "title": "Measurements made off the western African coast in 1997",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FDECKLAB%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FDECKLAB%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/DECKLAB/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/DECKLAB/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360199-OB_DAAC",
+            "issued": "1997-09-30",
+            "keyword": [
+                "ocean optics",
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/DECKLAB/DATA001",
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
+            "temporal": "1997-01-03T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements made off the western African coast in 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-SSA-RSS-1-ROCC-V1.0",
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
-                "titan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set consists of raw data collected during the Titan radio occultation of Voyager 1 in November 1980 plus ancillary files that might be useful in analysis of those data.  The raw data are sampled voltage outputs from receivers tuned to the Voyager carrier frequencies at both S-band and X-band during the occultations.  The data have been reduced to give profiles of atmospheric temperature and pressure as a function of height above the surface on both the ingress and egress sides of Titan and to make a marginal detection of an ionosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-ssa-rss-1-rocc-v1.0_eck8-hyus",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-SSA-RSS-1-ROCC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-ssa-rss-1-rocc-v1.0_eck8-hyus",
-            "description": "This data set consists of raw data collected during the Titan radio occultation of Voyager 1 in November 1980 plus ancillary files that might be useful in analysis of those data.  The raw data are sampled voltage outputs from receivers tuned to the Voyager carrier frequencies at both S-band and X-band during the occultations.  The data have been reduced to give profiles of atmospheric temperature and pressure as a function of height above the surface on both the ingress and egress sides of Titan and to make a marginal detection of an ionosphere.",
-            "title": "VOYAGER 1 TITAN RADIO\n                                      OCCULTATION RAW DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 TITAN RADIO\n                                      OCCULTATION RAW DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/WVCC/DATA209",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eric Fetzer, Brian Wilson, and Gerald Manipon. 2018-02-01. AIRS_MLS_IND. Version 1.0. Aqua AIRS-MLS Matchup Indexes V1.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/WVCC/DATA209. https://disc.gsfc.nasa.gov/datacollection/AIRS_MLS_IND_1.0.html. Digital Science Data.",
-            "issued": "2018-01-12",
-            "temporal": "2004-08-08T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-19",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GERALD MANIPON",
                 "hasEmail": "mailto:Geraldjohn.M.Manipon@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1451934338-GES_DISC",
-            "description": "This dataset is part of MEaSUREs 2012 Program, and represent Aqua/AIRS-Aura/MLS collocation indexes, in netCDF-4  format. These data map AIRS profile indexes to those of MLS.\n\nThe A-Train provides water vapor (H2O) retrievals from both the Atmospheric Infrared Sounder (AIRS) and Microwave Limb Sounder (MLS). While AIRS loses sensitivity to H2O at the elevated portions of the upper troposphere (UT), MLS cannot detect H2O below 316 hPa. Therefore, to obtain a full profile of H2O in the whole column of air, this dataset manages to join the two products together by utilizing their own averaging kernels (AK). In doing so, the dataset builds a solid H2O of the whole column of air, which will help understand the H2O budget and many processes governing the humidity around the upper troposphere and lower stratosphere (UTLS).  \n\nThe short name for this collections is AIRS_MLS_IND",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS_MLS_IND",
             "creator": "Eric Fetzer, Brian Wilson, and Gerald Manipon",
-            "title": "Aqua AIRS-MLS Matchup Indexes V1.0 (AIRS_MLS_IND) at GES_DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Fetzer/AIRS_MLS_H2O.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This dataset is part of MEaSUREs 2012 Program, and represent Aqua/AIRS-Aura/MLS collocation indexes, in netCDF-4  format. These data map AIRS profile indexes to those of MLS.\n\nThe A-Train provides water vapor (H2O) retrievals from both the Atmospheric Infrared Sounder (AIRS) and Microwave Limb Sounder (MLS). While AIRS loses sensitivity to H2O at the elevated portions of the upper troposphere (UT), MLS cannot detect H2O below 316 hPa. Therefore, to obtain a full profile of H2O in the whole column of air, this dataset manages to join the two products together by utilizing their own averaging kernels (AK). In doing so, the dataset builds a solid H2O of the whole column of air, which will help understand the H2O budget and many processes governing the humidity around the upper troposphere and lower stratosphere (UTLS).  \n\nThe short name for this collections is AIRS_MLS_IND",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWVCC%2FDATA209",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWVCC%2FDATA209",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -697684,10 +697662,10 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS_MLS_IND_1.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS_MLS_IND_1.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -697697,10 +697675,10 @@
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS_MLS_IND",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS_MLS_IND",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -697716,380 +697694,379 @@
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Fetzer/AIRS_MLS_H2O.jpg",
+            "identifier": "C1451934338-GES_DISC",
+            "issued": "2018-01-12",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/WVCC/DATA209",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-01-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRS_MLS_IND",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-08T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua AIRS-MLS Matchup Indexes V1.0 (AIRS_MLS_IND) at GES_DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA207",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-01-15. AIRX2SUP. Version 006. AIRS/Aqua L2 Support Retrieval (AIRS+AMSU) V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA207. https://disc.gsfc.nasa.gov/datacollection/AIRX2SUP_006.html. Digital Science Data.",
-            "issued": "2002-08-30",
-            "temporal": "2002-08-30T00:00:00Z/2016-09-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-24",
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
-                "atmospheric radiation",
-                "surface radiative properties",
-                "spectral/engineering",
-                "surface thermal properties",
-                "air quality",
-                "precipitation",
-                "ocean temperature",
-                "altitude",
-                "oceans",
-                "microwave",
-                "land surface",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1243477317-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The Support Product includes higher vertical resolution profiles of the quantities found in the Standard Product plus intermediate output (e.g., microwave-only retrieval), research products such as the abundance of trace gases, and detailed quality assessment information. The Support Product profiles contain 100 pressure levels between 1100 and .016 mb; this higher resolution simplifies the generation of radiances using forward models, though the vertical information content is no greater than in the Standard Product profiles. The horizontal resolution is 50 km. The intended users of the Support Product are researchers interested in generating forward radiance, or in examining research products, and the AIRS algorithm development team. The Support Product is generated at all locations as Standard Products. An AIRS granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRX2SUP",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "graphic-preview-description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS+AMSU) H2O Column Density Profile and Cloud Fraction.",
-            "title": "AIRS/Aqua L2 Support Retrieval (AIRS+AMSU) V006 (AIRX2SUP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX2SUP_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA207",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA207",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX2SUP_006.png",
-                    "description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS+AMSU) H2O Column Density Profile and Cloud Fraction.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS+AMSU) H2O Column Density Profile and Cloud Fraction.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX2SUP_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX2SUP_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX2SUP_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRX2SUP.006/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRX2SUP.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRX2SUP.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRX2SUP.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX2SUP+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX2SUP+006",
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
+            "graphic-preview-description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS+AMSU) H2O Column Density Profile and Cloud Fraction.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX2SUP_006.png",
+            "identifier": "C1243477317-GES_DISC",
+            "issued": "2002-08-30",
+            "keyword": [
+                "clouds",
+                "atmospheric radiation",
+                "surface radiative properties",
+                "spectral/engineering",
+                "surface thermal properties",
+                "air quality",
+                "precipitation",
+                "ocean temperature",
+                "altitude",
+                "oceans",
+                "microwave",
+                "land surface",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA207",
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
+            "series-name": "AIRX2SUP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2016-09-24T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L2 Support Retrieval (AIRS+AMSU) V006 (AIRX2SUP) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TNO-PHOT-V3.0",
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
+            "description": "This data set is a collection of all published colors of trans-Neptunian objects published through the indicated nstop date. This data set is updated annually.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-tno-phot-v3.0_ecq3-uzkq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TNO-PHOT-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-tno-phot-v3.0_ecq3-uzkq",
-            "description": "This data set is a collection of all published colors of trans-Neptunian objects published through the indicated nstop date. This data set is updated annually.",
-            "title": "TRANS-NEPTUNIAN OBJECT PHOTOMETRY V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TRANS-NEPTUNIAN OBJECT PHOTOMETRY V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-5-TPS-V1.0",
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
+            "description": "This data set contains over 21000 temperature-pressure profiles (TPS files) of the neutral atmosphere derived from Mars Global Surveyor (MGS) radio occultation data. The profiles were previously archived in the MGS-M-RSS-5-SDP-V1.0 data set along with other reduced data products from the MGS Radio Science Team (RST). Here they have been pulled from the original 38 volumes and reorganized in chronological order on a single volume. The profiles themselves have not been modified, and the labels have been edited only to conform with the requirements of the new data set. This set of profiles is accompanied by a single occultation summary file which lists key characteristics of each experiment.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-5-tps-v1.0_ecqi-29b4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-5-TPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-5-tps-v1.0_ecqi-29b4",
-            "description": "This data set contains over 21000 temperature-pressure profiles (TPS files) of the neutral atmosphere derived from Mars Global Surveyor (MGS) radio occultation data. The profiles were previously archived in the MGS-M-RSS-5-SDP-V1.0 data set along with other reduced data products from the MGS Radio Science Team (RST). Here they have been pulled from the original 38 volumes and reorganized in chronological order on a single volume. The profiles themselves have not been modified, and the labels have been edited only to conform with the requirements of the new data set. This set of profiles is accompanied by a single occultation summary file which lists key characteristics of each experiment.",
-            "title": "MGS RS: ATMOSPHERIC TEMPERATURE-PRESSURE PROFILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS RS: ATMOSPHERIC TEMPERATURE-PRESSURE PROFILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1529927432-GES_DISC.html",
             "citation": "NASA/GSFC. 2018-06-15. SCRN5L1RAD. Version 001. SCR/Nimbus-5 Level 1 Calibrated Radiances V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/SCRN5L1RAD_001.html. Digital Science Data.",
-            "issued": "1998-02-24",
-            "temporal": "1972-12-13T00:00:00Z/1974-12-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-02-24",
-            "references": [
-                "https://doi.org/10.1098/rspa.1973.0085"
-            ],
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
-            "identifier": "C1529927432-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "SCRN5L1RAD is the Nimbus-5 Selective Chopper Radiometer (SCR) Level 1 Calibrated Radiances data product. The calibrated radiances are measured at 16 channels from 2.3 to 133 micrometers with a ground resolution of 25 km, and are \"declouded\" (interpolated and smoothed across regions of cloud). The radiances were used to obtain the global temperature structure of the atmosphere up to 50 km altitude, the distribution of water vapor, and the density of ice particles in cirrus clouds. The data were recovered from the original 9-track tapes, and are now stored online as daily files in their original proprietary binary format with about 14 orbits per day.\n\nSpatial coverage is near global from latitude -80 to +80 degrees. The data are available from 13 December 1972 (day of year 347) to 26 December 1974 (day of year 360). The principal investigator for the SCR experiment was Dr. John T. Houghton from Oxford University.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00250 (old ID 72-097A-02A).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SCRN5L1RAD",
-            "creator": "NASA/GSFC",
-            "graphic-preview-description": "Typical data coverage of a Nimbus 5 SCR Level 1 daily data file.",
-            "title": "SCR/Nimbus-5 Level 1 Calibrated Radiances V001 (SCRN5L1RAD) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/SCRN5L1RAD_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/SCRN5L1RAD_Sample.png",
-                    "description": "Typical data coverage of a Nimbus 5 SCR Level 1 daily data file.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical data coverage of a Nimbus 5 SCR Level 1 daily data file.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/SCRN5L1RAD_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCRN5L1RAD_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCRN5L1RAD_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_SCR_Level1/SCRN5L1RAD.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_SCR_Level1/SCRN5L1RAD.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SCRN5L1RAD",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SCRN5L1RAD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_SCR_Level1/SCRN5L1RAD.001/doc/README.SCRN5L1RAD.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_SCR_Level1/SCRN5L1RAD.001/doc/README.SCRN5L1RAD.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.2_Product_Rqmts_Design/N5_SCR_onN5.pdf",
-                    "description": "The Selective Chopper Radiometer on Nimbus V Archived Data",
                     "@type": "dcat:Distribution",
+                    "description": "The Selective Chopper Radiometer on Nimbus V Archived Data",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.2_Product_Rqmts_Design/N5_SCR_onN5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/NIMBUS/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus5.tar.gz",
-                    "description": "Nimbus 5 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 5 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/NIMBUS/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus5.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N5_SCR_Inventory.xlsx",
-                    "description": "N5 SCR Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N5 SCR Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N5_SCR_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Typical data coverage of a Nimbus 5 SCR Level 1 daily data file.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/SCRN5L1RAD_Sample.png",
+            "identifier": "C1529927432-GES_DISC",
+            "issued": "1998-02-24",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1529927432-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1998-02-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1098/rspa.1973.0085"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SCRN5L1RAD",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "1972-12-13T00:00:00Z/1974-12-26T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SCR/Nimbus-5 Level 1 Calibrated Radiances V001 (SCRN5L1RAD) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/cassini",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/cassini/main/index.html"
-            ],
-            "keyword": [
-                "cassini-huygens mission",
-                "vehicles",
-                "orbiter",
-                "cassini",
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
-            "identifier": "NASA-325",
             "description": "Cassini spacecraft from SPACE rendering package, built by Michael Oberle under NASA contract at JPL. Includes orbiter only, Huygens probe detached. Accurate except no thermal blanketing is shown (this would cover most of the central structure of the spacecraft). Polygons: 9956 Vertices: 8130",
-            "title": "NASA 3D Models: Cassini",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -698097,154 +698074,179 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-325",
+            "issued": "2018-06-25",
+            "keyword": [
+                "cassini-huygens mission",
+                "vehicles",
+                "orbiter",
+                "cassini",
+                "3d model"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/cassini",
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
+                "http://www.nasa.gov/mission_pages/cassini/main/index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Cassini"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2012",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Feng, M., J.O. Sexton, P. Wang, S. Channan, P.M. Montesano, W. Wagner, M.R. Wooten, and C.S. Neigh. 2022. ABoVE: Tree Canopy Cover and Stand Age from Landsat, Boreal Forest Biome, 1984-2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2012",
-            "issued": "2022-12-02",
-            "temporal": "1984-01-01T00:00:00Z/2020-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
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
-            "identifier": "C2539841646-ORNL_CLOUD",
             "description": "This dataset contains Landsat-derived locally-calibrated estimates of tree canopy cover (TCC) and forest stand age across global boreal forests from 1984-2020 in Cloud-Optimized GeoTIFF (*.tif) format. These raster data span the circum-hemispheric boreal forest biome between 47 to 73 degrees north at 30 m resolution. Machine learning models calibrated with data from the World Reference System 2 were used to predict TCC from Landsat data at 30-m spatial resolution at annual temporal resolution. Through analysis of TCC time series, forest change estimates of stand age from 1984-2020 were developed. The broad spatial and temporal coverage of these data provide insight into forest and carbon dynamics of the global boreal forest system. Boreal forests store a large proportion of global soil and biomass carbon and have experienced disproportionately high levels of warming over the past century.",
-            "graphic-preview-description": "Tree canopy cover over global boreal forests in 2020.",
-            "title": "ABoVE: Tree Canopy Cover and Stand Age from Landsat, Boreal Forest Biome, 1984-2020",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Boreal_CanopyCover_StandAge_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2012",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2012",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Boreal_CanopyCover_StandAge/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Boreal_CanopyCover_StandAge/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Boreal_CanopyCover_StandAge.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Boreal_CanopyCover_StandAge.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2012",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2012",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Boreal_CanopyCover_StandAge/comp/Boreal_CanopyCover_StandAge.pdf",
-                    "description": "ABoVE: Tree Canopy Cover and Stand Age from Landsat, Boreal Forest Biome, 1984-2020: Boreal_CanopyCover_StandAge.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Tree Canopy Cover and Stand Age from Landsat, Boreal Forest Biome, 1984-2020: Boreal_CanopyCover_StandAge.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Boreal_CanopyCover_StandAge/comp/Boreal_CanopyCover_StandAge.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Boreal_CanopyCover_StandAge_Fig1.png",
-                    "description": "Tree canopy cover over global boreal forests in 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "Tree canopy cover over global boreal forests in 2020.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Boreal_CanopyCover_StandAge_Fig1.png",
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
+            "graphic-preview-description": "Tree canopy cover over global boreal forests in 2020.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Boreal_CanopyCover_StandAge_Fig1.png",
+            "identifier": "C2539841646-ORNL_CLOUD",
+            "issued": "2022-12-02",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "biosphere",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2012",
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
             "spatial": "-180.0 45.0 180.0 73.0",
+            "temporal": "1984-01-01T00:00:00Z/2020-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Tree Canopy Cover and Stand Age from Landsat, Boreal Forest Biome, 1984-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-EXT2-V1.0",
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
+            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the mission extension 2 (EXT2). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 06 Apr 2016 and 30 Jun 2016.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-ext2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-EXT2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-ext2-v1.0",
-            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the mission extension 2 (EXT2). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 06 Apr 2016 and 30 Jun 2016.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 3 EXT2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 3 EXT2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-POS-6-SC-TRAJ-JUP-COORDS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains the Galileo spacecraft trajectory data in three coordinate systems commonly used in the analysis of jovian magnetospheric data. These include System III (1965.0), Jupiter Solar Equatorial (JSE), and Jupiter Solar Magnetospheric (JSM) coordinates. The data are sampled every minute inside of 30 Jupiter radii, every ten minutes between 30 and 100 Rj, and every 30 minutes outside of 100 Rj. The data are derived from SPICE SP kernels which are archived at the NAIF Node of the PDS.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pos-6-sc-traj-jup-coords-v1.0_ed28-7hp2",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "io plasma torus",
                 "europa",
@@ -698255,57 +698257,36 @@
                 "ganymede",
                 "callisto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-POS-6-SC-TRAJ-JUP-COORDS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pos-6-sc-traj-jup-coords-v1.0_ed28-7hp2",
-            "description": "This data set contains the Galileo spacecraft trajectory data in three coordinate systems commonly used in the analysis of jovian magnetospheric data. These include System III (1965.0), Jupiter Solar Equatorial (JSE), and Jupiter Solar Magnetospheric (JSM) coordinates. The data are sampled every minute inside of 30 Jupiter radii, every ten minutes between 30 and 100 Rj, and every 30 minutes outside of 100 Rj. The data are derived from SPICE SP kernels which are archived at the NAIF Node of the PDS.",
-            "title": "GO JUP POS GLL TRAJECTORY JUPITER CENTERED COORDINATES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUP POS GLL TRAJECTORY JUPITER CENTERED COORDINATES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ed33-vxp2",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2022-10-20",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-20",
-            "keyword": [
-                "prognostics",
-                "degradation",
-                "phm",
-                "batteries"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Christopher Teubert",
                 "hasEmail": "mailto:Christopher.A.Teubert@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "PCoE"
-            },
-            "identifier": "https://data.nasa.gov/api/views/ed33-vxp2",
             "description": "This dataset is part of a series of datasets, where batteries are continuously cycled with randomly generated current profiles. Reference charging and discharging cycles are also performed after a fixed interval of randomized usage to provide reference benchmarks for battery state of health.\n\nIn this dataset, four 18650 Li-ion batteries (Identified as RW1, RW2, RW7 and RW8) were continuously operated by repeatedly discharging them to 3.2V using a randomized sequence of discharging currents between 0.5A and 4A. This type of discharging profile is referred to here as random walk (RW) discharging. After each discharging cycle the batteries were charged for a randomly selected duration between 0.5 hours and 3 hours. After every fifty RW cycles a series of reference charging and discharging cycles were performed in order to provide reference benchmarks for battery state health.",
-            "title": "Randomized Battery Usage 3: Room Temperature Variable Recharge Random Walk",
-            "programCode": [
-                "026:021"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -698313,1592 +698294,1589 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/ed33-vxp2",
+            "issued": "2022-10-20",
+            "keyword": [
+                "prognostics",
+                "degradation",
+                "phm",
+                "batteries"
+            ],
+            "landingPage": "https://data.nasa.gov/d/ed33-vxp2",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-10-20",
+            "programCode": [
+                "026:021"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "PCoE"
+            },
             "theme": [
                 "Raw Data"
-            ]
+            ],
+            "title": "Randomized Battery Usage 3: Room Temperature Variable Recharge Random Walk"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/887",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schroeder, W., and J.T. Morisette. 2008. LBA-ECO LC-23 Vegetation Fire Data, Roraima , Brazil: 2003. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/887",
-            "issued": "2023-10-03",
-            "temporal": "2003-01-19T00:00:00Z/2003-01-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "land surface",
-                "national geospatial data asset",
-                "ngda",
-                "surface thermal properties",
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
-            "identifier": "C2777369007-ORNL_CLOUD",
             "description": "This data set contains ASTER sensor Level-1B satellite imagery over controlled burns in the State of Roraima in Northern Brazil on January 19 and 28, 2003, plus simultaneously collected soil and near-surface air temperature profiles on January 28th. The ASTER imagery is provided in 14 zipped files containing HDF-EOS files (*.hdf and *.met file pairs), while the sample-based temperature profiles, one for the air the other for the ground, are provided as comma separated ASCII files.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-23 Vegetation Fire Data, Roraima , Brazil: 2003",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F887",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F887",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC23_Vegetation_Fires_2003/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC23_Vegetation_Fires_2003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC23_Vegetation_Fires_2003.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC23_Vegetation_Fires_2003.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/887",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/887",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fires_2003/comp/ASTER_GeoRef_FINAL.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fires_2003/comp/ASTER_GeoRef_FINAL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fires_2003/comp/aster_user_guide_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fires_2003/comp/aster_user_guide_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fires_2003/comp/LC23_Vegetation_Fires_2003.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fires_2003/comp/LC23_Vegetation_Fires_2003.pdf",
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
+            "identifier": "C2777369007-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "land surface",
+                "national geospatial data asset",
+                "ngda",
+                "surface thermal properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/887",
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
             "spatial": "-63.0 0.0 -60.0 5.0",
+            "temporal": "2003-01-19T00:00:00Z/2003-01-28T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-23 Vegetation Fire Data, Roraima , Brazil: 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/785/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
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
-            "identifier": "DASHLINK_785",
             "description": "A remaining useful life prediction methodology for elec- trolytic capacitors is presented. This methodology is based on the Kalman filter framework and an empirical degradation model. Electrolytic capacitors are used in several applications ranging from power supplies on critical avionics equipment to power drivers for electro-mechanical actuators. These devices are known for their comparatively low reliability and given their criticality in electronics subsystems they are a good can- didate for component level prognostics and health manage- ment. Prognostics provides a way to assess remaining use- ful life of a capacitor based on its current state of health and its anticipated future usage and operational conditions. We present here also, experimental results of an accelerated ag- ing test under electrical stresses. The data obtained in this test form the basis for a remaining life prediction algorithm where a model of the degradation process is suggested. This prelim- inary remaining life prediction algorithm serves as a demon- stration of how prognostics methodologies could be used for electrolytic capacitors. In addition, the use degradation pro- gression data from accelerated aging, provides an avenue for validation of applications of the Kalman filter based prognos- tics methods typically used for remaining useful life predic- tions in other applications.",
-            "title": "A Model-based Prognostics Methodology for Electrolytic Capacitors Based on Electrical Overstress Accelerated Aging",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_PHM_Capacitor.pdf",
-                    "description": "2011_PHM_Capacitor.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2011_PHM_Capacitor.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_PHM_Capacitor.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2011_PHM_Capacitor.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_785",
+            "issued": "2013-06-19",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/785/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Model-based Prognostics Methodology for Electrolytic Capacitors Based on Electrical Overstress Accelerated Aging"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67PCHURYUMOV-M27-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the ROSETTA EXTENSION 1 phase of the Rosetta mission, covering the period from 2016-03-08T23:25:00.000 to 2016-04-05T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67pchuryumov-m27-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67PCHURYUMOV-M27-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67pchuryumov-m27-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the ROSETTA EXTENSION 1 phase of the Rosetta mission, covering the period from 2016-03-08T23:25:00.000 to 2016-04-05T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP027 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP027 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/CERES/ISCCP-D2LIKE-DAY_TERRA_L3.003A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2013-11-26. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/CERES/ISCCP-D2LIKE-DAY_TERRA_L3.003A.",
-            "issued": "2013-12-18",
-            "temporal": "2000-03-01T00:00:00Z/2006-02-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-19",
-            "keyword": [
-                "land surface",
-                "atmosphere",
-                "clouds",
-                "national geospatial data asset",
-                "earth science",
-                "ngda",
-                "atmospheric radiation",
-                "aerosols",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID DOELLING",
                 "hasEmail": "mailto:david.r.doelling@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C7017993-LARC_ASDC",
             "description": "CER_ISCCP-D2like-Day_Terra-FM2-MODIS_Edition3A is the Clouds and the Earth's Radiant Energy System (CERES) Moderate Resolution Imaging Spectroradiometer (MODIS) Cloud Retrievals in International Satellite Cloud Climatology Project (ISCCP)-Day 2 like Format Daytime Terra Flight Model (FM2) Edition 3A data product, which was collected using the CERES-FM2 and MODIS instruments on the Terra platform. Data collection for this product is complete.\r\n\r\nThe Monthly Gridded Cloud Averages (ISCCP-D2like-Day) data product contains monthly and monthly 3-hourly (GMT-based) gridded regional mean CERES MODIS-derived cloud properties as a function of 18 cloud types, similar to the ISCCP D2 product, where the cloud properties are stratified by pressure, optical depth, and phase. There are separate daytime and nighttime data sets for both Terra-MODIS and Aqua-MODIS. The retrievals, and therefore the quality, are different for each data set. The CERES MODIS-derived cloud properties are not the official NASA MODIS cloud retrievals but are based on the CERES cloud working group retrievals that are also available in other CERES products. The CERES MODIS-derived cloud properties have coverage from pole to pole. For these MODIS-based ISCCP-D2like products, the cloud fractions for 42 cloud types, similar to the ISCCP D1 product, are also available. The Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF) data product is the input to this product. Each ISCCP-D2like file covers a single month.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES MODIS Cloud Retrievals in ISCCP-D2like Format Day Terra FM2 Edition3A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FISCCP-D2LIKE-DAY_TERRA_L3.003A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FISCCP-D2LIKE-DAY_TERRA_L3.003A",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/ISCCP-D2LIKE-DAY_TERRA_L3.003A",
-                    "description": "DOI data set landing page for CER_ISCCP-D2like-Day_Terra-FM1/2-MODIS_Edition3A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_ISCCP-D2like-Day_Terra-FM1/2-MODIS_Edition3A",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/ISCCP-D2LIKE-DAY_TERRA_L3.003A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7017993-LARC_ASDC",
-                    "description": "Earthdata Search for CER_ISCCP-D2like-Day_Terra-FM2-MODIS_Edition3A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_ISCCP-D2like-Day_Terra-FM2-MODIS_Edition3A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7017993-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_isccp-d2like.pdf",
-                    "description": "CERES Monthly Gridded Cloud Averages (ISCCP-D2like-Day/Nit) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Monthly Gridded Cloud Averages (ISCCP-D2like-Day/Nit) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_isccp-d2like.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ISCCP-D2like_Edition3A.pdf",
-                    "description": "Quality Summary: CERES_ISCCP-D2like_Ed3A (11/14/2013)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_ISCCP-D2like_Ed3A (11/14/2013)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ISCCP-D2like_Edition3A.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ISCCP-D2like-Day-Nit_R5V3.pdf",
-                    "description": "CERES Data Products Catalog R5V3 11/27/2013 Monthly Gridded Cloud Averages (ISCCP-D2like-Day/Nit)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R5V3 11/27/2013 Monthly Gridded Cloud Averages (ISCCP-D2like-Day/Nit)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ISCCP-D2like-Day-Nit_R5V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/TISAgrid_SampleRead_ISCCP-D2like-DayNit-986.txt",
-                    "description": "Readme Information on the CER_ISCCP-D2like-Day Edition 3A Data Sets",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information on the CER_ISCCP-D2like-Day Edition 3A Data Sets",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/TISAgrid_SampleRead_ISCCP-D2like-DayNit-986.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/TISAgrid_SampleRead_ISCCP-D2like-DayNit_R5-986.zip",
-                    "description": "Read Software Package - ISCCP-D2like-DayNit_R5-986 - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - ISCCP-D2like-DayNit_R5-986 - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/TISAgrid_SampleRead_ISCCP-D2like-DayNit_R5-986.zip",
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
-                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#aqua",
-                    "description": "CERES Overview of Aqua",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of Aqua",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#aqua",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#trmm",
-                    "description": "CERES Overview of TRMM",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of TRMM",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#trmm",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/input_datasets_for_Edition3A.pdf",
-                    "description": "CERES Input Data Sets (2000-2010)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Input Data Sets (2000-2010)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/input_datasets_for_Edition3A.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ISCCP-D2like-Day/Terra-FM2-MODIS_Edition3A/",
-                    "description": "ASDC Direct Data Download for CER_ISCCP-D2like-Day_Terra-FM2-MODIS_Edition3A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_ISCCP-D2like-Day_Terra-FM2-MODIS_Edition3A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ISCCP-D2like-Day/Terra-FM2-MODIS_Edition3A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ISCCP-D2like-Day/Terra-FM2-MODIS_Edition3A/contents.html",
-                    "description": "OPeNDAP data access for CER_ISCCP-D2like-Day_Terra-FM2-MODIS_Edition3A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_ISCCP-D2like-Day_Terra-FM2-MODIS_Edition3A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ISCCP-D2like-Day/Terra-FM2-MODIS_Edition3A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C7017993-LARC_ASDC",
+            "issued": "2013-12-18",
+            "keyword": [
+                "land surface",
+                "atmosphere",
+                "clouds",
+                "national geospatial data asset",
+                "earth science",
+                "ngda",
+                "atmospheric radiation",
+                "aerosols",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/CERES/ISCCP-D2LIKE-DAY_TERRA_L3.003A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-03-01T00:00:00Z/2006-02-28T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES MODIS Cloud Retrievals in ISCCP-D2like Format Day Terra FM2 Edition3A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-X-UVIS-2-WAV-V1.0",
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
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Imaging of the Saturn system at a wavelength in the far or extreme ultraviolet.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-x-uvis-2-wav-v1.0_edcu-hk6a",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-X-UVIS-2-WAV-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-x-uvis-2-wav-v1.0_edcu-hk6a",
-            "description": "Imaging of the Saturn system at a wavelength in the far or extreme ultraviolet.",
-            "title": "CASSINI ORBITER N/A UVIS IMAGE AT ONE WAVELENGTH",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER N/A UVIS IMAGE AT ONE WAVELENGTH"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-5-SGS-V1.0",
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
+            "description": "The ODY MARS GAMMA RAY SPECTROMETER 5 SGS (SGS) data set is a collection of data tables that contain a gamma spectrum and the associated engineering data that has been summed over 5-degree by 5-degree latitude longitude cells on the surface of Mars and over a time period of 15 degrees of solar longitude (Ls). The SGS are produced because the individual gamma spectra collected during an approximately 19.7 second collection interval do not contain enough counts to be statistically significant. The SGS are summed over large enough and long enough spatial and temporal intervals to provide a statistically meaningful spectrum that can be used for scientific data analysis.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-5-sgs-v1.0_edeh-mpxd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "2001 mars odyssey",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-5-SGS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-5-sgs-v1.0_edeh-mpxd",
-            "description": "The ODY MARS GAMMA RAY SPECTROMETER 5 SGS (SGS) data set is a collection of data tables that contain a gamma spectrum and the associated engineering data that has been summed over 5-degree by 5-degree latitude longitude cells on the surface of Mars and over a time period of 15 degrees of solar longitude (Ls). The SGS are produced because the individual gamma spectra collected during an approximately 19.7 second collection interval do not contain enough counts to be statistically significant. The SGS are summed over large enough and long enough spatial and temporal intervals to provide a statistically meaningful spectrum that can be used for scientific data analysis.",
-            "title": "ODY MARS GAMMA RAY SPECTROMETER 5 SGS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ODY MARS GAMMA RAY SPECTROMETER 5 SGS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC23-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC23) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 2, 12, 28, and on December 5 and 19, 2016, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc23-v1.0_edg4-66cd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC23-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc23-v1.0_edg4-66cd",
-            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC23) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 2, 12, 28, and on December 5 and 19, 2016, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC23 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SROC23 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast.delbo.radiometric-diameters-albedos&version=1.0",
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
+            "description": "This data set contains radiometric       albedos and diameters for Near Earth Asteroids (NEAs) derived by three different thermal models and reported in Delbo (2004) [DELBO2004].     The observed infrared fluxes on which the derivations were based are   also included.",
+            "identifier": "urn:nasa:pds:ast.delbo.radiometric-diameters-albedos",
+            "issued": "2021-05-21",
+            "keyword": [
+                "multiple asteroids",
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast.delbo.radiometric-diameters-albedos&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ast.delbo.radiometric-diameters-albedos",
-            "description": "This data set contains radiometric       albedos and diameters for Near Earth Asteroids (NEAs) derived by three different thermal models and reported in Delbo (2004) [DELBO2004].     The observed infrared fluxes on which the derivations were based are   also included.",
-            "title": "DELBO THERMAL INFRARED ASTEROID DIAMETERS AND ALBEDOS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DELBO THERMAL INFRARED ASTEROID DIAMETERS AND ALBEDOS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-2LRNUR-F08",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2023-07-31. Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Reduced Ocean Surface Topography (Unvalidated) F08. Version F08. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-2LRNUR-F08.",
-            "issued": "2020-12-17",
-            "temporal": "2020-11-30T14:26:00.843Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "earth science",
-                "oceans",
-                "sea surface topography",
-                "ocean waves"
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
-            "identifier": "C2619444006-POCLOUD",
-            "description": "Provides low resolution (LR) non-time critical (NTC; 60-day latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed. The NTC product is analogous to the Jason-3 GDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Reduced Ocean Surface Topography (Unvalidated) F08",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08_UNVALIDATED.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides low resolution (LR) non-time critical (NTC; 60-day latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed. The NTC product is analogous to the Jason-3 GDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LRNUR-F08",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LRNUR-F08",
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
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08_UNVALIDATED",
-                    "description": "Data Set Landing Page",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08_UNVALIDATED",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08_UNVALIDATED.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08_UNVALIDATED.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619444006-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619444006-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619444006-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619444006-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08_UNVALIDATED.jpg",
+            "identifier": "C2619444006-POCLOUD",
+            "issued": "2020-12-17",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "sea surface topography",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-2LRNUR-F08",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-03",
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
+            "temporal": "2020-11-30T14:26:00.843Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Reduced Ocean Surface Topography (Unvalidated) F08"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/316",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ryan, M.G., and M. Lavigne. 1999. BOREAS TE-02 Root Respiration Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/316",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-28T00:00:00Z/1994-09-12T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "soils",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
-                "land surface",
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
-            "identifier": "C2807653050-ORNL_CLOUD",
             "description": "Contains fine root respiration data collected by TE-02.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-02 Root Respiration Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F316",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F316",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te2rtrsp/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te2rtrsp/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE02_Root_Resp.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE02_Root_Resp.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/316",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/316",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2rtrsp/comp/TE02_Root_Resp.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2rtrsp/comp/TE02_Root_Resp.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2rtrsp/comp/TE02_Root_Resp.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2rtrsp/comp/TE02_Root_Resp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2rtrsp/comp/TE02_Root_Resp.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2rtrsp/comp/TE02_Root_Resp.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2rtrsp/comp/te2rtrsp.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2rtrsp/comp/te2rtrsp.def",
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
+            "identifier": "C2807653050-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "soils",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "land surface",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/316",
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
             "spatial": "-98.67 55.88 -98.48 55.93",
+            "temporal": "1994-05-28T00:00:00Z/1994-09-12T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-02 Root Respiration Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/665",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "White, M. A., G. P. Asner, R. R. Nemani, J. L. Privette, and S. W. Running. 2003. PROVE Land Cover and Leaf Area of Jornada Experimental Range, New Mexico, 1997. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/665",
-            "issued": "2023-11-19",
-            "temporal": "1997-05-13T00:00:00Z/1997-05-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "vegetation",
-                "spectral/engineering",
-                "land use/land cover",
-                "visible wavelengths",
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
-            "identifier": "C2804794793-ORNL_CLOUD",
             "description": "Field measurement of shrubland ecological properties is important for both site monitoring and validation of remote-sensing information. During the PROVE exercise on May 20-30, 1997, we calculated plot-level plant area index, leaf area index, total fractional cover, and green fractional cover.",
-            "graphic-preview-description": "Browse Image",
-            "title": "PROVE Land Cover and Leaf Area of Jornada Experimental Range, New Mexico, 1997",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F665",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F665",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/prove/jornada_landcover_lai/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/prove/jornada_landcover_lai/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/PROVE/guides/prove_landcover_lai_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/PROVE/guides/prove_landcover_lai_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/665",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/665",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_landcover_lai/comp/LAI_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_landcover_lai/comp/LAI_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_landcover_lai/comp/prove_landcover_lai_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_landcover_lai/comp/prove_landcover_lai_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_landcover_lai/comp/PROVE_landcover_lai_meas_descriptions.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_landcover_lai/comp/PROVE_landcover_lai_meas_descriptions.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
+            "identifier": "C2804794793-ORNL_CLOUD",
+            "issued": "2023-11-19",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation",
+                "spectral/engineering",
+                "land use/land cover",
+                "visible wavelengths",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/665",
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
             "spatial": "32.5 -106.75",
+            "temporal": "1997-05-13T00:00:00Z/1997-05-31T23:59:59Z",
             "theme": [
                 "PROVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PROVE Land Cover and Leaf Area of Jornada Experimental Range, New Mexico, 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0345-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-09T04:52:05.000 to 2014-10-09T15:28:48.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0345-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0345-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0345-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-09T04:52:05.000 to 2014-10-09T15:28:48.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0345 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0345 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHCMC-4FM02",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Canada Meteorological Center. 2012-11-19. GHRSST Level 4 CMC0.2deg Global Foundation Sea Surface Temperature Analysis (GDS version 2). Version 2.0. CMC 0.2 deg global sea surface temperature analysis. NASA/JPL/PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, Canada Meteorological Center. https://doi.org/10.5067/GHCMC-4FM02. Canada Meteorological Center, Canada Meteorological Center, 2012-11-19, GHRSST Level 4 CMC0.2deg Global Foundation Sea Surface Temperature Analysis (GDS version 2), none.",
-            "issued": "2013-09-23",
-            "temporal": "1991-09-01T00:00:00Z/2017-03-18T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "ocean temperature",
-                "earth science",
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
-            "identifier": "C2499940521-POCLOUD",
-            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) Level 4 sea surface temperature (SST) analysis produced daily on an operational basis at the Canadian Meteorological Center. This dataset merges infrared satellite SST at varying points in the time series from the (A)TSR series of radiometers from ERS-1, ERS-2 and Envisat, AVHRR from NOAA-16,17,18,19 and METOP-A, and microwave data from TMI, AMSR-E and Windsat in conjunction with in situ observations of SST from drifting buoys and ships from the ICOADS program. It uses the previous days analysis as the background field for the statistical interpolation used to assimilate the satellite and in situ observations. This dataset adheres to the GHRSST Data Processing Specification (GDS) version 2 format specifications.",
-            "release-place": "NASA/JPL/PO.DAAC",
-            "series-name": "GHRSST Level 4 CMC0.2deg Global Foundation Sea Surface Temperature Analysis (GDS version 2)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Canada Meteorological Center",
-            "title": "GHRSST Level 4 CMC0.2deg Global Foundation Sea Surface Temperature Analysis (GDS version 2)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CMC0.2deg-CMC-L4-GLOB-v2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) Level 4 sea surface temperature (SST) analysis produced daily on an operational basis at the Canadian Meteorological Center. This dataset merges infrared satellite SST at varying points in the time series from the (A)TSR series of radiometers from ERS-1, ERS-2 and Envisat, AVHRR from NOAA-16,17,18,19 and METOP-A, and microwave data from TMI, AMSR-E and Windsat in conjunction with in situ observations of SST from drifting buoys and ships from the ICOADS program. It uses the previous days analysis as the background field for the statistical interpolation used to assimilate the satellite and in situ observations. This dataset adheres to the GHRSST Data Processing Specification (GDS) version 2 format specifications.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHCMC-4FM02",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHCMC-4FM02",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CMC0.2deg-CMC-L4-GLOB-v2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CMC0.2deg-CMC-L4-GLOB-v2.0.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2499940521-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2499940521-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2499940521-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2499940521-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CMC0.2deg-CMC-L4-GLOB-v2.0.jpg",
+            "identifier": "C2499940521-POCLOUD",
+            "issued": "2013-09-23",
+            "keyword": [
+                "ocean temperature",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHCMC-4FM02",
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
+            "release-place": "NASA/JPL/PO.DAAC",
+            "series-name": "GHRSST Level 4 CMC0.2deg Global Foundation Sea Surface Temperature Analysis (GDS version 2)",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1991-09-01T00:00:00Z/2017-03-18T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 4 CMC0.2deg Global Foundation Sea Surface Temperature Analysis (GDS version 2)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2124",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schmiege, S.C., K. Griffin, N.T. Boleman, L. Vierling, S.G. Bruner, E. Min, A.J. Maguire, J. Jensen, and J. Eitel. 2023. ABoVE: White Spruce Photosynthetic and Leaf Traits, Alaska and New York, 2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2124",
-            "issued": "2023-03-17",
-            "temporal": "2017-06-19T00:00:00Z/2017-07-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "vegetation",
-                "ecosystems",
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
-            "identifier": "C2636355463-ORNL_CLOUD",
             "description": "This dataset provides measurements of gas exchange (light response curves, Kok curves and ACi curves), leaf traits (carbon, nitrogen, and specific leaf area), leaf pigments (Chlorophyll a, Chlorophyll b and Carotenoids), the photochemical reflectance index (PRI), and average photosynthetic photon flux density as collected from hemispherical photographs. Data were collected on white spruce trees (Picea glauca (Moench) Voss) growing at the northern edge of the species' distribution in Alaska and at the southern edge of the species' distribution in Black Rock Forest (BRF), New York. Measurements were taken at high and low canopy positions on each tree at both sites during the 2017 growing season (2017-06-19 to 2017-07-20).  Gas exchange, leaf trait, pigment and spectral measurements were obtained using a portable photosynthesis system (LI-6800, LI-COR, Lincoln, NE). Photochemical reflectance index was determined using a spectroradiometer, and hemispherical photographs were taken with a digital camera. These data were collected to better understand how vertical canopy gradients in photosynthetic physiology change from the southernmost to the northernmost range extremes of white spruce. The data are provided in comma-separated value (CSV) format.",
-            "graphic-preview-description": "Ratios of (a) maximum rate of carboxylation to respiration at 25 degrees C from Griffin et al. (2022) (Vcmax /R25 ) and (b) maximum electron transport rate to respiration at 25 degrees C from Griffin et al. (2022) (Jmax /R25 ) of white spruce from high and low canopy positions at the Forest Tundra Ecotone (FTE, blue), Alaska, and Black Rock Forest (BRF, green), New York. Boxplots show the median and first and third quartiles. Whiskers display the range of groups with individual points representing outliers falling outside 1.5 times the interquartile range. Different letters represent significant differences between locations and canopy positions.",
-            "title": "ABoVE: White Spruce Photosynthetic and Leaf Traits, Alaska and New York, 2017",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/WhiteSpruce_Leaf_Traits_Alaska_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2124",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2124",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/WhiteSpruce_Leaf_Traits_Alaska/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/WhiteSpruce_Leaf_Traits_Alaska/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/WhiteSpruce_Leaf_Traits_Alaska.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/WhiteSpruce_Leaf_Traits_Alaska.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2124",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2124",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/WhiteSpruce_Leaf_Traits_Alaska/comp/WhiteSpruce_Leaf_Traits_Alaska.pdf",
-                    "description": "ABoVE: White Spruce Photosynthetic and Leaf Traits, Alaska and New York, 2017: WhiteSpruce_Leaf_Traits_Alaska.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: White Spruce Photosynthetic and Leaf Traits, Alaska and New York, 2017: WhiteSpruce_Leaf_Traits_Alaska.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/WhiteSpruce_Leaf_Traits_Alaska/comp/WhiteSpruce_Leaf_Traits_Alaska.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/WhiteSpruce_Leaf_Traits_Alaska_Fig1.png",
-                    "description": "Ratios of (a) maximum rate of carboxylation to respiration at 25 degrees C from Griffin et al. (2022) (Vcmax /R25 ) and (b) maximum electron transport rate to respiration at 25 degrees C from Griffin et al. (2022) (Jmax /R25 ) of white spruce from high and low canopy positions at the Forest Tundra Ecotone (FTE, blue), Alaska, and Black Rock Forest (BRF, green), New York. Boxplots show the median and first and third quartiles. Whiskers display the range of groups with individual points representing outliers falling outside 1.5 times the interquartile range. Different letters represent significant differences between locations and canopy positions.",
                     "@type": "dcat:Distribution",
+                    "description": "Ratios of (a) maximum rate of carboxylation to respiration at 25 degrees C from Griffin et al. (2022) (Vcmax /R25 ) and (b) maximum electron transport rate to respiration at 25 degrees C from Griffin et al. (2022) (Jmax /R25 ) of white spruce from high and low canopy positions at the Forest Tundra Ecotone (FTE, blue), Alaska, and Black Rock Forest (BRF, green), New York. Boxplots show the median and first and third quartiles. Whiskers display the range of groups with individual points representing outliers falling outside 1.5 times the interquartile range. Different letters represent significant differences between locations and canopy positions.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/WhiteSpruce_Leaf_Traits_Alaska_Fig1.png",
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
+            "graphic-preview-description": "Ratios of (a) maximum rate of carboxylation to respiration at 25 degrees C from Griffin et al. (2022) (Vcmax /R25 ) and (b) maximum electron transport rate to respiration at 25 degrees C from Griffin et al. (2022) (Jmax /R25 ) of white spruce from high and low canopy positions at the Forest Tundra Ecotone (FTE, blue), Alaska, and Black Rock Forest (BRF, green), New York. Boxplots show the median and first and third quartiles. Whiskers display the range of groups with individual points representing outliers falling outside 1.5 times the interquartile range. Different letters represent significant differences between locations and canopy positions.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/WhiteSpruce_Leaf_Traits_Alaska_Fig1.png",
+            "identifier": "C2636355463-ORNL_CLOUD",
+            "issued": "2023-03-17",
+            "keyword": [
+                "vegetation",
+                "ecosystems",
+                "ecological dynamics",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2124",
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
             "spatial": "-149.75 41.4 -74.02 67.99",
+            "temporal": "2017-06-19T00:00:00Z/2017-07-20T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: White Spruce Photosynthetic and Leaf Traits, Alaska and New York, 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805858-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2024-07-19",
-            "temporal": "2017-11-29T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "earth science",
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
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C3166805858-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-20 VIIRS Level-3 Global Mapped 11\u00b5m Nighttime Sea Surface Temperature (NSST) Data, version 2024.0",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRSJ1/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for NOAA-20 VIIRS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for NOAA-20 VIIRS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRSJ1/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C3166805858-OB_DAAC",
+            "issued": "2024-07-19",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805858-OB_DAAC.html",
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
+            "title": "NOAA-20 VIIRS Level-3 Global Mapped 11\u00b5m Nighttime Sea Surface Temperature (NSST) Data, version 2024.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0023",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2006-03-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0023.",
-            "issued": "2006-03-16",
-            "temporal": "2001-07-01T00:00:00Z/2002-11-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "atmosphere",
-                "atmospheric winds",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ALLEN ROBINSON",
                 "hasEmail": "mailto:alr@andrew.cmu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2350085207-LARC_ASDC",
             "description": "NARSTO_EPA_SS_PITTSBURGH_MET_DATA is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Pittsburgh Meteorological Data product. It was obtained between July 1, 2001 and November 1, 2002 during the Pittsburgh Supersite Program. Ambient monitoring at the central super site and a set of satellite sites in the Pittsburgh region included numerous meteorological measurements. Meteorological parameters measured during the sampling period included temperature, relative humidity, precipitation, wind speed and direction, UV intensity, and solar intensity. The Pittsburgh Super Site Program was a comprehensive, multi-disciplinary investigation to characterize the ambient Particulate Matter (PM) in the Pittsburgh region, to improve understanding the links between ambient PM and public health, and to develop new instrumentation for PM measurements. The central super site was located next to the Carnegie Mellon University campus near downtown Pittsburgh. Five additional sites served as Satellite sites. The measurement campaign lasted for 18 months (May 2001-October 2002). \r\n\r\nThe specific objectives were to: Characterize the PM with regard to size, surface, and volume distribution; chemical composition as a function of size and on a single particle basis; temporal and spatial variability. Develop and evaluate the current and next generation atmospheric aerosol monitoring techniques including single particle measurements, continuous measurements, ultra-fine aerosol measurements, improved organic component characterization, and others. Quantify the impact of the various sources of PM concentrations in the area including transportation, power plants, natural, etc. Combine the ambient monitoring study with the proposed indoor, health, and modeling studies to elucidate of the links between PM characteristics and their health impacts in this area. \r\n\r\nThe EPA PM Super sites Program was an ambient air monitoring research program from 1999-2004 designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. Eight geographically diverse projects were chosen to specifically address these EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different methods of characterizing PM including testing new and emerging measurement methods. \r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Pittsburgh Meteorological Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0023",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0023",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2350085207-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_PITTSBURGH_MET_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_PITTSBURGH_MET_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2350085207-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0023",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_PITTSBURGH_MET_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_PITTSBURGH_MET_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0023",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_pittsburgh_met_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_PITTSBURGH Meteorological Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_PITTSBURGH Meteorological Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_pittsburgh_met_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Final_QA_Report.pdf",
-                    "description": "Quality Assurance Final Report for the Pittsburgh Air Quality Study Pittsburgh Supersite June 30, 2001 - September 30, 2002",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance Final Report for the Pittsburgh Air Quality Study Pittsburgh Supersite June 30, 2001 - September 30, 2002",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Final_QA_Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Final_Report.pdf",
-                    "description": "Pittsburgh Air Quality Study (PAQS) Final Report",
                     "@type": "dcat:Distribution",
+                    "description": "Pittsburgh Air Quality Study (PAQS) Final Report",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Final_Report.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_PITTSBURGH_MET_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_PITTSBURGH_MET_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_PITTSBURGH_MET_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_PITTSBURGH_MET_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2350085207-LARC_ASDC",
+            "issued": "2006-03-16",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmosphere",
+                "atmospheric winds",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0023",
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
             "spatial": "40.44 -79.94",
+            "temporal": "2001-07-01T00:00:00Z/2002-11-01T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Pittsburgh Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ee3g-swmf",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2020-10-27",
-            "temporal": "2014-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-14",
-            "keyword": [
-                "precipitation",
-                "modis",
-                "imerg",
-                "cloud regime",
-                "cloud-precipitation hybrid regime",
-                "cloud"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daeho Jin",
                 "hasEmail": "mailto:daeho.jin@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Daeho Jin"
-            },
-            "identifier": "https://data.nasa.gov/api/views/ee3g-swmf",
             "description": "Cloud-Precipitation Hybrid Regimes with MODIS C6.1 2D joint histogram of CTP and COT (total 42 bins) and IMERG v06B precipitation histogram (total 6 bins) derived in 15S-15N domain.\n\nThere are 4 kinds of regime sets:\n1) Cloud only (42bin), \n2) Cloud+Precipitation with weight 1 (Cld42+Pr6x1), \n3) Cloud+Precipitation with weight 3 (Cld42+Pr6x3), \n4) Cloud+Precipitation with weight 7 (Cld42+Pr6x7; equal weight).\n\nFile list:\n- MODIS_t+a_cld_hist_15S-15N_CR_set.Cld42.nc\n- MODIS_t+a_cld+pr6x1_hist_15S-15N_CPR_set.Cld42+Pr6x1.nc\n- MODIS_t+a_cld+pr6x3_hist_15S-15N_CPR_set.Cld42+Pr6x3.nc\n- MODIS_t+a_cld+pr6x7_hist_15S-15N_CPR_set.Cld42+Pr6x7.nc\n- MODIS_t+a_cld+pr6x7_hist_15S-15N_CPR_projected2IMERGdomain.Cld42+Pr6x7.nc",
-            "title": "Cloud-Precipitation Hybrid Regimes (MODIS-IMERG) in 15S-15N",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -699906,378 +699884,372 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/ee3g-swmf",
+            "issued": "2020-10-27",
+            "keyword": [
+                "precipitation",
+                "modis",
+                "imerg",
+                "cloud regime",
+                "cloud-precipitation hybrid regime",
+                "cloud"
+            ],
+            "landingPage": "https://data.nasa.gov/d/ee3g-swmf",
+            "modified": "2024-05-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Daeho Jin"
+            },
+            "temporal": "2014-01-01/2014-01-01",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Cloud-Precipitation Hybrid Regimes (MODIS-IMERG) in 15S-15N"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA+AQUA/CERES/SYN1DEG-3HOUR_L3.004A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-09-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA+AQUA/CERES/SYN1DEG-3HOUR_L3.004A.",
-            "issued": "2015-06-17",
-            "temporal": "2002-07-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-13",
-            "keyword": [
-                "national geospatial data asset",
-                "earth science",
-                "clouds",
-                "ngda",
-                "biosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmosphere",
-                "aerosols",
-                "vegetation"
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
-            "identifier": "C1227323456-LARC_ASDC",
             "description": "CER_SYN1deg-3Hour_Terra-Aqua-MODIS_Edition4A is the Clouds and the Earth's Radiant Energy System (CERES) and geostationary (GEO)-Enhanced Top of Atmosphere (TOA), Within-Atmosphere, and Surface Fluxes, Clouds and Aerosols 3-Hourly Terra-Aqua Edition4A data product. The instruments and platforms used to collect this data include: Imaging Radiometers on Geostationary Satellites platform; CERES Flight Model 1 (FM1), CERES FM2, CERES Scanner, and Moderate-Resolution Imaging Spectroradiometer (MODIS) on Terra; and CERES FM3, CERES FM4, CERES Scanner, and MODIS on Aqua. Data collection for this product is in progress.\r\n\r\nCERES Synoptic (SYN)1 degree products provide CERES-observed temporally interpolated TOA radiative fluxes and coincident MODIS-derived cloud and aerosol properties and include geostationary-derived cloud properties and broadband fluxes that have been carefully normalized with CERES fluxes in order to maintain the CERES calibration. They also contain computed initial TOA, in-atmosphere, and surface fluxes and computed fluxes that have been adjusted or constrained to the CERES-observed TOA fluxes. The computed fluxes are produced using the Langley Fu-Liou radiative transfer model. Computations use MODIS and geostationary satellite cloud properties along with atmospheric profiles provided by the NASA Global Modeling and Assimilation Office (GMAO). The adjustments to clouds and atmospheric properties are also provided. The computations are made for all-sky, clear-sky, pristine (clear-sky without aerosols), and all-sky without aerosol conditions. This product provides parameters on a three-hourly temporal resolution and 1\u00b0-regional spatial scales. Fluxes are provided for clear-sky and all-sky conditions in the longwave (LW), shortwave (SW), and window (WN) regions.\r\n\r\nCERES SYN1deg products use 1-hourly radiances and cloud property data from geostationary (GEO) imagers to more accurately model variability between CERES observations. To use GEO data to enhance diurnal sampling, several steps are involved. First, GEO radiances are cross-calibrated with the MODIS imager using only data that is coincident in time and ray-matched in angle. Next, the GEO cloud retrievals are inferred from the calibrated GEO radiances. The GEO radiances are converted from narrowband to broadband using empirical regressions and then to broadband GEO TOA fluxes using Angular Distribution Models (ADMs) and directional models. To ensure GEO and CERES TOA fluxes are consistent, a normalization technique is used. Instantaneous matched gridded fluxes from CERES and GEO are regressed against one another over a month from 5\u00b0x5 \u00b0 latitude-longitude regions. The regression relation is then applied to all GEO fluxes to remove biases that depend upon cloud amount, solar and view zenith angles, and regional dependencies. The regional means are determined for 1\u00b0 equal-angle grid boxes calculated by first interpolating each parameter for any missing times of the CERES/GEO observations to produce a complete 1-hourly time series for the month. Monthly means are calculated using the combination of observed and interpolated parameters from all days containing at least one CERES observation.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partner",
-            "title": "CERES and GEO-Enhanced TOA, Within-Atmosphere and Surface Fluxes, Clouds and Aerosols 3-Hourly Terra-Aqua Edition4A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA+AQUA%2FCERES%2FSYN1DEG-3HOUR_L3.004A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA+AQUA%2FCERES%2FSYN1DEG-3HOUR_L3.004A",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA+AQUA/CERES/SYN1DEG-3HOUR_L3.004A",
-                    "description": "DOI data set landing page for CER_SYN1deg-3Hour_Terra-Aqua-MODIS_Edition4A and CER_SYN1deg-3Hour_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_SYN1deg-3Hour_Terra-Aqua-MODIS_Edition4A and CER_SYN1deg-3Hour_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://doi.org/10.5067/TERRA+AQUA/CERES/SYN1DEG-3HOUR_L3.004A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/TISAavg_SampleRead_SYN1deg_R5-922.zip",
-                    "description": "Read Software Package - SYN1deg - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - SYN1deg - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/TISAavg_SampleRead_SYN1deg_R5-922.zip",
+                    "mediaType": "application/zip",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf",
-                    "description": "CERES SYN1deg Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES SYN1deg Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed4A_DQS.pdf",
-                    "description": "Quality Summary: CERES_SYN1deg_Ed4A (10/3/2017)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_SYN1deg_Ed4A (10/3/2017)",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed4A_DQS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1227323456-LARC_ASDC",
-                    "description": "Earthdata Search for CER_SYN1deg-3Hour_Terra-Aqua-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_SYN1deg-3Hour_Terra-Aqua-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1227323456-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#aqua",
-                    "description": "CERES Overview of Aqua",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of Aqua",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#aqua",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SYNI_R5V1.pdf",
-                    "description": "CERES Data Products Catalog R5V1 11/22/2013 Synoptic Radiative Fluxes and Clouds Intermediate (SYNI)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R5V1 11/22/2013 Synoptic Radiative Fluxes and Clouds Intermediate (SYNI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SYNI_R5V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#syn1deg-level-3",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#syn1deg-level-3",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
@@ -700287,775 +700259,775 @@
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SYN1deg-3Hour/Terra-Aqua-MODIS_Edition4A/",
-                    "description": "ASDC Direct Data Download for CER_SYN1deg-3Hour_Terra-Aqua-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_SYN1deg-3Hour_Terra-Aqua-MODIS_Edition4A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SYN1deg-3Hour/Terra-Aqua-MODIS_Edition4A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SYN1deg-3Hour/Terra-Aqua-MODIS_Edition4A/contents.html",
-                    "description": "OPeNDAP data access for CER_SYN1deg-3Hour_Terra-Aqua-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_SYN1deg-3Hour_Terra-Aqua-MODIS_Edition4A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SYN1deg-3Hour/Terra-Aqua-MODIS_Edition4A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1227323456-LARC_ASDC",
+            "issued": "2015-06-17",
+            "keyword": [
+                "national geospatial data asset",
+                "earth science",
+                "clouds",
+                "ngda",
+                "biosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmosphere",
+                "aerosols",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA+AQUA/CERES/SYN1DEG-3HOUR_L3.004A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2002-07-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES and GEO-Enhanced TOA, Within-Atmosphere and Surface Fluxes, Clouds and Aerosols 3-Hourly Terra-Aqua Edition4A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-6-EROS-MAPS-MODELS-V1.0",
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
+            "description": "NLR Level 3 Data Products includes spherical harmonic shape and gravity models, and gridded maps or images of those models.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-6-eros-maps-models-v1.0_ee6x-j7vn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-6-EROS-MAPS-MODELS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-6-eros-maps-models-v1.0_ee6x-j7vn",
-            "description": "NLR Level 3 Data Products includes spherical harmonic shape and gravity models, and gridded maps or images of those models.",
-            "title": "NEAR NLR LEVEL 3 DATA PRODUCTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR NLR LEVEL 3 DATA PRODUCTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/POSS/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hudak, David .2013. GPM GROUND VALIDATION ENVIRONMENT CANADA (EC) PRECIPITATION OCCURRENCE SENSOR SYSTEM (POSS) GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/POSS/DATA201",
-            "issued": "2013-09-03",
-            "temporal": "2012-01-15T00:00:00Z/2012-03-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-20",
-            "keyword": [
-                "radar",
-                "earth science",
-                "atmosphere",
-                "precipitation",
-                "spectral/engineering"
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
-            "identifier": "C1979685182-GHRC_DAAC",
             "description": "The GPM Ground Validation Environment Canada (EC) Precipitation Occurrence Sensor System (POSS) GCPEx dataset is comprised of data gathered during the GPM Cold-season Precipitation Experiment (GCPEx), which took place in Ontario, Canada, January 15 - March 1, 2012. GCPEx addressed shortcomings in the GPM snowfall retrieval algorithm by collecting microphysical properties, associated remote sensing observations, and coordinated model simulations of precipitating snow. The POSS is a bi-static X-band Doppler radar designed by Environment Canada. The POSS measures a signal whose frequency is proportional to the particle Doppler velocity and whose amplitude is proportional to the particle scattering cross-section. Its measurements can be used to provide information regarding precipitation occurrence, type, rate, and raindrop size distribution.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION ENVIRONMENT CANADA (EC) PRECIPITATION OCCURRENCE SENSOR SYSTEM (POSS) GCPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/poss_EC/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FPOSS%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FPOSS%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmpossgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmpossgcpex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/poss_EC/browse/CARE/gcpex_poss_pr_20120229_EC_CARE-TNE.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/poss_EC/browse/CARE/gcpex_poss_pr_20120229_EC_CARE-TNE.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmpossgcpex/gpmpossgcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmpossgcpex/gpmpossgcpex_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/poss_EC/doc/POSS_Documentation_for_PR_files_130211.doc",
-                    "description": "Description of the POSS post processed \u00bf\u00bf\u00bfPR\u00bf\u00bf\u00bf file Updated Feb. 11 2013",
                     "@type": "dcat:Distribution",
+                    "description": "Description of the POSS post processed \u00bf\u00bf\u00bfPR\u00bf\u00bf\u00bf file Updated Feb. 11 2013",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/poss_EC/doc/POSS_Documentation_for_PR_files_130211.doc",
+                    "mediaType": "application/msword",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/poss_EC/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/poss_EC/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/poss_EC/browse/",
+            "identifier": "C1979685182-GHRC_DAAC",
+            "issued": "2013-09-03",
+            "keyword": [
+                "radar",
+                "earth science",
+                "atmosphere",
+                "precipitation",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/POSS/DATA201",
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
             "spatial": "-79.93 44.18 -79.64 44.23",
+            "temporal": "2012-01-15T00:00:00Z/2012-03-01T23:59:59Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION ENVIRONMENT CANADA (EC) PRECIPITATION OCCURRENCE SENSOR SYSTEM (POSS) GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2732-V1.0",
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
-                "mars express"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-01-20T16:20:16 to 2011-01-20T18:14:57.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2732-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2732-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2732-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-01-20T16:20:16 to 2011-01-20T18:14:57.500.",
-            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2732 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2732 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/395",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kieser, B. 1998. BOREAS TGB-09 Above-canopy NMHC at SSA-OBS, SSA-OJP and SSA-OA Sites. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/395",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-27T00:00:00Z/1994-09-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
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
-            "identifier": "C2808132169-ORNL_CLOUD",
             "description": "Contains the mixing ratio and concentration of Non-Methane HydroCarbons (NMHC) taken by the TGB-09 group.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-09 Above-canopy NMHC at SSA-OBS, SSA-OJP and SSA-OA Sites",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F395",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F395",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb9nmhc/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb9nmhc/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB09_NMHC_DATA.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB09_NMHC_DATA.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/395",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/395",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb9nmhc/comp/TGB09_NMHC_DATA.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb9nmhc/comp/TGB09_NMHC_DATA.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb9nmhc/comp/TGB09_NMHC_DATA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb9nmhc/comp/TGB09_NMHC_DATA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb9nmhc/comp/TGB09_NMHC_DATA.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb9nmhc/comp/TGB09_NMHC_DATA.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb9nmhc/comp/tgb9nmhc.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb9nmhc/comp/tgb9nmhc.def",
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
+            "identifier": "C2808132169-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/395",
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
             "spatial": "-106.2 53.63 -104.69 53.99",
+            "temporal": "1994-05-27T00:00:00Z/1994-09-15T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-09 Above-canopy NMHC at SSA-OBS, SSA-OJP and SSA-OA Sites"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/V7J5AUOAVA4T",
             "citation": "Kevin W. Bowman. 2021-05-18. TRPSDL2PANCRSWCFHI. Version 1. TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for West Coast Fires HiRes, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/V7J5AUOAVA4T. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2PANCRSWCFHI_1.html. Digital Science Data.",
-            "issued": "2021-05-18",
-            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-18",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.5194/amt-7-3737-2014",
-                "https://doi.org/10.1109/TGRS.2006.871234",
-                "https://doi.org/10.1029/2002JD002299"
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
-            "identifier": "C2054599713-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for West Coast Fires HiRes, Standard Product contains the vertical distribution of the retrieved atmospheric state of peroxyacetyl nitrate (PAN), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. This product focuses on the CONUS region (20N-60N; 150W-40W) for the time period from 2020-08-01 to 2020-10-31, during the outbreak of U.S. West Coast wildfires. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 16 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2PANCRSWCFHI",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS/SNPP PAN (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
-            "title": "TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for West Coast Fires HiRes, Standard Product V1 (TRPSDL2PANCRSWCFHI) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2PANCRSWCFHI_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FV7J5AUOAVA4T",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FV7J5AUOAVA4T",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2PANCRSWCFHI_Sample.png",
-                    "description": "TROPESS CrIS/SNPP PAN (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS/SNPP PAN (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2PANCRSWCFHI_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2PANCRSWCFHI_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2PANCRSWCFHI_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2PANCRSWCFHI.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2PANCRSWCFHI.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2PANCRSWCFHI_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2PANCRSWCFHI_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2PANCRSWCFHI.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2PANCRSWCFHI.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2PANCRSWCFHI.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2PANCRSWCFHI.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CRIS-PAN_L2_Product_Quick_Start_User_Guide_Standard_only_2-22-21.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CRIS-PAN_L2_Product_Quick_Start_User_Guide_Standard_only_2-22-21.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS/SNPP PAN (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2PANCRSWCFHI_Sample.png",
+            "identifier": "C2054599713-GES_DISC",
+            "issued": "2021-05-18",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/V7J5AUOAVA4T",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.5194/amt-7-3737-2014",
+                "https://doi.org/10.1109/TGRS.2006.871234",
+                "https://doi.org/10.1029/2002JD002299"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2PANCRSWCFHI",
             "spatial": "-150.0 20.0 -40.0 60.0",
+            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for West Coast Fires HiRes, Standard Product V1 (TRPSDL2PANCRSWCFHI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA+NPP/CERES/SYN1DEG-MONTH_L3.01A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-10-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA+NPP/CERES/SYN1DEG-MONTH_L3.01A.",
-            "issued": "2017-09-21",
-            "temporal": "2012-02-01T00:00:00Z/2017-11-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-13",
-            "keyword": [
-                "atmospheric temperature",
-                "biosphere",
-                "atmospheric water vapor",
-                "ngda",
-                "clouds",
-                "national geospatial data asset",
-                "earth science",
-                "atmospheric pressure",
-                "aerosols",
-                "atmosphere",
-                "atmospheric radiation",
-                "vegetation"
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
-            "identifier": "C1424862293-LARC_ASDC",
             "description": "CER_SYN1deg-Month_Terra-NPP_Edition1A is the Clouds and the Earth's Radiant Energy System (CERES) and geostationary (GEO)-Enhanced Top-of-Atmosphere (TOA) Within-Atmosphere and Surface Fluxes, Clouds and Aerosols Monthly Terra-Suomi National Polar-orbiting Partnership (NPP) Edition1A data product. Data was collected using the CERES Imaging Radiometers on Geostationary Satellites; CERES Flight Model 1 (FM1), FM2, CERES Scanner, and Moderate-Resolution Imaging Spectroradiometer (MODIS) on Terra; and FM5, CERES Scanner, and Visible-Infrared Imager-Radiometer Suite (VIIRS) on NPP. Data collection for this product is complete. \r\n\r\nThe CERES SYN1deg products provide CERES-observed temporally interpolated TOA radiative fluxes and coincident MODIS-derived cloud and aerosol properties and include geostationary-derived cloud properties and broadband fluxes that have been carefully normalized with CERES fluxes in order to maintain the CERES calibration. They also contain computed initial TOA, in-atmosphere, and surface fluxes and computed fluxes that have been adjusted or constrained to the CERES-observed TOA fluxes. The computed fluxes are produced using the Langley Fu-Liou radiative transfer model. Computations use MODIS and geostationary satellite cloud properties along with atmospheric profiles provided by the Global Modeling and Assimilation Office (GMAO). The adjustments to clouds and atmospheric properties are also provided. The computations are made for all-sky, clear-sky, pristine (clear-sky without aerosols), and all-sky without aerosol conditions. This product provides parameters on a monthly temporal resolutions on 1\u00b0-regional, zonal, and global spatial scales. Fluxes are provided for clear-sky and all-sky conditions in the longwave (LW), shortwave (SW), and window (WN) regions.\r\n\r\nThe CERES SYN1deg products use 1-hourly radiances and cloud property data from geostationary (GEO) imagers to more accurately model variability between CERES observations. To use GEO data to enhance diurnal sampling, several steps are involved. First, GEO radiances are cross-calibrated with the MODIS imager using only data that is coincident in time and ray-matched in angle. Next, the GEO cloud retrievals are inferred from the calibrated GEO radiances. The GEO radiances are converted from narrowband to broadband using empirical regressions and then to broadband GEO TOA fluxes using Angular Distribution Models (ADMs) and directional models. To ensure GEO and CERES TOA fluxes are consistent, a normalization technique is used. Instantaneous matched gridded fluxes from CERES and GEO are regressed against one another over a month from 5\u00b0x5 \u00b0 latitude-longitude regions. The regression relation is then applied to all GEO fluxes to remove biases that depend upon cloud amount, solar and view zenith angles, and regional dependencies. The regional means are determined for 1\u00b0 equal-angle grid boxes calculated by first interpolating each parameter for any missing times of the CERES/GEO observations to produce a complete 1-hourly time series for the month. Monthly means are calculated using the combination of observed and interpolated parameters from all days containing at least one CERES observation.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi NPP satellite on O",
-            "title": "CERES and GEO-Enhanced TOA, Within-Atmosphere and Surface Fluxes, Clouds and Aerosols Monthly Terra-NPP Edition1A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA+NPP%2FCERES%2FSYN1DEG-MONTH_L3.01A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA+NPP%2FCERES%2FSYN1DEG-MONTH_L3.01A",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA+NPP/CERES/SYN1DEG-MONTH_L3.01A",
-                    "description": "DOI data set landing page for CER_SYN1deg-Month_Terra-NPP_Edition1A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_SYN1deg-Month_Terra-NPP_Edition1A",
+                    "downloadURL": "https://doi.org/10.5067/TERRA+NPP/CERES/SYN1DEG-MONTH_L3.01A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1424862293-LARC_ASDC",
-                    "description": "Earthdata Search for CER_SYN1deg-Month_Terra-NPP_Edition1A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_SYN1deg-Month_Terra-NPP_Edition1A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1424862293-LARC_ASDC",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed1A_DQS.pdf",
-                    "description": "Quality Summary: CERES_SYN1deg_Ed1A (10/3/2017)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_SYN1deg_Ed1A (10/3/2017)",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed1A_DQS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf",
-                    "description": "CERES SYN1deg Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES SYN1deg Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SYNI_R5V1.pdf",
-                    "description": "CERES Data Products Catalog R5V1 11/22/2013 Synoptic Radiative Fluxes and Clouds Intermediate (SYNI)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R5V1 11/22/2013 Synoptic Radiative Fluxes and Clouds Intermediate (SYNI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SYNI_R5V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#syn1deg-level-3",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#syn1deg-level-3",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
@@ -701065,441 +701037,452 @@
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SYN1deg-Month/Terra-NPP_Edition1A/",
-                    "description": "ASDC Direct Data Download for CER_SYN1deg-Month_Terra-NPP_Edition1A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_SYN1deg-Month_Terra-NPP_Edition1A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SYN1deg-Month/Terra-NPP_Edition1A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SYN1deg-Month/Terra-NPP_Edition1A/contents.html",
-                    "description": "OPeNDAP data access for CER_SYN1deg-Month_Terra-NPP_Edition1A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_SYN1deg-Month_Terra-NPP_Edition1A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SYN1deg-Month/Terra-NPP_Edition1A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1424862293-LARC_ASDC",
+            "issued": "2017-09-21",
+            "keyword": [
+                "atmospheric temperature",
+                "biosphere",
+                "atmospheric water vapor",
+                "ngda",
+                "clouds",
+                "national geospatial data asset",
+                "earth science",
+                "atmospheric pressure",
+                "aerosols",
+                "atmosphere",
+                "atmospheric radiation",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA+NPP/CERES/SYN1DEG-MONTH_L3.01A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2012-02-01T00:00:00Z/2017-11-30T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES and GEO-Enhanced TOA, Within-Atmosphere and Surface Fluxes, Clouds and Aerosols Monthly Terra-NPP Edition1A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-2-EAR1-MAG-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the EAR1 (Earth fly-by 1) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-2-ear1-mag-v1.0_eehb-8qbr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-2-EAR1-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-2-ear1-mag-v1.0_eehb-8qbr",
-            "description": "This archive contains data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the EAR1 (Earth fly-by 1) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER EARTH ROMAP 2 EAR1 MAG\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER EARTH ROMAP 2 EAR1 MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD09GQ.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD09GQ.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-01",
-            "temporal": "2000-02-24T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-01",
-            "keyword": [
-                "land surface",
-                "ngda",
-                "surface radiative properties",
-                "earth science",
-                "national geospatial data asset"
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
-            "identifier": "C2343115666-LPCLOUD",
             "description": "The MOD09GQ Version 6.1 product provides an estimate of the surface spectral reflectance of Terra Moderate Resolution Imaging Spectroradiometer (MODIS) 250 meter (m) bands 1 and 2, corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. Along with the 250 m surface reflectance bands are the Quality Assurance (QA) layer and five observation layers. This product is intended to be used in conjunction with the quality and viewing geometry information of the 500 m product (MOD09GA). \n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Reflectance products. Further details regarding MODIS land product validation for the MOD09 data product is available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD09).\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "title": "MODIS/Terra Surface Reflectance Daily L2G Global 250m SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2509506318-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09GQ.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09GQ.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD09GQ.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD09GQ.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2343115666-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2343115666-LPCLOUD",
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
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD09GQ.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD09GQ.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD09GQ",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD09GQ",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP124/MOLT/MOD09GQ.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP124/MOLT/MOD09GQ.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2509506318-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2509506318-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2509506318-LPCLOUD?h=85&w=85",
+            "identifier": "C2343115666-LPCLOUD",
+            "issued": "2021-02-01",
+            "keyword": [
+                "land surface",
+                "ngda",
+                "surface radiative properties",
+                "earth science",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD09GQ.061",
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
+            "temporal": "2000-02-24T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Surface Reflectance Daily L2G Global 250m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/L1UAFNTVCZGX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Ancillary Soil Characteristics Data, Georgia, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/L1UAFNTVCZGX.",
-            "issued": "2003-06-01",
-            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-31",
-            "keyword": [
-                "agriculture",
-                "soils",
-                "land surface",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Cosh",
                 "hasEmail": "mailto:mcosh@hydrolab.arsusda.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386250721-NSIDCV0",
             "description": "The SMEX03 Ancillary Soil Characteristics data set contains data for the regional study areas of Alabama, Georgia, and Oklahoma, USA as part of the 2003 Soil Moisture Experiment (SMEX03). The original data were extracted from a multi-layer soil characteristics database for the conterminous United States and generated using Environmental Systems Research Institute (ESRI) ArcMap software for each regional study area.",
-            "title": "SMEX03 Ancillary Soil Characteristics Data, Georgia, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL1UAFNTVCZGX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL1UAFNTVCZGX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ancillary_data/soils/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ancillary_data/soils/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ancillary_data/soils/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ancillary_data/soils/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/L1UAFNTVCZGX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/L1UAFNTVCZGX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/L1UAFNTVCZGX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/L1UAFNTVCZGX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "spatial": "-83.97 30.96 -83.36 31.9",
-            "theme": [
-                "geospatial"
+            "identifier": "C1386250721-NSIDCV0",
+            "issued": "2003-06-01",
+            "keyword": [
+                "agriculture",
+                "soils",
+                "land surface",
+                "earth science"
             ],
+            "landingPage": "https://doi.org/10.5067/L1UAFNTVCZGX",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/PLUMES_AND_BLOOMS/DATA001",
-            "bureauCode": [
-                "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/PLUMES_AND_BLOOMS/DATA001.",
-            "issued": "1996-08-09",
-            "temporal": "1996-08-09T17:14:59Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
-                "earth science",
-                "ocean chemistry",
-                "ocean optics"
+            "modified": "2003-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-83.97 30.96 -83.36 31.9",
+            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "SMEX03 Ancillary Soil Characteristics Data, Georgia, Version 1"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/PLUMES_AND_BLOOMS/DATA001.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C1633360616-OB_DAAC",
             "description": "The Plumes and Blooms program is a joint collaboration among UCSB faculty, student and staff researchers at the Institute of Computational Earth System Science (ICESS), NOAA researchers at the Coastal Services Center (Charleston, SC) and the NOAA sanctuary managers of the Channel Islands National Marine Sanctuary (CINMS). Since August, 1996, monthly research cruises have been conducted to collect measurements. These measurements include temperature and salinity, ocean color spectra, and water column profiles of red light transmission and chlorophyll fluorescence (indexes of suspended particulate load and phytoplankton abundance). The transect observations begin at the shelf waters north of Santa Rosa island and end at an area off Goleta Point. These repeat observations are combined with satellite imagery to build a time-series of the changing ocean color conditions in the Santa Barbara Channel.",
-            "title": "Plumes and Blooms",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPLUMES_AND_BLOOMS%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPLUMES_AND_BLOOMS%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Plumes_and_Blooms/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Plumes_and_Blooms/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360616-OB_DAAC",
+            "issued": "1996-08-09",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/PLUMES_AND_BLOOMS/DATA001",
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
+            "temporal": "1996-08-09T17:14:59Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Plumes and Blooms"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-PRL2-V1.0",
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
+            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter, acquired during the prelanding part 2 phase at the vicinity of the comet 67P/CG. It also contains documentation which describes the MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-prl2-v1.0_eejv-qtyx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-PRL2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-prl2-v1.0_eejv-qtyx",
-            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter, acquired during the prelanding part 2 phase at the vicinity of the comet 67P/CG. It also contains documentation which describes the MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER 67P RPCMIP 3 PRL2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P RPCMIP 3 PRL2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OEFD-3--EFIELD-HIRES-V1.0",
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
-                "pioneer venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains wave electric\nfield amplitudes measured at four different frequencies by the Pioneer Venus\nOrbiter Electric Field Detector.  The four frequencies are 100 Hz, 730 Hz,\n5.4 kHz, 30 kHz. The frequency filters are narrow-band, with a 30% bandwidth.\nThus wave intensities are given in V2/m2/Hz.  The filters are\ncontinuously active, but data are only provided at a rate determined\nby the spacecraft telemetry rate.  The wave antenna is oriented\nperpendicular to the spacecraft spin axis, and so the wave instrument\nmeasures only wave fields in the spacecraft spin plane.\nSpin modulation of naturally occurring signals can be used to\nobtain two dimensional wave field information.  The wave antenna\nis a small Y-shaped structure, with effective separation of 0.76\nmeters. The spin phase of the effective dipole is included\nwithin the high resolution data set for each of the channels, which\nare sampled at different times.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oefd-3--efield-hires-v1.0_eek2-ehzz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "pioneer venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OEFD-3--EFIELD-HIRES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oefd-3--efield-hires-v1.0_eek2-ehzz",
-            "description": "This data set contains wave electric\nfield amplitudes measured at four different frequencies by the Pioneer Venus\nOrbiter Electric Field Detector.  The four frequencies are 100 Hz, 730 Hz,\n5.4 kHz, 30 kHz. The frequency filters are narrow-band, with a 30% bandwidth.\nThus wave intensities are given in V2/m2/Hz.  The filters are\ncontinuously active, but data are only provided at a rate determined\nby the spacecraft telemetry rate.  The wave antenna is oriented\nperpendicular to the spacecraft spin axis, and so the wave instrument\nmeasures only wave fields in the spacecraft spin plane.\nSpin modulation of naturally occurring signals can be used to\nobtain two dimensional wave field information.  The wave antenna\nis a small Y-shaped structure, with effective separation of 0.76\nmeters. The spin phase of the effective dipole is included\nwithin the high resolution data set for each of the channels, which\nare sampled at different times.",
-            "title": "PVO VENUS SC POSITION DERIVED VSO COORDS 12 SECOND VER1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PVO VENUS SC POSITION DERIVED VSO COORDS 12 SECOND VER1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000081-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "2012-07-01",
-            "temporal": "1992-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-10-22",
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
-            "identifier": "C1000000081-CDDIS",
             "description": "Making Earth System Data Records for Use in Research Environments (MEaSUREs) empowers the research community to participate in developing and generating data products that complement and augment NASA produced and distributed Earth science data products. NASA\u2019s Enhanced Solid Earth Science Earth Science Data Record (ESDR) System (ESESES) continues and extends mature geodetic data product generation and archival as part of the MEaSUREs SESES project providing new, multi-decade, calibrated and validated geodetic-derived ESDRs obtained by the Scripps Institution of Oceanography (SIO) and NASA's Jet Propulsion Laboratory (JPL). These data-derived products include continuous multi-year high-rate GNSS, seismogeodetic, and meteorological time series, a catalog of transient deformation in tectonically active areas known for aseismic motion such as ETS with focus in Cascadia, and continuous estimation and cataloging of total near-surface water content derived from continuous GNSS time series over the continental U.S. These data products are daily geodetic displacement time series (compressed). They are combined, cleaned and filtered, GIPSY-GAMIT long-term time series of Continuous Global Navigation Satellite System (CGNSS) station positions (global and regional) in the latest version of ITRF",
-            "title": "CDDIS SESES MEaSUREs products daily GNSS geodetic displacement time series",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -701508,963 +701491,994 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000081-CDDIS",
+            "issued": "2012-07-01",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000081-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-10-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "GNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS SESES MEaSUREs products daily GNSS geodetic displacement time series"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/CLDMSK_L2_MODIS_Aqua.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2019-03-01. MODIS/Aqua Cloud Mask 5-Min Swath 1000 m. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/CLDMSK_L2_MODIS_Aqua.001. https://doi.org/10.5067/MODIS/CLDMSK_L2_MODIS_Aqua.001.",
-            "issued": "2019-02-15",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "keyword": [
-                "spectral/engineering",
-                "visible wavelengths",
-                "clouds",
-                "atmosphere",
-                "earth science",
-                "infrared wavelengths",
-                "national geospatial data asset",
-                "ngda"
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
-            "identifier": "C1593392869-LAADS",
-            "description": "The MODIS-VIIRS Cloud Mask (MVCM) is designed to facilitate continuity in cloud detection between the MODIS (Moderate Resolution Imaging Spectroradiometer) on the Aqua and Terra platforms and the series of VIIRS (Visible Infrared Imaging Radiometer Suite) instruments, beginning with the Suomi NPP spacecraft. To establish continuity, this MODIS MVCM product does not use an algorithm identical to that used in the standard MODIS product (MOD35/MYD35). The MVCM-MODIS Cloud Mask product is Aqua MOIDS Level-2, 5-Min Swath product generated at 1000 m (at nadir) spatial resolution. The algorithm employs a series of visible through infrared threshold and consistency tests to specify confidence that an unobstructed view of the Earth's surface has been observed. Radiometrically-accurate radiances are required, thus holes in the cloud mask will appear wherever the input radiances are incomplete or of poor quality.\r\n\r\nFor more information consult Product Page at: \r\nhttps://cimss.ssec.wisc.edu/MVCM/",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "MODIS/Aqua Cloud Mask 5-Min Swath 1000 m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS-VIIRS Cloud Mask (MVCM) is designed to facilitate continuity in cloud detection between the MODIS (Moderate Resolution Imaging Spectroradiometer) on the Aqua and Terra platforms and the series of VIIRS (Visible Infrared Imaging Radiometer Suite) instruments, beginning with the Suomi NPP spacecraft. To establish continuity, this MODIS MVCM product does not use an algorithm identical to that used in the standard MODIS product (MOD35/MYD35). The MVCM-MODIS Cloud Mask product is Aqua MOIDS Level-2, 5-Min Swath product generated at 1000 m (at nadir) spatial resolution. The algorithm employs a series of visible through infrared threshold and consistency tests to specify confidence that an unobstructed view of the Earth's surface has been observed. Radiometrically-accurate radiances are required, thus holes in the cloud mask will appear wherever the input radiances are incomplete or of poor quality.\r\n\r\nFor more information consult Product Page at: \r\nhttps://cimss.ssec.wisc.edu/MVCM/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FCLDMSK_L2_MODIS_Aqua.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FCLDMSK_L2_MODIS_Aqua.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/CLDMSK_L2_MODIS_Aqua.001",
-                    "description": "Data product's landing page",
                     "@type": "dcat:Distribution",
+                    "description": "Data product's landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/CLDMSK_L2_MODIS_Aqua.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/CLDMSK_L2_MODIS_Aqua--5110",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/CLDMSK_L2_MODIS_Aqua--5110",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5110/CLDMSK_L2_MODIS_Aqua/contents.html",
-                    "description": "Direct access to CLDMSK_L2_VIIRS_SNPP OPeNDAP data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to CLDMSK_L2_VIIRS_SNPP OPeNDAP data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5110/CLDMSK_L2_MODIS_Aqua/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/MODIS_VIIRS_Cloud-Mask_UG_Feb_2019.pdf",
-                    "description": "Product User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Product User's Guide",
+                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/MODIS_VIIRS_Cloud-Mask_UG_Feb_2019.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C1593392869-LAADS",
+            "issued": "2019-02-15",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "clouds",
+                "atmosphere",
+                "earth science",
+                "infrared wavelengths",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/CLDMSK_L2_MODIS_Aqua.001",
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
+            "temporal": "2002-07-04T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Cloud Mask 5-Min Swath 1000 m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-SLOPE-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-slope-ops-v1.0_eeqz-8gxi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-SLOPE-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-slope-ops-v1.0_eeqz-8gxi",
-            "description": "NULL",
-            "title": "MER 1 MARS NAVIGATION CAMERA SLOPE RDR\n                                      OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS NAVIGATION CAMERA SLOPE RDR\n                                      OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-MRI-2-9P-CRUISE-V1.0",
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
-                "deep impact"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains raw science calibration images acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the cruise phase of the mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-mri-2-9p-cruise-v1.0_ees3-5dgh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "deep impact"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-MRI-2-9P-CRUISE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-mri-2-9p-cruise-v1.0_ees3-5dgh",
-            "description": "This data set contains raw science calibration images acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the cruise phase of the mission.",
-            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW MRI CALIB DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW MRI CALIB DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-2-RVM1-SPM-V1.0",
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
+            "description": "This archive contains level 2 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the RMV1 (Rendez-vous Manoeuvre 1) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-2-rvm1-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-2-RVM1-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-2-rvm1-spm-v1.0",
-            "description": "This archive contains level 2 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the RMV1 (Rendez-vous Manoeuvre 1) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 2 RVM1 SPM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL ROMAP 2 RVM1 SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-5-DDR-PCC-V1.0",
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
-                "comet"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Physical characteristics of comets observed from -466 to 1975, compiled by S. K. Vsekhsvyatskii.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-5-ddr-pcc-v1.0_eeta-de8g",
+            "issued": "2018-06-26",
+            "keyword": [
+                "comet"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-5-DDR-PCC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-5-ddr-pcc-v1.0_eeta-de8g",
-            "description": "Physical characteristics of comets observed from -466 to 1975, compiled by S. K. Vsekhsvyatskii.",
-            "title": "PHYSICAL CHARACTERISTICS OF COMETS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHYSICAL CHARACTERISTICS OF COMETS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/BENEFIT/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/BENEFIT/DATA001.",
-            "issued": "2000-10-26",
-            "temporal": "2000-10-26T08:45:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "ocean chemistry",
-                "ocean temperature",
-                "ocean optics",
-                "salinity/density",
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
-            "identifier": "C1633360138-OB_DAAC",
             "description": "Measurements made off the Namibian and South African coasts between 2000 and 2002.",
-            "title": "Measurements made off the Namibian and South African coasts between 2000 and 2002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBENEFIT%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBENEFIT%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BENEFIT/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BENEFIT/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360138-OB_DAAC",
+            "issued": "2000-10-26",
+            "keyword": [
+                "earth science",
+                "ocean chemistry",
+                "ocean temperature",
+                "ocean optics",
+                "salinity/density",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/BENEFIT/DATA001",
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
+            "temporal": "2000-10-26T08:45:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements made off the Namibian and South African coasts between 2000 and 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC1-MTP011-V1.0",
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
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase from 19th Dec 2014 to 13th Jan 2015 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc1-mtp011-v1.0_eetu-gani",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC1-MTP011-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc1-mtp011-v1.0_eetu-gani",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase from 19th Dec 2014 to 13th Jan 2015 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 1 MTP011 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 1 MTP011 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP10A1.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VIIRS/NPP Snow Cover Daily L3 Global 375m SIN Grid V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP10A1.001.",
-            "issued": "2012-01-19",
-            "temporal": "2012-01-19T00:00:00Z/2024-06-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-16",
-            "keyword": [
-                "cryosphere",
-                "snow/ice",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "George Riggs",
                 "hasEmail": "mailto:George.A.Riggs@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1600510471-NSIDC_ECS",
             "description": "This data set contains daily snow cover derived from radiance data acquired by the Visible Infrared Imaging Radiometer Suite (VIIRS) on board the Suomi National Polar-orbiting Partnership (NPP) satellite. The data is a gridded composite, generated from 6 minute swaths, and projected to a 375 m Sinusoidal grid. Snow cover is identified using the Normalized Difference Snow Index (NDSI) and a series of screens designed to alleviate errors and flag uncertain snow cover detections.",
-            "title": "VIIRS/NPP Snow Cover Daily L3 Global 375m SIN Grid V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP10A1.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP10A1.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/daac/subscriptions.html",
-                    "description": "Subscribe to have new data automatically sent when the data become available.",
                     "@type": "dcat:Distribution",
+                    "description": "Subscribe to have new data automatically sent when the data become available.",
+                    "downloadURL": "http://nsidc.org/daac/subscriptions.html",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VNP10A1.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VNP10A1.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VNP10A1+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VNP10A1+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/VNP10A1/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/VNP10A1/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP10A1.001",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP10A1.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP10A1.001",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP10A1.001",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1600510471-NSIDC_ECS",
+            "issued": "2012-01-19",
+            "keyword": [
+                "cryosphere",
+                "snow/ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP10A1.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-06-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-06-24T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Snow Cover Daily L3 Global 375m SIN Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1285-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-25T19:23:50.000 to 2015-12-25T22:01:15.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1285-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1285-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1285-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-25T19:23:50.000 to 2015-12-25T22:01:15.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1285 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1285 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/75",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seastedt, T. R., and C. L. Turner. 1994. Root Biomass Data (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/75",
-            "issued": "2024-05-06",
-            "temporal": "1987-06-01T00:00:00Z/1987-11-12T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
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
-            "identifier": "C2980527540-ORNL_CLOUD",
             "description": "Plant root biomass data where grazing height/frequency were simulated by mowing",
-            "graphic-preview-description": "Browse Image",
-            "title": "Root Biomass Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F75",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F75",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_root_bio/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_root_bio/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Root_Biomass_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Root_Biomass_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/75",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/75",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_root_bio/comp/root_bio.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_root_bio/comp/root_bio.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_root_bio/comp/root_bio.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_root_bio/comp/root_bio.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_root_bio/comp/Root_Biomass_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_root_bio/comp/Root_Biomass_Data.pdf",
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
+            "identifier": "C2980527540-ORNL_CLOUD",
+            "issued": "2024-05-06",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/75",
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
             "spatial": "-96.61 38.98 -96.47 39.12",
+            "temporal": "1987-06-01T00:00:00Z/1987-11-12T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Root Biomass Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0639-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-12T10:22:50.000 to 2015-03-12T21:46:54.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0639-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0639-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0639-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-12T10:22:50.000 to 2015-03-12T21:46:54.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0639 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0639 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0688-5-CMORMETORB-V1.0",
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
-                "meteoroid",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A seven-year radar survey of meteor showers has been carried out with the Canadian Meteor Orbit Radar (CMOR) from 2002-2006 (Brown et al. 2008). This survey resulted in the unambiguous detection and orbital characterization of 45 major and minor meteor showers. This data set includes this list of the detected meteor showers along with their orbital parameters.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0688-5-cmormetorb-v1.0_eeyv-c2e3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "meteoroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0688-5-CMORMETORB-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0688-5-cmormetorb-v1.0_eeyv-c2e3",
-            "description": "A seven-year radar survey of meteor showers has been carried out with the Canadian Meteor Orbit Radar (CMOR) from 2002-2006 (Brown et al. 2008). This survey resulted in the unambiguous detection and orbital characterization of 45 major and minor meteor showers. This data set includes this list of the detected meteor showers along with their orbital parameters.",
-            "title": "CMOR METEOROID STREAM SURVEY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CMOR METEOROID STREAM SURVEY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CH4NS_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-03-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2CH4NS_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "air quality",
-                "atmospheric chemistry",
-                "atmosphere",
-                "atmospheric temperature",
-                "clouds",
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
-            "identifier": "C1331182632-LARC",
             "description": "TL2CH4NS_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Methane Nadir Special Observation Version 7 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object represented one of these sets. Thus, each limb standard product consisted of three swath objects, one for each observation, Limb 1, Limb",
-            "title": "TES/Aura L2 Methane Nadir Special Observation V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CH4NS_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CH4NS_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182632-LARC",
-                    "description": "Earthdata Search for TL2CH4NS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2CH4NS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182632-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CH4NS_L2.007",
-                    "description": "DOI data set landing page for TL2CH4NS_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2CH4NS_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CH4NS_L2.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CH4NS.007/contents.html",
-                    "description": "OPeNDAP data access for TL2CH4NS_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2CH4NS_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CH4NS.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CH4NS.007/",
-                    "description": "ASDC Direct Data Download for TL2CH4NS_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2CH4NS_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CH4NS.007/",
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
                 }
             ],
+            "identifier": "C1331182632-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "air quality",
+                "atmospheric chemistry",
+                "atmosphere",
+                "atmospheric temperature",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CH4NS_L2.007",
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
+            "title": "TES/Aura L2 Methane Nadir Special Observation V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHG16-2PO27",
             "citation": "NOAA/NESDIS/STAR. 2019-05-15. GHRSST NOAA/STAR GOES-16 ABI L2P America Region SST dataset in GDS2. Version 2.70. GHRSST Sea Surface Temperature 30W-135W and 65N-50S at 0.036 degree resolution from GOES-16 ABI. Camp Springs, MD (USA). Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHG16-2PO27.",
-            "issued": "2019-03-28",
-            "temporal": "2017-12-15T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-28",
-            "references": [
-                "https://doi.org/10.3390/rs8010079"
-            ],
-            "keyword": [
-                "ocean temperature",
-                "earth science",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036877465-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "GOES-16 (G16) is the first satellite in the US NOAA third generation of Geostationary Operational Environmental Satellites (GOES), a.k.a. GOES-R series (which will also include -S, -T, and -U). G16 was launched on 19 Nov 2016 and initially placed in an interim position at 89.5-deg W, between GOES-East and -West. Upon completion of Cal/Val in Dec 2018, it was moved to its permanent position at 75.2-deg W, and declared NOAA operational GOES-East on 18 Dec 2018. \r\nNOAA is responsible for all GOES-R products, including Sea Surface Temperature (SST) from the Advanced Baseline Imager (ABI). The ABI offers vastly enhanced capabilities for SST retrievals, over the heritage GOES-I/P Imager, including five narrow bands (centered at 3.9, 8.4, 10.3, 11.2, and 12.3 um) out of 16 that can be used for SST, as well as accurate sensor calibration, image navigation and co-registration, spectral fidelity, and sophisticated pre-processing (geo-rectification, radiance equalization, and mapping). From altitude 35,800 km, G16/ABI can accurately map SST in a Full Disk (FD) area from 15-135-deg W and 60S-60N, with spatial resolution 2km at nadir (degrading to 15km at view zenith angle, 67-deg) and temporal sampling of 10min (15min prior to 2 Apr 2019). \r\nThe Level 2 Preprocessed (L2P) SST product is derived at the native sensor resolution using NOAA Advanced Clear-Sky Processor for Ocean (ACSPO) system. ACSPO first processes every 10min FD data SSTs are derived from BTs using the ACSPO clear-sky mask (ACSM; Petrenko et al., 2010) and Non-Linear SST (NLSST) algorithm (Petrenko et al., 2014). Currently, only 4 longwave bands centered at 8.4, 10.3, 11.2, and 12.3 um are used (the 3.9 microns was initially excluded, to minimize possible discontinuities in the diurnal cycle). The regression is tuned against quality controlled in situ SSTs from drifting and tropical mooring buoys in the NOAA iQuam system (Xu and Ignatov, 2014). The 10-min FD data are subsequently collated in time, to produce 1-hr L2P product, with improved coverage, and reduced cloud leakages and image noise, compared to each individual 10min image. \r\nIn the collated L2P, SSTs and BTs are only reported in clear-sky water pixels (defined as ocean, sea, lake or river, and up to 5 km inland) and fill values elsewhere. The L2P is reported in netCDF4 GHRSST Data Specification version 2 (GDS2) format, 24 granules per day, with a total data volume of 0.6GB/day. In addition to SST, ACSPO files also include sun-sensor geometry, four BTs in ABI bands 11 (8.4um), 13 (10.3um), 14 (11.2um), and 15 (12.3um) and two reflectances in bands 2 and 3 (0.64um and 0.86um; used for cloud identification). The l2p_flags layer includes day/night, land, ice, twilight, and glint flags. Other variables include NCEP wind speed and ACSPO SST minus reference SST (Canadian Met Centre 0.1deg L4 SST; available at https://podaac.jpl.nasa.gov/dataset/CMC0.1deg-CMC-L4-GLOB-v3.0).\r\nPixel-level earth locations are not reported in the granules, as they remain unchanged from granule to granule. To obtain those, user has a choice of using a flat lat-lon file, or a Python script, both available at ftp://ftp.star.nesdis.noaa.gov/pub/socd4/coastwatch/sst/nrt/abi/nav/. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (SSES bias and standard deviation) are reported in each pixel. \r\nThe ACSPO VIIRS L2P product is monitored and validated against in situ data (Xu and Ignatov, 2014) using the Satellite Quality Monitor SQUAM (Dash et al, 2010), and BTs are validated against RTM simulation in MICROS (Liang and Ignatov, 2011). A reduced size (0.2GB/day), equal-angle gridded (0.02-deg resolution), ACSPO L3C product is also available at https://podaac.jpl.nasa.gov/dataset/ABI_G16-STAR-L3C-v2.70, where gridded L2P SSTs are reported, and BT layers omitted.",
-            "release-place": "Camp Springs, MD (USA)",
-            "series-name": "GHRSST NOAA/STAR GOES-16 ABI L2P America Region SST dataset in GDS2",
             "creator": "NOAA/NESDIS/STAR",
-            "title": "GHRSST NOAA/STAR GOES-16 ABI L2P America Region SST v2.70 dataset in GDS2",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ABI_G16-STAR-L2P-v2.70.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "GOES-16 (G16) is the first satellite in the US NOAA third generation of Geostationary Operational Environmental Satellites (GOES), a.k.a. GOES-R series (which will also include -S, -T, and -U). G16 was launched on 19 Nov 2016 and initially placed in an interim position at 89.5-deg W, between GOES-East and -West. Upon completion of Cal/Val in Dec 2018, it was moved to its permanent position at 75.2-deg W, and declared NOAA operational GOES-East on 18 Dec 2018. \r\nNOAA is responsible for all GOES-R products, including Sea Surface Temperature (SST) from the Advanced Baseline Imager (ABI). The ABI offers vastly enhanced capabilities for SST retrievals, over the heritage GOES-I/P Imager, including five narrow bands (centered at 3.9, 8.4, 10.3, 11.2, and 12.3 um) out of 16 that can be used for SST, as well as accurate sensor calibration, image navigation and co-registration, spectral fidelity, and sophisticated pre-processing (geo-rectification, radiance equalization, and mapping). From altitude 35,800 km, G16/ABI can accurately map SST in a Full Disk (FD) area from 15-135-deg W and 60S-60N, with spatial resolution 2km at nadir (degrading to 15km at view zenith angle, 67-deg) and temporal sampling of 10min (15min prior to 2 Apr 2019). \r\nThe Level 2 Preprocessed (L2P) SST product is derived at the native sensor resolution using NOAA Advanced Clear-Sky Processor for Ocean (ACSPO) system. ACSPO first processes every 10min FD data SSTs are derived from BTs using the ACSPO clear-sky mask (ACSM; Petrenko et al., 2010) and Non-Linear SST (NLSST) algorithm (Petrenko et al., 2014). Currently, only 4 longwave bands centered at 8.4, 10.3, 11.2, and 12.3 um are used (the 3.9 microns was initially excluded, to minimize possible discontinuities in the diurnal cycle). The regression is tuned against quality controlled in situ SSTs from drifting and tropical mooring buoys in the NOAA iQuam system (Xu and Ignatov, 2014). The 10-min FD data are subsequently collated in time, to produce 1-hr L2P product, with improved coverage, and reduced cloud leakages and image noise, compared to each individual 10min image. \r\nIn the collated L2P, SSTs and BTs are only reported in clear-sky water pixels (defined as ocean, sea, lake or river, and up to 5 km inland) and fill values elsewhere. The L2P is reported in netCDF4 GHRSST Data Specification version 2 (GDS2) format, 24 granules per day, with a total data volume of 0.6GB/day. In addition to SST, ACSPO files also include sun-sensor geometry, four BTs in ABI bands 11 (8.4um), 13 (10.3um), 14 (11.2um), and 15 (12.3um) and two reflectances in bands 2 and 3 (0.64um and 0.86um; used for cloud identification). The l2p_flags layer includes day/night, land, ice, twilight, and glint flags. Other variables include NCEP wind speed and ACSPO SST minus reference SST (Canadian Met Centre 0.1deg L4 SST; available at https://podaac.jpl.nasa.gov/dataset/CMC0.1deg-CMC-L4-GLOB-v3.0).\r\nPixel-level earth locations are not reported in the granules, as they remain unchanged from granule to granule. To obtain those, user has a choice of using a flat lat-lon file, or a Python script, both available at ftp://ftp.star.nesdis.noaa.gov/pub/socd4/coastwatch/sst/nrt/abi/nav/. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (SSES bias and standard deviation) are reported in each pixel. \r\nThe ACSPO VIIRS L2P product is monitored and validated against in situ data (Xu and Ignatov, 2014) using the Satellite Quality Monitor SQUAM (Dash et al, 2010), and BTs are validated against RTM simulation in MICROS (Liang and Ignatov, 2011). A reduced size (0.2GB/day), equal-angle gridded (0.02-deg resolution), ACSPO L3C product is also available at https://podaac.jpl.nasa.gov/dataset/ABI_G16-STAR-L3C-v2.70, where gridded L2P SSTs are reported, and BT layers omitted.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHG16-2PO27",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHG16-2PO27",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-netcdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/GOES16/STAR/docs/G16_075_0_W.nc",
-                    "description": "Example input file for python geolocation script",
                     "@type": "dcat:Distribution",
+                    "description": "Example input file for python geolocation script",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/GOES16/STAR/docs/G16_075_0_W.nc",
+                    "mediaType": "application/x-netcdf",
                     "title": "View the documentation for this dataset's algorithms"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ABI_G16-STAR-L2P-v2.70.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ABI_G16-STAR-L2P-v2.70.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
-                    "description": "SST Quality Monitor 2.1 Webpage",
                     "@type": "dcat:Distribution",
+                    "description": "SST Quality Monitor 2.1 Webpage",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
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
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
-                    "description": "in situ SST Quality Monitor v2.10 Webpage",
                     "@type": "dcat:Distribution",
+                    "description": "in situ SST Quality Monitor v2.10 Webpage",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
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
-                    "downloadURL": "https://www.ghrsst.org/",
-                    "description": "Home Page of the GHRSST Project",
                     "@type": "dcat:Distribution",
+                    "description": "Home Page of the GHRSST Project",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877465-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877465-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877465-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877465-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ABI_G16-STAR-L2P-v2.70.jpg",
+            "identifier": "C2036877465-POCLOUD",
+            "issued": "2019-03-28",
+            "keyword": [
+                "ocean temperature",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHG16-2PO27",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-28",
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
+            "series-name": "GHRSST NOAA/STAR GOES-16 ABI L2P America Region SST dataset in GDS2",
             "spatial": "-135.0 -59.0 -15.0 59.0",
+            "temporal": "2017-12-15T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST NOAA/STAR GOES-16 ABI L2P America Region SST v2.70 dataset in GDS2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-LRD-3-ENTRY-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Data from this instrument appear to have been lost due to the death of Co-Investigator Klaus Rinnert. Please refer to the following publications for results from this instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-lrd-3-entry-v1.0_ef78-rebd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-LRD-3-ENTRY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-lrd-3-entry-v1.0_ef78-rebd",
-            "description": "Data from this instrument appear to have been lost due to the death of Co-Investigator Klaus Rinnert. Please refer to the following publications for results from this instrument.",
-            "title": "GALILEO PROBE LRD RAW DATA SET",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO PROBE LRD RAW DATA SET"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ef88-sg27",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Martian regolith (unconsolidated surface material) is a potential medium for plant growth in bioregenerative life support systems during manned missions on Mars. However hydrated magnesium sulfate mineral levels in the regolith of Mars can reach as high as 10 wt% and would be expected to be highly inhibitory to plant growth. A global approach was used to identify novel genes with potential to enhance tolerance to high MgSO4 stress. The early Arabidopsis root transcriptome response to elevated concentrations of magnesium sulfate was characterized in col-0 and also between col-0 and the mutant line cax1-1 - a mutant relatively tolerant of high levels of MgSO4-7H2O in soil solution. After 3 weeks of growth under hydroponic conditions Arabidopsis thaliana col-0 roots were exposed to a basic nutrient solution (0.25 g/L MES 1/16x MS pH 5.7) with an additional 2.08 mM magnesium sulfate (total Ca:Mg ratio = 1:15) for 45 min. 90 min. or 180 min. while a col-0 control set was exposed to the basic nutrient solution without additional magnesium sulfate for 45 minutes. Arabidopsis thaliana cax1-1 roots were exposed to the basic nutrient solution with additional magnesium sulfate for 180 min. only. Four replicate containers were harvested for the control and each of the treatment sets resulting in a total of 20 samples. Gene expression of the col-0 sets exposed to magnesium sulfate treatment for 45 min. 90 min. or 180 min. was compared to gene expression of the col-0 control set. Gene expression of the cax1-1 set exposed to magnesium sulfate treatment for 180 min. was compared to gene expression of the col-0 set exposed to magnesium sulfate treatment for 180 minutes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-22",
+                    "mediaType": "text/html",
+                    "title": "Root transcriptome remodeling of Arabidopsis in response to high levels of magnesium sulfate"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-22_ef88-sg27",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic_acid_extraction",
                 "bioassay_data_transformation",
@@ -702486,72 +702500,34 @@
                 "image_aquisition",
                 "labeling"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/ef88-sg27",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-22_ef88-sg27",
-            "description": "Martian regolith (unconsolidated surface material) is a potential medium for plant growth in bioregenerative life support systems during manned missions on Mars. However hydrated magnesium sulfate mineral levels in the regolith of Mars can reach as high as 10 wt% and would be expected to be highly inhibitory to plant growth. A global approach was used to identify novel genes with potential to enhance tolerance to high MgSO4 stress. The early Arabidopsis root transcriptome response to elevated concentrations of magnesium sulfate was characterized in col-0 and also between col-0 and the mutant line cax1-1 - a mutant relatively tolerant of high levels of MgSO4-7H2O in soil solution. After 3 weeks of growth under hydroponic conditions Arabidopsis thaliana col-0 roots were exposed to a basic nutrient solution (0.25 g/L MES 1/16x MS pH 5.7) with an additional 2.08 mM magnesium sulfate (total Ca:Mg ratio = 1:15) for 45 min. 90 min. or 180 min. while a col-0 control set was exposed to the basic nutrient solution without additional magnesium sulfate for 45 minutes. Arabidopsis thaliana cax1-1 roots were exposed to the basic nutrient solution with additional magnesium sulfate for 180 min. only. Four replicate containers were harvested for the control and each of the treatment sets resulting in a total of 20 samples. Gene expression of the col-0 sets exposed to magnesium sulfate treatment for 45 min. 90 min. or 180 min. was compared to gene expression of the col-0 control set. Gene expression of the cax1-1 set exposed to magnesium sulfate treatment for 180 min. was compared to gene expression of the col-0 set exposed to magnesium sulfate treatment for 180 minutes.",
-            "title": "Root transcriptome remodeling of Arabidopsis in response to high levels of magnesium sulfate",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-22",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Root transcriptome remodeling of Arabidopsis in response to high levels of magnesium sulfate"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Root transcriptome remodeling of Arabidopsis in response to high levels of magnesium sulfate"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-08-24",
-            "temporal": "2021-08-24T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "station",
-                "coordinates",
-                "coords",
-                "ephemeris",
-                "international",
-                "iss",
-                "location",
-                "space",
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
-            "identifier": "nasa-iss-data_2021-08-24_ef8b-gs7p",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-08-24",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -702674,92 +702650,92 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-08-24_ef8b-gs7p",
+            "issued": "2021-08-24",
+            "keyword": [
+                "station",
+                "coordinates",
+                "coords",
+                "ephemeris",
+                "international",
+                "iss",
+                "location",
+                "space",
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
+            "temporal": "2021-08-24T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-08-24"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-PRL-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Prelanding mission phase, which took place between 2014-01-21 and 2014-11-19.  The current V3.0 data set supersedes the previous V2.0 data set with improved documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-prl-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-PRL-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-prl-v3.0",
-            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Prelanding mission phase, which took place between 2014-01-21 and 2014-11-19.  The current V3.0 data set supersedes the previous V2.0 data set with improved documentation.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 PRL V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 PRL V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114206-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOMS Science Team. 2011-02-24. TOMSEPOVP. Version 008. TOMS Earth Probe Ground Station Overpass Data V008. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOMSEPOVP_008.html. Digital Science Data.",
-            "issued": "2007-06-01",
-            "temporal": "1996-07-22T00:00:00Z/2005-12-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-06-01",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "atmospheric chemistry",
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
-            "identifier": "C1237114206-GES_DISC",
-            "description": "The Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 daily ground station overpass data product contains total column ozone, UV aerosol index, Lambertian effective surface reflectivity (Rayleigh corrected), UV aerosol index and sulfur dioxide index values. The overpass data files contain the data derived from the best-matched TOMS field-of-view (FOV) to a site for every day the TOMS instrument was operational. The data are stored in an ASCII format.\n\nTOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TOMSEPOVP",
             "creator": "TOMS Science Team",
-            "title": "TOMS Earth Probe Ground Station Overpass Data V008 (TOMSEPOVP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPOVP_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 daily ground station overpass data product contains total column ozone, UV aerosol index, Lambertian effective surface reflectivity (Rayleigh corrected), UV aerosol index and sulfur dioxide index values. The overpass data files contain the data derived from the best-matched TOMS field-of-view (FOV) to a site for every day the TOMS instrument was operational. The data are stored in an ASCII format.\n\nTOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -702768,205 +702744,231 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPOVP_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPOVP_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPOVP.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPOVP.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPOVP",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPOVP",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPOVP_008.png",
+            "identifier": "C1237114206-GES_DISC",
+            "issued": "2007-06-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "atmospheric chemistry",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114206-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-06-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TOMSEPOVP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-07-22T00:00:00Z/2005-12-13T23:59:59.999Z",
             "theme": [
                 "TOMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS Earth Probe Ground Station Overpass Data V008 (TOMSEPOVP) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/517",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rapalee, G., E.A. Davidson, J.W. Harden, S.E. Trumbore, and H. Veldhuis. 2000. BOREAS TGB-12 Soil Carbon and Flux Data of NSA-MSA in Raster Format. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/517",
-            "issued": "2023-11-22",
-            "temporal": "1937-01-01T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "ecological dynamics",
-                "agriculture",
-                "earth science",
-                "biosphere",
-                "ecosystems",
-                "vegetation",
-                "terrestrial hydrosphere",
-                "surface water",
-                "soils",
-                "land use/land cover",
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
-            "identifier": "C2808093149-ORNL_CLOUD",
             "description": "This data set contains (1) estimates of soil carbon stocks by horizon based on soil survey data and analyses of data from individual soil profiles; (2) estimates of soil carbon fluxes based on stocks, fire history, drainage, and soil C inputs and decomposition constants based on field work using radiocarbon analyses; (3) fire history data estimating age ranges of time since last fire; (4) a raster image and an associated soils table file from which area-weighted maps of soil carbon and fluxes and fire history may be generated.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-12 Soil Carbon and Flux Data of NSA-MSA in Raster Format",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F517",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F517",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb12cfd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb12cfd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB12_Soil_Carbon_Map.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB12_Soil_Carbon_Map.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/517",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/517",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/nsa_soil_carbon_hdr.asc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/nsa_soil_carbon_hdr.asc",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/nsa_soil_carbon_poly_attrib.asc.gz",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/nsa_soil_carbon_poly_attrib.asc.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/rapalee_thesis.tar.gz",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/rapalee_thesis.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/TGB12_Soil_Carbon_Map.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/TGB12_Soil_Carbon_Map.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/TGB12_Soil_Carbon_Map.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/TGB12_Soil_Carbon_Map.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/TGB12_Soil_Carbon_Map.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/TGB12_Soil_Carbon_Map.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/TGB12_Soil_Carbon_Map.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12cfd/comp/TGB12_Soil_Carbon_Map.txt",
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
+            "identifier": "C2808093149-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "ecological dynamics",
+                "agriculture",
+                "earth science",
+                "biosphere",
+                "ecosystems",
+                "vegetation",
+                "terrestrial hydrosphere",
+                "surface water",
+                "soils",
+                "land use/land cover",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/517",
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
+            "temporal": "1937-01-01T00:00:00Z/1996-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-12 Soil Carbon and Flux Data of NSA-MSA in Raster Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-3-VIRS-CDR-CALDATA-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS calibrated observations, also known as CDRs. The MASCS VIRS experiment is a fixed concave grating spectrograph with a beam splitter that simultaneously disperses the spectrum onto two photodiode arrays. There are two VIRS CDR data products, one for each array, which result in coverage of the wavelength ranges of the visible (VIS) and near infrared (NIR).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-3-virs-cdr-caldata-v1.0_efds-7p7s",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "messenger",
@@ -702974,223 +702976,223 @@
                 "earth",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-3-VIRS-CDR-CALDATA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-3-virs-cdr-caldata-v1.0_efds-7p7s",
-            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS calibrated observations, also known as CDRs. The MASCS VIRS experiment is a fixed concave grating spectrograph with a beam splitter that simultaneously disperses the spectrum onto two photodiode arrays. There are two VIRS CDR data products, one for each array, which result in coverage of the wavelength ranges of the visible (VIS) and near infrared (NIR).",
-            "title": "MESSENGER E/V/H MASCS 3 VIRS CALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESSENGER E/V/H MASCS 3 VIRS CALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/GAUGES/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A, David  Wolff, Jianxin  Wang and Ali  Tokay.2017. GPM Ground Validation Met One Rain Gauge Pairs OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/GAUGES/DATA201",
-            "issued": "2017-05-25",
-            "temporal": "2015-01-01T17:25:00Z/2016-06-20T10:26:00Z",
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
-            "identifier": "C1979701018-GHRC_DAAC",
             "description": "The GPM Ground Validation Met One Rain Gauge Pairs OLYMPEX dataset contains precipitation amount and precipitation rate data collected during the Global Precipitation Measurement mission (GPM) Ground Validation (GV) Olympic Mountains Experiment (OLYMPEX). The OLYMPEX field campaign took place between November 2015 and January 2016, with additional ground sampling continuing through February 2016, on the Olympic Peninsula in the Pacific Northwest of the United States. The purpose of the campaign was to provide ground-validation data for the measurements taken by instrumentation aboard the GPM Core Observatory satellite. The Met One Rain Gauge Pairs are tipping bucket precipitation gauges which collect precipitation amounts and calculate precipitation rates. This dataset contains two ASCII-tsv files per rain gauge and two rain gauges are located on each station platform. The Met One Rain Gauge Pairs OLYMPEX dataset files are available from January 1, 2015 through June 20, 2016 in ASCII-tsv format.",
-            "title": "GPM Ground Validation Met One Rain Gauge Pairs OLYMPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FGAUGES%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FGAUGES%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmrgnaolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmrgnaolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://s.campbellsci.com/documents/us/manuals/met1.pdf",
-                    "description": "Met One Rain Gage Models 380 and 385",
                     "@type": "dcat:Distribution",
+                    "description": "Met One Rain Gage Models 380 and 385",
+                    "downloadURL": "https://s.campbellsci.com/documents/us/manuals/met1.pdf",
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
-                    "downloadURL": "http://olympex.atmos.washington.edu/",
-                    "description": "University of Washington OLYMPEX Web Site",
                     "@type": "dcat:Distribution",
+                    "description": "University of Washington OLYMPEX Web Site",
+                    "downloadURL": "http://olympex.atmos.washington.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/rain_gauge_NASA/doc/gpmrgnaolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/rain_gauge_NASA/doc/gpmrgnaolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/1520-0426(2003)20%3C752:LREITB%3E2.0.CO;2",
-                    "description": "Local Random Errors in Tipping-Bucket Rain Gauge Measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Local Random Errors in Tipping-Bucket Rain Gauge Measurements",
+                    "downloadURL": "http://dx.doi.org/10.1175/1520-0426(2003)20%3C752:LREITB%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/2009JHM1137.1",
-                    "description": "Comparison of Rain Gauge Measurements in the Mid-Atlantic Region",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison of Rain Gauge Measurements in the Mid-Atlantic Region",
+                    "downloadURL": "http://dx.doi.org/10.1175/2009JHM1137.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/2007JTECHA895.1",
-                    "description": "Estimating Rain Rates from Tipping-Bucket Rain Gauge Measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Estimating Rain Rates from Tipping-Bucket Rain Gauge Measurements",
+                    "downloadURL": "http://dx.doi.org/10.1175/2007JTECHA895.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/2009JAMC2264.1",
-                    "description": "Evaluation of TRMM Ground-Validation Radar-Rain Errors Using Rain Gauge Measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluation of TRMM Ground-Validation Radar-Rain Errors Using Rain Gauge Measurements",
+                    "downloadURL": "http://dx.doi.org/10.1175/2009JAMC2264.1",
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
-                    "downloadURL": "https://doi.org/10.1175/JAMC-D-11-080.1",
-                    "description": "Evaluation of TRMM rain estimates using ground measurements over central Florida",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluation of TRMM rain estimates using ground measurements over central Florida",
+                    "downloadURL": "https://doi.org/10.1175/JAMC-D-11-080.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/olympex",
-                    "description": "OLYMPEX Field Campaign Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OLYMPEX Field Campaign Project Home Page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/olympex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
+            "identifier": "C1979701018-GHRC_DAAC",
+            "issued": "2017-05-25",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/GAUGES/DATA201",
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
             "spatial": "-124.369 46.4478 -122.631 48.0795",
+            "temporal": "2015-01-01T17:25:00Z/2016-06-20T10:26:00Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Met One Rain Gauge Pairs OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-3%2F4-9P-ENCOUNTER-V1.0",
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
+            "description": "This data set contains reduced spectral images of 9P/Tempel 1 acquired by the Deep Impact High Resolution Instrument Infrared Spectrometer during the encounter phase of the mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-3-4-9p-encounter-v1.0_efgt-crxm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "9p/tempel 1 (1867 g1)",
+                "deep impact"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-3%2F4-9P-ENCOUNTER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-3-4-9p-encounter-v1.0_efgt-crxm",
-            "description": "This data set contains reduced spectral images of 9P/Tempel 1 acquired by the Deep Impact High Resolution Instrument Infrared Spectrometer during the encounter phase of the mission.",
-            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED HRII SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED HRII SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-5-RTS-MOMENTS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-5-rts-moments-v1.0_efhg-qwws",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "callisto",
                 "jupiter",
@@ -703199,917 +703201,888 @@
                 "galileo",
                 "europa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-5-RTS-MOMENTS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-5-rts-moments-v1.0_efhg-qwws",
-            "description": "TBD",
-            "title": "GALILEO JUPITER RTS MOMENT DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO JUPITER RTS MOMENT DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NIMBUS/NmTHIR67-3H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus Temperature-Humidity Infrared Radiometer 6.7 \u00b5m Water Vapor Remapped Digital Data Daily L3, HDF5 V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NIMBUS/NmTHIR67-3H.",
-            "issued": "1970-05-10",
-            "temporal": "1970-05-10T00:00:00Z/1971-03-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1971-03-25",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "atmospheric water vapor"
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
-            "identifier": "C1242109306-NSIDC_ECS",
             "description": "This data set (NmTHIR67-3H) consists of daily, global composites of radiative temperatures measured in the 6.7 \u00b5m water vapor window (6.5 \u00b5m - 7.0 \u00b5m) by the Temperature-Humidity Infrared Radiometer (THIR) onboard the Nimbus 4 satellite. The composites were constructed from Nimbus 4 THIR <a href=\"http://nsidc.org/data/nmthir67-1h/\">swath data</a> and show water vapor distribution in the upper troposphere and stratosphere.",
-            "title": "Nimbus Temperature-Humidity Infrared Radiometer 6.7 \u00b5m Water Vapor Remapped Digital Data Daily L3, HDF5 V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmTHIR67-3H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmTHIR67-3H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR67-3H.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR67-3H.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1242109306-NSIDC_ECS&m=-31.359375%211.96875%211%211%210%210%2C2&q=NmTHIR67-3H",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1242109306-NSIDC_ECS&m=-31.359375%211.96875%211%211%210%210%2C2&q=NmTHIR67-3H",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR67-3H/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR67-3H/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR67-3H",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR67-3H",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR67-3H",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR67-3H",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1242109306-NSIDC_ECS",
+            "issued": "1970-05-10",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/NIMBUS/NmTHIR67-3H",
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
+            "title": "Nimbus Temperature-Humidity Infrared Radiometer 6.7 \u00b5m Water Vapor Remapped Digital Data Daily L3, HDF5 V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3DUAE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Monthly Climatology Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3DUAE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Monthly Climatology Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
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
-            "identifier": "C2491756015-POCLOUD",
-            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution density data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the monthly climatology,\nAscending sea surface density product for version 5.0. Only retrieved values for Ascending passes have been used to create this product.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product).  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Monthly Climatology Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Monthly Climatology Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_MONTHLY-CLIMATOLOGY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution density data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the monthly climatology,\nAscending sea surface density product for version 5.0. Only retrieved values for Ascending passes have been used to create this product.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product).  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3DUAE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3DUAE",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_MONTHLY-CLIMATOLOGY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_MONTHLY-CLIMATOLOGY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756015-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756015-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756015-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756015-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_MONTHLY-CLIMATOLOGY_V5.jpg",
+            "identifier": "C2491756015-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3DUAE",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Monthly Climatology Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Monthly Climatology Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1076-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-04T03:04:55.000 to 2015-10-04T09:59:26.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1076-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1076-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1076-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-04T03:04:55.000 to 2015-10-04T09:59:26.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1076 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1076 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1332-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-11T11:43:25.000 to 2016-01-11T14:26:59.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1332-v1.0_efn8-d4yy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1332-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1332-v1.0_efn8-d4yy",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-11T11:43:25.000 to 2016-01-11T14:26:59.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1332 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1332 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MAG-3-PREMAPPING-HIGHRES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Calibrated high time resolution (detail word) from the MAG instrument on the MGS spacecraft, collected during the premapping and aerobraking mission phases (1997-09-12 to 1999-03-08) expressed in payload and Sun-State coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mag-3-premapping-highres-v1.0_efp9-c7n6",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "mars global surveyor"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MAG-3-PREMAPPING-HIGHRES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mag-3-premapping-highres-v1.0_efp9-c7n6",
-            "description": "Calibrated high time resolution (detail word) from the MAG instrument on the MGS spacecraft, collected during the premapping and aerobraking mission phases (1997-09-12 to 1999-03-08) expressed in payload and Sun-State coordinates.",
-            "title": "MGS MARS MAG CALIBRATED PREMAPPING DETAIL WORD RES. V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS MARS MAG CALIBRATED PREMAPPING DETAIL WORD RES. V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/efpb-rfsr",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "treatment protocol",
-                "ionizing radiation",
-                "nucleic acid sequencing",
-                "nucleic acid extraction",
-                "hindlimb unloading",
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
-            "identifier": "nasa_genelab_GLDS-335_efpb-rfsr",
             "description": "Biological risks associated with space radiation and microgravity are major concerns for long-term space travel. Through a Systems Biology approach our previous NASA work has shown both TGF xce xb2 signaling pathways and miRNAs have a critical impact on defining health risks with and without space irradiation. We hypothesize that circulating microRNA (miRNA) signatures are driving microvascular disease and muscle degeneration associated with accelerating aging and will be enhanced by exposure to the space environment (radiation and microgravity). We investigated this hypothesis both in vivo and in vitro and test novel antagonist therapies to these miRNA signatures as countermeasures to reduce space radiation-induced health risks. A comprehensive Systems Biology approach was used to examine the influence by high atomic number by high (H) atomic number (Z) and energy (E) (HZE) irradiation. To simulate low-dose exposure due to galactic cosmic rays (GCR) we used the ions energy and doses determined by a NASA consensus formula of 7 different ions to represent GCR (referred to as GCR sim model). To simulate high-dose radiation exposure due to solar particle events (SPE) we used an acute dose of SPE simulated beam at 1Gy which has energies ranging from 50MeV to 150MeV. C57BL/6 wild-type mice were utilized for irradiation with our established simulated microgravity model (hindlimb suspension model) and an in vitro 3D microvasculature tissue model under simulated microgravity (clinostat) conditions will also be irradiated. To expand on the circulating miRNA signature determined from our preliminary data we determined a group of conserved miRNAs which are commonly being regulated in the majority of the organs and tissues throughout the host using our established techniques. MiRNA-sequencing on serum (before IR and at time of sacrifice) liver heart and muscle tissue for all radiation groups revealed the key circulating miRNA signature (consisting of multiple miRNAs) impacting disease risk. Collectively understanding of how whole body space radiation impacts microvascular and tissue degeneration through circulating miRNAs will greatly enhance health risk prognostication and provide possible new mechanisms for protection against space radiation.",
-            "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Liver tissue",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-335",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-335",
+                    "mediaType": "text/html",
                     "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Liver tissue"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-335_efpb-rfsr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "treatment protocol",
+                "ionizing radiation",
+                "nucleic acid sequencing",
+                "nucleic acid extraction",
+                "hindlimb unloading",
+                "library construction"
+            ],
+            "landingPage": "https://data.nasa.gov/d/efpb-rfsr",
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
+            "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Liver tissue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3YCLDN_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Global Cloud public Product in netCDF format covering a year;See ProductionDateTime for Published date.",
-            "issued": "2006-03-01",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
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
-            "identifier": "C108919911-LARC",
             "description": "This file contains the MISR Level 3 Global Cloud public Product in netCDF format covering a year",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Global Cloud public Product in netCDF format covering a year V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3YCLDN_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3YCLDN_L3.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C108919911-LARC",
+            "issued": "2006-03-01",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3YCLDN_L3.002",
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
+            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Global Cloud public Product in netCDF format covering a year V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/USWCD-ALT01",
             "citation": "OSU/COAS. 2012-12-17. Gridded Altimeter Fields with Enhanced Coastal Coverage Daily. Version 1. Gridded Altimeter Fields with Enhanced Coastal Coverage Daily. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, OSU/COAS. https://doi.org/10.5067/USWCD-ALT01.",
-            "issued": "2012-11-09",
-            "temporal": "1992-10-14T12:00:00Z/2011-01-19T12:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "references": [
-                "https://doi.org/10.1029/2008JC004756"
-            ],
-            "keyword": [
-                "earth science",
-                "sea surface topography",
-                "oceans",
-                "ocean circulation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036882016-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The Gridded Altimeter Fields with Enhanced Coastal Coverage data product contains Sea Surface Height Anomalies (SSHA or SLA) and zonal and meridional geostrophic velocities for the US west coast encompassing 35.25 deg-48.5 deg N latitude and 227.75 deg-248.5 deg E longitude.  This annually updated data product extends from October 14, 1992 through January 19, 2011.  SSHA and current velocities are derived from the AVISO quarter degree DT UPD MSLA version 3.0 grids, 0.75 deg and greater away from the coast.  Values within 0.75 deg of the coast are derived from tide gauge observations and interpolated out to the altimeter filled region.  Details on how these data are derived can be found in: Saraceno, M., P. T. Strub, and P. M. Kosro (2008), Estimates of sea surface height and near-surface alongshore coastal currents from combinations of altimeters and tide gauges, J. Geophys. Res., 113, C11013, doi:10.1029/2008JC004756.",
-            "release-place": "JPL",
-            "series-name": "Gridded Altimeter Fields with Enhanced Coastal Coverage Daily",
             "creator": "OSU/COAS",
-            "title": "Gridded Altimeter Fields with Enhanced Coastal Coverage Daily",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST_DAILY.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Gridded Altimeter Fields with Enhanced Coastal Coverage data product contains Sea Surface Height Anomalies (SSHA or SLA) and zonal and meridional geostrophic velocities for the US west coast encompassing 35.25 deg-48.5 deg N latitude and 227.75 deg-248.5 deg E longitude.  This annually updated data product extends from October 14, 1992 through January 19, 2011.  SSHA and current velocities are derived from the AVISO quarter degree DT UPD MSLA version 3.0 grids, 0.75 deg and greater away from the coast.  Values within 0.75 deg of the coast are derived from tide gauge observations and interpolated out to the altimeter filled region.  Details on how these data are derived can be found in: Saraceno, M., P. T. Strub, and P. M. Kosro (2008), Estimates of sea surface height and near-surface alongshore coastal currents from combinations of altimeters and tide gauges, J. Geophys. Res., 113, C11013, doi:10.1029/2008JC004756.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUSWCD-ALT01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUSWCD-ALT01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST_DAILY.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST_DAILY.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882016-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882016-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882016-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882016-POCLOUD",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/coastal_alt/preview/L4/OSU_COAS/docs/Coastal_alt_readme.txt",
-                    "description": "Gridded Altimeter Fields with Enhanced Coastal Coverage README",
                     "@type": "dcat:Distribution",
+                    "description": "Gridded Altimeter Fields with Enhanced Coastal Coverage README",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/coastal_alt/preview/L4/OSU_COAS/docs/Coastal_alt_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST_DAILY.jpg",
+            "identifier": "C2036882016-POCLOUD",
+            "issued": "2012-11-09",
+            "keyword": [
+                "earth science",
+                "sea surface topography",
+                "oceans",
+                "ocean circulation"
+            ],
+            "landingPage": "https://doi.org/10.5067/USWCD-ALT01",
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
+                "https://doi.org/10.1029/2008JC004756"
+            ],
+            "release-place": "JPL",
+            "series-name": "Gridded Altimeter Fields with Enhanced Coastal Coverage Daily",
             "spatial": "-133.0 35.0 -111.0 49.0",
+            "temporal": "1992-10-14T12:00:00Z/2011-01-19T12:00:00Z",
             "theme": [
                 "CIOSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gridded Altimeter Fields with Enhanced Coastal Coverage Daily"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-HET-3-RDR-FLUX-HIRES-V1.0",
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
-                "ulysses"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Data ====",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-het-3-rdr-flux-hires-v1.0_efqm-uy4r",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-HET-3-RDR-FLUX-HIRES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-het-3-rdr-flux-hires-v1.0_efqm-uy4r",
-            "description": "Data ====",
-            "title": "ULY JUP COSPIN HIGH ENERGY TELESCOPE HIGH RES. PARTICLE FLUX",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULY JUP COSPIN HIGH ENERGY TELESCOPE HIGH RES. PARTICLE FLUX"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/CFL/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/CFL/DATA001.",
-            "issued": "2008-03-24",
-            "temporal": "2008-03-24T00:00:02Z/2008-08-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "ocean temperature",
-                "ocean optics",
-                "oceans",
-                "ocean chemistry",
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
-            "identifier": "C2131352566-OB_DAAC",
             "description": "Measurements taken within the Cape Bathurst flaw lead on board the icebreaker C.C.G.S. Amundsen to examine how physical changes affect biological processes in the flaw lead\u00a0through an entire annual cycle (October 2007 - August 2008). The circumpolar flaw lead occurs each year when the central pack ice moves away from the coastal fast ice creating an area of open water called a flaw lead.",
-            "title": "Circumpolar\u00a0Flaw Lead System Study",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCFL%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCFL%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/CFL/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/CFL/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2131352566-OB_DAAC",
+            "issued": "2008-03-24",
+            "keyword": [
+                "earth science",
+                "ocean temperature",
+                "ocean optics",
+                "oceans",
+                "ocean chemistry",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/CFL/DATA001",
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
+            "temporal": "2008-03-24T00:00:02Z/2008-08-08T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Circumpolar\u00a0Flaw Lead System Study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2032",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Macander, M.J., and P.R. Nelson. 2022. ABoVE: Modeled Top Cover by Plant Functional Type over Alaska and Yukon, 1985-2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2032",
-            "issued": "2022-05-31",
-            "temporal": "1985-01-01T00:00:00Z/2020-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "ecosystems",
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
-            "identifier": "C2262496056-ORNL_CLOUD",
             "description": "This dataset contains data files of modeled top cover estimates by plant functional type (PFT) for the Arctic and Boreal Alaska and Yukon regions. Estimates are presented for single years at 5-year intervals from 1985 to 2020. Also included are root mean square error (RMSE) and source year, which indicate the specific year from which pixels in the top cover maps were derived. Plant functional types include conifer trees, broadleaf trees, deciduous shrubs, evergreen shrubs, graminoids, forbs, and light macrolichens. Estimates were derived through the combination of two stochastic gradient-boosting models that used environmental and spectral covariates. Environmental covariates represented topographic, climatic, permafrost, hydrographic, and phenological gradients, and spectral covariates were based on Landsat Thematic Mapper (TM), Enhanced Thematic Mapper Plus (ETM+), and Operational Land Imager (OLI) data collected between 1984-2020. These maps catalog widespread changes in the distribution of PFTs occurring in the Arctic and boreal forest ecosystems, such as tundra shrub expansion, due to the intensification of disturbances such as fire and climate-driven vegetation dynamics.",
-            "graphic-preview-description": "Map of deciduous shrub top cover over the study region in 2020.",
-            "title": "ABoVE: Modeled Top Cover by Plant Functional Type over Alaska and Yukon, 1985-2020",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/AK_Yukon_PFT_TopCover_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2032",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2032",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/AK_Yukon_PFT_TopCover/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/AK_Yukon_PFT_TopCover/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/AK_Yukon_PFT_TopCover.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/AK_Yukon_PFT_TopCover.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2032",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2032",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/AK_Yukon_PFT_TopCover/comp/AK_Yukon_PFT_TopCover.pdf",
-                    "description": "ABoVE: Modeled Top Cover by Plant Functional Type over Alaska and Yukon, 1985-2020: AK_Yukon_PFT_TopCover.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Modeled Top Cover by Plant Functional Type over Alaska and Yukon, 1985-2020: AK_Yukon_PFT_TopCover.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/AK_Yukon_PFT_TopCover/comp/AK_Yukon_PFT_TopCover.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/AK_Yukon_PFT_TopCover_Fig1.jpg",
-                    "description": "Map of deciduous shrub top cover over the study region in 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "Map of deciduous shrub top cover over the study region in 2020.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/AK_Yukon_PFT_TopCover_Fig1.jpg",
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
+            "graphic-preview-description": "Map of deciduous shrub top cover over the study region in 2020.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/AK_Yukon_PFT_TopCover_Fig1.jpg",
+            "identifier": "C2262496056-ORNL_CLOUD",
+            "issued": "2022-05-31",
+            "keyword": [
+                "ecosystems",
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2032",
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
             "spatial": "-176.1 51.0 -122.5 75.91",
+            "temporal": "1985-01-01T00:00:00Z/2020-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Modeled Top Cover by Plant Functional Type over Alaska and Yukon, 1985-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA3006",
             "citation": "Quintus Kleipool. 2010-12-09. OMLER. Version 003. OMI/Aura Surface Reflectance Climatology L3 Global Gridded 0.5 degree x 0.5 degree V3. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA3006. https://disc.gsfc.nasa.gov/datacollection/OMLER_003.html. Digital Science Data.",
-            "issued": "2005-01-01",
-            "temporal": "2005-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2010-12-09",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2006.869987",
-                "https://doi.org/10.1109/TGRS.2006.872935",
-                "https://doi.org/10.1117/12.627013"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JENNIFER WEI",
                 "hasEmail": "mailto:jennifer.c.wei@nasa.gov"
             },
+            "creator": "Quintus Kleipool",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1266136069-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMI Earth Surface Reflectance Climatology product, OMLER (Global 0.5 degrees Lat/Lon grid) which is based on Version 003 Level-1B top of atmosphere upwelling radiance and incoming irradiance. OMI calibrated and geolocated radiances from 159 channels in UV1(264-311 nm), 557 channels in UV2 (307-383 nm) and 751 channels in VIS (349-504) spectral regions, spectral irradiances, calibration measurements, and all derived geophysical atmospheric products (Level-2 and 3) are archived at the NASA Goddard DAAC.\n\nOMLER spectral surface reflectance product contains monthly and yearly climatology of the Earth's surface Lambert Equivalent Reflectance (LER) for 23 wavelengths in the spectral range 309 to 500 nm, at a spatial resolution of 0.5 by 0.5 degrees. This LER is defined as the required reflectance of an isotropic surface needed to match the observed top of the atmosphere (TOA) reflectance in a pure Rayleigh scattering atmosphere under cloud free conditions and no aerosols. The climatology is based on statistical analysis of the three years of OMI version 03 radiance data (Oct 2004-Oct 2007). This product also provides minimum spectral surface reflectivity observed during the three year period.\n\nThe OMLER product file is produced in the version 5 Hierarchical Data Format (HDF-EOS5). It is roughly 300 MB in size.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMLER",
-            "creator": "Quintus Kleipool",
-            "title": "OMI/Aura Surface Reflectance Climatology L3 Global Gridded 0.5 degree x 0.5 degree V3 (OMLER) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMLER_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA3006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA3006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -704119,59 +704092,59 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMLER_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMLER_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level3/OMLER.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level3/OMLER.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMLER_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMLER_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level3/OMLER.003/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level3/OMLER.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMLER.003/doc/OMLER_README_V003.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMLER.003/doc/OMLER_README_V003.pdf",
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
@@ -704181,55 +704154,54 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMLER_003.png",
+            "identifier": "C1266136069-GES_DISC",
+            "issued": "2005-01-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA3006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2010-12-09",
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
+            "series-name": "OMLER",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Surface Reflectance Climatology L3 Global Gridded 0.5 degree x 0.5 degree V3 (OMLER) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.lpi.usra.edu/resources/cla/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1967-01-01/1972-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.lpi.usra.edu/resources/apollopanoramas/",
-                "http://www.lpi.usra.edu/resources/cla/",
-                "http://www.lpi.usra.edu/resources/lunarorbiter/",
-                "http://www.lpi.usra.edu/resources/lunar_orbiter/",
-                "http://www.lpi.usra.edu/resources/ranger/",
-                "http://planetarynames.wr.usgs.gov/"
-            ],
-            "keyword": [
-                "space science",
-                "imagery",
-                "lunar science",
-                "modeling",
-                "circulation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul Schenk",
                 "hasEmail": "mailto:rpif@lpi.usra.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000030__1",
             "description": "The Consolidated Lunar Atlas is a collection of the best photographic images of the moon, including low-oblique photography, full-moon photography, and tabular and positional plates.",
-            "title": "Consolidated Lunar Atlas",
-            "programCode": [
-                "026:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -704237,262 +704209,268 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "NASA-0000030__1",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "imagery",
+                "lunar science",
+                "modeling",
+                "circulation"
+            ],
+            "landingPage": "http://www.lpi.usra.edu/resources/cla/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.lpi.usra.edu/resources/apollopanoramas/",
+                "http://www.lpi.usra.edu/resources/cla/",
+                "http://www.lpi.usra.edu/resources/lunarorbiter/",
+                "http://www.lpi.usra.edu/resources/lunar_orbiter/",
+                "http://www.lpi.usra.edu/resources/ranger/",
+                "http://planetarynames.wr.usgs.gov/"
+            ],
             "spatial": "Lunar",
-            "accrualPeriodicity": "irregular",
+            "temporal": "1967-01-01/1972-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Consolidated Lunar Atlas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Xie, P.-P., J.E. Janowiak, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2011. ISLSCP II Gauge-Based Analyses of Daily Precipitation over Global Land Areas. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1001",
-            "issued": "2023-10-15",
-            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
-            "keyword": [
-                "precipitation",
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
-            "identifier": "C2784899029-ORNL_CLOUD",
             "description": "The objective of this work was to construct a long-term data set of daily precipitation on half degree and one degree latitude/longitude grids over the global land areas. The analyses are defined by interpolating station observations from GTS (Global Telecommunications System) gauges using the algorithm of Shepard (1968). The algorithm of Shepard (1968) has been widely used to interpolate gauge observations of monthly, pentad, and daily precipitation (Rudolf 1993, Xie et al. 1996). This algorithm is used to interpolate the irregularly distributed station observations onto grid points. The weighting coefficients are inversely proportional to the gauge-grid point distance and are adjusted by a cosine function taking into account the directional isolation of each gauge relative to all other nearby gauges. There are 6 data files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Gauge-Based Analyses of Daily Precipitation over Global Land Areas",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1001_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/hydrology_soils/gts_precip_daily_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/hydrology_soils/gts_precip_daily_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/gts_precip_daily_xdeg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/gts_precip_daily_xdeg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1001",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/gts_precip_daily_xdeg/comp/0_gts_precip_daily_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/gts_precip_daily_xdeg/comp/0_gts_precip_daily_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/gts_precip_daily_xdeg/comp/1_gts_precip_daily_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/gts_precip_daily_xdeg/comp/1_gts_precip_daily_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1001_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1001_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1001",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1001",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1001/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1001/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1001_1_fit.png",
+            "identifier": "C2784899029-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1001",
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
+            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II Gauge-Based Analyses of Daily Precipitation over Global Land Areas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-REX-2-LAUNCH-V1.0",
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
-                "calibration",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons                Radio Science Experiment                                               instrument during the                                                    post-launch checkout                                                   mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-rex-2-launch-v1.0_efx8-kzdh",
+            "issued": "2018-09-05",
+            "keyword": [
+                "calibration",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-REX-2-LAUNCH-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-rex-2-launch-v1.0_efx8-kzdh",
-            "description": "This data set contains Raw data taken by the New Horizons                Radio Science Experiment                                               instrument during the                                                    post-launch checkout                                                   mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      REX POST-LAUNCH CHECKOUT                                                \n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      REX POST-LAUNCH CHECKOUT                                                \n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OMAG-3--SCCOORDS-HIRES-V1.0",
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
-                "pioneer venus",
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains vectors collected by the Pioneer Venus Orbiter (previously Pioneer 12) Magnetometer.  The data\nare provided in spacecraft coordinates.  In one format, apoapsis B, the\nmagnetometer can be commanded to return 3 vectors per minor frame. In most\nothers it transmits one vector per minor frame.  In one format, periapsis E,\nit has no words in a minor frame.  At very low sampling rates at which time\nthe sine wave due to spacecraft spin could not be resolved.  The magnetometer\nvalues are despun, and averaged on board using a Walsh transform\n(square wave) in phase and in quadiatune with the sun.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-omag-3--sccoords-hires-v1.0_efzp-guci",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pioneer venus",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OMAG-3--SCCOORDS-HIRES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-omag-3--sccoords-hires-v1.0_efzp-guci",
-            "description": "This dataset contains vectors collected by the Pioneer Venus Orbiter (previously Pioneer 12) Magnetometer.  The data\nare provided in spacecraft coordinates.  In one format, apoapsis B, the\nmagnetometer can be commanded to return 3 vectors per minor frame. In most\nothers it transmits one vector per minor frame.  In one format, periapsis E,\nit has no words in a minor frame.  At very low sampling rates at which time\nthe sine wave due to spacecraft spin could not be resolved.  The magnetometer\nvalues are despun, and averaged on board using a Walsh transform\n(square wave) in phase and in quadiatune with the sun.",
-            "title": "PVO VENUS MAG CALIBRATED S/C COORDINATES\n                                     HIGH RES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PVO VENUS MAG CALIBRATED S/C COORDINATES\n                                     HIGH RES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-RANGE-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-range-ops-v1.0_eg34-ce27",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-RANGE-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-range-ops-v1.0_eg34-ce27",
-            "description": "not applicable",
-            "title": "MER 1 MARS PANORAMIC CAMERA RANGE RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS PANORAMIC CAMERA RANGE RDR OPS V1.0"
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
-                "models",
-                "incompressible",
-                "flow",
-                "cases",
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
-            "identifier": "NASA-845__13",
             "description": "This grouping contains more recent incompressible-flow cases.",
-            "title": "Collaborative Testing of Turbulence Models: More Recent Incompressible Flow Cases",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -704500,171 +704478,195 @@
                     "mediaType": "application/dat"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-845__13",
+            "issued": "2018-06-25",
+            "keyword": [
+                "models",
+                "incompressible",
+                "flow",
+                "cases",
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
+            "title": "Collaborative Testing of Turbulence Models: More Recent Incompressible Flow Cases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/481/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-11-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
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
-            "identifier": "DASHLINK_481",
             "description": "Three grids: coarse, medium, and fine in Plot3d format.",
-            "title": "BSCW Multi-Block Structured Grids",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw-plot3d.tar.gz",
-                    "description": "Coarse/Medium/Fine Multiblock structured grids in Plot3d Format",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse/Medium/Fine Multiblock structured grids in Plot3d Format",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw-plot3d.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw-plot3d.tar.gz"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_481",
+            "issued": "2011-11-01",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/481/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "BSCW Multi-Block Structured Grids"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-3-RDR-STEP-12.8MIN-V1.0",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This far encounter step data set consists of the counting rate and flux data for electrons and ions from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Neptune. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Neptune far encounter, the entire LEPT (Low Energy Particle Telescope) and part of the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystems were turned on for data collection.  Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 12.8 minute rate and flux measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-3-rdr-step-12.8min-v1.0_eg73-8gn6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-3-RDR-STEP-12.8MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-3-rdr-step-12.8min-v1.0_eg73-8gn6",
-            "description": "This far encounter step data set consists of the counting rate and flux data for electrons and ions from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Neptune. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Neptune far encounter, the entire LEPT (Low Energy Particle Telescope) and part of the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystems were turned on for data collection.  Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 12.8 minute rate and flux measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
-            "title": "VG2 LECP 12.8 MINUTE NEPTUNE\n                                      FAR ENCOUNTER STEP DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 LECP 12.8 MINUTE NEPTUNE\n                                      FAR ENCOUNTER STEP DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSRORB_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSRORB_001.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-28",
-            "keyword": [
-                "gravity/gravitational field",
-                "geodetics",
-                "earth science",
-                "tectonics",
-                "solid earth"
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
-            "identifier": "C1427027545-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System Rapid Orbit Product (daily files, generated daily) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce precise orbits identifying the position and velocity of the GNSS satellites. The IGS Analysis Center Coordinator (ACC) uses these individual AC solutions to generate the official IGS rapid combined orbit products. The rapid combination is a daily solution available approximately 17 hours after the end of the previous UTC day.  All orbit solution files utilize the extended standard product-3 (SP3c) format and span 24 hours from 00:00 to 23:45 UTC. The IGS rapid products have a quality nearly comparable to that of the final products. For most applications the user of IGS products will not notice any significant differences between results obtained using the IGS Final and the IGS Rapid products.",
-            "title": "Global Navigation Satellite System (GNSS) Rapid Orbit Product (daily files, generated daily) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSRORB_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSRORB_001",
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
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSRORB_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSRORB_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1427027545-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "gravity/gravitational field",
+                "geodetics",
+                "earth science",
+                "tectonics",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSRORB_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Navigation Satellite System (GNSS) Rapid Orbit Product (daily files, generated daily) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aapollo_seismic_event_catalog&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Apollo Passive Seismic Experiment Expanded Event Catalog.",
+            "identifier": "urn:nasa:pds:apollo_seismic_event_catalog",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "apollo 15",
                 "apollo 14",
@@ -704672,99 +704674,74 @@
                 "apollo 16",
                 "apollo 12"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aapollo_seismic_event_catalog&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:apollo_seismic_event_catalog",
-            "description": "Apollo Passive Seismic Experiment Expanded Event Catalog.",
-            "title": "Apollo Passive Seismic Experiment Expanded Event Catalog Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Apollo Passive Seismic Experiment Expanded Event Catalog Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1213-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-26T05:33:50.000 to 2015-11-26T07:16:05.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1213-v1.0_egbw-t637",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1213-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1213-v1.0_egbw-t637",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-26T05:33:50.000 to 2015-11-26T07:16:05.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1213 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1213 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/sts",
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
-                "spacecraft",
-                "space shuttle",
-                "3d model",
-                "shuttle",
-                "vehicles"
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
-            "identifier": "NASA-402",
             "description": "Polygons: 2476  Vertices: 1353",
-            "title": "NASA 3D Models: Shuttle Model 1",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -704772,501 +704749,537 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-402",
+            "issued": "2018-06-25",
+            "keyword": [
+                "spacecraft",
+                "space shuttle",
+                "3d model",
+                "shuttle",
+                "vehicles"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/sts",
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
+            "title": "NASA 3D Models: Shuttle Model 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/648/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
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
-            "identifier": "DASHLINK_648",
             "description": "The following zip files contain individual flight recorded data in Matlab file format. There are 186 parameters each with a data structure that contains the following:\r\n\r\n<pre>\r\n-sensor recordings\r\n-sampling rate\r\n-units\r\n-parameter description\r\n-parameter ID\r\n</pre>",
-            "title": "Flight Data For Tail 670",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_1.zip",
-                    "description": "Tail 670 Set 1",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 670 Set 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_1.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_1.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_2.zip",
-                    "description": "Tail 670 Set 2",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 670 Set 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_2.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_2.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_3.zip",
-                    "description": "Tail 670 Set 3",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 670 Set 3",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_3.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_3.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_4.zip",
-                    "description": "Tail 670 Set 4",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 670 Set 4",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_4.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_4.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_10.zip",
-                    "description": "Tail_670 Set 10\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_670 Set 10\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_10.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_10.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_5.zip",
-                    "description": "Tail_670 Set 5\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_670 Set 5\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_5.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_5.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_6.zip",
-                    "description": "Tail_670 Set 6\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_670 Set 6\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_6.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_6.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_7.zip",
-                    "description": "Tail_670 Set 7\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_670 Set 7\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_7.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_7.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_8.zip",
-                    "description": "Tail_670 Set 8\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_670 Set 8\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_8.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_8.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_9.zip",
-                    "description": "Tail_670 Set 9\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_670 Set 9\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_670_9.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_670_9.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_648",
+            "issued": "2012-12-04",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/648/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Flight Data For Tail 670"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/G21LGCNLFSC5",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx17 Ground Penetrating Radar V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/G21LGCNLFSC5.",
-            "issued": "2017-02-08",
-            "temporal": "2017-02-08T00:00:00Z/2017-02-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-02-25",
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
-            "identifier": "C1655875737-NSIDC_ECS",
             "description": "This data set contains the results of a ground penetrating radar survey conducted at Grand Mesa, Colorado. Data include the two-way travel time, calculated snow depth, and calculated snow water equivalent. Data were collected between 08 February 2017 and 25 February 2017 as part of the 2017 SnowEx campaign.\n\nThe unprocessed, raw data are also archived at NSIDC (DOI: 10.5067/ZPOLBRHVWG5V).",
-            "title": "SnowEx17 Ground Penetrating Radar V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FG21LGCNLFSC5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FG21LGCNLFSC5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_GPR.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_GPR.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1655875737-NSIDC_ECS&q=SNEX17_GPR&m=29.76382409255042%21-108.823974609375%214%211%210%210%2C2&tl=1558474061%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1655875737-NSIDC_ECS&q=SNEX17_GPR&m=29.76382409255042%21-108.823974609375%214%211%210%210%2C2&tl=1558474061%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_GPR/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_GPR/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/G21LGCNLFSC5",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/G21LGCNLFSC5",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/G21LGCNLFSC5",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/G21LGCNLFSC5",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1655875737-NSIDC_ECS",
+            "issued": "2017-02-08",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/G21LGCNLFSC5",
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
             "spatial": "-108.22367 38.9935 -107.85785 39.11115",
+            "temporal": "2017-02-08T00:00:00Z/2017-02-25T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx17 Ground Penetrating Radar V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206894-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Monthly Summaries of Soil Temperature and Soil Moisture in China, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1998-06-01",
-            "temporal": "1998-06-01T00:00:00Z/2002-05-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-05-31",
-            "keyword": [
-                "earth science",
-                "soils",
-                "precipitation",
-                "atmospheric water vapor",
-                "land surface",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "frozen ground",
-                "cryosphere",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Zhao Lin",
                 "hasEmail": "mailto:linzhao@ns.lzb.ac.cn"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206894-NSIDCV0",
             "description": "This data set contains soil temperature and soil moisture data from nine sites in China. Temporal coverage varies by station; the earliest record is from June 1998, and the latest is from May 2002. Data from individual stations are available in tab-delimited ASCII text files. An Excel spreadsheet contains the same data compiled together in a single file. NSIDC currently provides these summary data via ftp; the full soil temperature and moisture data set is available from Ron Paetzold, USDA.",
-            "title": "Monthly Summaries of Soil Temperature and Soil Moisture in China, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD625_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD625_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD625/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD625/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD625/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD625/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206894-NSIDCV0",
+            "issued": "1998-06-01",
+            "keyword": [
+                "earth science",
+                "soils",
+                "precipitation",
+                "atmospheric water vapor",
+                "land surface",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "frozen ground",
+                "cryosphere",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206894-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "86.8861 31.8361 94.175 43.3194",
+            "temporal": "1998-06-01T00:00:00Z/2002-05-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Summaries of Soil Temperature and Soil Moisture in China, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0679-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-28T21:43:20.000 to 2015-03-28T22:55:12.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0679-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0679-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0679-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-28T21:43:20.000 to 2015-03-28T22:55:12.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0679 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0679 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0559-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-02T07:42:05.000 to 2015-02-02T10:54:12.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0559-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0559-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0559-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-02T07:42:05.000 to 2015-02-02T10:54:12.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0559 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0559 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/939/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2016-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kai Goebel",
                 "hasEmail": "mailto:kai.goebel@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_939",
             "description": "Failure prognosis - as a natural extension to the fault detection and isolation (FDI) problem - has become a key issue in a world where the economic impact of system reliability and cost-effective operation of critical assets is steadily increasing. Failure prognostic algorithms aim to characterize the evolution of incipient fault conditions in complex dynamic processes, thus allowing to estimate of the remaining useful life (RUL) of subsystems and components. Several examples can be used here to illustrate the range of possible applications for these algorithms: electro-mechanical systems, continuous-time manufacturing processes, structural damage analysis, and even fault tolerant\r\nsoftware architectures. Most of them have in common the fact that they are highly complex, nonlinear, and affected by large-grain uncertainty.\r\n\r\nWe introduce in this chapter an integrated failure prognosis architecture that is applicable to a variety of aircraft systems and industrial processes. We are targeting a specific rotorcraft system as a prototypical testbed for proof-of-concept. The overall architecture consists of an on-board and an off-board module for eventual on-platformimplementation purposes.",
-            "title": "A Combined Model-Based and Data-Driven Prognostic Approach for Aircraft System Life Management",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Chapter_OVG_V5.1_2.pdf",
-                    "description": "chapter",
                     "@type": "dcat:Distribution",
+                    "description": "chapter",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Chapter_OVG_V5.1_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Chapter_OVG V5.1.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_939",
+            "issued": "2016-01-14",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/939/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Combined Model-Based and Data-Driven Prognostic Approach for Aircraft System Life Management"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-MAG-4-SUMM-HGCOORDS-48.0SEC-V1.0",
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
+            "description": "This data set includes calibrated magnetic field data acquired by the Voyager 1 Low Field Magnetometer (LFM) during the Saturn encounter. Coverage begins in the solar wind inbound to Saturn and continues past the last outbound bowshock crossing. The data are in Heliographic (RTN) coordinates and have been averaged from the 9.6 second summary rate to a 48 second sample rate. All magnetic field measurements are given in nanoTesla (nT). The magnetic field data are calibrated (see the calibration description included in the Voyager 1 Magnetometer instrument catalog file for details).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-mag-4-summ-hgcoords-48.0sec-v1.0_eggb-nnpg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-MAG-4-SUMM-HGCOORDS-48.0SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-mag-4-summ-hgcoords-48.0sec-v1.0_eggb-nnpg",
-            "description": "This data set includes calibrated magnetic field data acquired by the Voyager 1 Low Field Magnetometer (LFM) during the Saturn encounter. Coverage begins in the solar wind inbound to Saturn and continues past the last outbound bowshock crossing. The data are in Heliographic (RTN) coordinates and have been averaged from the 9.6 second summary rate to a 48 second sample rate. All magnetic field measurements are given in nanoTesla (nT). The magnetic field data are calibrated (see the calibration description included in the Voyager 1 Magnetometer instrument catalog file for details).",
-            "title": "VG1 SAT MAG RESAMPLED HELIOGRAPHIC (RTN)\n                                      COORDS 48.0SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 SAT MAG RESAMPLED HELIOGRAPHIC (RTN)\n                                      COORDS 48.0SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-3-CR2-CALIB2-V1.0",
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
-                "solar wind"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the CRUISE 2\nmission phase where the primary target was the SOLAR WIND. It contains\ninstrument outputs in volts and amperes, calibrated and corrected for\ninstrument offsets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-3-cr2-calib2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-3-CR2-CALIB2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-3-cr2-calib2-v1.0",
-            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the CRUISE 2\nmission phase where the primary target was the SOLAR WIND. It contains\ninstrument outputs in volts and amperes, calibrated and corrected for\ninstrument offsets.",
-            "title": "ROSETTA-ORBITER SW RPCLAP 3\nCR2 CALIB2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SW RPCLAP 3\nCR2 CALIB2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-2-EAR2-MAG-V1.0",
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
+            "description": "This archive contains level 2 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired  during the EAR2 (Earth fly-by 2) phase It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-2-ear2-mag-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-2-EAR2-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-2-ear2-mag-v1.0",
-            "description": "This archive contains level 2 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired  during the EAR2 (Earth fly-by 2) phase It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER EARTH ROMAP 2 EAR2 MAG\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER EARTH ROMAP 2 EAR2 MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/egmv-36wq",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NA",
+                "hasEmail": "mailto:nasa-data@lists.arc.nasa.gov"
+            },
+            "description": "This data set contains a total of 73,031 landmarks. 10,433 landmarks were detected and extracted from 180 HiRISE browse images, and 62,598 landmarks were augmented from 10,433 original landmarks. For each original landmark, we cropped a square bounding box that includes the full extent of the landmark plus a 30-pixel margin to left, right, top and bottom. Each cropped landmark was resized to 227x227 pixels, and then was augmented to generate 6 additional landmarks using the following methods:\n\n1. 90 degrees clockwise rotation\n2. 180 degrees clockwise rotation\n3. 270 degrees clockwise rotation\n4. Horizontal flip\n5. Vertical flip\n6. Random brightness adjustment",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This data set contains a total of 73,031 landmarks. 10,433 landmarks were detected and extracted from 180 HiRISE browse images, and 62,598 landmarks were augmented from 10,433 original landmarks. For each original landmark, we cropped a square bounding box that includes the full extent of the landmark plus a 30-pixel margin to left, right, top and bottom. Each cropped landmark was resized to 227x227 pixels, and then was augmented to generate 6 additional landmarks using the following methods:\n\n1. 90 degrees clockwise rotation\n2. 180 degrees clockwise rotation\n3. 270 degrees clockwise rotation\n4. Horizontal flip\n5. Vertical flip\n6. Random brightness adjustment",
+                    "downloadURL": "https://zenodo.org/record/2538136",
+                    "mediaType": "text/html",
+                    "title": "Mars orbital image (HiRISE) labeled data set version 3"
+                }
+            ],
+            "identifier": "https://data.nasa.gov/api/views/egmv-36wq",
             "issued": "2020-01-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
             "keyword": [
                 "usg-ai-training-data",
                 "planetary science",
@@ -705275,214 +705288,203 @@
                 "hirise",
                 "usg-artificial-intelligence"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NA",
-                "hasEmail": "mailto:nasa-data@lists.arc.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/egmv-36wq",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA JPL"
             },
-            "identifier": "https://data.nasa.gov/api/views/egmv-36wq",
-            "description": "This data set contains a total of 73,031 landmarks. 10,433 landmarks were detected and extracted from 180 HiRISE browse images, and 62,598 landmarks were augmented from 10,433 original landmarks. For each original landmark, we cropped a square bounding box that includes the full extent of the landmark plus a 30-pixel margin to left, right, top and bottom. Each cropped landmark was resized to 227x227 pixels, and then was augmented to generate 6 additional landmarks using the following methods:\n\n1. 90 degrees clockwise rotation\n2. 180 degrees clockwise rotation\n3. 270 degrees clockwise rotation\n4. Horizontal flip\n5. Vertical flip\n6. Random brightness adjustment",
-            "title": "Mars orbital image (HiRISE) labeled data set version 3",
-            "programCode": [
-                "026:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://zenodo.org/record/2538136",
-                    "description": "This data set contains a total of 73,031 landmarks. 10,433 landmarks were detected and extracted from 180 HiRISE browse images, and 62,598 landmarks were augmented from 10,433 original landmarks. For each original landmark, we cropped a square bounding box that includes the full extent of the landmark plus a 30-pixel margin to left, right, top and bottom. Each cropped landmark was resized to 227x227 pixels, and then was augmented to generate 6 additional landmarks using the following methods:\n\n1. 90 degrees clockwise rotation\n2. 180 degrees clockwise rotation\n3. 270 degrees clockwise rotation\n4. Horizontal flip\n5. Vertical flip\n6. Random brightness adjustment",
-                    "@type": "dcat:Distribution",
-                    "title": "Mars orbital image (HiRISE) labeled data set version 3"
-                }
-            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Mars orbital image (HiRISE) labeled data set version 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TJLY2U5L0D4G",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Soil Climate Analysis Network (SCAN): Georgia, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/TJLY2U5L0D4G.",
-            "issued": "2003-06-01",
-            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-31",
-            "keyword": [
-                "atmospheric winds",
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "precipitation",
-                "agriculture",
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
-            "identifier": "C1386204210-NSIDCV0",
             "description": "This data set contains measurements taken during the Soil Moisture Experiment 2003 (SMEX03) from 1 June 2003 to 31 July 2003 from sensors at the Soil Climate Analysis Network (SCAN) station located in Little River, GA, USA.",
-            "title": "SMEX03 Soil Climate Analysis Network (SCAN): Georgia, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTJLY2U5L0D4G",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTJLY2U5L0D4G",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ground_soil_moisture/SCAN/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ground_soil_moisture/SCAN/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ground_soil_moisture/SCAN/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ground_soil_moisture/SCAN/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TJLY2U5L0D4G",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/TJLY2U5L0D4G",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TJLY2U5L0D4G",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/TJLY2U5L0D4G",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204210-NSIDCV0",
+            "issued": "2003-06-01",
+            "keyword": [
+                "atmospheric winds",
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "precipitation",
+                "agriculture",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/TJLY2U5L0D4G",
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
             "spatial": "-83.56 31.51 -83.56 31.51",
+            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Soil Climate Analysis Network (SCAN): Georgia, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_CSLC-S1-STATIC_V1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OPERA. 2023-12-05. OPERA Coregistered Single-Look Complex from Sentinel-1 Static Layers validated product (Version 1). Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Alaska Satellite Facility Distributed Active Archive Center. https://doi.org/10.5067/SNWG/OPERA_L2_CSLC-S1-STATIC_V1.",
-            "issued": "2014-04-03",
-            "temporal": "2014-04-03T00:00:00Z/2023-12-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-04-03",
-            "keyword": [
-                "glaciers/ice sheets",
-                "land surface",
-                "oceans",
-                "tectonics",
-                "solid earth",
-                "coastal processes",
-                "earth science",
-                "cryosphere",
-                "geomorphic landforms/processes"
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
-            "identifier": "C2795135668-ASF",
-            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Coregistered Single-Look Complex (CSLC) from Sentinel-1 (S1) Static Layers (CSLC-S1-STATIC) validated product contains static radar geometry layers associated with the OPERA Coregistered Single-Look Complex (CSLC) from Sentinel-1 (S1) validated product. Due to the S1 mission\u2019s narrow orbital tube, radar-geometry layers vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA CSLC-S1 product, as they are produced only once or a limited number of times, to account for changes in the DEM, in the S1 orbit, or in the static layers generation algorithm. Each OPERA CSLC-S1-STATIC product is distributed as a Hierarchical Data Format version 5 (HDF5) file following the CF-1.8 convention containing both data raster layers and product metadata and corresponds to matching CSLC-S1 products with the same burst ID. OPERA CSLC-S1 products are available over North America which includes the USA and U.S. Territories, Canada within 200 km of the U.S. border, and all mainland countries from the southern U.S. border down to and including Panama. The CSLC-S1 products are available in the associated OPERA Coregistered Single-Look Complex from Sentinel-1 validated product (Version 1) dataset.",
-            "graphic-preview-description": "Image to represent the collection",
             "creator": "OPERA",
-            "title": "OPERA Coregistered Single-Look Complex from Sentinel-1 Static Layers validated product (Version 1)",
-            "graphic-preview-file": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_CSLC-S1_T027-056657-IW3_20231008T132530Z_20231009T204501Z_S1A_VV_v1.0_BROWSE.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Coregistered Single-Look Complex (CSLC) from Sentinel-1 (S1) Static Layers (CSLC-S1-STATIC) validated product contains static radar geometry layers associated with the OPERA Coregistered Single-Look Complex (CSLC) from Sentinel-1 (S1) validated product. Due to the S1 mission\u2019s narrow orbital tube, radar-geometry layers vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA CSLC-S1 product, as they are produced only once or a limited number of times, to account for changes in the DEM, in the S1 orbit, or in the static layers generation algorithm. Each OPERA CSLC-S1-STATIC product is distributed as a Hierarchical Data Format version 5 (HDF5) file following the CF-1.8 convention containing both data raster layers and product metadata and corresponds to matching CSLC-S1 products with the same burst ID. OPERA CSLC-S1 products are available over North America which includes the USA and U.S. Territories, Canada within 200 km of the U.S. border, and all mainland countries from the southern U.S. border down to and including Panama. The CSLC-S1 products are available in the associated OPERA Coregistered Single-Look Complex from Sentinel-1 validated product (Version 1) dataset.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSNWG%2FOPERA_L2_CSLC-S1-STATIC_V1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSNWG%2FOPERA_L2_CSLC-S1-STATIC_V1",
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
-                    "downloadURL": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_CSLC-S1_T027-056657-IW3_20231008T132530Z_20231009T204501Z_S1A_VV_v1.0_BROWSE.png",
-                    "description": "Image to represent the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Image to represent the collection",
+                    "downloadURL": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_CSLC-S1_T027-056657-IW3_20231008T132530Z_20231009T204501Z_S1A_VV_v1.0_BROWSE.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Image to represent the collection",
+            "graphic-preview-file": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_CSLC-S1_T027-056657-IW3_20231008T132530Z_20231009T204501Z_S1A_VV_v1.0_BROWSE.png",
+            "identifier": "C2795135668-ASF",
+            "issued": "2014-04-03",
+            "keyword": [
+                "glaciers/ice sheets",
+                "land surface",
+                "oceans",
+                "tectonics",
+                "solid earth",
+                "coastal processes",
+                "earth science",
+                "cryosphere",
+                "geomorphic landforms/processes"
+            ],
+            "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_CSLC-S1-STATIC_V1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-04-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>62.5015467 -139.0996574 69.6867168 -139.3803251 71.2183663 -157.141417 68.3735763 -167.228812 65.4323808 -168.8440651 60.338896 -173.9306256 52.6155773 -180.0 50.8611463 -180.0 51.6129878 -170.6297483 56.0163229 -152.9114355 59.267895 -149.1913018 58.8520427 -140.3770183 56.9878841 -136.2583689 51.3393627 -131.6506428 48.4661107 -125.7549673 40.3311808 -124.4241493 34.7676709 -121.9778478 22.4311968 -110.234396 14.4339613 -97.1649601 13.1145391 -90.922636 8.0382063 -84.6585484 6.4264529 -82.198433 4.9744342 -79.0975897 6.6985362 -76.3425468 15.9928118 -83.7301124 21.8738063 -87.1827257 19.4394223 -93.6858487 26.8405583 -96.431852 28.7047067 -92.0810441 28.6812513 -88.09344 28.4115341 -85.094922 28.8151876 -83.4597433 23.5415141 -81.7506224 25.1215118 -78.2162044 29.3000106 -79.6727284 31.2954845 -79.6466319 34.8887882 -75.0796609 40.946987 -69.3403609 43.3742252 -64.4225561 48.2959502 -65.1335857 48.9438707 -71.4417716 45.7238643 -79.6545994 50.6822691 -88.2638649 50.3596533 -90.7298952 51.3673723 -95.3439882 51.22781 -104.3228708 51.0180252 -121.4385551 61.4158182 -134.3936582 62.5015467 -139.0996574</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2014-04-03T00:00:00Z/2023-12-11T00:00:00Z",
             "theme": [
                 "SNWG/OPERA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OPERA Coregistered Single-Look Complex from Sentinel-1 Static Layers validated product (Version 1)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-VIS-2-RAW-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Raw, uncalibrated image data from the Visible Camera (VIS) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-vis-2-raw-v1.0_egnx-zci7",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "moon",
@@ -705490,193 +705492,170 @@
                 "calibration",
                 "lunar crater observation and sensing satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-VIS-2-RAW-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-vis-2-raw-v1.0_egnx-zci7",
-            "description": "Raw, uncalibrated image data from the Visible Camera (VIS) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS EARTH/MOON VISIBLE CAMERA 2 RAW DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LCROSS EARTH/MOON VISIBLE CAMERA 2 RAW DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/MULTIPLE/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Huffman, George J, Erich  Stocker, David T Bolvin and Eric J Nelkin.2017. GPM Ground Validation TRMM Multi-satellite Precipitation Analysis (TMPA) IPHEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IPHEX/MULTIPLE/DATA301",
-            "issued": "2017-01-13",
-            "temporal": "2014-05-01T00:00:00Z/2014-06-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "precipitation",
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
-            "identifier": "C1979825245-GHRC_DAAC",
             "description": "This GPM Ground Validation TRMM Multi-satellite Precipitation Analysis (TMPA) IPHEx dataset is a subset of the TMPA 3B42RT gridded precipitation product selected for the time period of the GPM Ground Validation Integrated Precipitation and Hydrology Experiment (IPHEx) held in North Carolina during May 1, 2014 to June 15, 2014. The goal of IPHEx was to characterize warm season orographic precipitation regimes and the relationship between precipitation regimes and hydrologic processes in regions of complex terrain. This dataset contains 3-hourly, 0.25 degree maps of precipitation derived using microwave (MW), infra-red (IR),  surface precipitation gauge measurements, and other rain products that include the TRMM Precipitation Radar (PR) data.  The IPHEx TMPA product is available in netCDF-4 and binary formats.",
-            "title": "GPM Ground Validation TRMM Multi-satellite Precipitation Analysis (TMPA) IPHEx V7",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FMULTIPLE%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FMULTIPLE%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmtmpaiphx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmtmpaiphx",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/TMPA/doc/gpmtmpaiphx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/TMPA/doc/gpmtmpaiphx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/JHM560.1",
-                    "description": "The TRMM Multisatellite Precipitation Analysis (TMPA): Quasi-Global, Multiyear, Combined-Sensor Precipitation Estimates at Fine Scales",
                     "@type": "dcat:Distribution",
+                    "description": "The TRMM Multisatellite Precipitation Analysis (TMPA): Quasi-Global, Multiyear, Combined-Sensor Precipitation Estimates at Fine Scales",
+                    "downloadURL": "http://dx.doi.org/10.1175/JHM560.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/JHM560.1",
-                    "description": "The TRMM Multisatellite Precipitation Analysis (TMPA): Quasi-Global, Multiyear, Combined-Sensor Precipitation Estimates at Fine Scales",
                     "@type": "dcat:Distribution",
+                    "description": "The TRMM Multisatellite Precipitation Analysis (TMPA): Quasi-Global, Multiyear, Combined-Sensor Precipitation Estimates at Fine Scales",
+                    "downloadURL": "http://dx.doi.org/10.1175/JHM560.1",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
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
+            "identifier": "C1979825245-GHRC_DAAC",
+            "issued": "2017-01-13",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/MULTIPLE/DATA301",
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
             "spatial": "-180.0 -60.0 180.0 60.0",
+            "temporal": "2014-05-01T00:00:00Z/2014-06-16T23:59:59Z",
             "theme": [
                 "IPHEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation TRMM Multi-satellite Precipitation Analysis (TMPA) IPHEx V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-LSPN-N-NDR-HALLEY-V1.0",
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
-                "international halley watch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Large-Scale Phenomena Network has been organized into a set of digitized images and those left in the original analog state for reasons of quality, time coverage, or submission problems. These latter 1771 pieces of data are held in an archive both at Goddard Space Flight Center and with the Small Bodies Node of the Planetary Data System. (In the latter case, contact specifically the Comet Sub-Node of the PDS at the Laboratory for Atmospheric and Space Physics associated with the University of Colorado Boulder, for more assistance). Some of these analog images are presented in 'The International Halley Watch Atlas of Large-Scale Phenomena' (Brandt, John C., Niedner, Malcolm B. Jr., Rahe, Jurgen, 1992). The data cover a time range from 1984 December 22 through 1987 April 26 through 23 of the IHW Chronological Data Archive Collection",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-lspn-n-ndr-halley-v1.0_egqe-r7ee",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-LSPN-N-NDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-lspn-n-ndr-halley-v1.0_egqe-r7ee",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Large-Scale Phenomena Network has been organized into a set of digitized images and those left in the original analog state for reasons of quality, time coverage, or submission problems. These latter 1771 pieces of data are held in an archive both at Goddard Space Flight Center and with the Small Bodies Node of the Planetary Data System. (In the latter case, contact specifically the Comet Sub-Node of the PDS at the Laboratory for Atmospheric and Space Physics associated with the University of Colorado Boulder, for more assistance). Some of these analog images are presented in 'The International Halley Watch Atlas of Large-Scale Phenomena' (Brandt, John C., Niedner, Malcolm B. Jr., Rahe, Jurgen, 1992). The data cover a time range from 1984 December 22 through 1987 April 26 through 23 of the IHW Chronological Data Archive Collection",
-            "title": "IHW COMET HALLEY LSPN NON-DIGITIZED IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY LSPN NON-DIGITIZED IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/ares1simple-c",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/constellation/main/index.html"
-            ],
-            "keyword": [
-                "ares 1",
-                "vehicles",
-                "3d model",
-                "spacecraft"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brian Kumanchik",
                 "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-314",
             "description": "Polygons: 3872 Vertices: 2117",
-            "title": "NASA 3D Models: Ares 1",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -705684,955 +705663,978 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-314",
+            "issued": "2018-06-25",
+            "keyword": [
+                "ares 1",
+                "vehicles",
+                "3d model",
+                "spacecraft"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/ares1simple-c",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/constellation/main/index.html"
+            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: Ares 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-VIR-3-RDR-IR-CRUISE-SPECTRA-V1.0",
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
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the spectral      radiance (W/(m**2*sr*micron)) data from the Dawn VIR instrument         IR channel for all cruise mission phases. The data are from the         cruise phase from launch to Vesta (Sep 2009-May 2011), and Vesta        to Ceres (Sep 2012-Dec 2014).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-vir-3-rdr-ir-cruise-spectra-v1.0_egtm-xfu8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-VIR-3-RDR-IR-CRUISE-SPECTRA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-vir-3-rdr-ir-cruise-spectra-v1.0_egtm-xfu8",
-            "description": "This data set contains the spectral      radiance (W/(m**2*sr*micron)) data from the Dawn VIR instrument         IR channel for all cruise mission phases. The data are from the         cruise phase from launch to Vesta (Sep 2009-May 2011), and Vesta        to Ceres (Sep 2012-Dec 2014).",
-            "title": "DAWN VIR CAL (RDR) CRUISE CHECKOUT/CALIB IR SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN VIR CAL (RDR) CRUISE CHECKOUT/CALIB IR SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/9NCR9DDDOPFI",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2T3NPTDT. Version 5.12.4. MERRA-2 tavg3_3d_tdt_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Temperature Tendencies V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/9NCR9DDDOPFI. https://disc.gsfc.nasa.gov/datacollection/M2T3NPTDT_5.12.4.html. Digital Science Data.",
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
-                "atmosphere",
-                "atmospheric temperature",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812940-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2T3NPTDT (or  tavg3_3d_tdt_Np) is a 3-dimensional 3-hourly time averaged data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of air temperature tendencies on 42 pressure levels, such as total temperature analysis tendency, and tendency of air temperature due to  dynamics (or friction, moisture, radiation, and physics). The data field is available every three hour starting from 01:30 UTC, e.g.: 01:30, 04:30, \u2026 , 22:30 UTC. The information on the pressure levels can be found in the section 4.2 of the MERRA-2 File Specification document. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2T3NPTDT",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 tavg3_3d_tdt_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Temperature Tendencies 0.625 x 0.5 degree V5.12.4 (M2T3NPTDT) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#variableFacets=dataProductPlatformInstrument%3AMERRA-2%20Model%3B",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9NCR9DDDOPFI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9NCR9DDDOPFI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NPTDT_5.12.4.png",
-                    "description": "M2T3NPTDT variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2T3NPTDT variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NPTDT_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T3NPTDT_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T3NPTDT_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NPTDT.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NPTDT.5.12.4/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T3NPTDT",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T3NPTDT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2T3NPTDT.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2T3NPTDT.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T3NPTDT.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T3NPTDT.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T3NPTDT.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T3NPTDT.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NPTDT.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NPTDT.5.12.4/doc/MERRA2.README.pdf",
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
+            "identifier": "C1276812940-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/9NCR9DDDOPFI",
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
+            "series-name": "M2T3NPTDT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavg3_3d_tdt_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Temperature Tendencies 0.625 x 0.5 degree V5.12.4 (M2T3NPTDT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-4-SCRDR-V1.0",
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
+            "description": "Calibrated or converted engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-4-scrdr-v1.0_egw9-mife",
+            "issued": "2021-05-21",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-4-SCRDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-4-scrdr-v1.0_egw9-mife",
-            "description": "Calibrated or converted engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
-            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 4 SCRDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 4 SCRDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SMP53-3SPCS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Remote Sensing Systems (RSS). 2024-05-31. RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean Validated Dataset. Version 5.3. SMAP Sea Surface Salinity Products. Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Remote Sensing Systems (RSS). https://doi.org/10.5067/SMP53-3SPCS. http://podaac.jpl.nasa.gov/smap. Remote Sensing Systems (RSS), Remote Sensing Systems (RSS), 2022-02-25, RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.0 Validated Dataset, http://podaac.jpl.nasa.gov/smap.",
-            "issued": "2021-01-13",
-            "temporal": "2015-03-27T12:00:00Z/2024-01-05T00:00:00Z",
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
-            "identifier": "C2951822554-POCLOUD",
-            "description": "The RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.3 Validated Dataset produced by the Remote Sensing Systems (RSS) and sponsored by the NASA Ocean Salinity Science Team, is a validated product that provides orbital/swath data on sea surface salinity (SSS) derived from the NASA's Soil Moisture Active Passive (SMAP) mission. The SMAP satellite was launched on 31 January 2015\r\nwith a near-polar orbit at an inclination of 98 degrees and an altitude of 685 km. It has an ascending node time of 6 pm and is sun-synchronous. With its 1000km swath, SMAP achieves global coverage in approximately 3 days, but has an exact orbit repeat cycle of 8 days. Malfunction of the SMAP scatterometer on 7 July, 2015, has necessitated the use of collocated wind speed, primarily from WindSat, for the surface roughness correction required for the surface salinity retrieval.\r\n<br><br>\r\nThe evaluation Version 5.3 is identical to the Version 6.0 validated release with the exception that Version 5.3 uses the Version 5 L1B TA as input. The V6 L1B TA uses a lower\r\nTA threshold for RFI exclusion. Until the full back-processing of V6.0 is complete, the evaluation Version 5.3 can and should be used instead. Version 5.3 has been processed from the beginning of the SMAP mission to the end of 2023, and each data file is available in netCDF-4 file format.\r\nObservations are global in extent with an approximate spatial resolution of 40KM. Note that while a SSS 40KM variable is also included in the product for most open ocean applications, The standard product of the SMAP Version 5.3 release is the smoothed salinity product with a spatial resolution of approximately 70 km.",
-            "release-place": "Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA",
-            "series-name": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean Validated Dataset",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Remote Sensing Systems (RSS)",
-            "title": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.3 Validated Dataset",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.3 Validated Dataset produced by the Remote Sensing Systems (RSS) and sponsored by the NASA Ocean Salinity Science Team, is a validated product that provides orbital/swath data on sea surface salinity (SSS) derived from the NASA's Soil Moisture Active Passive (SMAP) mission. The SMAP satellite was launched on 31 January 2015\r\nwith a near-polar orbit at an inclination of 98 degrees and an altitude of 685 km. It has an ascending node time of 6 pm and is sun-synchronous. With its 1000km swath, SMAP achieves global coverage in approximately 3 days, but has an exact orbit repeat cycle of 8 days. Malfunction of the SMAP scatterometer on 7 July, 2015, has necessitated the use of collocated wind speed, primarily from WindSat, for the surface roughness correction required for the surface salinity retrieval.\r\n<br><br>\r\nThe evaluation Version 5.3 is identical to the Version 6.0 validated release with the exception that Version 5.3 uses the Version 5 L1B TA as input. The V6 L1B TA uses a lower\r\nTA threshold for RFI exclusion. Until the full back-processing of V6.0 is complete, the evaluation Version 5.3 can and should be used instead. Version 5.3 has been processed from the beginning of the SMAP mission to the end of 2023, and each data file is available in netCDF-4 file format.\r\nObservations are global in extent with an approximate spatial resolution of 40KM. Note that while a SSS 40KM variable is also included in the product for most open ocean applications, The standard product of the SMAP Version 5.3 release is the smoothed salinity product with a spatial resolution of approximately 70 km.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP53-3SPCS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP53-3SPCS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/ATBD_EOM_final.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/ATBD_EOM_final.pdf",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf",
-                    "description": "SMAP-SSS V6.0 Technical Guide (ATBD, Validation Analysis, Product Format Specification)",
                     "@type": "dcat:Distribution",
+                    "description": "SMAP-SSS V6.0 Technical Guide (ATBD, Validation Analysis, Product Format Specification)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2951822554-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2951822554-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2951822554-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2951822554-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6.jpg",
+            "identifier": "C2951822554-POCLOUD",
+            "issued": "2021-01-13",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMP53-3SPCS",
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
+            "temporal": "2015-03-27T12:00:00Z/2024-01-05T00:00:00Z",
             "theme": [
                 "SMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.3 Validated Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-2-EDR-CRUISE4-V1.0",
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
+            "description": "This data set contains the NEAR magnetometer (MAG) data for the CRUISE4 phase. The data set begins on 1998-12-24T00:00:00.000 and ends 2000-01-10T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw magnetometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-2-edr-cruise4-v1.0_egzp-j273",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-2-EDR-CRUISE4-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-2-edr-cruise4-v1.0_egzp-j273",
-            "description": "This data set contains the NEAR magnetometer (MAG) data for the CRUISE4 phase. The data set begins on 1998-12-24T00:00:00.000 and ends 2000-01-10T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw magnetometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
-            "title": "NEAR MAG DATA FOR CRUISE4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR MAG DATA FOR CRUISE4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FSW%2FJ%2FS-MAG-4-SUMM-1SECAVG-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains calibrated 1 second averaged Cassini magnetometer data, for the entire Cassini mission. These data are provided in Kronographic (KRTP, KSO, KSM) coordinates at Saturn, Geographic coordinates (GSE, GSM) for the Earth flyby, Jovigraphic coordinates for the Jupiter flyby, and RTN coordinates for the entire mission. These data were calibrated and converted to physical coordinates from the Cassini MAG Raw Data Set (CO-E/SW/J/S-MAG-2-REDR-RAW-DATA-V1.0), by the Cassini MAG team at Imperial College. The data averaged to 1 second at the PDS-PPI node at UCLA.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-sw-j-s-mag-4-summ-1secavg-v1.0_eh2m-5sak",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "saturn",
                 "cassini-huygens",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FSW%2FJ%2FS-MAG-4-SUMM-1SECAVG-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-sw-j-s-mag-4-summ-1secavg-v1.0_eh2m-5sak",
-            "description": "This data set contains calibrated 1 second averaged Cassini magnetometer data, for the entire Cassini mission. These data are provided in Kronographic (KRTP, KSO, KSM) coordinates at Saturn, Geographic coordinates (GSE, GSM) for the Earth flyby, Jovigraphic coordinates for the Jupiter flyby, and RTN coordinates for the entire mission. These data were calibrated and converted to physical coordinates from the Cassini MAG Raw Data Set (CO-E/SW/J/S-MAG-2-REDR-RAW-DATA-V1.0), by the Cassini MAG team at Imperial College. The data averaged to 1 second at the PDS-PPI node at UCLA.",
-            "title": "CASSINI ORBITER MAG CALIBRATED SUMMARY 1 SEC AVERAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER MAG CALIBRATED SUMMARY 1 SEC AVERAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-2LSNR",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2021-06-22. Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NRT Ocean Surface Topography   . Version F. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-2LSNR.",
-            "issued": "2020-12-07",
-            "temporal": "2020-11-30T00:00:00Z/2023-05-29T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-26",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "sea surface topography",
-                "ocean waves",
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
-            "identifier": "C1968979597-POCLOUD",
-            "description": "Provides low resolution (LR) near real time (NRT; 3-hour latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed, along with 1 Hz and 20 Hz measurements from the radar altimeter, orbit altitude, environmental range corrections, instrument corrections, and geophysical models. The NRT product is analogous to the Jason-3 OGDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NRT Ocean Surface Topography",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_LR_STD_OST_NRT_F.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides low resolution (LR) near real time (NRT; 3-hour latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed, along with 1 Hz and 20 Hz measurements from the radar altimeter, orbit altitude, environmental range corrections, instrument corrections, and geophysical models. The NRT product is analogous to the Jason-3 OGDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LSNR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LSNR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "description": "The mission page for Sentinel-6A MF on the European Organisation for the Exploitation of Meteorological Satellites (EUMETSAT) website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the European Organisation for the Exploitation of Meteorological Satellites (EUMETSAT) website.",
+                    "downloadURL": "https://www.eumetsat.int/sentinel-6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_STD_OST_NRT_F",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_STD_OST_NRT_F",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_LR_STD_OST_NRT_F.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_LR_STD_OST_NRT_F.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968979597-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968979597-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968979597-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968979597-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_LR_STD_OST_NRT_F.jpg",
+            "identifier": "C1968979597-POCLOUD",
+            "issued": "2020-12-07",
+            "keyword": [
+                "sea surface topography",
+                "ocean waves",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-2LSNR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-05-26",
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
+            "temporal": "2020-11-30T00:00:00Z/2023-05-29T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NRT Ocean Surface Topography"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/eh5s-w47p",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "nucleic acid extraction",
-                "weightlessness",
-                "sample collection",
-                "library construction",
-                "nucleic acid sequencing"
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
-            "identifier": "nasa_genelab_GLDS-164_eh5s-w47p",
             "description": "Spaceflight has been shown to suppress the adaptive immune response altering the distribution and function of lymphocyte populations. B lymphocytes express highly specific and highly diversified receptors known as immunoglobulins (Ig) that directly bind and neutralize pathogens. Ig diversity is achieved through the enzymatic splicing of gene segments within the genomic DNA of each B cell in a host. The collection of Ig specificities within a host or Ig repertoire has been increasingly characterized in both basic research and clinical settings using high-throughput sequencing technology (HTS). We utilized HTS to test the hypothesis that spaceflight affects the B-cell repertoire. To test this hypothesis we characterized the impact of spaceflight on the unimmunized Ig repertoire of C57BL/6 mice that were flown aboard the International Space Station (ISS) during the Rodent Research One validation flight in comparison to ground controls. Individual gene segment usage was similar between ground control and flight animals however gene segment combinations and the junctions in which gene segments combine was varied among animals within and between treatment groups. We also found that spontaneous somatic mutations in the IgH and Ig xce xba gene loci were not increased. These data suggest that space flight did not affect the B cell repertoire of mice flown and housed on the ISS over a short period of time.",
-            "title": "Effects of spaceflight on the immunoglobulin repertoire of unimmunized C57BL/6 mice",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-164",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-164",
+                    "mediaType": "text/html",
                     "title": "Effects of spaceflight on the immunoglobulin repertoire of unimmunized C57BL/6 mice"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "nasa_genelab_GLDS-164_eh5s-w47p",
+            "issued": "2018-06-26",
+            "keyword": [
+                "nucleic acid extraction",
+                "weightlessness",
+                "sample collection",
+                "library construction",
+                "nucleic acid sequencing"
+            ],
+            "landingPage": "https://data.nasa.gov/d/eh5s-w47p",
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
+            "title": "Effects of spaceflight on the immunoglobulin repertoire of unimmunized C57BL/6 mice"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10767",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-03-01",
-            "temporal": "2011-03-01T00:00:00Z/2014-02-01T00:00:00Z",
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
-                "wallops flight facility",
-                "project"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Charles Swenson",
                 "hasEmail": "mailto:chuck.swenson@lmco.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10767",
             "description": "&lt;p&gt;\r\n\t&amp;nbsp;&lt;/p&gt;\r\n&lt;p align=\"center\"&gt;\r\n\t&amp;nbsp;&lt;strong&gt;&lt;u&gt;Methodology &lt;/u&gt;&lt;/strong&gt;&lt;/p&gt;\r\n&lt;p&gt;\r\n\tFly a high altitude sounding rocket with multiple sub-payloads to measure electric and magnetic fields during an auroral event. Use ground based observations to observe winds and conductivities in the ionosphere.&lt;/p&gt;\r\n&lt;p&gt;\r\n\tThe Auroral Spatial Structures Probe (ASSP) is a NASA sounding rocket mission that, will be used to &lt;a href=\"http://adsabs.harvard.edu/abs/2011AGUFMSA31A1959S\" id=\"_GPLITA_0\" in_rurl=\"http://i.trkjmp.com/click?v=VVM6MzYxMzI6MjE1NTpzdHVkeTo2M2Y3MDQyYTE2ZTU0YTE5N2Q3OTVmNjk3ZWVhNmQwMjp6LTEwNDEtMTA3NTUzOmFkc2Ficy5oYXJ2YXJkLmVkdTozOTQ1NjpmYTVkMTdiYzQzNjMxMGQxNjJlYTMxYmFmYzZhN2MzMQ\" title=\"Click to Continue &amp;gt; by Text-Enhance\"&gt;study&lt;/a&gt; both the spatial and temporal small scale variation of the E-fields during breakup aurora and geomagnetically active conditions. This will be accomplished through the use of a constellation of small payloads that separate relative to each other throughout a sounding rocket flight. The multiple baseline observations of the electric and magnetic fields will be used to observe variability of both the E-field and the Poynting flux. These observations will be placed in the context of available data, including winds, large scale E-fields, and proxy conductivity (airglow images) observations. In this way we will address the main scientific objective of this mission which is: What are the contributions of small spatial scale and rapid temporal scale fluctuations of electric fields relative to the larger-scale electrodynamic processes? The high altitude rocket will be launched along the magnetic field line and carry six sub-payloads to be ejected from the main payload at high velocity. The sub-payloads will be deployed both along the flight path and perpendicular to the flight path so that both spatial features and temporal-spatial ambiguities can be explored. The low-mass sub-payloads that, for a fixed ejection impulse will achieve at least a 50 km separation by the end of the flight are key to the observational success. Each sub-payload will carry a crossed pair of double-probe sensors to measure in-situ electric fields, a three axis magnetometer, a Langmuir probe and a GPS receiver. In this poster we review the ASSP science and mission concepts.&lt;/p&gt;\r\n&lt;p&gt;\r\n\t&amp;nbsp;&lt;/p&gt;\r\n&lt;p&gt;\r\n\t&amp;nbsp;&lt;/p&gt;",
-            "title": "Auroral Spatial Structures Probe Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10767",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10767",
+            "issued": "2011-03-01",
+            "keyword": [
+                "active",
+                "wallops flight facility",
+                "project"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10767",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
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
+            "temporal": "2011-03-01T00:00:00Z/2014-02-01T00:00:00Z",
+            "title": "Auroral Spatial Structures Probe Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-MESH-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-mesh-ops-v1.0_eh9j-83ge",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-MESH-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-mesh-ops-v1.0_eh9j-83ge",
-            "description": "not applicable",
-            "title": "MER 2 MARS PANORAMIC CAMERA TERRAIN MESH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS PANORAMIC CAMERA TERRAIN MESH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0771-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-13T05:03:05.000 to 2015-05-13T07:05:20.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0771-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0771-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0771-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-13T05:03:05.000 to 2015-05-13T07:05:20.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0771 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0771 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H48P5XF7",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Agency for Toxic Substances and Disease Registry - ATSDR. 2010-05-26. ATSDR Hazardous Waste Site Polygon Data, Version 2. Version 2.00. Atlanta, GA. Archived by National Aeronautics and Space Administration, U.S. Government, Geospatial Research, Analysis, and Services Program (GRASP). https://doi.org/10.7927/H48P5XF7. https://doi.org/10.7927/H48P5XF7.",
-            "issued": "2010-05-26",
-            "temporal": "2010-05-26T00:00:00Z/2010-05-26T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2010-05-26",
-            "references": [
-                "https://doi.org/10.7927/H44X55RB",
-                "https://doi.org/10.7927/H4DF6P5Z"
-            ],
-            "keyword": [
-                "public health",
-                "earth science",
-                "human dimensions",
-                "environmental governance/management"
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
-            "identifier": "C1000000540-SEDAC",
-            "description": "The Agency for Toxic Substances and Disease Registry (ATSDR) Hazardous Waste Site Polygon Data, Version 2 consists of 2,080 polygons for selected hazardous waste sites that were compiled on May 26, 2010. Most polygons represent sites considered for cleanup under the Comprehensive Environmental Response, Compensation and Liability Act (CERCLA or Superfund). Typical sites are either on the EPA National Priorities List (NPL) or are being considered for inclusion on the NPL. The hazardous waste site boundaries maintained by the Geospatial Research, Analysis, and Services Program (GRASP, Division of Health Studies, Agency for Toxic Substances and Disease Registry, Centers for Disease Control and Prevention) contain NPL and non-NPL hazardous waste site boundaries for which health assessments or consultations have been requested.",
-            "release-place": "Atlanta, GA",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Agency for Toxic Substances and Disease Registry - ATSDR",
-            "title": "ATSDR Hazardous Waste Site Polygon Data, Version 2",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Agency for Toxic Substances and Disease Registry (ATSDR) Hazardous Waste Site Polygon Data, Version 2 consists of 2,080 polygons for selected hazardous waste sites that were compiled on May 26, 2010. Most polygons represent sites considered for cleanup under the Comprehensive Environmental Response, Compensation and Liability Act (CERCLA or Superfund). Typical sites are either on the EPA National Priorities List (NPL) or are being considered for inclusion on the NPL. The hazardous waste site boundaries maintained by the Geospatial Research, Analysis, and Services Program (GRASP, Division of Health Studies, Agency for Toxic Substances and Disease Registry, Centers for Disease Control and Prevention) contain NPL and non-NPL hazardous waste site boundaries for which health assessments or consultations have been requested.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH48P5XF7",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH48P5XF7",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/superfund/superfund-atsdr-hazardous-waste-site-v2/superfund-atsdr-hazardous-waste-site-v2-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/superfund/superfund-atsdr-hazardous-waste-site-v2/superfund-atsdr-hazardous-waste-site-v2-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/superfund-atsdr-hazardous-waste-site-v2/maps",
+            "identifier": "C1000000540-SEDAC",
+            "issued": "2010-05-26",
+            "keyword": [
+                "public health",
+                "earth science",
+                "human dimensions",
+                "environmental governance/management"
+            ],
+            "landingPage": "https://doi.org/10.7927/H48P5XF7",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2010-05-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H44X55RB",
+                "https://doi.org/10.7927/H4DF6P5Z"
+            ],
+            "release-place": "Atlanta, GA",
             "spatial": "-176.631973 13.433567 144.763215 68.36338",
+            "temporal": "2010-05-26T00:00:00Z/2010-05-26T00:00:00Z",
             "theme": [
                 "SSF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATSDR Hazardous Waste Site Polygon Data, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NDC8-E-ASAR-3-RDR-IMAGE-V1.0",
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
-                "earth",
-                "geologic remote sensing field experiment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "AIRSAR flew on NASA's DC-8 and acquired data at multiple incidence angles and azimuths over selected geological targets, such as sand dunes, volcanic fields, and alluvial fans. The GRSFE field areas overflown include the Lunar Crater Volcanic Field, Lunar Lake, Ubehebe Crater, and Death Valley. AIRSAR data consist of corrected Stokes matrices for the C, L, and P frequencies and data often exist for 2 or 3 incidence angles.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ndc8-e-asar-3-rdr-image-v1.0_ehaq-988b",
+            "issued": "2018-06-26",
+            "keyword": [
+                "earth",
+                "geologic remote sensing field experiment"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NDC8-E-ASAR-3-RDR-IMAGE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ndc8-e-asar-3-rdr-image-v1.0_ehaq-988b",
-            "description": "AIRSAR flew on NASA's DC-8 and acquired data at multiple incidence angles and azimuths over selected geological targets, such as sand dunes, volcanic fields, and alluvial fans. The GRSFE field areas overflown include the Lunar Crater Volcanic Field, Lunar Lake, Ubehebe Crater, and Death Valley. AIRSAR data consist of corrected Stokes matrices for the C, L, and P frequencies and data often exist for 2 or 3 incidence angles.",
-            "title": "NDC8 EARTH ASAR CALIBRATED REDUCED DATA RECORD IMAGE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NDC8 EARTH ASAR CALIBRATED REDUCED DATA RECORD IMAGE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR4A-CHECKOUT-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr4a-checkout-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "international rosetta mission",
@@ -706642,37 +706644,46 @@
                 "58 aql",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR4A-CHECKOUT-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr4a-checkout-v2.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 2 CR4A EDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 2 CR4A EDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ehhd-vvnw",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John M. Kusterer",
+                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
+            },
+            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist of half orbit (Night and Day) emissivity and cloud particle data related to pixels that have been co-located to the Lidar track.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l2_track_beta_v3_30_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000134",
             "issued": "2018-06-25",
-            "temporal": "2013-02-01/2014-06-05",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "atmospheric science",
                 "eos",
@@ -706682,274 +706693,264 @@
                 "satellite",
                 "climate"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/ehhd-vvnw",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000134",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist of half orbit (Night and Day) emissivity and cloud particle data related to pixels that have been co-located to the Lidar track.",
-            "title": "CALIPSO Imaging Infrared Radiometer L2 Data Track V3-30",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l2_track_beta_v3_30_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2013-02-01/2014-06-05",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Imaging Infrared Radiometer L2 Data Track V3-30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-EAR1-EARTHSWINGBY1-V1.0",
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
```

