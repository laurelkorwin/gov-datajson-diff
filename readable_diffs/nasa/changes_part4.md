# Change History for nasa.json (Part 4)

### Changes from ee34c60 to f6ed368
**Author:** Automated

**Date:** 2025-02-03 14:11:58+00:00

**Message:** Updated data: Mon Feb  3 14:11:58 UTC 2025

```diff
diff --git a/nasa.json b/nasa.json
index 5134a2c..0c365fe 100644
--- a/nasa.json
+++ b/nasa.json
@@ -6011,15 +6011,15 @@
             "identifier": "C1430594808-NSIDCV0",
             "issued": "1978-10-26",
             "keyword": [
-                "sea ice",
+                "earth science",
                 "cryosphere",
-                "earth science"
+                "sea ice"
             ],
             "landingPage": "https://doi.org/10.7265/N5K072F8",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-07-12",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -6028,7 +6028,7 @@
                 "name": "NSIDC"
             },
             "spatial": "-180.0 -90.0 180.0 -39.23",
-            "temporal": "1978-10-26T00:00:00Z/2024-07-15T00:00:00Z",
+            "temporal": "1978-10-26T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -22464,7 +22464,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-04",
+            "modified": "2025-01-12",
             "programCode": [
                 "026:001"
             ],
@@ -22473,7 +22473,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2000-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
@@ -22766,16 +22766,16 @@
             "identifier": "C2619443888-POCLOUD",
             "issued": "2020-12-17",
             "keyword": [
+                "earth science",
                 "oceans",
                 "sea surface topography",
-                "ocean waves",
-                "earth science"
+                "ocean waves"
             ],
             "landingPage": "https://doi.org/10.5067/S6AP4-1AHNTR-F08",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-23",
+            "modified": "2025-01-03",
             "programCode": [
                 "026:001"
             ],
@@ -22788,7 +22788,7 @@
             ],
             "release-place": "PO.DAAC",
             "spatial": "-180.0 -66.15 180.0 66.15",
-            "temporal": "2020-11-30T14:26:00.822Z/2025-01-27T00:00:00Z",
+            "temporal": "2020-11-30T14:26:00.822Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
@@ -30898,65 +30898,6 @@
             ],
             "title": "SMAPVEX16 Manitoba In Situ Vegetation Data V001"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "MISR Science Team (2015), Terra/MISR Level 2, Aerosol, version 2, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/Terra/MISR/MIL2ASAE_L2.002",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Earl Hansen",
-                "hasEmail": "mailto:earl.g.hansen@jpl.nasa.gov"
-            },
-            "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 2 Aerosol parameters V002 contains Aerosol optical depth and particle type, with associated atmospheric data.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL2ASAE_L2.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "The product quality assessment may be downloaded directly from this link",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/PRODOCS/misr/Quality_Summaries/L2_AS_Products.html",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677706-LARC",
-            "issued": "2003-03-24",
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "atmosphere",
-                "air quality"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL2ASAE_L2.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2018-10-15",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-24T16:33:37Z/2017-06-01T01:08:56Z",
-            "theme": [
-                "MISR",
-                "geospatial"
-            ],
-            "title": "MISR Level 2 Aerosol parameters V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -51732,54 +51673,6 @@
             ],
             "title": "SMEX02 Land Surface Information: Soils Database, Version 1"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Aerosol Product covering a quarter's (seasonal) products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Aerosol Product covering a quarter (seasonal)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QAE_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677727-LARC",
-            "issued": "2003-12-03",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QAE_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Aerosol Product covering a quarter (seasonal) V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -53876,20 +53769,20 @@
             "identifier": "C2105705664-LANCEMODIS",
             "issued": "2021-03-01",
             "keyword": [
-                "land surface",
-                "biosphere",
                 "earth science",
+                "biosphere",
                 "ecological dynamics",
-                "national geospatial data asset",
-                "ngda",
+                "land surface",
                 "surface radiative properties",
-                "surface thermal properties"
+                "surface thermal properties",
+                "ngda",
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/FIRMS/MODIS/MCD14DL.NRT.0061",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-28",
+            "modified": "2025-02-04",
             "programCode": [
                 "026:001"
             ],
@@ -53903,7 +53796,7 @@
             ],
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2019-12-15T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2019-12-15T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
@@ -55175,18 +55068,18 @@
             "identifier": "C2263893831-LAADS",
             "issued": "2022-05-05",
             "keyword": [
-                "clouds",
-                "ngda",
                 "earth science",
-                "atmospheric radiation",
                 "atmosphere",
+                "atmospheric radiation",
+                "clouds",
+                "ngda",
                 "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MCD06COSP_D3_MODIS.062",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-20",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -55196,7 +55089,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
@@ -58935,7 +58828,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO1BGEO Version 1 data product provides the geolocation information for the radiance values retrieved in the ECO1BRAD Version 1 data product (https://doi.org/10.5067/ECOSTRESS/ECO1BRAD.001). The ECO1BGEO data product should be used to georeference the ECO1BRAD, ECO2CLD, ECO2LSTE, ECO3ANCQA, ECO3ETPTJPL, ECO4ESIPTJPL, ECO4WUE data products. The geolocation processing corrects the ISS-reported ephemeris and attitude data by image matching with a global ortho-base derived from Landsat data, and then assigns latitude and longitude values to each of the Level 1 radiance pixels. When image matching is successful, the data are geolocated to better than 50 meter (m) accuracy. The ECO1BGEO data product is provided as swath data.\r\n\r\nThe ECO1BGEO data product contains data layers for latitude and longitude values, solar and view geometry information, surface height, and the fraction of pixel on land versus water.\r\n\r\nKnown Issues: *Geolocation accuracy: In cases where scenes were not successfully matched with the ortho-base, the geolocation error is significantly larger, with the worst-case geolocation error for uncorrected data being at 7 kilometers (km). Within the metadata of the ECO1BGEO file, if the field \"L1GEOMetadata/OrbitCorrectionPerformed\" is \"True,\" the data was corrected, and geolocation accuracy should be better than 50 m. If this is \"False,\" then the data was processed without correcting the geolocation and will have up to 7 km geolocation error.\r\n*Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECO1BGEO Version 1 data product provides the geolocation information for the radiance values retrieved in the ECO1BRAD Version 1 data product. The ECO1BGEO data product should be used to georeference the ECO1BRAD, ECO2CLD, ECO2LSTE, ECO3ANCQA, ECO3ETPTJPL, ECO4ESIPTJPL, and ECO4WUE data products. The geolocation processing corrects the ISS-reported ephemeris and attitude data by image matching with a global ortho-base derived from Landsat data and then assigns latitude and longitude values to each of the Level 1 radiance pixels. When image matching is successful, the data are geolocated to better than 50 meter (m) accuracy. The ECO1BGEO data product is provided as swath data.\n\nThe ECO1BGEO data product contains data variables for latitude and longitude values, solar and view geometry information, surface height, and the fraction of pixel on land versus water.\n\nKnown Issues\n\n* Geolocation accuracy: In cases where scenes were not successfully matched with the ortho-base, the geolocation error is significantly larger, with the worst-case geolocation error for uncorrected data being at 7 kilometers (km). Within the metadata of the ECO1BGEO file, if the field \"L1GEOMetadata/OrbitCorrectionPerformed\" is \"True,\" the data was corrected, and geolocation accuracy should be better than 50 m. If this is \"False,\" then the data was processed without correcting the geolocation and will have up to 7 km geolocation error.\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59005,21 +58898,21 @@
                     "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View information related to this dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -59030,7 +58923,7 @@
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
                     "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
@@ -59046,15 +58939,15 @@
             "identifier": "C1534584923-LPDAAC_ECS",
             "issued": "2019-03-27",
             "keyword": [
-                "sensor characteristics",
                 "earth science",
-                "spectral/engineering"
+                "spectral/engineering",
+                "sensor characteristics"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-09-04",
+            "modified": "2025-01-06",
             "programCode": [
                 "026:001"
             ],
@@ -59065,7 +58958,7 @@
             "release-place": "Sioux Falls, South Dakota, USA",
             "series-name": "ECO1BGEO.001",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-09-09T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-01-06T23:59:09Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -66003,15 +65896,15 @@
             "identifier": "C2548344839-NSIDC_ECS",
             "issued": "2024-08-29",
             "keyword": [
-                "sea ice",
+                "earth science",
                 "cryosphere",
-                "earth science"
+                "sea ice"
             ],
             "landingPage": "https://doi.org/10.5067/ATLAS/ATL07QL.006",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-02-02",
             "programCode": [
                 "026:001"
             ],
@@ -66020,7 +65913,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-08-29T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-08-29T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -85367,7 +85260,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-22",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -85377,7 +85270,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -87004,54 +86897,6 @@
             ],
             "title": "DAWN VIR RAW (EDR) VESTA VISIBLE SPECTRA V2.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Albedo product in netCDF format covering a year;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "MISR Level 3 Component Global Albedo publicly available product in netCDF format covering a year.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YALN_L3.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919888-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YALN_L3.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Albedo product in netCDF format covering a year V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -98977,54 +98822,6 @@
             ],
             "title": "IPCC IS92 Emissions Scenarios (A, B, C, D, E, F) Dataset Version 1.1"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "The TES Aura L3 ATD data consist of daily atmospheric temperature and VMR for the atmospheric species. Data are provided at 2 degree latitude X 4 degree longitude spatial grids and at a subset of TES standard pressure levels. The TES Science Data Processing L3 subsystem interpolates the L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products are composed of L3 HDF - EOS-EOS grid data. A separate product file is produced for each different atmospheric species. TES obtains data in two basic observation modes: Limb or Nadir. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing are the terms 'Daily' and 'Monthly' representing the approximate time coverage of the L3 products. However the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey will not be split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represent a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products are 'daily' and 'monthly'. L3 data is provided at uniform grids in latitude and longitude and at selected pressure levels. Details of the format of this product can be found in the TES Data Products Specifications (DPS) which is available from the LaRC ASDC site: https://eosweb.larc.nasa.gov/project/tes/DPS",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESTL3ATM_L3",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C1000000640-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESTL3ATM_L3",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L3 Atmospheric Temperatures Monthly Gridded V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -107593,7 +107390,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-07",
+            "modified": "2025-01-16",
             "programCode": [
                 "026:001"
             ],
@@ -107602,7 +107399,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1992-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1992-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IDS",
                 "geospatial"
@@ -109177,17 +108974,17 @@
             "identifier": "C1511761518-CDDIS",
             "issued": "1998-01-01",
             "keyword": [
-                "geodetics",
-                "tectonics",
                 "earth science",
                 "solid earth",
-                "gravity/gravitational field"
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSIONOTEC_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-11",
+            "modified": "2025-01-18",
             "programCode": [
                 "026:001"
             ],
@@ -109196,7 +108993,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1998-01-01T00:00:00Z/2025-01-20T00:00:00Z",
+            "temporal": "1998-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
@@ -120764,7 +120561,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-27",
+            "modified": "2025-02-03",
             "programCode": [
                 "026:001"
             ],
@@ -120773,7 +120570,7 @@
                 "name": "ASF"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2015-02-12T16:02:58Z/2025-01-27T00:00:00Z",
+            "temporal": "2015-02-12T16:02:58Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -136845,15 +136642,15 @@
             "identifier": "C2807623096-LANCEMODIS",
             "issued": "2023-11-20",
             "keyword": [
+                "earth science",
                 "land surface",
-                "surface radiative properties",
-                "earth science"
+                "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA2N.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -136863,7 +136660,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -137926,7 +137723,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-11",
+            "modified": "2025-01-18",
             "programCode": [
                 "026:001"
             ],
@@ -137935,7 +137732,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1992-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1992-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
@@ -137998,7 +137795,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -138008,7 +137805,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2021-09-13T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2021-09-13T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "Terra",
@@ -150631,64 +150428,6 @@
             ],
             "title": "ARC Code TI: Mariana"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "MISR Science Team (2015), Terra/MISR Level 2, TOA/Cloud Classifiers, version 3, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/Terra/MISR/MIL2TCCL_L2.003",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Roger Davies",
-                "hasEmail": "mailto:r.davies@auckland.ac.nz"
-            },
-            "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 2 TOA/Cloud Classifier parameters V003 contains the Angular Signature Cloud Mask (ASCM), Regional Cloud Classifiers, Cloud Shadow Mask, and Topographic Shadow Mask, with associated data.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL2TCCL_L2.003",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "The product quality assessment may be downloaded directly from this link",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/PRODOCS/misr/Quality_Summaries/L2_Cloud_Products.html",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677712-LARC",
-            "issued": "2003-03-24",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL2TCCL_L2.003",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2018-10-15",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-24T16:33:37Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "MISR",
-                "geospatial"
-            ],
-            "title": "MISR Level 2 TOA/Cloud Classifier parameters V003"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
@@ -150923,7 +150662,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -150933,7 +150672,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:45:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:45:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -151781,6 +151520,96 @@
             ],
             "title": "MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Gridded 1-Degree Annual Soil Moisture V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/CDNI7NG92EHP.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This data set contains Level-3 gridded annual global soil moisture estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCDNI7NG92EHP",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_ANSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2777839286-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_ANSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2777839286-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CDNI7NG92EHP",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CDNI7NG92EHP",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2777839286-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/CDNI7NG92EHP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Gridded 1-Degree Annual Soil Moisture V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -152700,17 +152529,17 @@
             "identifier": "C2551528419-NSIDC_ECS",
             "issued": "2024-08-29",
             "keyword": [
-                "spectral/engineering",
+                "earth science",
                 "atmosphere",
                 "clouds",
-                "earth science",
+                "spectral/engineering",
                 "lidar"
             ],
             "landingPage": "https://doi.org/10.5067/ATLAS/ATL09QL.006",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-02-02",
             "programCode": [
                 "026:001"
             ],
@@ -152719,7 +152548,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-08-29T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-08-29T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -154325,7 +154154,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Swath Geolocation Instantaneous Level 1B Global (ECO_L1B_GEO) Version 2 data product provides the geolocation information for the radiance values retrieved in the ECO_L1B_RAD (https://doi.org/10.5067/ecostress/eco_l1b_rad.002) Version 2 data product. The geolocation product gives geo-tagging to each of the radiance pixels. The geolocation processing corrects the ISS-reported ephemeris and attitude data by image matching with a global ortho-base derived from Landsat data, and then assigns latitude and longitude values to each of the Level 1 radiance pixels. When image matching is successful, the data are geolocated to better than 50 meter (m) accuracy. The ECO_L1B_GEO data product is provided as swath data.\n\nThe ECO_L1B_GEO data product contains data layers for latitude and longitude values, solar and view geometry information, surface height, and the fraction of pixel on land versus water distributed in HDF5 format.\n\nImprovements/Changes from Previous Versions\n\n-\tIf the initial co-registration is of poor quality or fails, up to four retries are attempted using modified parameters to match the scene. See Section 4.2 of the User Guide (https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf).\n\nKnown Issues\n\n-\tGeolocation accuracy: In cases where scenes were not successfully matched with the ortho-base, the geolocation error is significantly larger; the worst-case geolocation error for uncorrected data is 7 kilometers (km). Within the metadata of the ECO_L1B_GEO file, if the field \"L1GEOMetadata/OrbitCorrectionPerformed\" is \"True\", the data was corrected, and geolocation accuracy should be better than 50 m. If this field is \"False\", then the data was processed without correcting the geolocation and will have up to 7 km geolocation error.\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Swath Geolocation Instantaneous Level 1B Global (ECO_L1B_GEO) Version 2 data product provides the geolocation information for the radiance values retrieved in the ECO_L1B_RAD (https://doi.org/10.5067/ecostress/eco_l1b_rad.002) Version 2 data product. The geolocation product gives geo-tagging to each of the radiance pixels. The geolocation processing corrects the ISS-reported ephemeris and attitude data by image matching with a global ortho-base derived from Landsat data and then assigns latitude and longitude values to each of the Level 1 radiance pixels. When image matching is successful, the data are geolocated to better than 50 meter (m) accuracy. The ECO_L1B_GEO data product is provided as swath data.\n\nThe ECO_L1B_GEO data product contains data layers for latitude and longitude values, solar and view geometry information, surface height, and the fraction of pixel on land versus water distributed in HDF5 format.\n\nKnown Issues\n\n* Geolocation accuracy: In cases where scenes were not successfully matched with the ortho-base, the geolocation error is significantly larger; the worst-case geolocation error for uncorrected data is 7 kilometers (km). Within the metadata of the ECO_L1B_GEO file, if the field \"L1GEOMetadata/OrbitCorrectionPerformed\" is \"True\", the data was corrected, and geolocation accuracy should be better than 50 m. If this field is \"False\", then the data was processed without correcting the geolocation and will have up to 7 km geolocation error.\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\nImprovements/Changes from Previous Versions\n\n* If the initial co-registration is of poor quality or fails, up to four retries are attempted using modified parameters to match the scene. See Section 4.2 of the User Guide.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154422,15 +154251,15 @@
             "identifier": "C2076087338-LPCLOUD",
             "issued": "2022-11-14",
             "keyword": [
-                "surface thermal properties",
+                "earth science",
                 "land surface",
-                "earth science"
+                "surface thermal properties"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-19",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -154440,7 +154269,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-12-23T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -160409,55 +160238,6 @@
             ],
             "title": "USGS Global Forest Observations Initiative (GFOI) Cambodia"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESHNO3L_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C191856319-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "air quality",
-                "earth science",
-                "atmospheric chemistry/nitrogen compounds",
-                "atmosphere"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESHNO3L_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 HNO3 Limb V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -169533,7 +169313,7 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_FR_001.",
+            "citation": "International Laser Ranging Service (ILRS), SLR monthly full-rate data summary, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/SLR/slr_data_monthlysum_fr_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
@@ -169564,15 +169344,15 @@
             "identifier": "C3242607946-CDDIS",
             "issued": "1976-01-01",
             "keyword": [
+                "earth science",
                 "solid earth",
-                "geodetics",
-                "earth science"
+                "geodetics"
             ],
             "landingPage": "https://doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_FR_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-10-22",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -169581,7 +169361,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1976-01-01T00:00:00Z/2024-10-28T00:00:00Z",
+            "temporal": "1976-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -181392,27 +181172,27 @@
             "identifier": "C1238517289-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
-                "atmospheric chemistry",
+                "earth science",
+                "atmosphere",
+                "altitude",
                 "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
+                "land surface",
                 "surface radiative properties",
-                "ocean temperature",
                 "oceans",
+                "ocean temperature",
                 "surface thermal properties",
-                "land surface",
-                "earth science",
-                "clouds",
-                "atmospheric water vapor",
                 "air quality",
-                "altitude",
-                "atmospheric temperature",
-                "atmosphere",
-                "atmospheric radiation"
+                "atmospheric radiation",
+                "atmospheric chemistry"
             ],
             "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA303",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-17",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -181427,7 +181207,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "AIRS3STD",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-31T00:00:00Z/2025-01-20T00:00:00Z",
+            "temporal": "2002-08-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -196591,7 +196371,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-29",
+            "modified": "2025-01-05",
             "programCode": [
                 "026:001"
             ],
@@ -196600,7 +196380,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1992-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1992-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IDS",
                 "geospatial"
@@ -196869,54 +196649,6 @@
             ],
             "title": "JUNO JUPITER JIRAM REDUCED DATA         \n                                      RECORD V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESTLS_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C191856337-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESTLS_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 Atmospheric Temperatures Limb Special Observation V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -199583,23 +199315,23 @@
             "identifier": "C1443743314-LAADS",
             "issued": "2017-10-01",
             "keyword": [
-                "ngda",
-                "atmospheric radiation",
-                "aerosols",
-                "weather events",
-                "national geospatial data asset",
                 "earth science",
-                "clouds",
+                "atmosphere",
+                "aerosols",
+                "atmospheric chemistry",
+                "atmospheric radiation",
                 "atmospheric temperature",
                 "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric chemistry"
+                "clouds",
+                "weather events",
+                "ngda",
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MYD08_E3.061",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-17",
+            "modified": "2025-01-25",
             "programCode": [
                 "026:001"
             ],
@@ -199609,7 +199341,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -201833,7 +201565,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-25",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -201842,7 +201574,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -85.044 180.0 85.044",
-            "temporal": "2015-03-31T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2015-03-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -204045,7 +203777,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-15",
+            "modified": "2025-01-23",
             "programCode": [
                 "026:001"
             ],
@@ -204055,7 +203787,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -213410,54 +213142,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1388 V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Land Product covering a day's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Land Product covering a day",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DLS_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677716-LARC",
-            "issued": "2003-12-03",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DLS_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Land Product covering a day V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -214123,57 +213807,6 @@
             ],
             "title": "SAFARI 2000 MODIS Water and Heat Fluxes, Maun, Botswana, Dry Season 2001"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Near Real Time Level 2 Cloud Motion Vector parameters in BUFR format;See ProductionDateTime for published Date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This is the MISR Level 2 Cloud Motion Vector Product containing height-resolved cloud motion vectors with associated data in BUFR format.  It is used for MISR Near Real Time processing, and is derived from session-based Level 0 input files.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI2TC_CMV_BFR_NRT_L2.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C1000000120-LARC",
-            "issued": "2015-04-01",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI2TC_CMV_BFR_NRT_L2.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2017-06-21",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2021-10-11T03:30:50.121Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "MISR Near Real Time (NRT) Level 2 Cloud Motion Vector parameters in BUFR format V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -214374,14 +214007,14 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Simon Hook, Mike Smyth, Tom Logan, William Johnson. 2019-03-27. ECO1BATT.001. ECOSTRESS Attitude Daily L1B Global 70 m V001. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO1BATT.001. https://doi.org/10.5067/ECOSTRESS/ECO1BATT.001. The DOI landing page provides citations in APA and Chicago styles..",
+            "citation": "Simon Hook, Mike Smyth, Tom Logan, William Johnson. 2019-03-27. ECO1BATT.001. ECOSTRESS Attitude Daily L1B Global 70 m V001. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO1BATT.001. https://doi.org/10.5067/ECOSTRESS/ECO1BATT.001.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Simon Hook",
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO1BATT Version 1 data product provides both corrected and uncorrected attitude quaternions and spacecraft ephemeris data obtained from the ISS. The data are provided in 1 second intervals by the ISS, and each product file contains vectors from the duration of the orbit. The time elements are copied from the ISS raw data.  \r\n\r\nThe ECO1BATT Version 1 data product contains layers of corrected and uncorrected attitude quaternions, spacecraft ephemeris data including Earth-centered inertial (ECI) position and velocity, and associated time elements. \r\n\r\nKnown Issues: *Cannot perform spatial query on ECO1BATT in NASA Earthdata Search: ECO1BATT does not contain spatial attributes, so granules cannot be searched by geographic location. Users should search for ECO1BATT data products by orbit number instead.\r\n*Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECO1BATT Version 1 data product provides both corrected and uncorrected attitude quaternions and spacecraft ephemeris data obtained from the ISS. The data are provided in 1 second intervals by the ISS, and each product file contains vectors from the duration of the orbit. The time elements are copied from the ISS raw data.\n\nThe ECO1BATT Version 1 data product contains variables of corrected and uncorrected attitude quaternions, spacecraft ephemeris data including Earth-centered inertial (ECI) position and velocity, and associated time elements. \n\nKnown Issues\n\n* Cannot perform spatial query on ECO1BATT in NASA Earthdata Search: ECO1BATT does not contain spatial attributes, so granules cannot be searched by geographic location. Users should search for ECO1BATT data products by orbit number instead.\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -214451,21 +214084,21 @@
                     "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View information related to this dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -214478,15 +214111,15 @@
             "identifier": "C1534582884-LPDAAC_ECS",
             "issued": "2019-03-27",
             "keyword": [
-                "platform characteristics",
                 "earth science",
-                "spectral/engineering"
+                "spectral/engineering",
+                "platform characteristics"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO1BATT.001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-09-04",
+            "modified": "2025-01-06",
             "programCode": [
                 "026:001"
             ],
@@ -214497,8 +214130,9 @@
             "release-place": "Sioux Falls, South Dakota, USA",
             "series-name": "ECO1BATT.001",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-09-09T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-01-06T23:59:09Z",
             "theme": [
+                "ECOSTRESS",
                 "geospatial"
             ],
             "title": "ECOSTRESS Attitude Daily L1B Global 70m V001"
@@ -219495,111 +219129,6 @@
             ],
             "title": "Reflectance Reference Targets (OTTER)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "SAGE III/ISS Science Team (2022), SAGE III/ISS L1B Solar Event Transmission Data (Native), version 5.3, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/ISS/SAGEIII/SOLAR_BINARY_L1B-V5.3",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dr. David Flittner",
-                "hasEmail": "mailto:david.e.flittner@nasa.gov"
-            },
-            "description": "g3btb_53 is the Stratospheric Aerosol and Gas Experiment III (SAGE III) on the International Space Station (ISS) (SAGE III/ISS) Level 1B Solar Event Transmission Data (Native) V053 data product. It contains pixel group transmission profiles for a single solar event. SAGE III was Launched on February 19, 2017 on a SpaceX Falcon 9 from Kennedy Space Center, SAGE III-ISS is the second instrument from the SAGE III project, externally mounted on the ISS. Data collection for this product is ongoing. This ISS-based instrument uses a technique known as occultation, which involves looking at the light from the Sun or Moon as it passes through Earth's atmosphere at the edge, or limb, of the planet to provide long-term monitoring of ozone vertical profiles of the stratosphere and mesosphere. The data provided by SAGE III-ISS includes key components of atmospheric composition and their long-term variability, focusing on the study of aerosols, chlorine dioxide, clouds, nitrogen dioxide, nitrogen trioxide, pressure and temperature, and water vapor. SAGE data has historically been used by the World Meteorological Organization to inform their periodic assessments of ozone depletion. These new observations from the International Space Station will continue the SAGE team's contributions to ongoing scientific understanding of the Earth's atmosphere.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FSOLAR_BINARY_L1B-V5.3",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE project home page",
-                    "downloadURL": "https://sage.larc.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "DOI data set landing page for g3btb_53",
-                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_BINARY_L1B-V5.3",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.zip)",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/readers_G3B_v05.30.zip",
-                    "mediaType": "application/zip",
-                    "title": "Downloadable software applications"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Version 5.30 DPUG (Data Product User's Guide)",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG_G3B_v05.30.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's user's guide"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "How to cite ASDC data",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Open Source Agreement for Computer Software",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Version 5.30 Release Notes",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/ReleaseNotes_G3B_v05.30.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Earthdata Search for g3btb_53 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2626885220-LARC",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                }
-            ],
-            "identifier": "C2626885220-LARC",
-            "issued": "2022-11-10",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_BINARY_L1B-V5.3",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2022-11-17",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2017-06-07T00:00:00Z/2023-04-10T00:00:00Z",
-            "theme": [
-                "SAGE III-ISS",
-                "geospatial"
-            ],
-            "title": "SAGE III/ISS L1B Solar Event Transmission Data (Native) V053"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -220842,7 +220371,7 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/SLR/SLR_DAILY_NPT_001.",
+            "citation": "International Laser Ranging Service (ILRS), SLR daily normal point data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/SLR/slr_data_daily_npt_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
@@ -220883,16 +220412,16 @@
             "issued": "1976-01-01",
             "keyword": [
                 "earth science",
-                "geodetics",
-                "tectonics",
                 "solid earth",
-                "gravity/gravitational field"
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/SLR/SLR_DAILY_NPT_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-15",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -220901,7 +220430,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2016-01-01T00:00:00Z/2024-11-18T00:00:00Z",
+            "temporal": "2016-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
@@ -222199,55 +221728,6 @@
             ],
             "title": "CCD OBSERVATIONS V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESH2OL_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C191856311-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric temperature"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESH2OL_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 H2O Limb V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -222827,54 +222307,6 @@
             ],
             "title": "NEW HORIZONS\n      REX KEM1\n      RAW V2.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Global Cloud public Product in netCDF format covering a quarter;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Global Cloud public Product in netCDF format covering a quarter (seasonal)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3QCLDN_L3.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919910-LARC",
-            "issued": "2006-03-01",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3QCLDN_L3.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Global Cloud public Product in netCDF format covering a quarter V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -227696,99 +227128,6 @@
             ],
             "title": "MLS/Aura Level 3 Daily Binned Cloud Ice (IWC) on Zonal and Similar Grids V005 (ML3DZIWC) at GES DISC"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "2013-01-01. Archived by National Aeronautics and Space Administration, U.S. Government, ASDC. https://doi.org/10.5067/AURA/TES/TESTL3CO2LM_L3. http://eosweb.larc.nasa.gov/project/tes/tes_table.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "SCOTT GLUCK",
-                "hasEmail": "mailto:Scott.Gluck@jpl.nasa.gov"
-            },
-            "description": "The TES Aura L3 CO2 data consist of daily atmospheric temperature and VMR for the atmospheric species. Data are provided at 2 degree latitude X 4 degree longitude spatial grids and at a subset of TES standard pressure levels. The TES Science Data Processing L3 subsystem interpolates the L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products are composed of L3 HDF - EOS-EOS grid data. A separate product file is produced for each different atmospheric species. TES obtains data in two basic observation modes: Limb or Nadir. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing are the terms Daily and Monthly representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey will not be split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represent a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products are daily and monthly. Details of the format of this product can be found in the TES Data Products Specifications (DPS) which is available from the LaRC ASDC site: http://eosweb.larc.nasa.gov/project/tes/DPS",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESTL3CO2LM_L3",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://tes.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/project/tes/tes_table",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/project/tes/tes-quality-statements",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eospso.gsfc.nasa.gov/atbd-category/53",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://l5eil01.larc.nasa.gov/TES/TL3CO2LM.003/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through its archiver."
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://reverb.echo.nasa.gov/reverb/#utf8=%E2%9C%93&spatial_map=satellite&spatial_type=rectangle&keywords=TL3CO2",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "DOI data set landing page for TL3CO2LM_3",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TESTL3CO2LM_L3",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                }
-            ],
-            "identifier": "C189920635-LARC",
-            "issued": "2004-08-22",
-            "keyword": [
-                "atmospheric chemistry",
-                "air quality",
-                "atmosphere",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESTL3CO2LM_L3",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2024-12-18",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-08-22T00:00:00Z/2024-12-23T00:00:00Z",
-            "theme": [
-                "TES",
-                "geospatial"
-            ],
-            "title": "TES/Aura L3 CO2 Lite Monthly Gridded V003"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -231199,92 +230538,6 @@
             ],
             "title": "CALIPSO Lidar L2 1 km Cloud Layer Data V3-02"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "2013-01-01. Archived by National Aeronautics and Space Administration, U.S. Government, ASDC. https://doi.org/10.5067/AURA/TES/TESN2OL_L2.006. http://eosweb.larc.nasa.gov/project/tes/tes_table.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "SCOTT GLUCK",
-                "hasEmail": "mailto:Scott.Gluck@jpl.nasa.gov"
-            },
-            "description": "The TES Aura L2 NO2 data consist of information for one molecular species for an entire Global Survey or Special Observation. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality and other data (e.g., surface characteristics for nadir observations) are also provided. L2 modeled spectra are evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compares observed spectra to the modeled spectra and iteratively updates the atmospheric parameters. L2 standard product files include information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consists of a maximum of 16 consecutive orbits. Nadir and limb observations are in separate L2 files, and a single ancillary file is composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey is a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations currently only use a single set of filter mix. A Limb sequence within the TES Global Survey is three high-resolution scans over the same limb locations. The Limb standard product will consist of four files, where each file will be composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations use a repeating sequence of filter wheel positions. Special Observations can only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and are conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depends on the science requirement. See http://tes.jpl.nasa.gov/instrument/specialobservations/ for details. A Global Survey consists of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals are performed (1,152 nadir retrievals and 1,152 retrievals in time ordered sequence for each limb observation). Each observation is the input for retrievals of species Volume Mixing Ratios (VMR), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density and other diagnostic quantities. Each TES Level 2 standard product reports information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object is bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product can have a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals are not reported. Each limb observation Limb 1, Limb 2 and Limb 3, are processed independently. Thus each limb standard product consists of three sets where each set consist of 1,152 observations. For TES, the swath object represents one of these sets. Thus each limb standard product consists of three swath objects, one for each observation, Limb 1, Limb 2, and Limb 3. The organization of data within the Swath object is based on a superset of the UARS pressure levels used to report concentrations of trace atmospheric gases. The reporting grid is the same pressure grid used for modeling. There are 67 reporting levels from 1211.53 hPa, which allows for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products will report values directly at the surface when po",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESN2OL_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://tes.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/project/tes/tes_table",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/project/tes/tes-quality-statements",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eospso.gsfc.nasa.gov/atbd-category/53",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://l5eil01.larc.nasa.gov/TES/TL2NO2L.006/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through its archiver."
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://reverb.echo.nasa.gov/reverb/#utf8=?%3F%3F=&spatial_map=satellite&spatial_type=rectangle&keywords=TL2NO2",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                }
-            ],
-            "identifier": "C191856327-LARC",
-            "issued": "2004-08-22",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESN2OL_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2021-05-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-08-22T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "TES",
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 NO2 Limb V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -236486,7 +235739,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-17",
+            "modified": "2025-01-25",
             "programCode": [
                 "026:001"
             ],
@@ -236496,7 +235749,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-18T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2000-02-18T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
@@ -244779,6 +244032,98 @@
             ],
             "title": "BOREAS TGB-01 SF6 Chamber Flux Data: NSA"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Weekly Polar-Gridded Sea Surface Salinity V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/Aquarius/AQ3_SSS.005.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This data set consists of weekly gridded Level-3 products of Aquarius L-band radiometer Sea Surface Salinity (SSS) retrievals from the Aquarius/Sat\u00e9lite de Aplicaciones Cient\u00edficas (SAC-D) mission, developed collaboratively between the U.S. National Aeronautics and Space Administration (NASA) and Argentina's space agency, Comisi\u00f3n Nacional de Actividades Espaciales (CONAE).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAquarius%2FAQ3_SSS.005",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_SSS+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2791494051-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_SSS+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2791494051-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/Aquarius/AQ3_SSS.005",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/Aquarius/AQ3_SSS.005",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2791494051-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "sea ice",
+                "oceans",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aquarius/AQ3_SSS.005",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -79.0 180.0 -50.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-04T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Weekly Polar-Gridded Sea Surface Salinity V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -249234,16 +248579,16 @@
             "identifier": "C2619444025-POCLOUD",
             "issued": "2020-12-17",
             "keyword": [
-                "ocean waves",
                 "earth science",
                 "oceans",
-                "sea surface topography"
+                "sea surface topography",
+                "ocean waves"
             ],
             "landingPage": "https://doi.org/10.5067/S6AP4-2LSNUR-F08",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-03",
+            "modified": "2025-01-13",
             "programCode": [
                 "026:001"
             ],
@@ -249257,7 +248602,7 @@
             "release-place": "PO.DAAC",
             "series-name": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography (Unvalidated)",
             "spatial": "-180.0 -66.15 180.0 66.15",
-            "temporal": "2020-11-30T14:26:00.843Z/2025-01-27T00:00:00Z",
+            "temporal": "2020-11-30T14:26:00.843Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
@@ -249348,6 +248693,288 @@
             ],
             "title": "U.S. Climate Risk Projections by County, 2040-2049"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "MISR Science Team (2004), Terra/MISR Level 1B, Radiometric camera-by-camera Cloud Mask subset for the UAE region, version 3, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Diner",
+                "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
+            },
+            "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR radiometric camera-by-camera Cloud Mask subset for the UAE region V003 contains the Radiometric camera-by-camera Cloud Mask dataset. It is used to determine whether a scene is classified as clear or cloudy.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FUAEMIRCM.003",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
+                    "title": "View this dataset's data citation policy"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MISR",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
+                    "mediaType": "text/html",
+                    "title": "View this dataset's algorithm theoretical basis document"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc/misr_loc.html",
+                    "mediaType": "text/html",
+                    "title": "Use this dataset in a web based tool"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "UAE Local Mode Sites Table",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Overview of MISR Data at the ASDC, 2023",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's data quality document"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "MISR Level 2 Top-of-Atmosphere/Cloud Products Quality Statement - December 01, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L2_Cloud_Products.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's data quality document"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View a micro article on this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for UAEMIRCM_3",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/UAEMIRCM.003",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "MISR Level 2 Current Production Report",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L2_PR.cgi",
+                    "mediaType": "text/html",
+                    "title": "View this dataset's production history"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "MISR Mission Overview",
+                    "downloadURL": "https://misr.jpl.nasa.gov/Mission/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "MISR project home page",
+                    "downloadURL": "https://misr.jpl.nasa.gov/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR RCCM Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/rccm.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's production history"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's documented anomalies"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's user's guide"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR Data Versioning Index",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's production history"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents//misr/dps/misr_dps_dps.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's product usage"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for Specific Products MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's product usage"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC webpage for MISR Regional UAE Imagery Overview",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/field_campaign_imagery/uae/regional/overview.html",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for UAEMIRCM_3 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1627523806-LARC",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC MISR Acquisition Schedule for UAE2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/uae/uae_calendar.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's processing history"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for UAEMIRCM_003",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/UAE/UAEMIRCM.003/contents.html",
+                    "mediaType": "text/html",
+                    "title": "Use OPeNDAP to access the dataset's data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for UAEMIRCM_003",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/UAE/UAEMIRCM.003/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "MISR Peer-Reviewed Publications",
+                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
+                    "mediaType": "text/html",
+                    "title": "View this dataset's publications"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "TERRA Overview",
+                    "downloadURL": "https://terra.nasa.gov/about/terra-instruments/misr",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
+                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
+                    "mediaType": "text/html",
+                    "title": "View a micro article on this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
+                    "mediaType": "text/html",
+                    "title": "Visit this dataset's data center's home page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC webpage for MISR UAE Images",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/field_campaign_imagery/uae.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View a micro article on this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View a micro article on this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View a micro article on this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "MISR Science Data Product Guide - May 7, 2012",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's product usage"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "MISR Paths Tool - Direct File Download (.kml)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "Downloadable software applications"
+                }
+            ],
+            "identifier": "C1627523806-LARC",
+            "issued": "2019-07-31",
+            "landingPage": "https://doi.org/10.5067/TERRA/MISR/UAEMIRCM.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-08-02T06:35:51.404Z/2004-11-03T07:10:21.041Z",
+            "theme": [
+                "UAE_2004",
+                "geospatial"
+            ],
+            "title": "MISR radiometric camera-by-camera Cloud Mask subset for the UAE region V003"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -252219,15 +251846,15 @@
             "identifier": "C2808108845-LANCEMODIS",
             "issued": "2023-11-20",
             "keyword": [
-                "surface radiative properties",
                 "earth science",
-                "land surface"
+                "land surface",
+                "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VJ143IA2N.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -252237,7 +251864,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -252590,6 +252217,100 @@
             ],
             "title": "ROSETTA-ORBITER CAL RPCMIP 3 CR4B V1.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Weekly Polar-Gridded Brightness Temperature and Sea Surface Salinity V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/Aquarius/AQ3_TB.005.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "The data set consists of weekly gridded Level-3 products of Aquarius L-band radiometer brightness temperature (TB) observations and Sea Surface Salinity (SSS) retrievals from the Aquarius/Sat\u00e9lite de Aplicaciones Cient\u00edficas (SAC-D) mission, developed collaboratively between the U.S. National Aeronautics and Space Administration (NASA) and Argentina's space agency, Comisi\u00f3n Nacional de Actividades Espaciales (CONAE).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAquarius%2FAQ3_TB.005",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_TB+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2791494297-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_TB+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2791494297-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/Aquarius/AQ3_TB.005",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/Aquarius/AQ3_TB.005",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2791494297-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave",
+                "cryosphere",
+                "sea ice",
+                "oceans",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aquarius/AQ3_TB.005",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 50.0 180.0 87.4",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-04T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Weekly Polar-Gridded Brightness Temperature and Sea Surface Salinity V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -256756,14 +256477,14 @@
             "issued": "2024-12-01",
             "keyword": [
                 "earth science",
-                "sea surface topography",
-                "oceans"
+                "oceans",
+                "sea surface topography"
             ],
             "landingPage": "https://doi.org/10.5067/GMSLM-TJ152",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-14",
+            "modified": "2025-01-02",
             "programCode": [
                 "026:001"
             ],
@@ -256777,7 +256498,7 @@
             "release-place": "JPL",
             "series-name": "Global Mean Sea Level Trend from Integrated Multi-Mission Ocean Altimeters TOPEX/Poseidon Jason-1 and OSTM/Jason-2",
             "spatial": "-180.0 -66.0 180.0 66.0",
-            "temporal": "1992-09-01T00:00:00Z/2025-01-13T00:00:00Z",
+            "temporal": "1992-09-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NASA-SSH",
                 "MEaSUREs",
@@ -260291,18 +260012,18 @@
             "identifier": "C2023582667-LAADS",
             "issued": "2021-01-05",
             "keyword": [
-                "spectral/engineering",
                 "earth science",
-                "infrared wavelengths",
-                "visible wavelengths",
+                "atmosphere",
                 "clouds",
-                "atmosphere"
+                "spectral/engineering",
+                "infrared wavelengths",
+                "visible wavelengths"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/CLDPROP_D3_VIIRS_NOAA20.011",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -260312,7 +260033,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2018-03-17T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-03-17T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -270627,7 +270348,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-20",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -270636,7 +270357,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1992-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1992-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
@@ -278318,16 +278039,16 @@
             "identifier": "C1997866870-NSIDC_ECS",
             "issued": "2012-01-01",
             "keyword": [
-                "snow/ice",
-                "cryosphere",
                 "earth science",
-                "sea ice"
+                "cryosphere",
+                "sea ice",
+                "snow/ice"
             ],
             "landingPage": "https://doi.org/10.5067/JAQDJKPX0S60",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-28",
+            "modified": "2025-02-04",
             "programCode": [
                 "026:001"
             ],
@@ -278336,7 +278057,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2012-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2012-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -278447,7 +278168,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-02-02",
             "programCode": [
                 "026:001"
             ],
@@ -278456,7 +278177,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-08-29T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-08-29T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -293500,7 +293221,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -293510,7 +293231,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -316187,7 +315908,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-16",
+            "modified": "2025-01-24",
             "programCode": [
                 "026:001"
             ],
@@ -316196,7 +315917,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -318216,7 +317937,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -318226,7 +317947,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2017-02-03T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2017-02-03T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "Terra",
@@ -323625,7 +323346,7 @@
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "description": "This dataset contains Level 2 (L2) orthocorrected reflectance from the Airborne Visible / Infrared Imaging Spectrometer (AVIRIS-Classic) instrument. This is the NASA Earth Observing System Data and Information System (EOSDIS) facility instrument archive of these data. The NASA AVIRIS-Classic is a pushbroom spectral mapping system with high signal-to-noise ratio (SNR), designed and toleranced for high performance spectroscopy. AVIRIS-Classic measures reflected radiance in 224 contiguous bands at approximately 10-nm intervals in the Visible to Shortwave Infrared (VSWIR) spectral range from 400-2500 nm. The AVIRIS-Classic sensor has a 1 milliradian instantaneous field of view, providing altitude dependent ground sampling distances from 20 m to sub meter range. AVIRIS-Classic is flown on a variety of aircraft platforms including the Twin Otter, NASA's WB-57, and NASA's high altitude ER-2. For each flight line, two types of L2 data files may be included: (a) calibrated surface reflectance and (b) water vapor and optical absorption paths for liquid water and ice. The L2 data are provided in ENVI format, which includes a flat binary file accompanied by a header (.hdr) file holding metadata in text format. This archive currently includes data from 2008 - 2020. Additional AVIRIS-Classic facility instrument L2 data will be added as they become available. AVIRIS-Classic supports NASA Science and applications in many areas including plant composition and function, geology and soils, greenhouse gas mapping, and calibration of orbital platforms.",
+            "description": "This dataset contains Level 2 (L2) orthocorrected reflectance from the Airborne Visible / Infrared Imaging Spectrometer (AVIRIS-Classic) instrument. This is the NASA Earth Observing System Data and Information System (EOSDIS) facility instrument archive of these data. The NASA AVIRIS-Classic is a pushbroom spectral mapping system with high signal-to-noise ratio (SNR), designed and toleranced for high performance spectroscopy. AVIRIS-Classic measures reflected radiance in 224 contiguous bands at approximately 10-nm intervals in the Visible to Shortwave Infrared (VSWIR) spectral range from 400-2500 nm. The AVIRIS-Classic sensor has a 1 milliradian instantaneous field of view, providing altitude dependent ground sampling distances from 20 m to sub meter range. AVIRIS-Classic is flown on a variety of aircraft platforms including the Twin Otter, NASA's WB-57, and NASA's high altitude ER-2. For each flight line, two types of L2 data files may be included: (a) calibrated surface reflectance and (b) water vapor and optical absorption paths for liquid water and ice. The L2 data are provided in ENVI format, which includes a flat binary file accompanied by a header (.hdr) file holding metadata in text format. This archive currently includes data from 2008 - 2024. Additional AVIRIS-Classic facility instrument L2 data will be added as they become available. AVIRIS-Classic supports NASA Science and applications in many areas including plant composition and function, geology and soils, greenhouse gas mapping, and calibration of orbital platforms.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -323673,7 +323394,7 @@
             "graphic-preview-description": "RGB composite image from AVIRIS-Classic flight f060510t01p00r06 on May 10 2006 over Irvine, California. Source: f060510t01p00r06_sc01_RGB.jpeg.",
             "graphic-preview-file": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS-Classic_L2_Reflectance_Fig1.jpg",
             "identifier": "C2711871294-ORNL_CLOUD",
-            "issued": "2024-12-02",
+            "issued": "2025-01-28",
             "keyword": [
                 "earth science",
                 "atmosphere",
@@ -323685,7 +323406,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-03",
+            "modified": "2025-02-03",
             "programCode": [
                 "026:001"
             ],
@@ -323694,7 +323415,7 @@
                 "name": "ORNL_DAAC"
             },
             "spatial": "-171.84 18.57 -81.02 48.69",
-            "temporal": "2008-06-11T21:38:00Z/2020-10-13T23:03:00Z",
+            "temporal": "2008-06-11T00:00:00Z/2024-06-28T23:59:59Z",
             "theme": [
                 "AVIRIS",
                 "geospatial"
@@ -327516,14 +327237,14 @@
             "issued": "2021-07-27",
             "keyword": [
                 "earth science",
-                "ocean circulation",
-                "oceans"
+                "oceans",
+                "ocean circulation"
             ],
             "landingPage": "https://doi.org/10.5067/OSCAR-25N20",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-02",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -327537,7 +327258,7 @@
             "release-place": "CA, USA",
             "series-name": "Ocean Surface Current Analyses Real-time (OSCAR)",
             "spatial": "-180.0 -89.75 180.0 89.75",
-            "temporal": "2021-01-01T00:00:00Z/2025-01-06T00:00:00Z",
+            "temporal": "2021-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "OSCAR",
                 "geospatial"
@@ -328208,17 +327929,17 @@
             "identifier": "C1646609808-NSIDC_ECS",
             "issued": "2000-02-24",
             "keyword": [
+                "earth science",
                 "cryosphere",
                 "snow/ice",
-                "earth science",
-                "national geospatial data asset",
-                "ngda"
+                "ngda",
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MOD10C1.061",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-26",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -328227,7 +327948,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-24T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2000-02-24T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -328504,7 +328225,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -328514,7 +328235,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -329154,57 +328875,6 @@
             ],
             "title": "CASSINI RSS RAW DATA SET - ENGR2 V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "MISR Science Team (2018), Terra/MISR Level 3, Cloud Top Height-Optical Depth Product covering a month, version 1, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/TERRA/MISR/MIL3MCOD.001",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Roger Marchand",
-                "hasEmail": "mailto:rojmarch@u.washington.edu"
-            },
-            "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. This file contains the public MISR Level 3 Cloud Top Height-Optical Depth Product covering a month.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL3MCOD.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C1644916750-LARC",
-            "issued": "2018-08-06",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds"
-            ],
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL3MCOD.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2022-04-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-03-01T00:00:00Z/2022-05-03T00:00:00Z",
-            "theme": [
-                "MISR",
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Cloud Top Height-Optical Depth Product covering a month V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -330364,54 +330034,6 @@
             ],
             "title": "SURVEY OF COMET LIGHTCURVES V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Aerosol seasonal product in netCDF format;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Aerosol product in netCDF format covering a quarter (seasonal)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QAEN_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919894-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QAEN_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Aerosol seasonal product in netCDF format V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -331016,19 +330638,19 @@
             "identifier": "C3159617685-NSIDC_ECS",
             "issued": "2002-06-02",
             "keyword": [
-                "atmospheric winds",
-                "precipitation",
+                "earth science",
                 "atmosphere",
-                "ocean temperature",
+                "clouds",
+                "precipitation",
                 "oceans",
-                "earth science",
-                "clouds"
+                "ocean temperature",
+                "atmospheric winds"
             ],
             "landingPage": "https://doi.org/10.5067/1A3CSUWVLD7V",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-18",
+            "modified": "2025-01-25",
             "programCode": [
                 "026:001"
             ],
@@ -331037,7 +330659,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -89.24 180.0 89.24",
-            "temporal": "2002-06-02T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-06-02T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -335853,14 +335475,21 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS.",
+            "citation": "CDDIS VLBI TRF products, Greenbelt, MD, USA: NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/VLBI/vlbi_trf_products_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
-                "hasEmail": "mailto:support-cddis@earthdata.nasa.gov"
+                "hasEmail": "mailto:support-cddis@nasa.gov"
             },
             "description": "Terrestrial Reference Frame (TRF) product derived from the analysis of Very Long Baseline Interferometry (VLBI) data. The Terrestrial Reference Frame product includes station positions, velocities, and correlations. A minimum of three years of data are used in each solution. The TRF operational product is available quarterly at International VLBI Service for Geodesy and Astrometry (IVS) Data Centers.",
             "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVLBI%2Fvlbi_trf_products_001",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "CDDIS VLBI products",
@@ -335876,6 +335505,7 @@
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Dataset Landing Page",
                     "downloadURL": "https://doi.org/10.5067/VLBI/vlbi_trf_products_001",
                     "mediaType": "text/html",
                     "title": "This dataset's landing page"
@@ -335885,14 +335515,14 @@
             "issued": "2002-01-01",
             "keyword": [
                 "earth science",
-                "coordinate reference system",
-                "solid earth"
+                "solid earth",
+                "coordinate reference system"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2404809434-CDDIS.html",
+            "landingPage": "https://doi.org/10.5067/VLBI/vlbi_trf_products_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-05",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -335901,79 +335531,12 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-01-01T00:00:00Z/2024-12-09T00:00:00Z",
+            "temporal": "2002-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
             "title": "CDDIS VLBI products Terrestrial Reference Frame"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "VCST Team. 2024-01-22. VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ202GDC_NRT.002. https://doi.org/10.5067/VIIRS/VJ202GDC.002.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VINCENT Chiang",
-                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
-            },
-            "creator": "VCST Team",
-            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m product (VJ202GDC_NRT) contains unaggregated, calibrated TOA radiances for those VIIRS sub-pixel samples that are aggregated along-scan during post-calibration ground processing.  In other words, this file contains the calibrated M1 \u2013 M5, M7 and M13 dual gain band data from the nadir and near-nadir zones that would otherwise be discarded following post-calibration aggregation/Earth View Radiometric Calibration Unit.\r\n\r\nThe Level-1 and Level-2 swath products are generated from the processing of 6 minutes of VIIRS data acquired during theJPSS-2/NOAA-21 satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 &#181;m to 11.45 &#181;m. There are also 7 dual-gain VIIRS bands. The dual gain moderate resolution bands (M1 to M5, M7 and M13) have 6304 samples and the other moderate resolution bands have 3200.\r\n\r\nFor additional information, see the Operational Algorithm Description (OAD) Document for the L1B product at http://npp.gsfc.nasa.gov/sciencedocs/2015-08/474-00090_OAD-VIIRS-CAL-GEO-SDR_H.pdf. The document describes how VIIRS operates in space and provides the equations implemented by the L1B software to generate the MODIS Level-1 intermediate products. It is a summary document that presents the formulae and error budges used to transform VIIRS digital counts to radiance and reflectance.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202GDC_NRT.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Direct access to data from MODAPS public site.",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                }
-            ],
-            "identifier": "C2837615495-LANCEMODIS",
-            "issued": "2024-01-10",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "visible wavelengths"
-            ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202GDC_NRT.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-07",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "release-place": "MODAPS at NASA/GSFC",
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
-            "theme": [
-                "NOAA - SPACE WEATHER PROGRAM",
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m NRT"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -336605,7 +336168,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Glynn Hulley",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\nThe ECOSTRESS Swath Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m (ECO_L2_LSTE) Version 2 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO_L2_LSTE data product was derived using a physics-based Temperature and Emissivity Separation (TES) algorithm. The ECO_L2_LSTE is provided as swath data and has a spatial resolution of 70 meters (m). The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L2_LSTE data product.\nThe ECO_L2_LSTE Version 2 data product contains layers of LST, emissivity for bands 1 through 5, quality control for LST&E, LST error, emissivity error for bands 1 through 5, wideband emissivity, Precipitable Water Vapor (PWV), cloud mask, and water mask.\n\nImprovements/Changes from Previous Versions\n\n-\tAddition of cloud mask and water mask layers.\n\n-\tAddition of ECOSTRESS Gridded Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002 (ECO_L2G_LSTE.002 (https://doi.org/10.5067/ECOSTRESS/ECO_L2G_LSTE.002)) and ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002 (ECO_L2T_LSTE.002 (https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002)) data products.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\n-\tData alert: All users of ECOSTRESS L2 v002 products (ECO_L2T_LSTE, ECO_L2_LSTE, ECO_L2G_LSTE) should be aware that the cloud mask information previously available in the Quality Control (QC) layer in v001, is not available in the v002 QC layer. Instead, users should be using the \u2018cloud_mask\u2019 layer in the L2 LSTE product, or the cloud information in the standard cloud mask products (ECO_L2_CLOUD, ECO_L2T_CLOUD, ECO_L2G_CLOUD) to assess if a pixel is cle",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Swath Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m (ECO_L2_LSTE) Version 2 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO_L2_LSTE data product was derived using a physics-based Temperature and Emissivity Separation (TES) algorithm. The ECO_L2_LSTE is provided as swath data and has a spatial resolution of 70 meters (m). The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L2_LSTE data product.\n\nThe ECO_L2_LSTE Version 2 data product contains layers of LST, emissivity for bands 1 through 5, quality control for LST&E, LST error, emissivity error for bands 1 through 5, wideband emissivity, Precipitable Water Vapor (PWV), cloud mask, and water mask.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n* Data alert: All users of ECOSTRESS L2 v002 products (ECO_L2T_LSTE, ECO_L2_LSTE, ECO_L2G_LSTE) should be aware that the cloud mask information previously available in the Quality Control (QC) layer in v001, is not available in the v002 QC layer. Instead, users should be using the \u2018cloud_mask\u2019 layer in the L2 LSTE product, or the cloud information in the standard cloud mask products (ECO_L2_CLOUD, ECO_L2T_CLOUD, ECO_L2G_CLOUD) to assess if a pixel is clear or cloudy (see Section 3 of the User Guide). For v002, the information described by the mandatory QA flags in the QC bit mask can be found in Section 2.4 of the User Guide.\n\nImprovements/Changes from Previous Versions\n\n* Addition of cloud mask and water mask layers.\n* Addition of ECOSTRESS Gridded Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002 (ECO_L2G_LSTE.002 (https://doi.org/10.5067/ECOSTRESS/ECO_L2G_LST",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -336689,14 +336252,14 @@
             "issued": "2022-11-14",
             "keyword": [
                 "earth science",
-                "surface thermal properties",
-                "land surface"
+                "land surface",
+                "surface thermal properties"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2_LSTE.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-19",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -336706,7 +336269,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-12-23T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -344483,55 +344046,6 @@
             ],
             "title": "Measurements from the Gulf Of Maine during 2008 and 2009"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESH2OLS_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C191856312-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESH2OLS_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 H2O Limb Special Observation V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -345187,7 +344701,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-18",
+            "modified": "2024-12-25",
             "programCode": [
                 "026:001"
             ],
@@ -345196,7 +344710,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 55.0 180.0 90.0",
-            "temporal": "2010-09-15T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2010-09-15T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "MULTI_NASA",
                 "geospatial"
@@ -349565,57 +349079,6 @@
             ],
             "title": "MetOp-B ASCAT Level 2 25.0km Ocean Surface Wind Vectors in Full Orbit Swath"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Near Real Time Level 2 Cloud Motion Vector parameters;See ProductionDateTime for published Date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This is the MISR Level 2 Cloud Motion Vector Product containing height-resolved cloud motion vectors with associated data.  It is used for MISR Near Real Time processing, and is derived from session-based Level 0 input files.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI2TC_CMV_HDF_NRT_L2.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C1000000101-LARC",
-            "issued": "2015-04-01",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI2TC_CMV_HDF_NRT_L2.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2017-06-21",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2021-10-11T03:30:50.121Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "MISR Near Real Time (NRT) Level 2 Cloud Motion Vector parameters V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -350103,55 +349566,6 @@
             ],
             "title": "VG2 JUP PLS PLASMA DERIVED ION MOMENTS\n    96.0 SEC V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors including the mapping matrix to relate the reduced-size retrieval vectors, covariances, and averaging kernels back to the TES forward model pressure grid.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CO2LN_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C1000000260-LARC",
-            "issued": "2014-08-20",
-            "keyword": [
-                "atmosphere",
-                "air quality",
-                "earth science",
-                "atmospheric chemistry/carbon and hydrocarbon compounds"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CO2LN_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 Carbon Dioxide Lite Nadir V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -354603,16 +354017,16 @@
             "identifier": "C2623720879-POCLOUD",
             "issued": "2020-12-18",
             "keyword": [
-                "sea surface topography",
                 "earth science",
-                "ocean waves",
-                "oceans"
+                "oceans",
+                "sea surface topography",
+                "ocean waves"
             ],
             "landingPage": "https://doi.org/10.5067/S6AMW-2NTCUR-F08",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-03",
+            "modified": "2025-01-13",
             "programCode": [
                 "026:001"
             ],
@@ -354625,7 +354039,7 @@
             ],
             "release-place": "PO.DAAC",
             "spatial": "-180.0 -66.15 180.0 66.15",
-            "temporal": "2020-11-28T11:12:34.901Z/2025-01-27T00:00:00Z",
+            "temporal": "2020-11-28T11:12:34.901Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
@@ -372694,14 +372108,14 @@
             "issued": "2024-05-25",
             "keyword": [
                 "earth science",
-                "atmospheric radiation",
-                "atmosphere"
+                "atmosphere",
+                "atmospheric radiation"
             ],
             "landingPage": "https://doi.org/10.5067/PREFIRE-SAT2/PREFIRE/BUS-TLM_L0.R01",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -372713,7 +372127,7 @@
                 "https://doi.org/10.1175/BAMS-D-20-0155.1"
             ],
             "spatial": "-180.0 -84.0 180.0 84.0",
-            "temporal": "2024-05-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-05-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "PREFIRE",
                 "geospatial"
@@ -382679,7 +382093,7 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/SLR/SLR_MONTHLY_NPT_001.",
+            "citation": "International Laser Ranging Service (ILRS), SLR monthly normal point data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/SLR/slr_data_monthly_npt_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
@@ -382719,17 +382133,17 @@
             "identifier": "C1537476632-CDDIS",
             "issued": "1976-01-01",
             "keyword": [
-                "solid earth",
-                "tectonics",
                 "earth science",
+                "solid earth",
                 "geodetics",
-                "gravity/gravitational field"
+                "gravity/gravitational field",
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/SLR/SLR_MONTHLY_NPT_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-31",
+            "modified": "2025-02-28",
             "programCode": [
                 "026:001"
             ],
@@ -382738,7 +382152,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1982-01-01T00:00:00Z/2025-01-06T00:00:00Z",
+            "temporal": "1982-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
@@ -387255,7 +386669,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-11",
+            "modified": "2025-01-18",
             "programCode": [
                 "026:001"
             ],
@@ -387264,7 +386678,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1992-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1992-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
@@ -391500,7 +390914,7 @@
                 "hasEmail": "mailto:glynn.hulley@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Glynn Hulley",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO2LSTE Version 1 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO2LSTE data product was derived using a physics-based Temperature and Emissivity Separation (TES) algorithm. The ECO2LSTE is provided as swath data and has a spatial resolution of 70 meters (m).  The corresponding ECO1BGEO data product is required to georeference the ECO2LSTE data product. \r\n\r\nThe ECO2LSTE Version 1 data product contains layers of LST, emissivity for bands 1 through 5, quality control for LST&E, LST error, emissivity error for bands 1 through 5, wideband emissivity, and Precipitable Water Vapor (PWV). \r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website.\n\nThe ECO2LSTE Version 1 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO2LSTE data product was derived using a physics-based Temperature and Emissivity Separation (TES) algorithm. The ECO2LSTE is provided as swath data and has a spatial resolution of 70 meters (m). The corresponding ECO1BGEO data product is required to georeference the ECO2LSTE data product.\n\nThe ECO2LSTE Version 1 data product contains layers of LST, emissivity for bands 1 through 5, quality control for LST&E, LST error, emissivity error for bands 1 through 5, wideband emissivity, and Precipitable Water Vapor (PWV).\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -391563,14 +390977,14 @@
                     "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View information related to this dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -391588,7 +391002,7 @@
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
                     "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
@@ -391606,16 +391020,16 @@
             "identifier": "C1534729776-LPDAAC_ECS",
             "issued": "2019-06-20",
             "keyword": [
-                "surface thermal properties",
                 "earth science",
                 "land surface",
+                "surface thermal properties",
                 "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO2LSTE.001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-09-03",
+            "modified": "2025-01-06",
             "programCode": [
                 "026:001"
             ],
@@ -391626,7 +391040,7 @@
             "release-place": "Sioux Falls, South Dakota, USA",
             "series-name": "ECO2LSTE.001",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-09-09T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-01-06T23:59:09Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -391963,73 +391377,6 @@
             ],
             "title": "DSCOVR EPIC L2 Ozone (O3), Sulfur Dioxide (SO2) Aerosol Index (AI) with Epic L1B V03 Input, Version 2"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "VCST Team. 2024-01-22. VIIRS/JPSS2 Moderate Resolution 6-Min L1B Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ202MOD_NRT.002. https://doi.org/10.5067/VIIRS/VJ202MOD_NRT.002.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VINCENT Chiang",
-                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
-            },
-            "creator": "VCST Team",
-            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Moderate Resolution 6-Min L1B Swath 750m, short-name VJ202MOD_NRT is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21; referred to hereafter as J2) platform-derived NASA VIIRS L1B calibrated radiances product that comprises of sixteen moderate-resolution or M-bands with a spatial resolution of 750-meters at nadir. These M-bands comprise eleven reflective solar bands (RSB) and five thermal emissive bands (TEB). Each of the M-bands has 16 detectors in the along-track direction with 16 rows of pixels per scan that provide a 750-m resolution. Ranging in wavelengths from 0.402 \u00b5m to 12.49 \u00b5m, the M-bands are sensitive to visible, near-, shortwave-, mediumwave-, and longwave-infrared wavelengths. Derived from the NASA VIIRS L1A raw radiances, this product includes calibrated and geolocated radiance and reflectance data, quality flags, and granule- and collection-level metadata. In contrast to a MODIS L1B product, which temporally spans 5 minutes, the VIIRS L1B calibrated radiances product contains a nominal temporal duration of 6 minutes. The image dimensions of the 750-m swath product measure 3232 lines by 3200 pixels.\r\n\r\nThe J2 VIIRS radiometric calibration Level-1B reprocessing includes a few calibration updates for the reflective solar bands (RSB), but no significant changes for the day-night band (DNB) or thermal emissive bands (TEB).  For more information download VIIRS Level 1 Product User's Guide at: \r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/archive/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202MOD_NRT.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Direct access to data from MODAPS public site.",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                }
-            ],
-            "identifier": "C2837615938-LANCEMODIS",
-            "issued": "2024-01-10",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202MOD_NRT.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-07",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "release-place": "MODAPS at NASA/GSFC",
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
-            "theme": [
-                "NOAA - SPACE WEATHER PROGRAM",
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "VIIRS/JPSS2 Moderate Resolution 6-Min L1B Swath 750m NRT"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
@@ -408449,54 +407796,6 @@
             ],
             "title": "Sentinel-5P TROPOMI Radiance product band 8 (SWIR detector) L1B 5.5km x 7km V1 (S5P_L1B_RA_BD8_HiR) at GES DISC"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Cloud Product covering a day's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the public MISR Level 3 Component Global Cloud Product covering a day",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DCLD_L3.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C84942913-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DCLD_L3.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Cloud Product covering a day V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -408635,54 +407934,6 @@
             ],
             "title": "Dynamics and Chemistry of the Summer Stratosphere Airborne Data Products"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Land product in netCDF format covering a month's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Land product in netCDF format covering a month",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3MLSN_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C179031466-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3MLSN_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Land product in netCDF format covering a month V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -413365,55 +412616,6 @@
             ],
             "title": "West Africa Coastal Vulnerability Mapping: Deforestation, 2000-2012"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors including the mapping matrix to relate the reduced-size retrieval vectors, covariances, and averaging kernels back to the TES forward model pressure grid.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2FORLN_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C1000000362-LARC",
-            "issued": "2014-08-20",
-            "keyword": [
-                "atmospheric chemistry/carbon and hydrocarbon compounds",
-                "earth science",
-                "air quality",
-                "atmosphere"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2FORLN_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 Formic Acid Lite Nadir V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -419875,54 +419077,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0634 V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Cloud Fraction by Altitude Product for a day;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the public MISR Level 3 Cloud Fraction by Altitude Product covering a day",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DCFA_L3.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C188637668-LARC",
-            "issued": "2010-04-27",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DCFA_L3.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2017-10-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Cloud Fraction by Altitude Product covering a day V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -423829,16 +422983,16 @@
             "identifier": "C1449515322-NSIDC_ECS",
             "issued": "2016-12-01",
             "keyword": [
-                "sea ice",
-                "cryosphere",
                 "earth science",
+                "cryosphere",
+                "sea ice",
                 "snow/ice"
             ],
             "landingPage": "https://doi.org/10.5067/3KB2JPLFPK3R",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-28",
+            "modified": "2025-02-04",
             "programCode": [
                 "026:001"
             ],
@@ -423847,7 +423001,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2016-12-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2016-12-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -425919,17 +425073,17 @@
             "issued": "2022-05-30",
             "keyword": [
                 "earth science",
-                "salinity/density",
-                "ocean temperature",
                 "oceans",
+                "ocean chemistry",
                 "ocean optics",
-                "ocean chemistry"
+                "ocean temperature",
+                "salinity/density"
             ],
             "landingPage": "https://doi.org/10.5067/SeaBASS/PVST_VDIUP/DATA001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-10-31",
+            "modified": "2024-12-31",
             "programCode": [
                 "026:001"
             ],
@@ -425938,7 +425092,7 @@
                 "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2022-01-01T01:01:01Z/2024-12-23T00:00:00Z",
+            "temporal": "2022-01-01T01:01:01Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -428650,55 +427804,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P RPCMIP 3 PRL1 V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESHNO3S_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C191856320-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "atmospheric chemistry/nitrogen compounds",
-                "atmosphere",
-                "air quality",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESHNO3S_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 HNO3 Limb Special Observation V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -438159,7 +437264,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -438169,7 +437274,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -458590,17 +457695,17 @@
             "identifier": "C1646609745-NSIDC_ECS",
             "issued": "2002-07-04",
             "keyword": [
+                "earth science",
+                "cryosphere",
                 "snow/ice",
                 "ngda",
-                "national geospatial data asset",
-                "earth science",
-                "cryosphere"
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MYD10A1F.061",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-21",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -458609,7 +457714,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -461139,57 +460244,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0818 V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Near Real Time Level 1B2 terrain-projected Radiance parameters;See ProductionDateTime for published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains Terrain-projected TOA Radiance,resampled at the surface and topographically corrected, as well as geometrically corrected by PGE22.  It is used for MISR Near Real Time processing, and is derived from session-based Level 0 input files.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI1B2_TERRAIN_NRT_L1.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C1000000140-LARC",
-            "issued": "2015-04-01",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "visible wavelengths"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI1B2_TERRAIN_NRT_L1.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2017-06-21",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2021-10-11T03:27:20.409Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "MISR Near Real Time (NRT) Level 1B2 Terrain Data V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -474692,15 +473746,15 @@
             "identifier": "C2596864127-NSIDC_CPRD",
             "issued": "2018-10-14",
             "keyword": [
-                "topography",
                 "earth science",
-                "land surface"
+                "land surface",
+                "topography"
             ],
             "landingPage": "https://doi.org/10.5067/ATLAS/ATL03.006",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-10-08",
+            "modified": "2024-11-07",
             "programCode": [
                 "026:001"
             ],
@@ -474709,7 +473763,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2018-10-13T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-10-13T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -484044,19 +483098,19 @@
             "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
             "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-189,-99.16121842496285,151,102.16121842496285&l=SMAP_L2_Passive_Night_Soil_Moisture_Option3,SMAP_L2_Passive_Night_Soil_Moisture_Option2,SMAP_L2_Passive_Night_Soil_Moisture_Option1,SMAP_L2_Passive_Day_Soil_Moisture_Option3,SMAP_L2_Passive_Day_Soil_Moisture_Option2,SMAP_L2_Passive_Day_Soil_Moisture_Option1,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&lg=false&t=2015-03-31",
             "identifier": "C2312096175-NSIDC_ECS",
-            "issued": "2025-01-08",
+            "issued": "2025-01-09",
             "keyword": [
                 "earth science",
-                "soils",
                 "spectral/engineering",
                 "microwave",
-                "land surface"
+                "land surface",
+                "soils"
             ],
             "landingPage": "https://doi.org/10.5067/NCTT8THPWRTL",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-26",
+            "modified": "2025-02-02",
             "programCode": [
                 "026:001"
             ],
@@ -484065,7 +483119,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -85.044 180.0 85.044",
-            "temporal": "2025-01-08T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2025-01-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -484212,101 +483266,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0473 V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "Jones, C., T. Oliver, and Y. Lou. 2021. Pre-Delta-X: UAVSAR Georeferenced Channel Maps, Atchafalaya Basin, LA, USA, 2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1954",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@daac.ornl.gov"
-            },
-            "description": "This dataset provides spatial data on water channels in the estuary of the Atchafalaya Basin of the Mississippi River Delta of coastal Louisiana. These Level-3 (L3) channel maps were developed from interferograms derived from Uninhabited Aerial Vehicle Synthetic Aperture Radar (UAVSAR) data collected on 2016-10-16 and 2016-10-17 during low and high tides. The channel maps define open water paths in hydrodynamic models and are used to evaluate model performance.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1954",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "This link allows direct data access via Earthdata login",
-                    "downloadURL": "https://daac.ornl.gov/deltax/PreDeltaX_UAVSAR_Channel_Maps/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ORNL DAAC Data Set Documentation",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSAR_Channel_Maps.html",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Data set Landing Page DOI URL",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1954",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Pre-Delta-X: UAVSAR Georeferenced Channel Maps, Atchafalaya Basin, LA, USA, 2016: PreDeltaX_UAVSAR_Channel_Maps.pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/PreDeltaX_UAVSAR_Channel_Maps/comp/PreDeltaX_UAVSAR_Channel_Maps.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Water channels (blue) in the Atchafalaya Basin of the Mississippi River Delta of coastal Louisiana, U.S., during low tide on October 16, 2016. Source: PreDeltaX_channels_161016_lowtide_01.tif",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSAR_Channel_Maps_Fig1.jpg",
-                    "mediaType": "image/jpeg",
-                    "title": "Get a related visualization"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Delta-X Project Site",
-                    "downloadURL": "https://deltax.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                }
-            ],
-            "graphic-preview-description": "Water channels (blue) in the Atchafalaya Basin of the Mississippi River Delta of coastal Louisiana, U.S., during low tide on October 16, 2016. Source: PreDeltaX_channels_161016_lowtide_01.tif",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSAR_Channel_Maps_Fig1.jpg",
-            "identifier": "C2226539655-ORNL_CLOUD",
-            "issued": "2021-09-23",
-            "keyword": [
-                "biosphere",
-                "terrestrial hydrosphere",
-                "surface water",
-                "ecosystems",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1954",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2023-06-12",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "spatial": "-91.62 29.36 -91.06 29.76",
-            "temporal": "2016-10-16T14:08:00Z/2016-10-17T21:51:59Z",
-            "theme": [
-                "Delta-X",
-                "geospatial"
-            ],
-            "title": "Pre-Delta-X: UAVSAR Georeferenced Channel Maps, Atchafalaya Basin, LA, USA, 2016"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -501031,14 +499990,14 @@
             "keyword": [
                 "earth science",
                 "atmosphere",
-                "clouds",
-                "atmospheric radiation"
+                "atmospheric radiation",
+                "clouds"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_D3_VIIRS_SNPP.011",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-20",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -501048,7 +500007,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2012-03-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2012-03-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -526844,15 +525803,15 @@
             "identifier": "C2600305784-LAADS",
             "issued": "2023-01-10",
             "keyword": [
-                "aerosols",
+                "earth science",
                 "atmosphere",
-                "earth science"
+                "aerosols"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/AERDB_D3_VIIRS_NOAA20.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -526862,7 +525821,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2018-01-05T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-01-05T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -544514,7 +543473,7 @@
                 "hasEmail": "mailto:uso@asf.alaska.edu"
             },
             "creator": "OPERA",
-            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Coregistered Single-Look Complex (CSLC) from Sentinel-1 validated product consists of Single Look Complex (SLC) images which contain both amplitude and phase information of the complex radar return. The amplitude is primarily determined by ground surface properties (e.g., terrain slope, surface roughness, and physical properties), and phase primarily represents the distance between the radar and ground targets corrected for the geometrical distance between the two based on the knowledge from Digital Elevation Model and platform\u2019s position, i.e., the CSLC phase represents residual geometrical distance between the sensor and target, the atmospheric propagation delay and the target movements. The CSLC-S1 product is derived from Copernicus Sentinel-1A and Sentinel-1B Interferometric Wide (IW) SLC data, provided by the European Space Agency.  The CSLC images are precisely aligned or \u201ccoregistered\u201d to a pre-defined UTM/Polar stereographic map projection systems and posted at 5x10 m spacing in east and north direction, respectively.  Each CSLC-S1 product corresponds to a single S1 burst and is distributed as a Hierarchical Data Format version 5 (HDF5) file following the CF-1.8 convention containing both data raster layers (e.g., geocoded complex backscatter, low-resolution correction look-up tables) and product metadata. OPERA CSLC-S1 products are available over North America which includes the USA and U.S. Territories, Canada within 200 km of the U.S. border, and all mainland countries from the southern U.S. border down to and including Panama. Due to the S1 mission\u2019s narrow orbital tube, radar-geometry layers vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA CLSLC-S1 product, as they are produced only once or a limited number of times. The static layers are available in the associated OPERA Coregistered Single-Look Complex from Sentinel-1 Static Layers validated product (Version 1).",
+            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Coregistered Single-Look Complex (CSLC) from Sentinel-1 validated product consists of Single Look Complex (SLC) images which contain both amplitude and phase information of the complex radar return. The amplitude is primarily determined by ground surface properties (e.g., terrain slope, surface roughness, and physical properties), and phase primarily represents the distance between the radar and ground targets corrected for the geometrical distance between the two based on the knowledge from Digital Elevation Model and platform\u2019s position, i.e., the CSLC phase represents residual geometrical distance between the sensor and target, the atmospheric propagation delay and the target movements. The CSLC-S1 product is derived from Copernicus Sentinel-1A and Sentinel-1B Interferometric Wide (IW) SLC data.  \n\nThe CSLC images are precisely aligned or \u201ccoregistered\u201d to a pre-defined UTM/Polar stereographic map projection systems and posted at 5x10 m spacing in east and north direction, respectively.  Each CSLC-S1 product corresponds to a single S1 burst and is distributed as a Hierarchical Data Format version 5 (HDF5) file following the CF-1.8 convention containing both data raster layers (e.g., geocoded complex backscatter, low-resolution correction look-up tables) and product metadata. OPERA CSLC-S1 products are available over North America which includes the USA and U.S. Territories, Canada within 200 km of the U.S. border, and all mainland countries from the southern U.S. border down to and including Panama.  The OPERA CSLC-S1 product contains modified Copernicus Sentinel data (2016-2025).\n\nDue to the S1 mission\u2019s narrow orbital tube, radar-geometry layers vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA CLSLC-S1 product, as they are produced only once or a limited number of times. The static layers are available in the associated OPERA Coregistered Single-Look Complex from Sentinel-1 Static Layers validated product (Version 1).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -544557,21 +543516,21 @@
             "identifier": "C2777443834-ASF",
             "issued": "2016-07-01",
             "keyword": [
+                "earth science",
+                "cryosphere",
                 "glaciers/ice sheets",
-                "tectonics",
+                "land surface",
+                "geomorphic landforms/processes",
                 "solid earth",
+                "tectonics",
                 "oceans",
-                "coastal processes",
-                "cryosphere",
-                "earth science",
-                "geomorphic landforms/processes",
-                "land surface"
+                "coastal processes"
             ],
             "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_CSLC-S1_V1",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-06",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -544580,7 +543539,7 @@
                 "name": "ASF"
             },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>62.5015467 -139.0996574 69.6867168 -139.3803251 71.2183663 -157.141417 68.3735763 -167.228812 65.4323808 -168.8440651 60.338896 -173.9306256 52.6155773 -180.0 50.8611463 -180.0 51.6129878 -170.6297483 56.0163229 -152.9114355 59.267895 -149.1913018 58.8520427 -140.3770183 56.9878841 -136.2583689 51.3393627 -131.6506428 48.4661107 -125.7549673 40.3311808 -124.4241493 34.7676709 -121.9778478 22.4311968 -110.234396 14.4339613 -97.1649601 13.1145391 -90.922636 8.0382063 -84.6585484 6.4264529 -82.198433 4.9744342 -79.0975897 6.6985362 -76.3425468 15.9928118 -83.7301124 21.8738063 -87.1827257 19.4394223 -93.6858487 26.8405583 -96.431852 28.7047067 -92.0810441 28.6812513 -88.09344 28.4115341 -85.094922 28.8151876 -83.4597433 23.5415141 -81.7506224 25.1215118 -78.2162044 29.3000106 -79.6727284 31.2954845 -79.6466319 34.8887882 -75.0796609 40.946987 -69.3403609 43.3742252 -64.4225561 48.2959502 -65.1335857 48.9438707 -71.4417716 45.7238643 -79.6545994 50.6822691 -88.2638649 50.3596533 -90.7298952 51.3673723 -95.3439882 51.22781 -104.3228708 51.0180252 -121.4385551 61.4158182 -134.3936582 62.5015467 -139.0996574</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
-            "temporal": "2014-06-15T00:00:00Z/2025-01-13T00:00:00Z",
+            "temporal": "2014-06-15T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "SNWG/OPERA",
                 "geospatial"
@@ -556714,6 +555673,73 @@
             ],
             "title": "AMPR BRIGHTNESS TEMPERATURE CAMEX-1 V2"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "VIIRS Level 1 Processing Group. 2025-01-27. VIIRS/JPSS2 Raw Radiances in Counts 6-Min L1A Swath. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ201_NRT.021. https://doi.org/10.5067/VIIRS/VJ201_NRT.021.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "LANCEMODIS",
+                "hasEmail": "mailto:support@earthdata.nasa.gov"
+            },
+            "creator": "VIIRS Level 1 Processing Group",
+            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Raw Radiances in Counts 6-Min L1A Swath, short-name VJ201_NRT data product contains the unpacked, raw VIIRS science, calibration and engineering data; the extracted ephemeris and attitude data from the spacecraft diary packets; and the raw ADCS and bus-critical spacecraft telemetry data from those packets, with a few critical fields extracted.\n\nFor more information download VIIRS Level 1 Product User's Guide at:\nhttps://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document Archive/Science Data Product Documentation/Processing and Algorithm Version History/NASA_VIIRS_L1B_UG_August_2021.pdf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ201_NRT.021",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5201/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C3383725050-LANCEMODIS",
+            "issued": "2025-01-24",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ201_NRT.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2025-01-24T00:00:00Z/2025-02-03T00:00:00Z",
+            "theme": [
+                "NOAA - SPACE WEATHER PROGRAM",
+                "LANCE",
+                "geospatial"
+            ],
+            "title": "VIIRS/JPSS2 Raw Radiances in Counts 6-Min L1A Swath"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -580123,6 +579149,96 @@
             ],
             "title": "ASTEROID LIGHTCURVE DERIVED DATA V8.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Gridded 1-Degree Seasonal Soil Moisture Climatology V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/FUDM43XO9TDE.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This data set contains Level-3 gridded seasonal global soil moisture climatology estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFUDM43XO9TDE",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_SCSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782404746-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_SCSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782404746-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/FUDM43XO9TDE",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/FUDM43XO9TDE",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2782404746-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/FUDM43XO9TDE",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Gridded 1-Degree Seasonal Soil Moisture Climatology V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -590202,28 +589318,28 @@
             "identifier": "C1693440800-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
-                "ocean temperature",
+                "earth science",
+                "atmosphere",
                 "air quality",
                 "altitude",
-                "atmosphere",
                 "atmospheric chemistry",
                 "atmospheric pressure",
                 "atmospheric radiation",
                 "atmospheric temperature",
                 "atmospheric water vapor",
                 "clouds",
-                "earth science",
-                "land surface",
-                "oceans",
                 "precipitation",
+                "land surface",
                 "surface radiative properties",
-                "surface thermal properties"
+                "surface thermal properties",
+                "oceans",
+                "ocean temperature"
             ],
             "landingPage": "https://doi.org/10.5067/BZBSA32DWAPN",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-30",
+            "modified": "2024-12-16",
             "programCode": [
                 "026:001"
             ],
@@ -590242,7 +589358,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "SNDRAQIL3CDCCP",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2002-08-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -596925,57 +596041,6 @@
             ],
             "title": "Planetary Science Technology Program"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Near Real Time Level 1B2 ellipsoid-projected Radiance parameters;See ProductionDateTime for published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains Ellipsoid-projected TOA Radiance,resampled at the surface and topographically corrected, as well as geometrically corrected by PGE22.  It is used for MISR Near Real Time processing, and is derived from session-based Level 0 input files.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI1B2_ELLIPSOID_NRT_L1.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C1000000100-LARC",
-            "issued": "2015-04-01",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI1B2_ELLIPSOID_NRT_L1.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2017-06-21",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2021-10-11T03:27:20.409Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "MISR Near Real Time (NRT) Level 1B2 Ellipsoid Data V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -601413,7 +600478,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -601423,7 +600488,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -602113,11 +601178,11 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/VLBI/vlbi_data_aux_001.",
+            "citation": "CDDIS VLBI Auxiliary Files, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/VLBI/vlbi_data_aux_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
-                "hasEmail": "mailto:support-cddis@earthdata.nasa.gov"
+                "hasEmail": "mailto:support-cddis@nasa.gov"
             },
             "description": "Very Long Baseline Interferometry (VLBI) auxiliary ASCII files provided by the International VLBI Service for Geodesy and Astrometry (IVS) include schedules, notes, and session log files.",
             "distribution": [
@@ -602151,16 +601216,16 @@
             "identifier": "C2404928689-CDDIS",
             "issued": "2005-01-01",
             "keyword": [
+                "earth science",
                 "solid earth",
                 "coordinate reference system",
-                "earth science",
                 "gravity/gravitational field"
             ],
             "landingPage": "https://doi.org/10.5067/VLBI/vlbi_data_aux_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-05",
+            "modified": "2025-01-28",
             "programCode": [
                 "026:001"
             ],
@@ -602169,7 +601234,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2005-01-01T00:00:00Z/2024-12-09T00:00:00Z",
+            "temporal": "2005-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -606582,15 +605647,15 @@
             "identifier": "C1371883515-NSIDC_ECS",
             "issued": "1978-10-25",
             "keyword": [
-                "spectral/engineering",
                 "earth science",
+                "spectral/engineering",
                 "microwave"
             ],
             "landingPage": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/NSIDC-0630.001",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-24",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -606599,7 +605664,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1978-10-25T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1978-10-25T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -607848,22 +606913,22 @@
             "identifier": "C2560852594-GES_DISC",
             "issued": "2017-12-11",
             "keyword": [
+                "earth science",
                 "atmosphere",
                 "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric water vapor",
                 "land surface",
-                "oceans",
-                "earth science",
                 "surface thermal properties",
-                "atmospheric temperature",
-                "precipitation",
+                "oceans",
                 "ocean temperature",
-                "atmospheric water vapor"
+                "precipitation"
             ],
             "landingPage": "https://doi.org/10.5067/WEO3KIK1GBGT",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-02",
+            "modified": "2024-12-29",
             "programCode": [
                 "026:001"
             ],
@@ -607881,7 +606946,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "SNDRJ1ML2RMSSUP",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2017-12-01T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2017-12-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
@@ -621685,54 +620750,6 @@
             ],
             "title": "ISLSCP II Cloud and Meteorology Parameters"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESHDOL_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C191856315-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESHDOL_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 HDO Limb V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -644207,6 +643224,96 @@
             ],
             "title": "ROSETTA-LANDER MARS ROMAP 2 MARS SPM V1.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Gridded 1-Degree Weekly Soil Moisture V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/1VZM9975ARHP.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This data set contains Level-3 gridded weekly global soil moisture estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1VZM9975ARHP",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_WKSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782408424-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_WKSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782408424-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/1VZM9975ARHP",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/1VZM9975ARHP",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2782408424-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/1VZM9975ARHP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Gridded 1-Degree Weekly Soil Moisture V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -645108,7 +644215,7 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/SLR/SLR_MONTHLY_FR_001.",
+            "citation": "International Laser Ranging Service (ILRS), SLR monthly full-rate data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/SLR/slr_data_monthly_fr_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
@@ -645150,15 +644257,15 @@
             "keyword": [
                 "earth science",
                 "solid earth",
-                "tectonics",
                 "geodetics",
-                "gravity/gravitational field"
+                "gravity/gravitational field",
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/SLR/SLR_MONTHLY_FR_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-31",
+            "modified": "2025-02-28",
             "programCode": [
                 "026:001"
             ],
@@ -645167,7 +644274,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1976-01-01T00:00:00Z/2025-01-06T00:00:00Z",
+            "temporal": "1976-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
@@ -655508,7 +654615,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-27",
+            "modified": "2025-02-03",
             "programCode": [
                 "026:001"
             ],
@@ -655517,7 +654624,7 @@
                 "name": "ASF"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2015-02-12T16:02:58Z/2025-01-27T00:00:00Z",
+            "temporal": "2015-02-12T16:02:58Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -666205,28 +665312,28 @@
             "identifier": "C1701805657-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
-                "clouds",
+                "earth science",
+                "atmosphere",
                 "air quality",
                 "altitude",
-                "atmosphere",
                 "atmospheric chemistry",
                 "atmospheric pressure",
                 "atmospheric radiation",
                 "atmospheric temperature",
                 "atmospheric water vapor",
-                "earth science",
-                "land surface",
-                "oceans",
-                "ocean temperature",
+                "clouds",
                 "precipitation",
+                "land surface",
                 "surface radiative properties",
-                "surface thermal properties"
+                "surface thermal properties",
+                "oceans",
+                "ocean temperature"
             ],
             "landingPage": "https://doi.org/10.5067/ENI8HFAJE9CH",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-17",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -666241,7 +665348,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "AIRS3SPD",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-31T00:00:00Z/2025-01-20T00:00:00Z",
+            "temporal": "2002-08-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -668655,17 +667762,17 @@
             "identifier": "C1646610415-NSIDC_ECS",
             "issued": "2000-02-18",
             "keyword": [
-                "ngda",
-                "cryosphere",
                 "earth science",
+                "cryosphere",
                 "snow/ice",
+                "ngda",
                 "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MOD10A2.061",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-16",
+            "modified": "2025-01-24",
             "programCode": [
                 "026:001"
             ],
@@ -668674,7 +667781,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-18T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2000-02-18T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -699189,7 +698296,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-03",
+            "modified": "2025-01-13",
             "programCode": [
                 "026:001"
             ],
@@ -699202,7 +698309,7 @@
             ],
             "release-place": "PO.DAAC",
             "spatial": "-180.0 -66.15 180.0 66.15",
-            "temporal": "2020-11-30T14:26:00.843Z/2025-01-27T00:00:00Z",
+            "temporal": "2020-11-30T14:26:00.843Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
@@ -703726,54 +702833,6 @@
             ],
             "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Liver tissue"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Global Cloud public Product in netCDF format covering a year;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Global Cloud public Product in netCDF format covering a year",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3YCLDN_L3.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919911-LARC",
-            "issued": "2006-03-01",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3YCLDN_L3.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Global Cloud public Product in netCDF format covering a year V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -717981,7 +717040,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Glynn Hulley",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Swath Cloud Mask Instantaneous L2 Global 70 m (ECO_L2_CLOUD) Version 2 data product is derived using a single-channel Bayesian cloud threshold with a look-up-table (LUT) approach. The ECOSTRESS Level 2 cloud product provides a cloud mask that can be used to determine cloud cover for accurate land surface temperature and evapotranspiration estimation. The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L2_CLOUD data product.\n \nThe ECO_L2_CLOUD Version 2 data product contains two cloud mask layers: Brightness temperature LUT test and Final cloud mask. Information on how to interpret the bit fields in the cloud mask is provided in Table 7 of the User Guide.\n\nImprovements/Changes from Previous Versions\n\n-\tECO_L2_CLOUD Version 2 data product algorithm has been revamped to have a more rigorous single-channel Bayesian cloud threshold with a look-up-table (LUT). See Section 3.1 of the User Guide (https://lpdaac.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf).\n\n-\tAddition of brightness temperature LUT test and brightness temperature difference test data layers.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Swath Cloud Mask Instantaneous L2 Global 70 m (ECO_L2_CLOUD) Version 2 data product is derived using a single-channel Bayesian cloud threshold with a look-up-table (LUT) approach. The ECOSTRESS Level 2 cloud product provides a cloud mask that can be used to determine cloud cover for accurate land surface temperature and evapotranspiration estimation. The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L2_CLOUD data product.\n \nThe ECO_L2_CLOUD Version 2 data product contains two cloud mask layers: Brightness temperature LUT test and Final cloud mask. Information on how to interpret the bit fields in the cloud mask is provided in Table 7 of the User Guide.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\nImprovements/Changes from Previous Versions\n\n* ECO_L2_CLOUD Version 2 data product algorithm has been revamped to have a more rigorous single-channel Bayesian cloud threshold with a look-up-table (LUT). See Section 3.1 of the User Guide.\n* Addition of brightness temperature LUT test and brightness temperature difference test data layers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -718072,7 +717131,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-19",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -718082,7 +717141,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-12-23T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -721237,6 +720296,74 @@
             ],
             "title": "CAMEX-3 JPL SURFACE ACOUSTIC WAVE (SAW) HYGROMETER V1"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "VCST Team. 2025-01-27. VIIRS/JPSS2 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath IP 750m NRT. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ203MOD_NRT.021. https://doi.org/10.5067/VIIRS/VJ203MOD_NRT.021.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VINCENT Chiang",
+                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
+            },
+            "creator": "VCST Team",
+            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath, short-name VJ203MOD_NRT) is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-based NASA VIIRS L1 terrain-corrected geolocation product, and contains the derived line-of-sight (LOS) vectors for each of the 750-m moderate-resolution, or M-bands. The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform's ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry. It produces geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel. The VJ203MOD product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, and quality flag for every pixel location. VJ203MOD provides a fundamental input to derive a number of VIIRS M-band higher-level products.\r\n\r\n\r\nThe J2 VIIRS geolocation underwent an on-orbit validation. Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands. The Day-Night band (DNB) geolocation error of about 2000 m was corrected. Further, the geolocation biases in the scan profile were also corrected. All these corrections bring the geolocation uncertainties for the J2 L1 products to within 75 m (1-sigma) in both the along-scan and along-track directions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203MOD_NRT.021",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5201/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through MODAPS"
+                }
+            ],
+            "identifier": "C3383721151-LANCEMODIS",
+            "issued": "2025-01-25",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "sensor characteristics",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203MOD_NRT.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2025-01-27T00:00:00Z/2025-02-03T00:00:00Z",
+            "theme": [
+                "NOAA - SPACE WEATHER PROGRAM",
+                "LANCE",
+                "geospatial"
+            ],
+            "title": "VIIRS/JPSS2 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath IP 750m NRT"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -735047,55 +734174,6 @@
                     "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "Downloadable software applications"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "How to cite ASDC data",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's data citation policy"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc/misr_loc.html",
-                    "mediaType": "text/html",
-                    "title": "Use this dataset in a web based tool"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA EOS ATB Documents: MISR",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's algorithm theoretical basis document"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Level 1 Production Report",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
-                    "mediaType": "text/html",
-                    "title": "Use this dataset in a web based tool"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's data quality document"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Order and Customization Tool",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR/cgi-bin/MISR/main.cgi",
-                    "mediaType": "text/html",
-                    "title": "Use this dataset in a web based tool"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR project home page",
-                    "downloadURL": "https://misr.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "Overview of MISR Data at the ASDC, 2023",
@@ -735152,41 +734230,6 @@
                     "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's user's guide"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "TERRA Overview",
-                    "downloadURL": "https://terra.nasa.gov/about/terra-instruments/misr",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "DOI data set landing page for MIB2GEOP_003",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MIB2GEOP_L1.003",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Peer-Reviewed Publications",
-                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's publications"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "ASDC Direct Data Download for MIB2GEOP_003",
@@ -735194,68 +734237,12 @@
                     "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
-                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
-                    "mediaType": "text/html",
-                    "title": "View a micro article on this dataset"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "OPeNDAP data access for MIB2GEOP_003",
                     "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MIB2GEOP.003/contents.html",
                     "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Earthdata Search for MIB2GEOP_003",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2794387069-LARC",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Data and Information for MISR",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "mediaType": "text/html",
-                    "title": "Visit this dataset's data center's home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Science Data Product Guide - May 7, 2012",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's product usage"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Paths Tool - Direct File Download (.kml)",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "title": "Downloadable software applications"
                 }
             ],
             "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
@@ -735263,15 +734250,15 @@
             "identifier": "C2794387069-LARC",
             "issued": "2023-11-02",
             "keyword": [
-                "spectral/engineering",
                 "earth science",
+                "spectral/engineering",
                 "sensor characteristics"
             ],
             "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIB2GEOP_L1.003",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-10",
+            "modified": "2024-11-15",
             "programCode": [
                 "026:001"
             ],
@@ -735280,7 +734267,7 @@
                 "name": "NASA/LARC/SD/ASDC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1999-12-18T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
@@ -736860,7 +735847,7 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSCSNX_001.",
+            "citation": "International GNSS Service, GNSS Final Cumulative Station Positions/Velocities Product, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi: 10.5067/GNSS/gnss_igscsnx_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
@@ -736892,7 +735879,7 @@
                 {
                     "@type": "dcat:Distribution",
                     "description": "URL for more information about GNSS derived products",
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSCSNX_001",
+                    "downloadURL": "http://doi.org/10.5067/GNSS/GNSS_IGSCSNX_001",
                     "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
@@ -736900,17 +735887,17 @@
             "identifier": "C1605122460-CDDIS",
             "issued": "1992-01-01",
             "keyword": [
-                "tectonics",
+                "earth science",
                 "solid earth",
-                "gravity/gravitational field",
                 "geodetics",
-                "earth science"
+                "gravity/gravitational field",
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSCSNX_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-23",
+            "modified": "2025-01-18",
             "programCode": [
                 "026:001"
             ],
@@ -736919,7 +735906,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1992-01-01T00:00:00Z/2024-12-16T00:00:00Z",
+            "temporal": "1992-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
@@ -739886,18 +738873,18 @@
             "identifier": "C1942970257-LANCEMODIS",
             "issued": "2020-08-05",
             "keyword": [
-                "surface radiative properties",
-                "surface thermal properties",
+                "earth science",
+                "biosphere",
                 "ecological dynamics",
                 "land surface",
-                "earth science",
-                "biosphere"
+                "surface radiative properties",
+                "surface thermal properties"
             ],
             "landingPage": "https://doi.org/10.5067/FIRMS/VIIRS/VNP14IMGT_NRT.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-28",
+            "modified": "2025-02-04",
             "programCode": [
                 "026:001"
             ],
@@ -739911,7 +738898,7 @@
             ],
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2016-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2016-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "FIRMS",
                 "LANCE",
@@ -750761,54 +749748,6 @@
             ],
             "title": "ASTEROID POLARIMETRIC DATABASE V8.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Radiance Product for a quarter (seasonal);See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Radiance Product covering a quarter (seasonal)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QRD_L3.005",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677732-LARC",
-            "issued": "2003-12-03",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QRD_L3.005",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Radiance Product covering a quarter (seasonal) V005"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -755128,126 +754067,6 @@
             ],
             "title": "GIBS Web Map Tile Service (WMTS)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "2017-03-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.2. https://asdc.larc.nasa.gov/project/SAGE%20III-ISS.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dr. Flittner",
-                "hasEmail": "mailto:david.e.flittner@nasa.gov"
-            },
-            "description": "g3bt_52 is the Stratospheric Aerosol and Gas Experiment III (SAGE III) on the International Space Station (ISS) (SAGE III/ISS) Level 1B Lunar Event Species Profiles (HDF5) V052 data product. It contains pixel group transmission profiles for a single solar event. SAGE III was Launched on February 19, 2017 on a SpaceX Falcon 9 from Kennedy Space Center, SAGE III-ISS is the second instrument from the SAGE III project, externally mounted on the ISS. This ISS-based instrument uses a technique known as occultation, which involves looking at the light from the Sun or Moon as it passes through Earth's atmosphere at the edge, or limb, of the planet to provide long-term monitoring of ozone vertical profiles of the stratosphere and mesosphere. The data provided by SAGE III-ISS includes key components of atmospheric composition and their long-term variability, focusing on the study of aerosols, chlorine dioxide, clouds, nitrogen dioxide, nitrogen trioxide, pressure and temperature, and water vapor. SAGE data has historically been used by the World Meteorological Organization to inform their periodic assessments of ozone depletion. These new observations from the International Space Station will continue the SAGE team's contributions to ongoing scientific understanding of the Earth's atmosphere.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FSOLAR_HDF5_L1B-V5.2",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE project home page",
-                    "downloadURL": "https://sage.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Data Products User\u2019s Guide, April 2021",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG-G3B.docx",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's user's guide"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.tar)",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/sageiii_iss_readers.tar",
-                    "mediaType": "application/x-tar",
-                    "title": "Downloadable software applications"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "How to cite ASDC data",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's data citation policy"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "DOI data set landing page for g3bt_52",
-                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.2",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Version 5.2 Release Notes",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/Release_Notes_v5.2.docx",
-                    "mediaType": "text/html",
-                    "title": "View an important notice for this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Open Source Agreement for Computer Software",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's product history"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Earthdata Search for g3bt_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2066317194-LARC",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Direct Data Download for g3bt_52",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SAGE_III_ISS/g3bt.052/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Data and Information for SAGE III-ISS",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/SAGE%20III-ISS",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                }
-            ],
-            "identifier": "C2066317194-LARC",
-            "issued": "2018-08-22",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric radiation"
-            ],
-            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.2",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2019-06-19",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2017-06-07T00:00:00Z/2023-02-28T00:00:00Z",
-            "theme": [
-                "SAGE III-ISS",
-                "geospatial"
-            ],
-            "title": "SAGE III/ISS L1B Solar Event Transmission Data (HDF5) V052"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -760694,7 +759513,7 @@
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
-                "hasEmail": "mailto:support-cddis@earthdata.nasa.gov"
+                "hasEmail": "mailto:support-cddis@nasa.gov"
             },
             "description": "Very Long Baseline Interferometry (VLBI) binary files provided by the International VLBI Service for Geodesy and Astrometry (IVS) in vgosDB format.",
             "distribution": [
@@ -760728,15 +759547,15 @@
             "identifier": "C2404975699-CDDIS",
             "issued": "2005-01-01",
             "keyword": [
-                "coordinate reference system",
                 "earth science",
-                "solid earth"
+                "solid earth",
+                "coordinate reference system"
             ],
             "landingPage": "https://doi.org/10.5067/VLBI/vlbi_db_data_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-05",
+            "modified": "2025-01-28",
             "programCode": [
                 "026:001"
             ],
@@ -760745,7 +759564,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2005-01-01T00:00:00Z/2024-12-09T00:00:00Z",
+            "temporal": "2005-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -762253,54 +761072,6 @@
             ],
             "title": "VENUS CLIMATE ORBITER LIR CALIBRATED\n                                      DATA V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Aerosol product in netCDF format covering a day's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Aerosol product in netCDF format covering a day",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DAEN_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919891-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DAEN_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Aerosol product in netCDF format covering a day V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -770855,73 +769626,6 @@
             ],
             "title": "SnowEx20 Grand Mesa Intensive Observation Period Snow Pit Measurements V001"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "VIIRS Level 1 Processing Group. 2024-01-22. VIIRS/JPSS2 Raw Radiances in Counts 6-Min L1A Swath NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ201_NRT.002. https://doi.org/10.5067/VIIRS/VJ201_NRT.002.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "LANCEMODIS",
-                "hasEmail": "mailto:support@earthdata.nasa.gov"
-            },
-            "creator": "VIIRS Level 1 Processing Group",
-            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Raw Radiances in Counts 6-Min L1A Swath, short-name VJ201_NRT data product contains the unpacked, raw VIIRS science, calibration and engineering data; the extracted ephemeris and attitude data from the spacecraft diary packets; and the raw ADCS and bus-critical spacecraft telemetry data from those packets, with a few critical fields extracted.\r\n\r\nFor more information download VIIRS Level 1 Product User's Guide at:\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/archive/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ201_NRT.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Direct access to data from MODAPS public site.",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                }
-            ],
-            "identifier": "C2837614569-LANCEMODIS",
-            "issued": "2024-01-10",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "spectral/engineering",
-                "infrared wavelengths"
-            ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ201_NRT.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-07",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "release-place": "MODAPS at NASA/GSFC",
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
-            "theme": [
-                "NOAA - SPACE WEATHER PROGRAM",
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "VIIRS/JPSS2 Raw Radiances in Counts 6-Min L1A Swath NRT"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
@@ -784789,28 +783493,28 @@
             "identifier": "C1238517272-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry",
                 "earth science",
+                "atmosphere",
+                "altitude",
+                "atmospheric pressure",
                 "atmospheric temperature",
                 "atmospheric water vapor",
                 "clouds",
-                "atmosphere",
-                "altitude",
-                "air quality",
-                "ocean temperature",
-                "precipitation",
+                "land surface",
                 "surface radiative properties",
+                "oceans",
+                "ocean temperature",
                 "surface thermal properties",
-                "land surface",
-                "oceans"
+                "air quality",
+                "atmospheric radiation",
+                "atmospheric chemistry",
+                "precipitation"
             ],
             "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA306",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-17",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -784825,7 +783529,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "AIRS3SPD",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-31T00:00:00Z/2025-01-20T00:00:00Z",
+            "temporal": "2002-08-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -790309,15 +789013,15 @@
             "identifier": "C2752556504-NSIDC_CPRD",
             "issued": "2019-03-29",
             "keyword": [
-                "cryosphere",
                 "earth science",
+                "cryosphere",
                 "glaciers/ice sheets"
             ],
             "landingPage": "https://doi.org/10.5067/ATLAS/ATL11.006",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-08-29",
+            "modified": "2024-11-07",
             "programCode": [
                 "026:001"
             ],
@@ -790326,7 +789030,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2019-03-29T00:00:00Z/2024-11-04T00:00:00Z",
+            "temporal": "2019-03-29T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -795626,55 +794330,6 @@
             ],
             "title": "LBA-ECO LC-13 GIS Coverages of Logged Areas, Tapajos Forest, Para, Brazil: 1996, 1998"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team; processed/stored at the Langley DAAC; MISR L1B3 Radiometric Camera-by-camera Cloud Mask Product subset for the RICO region; See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Diner",
-                "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
-            },
-            "description": "This file contains the Radiometric camera-by-camera Cloud Mask dataset over the RICO region. It is used to determine whether a scene is classified as clear or cloudy. A new parameter has been added to indicate dust over ocean. This version of the ESDT is used by MISR PGE 13.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FRICMIRCM_L1B3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C1411142650-LARC",
-            "issued": "2017-08-07",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/RICMIRCM_L1B3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2022-04-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-11-01T14:36:42Z/2005-01-31T15:19:32Z",
-            "theme": [
-                "RICO_2004",
-                "geospatial"
-            ],
-            "title": "MISR L1B3 Radiometric Camera-by-camera Cloud Mask Product subset for the RICO region V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -798304,7 +796959,7 @@
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
-                "hasEmail": "mailto:support-cddis@earthdata.nasa.gov"
+                "hasEmail": "mailto:support-cddis@nasa.gov"
             },
             "description": "Very Long Baseline Interferometry (VLBI) ASCII files in the NGS card format. Very Long Baseline Interferometry (VLBI) auxiliary ASCII files provided by the International VLBI Service for Geodesy and Astrometry (IVS) include schedules, notes, and session log files.",
             "distribution": [
@@ -798338,15 +796993,15 @@
             "identifier": "C2404965297-CDDIS",
             "issued": "2005-01-01",
             "keyword": [
+                "earth science",
                 "solid earth",
-                "coordinate reference system",
-                "earth science"
+                "coordinate reference system"
             ],
             "landingPage": "https://doi.org/10.5067/VLBI/vlbi_ngs_data_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-05",
+            "modified": "2025-01-28",
             "programCode": [
                 "026:001"
             ],
@@ -798355,7 +797010,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2005-01-01T00:00:00Z/2024-12-09T00:00:00Z",
+            "temporal": "2005-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -805343,7 +803998,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -805353,7 +804008,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -816198,7 +814853,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-10",
+            "modified": "2024-11-14",
             "programCode": [
                 "026:001"
             ],
@@ -816207,7 +814862,7 @@
                 "name": "NASA/LARC/SD/ASDC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1999-12-18T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
@@ -818605,6 +817260,96 @@
             },
             "title": "Thermal-Inertial UAV Night Dataset"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Gridded 1-Degree Monthly Soil Moisture Climatology V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/O19KHW22C685.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This data set contains Level-3 gridded monthly global soil moisture climatology estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FO19KHW22C685",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_MCSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782399097-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_MCSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782399097-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/O19KHW22C685",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/O19KHW22C685",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2782399097-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/O19KHW22C685",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Gridded 1-Degree Monthly Soil Moisture Climatology V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -822440,73 +821185,6 @@
             ],
             "title": "COMEX: AVIRIS-Classic Facility Instrument Associated Flights and Information, 2014"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "VCST Team. 2024-01-22. VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ202IMG_NRT.002. https://doi.org/10.5067/VIIRS/VJ202IMG_NRT.002.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VINCENT Chiang",
-                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
-            },
-            "creator": "VCST Team",
-            "description": "The VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375m Near Real Time (NRT), short-name VJ202IMG_NRT is platform-derived NASA VIIRS L1B calibrated radiances product that comprises five image-resolution or I-bands, which have a 375-meter resolution at nadir. These I-bands comprise three reflective solar bands (RSB) and two thermal emissive bands (TEB). Each of the I-bands has 32 detectors in the along-track direction with 32 rows of pixels per scan that offer a resolution that is twice finer than that of the moderate (M) and Day-Night bands (DNB). Ranging in wavelengths from 0.6 \u00b5m to 12.4 \u00b5m, the I-bands are sensitive to visible/reflective, near-, shortwave-, mediumwave-, and longwave-infrared wavelengths. Derived from the NASA VIIRS L1A raw radiances, this product includes calibrated and geolocated radiance and reflectance data, quality flags, and granule- and collection-level metadata. In contrast to a MODIS L1B product, which temporally spans 5 minutes, the VIIRS L1B calibrated radiances product contains a nominal temporal duration of 6 minutes. The image dimensions of the 375-m swath product measure 6464 lines by 6400 pixels.\r\n\r\nThe J2 VIIRS radiometric calibration Level-1B reprocessing includes a few calibration updates for the reflective solar bands (RSB), but no significant changes for the day-night band (DNB) or thermal emissive bands (TEB).  For more information download VIIRS Level 1 Product User's Guide at: \r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/archive/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202IMG_NRT.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Direct access to data from MODAPS public site.",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                }
-            ],
-            "identifier": "C2837615614-LANCEMODIS",
-            "issued": "2024-01-10",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "visible wavelengths",
-                "spectral/engineering"
-            ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202IMG_NRT.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-07",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "release-place": "MODAPS at NASA/GSFC",
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
-            "theme": [
-                "NOAA - SPACE WEATHER PROGRAM",
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375m NRT"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -822895,18 +821573,18 @@
             "identifier": "C2947062938-LAADS",
             "issued": "2024-02-14",
             "keyword": [
+                "earth science",
                 "atmosphere",
                 "atmospheric radiation",
-                "ngda",
                 "clouds",
-                "earth science",
+                "ngda",
                 "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_D3_MODIS_Aqua.011",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-20",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -822916,7 +821594,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -824562,18 +823240,18 @@
             "identifier": "C3264430167-LANCEMODIS",
             "issued": "2024-10-01",
             "keyword": [
-                "surface thermal properties",
-                "biosphere",
                 "earth science",
+                "biosphere",
                 "ecological dynamics",
                 "land surface",
-                "surface radiative properties"
+                "surface radiative properties",
+                "surface thermal properties"
             ],
             "landingPage": "https://doi.org/10.5067/FIRMS/VIIRS/VJ114IMGT_NRT.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-28",
+            "modified": "2025-02-04",
             "programCode": [
                 "026:001"
             ],
@@ -824587,7 +823265,7 @@
             ],
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2024-10-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-10-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "FIRMS",
                 "LANCE",
@@ -825918,7 +824596,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -825928,7 +824606,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -828332,16 +827010,16 @@
             "identifier": "C2619443979-POCLOUD",
             "issued": "2020-12-17",
             "keyword": [
-                "oceans",
-                "ocean waves",
                 "earth science",
-                "sea surface topography"
+                "oceans",
+                "sea surface topography",
+                "ocean waves"
             ],
             "landingPage": "https://doi.org/10.5067/S6AP4-2HSNUR-F08",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-03",
+            "modified": "2025-01-10",
             "programCode": [
                 "026:001"
             ],
@@ -828354,7 +827032,7 @@
             ],
             "release-place": "PO.DAAC",
             "spatial": "-180.0 -66.15 180.0 66.15",
-            "temporal": "2020-11-30T14:26:00.875Z/2025-01-27T00:00:00Z",
+            "temporal": "2020-11-30T14:26:00.875Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
@@ -846788,7 +845466,7 @@
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "description": "This dataset provides Level 2 Solar-Induced Fluorescence (SIF) of Chlorophyll estimates derived from the Global Ozone Monitoring Experiment (GOME) instrument on the European Space Agency's (ESA's) European Remote-Sensing 2 (ERS-2) satellite. Each file contains daily raw and bias-adjusted solar-induced fluorescence on an orbital basis (land pixels only), at a resolution of 40 km x 320 km, along with quality control information and ancillary data. Data is provided for the period from 19950701 to 20030622. The GOME SIF product is inherently noisy due to low signal levels and has undergone only a limited amount of validation.",
+            "description": "This dataset provides Level 2 Solar-Induced Fluorescence (SIF) of Chlorophyll estimates derived from the Global Ozone Monitoring Experiment (GOME) instrument on the European Space Agency's (ESA's) European Remote-Sensing 2 (ERS-2) satellite. Each file contains daily raw and bias-adjusted solar-induced fluorescence on an orbital basis (land pixels only), at a resolution of 40 km x 320 km, along with quality control information and ancillary data. Data is provided for the period from 1995-07-01 to 2003-06-22. The GOME SIF product is inherently noisy due to low signal levels and has undergone only a limited amount of validation. This dataset includes both Version 1 and Version 2 files.  Version 2 includes new fields such as SIF uncertainties, longitude-latitude corners, and data coverage over ocean. In addition, the SIF bias adjustment differs between Versions 1 and 2. The data are provided in NetCDF format.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -846800,16 +845478,23 @@
                 {
                     "@type": "dcat:Distribution",
                     "description": "This link allows direct data access via Earthdata login",
-                    "downloadURL": "https://daac.ornl.gov/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/data/",
                     "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/ERS2_GOME_SIF_1758.zip",
+                    "mediaType": "application/zip",
+                    "title": "Download this dataset"
+                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "ORNL DAAC Data Set Documentation",
                     "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF.html",
                     "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
+                    "title": "View this dataset's user's guide"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -846825,6 +845510,13 @@
                     "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/ERS2_GOME_SIF_1758.zip",
+                    "mediaType": "application/zip",
+                    "title": "View documentation related to this dataset"
+                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003: ERS2_GOME_SIF.pdf",
@@ -846834,16 +845526,16 @@
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003: README_ERSGOME-F_v28.pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/comp/README_ERSGOME-F_v28.pdf",
+                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from ERS-2 GOME, 1995-2003: ERS2_GOME_SIF.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/ERS2_GOME_SIF/comp/ERS2_GOME_SIF.pdf",
                     "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "description": "Figure 1: Solar-Induced Fluorescence derived along ERS2 GOME orbital tracks on 1 July 1995.",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF_Fig1.png",
-                    "mediaType": "image/png",
+                    "description": "Figure 1: Solar-induced fluorescence (SIF) derived along ERS2 GOME orbital tracks on 1 June 1998.",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
@@ -846861,23 +845553,23 @@
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "graphic-preview-description": "Figure 1: Solar-Induced Fluorescence derived along ERS2 GOME orbital tracks on 1 July 1995.",
-            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF_Fig1.png",
+            "graphic-preview-description": "Figure 1: Solar-induced fluorescence (SIF) derived along ERS2 GOME orbital tracks on 1 June 1998.",
+            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/ERS2_GOME_SIF_Fig1.jpg",
             "identifier": "C2207946101-ORNL_CLOUD",
-            "issued": "2022-01-09",
+            "issued": "2025-01-28",
             "keyword": [
-                "surface radiative properties",
-                "biosphere",
                 "earth science",
+                "biosphere",
                 "ecological dynamics",
                 "vegetation",
-                "land surface"
+                "land surface",
+                "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/1758",
             "language": [
                 "en-US"
             ],
-            "modified": "2023-07-17",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -846885,7 +845577,7 @@
                 "@type": "org:Organization",
                 "name": "ORNL_DAAC"
             },
-            "spatial": "-180.0 -90.0 180.0 90.0",
+            "spatial": "-180.0 -84.37 180.0 85.42",
             "temporal": "1995-07-01T00:00:00Z/2003-06-22T23:59:59Z",
             "theme": [
                 "SIF-ESDR",
@@ -853136,55 +851828,6 @@
             ],
             "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 INCID OVER FLX SCI V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors including the mapping matrix to relate the reduced-size retrieval vectors, covariances, and averaging kernels back to the TES forward model pressure grid.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESCH4LN_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C1000000320-LARC",
-            "issued": "2014-08-20",
-            "keyword": [
-                "atmosphere",
-                "air quality",
-                "earth science",
-                "atmospheric chemistry/carbon and hydrocarbon compounds"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESCH4LN_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 Methane Lite Nadir V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -854219,7 +852862,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-19",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -854228,7 +852871,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -60.0 180.0 60.0",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2015-03-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -854811,7 +853454,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO1BMAPRAD Version 1 data product combines the at-sensor calibrated radiance values retrieved for the ECO1BRAD (https://doi.org/10.5067/ECOSTRESS/ECO1BRAD.001) data product and the geolocation information provided in the ECO1BGEO (https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001) data product to produce a geotagged, resampled radiance product.  The ECO1BMAPRAD data product is produced as a map registered product that is in a rotated geographic projection with a spatial resolution of 70 m. The ECO1BMAPRAD data product accounts for the overlap and variable pixel size in the ECO1BRAD data product.\r\n\r\nThe ECO1BMAPRAD Version 1 data product contains data layers including the radiance values for the five thermal infrared (TIR) bands, digital number (DN) values for the shortwave infrared (SWIR) band, associated data quality indicators, latitude and longitude values, solar and view geometry information, and surface height.\r\n\r\nThe ECO1BMAPRAD Version 1 data product contains data layers including the radiance values for the five thermal infrared (TIR) bands, digital number (DN) values for the shortwave infrared (SWIR) band, associated data quality indicators, latitude and longitude values, solar and view geometry information, and surface height.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Resampled data: The data has been resampled, so users interested in working with data closest to that acquired by the instrument may want to work with the swath products. \r\n*Missing scan data: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see section 3.3.2 of the User Guide.\r\n*Cold bias: ECOSTRESS Level-1 Radiance data shows high correlation with in-situ ground measurements (R2 = 0.99 in all bands). Currently, ECOSTRESS has a cold bias of approximately 0.7 Kelvin (K), which will be corrected through calibration in future data releases.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmwar",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECO1BMAPRAD Version 1 data product combines the at-sensor calibrated radiance values retrieved for the ECO1BRAD data product and the geolocation information provided in the ECO1BGEO data product to produce a geotagged, resampled radiance product. The ECO1BMAPRAD data product is produced as a map registered product that is in a rotated geographic projection with a spatial resolution of 70 meters (m). The ECO1BMAPRAD data product accounts for the overlap and variable pixel size in the ECO1BRAD data product.\n\nThe ECO1BMAPRAD Version 1 data product contains data variables including the radiance values for the five thermal infrared (TIR) bands, digital number (DN) values for the shortwave infrared (SWIR) band, associated data quality indicators, latitude and longitude values, solar and view geometry information, and surface height.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Resampled data: The data has been resampled, so users interested in working with data closest to that acquired by the instrument may want to work with the swath products. \n* Missing scan data: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see Section 3.3.2 of the User Guide.\n* Cold bias: ECOSTRESS Level-1 Radiance data shows high correlation with in-situ ground measurements (R2 = 0.99 in all bands). Currently, ECOSTRESS has a cold bias of approximately 0.7 Kelvin (K), which will be corrected through calibration in future data releases.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -854881,21 +853524,21 @@
                     "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View information related to this dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -854913,7 +853556,7 @@
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
                     "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
@@ -854932,14 +853575,14 @@
             "issued": "2019-03-27",
             "keyword": [
                 "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
+                "spectral/engineering",
+                "infrared wavelengths"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO1BMAPRAD.001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-08-26",
+            "modified": "2025-01-06",
             "programCode": [
                 "026:001"
             ],
@@ -854950,7 +853593,7 @@
             "release-place": "Sioux Falls, South Dakota, USA",
             "series-name": "ECO1BMAPRAD.001",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-09-02T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-01-06T23:59:09Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -855529,7 +854172,7 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_NPT_001.",
+            "citation": "International Laser Ranging Service (ILRS), SLR monthly normal point data summary, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/SLR/slr_data_monthlysum_npt_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
@@ -855561,7 +854204,7 @@
                 {
                     "@type": "dcat:Distribution",
                     "description": "URL for more information about SLR data",
-                    "downloadURL": "http://dx.doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_NPT_001",
+                    "downloadURL": "https://doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_NPT_001",
                     "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
@@ -855571,15 +854214,15 @@
             "keyword": [
                 "earth science",
                 "solid earth",
-                "tectonics",
+                "geodetics",
                 "gravity/gravitational field",
-                "geodetics"
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/SLR/SLR_DATA_MONTHLYSUM_NPT_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-31",
+            "modified": "2025-02-28",
             "programCode": [
                 "026:001"
             ],
@@ -855588,7 +854231,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1982-01-01T00:00:00Z/2025-01-06T00:00:00Z",
+            "temporal": "1982-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
@@ -856437,7 +855080,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -856447,7 +855090,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -872357,27 +871000,27 @@
             "identifier": "C1701805652-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
-                "atmospheric pressure",
-                "air quality",
-                "surface thermal properties",
-                "surface radiative properties",
-                "ocean temperature",
-                "oceans",
-                "land surface",
                 "earth science",
+                "atmosphere",
+                "air quality",
                 "altitude",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
+                "atmospheric chemistry",
+                "atmospheric pressure",
                 "atmospheric radiation",
-                "atmosphere",
-                "atmospheric chemistry"
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
+                "land surface",
+                "surface radiative properties",
+                "surface thermal properties",
+                "oceans",
+                "ocean temperature"
             ],
             "landingPage": "https://doi.org/10.5067/UO3Q64CTTS1U",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-17",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -872392,7 +871035,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "AIRS3STD",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-31T00:00:00Z/2025-01-20T00:00:00Z",
+            "temporal": "2002-08-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -872723,54 +871366,6 @@
             ],
             "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the KONza Validation EXperiment (KONVEX)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Aerosol Product covering a year's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Aerosol Product covering a year",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YAE_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677733-LARC",
-            "issued": "2003-12-03",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YAE_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Aerosol Product covering a year V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -879024,7 +877619,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-27",
+            "modified": "2025-02-03",
             "programCode": [
                 "026:001"
             ],
@@ -879033,7 +877628,7 @@
                 "name": "ASF"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2015-02-12T16:02:58Z/2025-01-27T00:00:00Z",
+            "temporal": "2015-02-12T16:02:58Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -883796,7 +882391,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -883806,7 +882401,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -896749,6 +895344,98 @@
             ],
             "title": "MESSENGER V/H RADIO SCIENCE SUBSYSTEM 1 EDR V1.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L2 Swath Single Orbit Soil Moisture V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/GB6FZ0UPCOGP.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This data set contains Level-2 global soil moisture estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGB6FZ0UPCOGP",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ2_SM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2770316046-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ2_SM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2770316046-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/GB6FZ0UPCOGP",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/GB6FZ0UPCOGP",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2770316046-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave",
+                "agriculture",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/GB6FZ0UPCOGP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L2 Swath Single Orbit Soil Moisture V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -900998,73 +899685,6 @@
             ],
             "title": "NOAA-07 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "VCST Team. 2024-01-22. VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.002. https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.002.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VINCENT Chiang",
-                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
-            },
-            "creator": "VCST Team",
-            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m, short-name VJ203DNB_NRT is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-based NASA VIIRS L1 terrain-corrected geolocation product, and contains the derived line-of-sight (LOS) vectors for the single panchromatic Day-Night band (DNB). The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform's ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry. It provides geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel. The VJ203DNB product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, lunar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, moon illumination fraction and phase angle, and quality flag for every pixel location.\r\n\r\n\r\nThe J2 VIIRS geolocation underwent an on-orbit validation. Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands. The Day-Night band (DNB) geolocation error of about 2000 m was corrected. Further, the geolocation biases in the scan profile were also corrected. All these corrections bring the geolocation uncertainties for the J2 L1 products to within 75 m (1-sigma) in both the along-scan and along-track directions.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203DNB_NRT.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Direct access to data from MODAPS public site.",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                }
-            ],
-            "identifier": "C2837614124-LANCEMODIS",
-            "issued": "2024-01-10",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
-                "visible wavelengths"
-            ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-07",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "release-place": "MODAPS at NASA/GSFC",
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
-            "theme": [
-                "NOAA - SPACE WEATHER PROGRAM",
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -903240,54 +901860,6 @@
             ],
             "title": "ROSETTA-ORBITER CHECK MIRO 2 CVP COMMISSIONING V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESATMTL_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C191856297-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESATMTL_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 Atmospheric Temperatures Limb V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -909878,7 +908450,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Gregory Halverson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Tiled Downscaled Meteorology Instantaneous L3 Global 70 m (ECO_L3T_MET) Version 2 data product provides instantaneous near-surface air temperature (Ta) and relative humidity (RH) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and Ta or RH from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. The downscaled meteorology estimates are recorded into the ECO_L3T_MET data product and tiled using a modified version of the Military Grid Reference System (MGRS (https://hls.gsfc.nasa.gov/products-description/tiling-system/)) which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 m spatial resolution.\n\nThe ECO_L3T_MET Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format with each data layer distributed as a separate COG. This product contains four layers including Ta, RH, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Tiled Downscaled Meteorology Instantaneous L3 Global 70 m (ECO_L3T_MET) Version 2 data product provides instantaneous near-surface air temperature (Ta) and relative humidity (RH) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and Ta or RH from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. The downscaled meteorology estimates are recorded into the ECO_L3T_MET data product and tiled using a modified version of the Military Grid Reference System (MGRS) (https://hls.gsfc.nasa.gov/products-description/tiling-system/) which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 m spatial resolution.\n\nThe ECO_L3T_MET Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format with each data layer distributed as a separate COG. This product contains four layers including Ta, RH, cloud mask, and water mask.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -909942,16 +908514,16 @@
             "identifier": "C2074877891-LPCLOUD",
             "issued": "2024-05-01",
             "keyword": [
-                "atmospheric temperature",
                 "earth science",
-                "atmospheric water vapor",
-                "atmosphere"
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L3T_MET.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -909961,7 +908533,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -912642,15 +911214,15 @@
             "identifier": "C2807625522-LANCEMODIS",
             "issued": "2023-11-20",
             "keyword": [
+                "earth science",
                 "land surface",
-                "surface radiative properties",
-                "earth science"
+                "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA3N.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -912660,7 +911232,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "LANCE",
                 "Suomi-NPP",
@@ -913671,7 +912243,7 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/SLR/SLR_HOURLY_NPT_001.",
+            "citation": "International Laser Ranging Service (ILRS), SLR hourly normal point data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/SLR/slr_data_hourly_npt_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
@@ -913711,17 +912283,17 @@
             "identifier": "C1537476919-CDDIS",
             "issued": "1976-01-01",
             "keyword": [
+                "earth science",
                 "solid earth",
                 "geodetics",
                 "gravity/gravitational field",
-                "tectonics",
-                "earth science"
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/SLR/SLR_HOURLY_NPT_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-15",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -913730,7 +912302,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2010-01-01T00:00:00Z/2024-11-18T00:00:00Z",
+            "temporal": "2010-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
@@ -919057,17 +917629,17 @@
             "identifier": "C1646610417-NSIDC_ECS",
             "issued": "2000-02-24",
             "keyword": [
-                "ngda",
-                "national geospatial data asset",
                 "earth science",
+                "cryosphere",
                 "snow/ice",
-                "cryosphere"
+                "ngda",
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MOD10A1.061",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-26",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -919076,7 +917648,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-24T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2000-02-24T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -931279,7 +929851,7 @@
             "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
             "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-188,-85,183,86&l=SMAP_L1_Passive_Faraday_Rotation_Fore,SMAP_L1_Passive_Faraday_Rotation_Aft,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
             "identifier": "C2257958430-NSIDC_ECS",
-            "issued": "2025-01-08",
+            "issued": "2025-01-09",
             "keyword": [
                 "earth science",
                 "spectral/engineering",
@@ -931290,7 +929862,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-26",
+            "modified": "2025-02-02",
             "programCode": [
                 "026:001"
             ],
@@ -931299,7 +929871,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -86.4 180.0 86.4",
-            "temporal": "2025-01-08T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2025-01-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -937880,15 +936452,15 @@
             "identifier": "C3271469675-LARC_ASDC",
             "issued": "2024-10-09",
             "keyword": [
-                "aerosols",
+                "earth science",
                 "atmosphere",
-                "earth science"
+                "aerosols"
             ],
             "landingPage": "https://doi.org/10.5067/SurfaceMonitorNetwork/MAIA/SURFACEMONITOR_PM_TOTAL_ANC.C01",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-21",
+            "modified": "2025-01-28",
             "programCode": [
                 "026:001"
             ],
@@ -937897,7 +936469,7 @@
                 "name": "NASA/LARC/SD/ASDC"
             },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
-            "temporal": "2021-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2021-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "MAIA",
                 "geospatial"
@@ -949871,28 +948443,28 @@
             "identifier": "C1693440802-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry",
+                "earth science",
                 "atmosphere",
-                "altitude",
                 "air quality",
+                "altitude",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
+                "precipitation",
+                "land surface",
                 "surface radiative properties",
                 "surface thermal properties",
-                "land surface",
-                "earth science",
                 "oceans",
-                "ocean temperature",
-                "clouds",
-                "precipitation",
-                "atmospheric water vapor",
-                "atmospheric temperature"
+                "ocean temperature"
             ],
             "landingPage": "https://doi.org/10.5067/47IB56XWPHB3",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-30",
+            "modified": "2024-12-16",
             "programCode": [
                 "026:001"
             ],
@@ -949911,7 +948483,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "SNDRAQIL3SDCCP",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2002-08-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -950043,57 +948615,6 @@
             ],
             "title": "SWOT Level 1B High-Rate Single-look Complex Data Product, Version 1.1"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "MISR Science Team (2018), Terra/MISR Level 3, Cloud Top Height-Optical Depth Product covering a quarter (seasonal), version 1, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/TERRA/MISR/MIL3QCOD.001",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Roger Marchand",
-                "hasEmail": "mailto:rojmarch@u.washington.edu"
-            },
-            "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. This file contains the public MISR Level 3 CloudTopHeight-OpticalDepth Product covering a quarter (seasonal).",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL3QCOD.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C1644916755-LARC",
-            "issued": "2018-08-06",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
-            ],
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL3QCOD.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2022-04-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-03-01T00:00:00Z/2022-05-03T00:00:00Z",
-            "theme": [
-                "MISR",
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Cloud Top Height-Optical Depth Product covering a quarter (seasonal) V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -956099,7 +954620,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Gregory Halverson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Gridded Surface Energy Balance Instantaneous L3 Global 70 m (ECO_L3G_SEB) Version 2 data product provides estimated incoming surface radiation (Rg) and net radiation (Rn) aligned with each daytime ECOSTRESS overpass. The Rg was generated using the Forest Light Environmental Simulator (FLiES) radiative transfer model implemented in an artificial neural network using Cloud Optical Thickness (COT) and Aerosol Optical Thickness (AOT) from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) along with albedo from ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS) Version 2 as variables. The Rg output from the FLiES model was bias corrected to Rg from GEOS-FP. The Rn is an output from the Breathing Earth System Simulator (BESS) algorithm. This data product is mosaicked from the L3 tiled SEB (ECO_L3T_SEB (https://doi.org/10.5067/ECOSTRESS/ECO_L3T_SEB.002)) product, projected to a globally snapped 0.0006\u00b0 grid, and has a spatial resolution of 70 meters (m).\n\nThe ECO_L3G_SEB Version 2 data product contains four layers distributed in an HDF5 format file including Rg, Rn, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\n-\tMissing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mask products (ECO_L2_CLOUD and ECO_L2G_CLOUD) to assess if a pixel is clear or cloudy (see section 3 of the User Guide).",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Gridded Surface Energy Balance Instantaneous L3 Global 70 m (ECO_L3G_SEB) Version 2 data product provides estimated incoming surface radiation (Rg) and net radiation (Rn) aligned with each daytime ECOSTRESS overpass. The Rg was generated using the Forest Light Environmental Simulator (FLiES) radiative transfer model implemented in an artificial neural network using Cloud Optical Thickness (COT) and Aerosol Optical Thickness (AOT) from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) along with albedo from ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS) (https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002) Version 2 as variables. The Rg output from the FLiES model was bias corrected to Rg from GEOS-FP. The Rn is an output from the Breathing Earth System Simulator (BESS) algorithm. This data product is mosaicked from the L3 tiled SEB (ECO_L3T_SEB) (https://doi.org/10.5067/ECOSTRESS/ECO_L3T_SEB.002) product, projected to a globally snapped 0.0006 degree grid, and has a spatial resolution of 70 meters (m).\n\nThe ECO_L3G_SEB Version 2 data product contains four layers distributed in an HDF5 format file including Rg, Rn, cloud mask, and water mask.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n* Missing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB, and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mask products (ECO_L2_CLOUD and ECO_L2G_CLOUD) to assess if a pixel is clear or cloudy (see Section 3 of the User Guide).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -956156,15 +954677,15 @@
             "identifier": "C2074855428-LPCLOUD",
             "issued": "2024-04-25",
             "keyword": [
-                "surface thermal properties",
                 "earth science",
-                "land surface"
+                "land surface",
+                "surface thermal properties"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L3G_SEB.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -956174,7 +954695,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -959163,13 +957684,6 @@
                     "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "How to cite ASDC data",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's data citation policy"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "NASA EOS ATB Documents: MISR",
@@ -959205,13 +957719,6 @@
                     "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "DOI data set landing page for MIL2TCSP_002",
-                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MIL2TCSP_L2.002",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
@@ -959240,13 +957747,6 @@
                     "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Earthdata Search for MIL2TCSP_002 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)\"",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2794379117-LARC",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
@@ -959303,13 +957803,6 @@
                     "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR project home page",
-                    "downloadURL": "https://misr.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "ASDC Direct Data Download for MIL2TCSP_002",
@@ -959385,7 +957878,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-10",
+            "modified": "2024-11-15",
             "programCode": [
                 "026:001"
             ],
@@ -959394,7 +957887,7 @@
                 "name": "NASA/LARC/SD/ASDC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1999-12-18T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
@@ -960914,17 +959407,17 @@
             "identifier": "C2938665243-NSIDC_CPRD",
             "issued": "2015-03-31",
             "keyword": [
+                "earth science",
                 "land surface",
+                "soils",
                 "ngda",
-                "national geospatial data asset",
-                "earth science",
-                "soils"
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/3K9F0S1Q5J2U",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-16",
+            "modified": "2025-01-24",
             "programCode": [
                 "026:001"
             ],
@@ -960933,7 +959426,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -85.044 180.0 85.044",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2015-03-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -966615,7 +965108,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Gregory Halverson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Tiled Surface Energy Balance Instantaneous L3 Global 70 m (ECO_L3T_SEB) Version 2 data product provides estimated incoming surface radiation (Rg) and net radiation (Rn) aligned with each daytime ECOSTRESS overpass. The Rg was generated using the Forest Light Environmental Simulator (FLiES) radiative transfer model implemented in an artificial neural network using Cloud Optical Thickness (COT) and Aerosol Optical Thickness (AOT) from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) along with albedo from ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS (https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002)) Version 2 as variables. The Rg output from the FLiES model was bias corrected to Rg from GEOS-FP. The Rn is an output from the Breathing Earth System Simulator (BESS) algorithm. This data product is tiled using a modified version of the Military Grid Reference System (MGRS (https://hls.gsfc.nasa.gov/products-description/tiling-system/)), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 meter (m) spatial resolution.\n\nThe ECO_L3T_SEB Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format with each data layer distributed as a separate COG. This product contains four layers including Rg, Rn, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\n-\tMissing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mask products (",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Tiled Surface Energy Balance Instantaneous L3 Global 70 m (ECO_L3T_SEB) Version 2 data product provides estimated incoming surface radiation (Rg) and net radiation (Rn) aligned with each daytime ECOSTRESS overpass. The Rg was generated using the Forest Light Environmental Simulator (FLiES) radiative transfer model implemented in an artificial neural network using Cloud Optical Thickness (COT) and Aerosol Optical Thickness (AOT) from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) along with albedo from ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS) (https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002) Version 2 as variables. The Rg output from the FLiES model was bias corrected to Rg from GEOS-FP. The Rn is an output from the Breathing Earth System Simulator (BESS) algorithm. This data product is tiled using a modified version of the Military Grid Reference System (MGRS) (https://hls.gsfc.nasa.gov/products-description/tiling-system/), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 meter (m) spatial resolution.\n\nThe ECO_L3T_SEB Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format with each data layer distributed as a separate COG. This product contains four layers including Rg, Rn, cloud mask, and water mask.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n* Missing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB, and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mas",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -966687,7 +965180,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -966697,7 +965190,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -969153,104 +967646,6 @@
             ],
             "title": "Gridded Species Distribution: Global Mammal Richness Grids, 2015 Release"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "Nghiem, J., G. Salter, and M.P. Lamb. 2023. Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2021, Version 2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2135",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@daac.ornl.gov"
-            },
-            "description": "This dataset provides sediment concentration and grain size distribution measurements from suspended and bed sediment samples collected in the Atchafalaya and Terrebonne River Basins as part of the Delta-X Spring campaign between March 24 to April 2, 2021 and Delta-X Fall campaign between August 17-25, 2021. During the field campaign, samples were collected in the main distributary channels and the interior of Mike Island in the Wax Lake Delta, Louisiana and at site CRMS0421 inside the Terrebonne River Basin. Sediment samples were collected from a boat using a Van Dorn sampler (for suspended sediment samples) or a Ponar bed sampler (for bed samples). Suspended sediment samples were collected from a boat drifting at approximately the same velocity as the water flow. One sample was collected per drift. Bed samples were collected in a similar fashion. Data includes measurements of sediment grain size, total sediment concentration, as well as water temperature, velocity, salinity, and depth. This Version 2 includes the initial release of Fall 2021 data and an update to the Version 1 (Spring 2021) data file in which an error in the data was resolved.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2135",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "This link allows direct data access via Earthdata login",
-                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_Sediment_Grain_Size_V2/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ORNL DAAC Data Set Documentation",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V2.html",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Data set Landing Page DOI URL",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2135",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2021, Version 2: DeltaX_Sediment_Grain_Size_V2.pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Sediment_Grain_Size_V2/comp/DeltaX_Sediment_Grain_Size_V2.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Figure 1: Suspended and bed sediment sampling locations in the Wax Lake Delta, Louisiana. Clusters of measurements are grouped together into single points on this map. Map excludes measurements made far upstream of the Wax Lake Delta or in the Terrebonne River Basin.",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V2_Fig1.png",
-                    "mediaType": "image/png",
-                    "title": "Get a related visualization"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Delta-X Project Site",
-                    "downloadURL": "https://deltax.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                }
-            ],
-            "graphic-preview-description": "Figure 1: Suspended and bed sediment sampling locations in the Wax Lake Delta, Louisiana. Clusters of measurements are grouped together into single points on this map. Map excludes measurements made far upstream of the Wax Lake Delta or in the Terrebonne River Basin.",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V2_Fig1.png",
-            "identifier": "C2619216342-ORNL_CLOUD",
-            "issued": "2023-02-23",
-            "keyword": [
-                "land surface",
-                "biosphere",
-                "ecosystems",
-                "geomorphic landforms/processes",
-                "water quality/water chemistry",
-                "surface water",
-                "terrestrial hydrosphere",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2135",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2023-06-12",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "spatial": "-91.45 29.17 -90.82 29.7",
-            "temporal": "2021-03-24T17:22:00Z/2021-08-25T17:08:00Z",
-            "theme": [
-                "Delta-X",
-                "geospatial"
-            ],
-            "title": "Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2021, Version 2"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -985923,16 +984318,16 @@
             "identifier": "C1450086509-NSIDC_ECS",
             "issued": "2009-08-17",
             "keyword": [
+                "earth science",
                 "cryosphere",
                 "sea ice",
-                "earth science",
                 "snow/ice"
             ],
             "landingPage": "https://doi.org/10.5067/VF7QO90IHZ99",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-28",
+            "modified": "2025-02-04",
             "programCode": [
                 "026:001"
             ],
@@ -985941,7 +984336,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2009-08-17T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2009-08-17T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -995712,6 +994107,96 @@
             ],
             "title": "GLL PPR EARTH-2 ENCOUNTER EDR"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Gridded 1-Degree Seasonal Soil Moisture V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/O6J9L5JKD5YR.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This data set contains Level-3 gridded seasonal global soil moisture estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FO6J9L5JKD5YR",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_SNSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782405185-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_SNSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782405185-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/O6J9L5JKD5YR",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/O6J9L5JKD5YR",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2782405185-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/O6J9L5JKD5YR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Gridded 1-Degree Seasonal Soil Moisture V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1000163,7 +998648,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Gregory Halverson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Gridded Downscaled Meteorology Instantaneous L3 Global 70 m (ECO_L3G_MET) Version 2 data product provides instantaneous near-surface air temperature (Ta) and relative humidity (RH) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and Ta or RH from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. This data product is mosaicked from the L3 tiled MET (ECO_L3T_MET (https://doi.org/10.5067/ECOSTRESS/ECO_L3T_MET.002)) product, projected to a globally snapped 0.0006\u00b0 grid, and has a spatial resolution of 70 meters (m).\n\nThe ECO_L3G_MET Version 2 data product contains four layers distributed in an HDF5 format file including Ta, RH, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Gridded Downscaled Meteorology Instantaneous L3 Global 70 m (ECO_L3G_MET) Version 2 data product provides instantaneous near-surface air temperature (Ta) and relative humidity (RH) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and Ta or RH from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. This data product is mosaicked from the L3 tiled MET (ECO_L3T_MET) (https://doi.org/10.5067/ECOSTRESS/ECO_L3T_MET.002) product, projected to a globally snapped 0.0006 degree grid, and has a spatial resolution of 70 meters (m).\n\nThe ECO_L3G_MET Version 2 data product contains four layers distributed in an HDF5 format file including Ta, RH, cloud mask, and water mask.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1000220,16 +998705,16 @@
             "identifier": "C2074897737-LPCLOUD",
             "issued": "2024-04-25",
             "keyword": [
-                "atmosphere",
                 "earth science",
-                "atmospheric water vapor",
-                "atmospheric temperature"
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L3G_MET.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1000239,7 +998724,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -1000352,7 +998837,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -1000362,7 +998847,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2012-03-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2012-03-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -1009330,7 +1007815,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-25",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -1009339,7 +1007824,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -85.044 180.0 85.044",
-            "temporal": "2015-03-31T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2015-03-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1011122,55 +1009607,6 @@
             ],
             "title": "CASSINI SS/S RPWS CALIBRATED LP CONTINUOUS CURRENT V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Monthly averages of atmospheric temperature and VMR for atmospheric species are provided at 2 deg. lat. X 4 deg. long. spatial grids and at a subset of TES standard pressure levels. Algorithms for deriving TES L3 data will be provided in the data files.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESTL3COM_L3",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C189204048-LARC",
-            "issued": "2010-08-11",
-            "keyword": [
-                "atmosphere",
-                "air quality",
-                "earth science",
-                "atmospheric chemistry/carbon and hydrocarbon compounds"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESTL3COM_L3",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-06",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L3 CO Monthly Gridded V003"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1012606,7 +1011042,7 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/SLR/SLR_DAILY_NPT_001.",
+            "citation": "International Laser Ranging Service (ILRS), SLR daily full-rate data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/SLR/slr_data_daily_fr_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
@@ -1012646,17 +1011082,17 @@
             "identifier": "C1537486947-CDDIS",
             "issued": "1976-01-01",
             "keyword": [
+                "earth science",
                 "solid earth",
-                "tectonics",
-                "gravity/gravitational field",
                 "geodetics",
-                "earth science"
+                "gravity/gravitational field",
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/SLR/SLR_DAILY_NPT_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-15",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -1012665,7 +1011101,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1976-01-01T00:00:00Z/2024-11-18T00:00:00Z",
+            "temporal": "1976-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
@@ -1018621,15 +1017057,15 @@
             "identifier": "C2807627777-LANCEMODIS",
             "issued": "2023-11-20",
             "keyword": [
+                "earth science",
                 "land surface",
-                "surface radiative properties",
-                "earth science"
+                "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA4N.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1018639,7 +1017075,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -1028185,73 +1026621,6 @@
             ],
             "title": "CASSINI RSS RAW DATA SET - SROC10 V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "VCST Team. 2024-01-22. VIIRS/JPSS2 Day/Night Band 6-Min L1B Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ202DNB_NRT.002. https://dx.doi.org/10.5067/VIIRS/VJ202DNB_NRT.002.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VINCENT Chiang",
-                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
-            },
-            "creator": "VCST Team",
-            "description": "The Near Real Time (NRT) VIIRS Level 1 and Level 2 swath (VJ202DNB_NRT) product is single NASA VIIRS panchromatic Day-Night band (DNB) calibrated radiance product. The DNB is one of the M-bands with an at-nadir spatial resolution of 750 meters (across the entire scan). The panchromatic DNB's spectral wavelength ranges from 0.5 \u00b5m to 0.9 \u00b5m. It facilitates measuring night lights, reflected solar/lunar lights with a large dynamic range between a low of a quarter moon illumination to the brightest daylight. The DNB attempts to maintain a nearly constant 750-m resolution over the entire 3060 km orbital swath by resorting to an on-board aggregation method, which also renders the calibration of the DNB a challenge. Stray-light and other sources of noise (lunar illuminance, twilight, clouds, noisy scan-edges, etc.) affect the DNB quality, and warrant correction.\r\n\r\nFor more information download VIIRS Level 1 Product User's Guide at:\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/archive/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202DNB_NRT.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Direct access to data from MODAPS public site.",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                }
-            ],
-            "identifier": "C2837615105-LANCEMODIS",
-            "issued": "2024-01-10",
-            "keyword": [
-                "infrared wavelengths",
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
-            ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202DNB_NRT.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-07",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "release-place": "MODAPS at NASA/GSFC",
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
-            "theme": [
-                "NOAA - SPACE WEATHER PROGRAM",
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "VIIRS/JPSS2 Day/Night Band 6-Min L1B Swath 750m NRT"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1029736,28 +1028105,28 @@
             "identifier": "C1693440795-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
-                "clouds",
-                "atmospheric water vapor",
-                "altitude",
-                "atmospheric temperature",
+                "earth science",
                 "atmosphere",
-                "atmospheric chemistry",
                 "air quality",
+                "altitude",
+                "atmospheric chemistry",
+                "atmospheric pressure",
                 "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
                 "precipitation",
+                "land surface",
                 "surface radiative properties",
                 "surface thermal properties",
-                "atmospheric pressure",
-                "ocean temperature",
                 "oceans",
-                "earth science",
-                "land surface"
+                "ocean temperature"
             ],
             "landingPage": "https://doi.org/10.5067/ILFPVBTDHTDL",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-01",
+            "modified": "2024-12-31",
             "programCode": [
                 "026:001"
             ],
@@ -1029777,7 +1028146,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "SNDRAQIL2CCPRET",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-30T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2002-08-30T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -1030880,7 +1029249,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-20",
+            "modified": "2025-01-25",
             "programCode": [
                 "026:001"
             ],
@@ -1030889,7 +1029258,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2012-07-02T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2012-07-02T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1031561,7 +1029930,7 @@
                 "name": "NASA/LARC/SD/ASDC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2025-01-20T00:00:00Z",
+            "temporal": "1999-12-18T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
@@ -1036418,15 +1034787,15 @@
             "identifier": "C2750966856-NSIDC_ECS",
             "issued": "2019-03-29",
             "keyword": [
-                "glaciers/ice sheets",
+                "earth science",
                 "cryosphere",
-                "earth science"
+                "glaciers/ice sheets"
             ],
             "landingPage": "https://doi.org/10.5067/ATLAS/ATL11.006",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-08-29",
+            "modified": "2024-11-07",
             "programCode": [
                 "026:001"
             ],
@@ -1036435,7 +1034804,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2019-03-29T00:00:00Z/2024-11-04T00:00:00Z",
+            "temporal": "2019-03-29T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1048372,17 +1046741,17 @@
             "identifier": "C1708941000-CDDIS",
             "issued": "1990-01-01",
             "keyword": [
-                "tectonics",
                 "earth science",
-                "gravity/gravitational field",
                 "solid earth",
-                "geodetics"
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1708941000-CDDIS.html",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-26",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1048390,7 +1046759,7 @@
                 "@type": "org:Organization",
                 "name": "CDDIS"
             },
-            "temporal": "1992-01-01T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "1992-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IDS",
                 "geospatial"
@@ -1051359,74 +1049728,6 @@
             ],
             "title": "BOREAS TE-21 Daily Surface Meteorological Data"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "VCST Team. 2024-01-22. VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ203MOD_NRT.002. https://doi.org/10.5067/VIIRS/VJ203MOD_NRT.002.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VINCENT Chiang",
-                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
-            },
-            "creator": "VCST Team",
-            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath, short-name VJ203MOD_NRT) is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-based NASA VIIRS L1 terrain-corrected geolocation product, and contains the derived line-of-sight (LOS) vectors for each of the 750-m moderate-resolution, or M-bands. The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform's ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry. It produces geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel. The VJ203MOD product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, and quality flag for every pixel location. VJ203MOD provides a fundamental input to derive a number of VIIRS M-band higher-level products.\r\n\r\n\r\nThe J2 VIIRS geolocation underwent an on-orbit validation. Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands. The Day-Night band (DNB) geolocation error of about 2000 m was corrected. Further, the geolocation biases in the scan profile were also corrected. All these corrections bring the geolocation uncertainties for the J2 L1 products to within 75 m (1-sigma) in both the along-scan and along-track directions.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203MOD_NRT.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Direct access to data from MODAPS public site.",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through MODAPS"
-                }
-            ],
-            "identifier": "C2837613785-LANCEMODIS",
-            "issued": "2024-01-10",
-            "keyword": [
-                "sensor characteristics",
-                "visible wavelengths",
-                "spectral/engineering",
-                "earth science",
-                "infrared wavelengths"
-            ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203MOD_NRT.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-07",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "release-place": "MODAPS at NASA/GSFC",
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-01-10T00:00:00Z/2025-01-13T00:00:00Z",
-            "theme": [
-                "NOAA - SPACE WEATHER PROGRAM",
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "VIIRS/JPSS2 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1054301,7 +1052602,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1054311,7 +1052612,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -1065086,54 +1063387,6 @@
             ],
             "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 3 CR2 V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Global Cloud public Product in netCDF format covering a month;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Global Cloud public Product in netCDF format covering a month",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3MCLDN_L3.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919908-LARC",
-            "issued": "2006-03-01",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3MCLDN_L3.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Global Cloud public Product in netCDF format covering a month V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1072852,7 +1071105,7 @@
                     "description": "ORNL DAAC Data Set Documentation",
                     "downloadURL": "https://daac.ornl.gov/GEDI/guides/GEDI_L4C_WSCI.html",
                     "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
+                    "title": "View this dataset's user's guide"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -1072900,18 +1071153,18 @@
             "graphic-preview-description": "Example subset of the Waveform Structural Complexity Index (WSCI) predictions from the GEDI Level-4C footprint product over the Eastern Amazon.",
             "graphic-preview-file": "https://daac.ornl.gov/GEDI/guides/GEDI_L4C_WSCI_Fig1.jpg",
             "identifier": "C3049900163-ORNL_CLOUD",
-            "issued": "2024-09-26",
+            "issued": "2025-01-27",
             "keyword": [
-                "biosphere",
-                "vegetation",
                 "earth science",
-                "ecosystems"
+                "biosphere",
+                "ecosystems",
+                "vegetation"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/2338",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-09-27",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1086199,21 +1084452,21 @@
             "issued": "2017-12-11",
             "keyword": [
                 "earth science",
-                "land surface",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric temperature",
                 "atmospheric water vapor",
+                "land surface",
+                "surface thermal properties",
                 "oceans",
-                "atmospheric pressure",
-                "atmosphere",
                 "ocean temperature",
-                "precipitation",
-                "surface thermal properties",
-                "atmospheric temperature"
+                "precipitation"
             ],
             "landingPage": "https://doi.org/10.5067/69Y2R9BJAJS3",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-02",
+            "modified": "2024-12-29",
             "programCode": [
                 "026:001"
             ],
@@ -1086231,7 +1084484,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "SNDRJ1ML2RMS",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2017-12-01T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2017-12-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
@@ -1093854,6 +1092107,113 @@
             ],
             "title": "Global colored dissolved organic matter (CDOM) measurements"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Nghiem, J., G. Salter, and M.P. Lamb. 2024. Delta-X: Sediment Core Grain Size Distribution, Wax Lake Delta, MRD, LA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2382",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@daac.ornl.gov"
+            },
+            "description": "This dataset provides grain size distribution measurements collected from sediment core samples on Mike Island in the Wax Lake Delta, Louisiana, as part of the Delta-X Spring campaign in March, 2021,and the Fall campaign during August, 2021. The data are for March 26 and 29, and August 18 and 24. Sediment cores were collected using a piston core, then volume-based grain size distribution for each sample was measured using a laser diffraction particle size analyzer. The data are provided in comma separated values (CSV) format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2382",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Sediment_Core_GrainSize/data/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_Sediment_Core_GrainSize_2382.zip",
+                    "mediaType": "application/zip",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Core_GrainSize.html",
+                    "mediaType": "text/html",
+                    "title": "View this dataset's user's guide"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2382",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_Sediment_Core_GrainSize_2382.zip",
+                    "mediaType": "application/zip",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Delta-X: Sediment Core Grain Size Distribution, Wax Lake Delta, MRD, LA: DeltaX_Sediment_Core_GrainSize.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Sediment_Core_GrainSize/comp/DeltaX_Sediment_Core_GrainSize.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Sediment core sampling locations in the Wax Lake Delta, Louisiana. All sediment cores were sampled on Mike Island.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Core_GrainSize_Fig1.png",
+                    "mediaType": "image/png",
+                    "title": "Get a related visualization"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Delta-X Project Site",
+                    "downloadURL": "https://deltax.jpl.nasa.gov/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                }
+            ],
+            "graphic-preview-description": "Sediment core sampling locations in the Wax Lake Delta, Louisiana. All sediment cores were sampled on Mike Island.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Core_GrainSize_Fig1.png",
+            "identifier": "C3386034988-ORNL_CLOUD",
+            "issued": "2025-01-24",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geomorphic landforms/processes"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2382",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
+            "spatial": "-91.45 29.48 -91.44 29.51",
+            "temporal": "2021-03-26T17:23:03Z/2021-08-24T18:09:46Z",
+            "theme": [
+                "Delta-X",
+                "geospatial"
+            ],
+            "title": "Delta-X: Sediment Core Grain Size Distribution, Wax Lake Delta, MRD, LA"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1094841,6 +1093201,96 @@
             ],
             "title": "Microarray Profile of Gene Expression during Osteoclast Differentiation in Modeled Microgravity"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Gridded 1-Degree Daily Soil Moisture V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/PTKXKSE28XYN.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This data set contains Level-3 gridded daily global soil moisture estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPTKXKSE28XYN",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_DYSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782398419-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_DYSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782398419-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/PTKXKSE28XYN",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/PTKXKSE28XYN",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2782398419-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/PTKXKSE28XYN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Gridded 1-Degree Daily Soil Moisture V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1095493,54 +1093943,6 @@
             ],
             "title": "PVO VENUS ONMS BROWSE NEUTRAL\n                                      DENSITY 12 SECOND V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Radiance Product for a day;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Radiance Product covering a day",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DRD_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677717-LARC",
-            "issued": "2003-12-03",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DRD_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Radiance Product covering a day V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1104702,6 +1103104,73 @@
             ],
             "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1017 V1.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "VCST Team. 2025-01-27. VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath IP 750m NRT. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.021. https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.021.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VINCENT Chiang",
+                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
+            },
+            "creator": "VCST Team",
+            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m, short-name VJ203DNB_NRT is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-based NASA VIIRS L1 terrain-corrected geolocation product, and contains the derived line-of-sight (LOS) vectors for the single panchromatic Day-Night band (DNB). The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform's ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry. It provides geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel. The VJ203DNB product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, lunar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, moon illumination fraction and phase angle, and quality flag for every pixel location.\n\nThe J2 VIIRS geolocation underwent an on-orbit validation. Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands. The Day-Night band (DNB) geolocation error of about 2000 m was corrected. Further, the geolocation biases in the scan profile were also corrected. All these corrections bring the geolocation uncertainties for the J2 L1 products to within 75 m (1-sigma) in both the along-scan and along-track directions.\n\nVIIRS Level-1B Geolocation ATBD \n\nhttps://ladsweb.modaps.eosdis.nasa.gov/internal/deploy/web-stage/ladsweb/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/Product%20Generation%20Algorithms/NASARevisedVIIRSGeolocationATBD2014.pdf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203DNB_NRT.021",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5201/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C3383695704-LANCEMODIS",
+            "issued": "2025-01-25",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203DNB_NRT.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2025-01-27T00:00:00Z/2025-02-03T00:00:00Z",
+            "theme": [
+                "NOAA - SPACE WEATHER PROGRAM",
+                "LANCE",
+                "geospatial"
+            ],
+            "title": "VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath IP 750m NRT"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1113817,54 +1112286,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP020 RDR-REFLECT V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a day's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a day",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3DAEF_L3.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C156141681-LARC",
-            "issued": "2007-07-30",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3DAEF_L3.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a day V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1117595,6 +1116016,115 @@
             ],
             "title": "P445.3 (PLUTO) OCCULTATION V1.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Jones, C., B. Varugu, T. Oliver-Cabrera, and Y. Lou. 2024. Pre-Delta-X: UAVSAR Georeferenced Channel Maps, Atchafalaya Basin, LA, USA, 2016, V2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2366",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@daac.ornl.gov"
+            },
+            "description": "This dataset provides spatial data on water channels in the estuary of the Atchafalaya Basin of the Mississippi River Delta of coastal Louisiana. These Level-3 (L3) channel maps were developed from interferograms derived from Uninhabited Aerial Vehicle Synthetic Aperture Radar (UAVSAR) data collected on 2016-10-16 (low tides) and 2016-10-17 (high tides). The channel maps define open water paths in hydrodynamic models and are used to evaluate model performance. This is version 2 of this dataset. Data are provided in cloud optimized GeoTIFF format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2366",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/PreDeltaX_UAVSARChannelMaps_V2/data/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/PreDeltaX_UAVSARChannelMaps_V2_2366.zip",
+                    "mediaType": "application/zip",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSARChannelMaps_V2.html",
+                    "mediaType": "text/html",
+                    "title": "View this dataset's user's guide"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2366",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/PreDeltaX_UAVSARChannelMaps_V2_2366.zip",
+                    "mediaType": "application/zip",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Pre-Delta-X: UAVSAR Georeferenced Channel Maps, Atchafalaya Basin, LA, USA, 2016, V2: PreDeltaX_UAVSARChannelMaps_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/PreDeltaX_UAVSARChannelMaps_V2/comp/PreDeltaX_UAVSARChannelMaps_V2.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Water channels in the Atchafalaya Basin of the Mississippi River Delta of coastal Louisiana, U.S., during high tide derived from data acquired on October 17, 2016, between 19:37 and 21:51 UTC.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSARChannelMaps_V2_Fig1.png",
+                    "mediaType": "image/png",
+                    "title": "Get a related visualization"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Delta-X Project Site",
+                    "downloadURL": "https://deltax.jpl.nasa.gov/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                }
+            ],
+            "graphic-preview-description": "Water channels in the Atchafalaya Basin of the Mississippi River Delta of coastal Louisiana, U.S., during high tide derived from data acquired on October 17, 2016, between 19:37 and 21:51 UTC.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSARChannelMaps_V2_Fig1.png",
+            "identifier": "C3385943342-ORNL_CLOUD",
+            "issued": "2025-01-28",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "ecosystems",
+                "terrestrial hydrosphere",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2366",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
+            "spatial": "-91.62 29.36 -91.06 29.76",
+            "temporal": "2016-10-16T14:08:00Z/2016-10-17T21:51:59Z",
+            "theme": [
+                "Delta-X",
+                "geospatial"
+            ],
+            "title": "Pre-Delta-X: UAVSAR Georeferenced Channel Maps, Atchafalaya Basin, LA, USA, 2016, V2"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1128950,19 +1127480,19 @@
             "issued": "2017-10-01",
             "keyword": [
                 "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "ultraviolet wavelengths",
-                "atmospheric radiation",
                 "atmosphere",
+                "atmospheric radiation",
                 "spectral/engineering",
-                "infrared wavelengths"
+                "infrared wavelengths",
+                "ultraviolet wavelengths",
+                "ngda",
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MYDCSR_8.061",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-15",
+            "modified": "2025-01-23",
             "programCode": [
                 "026:001"
             ],
@@ -1128972,7 +1127502,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -1130595,7 +1129125,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1130605,7 +1129135,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2021-09-15T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2021-09-15T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "Terra",
@@ -1134317,6 +1132847,96 @@
             ],
             "title": "CERES ERBE-like Time-Interpolated TOA Fluxes Terra Crosstrack Edition4"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Gridded 1-Degree Monthly Soil Moisture V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MJCEUOW1H6ON.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This data set contains Level-3 gridded monthly global soil moisture estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMJCEUOW1H6ON",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_MOSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782402143-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_MOSM+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2782402143-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MJCEUOW1H6ON",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MJCEUOW1H6ON",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2782402143-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/MJCEUOW1H6ON",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Gridded 1-Degree Monthly Soil Moisture V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1134708,16 +1133328,16 @@
             "identifier": "C2619443946-POCLOUD",
             "issued": "2020-12-17",
             "keyword": [
-                "sea surface topography",
                 "earth science",
                 "oceans",
+                "sea surface topography",
                 "ocean waves"
             ],
             "landingPage": "https://doi.org/10.5067/S6AP4-2HRNUR-F08",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-03",
+            "modified": "2025-01-10",
             "programCode": [
                 "026:001"
             ],
@@ -1134730,7 +1133350,7 @@
             ],
             "release-place": "PO.DAAC",
             "spatial": "-180.0 -66.15 180.0 66.15",
-            "temporal": "2020-11-30T14:26:00.875Z/2025-01-27T00:00:00Z",
+            "temporal": "2020-11-30T14:26:00.875Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
@@ -1138232,17 +1136852,17 @@
             "identifier": "C3363997464-LANCEMODIS",
             "issued": "2024-12-31",
             "keyword": [
-                "vegetation",
                 "earth science",
                 "biosphere",
-                "surface radiative properties",
-                "land surface"
+                "vegetation",
+                "land surface",
+                "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VNP13A4N.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-03",
+            "modified": "2025-02-10",
             "programCode": [
                 "026:001"
             ],
@@ -1138252,7 +1136872,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2025-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2025-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "CWIC",
                 "Suomi-NPP",
@@ -1142614,54 +1141234,6 @@
             ],
             "title": "SHAPE MODEL OF ASTEROID (153591) 2001 SN263"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Cloud Motion Vector quarterly Product in netCDF format;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Cloud Motion Vector quarterly Product in netCDF format",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3QCMVN_L3.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C194517135-LARC",
-            "issued": "2012-08-16",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3QCMVN_L3.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2017-04-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Cloud Motion Vector quarterly Product in netCDF format V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1148898,54 +1147470,6 @@
             ],
             "title": "VIKING LANDER 2 MARS SEISMOLOGY\n                                     RESTORED DATA V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Albedo product in netCDF format covering a month;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "MISR Level 3 Component Global Albedo publicly available product in netCDF format covering a month.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3MALN_L3.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919887-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3MALN_L3.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Albedo product in netCDF format covering a month V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1166717,16 +1165241,16 @@
             "identifier": "C2946990777-LAADS",
             "issued": "2024-02-10",
             "keyword": [
-                "atmospheric radiation",
-                "clouds",
+                "earth science",
                 "atmosphere",
-                "earth science"
+                "atmospheric radiation",
+                "clouds"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_D3_VIIRS_NOAA20.011",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-20",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -1166736,7 +1165260,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2018-02-17T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-02-17T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -1172741,51 +1171265,6 @@
             ],
             "title": "MSL MARS ALPHA PARTICLE X-RAY SPECTROMETER 2 EDR V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, LaRC.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support@earthdata.nasa.gov"
-            },
-            "description": "MOPITT Calibration History File",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1288777498-LARC.html",
-                    "mediaType": "text/html",
-                    "title": "CMR"
-                }
-            ],
-            "identifier": "C1288777498-LARC",
-            "issued": "2016-06-15",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1288777498-LARC.html",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2016-07-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MOPITT Calibration History File V007"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1174395,54 +1172874,6 @@
             ],
             "title": "VIIRS/NPP BRDF/Albedo Parameter 1 Band M8 Daily L3 Global 30 ArcSec CMG V001"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Albedo seasonal product in netCDF format;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "MISR Level 3 Component Global Albedo publicly available product in netCDF format covering a quarter (seasonal).",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QALN_L3.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919886-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QALN_L3.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Albedo seasonal product in netCDF format V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1182049,7 +1180480,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1182059,7 +1180490,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -1187898,6 +1186329,73 @@
             ],
             "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0676 V1.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "VCST Team. 2025-01-27. VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath SDR 375m NRT. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ202IMG_NRT.021. https://doi.org/10.5067/VIIRS/VJ202IMG_NRT.021.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VINCENT Chiang",
+                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
+            },
+            "creator": "VCST Team",
+            "description": "The VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375m Near Real Time (NRT), short-name VJ202IMG_NRT is platform-derived NASA VIIRS L1B calibrated radiances product that comprises five image-resolution or I-bands, which have a 375-meter resolution at nadir. These I-bands comprise three reflective solar bands (RSB) and two thermal emissive bands (TEB). Each of the I-bands has 32 detectors in the along-track direction with 32 rows of pixels per scan that offer a resolution that is twice finer than that of the moderate (M) and Day-Night bands (DNB). Ranging in wavelengths from 0.6 \u00b5m to 12.4 \u00b5m, the I-bands are sensitive to visible/reflective, near-, shortwave-, mediumwave-, and longwave-infrared wavelengths. Derived from the NASA VIIRS L1A raw radiances, this product includes calibrated and geolocated radiance and reflectance data, quality flags, and granule- and collection-level metadata. In contrast to a MODIS L1B product, which temporally spans 5 minutes, the VIIRS L1B calibrated radiances product contains a nominal temporal duration of 6 minutes. The image dimensions of the 375-m swath product measure 6464 lines by 6400 pixels.\n\nThe J2 VIIRS radiometric calibration Level-1B reprocessing includes a few calibration updates for the reflective solar bands (RSB), but no significant changes for the day-night band (DNB) or thermal emissive bands (TEB).  For more information download VIIRS Level 1 Product User's Guide at: \n\nhttps://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document Archive/Science Data Product Documentation/Processing and Algorithm Version History/NASA_VIIRS_L1B_UG_August_2021.pdf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202IMG_NRT.021",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5201/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C3383724133-LANCEMODIS",
+            "issued": "2025-01-25",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202IMG_NRT.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2025-01-27T00:00:00Z/2025-02-03T00:00:00Z",
+            "theme": [
+                "NOAA - SPACE WEATHER PROGRAM",
+                "LANCE",
+                "geospatial"
+            ],
+            "title": "VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath SDR 375m NRT"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1194001,54 +1192499,6 @@
             ],
             "title": "MERRA-2 tavg3_3d_qdt_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Moist Tendencies 0.625 x 0.5 degree V5.12.4 (M2T3NPQDT) at GES DISC"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Land seasonal product in netCDF format;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Land product in netCDF format covering a quarter (seasonal)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QLSN_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919903-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QLSN_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Land seasonal product in netCDF format V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1196410,14 +1194860,21 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS.",
+            "citation": "International VLBI Service for Geodesy and Astrometry (IVS) Intensive Earth Orientation Parameter Series (EOP-I) Product [online]. Available from the NASA Crustal Dynamics Data Information System DAAC, Greenbelt, MD, USA at: DOI: 10.5067/VLBI/VLBI_intensive_eopi_001, Accessed [[enter user data access date]]",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
-                "hasEmail": "mailto:support-cddis@earthdata.nasa.gov"
+                "hasEmail": "mailto:support-cddis@nasa.gov"
             },
             "description": "These derived data products are intensive (1-hour experiments) Earth orientation parameter (EOPI) solutions obtained with Very Long Baseline Interferometry (VLBI). The CDDIS archive contains EOPI solutions provided by various analysis centers of the International VLBI Service for Geodesy and Astrometry (IVS). The VLBI EOPI series products includes one for each Universal Time (UT1) intensive session with a minimum of one year of data. The operational EOPI product is available at IVS Data Centers 24 hours after the Intensive data become available.",
             "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVLBI%2FVLBI_intensive_eopi_001",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "CDDIS VLBI products",
@@ -1196434,6 +1194891,7 @@
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Dataset Landing Page",
                     "downloadURL": "https://doi.org/10.5067/VLBI/VLBI_intensive_eopi_001",
                     "mediaType": "text/html",
                     "title": "This dataset's landing page"
@@ -1196442,16 +1194900,16 @@
             "identifier": "C2398710772-CDDIS",
             "issued": "2014-01-02",
             "keyword": [
-                "geodetics",
                 "earth science",
+                "solid earth",
                 "coordinate reference system",
-                "solid earth"
+                "geodetics"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2398710772-CDDIS.html",
+            "landingPage": "https://doi.org/10.5067/VLBI/VLBI_intensive_eopi_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-12",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -1196460,7 +1194918,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2005-01-01T00:00:00Z/2024-12-16T00:00:00Z",
+            "temporal": "2005-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1201643,17 +1200101,17 @@
             "identifier": "C3255933550-LARC_CLOUD",
             "issued": "2024-06-07",
             "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
                 "earth science",
+                "atmosphere",
                 "atmospheric radiation",
-                "atmosphere"
+                "spectral/engineering",
+                "infrared wavelengths"
             ],
             "landingPage": "https://doi.org/10.5067/PREFIRE-SAT1/PREFIRE/PAYLOAD-TLM_L0.R01",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1201662,7 +1200120,7 @@
                 "name": "NASA/LARC/SD/ASDC"
             },
             "spatial": "-180.0 -84.0 180.0 84.0",
-            "temporal": "2024-06-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-06-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "PREFIRE",
                 "geospatial"
@@ -1203816,6 +1202274,116 @@
             ],
             "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V3.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Nghiem, J., G. Salter, and M.P. Lamb. 2024. Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2019-2021, V3. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2379",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@daac.ornl.gov"
+            },
+            "description": "This dataset includes sediment concentration and grain size distribution measurements from suspended and bed sediment samples collected in the Atchafalaya River and Terrebonne Basins as part of the Delta-X Spring campaign between March 25 and April 2, 2021, and the Delta-X Fall campaign between August 17 and 22, 2021. In addition, ten samples were collected during a field campaign in October 2019. Samples were collected in the main channels and the interior of Mike Island in the Wax Lake Delta, Louisiana and at site CRMS0421 inside the Terrebonne Basin. Sediment samples were collected from a boat using a Van Dorn sampler (for suspended sediment samples) or a Ponar bed sampler (for bed samples). Suspended sediment samples were collected from a boat drifting at approximately the same velocity as the water flow. One sample was collected per drift. Bed samples were collected in a similar fashion. Data include measurements of sediment grain size distribution, total sediment concentration, water temperature, flow velocity, salinity, and depth. This Version 3 updates Version 2 to include data from more samples and reprocessed laser diffraction grain size distributions with optimized sediment optical properties. The data is provided in comma separated values (CSV) format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2379",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Sediment_Grain_Size_V3/data/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_Sediment_Grain_Size_V3_2379.zip",
+                    "mediaType": "application/zip",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V3.html",
+                    "mediaType": "text/html",
+                    "title": "View this dataset's user's guide"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2379",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_Sediment_Grain_Size_V3_2379.zip",
+                    "mediaType": "application/zip",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2019-2021, V3: DeltaX_Sediment_Grain_Size_V3.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Sediment_Grain_Size_V3/comp/DeltaX_Sediment_Grain_Size_V3.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Figure 1: Suspended and bed sediment sampling locations (dots) in the Wax Lake Delta, Louisiana. Clusters of measurements are grouped together into single points on this map. Map excludes measurements made far upstream of the Wax Lake Delta or in the Terrebonne River Basin.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V3_Fig1.png",
+                    "mediaType": "image/png",
+                    "title": "Get a related visualization"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Delta-X Project Site",
+                    "downloadURL": "https://deltax.jpl.nasa.gov/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                }
+            ],
+            "graphic-preview-description": "Figure 1: Suspended and bed sediment sampling locations (dots) in the Wax Lake Delta, Louisiana. Clusters of measurements are grouped together into single points on this map. Map excludes measurements made far upstream of the Wax Lake Delta or in the Terrebonne River Basin.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V3_Fig1.png",
+            "identifier": "C3388150145-ORNL_CLOUD",
+            "issued": "2025-01-28",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "geomorphic landforms/processes",
+                "terrestrial hydrosphere",
+                "surface water",
+                "water quality/water chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2379",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
+            "spatial": "-91.45 29.17 -90.82 29.7",
+            "temporal": "2019-10-25T14:45:34Z/2021-08-24T17:08:00Z",
+            "theme": [
+                "Delta-X",
+                "geospatial"
+            ],
+            "title": "Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2019-2021, V3"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1205064,123 +1203632,6 @@
             ],
             "title": "MODIS/Aqua Surface Reflectance Daily L2G Global 500m SIN Grid NRT"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "VCST Team. 2024-01-22. VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ203IMG_NRT.002. https://doi.org/10.5067/VIIRS/VJ203IMG_NRT.002.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VINCENT Chiang",
-                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
-            },
-            "creator": "VCST Team",
-            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath, short-name VJ203IMG_NRT is  the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-derived NASA VIIRS L1 terrain-corrected geolocation product and contains the derived line-of-sight (LOS) vectors for each of the 375-m image-resolution or I-bands. The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform's ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry. It produces geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel. The VJ203IMG product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, and quality flag for every pixel location. VJ203IMG provides a fundamental input to derive a number of VIIRS I-band higher-level products.\r\n\r\n\r\nThe J2 VIIRS geolocation underwent an on-orbit validation. Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands. The Day-Night band (DNB) geolocation error of about 2000 m was corrected. Further, the geolocation biases in the scan profile were also corrected. All these corrections bring the geolocation uncertainties for the J2 L1 products to within 75 m (1-sigma) in both the along-scan and along-track directions.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203IMG_NRT.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Direct access to data from MODAPS public site.",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through MODAPS"
-                }
-            ],
-            "identifier": "C2837614053-LANCEMODIS",
-            "issued": "2024-01-10",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203IMG_NRT.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-07",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "release-place": "MODAPS at NASA/GSFC",
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
-            "theme": [
-                "NOAA - SPACE WEATHER PROGRAM",
-                "LANCE",
-                "geospatial"
-            ],
-            "title": "VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375m NRT"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 1B1 Local Mode product;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This is the Local Mode Level 1B1 Product containing the DNs radiometrically scaled to radiances with no geometric resampling",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIB1LM_L1.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C179031461-LARC",
-            "issued": "2003-03-24",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIB1LM_L1.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2022-10-13",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2023-11-06T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 1B1 Local Mode Radiance Data V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1211784,54 +1210235,6 @@
             ],
             "title": "ROSETTA-ORBITER CRUISE 2 OSINAC 3 RDR\n                                      V1.4"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Radiance Product for a year; See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Radiance Product covering a year",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YRD_L3.005",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677738-LARC",
-            "issued": "2003-12-03",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YRD_L3.005",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Radiance Product covering a year V005"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1212066,6 +1210469,73 @@
             ],
             "title": "Low dose ionizing radiation treated lymphoblastoid cells"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "VCST Team. 2025-01-27. VIIRS/JPSS2 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath IP 750m NRT. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ202MOD_NRT.002. https://doi.org/10.5067/VIIRS/VJ202MOD_NRT.021.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VINCENT Chiang",
+                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
+            },
+            "creator": "VCST Team",
+            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Moderate Resolution 6-Min L1B Swath 750m, short-name VJ202MOD_NRT is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21; referred to hereafter as J2) platform-derived NASA VIIRS L1B calibrated radiances product that comprises of sixteen moderate-resolution or M-bands with a spatial resolution of 750-meters at nadir. These M-bands comprise eleven reflective solar bands (RSB) and five thermal emissive bands (TEB). Each of the M-bands has 16 detectors in the along-track direction with 16 rows of pixels per scan that provide a 750-m resolution. Ranging in wavelengths from 0.402 \u00b5m to 12.49 \u00b5m, the M-bands are sensitive to visible, near-, shortwave-, mediumwave-, and longwave-infrared wavelengths. Derived from the NASA VIIRS L1A raw radiances, this product includes calibrated and geolocated radiance and reflectance data, quality flags, and granule- and collection-level metadata. In contrast to a MODIS L1B product, which temporally spans 5 minutes, the VIIRS L1B calibrated radiances product contains a nominal temporal duration of 6 minutes. The image dimensions of the 750-m swath product measure 3232 lines by 3200 pixels.\n\nThe J2 VIIRS radiometric calibration Level-1B reprocessing includes a few calibration updates for the reflective solar bands (RSB), but no significant changes for the day-night band (DNB) or thermal emissive bands (TEB).  For more information download VIIRS Level 1 Product User's Guide at: \n\nhttps://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document Archive/Science Data Product Documentation/Processing and Algorithm Version History/NASA_VIIRS_L1B_UG_August_2021.pdf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202MOD_NRT.002",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5201/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C3383723948-LANCEMODIS",
+            "issued": "2025-01-25",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202MOD_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2025-01-27T00:00:00Z/2025-02-03T00:00:00Z",
+            "theme": [
+                "NOAA - SPACE WEATHER PROGRAM",
+                "LANCE",
+                "geospatial"
+            ],
+            "title": "VIIRS/JPSS2 Moderate Resolution 6-Min L1B Swath SDR 750m NRT"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1212654,54 +1211124,6 @@
             ],
             "title": "CASSINI E/J/S/SW CAPS UNCALIBRATED V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Aerosol product in netCDF format covering a year's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Aerosol product in netCDF format covering a year",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YAEN_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919893-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YAEN_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Aerosol product in netCDF format covering a year V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1217485,7 +1215907,7 @@
                 "hasEmail": "mailto:uso@asf.alaska.edu"
             },
             "creator": "OPERA",
-            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Radiometric Terrain Corrected (RTC) SAR Backscatter from Sentinel-1 (S1) validated product consists of radar backscatter normalized with respect to the topography. The product maps signals related to the physical properties of ground scattering objects, such as surface roughness and soil moisture and/or vegetation. The OPERA RTC-S1 product is derived from the original Copernicus Sentinel-1 Interferometric Wide (IW) Single Look Complex (SLC) data, provided by the European Space Agency, with a near global scope and temporal sampling coincident with the availability of S1 SLC data. Each OPERA RTC-S1 product corresponds to a single S1 burst projected onto a pre-defined UTM/Polar stereographic map projection system map grid with a 30-meter spacing. The Copernicus global 30 m (GLO-30) Digital Elevation Model (DEM) is the reference DEM used to correct for the impacts of topography and to geocode the product.  The OPERA RTC-S1 product is normalized to the backscatter coefficient gamma-naught, \u02630,  obtained from the original radar brightness beta-naught, \u03b20,  through radiometric terrain correction.  The RTC-S1 product is distributed as cloud optimized GeoTIFFs with one GeoTIFF file per processed polarization. The RTC-S1 product metadata is provided in the Hierarchical Data Format version 5 (HDF5) format. Due to the S1 mission\u2019s narrow orbital tube, radar-geometry layers such as incidence angle, local incidence angle, number of looks, and RTC Area Normalization Factor (ANF) vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA RTC-S1 product, as they are produced only once or a limited number of times, to account for changes in the DEM, in the S1 orbit, or in the static-layers generation algorithm. The static layers are available in the associated OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 Static Layers validated product (Version 1) dataset.",
+            "description": "The Observational Products for End-Users from Remote Sensing Analysis (OPERA) Radiometric Terrain Corrected (RTC) SAR Backscatter from Sentinel-1 (S1) validated product consists of radar backscatter normalized with respect to the topography. The product maps signals related to the physical properties of ground scattering objects, such as surface roughness and soil moisture and/or vegetation. The OPERA RTC-S1 product is derived from Copernicus Sentinel-1 Interferometric Wide (IW) Single Look Complex (SLC) data with a near global scope and temporal sampling coincident with the availability of S1 SLC data. \n\nEach OPERA RTC-S1 product corresponds to a single S1 burst projected onto a pre-defined UTM/Polar stereographic map projection system map grid with a 30-meter spacing. The Copernicus global 30 m (GLO-30) Digital Elevation Model (DEM) is the reference DEM used to correct for the impacts of topography and to geocode the product.  The OPERA RTC-S1 product is normalized to the backscatter coefficient gamma-naught, \u02630,  obtained from the original radar brightness beta-naught, \u03b20,  through radiometric terrain correction.  The RTC-S1 product is distributed as cloud optimized GeoTIFFs with one GeoTIFF file per processed polarization. The RTC-S1 product metadata is provided in the Hierarchical Data Format version 5 (HDF5) format. The OPERA RTC-S1 product contains modified Copernicus Sentinel data (2022-2025).\n\nDue to the S1 mission\u2019s narrow orbital tube, radar-geometry layers such as incidence angle, local incidence angle, number of looks, and RTC Area Normalization Factor (ANF) vary slightly over time for each position on the ground, and therefore are considered static. These static layers are provided separately from the OPERA RTC-S1 product, as they are produced only once or a limited number of times, to account for changes in the DEM, in the S1 orbit, or in the static-layers generation algorithm. The static layers are available in the associated OPERA Radiometric Terrain Corrected SAR Backscatter from Sentinel-1 Static Layers validated product (Version 1) dataset.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1217526,23 +1215948,23 @@
             "graphic-preview-description": "Image to represent the collection",
             "graphic-preview-file": "https://datapool.asf.alaska.edu/BROWSE/OPERA-S1/OPERA_L2_RTC-S1_T124-264306-IW2_20231027T043121Z_20231027T184651Z_S1A_30_v1.0_BROWSE.png",
             "identifier": "C2777436413-ASF",
-            "issued": "2021-01-01",
+            "issued": "2022-01-01",
             "keyword": [
-                "coastal processes",
-                "oceans",
+                "earth science",
                 "cryosphere",
-                "land surface",
                 "glaciers/ice sheets",
+                "land surface",
                 "geomorphic landforms/processes",
-                "earth science",
-                "tectonics",
-                "solid earth"
+                "solid earth",
+                "oceans",
+                "coastal processes",
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_RTC-S1_V1",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-27",
+            "modified": "2025-01-28",
             "programCode": [
                 "026:001"
             ],
@@ -1217554,7 +1215976,7 @@
                 "https://doi.org/10.1109/TGRS.2022.3147472"
             ],
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2021-01-01T00:00:00Z/2024-12-02T00:00:00Z",
+            "temporal": "2021-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "SNWG/OPERA",
                 "geospatial"
@@ -1218191,7 +1216613,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-16",
+            "modified": "2025-01-24",
             "programCode": [
                 "026:001"
             ],
@@ -1218200,7 +1216622,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-18T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2000-02-18T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1232096,16 +1230518,16 @@
             "identifier": "C1693440794-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
+                "earth science",
                 "spectral/engineering",
                 "infrared wavelengths",
-                "microwave",
-                "earth science"
+                "microwave"
             ],
             "landingPage": "https://doi.org/10.5067/9RRS80QCT0E9",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-01",
+            "modified": "2024-12-31",
             "programCode": [
                 "026:001"
             ],
@@ -1232124,7 +1230546,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "SNDRAQIL2CCPCCR",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-30T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2002-08-30T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -1232235,6 +1230657,73 @@
             ],
             "title": "NEW HORIZONS LORRI JUPITER ENCOUNTER V1.1"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "VCST Team. 2025-01-27. VIIRS/JPSS2 Dual Gain IP NRT. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ202GDC_NRT.021. https://doi.org/10.5067/VIIRS/VJ202GDC.021.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VINCENT Chiang",
+                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
+            },
+            "creator": "VCST Team",
+            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m product (VJ202GDC_NRT) contains unaggregated, calibrated TOA radiances for those VIIRS sub-pixel samples that are aggregated along-scan during post-calibration ground processing.  In other words, this file contains the calibrated M1 \u2013 M5, M7 and M13 dual gain band data from the nadir and near-nadir zones that would otherwise be discarded following post-calibration aggregation/Earth View Radiometric Calibration Unit.\r\n\r\nThe Level-1 and Level-2 swath products are generated from the processing of 6 minutes of VIIRS data acquired during theJPSS-2/NOAA-21 satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 &#181;m to 11.45 &#181;m. There are also 7 dual-gain VIIRS bands. The dual gain moderate resolution bands (M1 to M5, M7 and M13) have 6304 samples and the other moderate resolution bands have 3200.\r\n\r\nFor additional information, see the Operational Algorithm Description (OAD) Document for the L1B product at http://npp.gsfc.nasa.gov/sciencedocs/2015-08/474-00090_OAD-VIIRS-CAL-GEO-SDR_H.pdf. The document describes how VIIRS operates in space and provides the equations implemented by the L1B software to generate the MODIS Level-1 intermediate products. It is a summary document that presents the formulae and error budges used to transform VIIRS digital counts to radiance and reflectance.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202GDC_NRT.021",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5201/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C3383725663-LANCEMODIS",
+            "issued": "2024-01-10",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202GDC_NRT.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2025-01-24T00:00:00Z/2025-02-03T00:00:00Z",
+            "theme": [
+                "NOAA - SPACE WEATHER PROGRAM",
+                "LANCE",
+                "geospatial"
+            ],
+            "title": "VIIRS/JPSS2 Dual Gain IP NRT"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1232483,92 +1230972,6 @@
             ],
             "title": "MRO MARS CLIMATE SOUNDER LEVEL 5 DDR V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "2013-01-01. Archived by National Aeronautics and Space Administration, U.S. Government, ASDC. https://doi.org/10.5067/AURA/TES/TESTL3CO2M_L3. http://eosweb.larc.nasa.gov/project/tes/tes_table.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "SCOTT GLUCK",
-                "hasEmail": "mailto:Scott.Gluck@jpl.nasa.gov"
-            },
-            "description": "The TES Aura L3 CO2 data consist of daily atmospheric temperature and VMR for the atmospheric species. Data are provided at 2 degree latitude X 4 degree longitude spatial grids and at a subset of TES standard pressure levels. The TES Science Data Processing L3 subsystem interpolates the L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products are composed of L3 HDF - EOS-EOS grid data. A separate product file is produced for each different atmospheric species. TES obtains data in two basic observation modes: Limb or Nadir. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing are the terms Daily and Monthly representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey will not be split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represent a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products are daily and monthly. Details of the format of this product can be found in the TES Data Products Specifications (DPS) which is available from the LaRC ASDC site: http://eosweb.larc.nasa.gov/project/tes/DPS",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESTL3CO2M_L3",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://tes.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/project/tes/tes_table",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/project/tes/tes-quality-statements",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eospso.gsfc.nasa.gov/atbd-category/53",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://l5eil01.larc.nasa.gov/TES/TL3CO2M.003/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through its archiver."
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://reverb.echo.nasa.gov/reverb/#utf8=%E2%9C%93&spatial_map=satellite&spatial_type=rectangle&keywords=TL3CO2",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                }
-            ],
-            "identifier": "C189920636-LARC",
-            "issued": "2004-08-22",
-            "keyword": [
-                "atmospheric chemistry",
-                "air quality",
-                "atmosphere",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESTL3CO2M_L3",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2021-05-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-08-22T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "TES",
-                "geospatial"
-            ],
-            "title": "TES/Aura L3 CO2 Monthly Gridded V003"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1235160,216 +1233563,69 @@
                     "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
                     "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "Downloadable software applications"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc/misr_loc.html",
-                    "mediaType": "text/html",
-                    "title": "Use this dataset in a web based tool"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA EOS ATB Documents: MISR",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's algorithm theoretical basis document"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "How to cite ASDC data",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's data citation policy"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Overview of MISR Data at the ASDC, 2023",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Level 1 Production Report",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
-                    "mediaType": "text/html",
-                    "title": "Use this dataset in a web based tool"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Order and Customization Tool",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR/cgi-bin/MISR/main.cgi",
-                    "mediaType": "text/html",
-                    "title": "Use this dataset in a web based tool"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's data quality document"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR project home page",
-                    "downloadURL": "https://misr.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Overview of MISR Data Versioning Index",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's production history"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Data Product Specification for Specific Products MISR Data Products",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's product usage"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's production history"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's documented anomalies"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Quality Statements for Current Products",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's data quality document"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Data Product Specification for MISR Data Products",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents//misr/dps/misr_dps_dps.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's product usage"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's user's guide"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Direct Data Download for MI1B2T_004",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI1B2T.004/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "DOI data set landing page for MI1B2T_004",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MI1B2T_L1.004",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Peer-Reviewed Publications",
-                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's publications"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
-                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
-                    "mediaType": "text/html",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Data and Information for MISR",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "mediaType": "text/html",
-                    "title": "Visit this dataset's data center's home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "OPeNDAP data access for MI1B2T_004",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI1B2T.004/contents.html",
-                    "mediaType": "text/html",
-                    "title": "Use OPeNDAP to access the dataset's data"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Earthdata Search for MI1B2T_004",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2794373806-LARC",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Science Data Product Guide - May 7, 2012",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's product usage"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "TERRA Overview",
-                    "downloadURL": "https://terra.nasa.gov/about/terra-instruments/misr",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Paths Tool - Direct File Download (.kml)",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "title": "Downloadable software applications"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Overview of MISR Data at the ASDC, 2023",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR Data Versioning Index",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's production history"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for Specific Products MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's product usage"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's documented anomalies"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements for Current Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's data quality document"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents//misr/dps/misr_dps_dps.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's product usage"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MI1B2T_004",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI1B2T.004/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MI1B2T_004",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI1B2T.004/contents.html",
+                    "mediaType": "text/html",
+                    "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
             "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
@@ -1235378,14 +1233634,14 @@
             "issued": "2023-11-02",
             "keyword": [
                 "earth science",
-                "visible wavelengths",
-                "spectral/engineering"
+                "spectral/engineering",
+                "visible wavelengths"
             ],
             "landingPage": "https://doi.org/10.5067/TERRA/MISR/MI1B2T_L1.004",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-11",
+            "modified": "2024-12-13",
             "programCode": [
                 "026:001"
             ],
@@ -1235393,7 +1233649,7 @@
                 "@type": "org:Organization",
                 "name": "NASA/LARC/SD/ASDC"
             },
-            "temporal": "1999-12-18T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1999-12-18T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
@@ -1236970,14 +1235226,14 @@
             "issued": "2023-11-20",
             "keyword": [
                 "earth science",
-                "surface radiative properties",
-                "land surface"
+                "land surface",
+                "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VNP43IA2N.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1236987,7 +1235243,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -1241893,112 +1240149,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP013 RDR-INF-REFL V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "SAGE III/ISS Science Team (2022), SAGE III/ISS L1B Solar Event Transmission Data (HDF5), version 5.3, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.3",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dr. David Flittner",
-                "hasEmail": "mailto:david.e.flittner@nasa.gov"
-            },
-            "description": "g3bt_53 is the Stratospheric Aerosol and Gas Experiment III (SAGE III) on the International Space Station (ISS) (SAGE III/ISS) Level 1B Solar Event Transmission Data (HDF5) V053 data product. It contains pixel group transmission profiles for a single solar event. SAGE III was Launched on February 19, 2017 on a SpaceX Falcon 9 from Kennedy Space Center, SAGE III-ISS is the second instrument from the SAGE III project, externally mounted on the ISS. This ISS-based instrument uses a technique known as occultation, which involves looking at the light from the Sun or Moon as it passes through Earth's atmosphere at the edge, or limb, of the planet to provide long-term monitoring of ozone vertical profiles of the stratosphere and mesosphere. The data provided by SAGE III-ISS includes key components of atmospheric composition and their long-term variability, focusing on the study of aerosols, chlorine dioxide, clouds, nitrogen dioxide, nitrogen trioxide, pressure and temperature, and water vapor. SAGE data has historically been used by the World Meteorological Organization to inform their periodic assessments of ozone depletion. These new observations from the International Space Station will continue the SAGE team's contributions to ongoing scientific understanding of the Earth's atmosphere.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FSOLAR_HDF5_L1B-V5.3",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE project home page",
-                    "downloadURL": "https://sage.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.zip)",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/readers_G3B_v05.30.zip",
-                    "mediaType": "application/zip",
-                    "title": "Downloadable software applications"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "How to cite ASDC data",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "DOI data set landing page for g3bt_53",
-                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.3",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Version 5.30 DPUG (Data Product User's Guide)",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG_G3B_v05.30.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's user's guide"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Open Source Agreement for Computer Software",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Version 5.30 Release Notes",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/ReleaseNotes_G3B_v05.30.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Earthdata Search for g3bt_53 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2626885264-LARC",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                }
-            ],
-            "identifier": "C2626885264-LARC",
-            "issued": "2022-11-10",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
-            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.3",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2022-11-17",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2017-06-07T00:00:00Z/2023-04-10T00:00:00Z",
-            "theme": [
-                "SAGE III-ISS",
-                "geospatial"
-            ],
-            "title": "SAGE III/ISS L1B Solar Event Transmission Data (HDF5) V053"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1249703,7 +1247853,7 @@
                 {
                     "@type": "dcat:Distribution",
                     "description": "This link allows direct data access via Earthdata login",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/gedi/GEDI_L4A_AGB_Density_V2_1/",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/gedi/GEDI_L4A_AGB_Density_V2_1/data/",
                     "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
@@ -1249712,7 +1247862,7 @@
                     "description": "ORNL DAAC Data Set Documentation",
                     "downloadURL": "https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html",
                     "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
+                    "title": "View this dataset's user's guide"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -1249802,20 +1247952,20 @@
             "graphic-preview-description": "Example subset of aboveground biomass density (AGBD; Mg ha-1) predictions from the GEDI Level-4A footprint product over Northern California, U.S., spanning April to July 2019. GEDI footprints are spaced 60m along-track and 600m across-track.",
             "graphic-preview-file": "https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1_Fig1.png",
             "identifier": "C2237824918-ORNL_CLOUD",
-            "issued": "2023-11-03",
+            "issued": "2025-01-29",
             "keyword": [
-                "ecosystems",
                 "earth science",
                 "biosphere",
-                "spectral/engineering",
+                "ecosystems",
                 "vegetation",
+                "spectral/engineering",
                 "lidar"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/2056",
             "language": [
                 "en-US"
             ],
-            "modified": "2023-11-06",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1251127,18 +1249277,18 @@
             "identifier": "C1443528505-LAADS",
             "issued": "2017-11-01",
             "keyword": [
-                "national geospatial data asset",
+                "earth science",
                 "atmosphere",
                 "aerosols",
-                "earth science",
                 "atmospheric radiation",
-                "ngda"
+                "ngda",
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MYD04_3K.061",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1251148,7 +1249298,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:45:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:45:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -1267001,16 +1265151,16 @@
             "identifier": "C2619443894-POCLOUD",
             "issued": "2020-12-17",
             "keyword": [
+                "earth science",
                 "oceans",
                 "sea surface topography",
-                "ocean waves",
-                "earth science"
+                "ocean waves"
             ],
             "landingPage": "https://doi.org/10.5067/S6AP4-1BHNTR-F08",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-03",
+            "modified": "2025-01-10",
             "programCode": [
                 "026:001"
             ],
@@ -1267023,7 +1265173,7 @@
             ],
             "release-place": "PO.DAAC",
             "spatial": "-180.0 -66.15 180.0 66.15",
-            "temporal": "2020-11-30T14:26:00.875Z/2025-01-27T00:00:00Z",
+            "temporal": "2020-11-30T14:26:00.875Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
@@ -1271329,54 +1269479,6 @@
             ],
             "title": "SMEX04 Terra MODIS Data, Arizona, Version 1"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Land Product covering a month's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Land Product covering a month",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3MLS_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677721-LARC",
-            "issued": "2003-12-03",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3MLS_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Land Product covering a month V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1281195,7 +1279297,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO1BRAD Version 1 data product provides at-sensor calibrated radiance values retrieved for five thermal infrared (TIR) bands operating between 8 and 12.5 \u00b5m.  Additionally, the digital numbers (DN) for the shortwave infrared (SWIR) band are provided. The TIR bands are spatially co-registered to produce a variable spatial resolution between 70 meters (m) to 90 m at the edge of the swath. The ECO1BRAD data product is provided as swath data and does not contain geolocation information. The corresponding ECO1BGEO (https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001) data product is required to georeference the ECO1BRAD data product.  The geographic coverage of acquisitions for the ECO1BRAD Version 1 data product extends to areas outside of those indicated on the coverage map. However, corresponding higher-level products over these areas are not available at this time.\r\n\r\nThe ECO1BRAD Version 1 data product contains layers of radiance values for the five TIR bands, DN values for the SWIR band, associated data quality indicators, and ancillary data.\r\n\r\nKnown Issues: *Cannot perform spatial query on ECO1BRAD in NASA Earthdata Search: ECO1BRAD does not contain spatial attributes, so granules cannot be searched by geographic location. Users should search for ECO1BRAD data products by orbit number instead.\r\n*Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Missing scan data/striping features: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see section 3.3.2 of the User Guide.\r\n*Scan overlap: An overlap between ECOSTRESS scans results in a clear line overlap and repeating data. Additional information is available in section 3.2 of the User Guide.\r\n*Scan flipping: Improvements to the visualization of the data to compensate for instrument orientation are discussed in section 3.4 of the User Guide.\r\n*Cold bias: ECOSTRESS Level-1 Radiance data shows high correlation with in-situ ground measurements (R2 = 0.99 in all bands). Currently, ECOSTRESS has a cold bias of approximately 0.7 Kelvin (K), which will be corrected through calibration in fu",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECO1BRAD Version 1 data product provides at-sensor calibrated radiance values retrieved for five thermal infrared (TIR) bands operating between 8 and 12.5 microns. Additionally, the digital numbers (DN) for the shortwave infrared (SWIR) band are provided. The TIR bands are spatially co-registered to produce a variable spatial resolution between 70 meters (m) to 90 m at the edge of the swath. The ECO1BRAD data product is provided as swath data and does not contain geolocation information. The corresponding ECO1BGEO data product is required to georeference the ECO1BRAD data product. The geographic coverage of acquisitions for the ECO1BRAD Version 1 data product extends to areas outside of those indicated on the coverage map. However, corresponding higher-level products over these areas are not available at this time.\n\nThe ECO1BRAD Version 1 data product contains variables of radiance values for the five TIR bands, DN values for the SWIR band, associated data quality indicators, and ancillary data.\n\nKnown Issues\n\n* Cannot perform spatial query on ECO1BRAD in NASA Earthdata Search: ECO1BRAD does not contain spatial attributes, so granules cannot be searched by geographic location. Users should search for ECO1BRAD data products by orbit number instead.\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Missing scan data/striping features: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see Section 3.3.2 of the User Guide.\n* Scan overlap: An overlap between ECOSTRESS scans results in a clear line overlap and repeating data. Additional information is available in Section 3.2 of the User Guide.\n* Scan flipping: Improvements to the visualization of the data to compensate for instrument orientation are discussed in Section 3.4 of the User Guide.\n* Cold bias: ECOSTRESS Level-1 Radiance data shows high correlation with in-situ ground measurements (R2 = 0.99 in all bands). Currently, ECOSTRESS has a cold bias of approximately 0.7 Kelvin (K), which will be corrected through calibration in future data releases.\n* Data acquis",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1281265,21 +1279367,21 @@
                     "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View information related to this dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -1281308,15 +1279410,15 @@
             "identifier": "C1534582789-LPDAAC_ECS",
             "issued": "2019-03-27",
             "keyword": [
-                "spectral/engineering",
                 "earth science",
+                "spectral/engineering",
                 "infrared wavelengths"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO1BRAD.001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-09-04",
+            "modified": "2025-01-06",
             "programCode": [
                 "026:001"
             ],
@@ -1281327,7 +1279429,7 @@
             "release-place": "Sioux Falls, South Dakota, USA",
             "series-name": "ECO1BRAD.001",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-09-09T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-01-06T23:59:09Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -1316836,8 +1314938,8 @@
             "issued": "2016-01-01",
             "keyword": [
                 "earth science",
-                "geodetics",
                 "solid earth",
+                "geodetics",
                 "gravity/gravitational field",
                 "tectonics"
             ],
@@ -1316845,7 +1314947,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-11",
+            "modified": "2025-01-18",
             "programCode": [
                 "026:001"
             ],
@@ -1316854,7 +1314956,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2016-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2016-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
@@ -1329050,20 +1327152,20 @@
             "identifier": "C2791411861-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
-                "altitude",
                 "earth science",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric chemistry",
                 "atmosphere",
-                "air quality"
+                "air quality",
+                "altitude",
+                "atmospheric chemistry",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds"
             ],
             "landingPage": "https://doi.org/10.5067/2UUZUX6GJ49C",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-01",
+            "modified": "2024-12-31",
             "programCode": [
                 "026:001"
             ],
@@ -1329082,7 +1327184,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "SNDRAQIL2PLEVCPS",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2002-08-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -1333525,55 +1331627,6 @@
             ],
             "title": "TES/Aura L2 Carbon Monoxide Nadir V007"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESO3L_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C191856329-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "atmospheric chemistry/oxygen compounds",
-                "air quality",
-                "atmosphere",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESO3L_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 O3 Limb V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1335623,54 +1333676,6 @@
             ],
             "title": "SCATSAT-1 Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors Version 1.1"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Aerosol product in netCDF format covering a month's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Aerosol product in netCDF format covering a month",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3MAEN_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919889-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3MAEN_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Aerosol product in netCDF format covering a month V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1337184,7 +1335189,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Gregory Halverson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found on the ECOSTRESS website.\n\nThe ECOSTRESS Gridded Downscaled Soil Moisture Instantaneous L3 Global 70 m (ECO_L3G_SM) Version 2 data product provides instantaneous soil moisture (SM) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and SM from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. This data product is mosaicked from the L3 tiled SM (ECO_L3T_SM) product, is projected to a globally snapped 0.0006\u00b0 grid, and has a spatial resolution of 70 m.\n\nThe ECO_L3G_SM Version 2 data product contains three layers distributed in an HDF5 file including SM, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU, and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach, only Thermal Infrared (TIR) bands 2, 4, and 5 are being downloaded. The data products are the same as before, but the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\n-\tMissing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mask products (ECO_L2_CLOUD and ECO_L2G_CLOUD) to assess if a pixel is clear or cloudy (see section 3 of the User Guide).",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website.\n\nThe ECOSTRESS Gridded Downscaled Soil Moisture Instantaneous L3 Global 70 m (ECO_L3G_SM) Version 2 data product provides instantaneous soil moisture (SM) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and SM from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. This data product is mosaicked from the L3 tiled SM (ECO_L3T_SM) product, is projected to a globally snapped 0.0006 degree grid, and has a spatial resolution of 70 m.\n\nThe ECO_L3G_SM Version 2 data product contains three layers distributed in an HDF5 file including SM, cloud mask, and water mask.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU, and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach, only Thermal Infrared (TIR) bands 2, 4, and 5 are being downloaded. The data products are the same as before, but the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n* Missing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB, and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mask products (ECO_L2_CLOUD and ECO_L2G_CLOUD) to assess if a pixel is clear or cloudy (see Section 3 of the User Guide).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1337241,17 +1335246,17 @@
             "identifier": "C2074890845-LPCLOUD",
             "issued": "2024-04-29",
             "keyword": [
+                "earth science",
                 "land surface",
                 "surface thermal properties",
                 "climate indicators",
-                "land surface/agriculture indicators",
-                "earth science"
+                "land surface/agriculture indicators"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L3G_SM.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1337261,7 +1335266,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -1337503,54 +1335508,6 @@
             ],
             "title": "Spatial Statistical Data Fusion (SSDF) Level 3: CONUS Near-Surface Vapor Pressure Deficit from SNPP CrIMSS and Aqua AIRS, V2 (SNDR13IML3SSDFCVPD)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESHDOLS_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C191856316-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESHDOLS_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 HDO Limb Special Observation V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1343622,17 +1341579,17 @@
             "identifier": "C1511762113-CDDIS",
             "issued": "1998-01-01",
             "keyword": [
+                "earth science",
+                "solid earth",
                 "geodetics",
                 "gravity/gravitational field",
-                "earth science",
-                "tectonics",
-                "solid earth"
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSIONORTEC_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1343641,7 +1341598,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1998-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1998-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
@@ -1354996,104 +1352953,6 @@
             ],
             "title": "MSL MARS DESCENT IMAGER 4 RDR\n                                      VIDEO V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "Twilley, R., A. Fontenot-Cassaway, and A. Rovai. 2022. Delta-X: Feldspar Sediment Accretion Measurements, MRD, LA, USA, 2019-2023, Version 3. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2290",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@daac.ornl.gov"
-            },
-            "description": "This dataset provides elevation, hydrogeomorphic zone classification, soil carbon content, bulk density, organic matter content, and sediment accretion measurements collected at feldspar stations established near Louisiana's Coastwide Reference Monitoring Systems (CRMS) sites and on Mike Island in Wax Lake Delta (WLD). Feldspar stations were established to capture recent sediment deposition rates across hydrogeomorphic zones defined as discrete surface elevation ranges relative to NAVD88 (e.g., subtidal < -0.04 m, intertidal -0.04 m to 0.30 m, and supratidal > 0.30 m). Hydrogeomorphic zones classification was based on marsh surface elevations extracted from the U.S. Geological Survey (USGS) Atchafalaya 2 project LiDAR Survey 2012 digital elevation model and field GPS measurements in November - December 2020. Between two and three feldspar stations were deployed approximately 25 and 50 meters from the main channel to represent existing hydrogeomorphic zones in brackish and saline emergent marsh vegetation, tidal freshwater emergent marshes, and forested swamps. Cryocore technique was used to determine recent sediment deposition. Soil samples were collected to determine organic and inorganic fractions and organic carbon content. This dataset is from the Delta-X field studies conducted during Fall 2020, Spring 2021, Fall 2021, Spring 2022, Fall 2022, and Spring 2023.  The data are provided in comma-separated values (CSV) format.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2290",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "This link allows direct data access via Earthdata login",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Feldspar_Sediment_V3/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ORNL DAAC Data Set Documentation",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Feldspar_Sediment_V3.html",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Data set Landing Page DOI URL",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2290",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Delta-X: Feldspar Sediment Accretion Measurements, MRD, LA, USA, 2019-2023, Version 3: DeltaX_Feldspar_Sediment_V3.pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Feldspar_Sediment_V3/comp/DeltaX_Feldspar_Sediment_V3.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Top image: Cryocores showing sediment deposited on top of feldspar marker horizon; Bottom image: Feldspar station set up.",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Feldspar_Sediment_V3_Fig1.png",
-                    "mediaType": "image/png",
-                    "title": "Get a related visualization"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Delta-X Project Site",
-                    "downloadURL": "https://deltax.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                }
-            ],
-            "graphic-preview-description": "Top image: Cryocores showing sediment deposited on top of feldspar marker horizon; Bottom image: Feldspar station set up.",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Feldspar_Sediment_V3_Fig1.png",
-            "identifier": "C2840822190-ORNL_CLOUD",
-            "issued": "2024-01-18",
-            "keyword": [
-                "water quality/water chemistry",
-                "surface water",
-                "terrestrial hydrosphere",
-                "geomorphic landforms/processes",
-                "land surface",
-                "earth science",
-                "solid earth",
-                "soils"
-            ],
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2290",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2024-01-22",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "spatial": "-91.45 29.17 -90.82 29.56",
-            "temporal": "2019-10-04T00:00:00Z/2023-04-28T23:59:59Z",
-            "theme": [
-                "Delta-X",
-                "geospatial"
-            ],
-            "title": "Delta-X: Feldspar Sediment Accretion Measurements, MRD, LA, USA, 2019-2023, Version 3"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1377116,54 +1374975,6 @@
             ],
             "title": "MARINER 10 MERC POS M1 FLYBY TRAJ V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Albedo product covering a quarter (seasonal);See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "MISR Level 3 Component Global Albedo publicly available product covering a quarter (seasonal) to be used starting with MISR Release V3.2.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QAL_L3.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C61096008-LARC",
-            "issued": "2004-11-04",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QAL_L3.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Albedo product covering a quarter (seasonal) V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1382402,15 +1380213,15 @@
             "identifier": "C3026778309-LARC_ASDC",
             "issued": "2024-04-24",
             "keyword": [
-                "clouds",
                 "earth science",
-                "atmosphere"
+                "atmosphere",
+                "clouds"
             ],
             "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/CLOUDHEIGHT_L2.001",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-13",
+            "modified": "2025-01-24",
             "programCode": [
                 "026:001"
             ],
@@ -1382419,7 +1380230,7 @@
                 "name": "NASA/LARC/SD/ASDC"
             },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
-            "temporal": "2015-06-15T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2015-06-15T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "DSCOVR",
                 "geospatial"
@@ -1390061,6 +1387872,73 @@
             ],
             "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP002 RDR-STRLIGHT V1.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "VCST Team. 2025-01-27. VIIRS/JPSS2 Day/Night Band 6-Min L1B Swath SDR 750m NRT. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ202DNB_NRT.021. https://dx.doi.org/10.5067/VIIRS/VJ202DNB_NRT.021.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VINCENT Chiang",
+                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
+            },
+            "creator": "VCST Team",
+            "description": "The Near Real Time (NRT) VIIRS Level 1 and Level 2 swath (VJ202DNB_NRT) product is single NASA VIIRS panchromatic Day-Night band (DNB) calibrated radiance product. The DNB is one of the M-bands with an at-nadir spatial resolution of 750 meters (across the entire scan). The panchromatic DNB's spectral wavelength ranges from 0.5 \u00b5m to 0.9 \u00b5m. It facilitates measuring night lights, reflected solar/lunar lights with a large dynamic range between a low of a quarter moon illumination to the brightest daylight. The DNB attempts to maintain a nearly constant 750-m resolution over the entire 3060 km orbital swath by resorting to an on-board aggregation method, which also renders the calibration of the DNB a challenge. Stray-light and other sources of noise (lunar illuminance, twilight, clouds, noisy scan-edges, etc.) affect the DNB quality, and warrant correction.\n\nFor more information download VIIRS Level 1 Product User's Guide at:\nhttps://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document Archive/Science Data Product Documentation/Processing and Algorithm Version History/NASA_VIIRS_L1B_UG_August_2021.pdf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202DNB_NRT.021",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5201/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C3383724892-LANCEMODIS",
+            "issued": "2025-01-24",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202DNB_NRT.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2025-01-24T00:00:00Z/2025-02-03T00:00:00Z",
+            "theme": [
+                "NOAA - SPACE WEATHER PROGRAM",
+                "LANCE",
+                "geospatial"
+            ],
+            "title": "VIIRS/JPSS2 Day/Night Band 6-Min L1B Swath SDR 750m NRT"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1402610,7 +1400488,7 @@
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "description": "This dataset contains Level 1B (L1B) orthocorrected, scaled radiance image files as well as files of observational geometry and illumination parameters and supporting sensor band information from the Airborne Visible / Infrared Imaging Spectrometer (AVIRIS-Classic) instrument. This is the NASA Earth Observing System Data and Information System (EOSDIS) facility instrument archive of these data. The NASA AVIRIS-Classic is a pushbroom spectral mapping system with high signal-to-noise ratio (SNR), designed and toleranced for high performance spectroscopy. AVIRIS-Classic measures reflected radiance in 224 contiguous bands at approximately 10-nm intervals in the Visible to Shortwave Infrared (VSWIR) spectral range from 400-2500 nm. The AVIRIS-Classic sensor has a 1 milliradian instantaneous field of view, providing altitude dependent ground sampling distances from 20 m to sub meter range. AVIRIS-Classic is flown on a variety of aircraft platforms including the Twin Otter, NASA's WB-57, and NASA's high altitude ER-2. Multiple file types are included for each flight line. The primary data files include: orthocorrected calibrated radiance image (img) files, geometric lookup table (glt) and orthocorrected observation geometry and illumination (obs_ort) files. Also included are unprojected files of input geometry (igm), and parameters relating to the geometry of observation and illumination (obs). Additional files provide information on spectral (spc) and radiometric calibration (rcc, gain), spatial resolution (geo), aircraft and sensor position (eph, nav), deployment notes (info), and data processing (plog). Quicklook images (jpeg) and polygon outlines of imagery footprints (kmz) are provided for each flight line. The primary AVIRIS-Classic L1B data are provided in ENVI binary format, which includes a flat binary file accompanied by a header (.hdr) file holding metadata in text format. The ancillary files include JPEG images, maps in Keyhole Markup Language (KML), and calibration files in binary and text formats.This archive currently includes data from 2006 - 2021. Additional L1B data will be added as they become available. AVIRIS-Classic supports NASA Science and applications in many areas including plant composition and function, geology and soils, greenhouse gas mapping, and calibration of orbital platforms.",
+            "description": "This dataset contains Level 1B (L1B) orthocorrected, scaled radiance image files as well as files of observational geometry and illumination parameters and supporting sensor band information from the Airborne Visible / Infrared Imaging Spectrometer (AVIRIS-Classic) instrument. This is the NASA Earth Observing System Data and Information System (EOSDIS) facility instrument archive of these data. The NASA AVIRIS-Classic is a pushbroom spectral mapping system with high signal-to-noise ratio (SNR), designed and toleranced for high performance spectroscopy. AVIRIS-Classic measures reflected radiance in 224 contiguous bands at approximately 10-nm intervals in the Visible to Shortwave Infrared (VSWIR) spectral range from 400-2500 nm. The AVIRIS-Classic sensor has a 1 milliradian instantaneous field of view, providing altitude dependent ground sampling distances from 20 m to sub meter range. AVIRIS-Classic is flown on a variety of aircraft platforms including the Twin Otter, NASA's WB-57, and NASA's high altitude ER-2. Multiple file types are included for each flight line. The primary data files include: orthocorrected calibrated radiance image (img) files, geometric lookup table (glt) and orthocorrected observation geometry and illumination (obs_ort) files. Also included are unprojected files of input geometry (igm), and parameters relating to the geometry of observation and illumination (obs). Additional files provide information on spectral (spc) and radiometric calibration (rcc, gain), spatial resolution (geo), aircraft and sensor position (eph, nav), deployment notes (info), and data processing (plog). Quicklook images (jpeg) and polygon outlines of imagery footprints (kmz) are provided for each flight line. The primary AVIRIS-Classic L1B data are provided in ENVI binary format, which includes a flat binary file accompanied by a header (.hdr) file holding metadata in text format. The ancillary files include JPEG images, maps in Keyhole Markup Language (KML), and calibration files in binary and text formats. This archive currently includes data from 2004, and 2006 - 2024. Additional L1B data will be added as they become available. AVIRIS-Classic supports NASA Science and applications in many areas including plant composition and function, geology and soils, greenhouse gas mapping, and calibration of orbital platforms.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1402622,7 +1400500,7 @@
                 {
                     "@type": "dcat:Distribution",
                     "description": "This link allows direct data access via Earthdata login",
-                    "downloadURL": "https://daac.ornl.gov/aviris/AVIRIS-Classic_L1B_Radiance/",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/aviris/AVIRIS-Classic_L1B_Radiance/data/",
                     "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
@@ -1402631,7 +1400509,7 @@
                     "description": "ORNL DAAC Data Set Documentation",
                     "downloadURL": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS-Classic_L1B_Radiance.html",
                     "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
+                    "title": "View this dataset's user's guide"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -1402658,18 +1400536,18 @@
             "graphic-preview-description": "RGB composite image from AVIRIS-Classic flightline f170628t01p00r04 acquired on June 28 2017 northwest of Mojave, California.  Source: f170628t01p00r04_sc01_RGB.jpeg",
             "graphic-preview-file": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS-Classic_L1B_Radiance_Fig1.jpg",
             "identifier": "C2714723060-ORNL_CLOUD",
-            "issued": "2023-06-15",
+            "issued": "2025-01-28",
             "keyword": [
-                "visible wavelengths",
                 "earth science",
+                "spectral/engineering",
                 "infrared wavelengths",
-                "spectral/engineering"
+                "visible wavelengths"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/2155",
             "language": [
                 "en-US"
             ],
-            "modified": "2023-06-21",
+            "modified": "2025-02-03",
             "programCode": [
                 "026:001"
             ],
@@ -1402678,7 +1400556,7 @@
                 "name": "ORNL_DAAC"
             },
             "spatial": "-171.84 -0.03 -68.34 56.17",
-            "temporal": "2006-04-26T17:52:00Z/2021-04-02T23:16:00Z",
+            "temporal": "2004-08-25T00:00:00Z/2024-06-28T23:59:59Z",
             "theme": [
                 "AVIRIS",
                 "geospatial"
@@ -1404626,6 +1402504,73 @@
             ],
             "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 3 PHC V2.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "VCST Team. 2025-01-27. VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath IP 375m NRT. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ203IMG_NRT.021. https://doi.org/10.5067/VIIRS/VJ203IMG_NRT.021.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VINCENT Chiang",
+                "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
+            },
+            "creator": "VCST Team",
+            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath, short-name VJ203IMG_NRT is  the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-derived NASA VIIRS L1 terrain-corrected geolocation product and contains the derived line-of-sight (LOS) vectors for each of the 375-m image-resolution or I-bands. The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform's ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry. It produces geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel. The VJ203IMG product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, and quality flag for every pixel location. VJ203IMG provides a fundamental input to derive a number of VIIRS I-band higher-level products.\n\n\nThe J2 VIIRS geolocation underwent an on-orbit validation. Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands. The Day-Night band (DNB) geolocation error of about 2000 m was corrected. Further, the geolocation biases in the scan profile were also corrected. All these corrections bring the geolocation uncertainties for the J2 L1 products to within 75 m (1-sigma) in both the along-scan and along-track directions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203IMG_NRT.021",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5201/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through MODAPS"
+                }
+            ],
+            "identifier": "C3383706938-LANCEMODIS",
+            "issued": "2025-01-25",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203IMG_NRT.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2025-01-27T00:00:00Z/2025-02-03T00:00:00Z",
+            "theme": [
+                "NOAA - SPACE WEATHER PROGRAM",
+                "LANCE",
+                "geospatial"
+            ],
+            "title": "VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath IP 375m NRT"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1407774,6 +1405719,82 @@
             ],
             "title": "MCDONALD OBSERVATORY 9P/TEMPEL 1 DATA V1.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Weekly Polar-Gridded Landscape Freeze/Thaw Data V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/OV4R18NL3BQR.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "This Level-3 (L3) data set includes weekly Northern Hemisphere landscape freeze/thaw (FT) data derived from L-band radiometer brightness temperature observations, acquired by the Aquarius sensor on board Argentina's Sat\u00e9lite de Aplicaciones Cient\u00edficas (SAC-D) satellite. The data are distributed on the Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0), with a spatial resolution of 36 km. The SAC-D satellite was developed collaboratively between NASA and Argentina's space agency, Comisi\u00f3n Nacional de Actividades Espaciales (CONAE).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOV4R18NL3BQR",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_FT+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2777852942-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/OV4R18NL3BQR",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/OV4R18NL3BQR",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2777852942-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/OV4R18NL3BQR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 50.0 180.0 87.4",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-04T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Weekly Polar-Gridded Landscape Freeze/Thaw Data V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1415843,14 +1413864,14 @@
             "issued": "2023-11-20",
             "keyword": [
                 "earth science",
-                "surface radiative properties",
-                "land surface"
+                "land surface",
+                "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VJ143IA1N.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1415860,7 +1413881,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -1417425,54 +1415446,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P RPCLAP 5\nEXT2 DERIV2 V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Land Product covering a quarter's (seasonal) products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Land Product covering a quarter (seasonal)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QLS_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677728-LARC",
-            "issued": "2003-12-03",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QLS_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Land Product covering a quarter (seasonal) V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1431456,7 +1429429,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-02-02",
             "programCode": [
                 "026:001"
             ],
@@ -1431465,7 +1429438,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-08-30T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-08-30T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1456726,7 +1454699,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -1456736,7 +1454709,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2012-01-19T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2012-01-19T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -1458917,18 +1456890,18 @@
             "identifier": "C2938663471-NSIDC_CPRD",
             "issued": "2015-03-31",
             "keyword": [
-                "land surface",
-                "microwave",
-                "spectral/engineering",
                 "earth science",
-                "soils",
-                "radar"
+                "spectral/engineering",
+                "microwave",
+                "radar",
+                "land surface",
+                "soils"
             ],
             "landingPage": "https://doi.org/10.5067/ASB0EQO2LYJV",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-19",
+            "modified": "2025-01-27",
             "programCode": [
                 "026:001"
             ],
@@ -1458937,7 +1456910,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -60.0 180.0 60.0",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2015-03-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1463135,6 +1461108,115 @@
             ],
             "title": "GASKELL MIMAS SHAPE MODEL"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Twilley, R., A.F. Cassaway, A. Rovai, I.A. Vargas-Lopez, and J.A. Pineda-gomez. 2024. Delta-X: Feldspar Sediment Accretion Measurements, MRD, LA, USA, 2019-2023, Version 4. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2381",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@daac.ornl.gov"
+            },
+            "description": "This dataset provides elevation, hydrogeomorphic zone classification, soil carbon content, bulk density, organic matter content, and sediment accretion measurements collected at feldspar stations established near Louisiana's Coastwide Reference Monitoring Systems (CRMS) sites and on Mike Island in Wax Lake Delta (WLD). Feldspar stations were established to capture recent sediment deposition rates across hydrogeomorphic zones defined as discrete surface elevation ranges relative to NAVD88 (e.g., subtidal < -0.04 m, intertidal -0.04 m to 0.30 m, and supratidal > 0.30 m). Hydrogeomorphic zones classification was based on marsh surface elevation measurements acquired in November - December 2020 using a RTK GPS (Trible R12, using Geoid 18). Between two and four feldspar stations were deployed approximately 25 and 50 meters from a main channel to represent existing hydrogeomorphic zones in brackish and saline emergent marsh vegetation, brackish and saline ponds within emergent marshes, tidal freshwater emergent marshes, and forested swamps. Cryocore technique was used to determine recent sediment deposition. Soil samples were collected to determine organic and inorganic fractions and organic carbon content. The data cover the Delta-X field studies conducted from Fall 2020 through Fall 2023. The first feldspar markers were deployed in October of 2019. The data are provided in comma-separated values (CSV) format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2381",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Feldspar_Sediment_V4/data/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_Feldspar_Sediment_V4_2381.zip",
+                    "mediaType": "application/zip",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Feldspar_Sediment_V4.html",
+                    "mediaType": "text/html",
+                    "title": "View this dataset's user's guide"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2381",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_Feldspar_Sediment_V4_2381.zip",
+                    "mediaType": "application/zip",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Delta-X: Feldspar Sediment Accretion Measurements, MRD, LA, USA, 2019-2023, Version 4: DeltaX_Feldspar_Sediment_V4.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Feldspar_Sediment_V4/comp/DeltaX_Feldspar_Sediment_V4.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Top image: Cryocores showing sediment deposited on top of feldspar marker horizon; Bottom image: Feldspar station set up.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Feldspar_Sediment_V4_Fig1.png",
+                    "mediaType": "image/png",
+                    "title": "Get a related visualization"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Delta-X Project Site",
+                    "downloadURL": "https://deltax.jpl.nasa.gov/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                }
+            ],
+            "graphic-preview-description": "Top image: Cryocores showing sediment deposited on top of feldspar marker horizon; Bottom image: Feldspar station set up.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Feldspar_Sediment_V4_Fig1.png",
+            "identifier": "C3386847957-ORNL_CLOUD",
+            "issued": "2025-01-24",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "geomorphic landforms/processes",
+                "soils",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2381",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
+            "spatial": "-91.44 29.17 -90.82 29.56",
+            "temporal": "2019-10-04T12:00:00Z/2023-11-02T12:00:00Z",
+            "theme": [
+                "Delta-X",
+                "geospatial"
+            ],
+            "title": "Delta-X: Feldspar Sediment Accretion Measurements, MRD, LA, USA, 2019-2023, Version 4"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1479126,26 +1477208,26 @@
             "identifier": "C2790952275-GES_DISC",
             "issued": "2002-08-31",
             "keyword": [
-                "surface thermal properties",
-                "ocean temperature",
-                "oceans",
-                "land surface",
                 "earth science",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric chemistry",
                 "atmosphere",
-                "altitude",
                 "air quality",
-                "precipitation"
+                "altitude",
+                "atmospheric chemistry",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
+                "precipitation",
+                "land surface",
+                "surface thermal properties",
+                "oceans",
+                "ocean temperature"
             ],
             "landingPage": "https://doi.org/10.5067/WZVJ68EXNLK7",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-01",
+            "modified": "2024-12-31",
             "programCode": [
                 "026:001"
             ],
@@ -1479169,7 +1477251,7 @@
             "release-place": "Greenbelt, MD, USA",
             "series-name": "SNDRAQIL2CPS",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
+            "temporal": "2002-08-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
@@ -1482210,57 +1480292,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P MIRO 3 EXT1 V3.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "MISR Science Team (2018), Terra/MISR Level 3, Cloud Top Height-Optical Depth Product covering a day, version 1, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/TERRA/MISR/MIL3DCOD.001",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Roger Marchand",
-                "hasEmail": "mailto:rojmarch@u.washington.edu"
-            },
-            "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. This file contains the public MISR Level 3 Cloud Top Height-Optical Depth Product covering a day.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL3DCOD.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C1644916756-LARC",
-            "issued": "2018-08-06",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere"
-            ],
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL3DCOD.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2022-04-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-03-01T00:00:00Z/2022-05-03T00:00:00Z",
-            "theme": [
-                "MISR",
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Cloud Top Height-Optical Depth Product covering a day V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1482716,54 +1480747,6 @@
             ],
             "title": "GPM Ground Validation Dual-frequency Dual-polarized Doppler Radar (D3R) ICE POP V1"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Cloud Product covering a year's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the public MISR Level 3 Component Global Cloud Product covering a year",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YCLD_L3.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C84942920-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YCLD_L3.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Cloud Product covering a year V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1485606,54 +1483589,6 @@
             ],
             "title": "ALOS_PALSAR_LEVEL2.2"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Cloud Fraction by Altitude Product for a quarter (seasonal);See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the public MISR Level 3 Cloud Fraction by Altitude Product covering a quarter (seasonal)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QCFA_L3.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C188637670-LARC",
-            "issued": "2010-04-27",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QCFA_L3.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2017-10-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Cloud Fraction by Altitude Product covering a quarter (seasonal) V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1486373,54 +1484308,6 @@
             ],
             "title": "ROSETTA-ORBITER LUTETIA FLY-BY OSINAC 2 EDR V1.1"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Land product in netCDF format covering a day's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Land product in netCDF format covering a day",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DLSN_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919897-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DLSN_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Land product in netCDF format covering a day V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1490992,7 +1488879,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Gregory Halverson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found on the ECOSTRESS website.\nThe ECOSTRESS Tiled Downscaled Soil Moisture Instantaneous L3 Global 70 m (ECO_L3T_SM) Version 2 data product provides instantaneous soil moisture (SM) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and SM from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. The downscaled soil moisture estimates are recorded into the ECO_L3T_SM data product and tiled using a modified version of the Military Grid Reference System (MGRS), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 m spatial resolution.\nThe ECO_L3T_SM Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format, and each band is distributed as a separate COG. This product contains three layers including SM, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU, and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach, only Thermal Infrared (TIR) bands 2, 4, and 5 are being downloaded. The data products are the same as before, but the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\n-\tMissing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mask products (ECO_L2_CLOUD and ECO_L2G_CLOUD) to assess if a pixel is clear or cloudy (see section 3 of the User Guide).",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Tiled Downscaled Soil Moisture Instantaneous L3 Global 70 m (ECO_L3T_SM) Version 2 data product provides instantaneous soil moisture (SM) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and SM from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. The downscaled soil moisture estimates are recorded into the ECO_L3T_SM data product and tiled using a modified version of the Military Grid Reference System (MGRS) (https://hls.gsfc.nasa.gov/products-description/tiling-system/), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 m spatial resolution.\n\nThe ECO_L3T_SM Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format, and each band is distributed as a separate COG. This product contains three layers including SM, cloud mask, and water mask.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU, and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach, only Thermal Infrared (TIR) bands 2, 4, and 5 are being downloaded. The data products are the same as before, but the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n* Missing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB, and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mask products (ECO_L2_CLOUD and ECO_L2G_CLOUD) to assess if a pixel is clear or cloudy (see Section 3 of the User Gui",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1491056,17 +1488943,17 @@
             "identifier": "C2074860916-LPCLOUD",
             "issued": "2024-04-29",
             "keyword": [
+                "earth science",
                 "land surface",
-                "land surface/agriculture indicators",
-                "climate indicators",
                 "surface thermal properties",
-                "earth science"
+                "climate indicators",
+                "land surface/agriculture indicators"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L3T_SM.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1491076,7 +1488963,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -1492392,15 +1490279,15 @@
             "identifier": "C2808131488-LANCEMODIS",
             "issued": "2023-11-20",
             "keyword": [
-                "surface radiative properties",
                 "earth science",
-                "land surface"
+                "land surface",
+                "surface radiative properties"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VJ143MA1N.002",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1492410,7 +1490297,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -1494296,7 +1492183,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-03",
+            "modified": "2025-01-13",
             "programCode": [
                 "026:001"
             ],
@@ -1494309,7 +1492196,7 @@
             ],
             "release-place": "PO.DAAC",
             "spatial": "-180.0 -66.15 180.0 66.15",
-            "temporal": "2020-11-30T14:26:00.843Z/2025-01-27T00:00:00Z",
+            "temporal": "2020-11-30T14:26:00.843Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
@@ -1495092,7 +1492979,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1495102,7 +1492989,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
@@ -1503298,7 +1501185,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-17",
+            "modified": "2025-01-26",
             "programCode": [
                 "026:001"
             ],
@@ -1503308,7 +1501195,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-24T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2000-02-24T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
@@ -1505419,7 +1503306,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-02-03",
             "programCode": [
                 "026:001"
             ],
@@ -1505428,7 +1503315,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1998-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1998-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
@@ -1517841,16 +1515728,16 @@
             "identifier": "C1431413941-NSIDC_ECS",
             "issued": "2010-09-20",
             "keyword": [
-                "snow/ice",
                 "earth science",
+                "cryosphere",
                 "sea ice",
-                "cryosphere"
+                "snow/ice"
             ],
             "landingPage": "https://doi.org/10.5067/96JO0KIFDAS8",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-18",
+            "modified": "2024-12-25",
             "programCode": [
                 "026:001"
             ],
@@ -1517859,7 +1515746,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 55.0 180.0 90.0",
-            "temporal": "2010-09-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2010-09-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "MULTI_NASA",
                 "geospatial"
@@ -1521077,54 +1518964,6 @@
             ],
             "title": "Ground-Based Global Navigation Satellite System (GNSS) Beidou Broadcast Ephemeris Data (daily files) from NASA CDDIS"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Cloud Fraction by Altitude Product for a year;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the public MISR Level 3 Cloud Fraction by Altitude Product covering a year",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YCFA_L3.001",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C188637672-LARC",
-            "issued": "2010-04-27",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YCFA_L3.001",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2017-10-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Cloud Fraction by Altitude Product covering a year V001"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1523401,6 +1521240,134 @@
             ],
             "title": "Milling Wear"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "AIRS project. 2025-01-30. AIRSAQIRL1B_NRT. Version 8.0. AIRS/Aqua L1B Near Real Time (NRT) Infrared (IR) geolocated and calibrated radiances V8.0 (AIRSAQIRL1B_NRT) . Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/AIRSAQIRL1B_NRT_8.0.html. Digital Science Data.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lena Iredell",
+                "hasEmail": "mailto:lena.iredell@nasa.gov"
+            },
+            "creator": "AIRS project",
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The AIRS Infrared (IR) level 1B data set contains AIRS calibrated and geolocated radiances in milliWatts/m^2/cm^-1/steradian for 2378 infrared channels in the 3.74 to 15.4 micron region of the spectrum. \n\nThe AIRS Level 1B Near Real Time (NRT) product (AIRSIRAQL1B_NRT_v8.0) differs from the routine product (AIRSAQIRL1B_8) in 2 ways to meet the three hour latency requirements of the Land Atmosphere NRT Capability Earth Observing System (LANCE): (1) The NRT granules are produced without previous or subsequent granules if those granules are not available within 5 minutes, (2) the predictive ephemeris/attitude data are used rather than the definitive ephemeris/attitude. The consequences of these differences are described in the AIRS Near Real Time (NRT) data products document. \n\nThe products are stored in files (often referred to as \"granules\") that contain 6 minutes of data, 90 footprints across track by 135 lines along track.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Sample image of AIRSAQIRL1B_NRT",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRIBRAD_005.jpeg",
+                    "mediaType": "image/jpeg",
+                    "title": "Get a related visualization"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRSAQIRL1B_NRT_8.0.html",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRSAQIRL1B_NRT.8.0/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through a directory map"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_NRT/AIRSAQIRL1B_NRT.8.0/",
+                    "mediaType": "text/html",
+                    "title": "Use OPeNDAP to access the dataset's data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRSAQIRL1B_NRT+8.0",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument suite, algorithms, and other AIRS-related activities can be found.",
+                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "AIRS Documentation Page",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=AIRS+Documentation",
+                    "mediaType": "text/html",
+                    "title": "View information related to this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/README.AIRSAQIRL1B.v8.0.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's read me document"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Test Report, summary of validation status of products",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/AIRS_V8.0_L1B_Test_Report.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's data quality document"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "ATBD Documentation",
+                    "downloadURL": "https://eospso.nasa.gov/sites/default/files/atbd/AIRS_V8_L1B_ATBD.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's algorithm theoretical basis document"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Memo on NRT vs Standard Product",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.5_ProductQuality/nrt_memo_v6.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "graphic-preview-description": "Sample image of AIRSAQIRL1B_NRT",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRIBRAD_005.jpeg",
+            "identifier": "C3173404183-GES_DISC",
+            "issued": "2025-02-02",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "atmospheric chemistry",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3173404183-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRSAQIRL1B_NRT",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2025-02-03T00:00:00Z",
+            "theme": [
+                "Aqua",
+                "geospatial"
+            ],
+            "title": "AIRS/Aqua L1B Near Real Time (NRT) Infrared (IR) geolocated and calibrated radiances V8.0 (AIRSAQIRL1B_NRT) at GES DISC"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1532070,7 +1530037,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-09",
+            "modified": "2025-01-29",
             "programCode": [
                 "026:001"
             ],
@@ -1532079,7 +1530046,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-13T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1536650,7 +1534617,7 @@
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\nThe ECOSTRESS Swath Top of Atmosphere Calibrated Radiance Instantaneous L1B Global 70 m (ECO_L1B_RAD) Version 2 data product provides at-sensor calibrated radiance values retrieved for five thermal infrared (TIR) bands operating between 8 and 12.5 \u00b5m. Additionally, the digital numbers (DN) for the shortwave infrared (SWIR) band are provided. The TIR bands are spatially co-registered to produce a variable spatial resolution between 70 meters (m) and 90 m at the edge of the swath. The ECO_L1B_RAD data product is provided as swath data and does not contain geolocation information. The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L1B_RAD data product. The geographic coverage of acquisitions for the ECO_L1B_RAD Version 2 data product extends to areas outside of those indicated on the coverage map. \nThe ECO_L1B_RAD Version 2 data product contains layers of radiance values for the five TIR bands, DN values for the SWIR band, associated data quality indicators, and ancillary data distributed in HDF5 format.\n\nImprovements/Changes from Previous Versions\n\n-\tA radiance calibration has been applied to correct the ~1K cold bias that has been observed in previous studies. These values are described in Section 3 of the User Guide (https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf).\n\nKnown Issues\n\n-\tCannot perform spatial query on ECO_L1B_RAD in NASA Earthdata Search: ECO_L1B_RAD does not contain spatial attributes, so granules cannot be searched by geographic location. Users should search for ECO_L1B_RAD data products by orbit number instead.\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tMissing scan data/striping features: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see Section 3.3.2 of the User Guide (https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf).\n\n-\tScan overlap: An overlap between ECOSTRESS scans results in a clear line overlap and repeating data. Additional information is available in Section 3.2 of the User Guide (",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Swath Top of Atmosphere Calibrated Radiance Instantaneous L1B Global 70 m (ECO_L1B_RAD) Version 2 data product provides at-sensor calibrated radiance values retrieved for five thermal infrared (TIR) bands operating between 8 and 12.5 micons. Additionally, the digital numbers (DN) for the shortwave infrared (SWIR) band are provided. The TIR bands are spatially co-registered to produce a variable spatial resolution between 70 meters (m) and 90 m at the edge of the swath. The ECO_L1B_RAD data product is provided as swath data and does not contain geolocation information. The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L1B_RAD data product. The geographic coverage of acquisitions for the ECO_L1B_RAD Version 2 data product extends to areas outside of those indicated on the coverage map. \n\nThe ECO_L1B_RAD Version 2 data product contains layers of radiance values for the five TIR bands, DN values for the SWIR band, associated data quality indicators, and ancillary data distributed in HDF5 format.\n\nKnown Issues\n\n* Cannot perform spatial query on ECO_L1B_RAD in NASA Earthdata Search: ECO_L1B_RAD does not contain spatial attributes, so granules cannot be searched by geographic location. Users should search for ECO_L1B_RAD data products by orbit number instead.\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Missing scan data/striping features: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see Section 3.3.2 of the User Guide.\n* Scan overlap: An overlap between ECOSTRESS scans results in a clear line overlap and repeating data. Additional information is available in Section 3.2 of the User Guide. \n* Scan flipping: Improvements to the visualization of the data to compensate for instrument orientation are discussed in Section 3.4 of the User Guide. \n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1536748,7 +1534715,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2024-12-19",
+            "modified": "2025-01-31",
             "programCode": [
                 "026:001"
             ],
@@ -1536758,7 +1534725,7 @@
             },
             "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-12-23T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -1538944,54 +1536911,6 @@
             ],
             "title": "Mirador - Climate Variability and Change"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Cloud Motion Vector monthly Product in netCDF format;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Cloud Motion Vector monthly Product in netCDF format",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3MCMVN_L3.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C194517134-LARC",
-            "issued": "2012-08-16",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3MCMVN_L3.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2017-04-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Cloud Motion Vector monthly Product in netCDF format V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1539702,7 +1537621,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-16",
+            "modified": "2025-01-24",
             "programCode": [
                 "026:001"
             ],
@@ -1539711,7 +1537630,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2002-07-04T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1544283,16 +1542202,16 @@
             "issued": "2024-06-03",
             "keyword": [
                 "earth science",
-                "spectral/engineering",
                 "atmosphere",
                 "atmospheric radiation",
+                "spectral/engineering",
                 "infrared wavelengths"
             ],
             "landingPage": "https://doi.org/10.5067/PREFIRE-SAT2/PREFIRE/PAYLOAD-TLM_L0.R01",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1544304,7 +1542223,7 @@
                 "https://doi.org/10.1175/BAMS-D-20-0155.1"
             ],
             "spatial": "-180.0 -84.0 180.0 84.0",
-            "temporal": "2024-05-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-05-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "PREFIRE",
                 "geospatial"
@@ -1557264,7 +1555183,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-16",
+            "modified": "2025-01-24",
             "programCode": [
                 "026:001"
             ],
@@ -1557273,7 +1555192,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -85.044 180.0 85.044",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2015-03-31T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1562222,55 +1560141,6 @@
             ],
             "title": "IceBridge ATM L1B Elevation and Return Strength V002"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "MISR Science Team (2015), Terra/MISR Level 1B, Radiometric Camera-by-camera Cloud Mask, version 4, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/Terra/MISR/MIRCCM_L2.004",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Diner",
-                "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
-            },
-            "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR radiometric camera-by-camera Cloud Mask V004 contains the Radiometric camera-by-camera Cloud Mask dataset. It is used to determine whether a scene is classified as clear or cloudy. A new parameter has been added to indicate dust over ocean. This version of the ESDT is used by MISR PGE 13.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIRCCM_L2.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C73016614-LARC",
-            "issued": "2004-06-14",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIRCCM_L2.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2018-10-15",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-24T16:33:38Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "MISR",
-                "geospatial"
-            ],
-            "title": "MISR radiometric camera-by-camera Cloud Mask V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1585580,54 +1583450,6 @@
             ],
             "title": "Borehole and environmental protection descriptive and numerical data, Yamal Peninsula, Russia, Version 1"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Radiance Product for a month;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Radiance Product covering a month",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3MRD_L3.005",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C43677725-LARC",
-            "issued": "2003-12-03",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3MRD_L3.005",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Radiance Product covering a month V005"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1586862,41 +1584684,6 @@
                     "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "Downloadable software applications"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA EOS ATB Documents: MISR",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's algorithm theoretical basis document"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "How to cite ASDC data",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's data citation policy"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc/misr_loc.html",
-                    "mediaType": "text/html",
-                    "title": "Use this dataset in a web based tool"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Level 1 Production Report",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
-                    "mediaType": "text/html",
-                    "title": "Use this dataset in a web based tool"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's data quality document"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "Overview of MISR Data at the ASDC, 2023",
@@ -1586904,34 +1584691,6 @@
                     "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Order and Customization Tool",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR/cgi-bin/MISR/main.cgi",
-                    "mediaType": "text/html",
-                    "title": "Use this dataset in a web based tool"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR project home page",
-                    "downloadURL": "https://misr.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "TERRA Overview",
-                    "downloadURL": "https://terra.nasa.gov/about/terra-instruments/misr",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
@@ -1586953,20 +1584712,6 @@
                     "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "DOI data set landing page for MI1B2E_004",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MI1B2E_L1.004",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's production history"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
@@ -1586974,20 +1584719,6 @@
                     "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Peer-Reviewed Publications",
-                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's publications"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's user's guide"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "Data Product Specification for Specific Products MISR Data Products",
@@ -1587009,68 +1584740,12 @@
                     "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Data and Information for MISR",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "mediaType": "text/html",
-                    "title": "Visit this dataset's data center's home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
-                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
-                    "mediaType": "text/html",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Earthdata Search for MI1B2E_004",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2794373815-LARC",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View a micro article on this dataset"
-                },
                 {
                     "@type": "dcat:Distribution",
                     "description": "OPeNDAP data access for MI1B2E_004",
                     "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI1B2E.004/contents.html",
                     "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Science Data Product Guide - May 7, 2012",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's product usage"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "MISR Paths Tool - Direct File Download (.kml)",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "title": "Downloadable software applications"
                 }
             ],
             "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
@@ -1587078,18 +1584753,18 @@
             "identifier": "C2794373815-LARC",
             "issued": "2023-11-02",
             "keyword": [
-                "atmospheric pressure",
+                "earth science",
                 "atmosphere",
-                "spectral/engineering",
+                "atmospheric pressure",
                 "atmospheric temperature",
-                "earth science",
+                "spectral/engineering",
                 "visible wavelengths"
             ],
             "landingPage": "https://doi.org/10.5067/TERRA/MISR/MI1B2E_L1.004",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-23",
+            "modified": "2024-12-11",
             "programCode": [
                 "026:001"
             ],
@@ -1587097,7 +1584772,7 @@
                 "@type": "org:Organization",
                 "name": "NASA/LARC/SD/ASDC"
             },
-            "temporal": "1999-12-18T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "1999-12-18T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
@@ -1609634,125 +1607309,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P RPCICA 2 PRL UNCALIBRATED V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "2017-03-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/SAGEIII/SOLAR_BINARY_L1B-V5.2. https://asdc.larc.nasa.gov/project/SAGE%20III-ISS.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Flittner",
-                "hasEmail": "mailto:david.e.flittner@nasa.gov"
-            },
-            "description": "g3btb_52 is the Stratospheric Aerosol and Gas Experiment III (SAGE III) on the International Space Station (ISS) (SAGE III/ISS) Level 1B Solar Event Transmission Data (Native) V052data product. It contains pixel group transmission profiles for a single solar event. SAGE III was Launched on February 19, 2017 on a SpaceX Falcon 9 from Kennedy Space Center, SAGE III-ISS is the second instrument from the SAGE III project, externally mounted on the ISS. Data collection for this product is ongoing. \r\rThis ISS-based instrument uses a technique known as occultation, which involves looking at the light from the Sun or Moon as it passes through Earth's atmosphere at the edge, or limb, of the planet to provide long-term monitoring of ozone vertical profiles of the stratosphere and mesosphere. The data provided by SAGE III-ISS includes key components of atmospheric composition and their long-term variability, focusing on the study of aerosols, chlorine dioxide, clouds, nitrogen dioxide, nitrogen trioxide, pressure and temperature, and water vapor. SAGE data has historically been used by the World Meteorological Organization to inform their periodic assessments of ozone depletion. These new observations from the International Space Station will continue the SAGE team's contributions to ongoing scientific understanding of the Earth's atmosphere.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FSOLAR_BINARY_L1B-V5.2",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE project home page",
-                    "downloadURL": "https://sage.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "DOI data set landing page for g3btb_52",
-                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_BINARY_L1B-V5.2",
-                    "mediaType": "text/html",
-                    "title": "This dataset's landing page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.tar)",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/sageiii_iss_readers.tar",
-                    "mediaType": "application/x-tar",
-                    "title": "Downloadable software applications"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Data Products User\u2019s Guide, April 2021",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG-G3B.docx",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's user's guide"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "SAGE III/ISS Version 5.2 Release Notes",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/Release_Notes_v5.2.docx",
-                    "mediaType": "text/html",
-                    "title": "View an important notice for this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "How to cite ASDC data",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "mediaType": "text/html",
-                    "title": "View this dataset's data citation policy"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "NASA Open Source Agreement for Computer Software",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "View this dataset's product usage"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Data and Information for SAGE III-ISS",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/SAGE%20III-ISS",
-                    "mediaType": "text/html",
-                    "title": "View documentation related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Earthdata Search for g3btb_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2066317193-LARC",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "ASDC Direct Data Download for g3btb_52",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SAGE_III_ISS/g3btb.052/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset"
-                }
-            ],
-            "identifier": "C2066317193-LARC",
-            "issued": "2018-08-22",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
-                "atmosphere"
-            ],
-            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_BINARY_L1B-V5.2",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2019-06-19",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2017-06-07T00:00:00Z/2023-02-28T00:00:00Z",
-            "theme": [
-                "SAGE III-ISS",
-                "geospatial"
-            ],
-            "title": "SAGE III/ISS L1B Solar Event Transmission Data (Native) V052"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1616917,14 +1614473,14 @@
             "issued": "2024-06-05",
             "keyword": [
                 "earth science",
-                "atmospheric radiation",
-                "atmosphere"
+                "atmosphere",
+                "atmospheric radiation"
             ],
             "landingPage": "https://doi.org/10.5067/PREFIRE-SAT1/PREFIRE/BUS-TLM_L0.R01",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-01-30",
             "programCode": [
                 "026:001"
             ],
@@ -1616936,7 +1614492,7 @@
                 "https://doi.org/10.1175/BAMS-D-20-0155.1"
             ],
             "spatial": "-180.0 -84.0 180.0 84.0",
-            "temporal": "2024-06-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-06-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "PREFIRE",
                 "geospatial"
@@ -1617249,7 +1614805,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-20",
+            "modified": "2025-01-26",
             "programCode": [
                 "026:001"
             ],
@@ -1617257,7 +1614813,7 @@
                 "@type": "org:Organization",
                 "name": "CDDIS"
             },
-            "temporal": "2021-01-01T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2021-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1638173,7 +1635729,7 @@
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSCSSC_001.",
+            "citation": "International GNSS Service, GNSS Final Cumulative Combined Set of Station Coordinates Product, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi: 10.5067/GNSS/gnss_igscssc_001",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
@@ -1638205,7 +1635761,7 @@
                 {
                     "@type": "dcat:Distribution",
                     "description": "URL for more information about GNSS derived products",
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSCSSC_001",
+                    "downloadURL": "http://doi.org/10.5067/GNSS/GNSS_IGSCSSC_001",
                     "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
@@ -1638213,17 +1635769,17 @@
             "identifier": "C1501533138-CDDIS",
             "issued": "1992-01-01",
             "keyword": [
-                "geodetics",
                 "earth science",
-                "tectonics",
                 "solid earth",
-                "gravity/gravitational field"
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSCSSC_001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-11-23",
+            "modified": "2025-01-18",
             "programCode": [
                 "026:001"
             ],
@@ -1638232,7 +1635788,7 @@
                 "name": "CDDIS"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1992-01-01T00:00:00Z/2024-12-09T00:00:00Z",
+            "temporal": "1992-01-01T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
@@ -1642037,6 +1639593,98 @@
             ],
             "title": "MER MARS MOESSBAUER RELATIVE FE ABUNDANCE V1.0"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Aquarius L3 Weekly Polar-Gridded Normalized Radar Cross Section V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/Aquarius/AQ3_NRCS.005.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSIDC Services",
+                "hasEmail": "mailto:nsidc@nsidc.org"
+            },
+            "description": "The data set consists of weekly polar-gridded Level-3 products of Aquarius L-band Normalized Radar Cross Section (NRCS) retrievals from the Aquarius/Sat\u00e9lite de Aplicaciones Cient\u00edficas (SAC-D) mission, developed collaboratively between the U.S. National Aeronautics and Space Administration (NASA) and Argentina's space agency, Comisi\u00f3n Nacional de Actividades Espaciales (CONAE).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAquarius%2FAQ3_NRCS.005",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_NRCS+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2786542190-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_NRCS+V005",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through Earthdata Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2786542190-NSIDC_CPRD",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/Aquarius/AQ3_NRCS.005",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/Aquarius/AQ3_NRCS.005",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C2786542190-NSIDC_CPRD",
+            "issued": "2011-08-25",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "sea ice",
+                "spectral/engineering",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aquarius/AQ3_NRCS.005",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 -79.0 180.0 -50.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-04T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Aquarius L3 Weekly Polar-Gridded Normalized Radar Cross Section V005"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1644520,54 +1642168,6 @@
             ],
             "title": "ROSETTA-ORBITER EARTH MIRO 3 EAR1 EARTH1 V1.1"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Land product in netCDF format covering a year's products;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Land product in netCDF format covering a year",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YLSN_L3.004",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C108919901-LARC",
-            "issued": "2005-11-28",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YLSN_L3.004",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Land product in netCDF format covering a year V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1649099,55 +1646699,6 @@
             ],
             "title": "ROSETTA-ORBITER 67P OSINAC 3 EXT2-MTP029 RDR V3.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "Atmospheric vertical profile estimates and associated errors including the mapping matrix to relate the reduced-size retrieval vectors, covariances, and averaging kernels back to the TES forward model pressure grid.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2COLN_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C1000000340-LARC",
-            "issued": "2014-08-20",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry/carbon and hydrocarbon compounds",
-                "air quality",
-                "atmosphere"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2COLN_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 Carbon Monoxide Lite Nadir V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1654273,7 +1651824,7 @@
                 "hasEmail": "mailto:glynn.hulley@jpl.nasa.gov"
             },
             "creator": "Simon Hook, Glynn Hulley",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO2CLD Version 1 data product provides a cloud mask that can be used to determine cloud cover for the ECO1BRAD, ECO2LSTE, ECO3ETPTJPL, ECO4ESIPTJPL, and ECO4WUE data products. The ECOSTRESS Level 2 cloud product is derived using the five calibrated thermal bands in a multispectral cloud-conservative thresholding approach. The details of the algorithm are provided in the Algorithm Theoretical Basis Document (ATBD). The corresponding ECO1BGEO (https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001) data product is required to georeference the ECO2CLD data product.\r\n\r\nThe ECO2CLD Version 1 data product contains a single cloud mask layer. Information on how to interpret the bit fields in the cloud mask is provided in section 3.1 of the User Guide.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52 degrees N and 52 degrees S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECO2CLD Version 1 data product provides a cloud mask that can be used to determine cloud cover for the ECO1BRAD, ECO2LSTE, ECO3ETPTJPL, ECO4ESIPTJPL, and ECO4WUE data products. The ECOSTRESS Level 2 cloud product is derived using the five calibrated thermal bands in a multispectral cloud-conservative thresholding approach. The details of the algorithm are provided in the Algorithm Theoretical Basis Document (ATBD). The corresponding ECO1BGEO data product is required to georeference the ECO2CLD data product.\n\nThe ECO2CLD Version 1 data product contains a single cloud mask variable. Information on how to interpret the bit fields in the cloud mask is provided in section 3.1 of the User Guide.\n\nKnown Issues\n\n* Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n* Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n* Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1654336,14 +1651887,14 @@
                     "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View information related to this dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
                     "mediaType": "application/pdf",
-                    "title": "View documentation related to this dataset"
+                    "title": "View the documentation for this dataset's algorithms"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -1654361,7 +1651912,7 @@
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
                     "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
@@ -1654379,15 +1651930,15 @@
             "identifier": "C1534730833-LPDAAC_ECS",
             "issued": "2019-06-20",
             "keyword": [
+                "earth science",
                 "atmosphere",
-                "clouds",
-                "earth science"
+                "clouds"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO2CLD.001",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-09-03",
+            "modified": "2025-01-06",
             "programCode": [
                 "026:001"
             ],
@@ -1654398,7 +1651949,7 @@
             "release-place": "Sioux Falls, South Dakota, USA",
             "series-name": "ECO2CLD.001",
             "spatial": "-180.0 -54.0 180.0 54.0",
-            "temporal": "2018-07-09T00:00:00Z/2024-09-09T00:00:00Z",
+            "temporal": "2018-07-09T00:00:00Z/2025-01-06T23:59:09Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
@@ -1658337,15 +1655888,15 @@
             "identifier": "C2548345108-NSIDC_ECS",
             "issued": "2024-08-29",
             "keyword": [
-                "landscape",
                 "earth science",
-                "land surface"
+                "land surface",
+                "landscape"
             ],
             "landingPage": "https://doi.org/10.5067/ATLAS/ATL08QL.006",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-23",
+            "modified": "2025-02-02",
             "programCode": [
                 "026:001"
             ],
@@ -1658354,7 +1655905,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2024-08-29T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2024-08-29T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1670984,15 +1668535,15 @@
             "identifier": "C2559919423-NSIDC_ECS",
             "issued": "2018-10-14",
             "keyword": [
-                "land surface",
                 "earth science",
+                "land surface",
                 "topography"
             ],
             "landingPage": "https://doi.org/10.5067/ATLAS/ATL03.006",
             "language": [
                 "en-US"
             ],
-            "modified": "2024-10-08",
+            "modified": "2024-11-07",
             "programCode": [
                 "026:001"
             ],
@@ -1671001,7 +1668552,7 @@
                 "name": "NASA NSIDC DAAC"
             },
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2018-10-13T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2018-10-13T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
@@ -1676168,55 +1673719,6 @@
             ],
             "title": "PHOENIX MARS SURFACE STEREO IMAGER 4 LINEARIZED OPS V1.0"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "The TES Aura L3 CH4 data consist of monthly averages of atmospheric Methane for atmospheric species. Data are provided at 2 degree latitude X 4 degree longitude spatial grids and at a subset of TES standard pressure levels. The TES Science Data Processing L3 subsystem interpolates the L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products are composed of L3 HDF - EOS-EOS grid data. A separate product file is produced for each different atmospheric species. TES obtains data in two basic observation modes: Limb or Nadir. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing are the terms 'Daily' and 'Monthly' representing the approximate time coverage of the L3 products. However the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey will not be split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represent a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products are 'daily' and 'monthly'. L3 data is provided at uniform grids in latitude and longitude and at selected pressure levels. Details of the format of this product can be found in the TES Data Products Specifications (DPS) which is available from the LaRC ASDC site: http://eosweb.larc.nasa.gov/project/tes/DPS",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESTL3CH4M_L3",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "identifier": "C1000000660-LARC",
-            "issued": "2013-03-29",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "air quality",
-                "atmospheric chemistry/carbon and hydrocarbon compounds"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESTL3CH4M_L3",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-10-28",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "TES/Aura L3 CH4 Monthly Gridded V004"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1677586,92 +1675088,6 @@
             ],
             "title": "MISR L2 Surface Product subset for the SAMUM region V002"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "2013-01-01. Archived by National Aeronautics and Space Administration, U.S. Government, ASDC. https://doi.org/10.5067/AURA/TES/TL2NO2S_L2.006. http://eosweb.larc.nasa.gov/project/tes/tes_table.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "SCOTT GLUCK",
-                "hasEmail": "mailto:Scott.Gluck@jpl.nasa.gov"
-            },
-            "description": "The TES Aura L2 NO2 data consist of information for one molecular species for an entire Global Survey or Special Observation. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality and other data (e.g., surface characteristics for nadir observations) are also provided. L2 modeled spectra are evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compares observed spectra to the modeled spectra and iteratively updates the atmospheric parameters. L2 standard product files include information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consists of a maximum of 16 consecutive orbits. Nadir and limb observations are in separate L2 files, and a single ancillary file is composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey is a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations currently only use a single set of filter mix. A Limb sequence within the TES Global Survey is three high-resolution scans over the same limb locations. The Limb standard product will consist of four files, where each file will be composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations use a repeating sequence of filter wheel positions. Special Observations can only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and are conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depends on the science requirement. See http://tes.jpl.nasa.gov/instrument/specialobservations/ for details. A Global Survey consists of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals are performed (1,152 nadir retrievals and 1,152 retrievals in time ordered sequence for each limb observation). Each observation is the input for retrievals of species Volume Mixing Ratios (VMR), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density and other diagnostic quantities. Each TES Level 2 standard product reports information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object is bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product can have a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals are not reported. Each limb observation Limb 1, Limb 2 and Limb 3, are processed independently. Thus each limb standard product consists of three sets where each set consist of 1,152 observations. For TES, the swath object represents one of these sets. Thus each limb standard product consists of three swath objects, one for each observation, Limb 1, Limb 2, and Limb 3. The organization of data within the Swath object is based on a superset of the UARS pressure levels used to report concentrations of trace atmospheric gases. The reporting grid is the same pressure grid used for modeling. There are 67 reporting levels from 1211.53 hPa, which allows for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products will report values directly at the surface when po",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2NO2S_L2.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://tes.jpl.nasa.gov/",
-                    "mediaType": "text/html",
-                    "title": "The dataset's project home page"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/project/tes/tes_table",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/project/tes/tes-quality-statements",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eospso.gsfc.nasa.gov/atbd-category/53",
-                    "mediaType": "text/html",
-                    "title": "View information related to this dataset"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://l5eil01.larc.nasa.gov/TES/TL2NO2S.006/",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through its archiver."
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://reverb.echo.nasa.gov/reverb/#utf8=%E2%9C%93&spatial_map=satellite&spatial_type=rectangle&keywords=TL2NO2",
-                    "mediaType": "text/html",
-                    "title": "Download this dataset through Earthdata Search"
-                }
-            ],
-            "identifier": "C191856328-LARC",
-            "issued": "2004-08-22",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality",
-                "earth science"
-            ],
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2NO2S_L2.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2021-05-26",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ASDC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2004-08-22T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "TES",
-                "geospatial"
-            ],
-            "title": "TES/Aura L2 NO2 Limb Special Observation V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1688078,54 +1685494,6 @@
             ],
             "title": "Microbiological and nutritional analysis of lettuce crops grown on the International Space Station-VEG03A"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Albedo product covering a year;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "MISR Level 3 Component Global Albedo publicly available product covering a year to be used starting with MISR Release V3.2.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YAL_L3.006",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C61096037-LARC",
-            "issued": "2004-11-04",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YAL_L3.006",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Albedo product covering a year V006"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1693937,7 +1691305,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1693947,7 +1691315,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2021-09-16T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2021-09-16T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
@@ -1697688,7 +1695056,7 @@
             "language": [
                 "en-US"
             ],
-            "modified": "2025-02-11",
+            "modified": "2025-02-18",
             "programCode": [
                 "026:001"
             ],
@@ -1697698,7 +1695066,7 @@
             },
             "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
-            "temporal": "2023-11-20T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2023-11-20T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
@@ -1699951,20 +1697319,20 @@
             "identifier": "C1444143868-LAADS",
             "issued": "2017-10-01",
             "keyword": [
-                "spectral/engineering",
-                "national geospatial data asset",
-                "ngda",
-                "infrared wavelengths",
                 "earth science",
-                "atmospheric radiation",
                 "atmosphere",
-                "ultraviolet wavelengths"
+                "atmospheric radiation",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "ultraviolet wavelengths",
+                "ngda",
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MODCSR_8.061",
             "language": [
                 "en-US"
             ],
-            "modified": "2025-01-17",
+            "modified": "2025-01-26",
             "programCode": [
                 "026:001"
             ],
@@ -1699974,7 +1697342,7 @@
             },
             "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "2000-02-24T00:00:00Z/2025-01-27T00:00:00Z",
+            "temporal": "2000-02-24T00:00:00Z/2025-02-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
@@ -1704068,54 +1701436,6 @@
             ],
             "title": "TES/Aura L2 Ancillary Product V007"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Radiance Regional public Product covering a month;See ProductionDateTime for Published date.",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "User Representative",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
-            "description": "This file contains the MISR Level 3 Component Global Radiance Regional public Product covering a month",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3MRDR_L3.002",
-                    "mediaType": "text/html",
-                    "title": "Google Scholar search results"
-                }
-            ],
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "identifier": "C179031524-LARC",
-            "issued": "2006-03-01",
-            "keyword": [
-                "nasa"
-            ],
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3MRDR_L3.002",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2015-05-05",
-            "programCode": [
-                "026:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "MISR Level 3 Component Global Radiance Regional public Product covering a month V002"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
```

### Changes from 15bc04c to ee34c60
**Author:** Automated

**Date:** 2025-02-03 13:13:50+00:00

**Message:** Updated data: Mon Feb  3 13:13:50 UTC 2025

```diff
diff --git a/nasa.json b/nasa.json
index d857f46..5134a2c 100644
--- a/nasa.json
+++ b/nasa.json
@@ -5049,10 +5049,10 @@
             "identifier": "C3087325222-GES_DISC",
             "issued": "2024-05-15",
             "keyword": [
+                "atmosphere",
                 "air quality",
                 "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
+                "atmospheric chemistry"
             ],
             "landingPage": "https://doi.org/10.5067/KKPPL39PEIGE",
             "language": [
@@ -15909,8 +15909,8 @@
             "issued": "2021-04-29",
             "keyword": [
                 "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
+                "atmospheric chemistry",
+                "atmosphere"
             ],
             "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3513",
             "language": [
@@ -26863,13 +26863,13 @@
             "identifier": "C2086582256-GES_DISC",
             "issued": "2014-12-09",
             "keyword": [
+                "ultraviolet wavelengths",
                 "platform characteristics",
-                "atmospheric radiation",
-                "atmosphere",
                 "sensor characteristics",
-                "spectral/engineering",
                 "earth science",
-                "ultraviolet wavelengths"
+                "atmosphere",
+                "atmospheric radiation",
+                "spectral/engineering"
             ],
             "landingPage": "https://doi.org/10.5270/S5P-kb39wni",
             "language": [
@@ -37947,11 +37947,11 @@
             "identifier": "C2980782944-ORNL_CLOUD",
             "issued": "2024-05-04",
             "keyword": [
-                "atmospheric pressure",
-                "atmospheric temperature",
                 "earth science",
+                "atmosphere",
                 "altitude",
-                "atmosphere"
+                "atmospheric temperature",
+                "atmospheric pressure"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/73",
             "language": [
@@ -55220,8 +55220,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc1-edited-v1.0_2xyi-tp2h",
             "issued": "2018-06-26",
             "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC1-EDITED-V1.0",
             "modified": "2023-01-26",
@@ -74180,12 +74180,12 @@
             "identifier": "OCIO-Fitara-8",
             "issued": "2009-05-09",
             "keyword": [
-                "electronic",
-                "ocio",
-                "nasa it policy",
                 "it policy",
+                "electronic",
+                "chief information officer",
                 "information security",
-                "chief information officer"
+                "nasa it policy",
+                "ocio"
             ],
             "landingPage": "http://www.nasa.gov/content/it-policies-and-standards/#.VZFTzuuxEwB",
             "modified": "2020-01-29",
@@ -83646,10 +83646,10 @@
             "identifier": "https://data.nasa.gov/api/views/3gjn-n6ht",
             "issued": "2021-01-19",
             "keyword": [
-                "is",
                 "this",
+                "test",
                 "a",
-                "test"
+                "is"
             ],
             "landingPage": "https://data.nasa.gov/d/3gjn-n6ht",
             "modified": "2023-01-31",
@@ -90573,9 +90573,9 @@
             "identifier": "API-103",
             "issued": "2015-11-30",
             "keyword": [
-                "sound cloud file",
-                "space sounds",
                 "api",
+                "space sounds",
+                "sound cloud file",
                 "audio"
             ],
             "landingPage": "https://api.nasa.gov/api.html#sounds",
@@ -91439,8 +91439,8 @@
             "identifier": "TECHPORT_10766",
             "issued": "2010-12-01",
             "keyword": [
-                "active",
                 "project",
+                "active",
                 "wallops flight facility"
             ],
             "landingPage": "http://techport.nasa.gov/view/10766",
@@ -95098,18 +95098,18 @@
             "identifier": "C2254686682-ORNL_CLOUD",
             "issued": "2022-04-20",
             "keyword": [
-                "climate indicators",
-                "terrestrial hydrosphere indicators",
-                "soils",
-                "land surface/agriculture indicators",
                 "land surface",
-                "frozen ground",
-                "earth science",
-                "cryosphere",
-                "climate feedbacks",
-                "carbon flux",
+                "atmosphere",
                 "atmospheric chemistry",
-                "atmosphere"
+                "carbon flux",
+                "climate feedbacks",
+                "climate indicators",
+                "cryosphere",
+                "earth science",
+                "frozen ground",
+                "land surface/agriculture indicators",
+                "soils",
+                "terrestrial hydrosphere indicators"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/1872",
             "language": [
@@ -96402,10 +96402,10 @@
             "issued": "1999-08-04",
             "keyword": [
                 "earth science",
-                "solar activity",
-                "atmosphere",
                 "atmospheric radiation",
-                "sun-earth interactions"
+                "atmosphere",
+                "sun-earth interactions",
+                "solar activity"
             ],
             "landingPage": "https://doi.org/10.5067/ACRIMSAT/ACRIMIII/ACR3L2SC_L2.001",
             "language": [
@@ -101931,14 +101931,14 @@
             "identifier": "NASA-397",
             "issued": "2018-06-25",
             "keyword": [
-                "skylab",
+                "spacecraft",
                 "vehicles",
-                "3d model",
-                "rocket",
                 "satellite",
                 "saturn v",
+                "skylab",
+                "3d model",
                 "apollo",
-                "spacecraft"
+                "rocket"
             ],
             "landingPage": "http://nasa3d.arc.nasa.gov/detail/saturnv-c",
             "modified": "2020-01-29",
@@ -103735,24 +103735,24 @@
             "identifier": "C2954424032-OB_DAAC",
             "issued": "2022-09-13",
             "keyword": [
-                "biosphere",
+                "ocean optics",
                 "coastal processes",
-                "environmental advisories",
-                "earth science",
-                "oceans",
                 "water quality/water chemistry",
-                "terrestrial hydrosphere",
+                "earth science services",
+                "human dimensions",
                 "biological classification",
-                "ecosystems",
                 "surface water",
-                "earth science services",
+                "terrestrial hydrosphere",
+                "oceans",
+                "marine environment monitoring",
                 "aquatic sciences",
+                "environmental advisories",
                 "bacteria/archaea",
                 "hydrological advisories",
-                "marine environment monitoring",
                 "environmental governance/management",
-                "human dimensions",
-                "ocean optics"
+                "biosphere",
+                "ecosystems",
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/S3A/OLCI/L2/ILW/4",
             "language": [
@@ -103825,8 +103825,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v9.0_3u62-i5nw",
             "issued": "2018-06-26",
             "keyword": [
-                "asteroid",
-                "support archives"
+                "support archives",
+                "asteroid"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V9.0",
             "modified": "2023-01-26",
@@ -106663,24 +106663,24 @@
             "identifier": "NASA-0000091",
             "issued": "2018-06-25",
             "keyword": [
-                "operations",
                 "aeronautics",
-                "apollo",
-                "climate",
+                "literature",
                 "earth science",
-                "google",
-                "imagery",
                 "institutional",
-                "journal papers",
-                "literature",
                 "moon",
                 "naca",
+                "google",
+                "apollo",
+                "climate",
+                "imagery",
                 "nix",
-                "ntrs",
-                "pdf",
                 "space science",
+                "pdf",
                 "sti",
-                "technical reports"
+                "technical reports",
+                "operations",
+                "ntrs",
+                "journal papers"
             ],
             "landingPage": "https://data.nasa.gov/d/3vrm-5u9n",
             "modified": "2020-01-29",
@@ -107830,9 +107830,9 @@
             "identifier": "C2837624975-GES_DISC",
             "issued": "2023-01-09",
             "keyword": [
-                "atmosphere",
+                "earth science",
                 "atmospheric chemistry",
-                "earth science"
+                "atmosphere"
             ],
             "landingPage": "https://doi.org/10.5067/M2YSWFL9RSSH",
             "language": [
@@ -110692,20 +110692,20 @@
             "identifier": "C2574191901-POCLOUD",
             "issued": "2021-10-19",
             "keyword": [
-                "ocean chemistry",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "earth science",
-                "ocean circulation",
-                "ocean optics",
-                "oceans",
                 "ocean temperature",
                 "ocean waves",
                 "ocean winds",
-                "salinity/density"
+                "salinity/density",
+                "atmosphere",
+                "ocean circulation",
+                "ocean chemistry",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "ocean optics",
+                "oceans"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2574191901-POCLOUD.html",
             "language": [
@@ -115422,11 +115422,11 @@
             "issued": "2023-04-15",
             "keyword": [
                 "earth science",
+                "aerosols",
                 "atmosphere",
                 "air quality",
-                "aerosols",
-                "human dimensions",
-                "public health"
+                "public health",
+                "human dimensions"
             ],
             "landingPage": "https://doi.org/doi:10.5067/Q5ZFRUBCRWIW",
             "language": [
@@ -131747,14 +131747,14 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cvp2-checkout-v1.0",
             "issued": "2021-05-21",
             "keyword": [
-                "international rosetta mission",
-                "venus",
-                "vega",
-                "area 98",
-                "58 aql",
                 "m42",
+                "58 aql",
+                "16 cyg b",
+                "vega",
                 "earth",
-                "16 cyg b"
+                "venus",
+                "international rosetta mission",
+                "area 98"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CVP2-CHECKOUT-V1.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -143332,11 +143332,11 @@
             "identifier": "C2519119034-LPCLOUD",
             "issued": "2024-04-23",
             "keyword": [
-                "human dimensions",
                 "earth science",
+                "land use/land cover",
                 "land surface",
-                "environmental impacts",
-                "land use/land cover"
+                "human dimensions",
+                "environmental impacts"
             ],
             "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L3_DIST-ANN-HLS_V1.001",
             "language": [
@@ -145802,10 +145802,10 @@
             "issued": "2013-11-20",
             "keyword": [
                 "land surface",
+                "radar",
                 "spectral/engineering",
                 "topography",
-                "earth science",
-                "radar"
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/MEASURES/SRTM/SRTMGL1_NC.003",
             "language": [
@@ -151538,9 +151538,9 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-3-ear2-calibrated-v9.0_4qw2-yje9",
             "issued": "2021-05-21",
             "keyword": [
+                "international rosetta mission",
                 "checkout",
-                "earth",
-                "international rosetta mission"
+                "earth"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-3-EAR2-CALIBRATED-V9.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -152389,9 +152389,9 @@
             "identifier": "C1220566178-USGS_LTA",
             "issued": "1960-07-31",
             "keyword": [
+                "visible wavelengths",
                 "earth science",
                 "infrared wavelengths",
-                "visible wavelengths",
                 "spectral/engineering"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566178-USGS_LTA.html",
@@ -155447,10 +155447,10 @@
             "identifier": "API-23",
             "issued": "2015-11-30",
             "keyword": [
-                "open government",
-                "api",
                 "open data",
-                "agency management operations"
+                "agency management operations",
+                "open government",
+                "api"
             ],
             "landingPage": "https://data.nasa.gov/api-documents/foundry/#/data.nasa.gov/fk38-4khf",
             "modified": "2020-01-29",
@@ -165008,8 +165008,8 @@
             "issued": "2018-06-25",
             "keyword": [
                 "crew lock bag",
-                "3d model",
                 "shuttle",
+                "3d model",
                 "astronaut"
             ],
             "landingPage": "http://nasa3d.arc.nasa.gov/detail/crew-lock-bag",
@@ -207264,8 +207264,8 @@
             "keyword": [
                 "spalart",
                 "models",
-                "allmaras",
-                "turbulence"
+                "turbulence",
+                "allmaras"
             ],
             "landingPage": "http://turbmodels.larc.nasa.gov/spalart.html",
             "modified": "2020-01-29",
@@ -210715,8 +210715,8 @@
             "identifier": "urn:nasa:pds:compil.ast.masses",
             "issued": "2021-05-21",
             "keyword": [
-                "none",
-                "multiple asteroids"
+                "multiple asteroids",
+                "none"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acompil.ast.masses&version=1.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -232453,11 +232453,11 @@
             "identifier": "https://data.nasa.gov/api/views/68sc-yhe3",
             "issued": "2020-11-18",
             "keyword": [
-                "imerg",
                 "cloud regime",
+                "precipitation",
                 "cloud-precipitation hybrid regime",
+                "imerg",
                 "cloud",
-                "precipitation",
                 "modis"
             ],
             "landingPage": "https://data.nasa.gov/d/68sc-yhe3",
@@ -236060,15 +236060,15 @@
             "identifier": "C1220567084-USGS_LTA",
             "issued": "1972-08-09",
             "keyword": [
+                "earth science",
+                "land surface",
                 "land use/land cover",
-                "surface thermal properties",
-                "surface radiative properties",
-                "spectral/engineering",
-                "sensor characteristics",
-                "ngda",
                 "national geospatial data asset",
-                "land surface",
-                "earth science"
+                "ngda",
+                "sensor characteristics",
+                "spectral/engineering",
+                "surface radiative properties",
+                "surface thermal properties"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567084-USGS_LTA.html",
             "language": [
@@ -236230,14 +236230,14 @@
             "identifier": "C2142776747-LPCLOUD",
             "issued": "2021-07-27",
             "keyword": [
-                "spectral/engineering",
-                "sensor characteristics",
                 "lidar",
+                "topography",
+                "spectral/engineering",
                 "biosphere",
                 "earth science",
-                "land surface",
                 "vegetation",
-                "topography"
+                "sensor characteristics",
+                "land surface"
             ],
             "landingPage": "https://doi.org/10.5067/GEDI/GEDI02_B.002",
             "language": [
@@ -253383,9 +253383,9 @@
             "identifier": "C1997469066-LARC_ASDC",
             "issued": "2020-11-18",
             "keyword": [
-                "atmospheric chemistry",
+                "atmosphere",
                 "earth science",
-                "atmosphere"
+                "atmospheric chemistry"
             ],
             "landingPage": "https://doi.org/10.5067/Suborbital/OWLETS-2/Ship_Data_1",
             "language": [
@@ -264252,9 +264252,9 @@
             "identifier": "DASHLINK_565",
             "issued": "2012-04-02",
             "keyword": [
+                "nasa",
                 "dashlink",
-                "ames",
-                "nasa"
+                "ames"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/565/",
             "modified": "2020-01-29",
@@ -265923,11 +265923,11 @@
             "identifier": "C2408034484-LPCLOUD",
             "issued": "2023-06-07",
             "keyword": [
-                "soils",
-                "rocks/minerals/crystals",
                 "earth science",
+                "soils",
+                "land surface",
                 "solid earth",
-                "land surface"
+                "rocks/minerals/crystals"
             ],
             "landingPage": "https://doi.org/10.5067/EMIT/EMITL2BMIN.001",
             "language": [
@@ -271607,8 +271607,8 @@
             "identifier": "DASHLINK_732",
             "issued": "2013-05-09",
             "keyword": [
-                "dashlink",
                 "nasa",
+                "dashlink",
                 "ames"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/732/",
@@ -282504,11 +282504,11 @@
             "identifier": "API-104",
             "issued": "2015-11-30",
             "keyword": [
-                "nea",
                 "asteroid",
+                "nea",
                 "api",
-                "neo",
-                "trajectory"
+                "trajectory",
+                "neo"
             ],
             "landingPage": "https://api.nasa.gov/api.html#NeoWS",
             "modified": "2020-01-29",
@@ -282880,9 +282880,9 @@
             "identifier": "DASHLINK_120",
             "issued": "2010-09-10",
             "keyword": [
-                "ames",
                 "dashlink",
-                "nasa"
+                "nasa",
+                "ames"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/120/",
             "modified": "2020-01-29",
@@ -284151,12 +284151,12 @@
             "identifier": "C3336442614-NSIDCV0",
             "issued": "2000-03-01",
             "keyword": [
+                "earth science",
                 "snow/ice",
-                "national geospatial data asset",
-                "ngda",
                 "terrestrial hydrosphere",
                 "cryosphere",
-                "earth science"
+                "national geospatial data asset",
+                "ngda"
             ],
             "landingPage": "https://doi.org/10.7265/f6j3-f387",
             "language": [
@@ -294466,10 +294466,10 @@
             "identifier": "C1990404810-POCLOUD",
             "issued": "2021-01-01",
             "keyword": [
-                "earth science services",
                 "earth science",
-                "earth science reanalyses/assimilation models",
                 "oceans",
+                "earth science services",
+                "earth science reanalyses/assimilation models",
                 "ocean circulation",
                 "models"
             ],
@@ -302608,9 +302608,9 @@
             "identifier": "C2623698025-NSIDC_ECS",
             "issued": "2015-04-01",
             "keyword": [
+                "land surface",
                 "soils",
-                "earth science",
-                "land surface"
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/U8QZ2AXE5V7B",
             "language": [
@@ -308983,11 +308983,11 @@
             "identifier": "C2738888256-LAADS",
             "issued": "2022-08-02",
             "keyword": [
-                "surface radiative properties",
-                "land surface",
+                "earth science",
                 "infrared wavelengths",
+                "surface radiative properties",
                 "spectral/engineering",
-                "earth science"
+                "land surface"
             ],
             "landingPage": "https://doi.org/10.5067/AVHRR/N07_AVH09C1.006",
             "language": [
@@ -323962,16 +323962,16 @@
             "identifier": "C1235542031-USGS_LTA",
             "issued": "2013-02-11",
             "keyword": [
-                "landscape",
-                "visible wavelengths",
-                "surface radiative properties",
+                "land use/land cover",
+                "sensor characteristics",
                 "spectral/engineering",
+                "surface radiative properties",
+                "visible wavelengths",
+                "landscape",
+                "land surface",
                 "earth science",
                 "geomorphic landforms/processes",
-                "infrared wavelengths",
-                "land surface",
-                "land use/land cover",
-                "sensor characteristics"
+                "infrared wavelengths"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1235542031-USGS_LTA.html",
             "language": [
@@ -333834,10 +333834,10 @@
             "identifier": "C2396938169-ORNL_CLOUD",
             "issued": "2024-05-01",
             "keyword": [
-                "land surface",
-                "topography",
                 "spectral/engineering",
                 "lidar",
+                "land surface",
+                "topography",
                 "earth science"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/1518",
@@ -334295,13 +334295,13 @@
             "identifier": "C3235688636-ORNL_CLOUD",
             "issued": "2024-09-06",
             "keyword": [
+                "land use/land cover",
+                "human dimensions",
                 "environmental governance/management",
-                "earth science",
                 "land surface",
                 "ecosystems",
-                "land use/land cover",
-                "biosphere",
-                "human dimensions"
+                "earth science",
+                "biosphere"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/2367",
             "language": [
@@ -358670,8 +358670,8 @@
             "issued": "2015-10-14",
             "keyword": [
                 "fungal",
-                "phenotypic",
-                "pathogen"
+                "pathogen",
+                "phenotypic"
             ],
             "landingPage": "https://data.nasa.gov/d/8e7s-kdza",
             "modified": "2023-01-31",
@@ -378232,9 +378232,9 @@
             "identifier": "NASA-834",
             "issued": "2018-06-25",
             "keyword": [
-                "turbulence",
                 "models",
-                "wilcox"
+                "wilcox",
+                "turbulence"
             ],
             "landingPage": "http://turbmodels.larc.nasa.gov/wilcox.html",
             "modified": "2020-01-29",
@@ -379081,12 +379081,12 @@
             "identifier": "C2896484540-OB_DAAC",
             "issued": "2013-01-04",
             "keyword": [
-                "ocean optics",
-                "earth science",
-                "ocean temperature",
+                "ocean chemistry",
                 "salinity/density",
+                "ocean temperature",
+                "earth science",
                 "oceans",
-                "ocean chemistry"
+                "ocean optics"
             ],
             "landingPage": "https://doi.org/10.5067/SeaBASS/CAML/DATA001",
             "language": [
@@ -397858,13 +397858,13 @@
             "identifier": "API-105",
             "issued": "2015-11-30",
             "keyword": [
+                "camera",
                 "api",
                 "photo",
+                "martian",
                 "images",
-                "camera",
                 "planetary science research",
-                "imagery",
-                "martian"
+                "imagery"
             ],
             "landingPage": "https://api.nasa.gov/",
             "modified": "2020-06-08",
@@ -403161,16 +403161,16 @@
             "identifier": "NASA-0000228",
             "issued": "2018-06-25",
             "keyword": [
-                "pulsars",
-                "space science",
-                "light arcs",
+                "solar flares",
                 "fermi",
                 "gamma-ray bursts",
                 "gbm",
                 "lat",
-                "photons",
-                "solar flares",
+                "light arcs",
                 "particle physics",
+                "photons",
+                "pulsars",
+                "space science",
                 "astrophysics"
             ],
             "landingPage": "https://data.nasa.gov/d/95b6-teh2",
@@ -409011,9 +409011,9 @@
             "identifier": "DASHLINK_713",
             "issued": "2013-04-26",
             "keyword": [
-                "nasa",
                 "ames",
-                "dashlink"
+                "dashlink",
+                "nasa"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/713/",
             "modified": "2020-01-29",
@@ -411620,8 +411620,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-alice-3-pluto-v1.0_9ask-q7fv",
             "issued": "2021-05-21",
             "keyword": [
-                "pluto",
                 "sun",
+                "pluto",
                 "new horizons"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-ALICE-3-PLUTO-V1.0",
@@ -418497,18 +418497,18 @@
             "identifier": "NASA-0000104",
             "issued": "2018-06-25",
             "keyword": [
-                "planetary data system",
-                "space science",
-                "laboratory",
-                "mapping",
                 "planetary science",
+                "mapping",
+                "pds",
+                "astronomical observation",
+                "planetary data system",
                 "circulation",
                 "images",
-                "proposals",
-                "pds",
+                "laboratory",
+                "space science",
                 "planetary missions",
-                "planetary science research",
-                "astronomical observation"
+                "proposals",
+                "planetary science research"
             ],
             "landingPage": "https://data.nasa.gov/d/9epu-76zj",
             "modified": "2021-07-02",
@@ -432363,12 +432363,12 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rosina-2-cr5-v2.0_9pbi-5qet",
             "issued": "2018-06-26",
             "keyword": [
-                "international rosetta mission",
+                "earth",
                 "unknown",
-                "21 lutetia",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "earth",
-                "2867 steins"
+                "21 lutetia",
+                "2867 steins",
+                "international rosetta mission"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ROSINA-2-CR5-V2.0",
             "modified": "2023-01-26",
@@ -436303,9 +436303,9 @@
             "issued": "2022-01-03",
             "keyword": [
                 "atmospheric chemistry",
+                "earth science",
                 "air quality",
-                "atmosphere",
-                "earth science"
+                "atmosphere"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/1927",
             "language": [
@@ -439722,22 +439722,22 @@
             "identifier": "NASA-0000082",
             "issued": "2018-06-25",
             "keyword": [
-                "land temperature",
-                "land height",
-                "atmospheric radiation",
-                "climate",
+                "ice",
+                "snow",
+                "geodata",
+                "terrestrial water",
                 "soil",
                 "clouds",
-                "snow",
+                "climate",
+                "atmospheric radiation",
+                "mirador",
                 "rain",
+                "land height",
+                "land temperature",
                 "precipitation",
-                "geodata",
-                "ges disc",
-                "mirador",
-                "terrestrial water",
                 "heat flux",
-                "ice",
-                "surface radiation"
+                "surface radiation",
+                "ges disc"
             ],
             "landingPage": "http://mirador.gsfc.nasa.gov/cgi-bin/mirador/presentNavigation.pl?tree=scienceArea&scienceArea=Water%20and%20Energy%20Cycles",
             "modified": "2020-01-29",
@@ -445189,28 +445189,28 @@
             "issued": "2018-06-26",
             "keyword": [
                 "p-gse8573-7",
-                "p-gse8573-12",
-                "p-gse8573-11",
-                "p-gse8573-10",
-                "p-gse8573-1",
-                "nucleic_acid_extraction",
-                "labeling",
+                "p-gse8573-6",
+                "p-gse8573-5",
                 "image_aquisition",
-                "hybridization",
-                "gravity",
-                "p-gse8573-13",
+                "p-gse8573-4",
                 "feature_extraction",
-                "p-gse8573-14",
-                "bioassay_data_transformation",
                 "absorbed radiation dose",
+                "p-gse8573-9",
+                "p-gse8573-11",
+                "gravity",
+                "nucleic_acid_extraction",
+                "p-gse8573-14",
                 "p-gse8573-2",
                 "p-gse8573-3",
-                "p-gse8573-4",
-                "p-gse8573-5",
-                "p-gse8573-6",
+                "bioassay_data_transformation",
                 "p-gse8573-8",
-                "p-gse8573-9",
-                "radiation dosimetry"
+                "radiation dosimetry",
+                "p-gse8573-10",
+                "p-gse8573-13",
+                "p-gse8573-12",
+                "p-gse8573-1",
+                "labeling",
+                "hybridization"
             ],
             "landingPage": "https://data.nasa.gov/d/9wp5-r7cc",
             "modified": "2023-01-26",
@@ -466844,16 +466844,16 @@
             "identifier": "nasa-iss-data_2021-12-18_ab4w-qgv8",
             "issued": "2021-12-18",
             "keyword": [
-                "coordinates",
-                "topo",
-                "trajectory",
                 "space",
+                "location",
                 "station",
-                "ephemeris",
+                "trajectory",
                 "coords",
+                "ephemeris",
                 "international",
                 "iss",
-                "location"
+                "topo",
+                "coordinates"
             ],
             "landingPage": "https://spotthestation.nasa.gov",
             "language": [
@@ -491784,10 +491784,10 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcmag-4-prl-resampled-v5.0_arbf-4fci",
             "issued": "2018-06-26",
             "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "solar wind",
                 "international rosetta mission",
-                "checkout"
+                "solar wind",
+                "checkout",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCMAG-4-PRL-RESAMPLED-V5.0",
             "modified": "2023-01-26",
@@ -501784,11 +501784,11 @@
             "identifier": "https://data.nasa.gov/api/views/awzu-cpt8",
             "issued": "2023-03-31",
             "keyword": [
-                "ivhm",
-                "degradation",
-                "phm",
                 "prognostics",
-                "structures"
+                "structures",
+                "phm",
+                "ivhm",
+                "degradation"
             ],
             "landingPage": "https://data.nasa.gov/d/awzu-cpt8",
             "license": "https://www.usa.gov/government-works",
@@ -502226,8 +502226,8 @@
             "issued": "2023-10-03",
             "keyword": [
                 "earth science",
-                "terrestrial hydrosphere",
-                "surface water"
+                "surface water",
+                "terrestrial hydrosphere"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/1138",
             "language": [
@@ -514315,13 +514315,13 @@
             "identifier": "https://data.nasa.gov/api/views/b67r-rgxc",
             "issued": "2015-04-07",
             "keyword": [
-                "airburstvisual",
-                "spaceapps",
                 "platform",
-                "model",
-                "intermediate",
+                "spaceapps",
+                "airburstvisual",
                 "outerspace",
-                "data visualization"
+                "intermediate",
+                "data visualization",
+                "model"
             ],
             "landingPage": "https://data.nasa.gov/d/b67r-rgxc",
             "modified": "2023-01-31",
@@ -514434,11 +514434,11 @@
             "identifier": "NASA-844__4",
             "issued": "2018-06-25",
             "keyword": [
-                "turbulence",
-                "flow",
+                "cases",
                 "models",
                 "incompressible",
-                "cases"
+                "flow",
+                "turbulence"
             ],
             "landingPage": "http://turbmodels.larc.nasa.gov/bradshaw.html",
             "modified": "2020-01-29",
@@ -514796,11 +514796,11 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc2-67pchuryumov-m15-v2.0_b6k9-hmuq",
             "issued": "2021-05-21",
             "keyword": [
+                "dark",
                 "calibration",
+                "international rosetta mission",
                 "bias",
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "dark",
-                "international rosetta mission"
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC2-67PCHURYUMOV-M15-V2.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -518943,10 +518943,10 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-nims-3-gaspraspec-v1.0_b8gs-eijc",
             "issued": "2018-06-26",
             "keyword": [
-                "galileo",
-                "gaspra",
                 "951 gaspra",
-                "calibration"
+                "galileo",
+                "calibration",
+                "gaspra"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-NIMS-3-GASPRASPEC-V1.0",
             "modified": "2023-01-26",
@@ -529421,8 +529421,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-m-hrii-2-epoxi-mars-v1.0_bed7-ejd9",
             "issued": "2021-05-21",
             "keyword": [
-                "epoxi",
-                "mars"
+                "mars",
+                "epoxi"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-M-HRII-2-EPOXI-MARS-V1.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -534482,12 +534482,12 @@
             "identifier": "nasa_genelab_GLDS-106_bhd4-cidu",
             "issued": "2018-06-26",
             "keyword": [
+                "sample collection",
                 "weightlessness simulation",
-                "sequence analysis data transformation",
                 "library construction",
-                "sample collection",
-                "nucleic acid sequencing",
-                "nucleic acid extraction"
+                "nucleic acid extraction",
+                "sequence analysis data transformation",
+                "nucleic acid sequencing"
             ],
             "landingPage": "https://data.nasa.gov/d/bhd4-cidu",
             "modified": "2023-01-26",
@@ -537331,10 +537331,10 @@
             "identifier": "NASA-591",
             "issued": "2018-06-26",
             "keyword": [
-                "ingest",
-                "catalog",
                 "pds",
-                "tool"
+                "tool",
+                "catalog",
+                "ingest"
             ],
             "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
             "modified": "2020-01-29",
@@ -537701,8 +537701,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-5-ddr-eledens-bmag-ext4v1.0",
             "issued": "2021-05-21",
             "keyword": [
-                "mars",
-                "mars express"
+                "mars express",
+                "mars"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-5-DDR-ELEDENS%2FBMAG-EXT4V1.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -548641,11 +548641,11 @@
             "identifier": "https://data.nasa.gov/api/views/brfb-gzcv",
             "issued": "2023-11-02",
             "keyword": [
-                "diagnostics",
-                "phm",
+                "bearings",
                 "prognostics",
-                "degradation",
-                "bearings"
+                "phm",
+                "diagnostics",
+                "degradation"
             ],
             "landingPage": "https://data.nasa.gov/d/brfb-gzcv",
             "license": "https://www.usa.gov/government-works",
@@ -554969,11 +554969,11 @@
             "identifier": "NASA-832",
             "issued": "2018-06-25",
             "keyword": [
-                "turbulence",
-                "transport",
-                "menter",
                 "models",
                 "shear",
+                "menter",
+                "turbulence",
+                "transport",
                 "stress"
             ],
             "landingPage": "http://turbmodels.larc.nasa.gov/sst.html",
@@ -558112,8 +558112,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lend-2-edr-v1.0_bxcx-75qz",
             "issued": "2021-05-21",
             "keyword": [
-                "lunar reconnaissance orbiter",
-                "moon"
+                "moon",
+                "lunar reconnaissance orbiter"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LEND-2-EDR-V1.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -561975,18 +561975,18 @@
             "identifier": "https://data.nasa.gov/api/views/byqb-7uyn",
             "issued": "2018-01-01",
             "keyword": [
-                "training data",
-                "abstracts",
-                "acronyms",
+                "publications",
                 "machine-learning",
-                "natural language processing",
-                "nlp",
                 "prepped data",
-                "publications",
                 "usg-artificial-intelligence",
                 "usg-ai-training-data",
-                "text",
-                "topics"
+                "acronyms",
+                "abstracts",
+                "nlp",
+                "natural language processing",
+                "training data",
+                "topics",
+                "text"
             ],
             "landingPage": "https://www.sti.nasa.gov/",
             "language": [
@@ -562267,11 +562267,11 @@
             "identifier": "NASA-386",
             "issued": "2018-06-25",
             "keyword": [
+                "structures",
+                "space stations",
                 "mir space station",
                 "mir",
-                "3d model",
-                "structures",
-                "space stations"
+                "3d model"
             ],
             "landingPage": "http://nasa3d.arc.nasa.gov/detail/mir",
             "modified": "2020-01-29",
@@ -567455,8 +567455,8 @@
             "issued": "2013-05-06",
             "keyword": [
                 "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
+                "earth science",
+                "atmospheric chemistry"
             ],
             "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA305",
             "language": [
@@ -570050,8 +570050,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ion-mom-96.0sec_c5ta-7w3b",
             "issued": "2018-06-26",
             "keyword": [
-                "saturn",
-                "voyager"
+                "voyager",
+                "saturn"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ION-MOM-96.0SEC",
             "modified": "2023-01-26",
@@ -579816,10 +579816,10 @@
             "identifier": "C2799465542-POCLOUD",
             "issued": "2022-06-28",
             "keyword": [
-                "sea surface topography",
-                "earth science",
                 "oceans",
-                "ocean waves"
+                "sea surface topography",
+                "ocean waves",
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/SWOT-NALT-OGDR-1.0",
             "language": [
@@ -584029,13 +584029,13 @@
             "issued": "2018-06-26",
             "keyword": [
                 "calibration",
-                "16 cyg b",
                 "vega",
                 "moon",
                 "jupiter",
                 "international rosetta mission",
                 "earth",
-                "dark"
+                "dark",
+                "16 cyg b"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSIWAC-2-EAR2-EARTHSWINGBY2-V1.4",
             "modified": "2023-01-26",
@@ -584998,8 +584998,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67p-m29-inf-refl-v1.0",
             "issued": "2021-05-21",
             "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67P-M29-INF-REFL-V1.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -596317,9 +596317,9 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v9.0_cjdc-9v26",
             "issued": "2021-05-21",
             "keyword": [
-                "asteroid",
                 "satellite",
-                "support archives"
+                "support archives",
+                "asteroid"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V9.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -596496,13 +596496,13 @@
             "identifier": "https://data.nasa.gov/api/views/cjex-ucks",
             "issued": "2020-01-22",
             "keyword": [
-                "mars",
                 "planetary science",
+                "mahli",
                 "usg-artificial-intelligence",
-                "mastcam",
-                "mars science laboratory",
                 "machine-learning",
-                "mahli"
+                "mastcam",
+                "mars",
+                "mars science laboratory"
             ],
             "landingPage": "https://data.nasa.gov/d/cjex-ucks",
             "license": "https://www.usa.gov/government-works",
@@ -598580,8 +598580,8 @@
             "identifier": "C179001769-SEDAC",
             "issued": "2005-12-31",
             "keyword": [
-                "earth science",
                 "natural hazards",
+                "earth science",
                 "human dimensions"
             ],
             "landingPage": "https://doi.org/10.7927/H4BZ63ZS",
@@ -602956,17 +602956,17 @@
             "issued": "2017-09-21",
             "keyword": [
                 "atmospheric water vapor",
-                "aerosols",
+                "biosphere",
                 "atmosphere",
-                "atmospheric pressure",
                 "atmospheric radiation",
-                "vegetation",
-                "ngda",
-                "national geospatial data asset",
-                "earth science",
-                "clouds",
                 "atmospheric temperature",
-                "biosphere"
+                "clouds",
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "vegetation",
+                "aerosols",
+                "atmospheric pressure"
             ],
             "landingPage": "https://doi.org/10.5067/TERRA+NPP/CERES/SYN1DEG-1HOUR_L3.01A",
             "language": [
@@ -604290,10 +604290,10 @@
             "issued": "2023-11-02",
             "keyword": [
                 "prognostics",
+                "phm",
                 "diagnostics",
                 "degradation",
-                "batteries",
-                "phm"
+                "batteries"
             ],
             "landingPage": "https://data.nasa.gov/d/cpqc-ztjh",
             "license": "https://www.usa.gov/government-works",
@@ -608919,14 +608919,14 @@
             "identifier": "C2784893177-ORNL_CLOUD",
             "issued": "2023-10-15",
             "keyword": [
-                "vegetation",
                 "land surface",
+                "biosphere",
+                "vegetation",
                 "national geospatial data asset",
                 "land use/land cover",
-                "ngda",
-                "biosphere",
                 "earth science",
-                "surface radiative properties"
+                "surface radiative properties",
+                "ngda"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/972",
             "language": [
@@ -609124,35 +609124,35 @@
             "identifier": "NASA-0000065",
             "issued": "2018-06-25",
             "keyword": [
-                "dss",
                 "stsci",
-                "euve",
-                "iue",
+                "astro",
+                "astronomical data archive",
+                "befs",
                 "copernicus",
-                "imaps",
-                "hut",
-                "hst",
+                "dss",
                 "epoch",
-                "galex",
+                "euve",
+                "first",
                 "fuse",
+                "galex",
+                "gsc",
+                "hpol",
+                "hst",
+                "hut",
+                "imaps",
+                "iue",
+                "kepler",
                 "mast",
                 "optical astronomy",
                 "orfeus",
-                "kepler",
                 "rosat",
-                "ultraviolet astronomy",
-                "uit",
-                "tues",
-                "hpol",
-                "gsc",
                 "sdss",
-                "astro",
-                "first",
-                "astronomical data archive",
-                "befs",
-                "xmmom",
+                "tues",
+                "uit",
+                "ultraviolet astronomy",
+                "vlafirst",
                 "wuppe",
-                "vlafirst"
+                "xmmom"
             ],
             "landingPage": "http://archive.stsci.edu/kepler/",
             "modified": "2020-01-29",
@@ -610736,13 +610736,13 @@
             "identifier": "C2789024214-ORNL_CLOUD",
             "issued": "2023-10-18",
             "keyword": [
-                "atmosphere",
                 "human dimensions",
                 "earth science",
-                "ecological dynamics",
+                "atmospheric chemistry",
+                "atmosphere",
                 "environmental impacts",
-                "biosphere",
-                "atmospheric chemistry"
+                "ecological dynamics",
+                "biosphere"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/752",
             "language": [
@@ -617901,16 +617901,16 @@
             "identifier": "API-16",
             "issued": "2015-11-30",
             "keyword": [
-                "matlab",
+                "perl",
                 "products",
-                "api",
-                "collections",
-                "java",
+                "r",
+                "python",
                 "kepler",
-                "perl",
+                "java",
+                "matlab",
                 "modis",
-                "python",
-                "r"
+                "api",
+                "collections"
             ],
             "landingPage": "http://daac.ornl.gov/MODIS/MODIS-menu/modis_webservice.html",
             "modified": "2020-01-29",
@@ -619452,14 +619452,14 @@
             "identifier": "C2761597892-LARC_ASDC",
             "issued": "1997-10-07",
             "keyword": [
-                "atmosphere",
-                "air quality",
-                "altitude",
                 "atmospheric chemistry",
+                "air quality",
                 "atmospheric radiation",
+                "spectral/engineering",
+                "altitude",
                 "earth science",
-                "lidar",
-                "spectral/engineering"
+                "atmosphere",
+                "lidar"
             ],
             "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_AircraftRemoteSensing_DC8_DIAL_Data_1",
             "language": [
@@ -620476,16 +620476,16 @@
             "identifier": "https://data.nasa.gov/api/views/cykx-2qix",
             "issued": "2021-05-11",
             "keyword": [
+                "citizen science",
+                "autonomous",
+                "mer-a",
+                "mars",
+                "curiosity",
                 "computer vision",
-                "spirit",
                 "opportunity",
                 "msl",
                 "mer-b",
-                "mer-a",
-                "mars",
-                "curiosity",
-                "citizen science",
-                "autonomous",
+                "spirit",
                 "terrain"
             ],
             "landingPage": "https://data.nasa.gov/d/cykx-2qix",
@@ -642125,15 +642125,15 @@
             "identifier": "OCIO-Fitara-151",
             "issued": "1979-12-31",
             "keyword": [
-                "altimetry",
-                "imagery",
+                "radar",
+                "venus",
+                "working group for planetary system nomenclature",
                 "images",
+                "imagery",
                 "planets",
+                "altimetry",
                 "quadrangles",
-                "radar",
-                "usgs",
-                "venus",
-                "working group for planetary system nomenclature"
+                "usgs"
             ],
             "landingPage": "http://planetarynames.wr.usgs.gov/Page/venus1to10m_Altimetry",
             "modified": "2020-01-29",
@@ -642702,18 +642702,18 @@
             "identifier": "C1227352388-LARC_ASDC",
             "issued": "2017-09-21",
             "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "earth science",
-                "national geospatial data asset",
+                "atmospheric water vapor",
+                "atmospheric temperature",
                 "ngda",
+                "national geospatial data asset",
+                "earth science",
+                "clouds",
                 "biosphere",
                 "aerosols",
-                "clouds",
+                "atmospheric radiation",
+                "atmosphere",
                 "atmospheric pressure",
-                "vegetation",
-                "atmospheric temperature",
-                "atmospheric water vapor"
+                "vegetation"
             ],
             "landingPage": "https://doi.org/10.5067/Terra+Aqua/CERES/SYN1deg-MHour_L3.004A",
             "language": [
@@ -646642,14 +646642,14 @@
             "identifier": "OCIO-Fitara-130",
             "issued": "2015-01-07",
             "keyword": [
-                "mfs",
                 "aviation",
-                "multi-fidelity",
-                "ocsvm",
-                "air traffic flow",
                 "airspace",
                 "simulator",
-                "mfsim"
+                "ocsvm",
+                "multi-fidelity",
+                "air traffic flow",
+                "mfsim",
+                "mfs"
             ],
             "landingPage": "http://ti.arc.nasa.gov/opensource/projects/mfsim/",
             "modified": "2020-01-29",
@@ -653068,13 +653068,13 @@
             "identifier": "C1517102461-SEDAC",
             "issued": "2017-12-06",
             "keyword": [
-                "habitat conversion/fragmentation",
-                "human dimensions",
                 "land surface",
-                "land use/land cover",
-                "biosphere",
+                "ecosystems",
                 "earth science",
-                "ecosystems"
+                "biosphere",
+                "habitat conversion/fragmentation",
+                "human dimensions",
+                "land use/land cover"
             ],
             "landingPage": "https://doi.org/10.7927/H4P55KKF",
             "language": [
@@ -671689,9 +671689,9 @@
             "identifier": "C2799438266-POCLOUD",
             "issued": "2022-07-20",
             "keyword": [
-                "earth science",
+                "surface water",
                 "terrestrial hydrosphere",
-                "surface water"
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/SWOT-PIXC-2.0",
             "language": [
@@ -675073,11 +675073,11 @@
             "identifier": "C1220567948-USGS_LTA",
             "issued": "1972-01-01",
             "keyword": [
-                "food science",
-                "agricultural plant science",
                 "earth science",
+                "agriculture",
                 "plant commodities",
-                "agriculture"
+                "food science",
+                "agricultural plant science"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567948-USGS_LTA.html",
             "language": [
@@ -678601,11 +678601,11 @@
             "identifier": "C1419745913-CDDIS",
             "issued": "1998-01-01",
             "keyword": [
+                "geodetics",
                 "gravity/gravitational field",
-                "earth science",
-                "solid earth",
                 "tectonics",
-                "geodetics"
+                "earth science",
+                "solid earth"
             ],
             "landingPage": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_D_001",
             "language": [
@@ -691965,18 +691965,18 @@
             "identifier": "OCIO-Fitara-160",
             "issued": "2013-02-13",
             "keyword": [
-                "north pole",
-                "far side",
-                "imagery",
-                "images",
-                "lunar",
-                "maps",
-                "moon",
-                "near side",
-                "south pole",
                 "topography",
+                "imagery",
+                "working group for planetary system nomenclature",
                 "usgs",
-                "working group for planetary system nomenclature"
+                "south pole",
+                "north pole",
+                "near side",
+                "moon",
+                "maps",
+                "lunar",
+                "images",
+                "far side"
             ],
             "landingPage": "http://planetarynames.wr.usgs.gov/Page/moon1to10mShadedRelief",
             "modified": "2020-01-29",
@@ -696503,14 +696503,14 @@
             "issued": "2014-04-03",
             "keyword": [
                 "geomorphic landforms/processes",
-                "tectonics",
                 "solid earth",
                 "oceans",
-                "coastal processes",
-                "cryosphere",
                 "earth science",
+                "coastal processes",
                 "land surface",
-                "glaciers/ice sheets"
+                "glaciers/ice sheets",
+                "cryosphere",
+                "tectonics"
             ],
             "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_RTC-S1-STATIC_V1",
             "language": [
@@ -705002,16 +705002,16 @@
             "identifier": "C1386206894-NSIDCV0",
             "issued": "1998-06-01",
             "keyword": [
+                "atmospheric temperature",
+                "land surface",
+                "precipitation",
+                "earth science",
                 "frozen ground",
                 "atmospheric winds",
-                "soils",
-                "cryosphere",
                 "atmospheric water vapor",
-                "earth science",
-                "precipitation",
-                "land surface",
-                "atmospheric temperature",
-                "atmosphere"
+                "soils",
+                "atmosphere",
+                "cryosphere"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206894-NSIDCV0.html",
             "language": [
@@ -705281,12 +705281,12 @@
             "identifier": "https://data.nasa.gov/api/views/egmv-36wq",
             "issued": "2020-01-22",
             "keyword": [
+                "planetary science",
+                "usg-artificial-intelligence",
+                "usg-ai-training-data",
                 "mars reconnaissance orbiter",
                 "machine-learning",
-                "hirise",
-                "usg-ai-training-data",
-                "usg-artificial-intelligence",
-                "planetary science"
+                "hirise"
             ],
             "landingPage": "https://data.nasa.gov/d/egmv-36wq",
             "modified": "2023-01-31",
@@ -714596,8 +714596,8 @@
             "identifier": "C2519125808-LPCLOUD",
             "issued": "2023-06-12",
             "keyword": [
-                "land surface",
                 "surface radiative properties",
+                "land surface",
                 "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VNP09H1.002",
@@ -722062,30 +722062,30 @@
             "identifier": "C1327985647-ASF",
             "issued": "2016-08-20",
             "keyword": [
-                "coastal processes",
-                "surface water",
                 "terrestrial hydrosphere",
+                "biosphere",
+                "coastal processes",
+                "agriculture",
                 "cryosphere",
                 "earth science",
                 "erosion/sedimentation",
                 "forest science",
-                "solid earth",
                 "frozen ground",
                 "geomorphic landforms/processes",
-                "agriculture",
-                "ocean winds",
-                "sea ice",
-                "terrestrial ecosystems",
                 "glaciers/ice sheets",
-                "ocean waves",
-                "tectonics",
                 "landscape",
                 "land surface",
                 "land use/land cover",
-                "topography",
                 "oceans",
+                "ocean waves",
+                "ocean winds",
+                "sea ice",
                 "snow/ice",
-                "biosphere"
+                "solid earth",
+                "surface water",
+                "tectonics",
+                "terrestrial ecosystems",
+                "topography"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985647-ASF.html",
             "language": [
@@ -723958,17 +723958,17 @@
             "identifier": "C1220567909-USGS_LTA",
             "issued": "2019-09-20",
             "keyword": [
-                "earth science",
-                "geomorphic landforms/processes",
-                "topography",
+                "erosion/sedimentation",
                 "surface radiative properties",
                 "soils",
-                "oceans",
-                "land use/land cover",
+                "coastal processes",
+                "topography",
                 "land surface",
+                "land use/land cover",
+                "earth science",
+                "oceans",
                 "landscape",
-                "coastal processes",
-                "erosion/sedimentation"
+                "geomorphic landforms/processes"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567909-USGS_LTA.html",
             "language": [
@@ -724124,12 +724124,12 @@
             "identifier": "C1220567951-USGS_LTA",
             "issued": "2001-05-01",
             "keyword": [
+                "visible wavelengths",
                 "earth science",
-                "surface radiative properties",
+                "infrared wavelengths",
                 "land surface",
                 "spectral/engineering",
-                "visible wavelengths",
-                "infrared wavelengths"
+                "surface radiative properties"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567951-USGS_LTA.html",
             "language": [
@@ -732706,10 +732706,10 @@
             "identifier": "API-100",
             "issued": "2015-11-30",
             "keyword": [
+                "apod",
                 "sharing share",
-                "social media",
                 "api",
-                "apod"
+                "social media"
             ],
             "landingPage": "https://api.nasa.gov/api.html",
             "modified": "2020-01-29",
@@ -734191,13 +734191,13 @@
             "identifier": "NASA-867__4",
             "issued": "2018-06-25",
             "keyword": [
+                "training",
                 "project",
+                "management",
                 "knowledge",
-                "training",
                 "sharing",
-                "appel",
                 "case studies",
-                "management"
+                "appel"
             ],
             "landingPage": "http://appel.nasa.gov/knowledge-sharing/case-studies/appel-case-studies/",
             "modified": "2020-01-29",
@@ -743678,16 +743678,16 @@
             "identifier": "https://data.nasa.gov/api/views/f7qz-8dsr",
             "issued": "2018-10-01",
             "keyword": [
-                "asteroids",
-                "composite materials",
-                "microct",
-                "porous materials",
+                "carbon-phenolic composites",
                 "textiles",
-                "thermal protection",
+                "porous materials",
+                "microct",
                 "meteorites",
-                "woven composites",
+                "composite materials",
+                "thermal protection",
+                "asteroids",
                 "tomography",
-                "carbon-phenolic composites"
+                "woven composites"
             ],
             "landingPage": "https://data.nasa.gov/d/f7qz-8dsr",
             "modified": "2024-05-15",
@@ -751166,8 +751166,8 @@
             "keyword": [
                 "atmospheric radiation",
                 "earth science",
-                "atmosphere",
-                "aerosols"
+                "aerosols",
+                "atmosphere"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/1898",
             "language": [
@@ -756225,10 +756225,10 @@
             "issued": "2022-07-14",
             "keyword": [
                 "ivhm",
-                "prognostics",
-                "fan degradation",
                 "degradation",
-                "phm"
+                "fan degradation",
+                "phm",
+                "prognostics"
             ],
             "landingPage": "https://data.nasa.gov/d/ff5v-kuh6",
             "modified": "2024-05-15",
@@ -761385,13 +761385,13 @@
             "identifier": "NASA-0000023",
             "issued": "2018-06-25",
             "keyword": [
-                "black hole",
                 "neutron stars",
-                "binary",
                 "ligo",
-                "gravitational waves",
+                "binary",
+                "astronomy",
                 "space science",
-                "astronomy"
+                "black hole",
+                "gravitational waves"
             ],
             "landingPage": "https://asd.gsfc.nasa.gov/archive/astrogravs/docs/catalog.html#bhns",
             "modified": "2024-08-16",
@@ -765215,11 +765215,11 @@
             "issued": "2023-04-15",
             "keyword": [
                 "human dimensions",
-                "aerosols",
                 "earth science",
-                "public health",
+                "atmosphere",
                 "air quality",
-                "atmosphere"
+                "aerosols",
+                "public health"
             ],
             "landingPage": "https://doi.org/doi:10.5067/ZDLBXTRFQ7U9",
             "language": [
@@ -776271,10 +776271,10 @@
             "identifier": "C1220566083-USGS_LTA",
             "issued": "1969-07-16",
             "keyword": [
-                "spectral/engineering",
                 "earth science",
                 "infrared wavelengths",
-                "visible wavelengths"
+                "visible wavelengths",
+                "spectral/engineering"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566083-USGS_LTA.html",
             "language": [
@@ -793949,9 +793949,9 @@
             "identifier": "C1200034342-OB_DAAC",
             "issued": "2017-01-11",
             "keyword": [
+                "oceans",
                 "earth science",
-                "ocean chemistry",
-                "oceans"
+                "ocean chemistry"
             ],
             "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3M/CHL/2014",
             "language": [
@@ -799012,12 +799012,12 @@
             "issued": "2014-06-03",
             "keyword": [
                 "microwave",
-                "earth science",
-                "atmosphere",
                 "radar",
+                "spectral/engineering",
                 "lidar",
+                "atmosphere",
                 "clouds",
-                "spectral/engineering"
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/ADMIRARI/DATA201",
             "language": [
@@ -806519,8 +806519,8 @@
             "identifier": "DASHLINK_559",
             "issued": "2012-03-26",
             "keyword": [
-                "dashlink",
                 "nasa",
+                "dashlink",
                 "ames"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/559/",
@@ -814643,13 +814643,13 @@
             "identifier": "https://data.nasa.gov/api/views/gh4g-9sfh",
             "issued": "2015-07-20",
             "keyword": [
-                "airburstvisual",
-                "model",
-                "intermediate",
-                "spaceapps",
                 "data visualization",
+                "spaceapps",
                 "platform",
-                "outerspace"
+                "outerspace",
+                "model",
+                "intermediate",
+                "airburstvisual"
             ],
             "landingPage": "https://data.nasa.gov/d/gh4g-9sfh",
             "modified": "2023-01-31",
@@ -817022,8 +817022,8 @@
             "issued": "1997-06-03",
             "keyword": [
                 "earth science",
-                "sun-earth interactions",
-                "solar energetic particle properties"
+                "solar energetic particle properties",
+                "sun-earth interactions"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273348498-GES_DISC.html",
             "language": [
@@ -825773,9 +825773,9 @@
             "identifier": "DASHLINK_14",
             "issued": "2010-09-10",
             "keyword": [
-                "nasa",
+                "ames",
                 "dashlink",
-                "ames"
+                "nasa"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/14/",
             "modified": "2022-07-14",
@@ -830557,23 +830557,23 @@
             "identifier": "NASA-0000042",
             "issued": "2018-06-25",
             "keyword": [
+                "oceans",
                 "climate",
-                "wwhgd",
-                "wise",
-                "sun-earth interaction",
-                "spectrometry",
-                "paleoclimate",
+                "agriculture",
                 "operations",
-                "oceans",
                 "land",
+                "wise",
+                "wwhgd",
+                "paleoclimate",
                 "hydrosphere",
                 "geospatial",
+                "spectrometry",
                 "engineering",
                 "earth science",
-                "agriculture",
-                "cryosphere",
+                "sun-earth interaction",
                 "atmosphere",
                 "biology",
+                "cryosphere",
                 "biosphere"
             ],
             "landingPage": "https://data.nasa.gov/d/gt6i-nuv6",
@@ -836317,15 +836317,15 @@
             "identifier": "NASA-851__2",
             "issued": "2018-06-25",
             "keyword": [
-                "models",
+                "experiment",
                 "airfoil",
-                "validation",
                 "turbulence",
-                "tangential",
+                "models",
                 "synthetic",
-                "jets",
+                "tangential",
+                "validation",
                 "coanda",
-                "experiment"
+                "jets"
             ],
             "landingPage": "https://turbmodels.larc.nasa.gov/Other_exp_Data/cfdval2004_exp.html",
             "modified": "2024-08-07",
@@ -840394,9 +840394,9 @@
             "identifier": "TECHPORT_12110",
             "issued": "2012-09-01",
             "keyword": [
-                "active",
-                "project",
                 "twdec",
+                "project",
+                "active",
                 "johnson space center"
             ],
             "landingPage": "http://techport.nasa.gov/view/12110",
@@ -847487,8 +847487,8 @@
             "issued": "2023-10-15",
             "keyword": [
                 "vegetation",
-                "earth science",
-                "biosphere"
+                "biosphere",
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/970",
             "language": [
@@ -848812,23 +848812,23 @@
             "identifier": "NASA-908",
             "issued": "2015-08-21",
             "keyword": [
-                "atmosphere",
-                "astronomy",
-                "heat",
+                "photos of earth",
                 "image of the day",
-                "imagery",
-                "images",
+                "earth science",
+                "astronomy",
                 "land",
                 "life",
                 "media gallery",
-                "natural hazards",
-                "photos of earth",
+                "water",
+                "atmosphere",
+                "heat",
+                "imagery",
                 "picture of the day",
-                "remote sensing",
+                "images",
                 "snow and ice",
-                "water",
-                "world of change",
-                "earth science"
+                "natural hazards",
+                "remote sensing",
+                "world of change"
             ],
             "landingPage": "http://earthobservatory.nasa.gov/Images/?eocn=topnav&eoci=images",
             "modified": "2020-01-29",
@@ -856470,8 +856470,8 @@
             "identifier": "DASHLINK_190",
             "issued": "2010-09-22",
             "keyword": [
-                "ames",
                 "dashlink",
+                "ames",
                 "nasa"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/190/",
@@ -856873,11 +856873,11 @@
             "identifier": "C2343111356-LPCLOUD",
             "issued": "2021-02-01",
             "keyword": [
-                "national geospatial data asset",
                 "surface radiative properties",
-                "ngda",
                 "earth science",
-                "land surface"
+                "land surface",
+                "ngda",
+                "national geospatial data asset"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MOD09A1.061",
             "language": [
@@ -864858,9 +864858,9 @@
             "keyword": [
                 "bias",
                 "4 vesta",
+                "vega",
                 "international rosetta mission",
-                "dark",
-                "vega"
+                "dark"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-2-CR5-CHECKOUT-V2.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -879288,8 +879288,8 @@
             "issued": "2023-07-01",
             "keyword": [
                 "precipitation",
-                "earth science",
-                "atmosphere"
+                "atmosphere",
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/GPM/IMERG/3B-HH/07",
             "language": [
@@ -901843,13 +901843,13 @@
             "identifier": "C1879283378-SEDAC",
             "issued": "2020-06-23",
             "keyword": [
+                "sustainability",
+                "human settlements",
+                "human dimensions",
+                "population",
                 "earth science",
                 "infrastructure",
-                "population",
-                "human settlements",
-                "economic resources",
-                "sustainability",
-                "human dimensions"
+                "economic resources"
             ],
             "landingPage": "https://doi.org/10.7927/9ryj-6467",
             "language": [
@@ -916954,8 +916954,8 @@
             "identifier": "C2929136513-ORNL_CLOUD",
             "issued": "2023-11-22",
             "keyword": [
-                "surface radiative properties",
                 "earth science",
+                "surface radiative properties",
                 "land surface"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/482",
@@ -917685,8 +917685,8 @@
             "identifier": "C2799438230-POCLOUD",
             "issued": "2022-07-20",
             "keyword": [
-                "terrestrial hydrosphere",
                 "earth science",
+                "terrestrial hydrosphere",
                 "surface water"
             ],
             "landingPage": "https://doi.org/10.5067/SWOT-LAKESP-2.0",
@@ -920481,14 +920481,14 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-irrdr-cleaned-v1.0",
             "issued": "2021-05-21",
             "keyword": [
-                "mars",
+                "comet",
                 "sun",
                 "sky",
-                "calibration",
                 "phobos",
                 "mars express",
+                "mars",
                 "deimos",
-                "comet"
+                "calibration"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-IRRDR-CLEANED-V1.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -925945,15 +925945,15 @@
             "identifier": "C1220567858-USGS_LTA",
             "issued": "2019-09-20",
             "keyword": [
+                "soils",
                 "topography",
-                "earth science",
-                "erosion/sedimentation",
-                "geomorphic landforms/processes",
-                "landscape",
                 "land surface",
-                "land use/land cover",
-                "soils",
-                "surface radiative properties"
+                "landscape",
+                "geomorphic landforms/processes",
+                "erosion/sedimentation",
+                "earth science",
+                "surface radiative properties",
+                "land use/land cover"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567858-USGS_LTA.html",
             "language": [
@@ -940297,10 +940297,10 @@
             "identifier": "C2662353694-LARC_ASDC",
             "issued": "1997-10-09",
             "keyword": [
-                "air quality",
+                "atmospheric chemistry",
                 "earth science",
+                "air quality",
                 "atmosphere",
-                "atmospheric chemistry",
                 "aerosols"
             ],
             "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Aerosol_AircraftInSitu_DC8_Data_1",
@@ -943609,8 +943609,8 @@
             "identifier": "C2925500837-NSIDCV0",
             "issued": "1979-10-01",
             "keyword": [
-                "cryosphere",
                 "earth science",
+                "cryosphere",
                 "sea ice"
             ],
             "landingPage": "https://doi.org/10.5067/LKARAZONXGR0",
@@ -948382,11 +948382,11 @@
             "identifier": "NASA-334",
             "issued": "2018-06-25",
             "keyword": [
+                "deep space 1",
                 "spacecraft",
+                "satellite",
                 "3d model",
-                "eyes on the solar system",
-                "deep space 1",
-                "satellite"
+                "eyes on the solar system"
             ],
             "landingPage": "http://nasa3d.arc.nasa.gov/detail/jpl-vtad-ds1",
             "modified": "2020-01-29",
@@ -960468,13 +960468,13 @@
             "identifier": "C2712794398-LARC_ASDC",
             "issued": "1997-04-16",
             "keyword": [
-                "atmosphere",
                 "atmospheric temperature",
-                "topography",
+                "atmospheric chemistry",
+                "atmosphere",
+                "clouds",
                 "earth science",
                 "land surface",
-                "clouds",
-                "atmospheric chemistry"
+                "topography"
             ],
             "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/POLARIS_jValue_AircraftInSitu_ER2_Data_1",
             "language": [
@@ -970783,10 +970783,10 @@
             "identifier": "C1599922061-LARC_ASDC",
             "issued": "2018-08-13",
             "keyword": [
-                "atmosphere",
                 "aerosols",
-                "earth science",
-                "clouds"
+                "atmosphere",
+                "clouds",
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmPro",
             "language": [
@@ -977301,12 +977301,12 @@
             "identifier": "C2264350397-ORNL_CLOUD",
             "issued": "2024-12-02",
             "keyword": [
-                "ecosystems",
-                "vegetation",
                 "earth science",
+                "vegetation",
+                "topography",
                 "land surface",
                 "biosphere",
-                "topography"
+                "ecosystems"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/1923",
             "language": [
@@ -978467,9 +978467,9 @@
             "identifier": "C1243477370-GES_DISC",
             "issued": "2010-01-01",
             "keyword": [
-                "atmospheric chemistry",
                 "earth science",
-                "atmosphere"
+                "atmosphere",
+                "atmospheric chemistry"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243477370-GES_DISC.html",
             "language": [
@@ -979678,9 +979678,9 @@
             "identifier": "C1918210023-GES_DISC",
             "issued": "2017-05-05",
             "keyword": [
+                "atmosphere",
                 "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
+                "atmospheric chemistry"
             ],
             "landingPage": "https://doi.org/10.5270/S5P-vg1i7t0",
             "language": [
@@ -985202,12 +985202,12 @@
             "identifier": "C2006849345-POCLOUD",
             "issued": "2021-01-20",
             "keyword": [
-                "ocean circulation",
-                "oceans",
+                "ocean heat budget",
                 "ocean temperature",
                 "salinity/density",
                 "earth science",
-                "ocean heat budget"
+                "ocean circulation",
+                "oceans"
             ],
             "landingPage": "https://doi.org/10.5067/PRESW-RMJ10",
             "language": [
@@ -998024,11 +998024,11 @@
             "identifier": "NASA-0000030__3",
             "issued": "2018-06-25",
             "keyword": [
-                "lunar science",
-                "circulation",
                 "space science",
+                "circulation",
                 "modeling",
-                "imagery"
+                "imagery",
+                "lunar science"
             ],
             "landingPage": "http://www.lpi.usra.edu/resources/cla/",
             "modified": "2020-01-29",
@@ -1020221,13 +1020221,13 @@
             "identifier": "C1979814484-GHRC_DAAC",
             "issued": "2018-05-17",
             "keyword": [
-                "atmospheric winds",
                 "atmospheric temperature",
                 "atmospheric water vapor",
-                "atmospheric pressure",
+                "atmospheric winds",
                 "earth science",
                 "altitude",
-                "atmosphere"
+                "atmosphere",
+                "atmospheric pressure"
             ],
             "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/RADIOSONDES/DATA101",
             "language": [
@@ -1023911,8 +1023911,8 @@
             "identifier": "DASHLINK_682",
             "issued": "2013-03-29",
             "keyword": [
-                "dashlink",
                 "ames",
+                "dashlink",
                 "nasa"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/682/",
@@ -1034929,8 +1034929,8 @@
             "identifier": "C2062213246-LAADS",
             "issued": "2021-05-04",
             "keyword": [
-                "spectral/engineering",
                 "earth science",
+                "spectral/engineering",
                 "biosphere"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VNP46A4.001",
@@ -1043785,11 +1043785,11 @@
             "identifier": "C1237114211-GES_DISC",
             "issued": "2004-04-30",
             "keyword": [
+                "aerosols",
                 "atmospheric radiation",
-                "atmosphere",
                 "atmospheric chemistry",
-                "earth science",
-                "aerosols"
+                "atmosphere",
+                "earth science"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114211-GES_DISC.html",
             "language": [
@@ -1057350,8 +1057350,8 @@
             "identifier": "nasa_genelab_GLDS-264_kz2q-9agt",
             "issued": "2021-05-21",
             "keyword": [
-                "['sample collection' 'nucleic acid extraction' 'nucleic acid sequencing' 'sequence assembly']",
-                "['spaceflight']"
+                "['spaceflight']",
+                "['sample collection' 'nucleic acid extraction' 'nucleic acid sequencing' 'sequence assembly']"
             ],
             "landingPage": "https://data.nasa.gov/d/kz2q-9agt",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -1060042,10 +1060042,10 @@
             "identifier": "C2216864285-ORNL_CLOUD",
             "issued": "2020-05-11",
             "keyword": [
-                "earth science",
                 "land surface",
                 "soils",
                 "surface water",
+                "earth science",
                 "terrestrial hydrosphere"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/1566",
@@ -1068888,8 +1068888,8 @@
             "issued": "2010-09-09",
             "keyword": [
                 "dashlink",
-                "ames",
-                "nasa"
+                "nasa",
+                "ames"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/3/",
             "modified": "2020-01-29",
@@ -1072902,10 +1072902,10 @@
             "identifier": "C3049900163-ORNL_CLOUD",
             "issued": "2024-09-26",
             "keyword": [
-                "earth science",
-                "ecosystems",
+                "biosphere",
                 "vegetation",
-                "biosphere"
+                "earth science",
+                "ecosystems"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/2338",
             "language": [
@@ -1074848,21 +1074848,21 @@
             "identifier": "nasa_genelab_GLDS-27_mazn-9rvz",
             "issued": "2021-05-21",
             "keyword": [
-                "treatment protocol",
-                "labeling",
-                "temperature",
-                "feature_extraction",
-                "time",
-                "data transformation",
+                "affymetrix:protocol:hybridization-unknown",
+                "nucleic_acid_extraction",
                 "p-affy-2",
                 "genelab microarray data processing protocol",
-                "hybridization",
-                "altered gravity simulator",
-                "nucleic_acid_extraction",
                 "p-affy-6",
+                "feature_extraction",
+                "data transformation",
+                "altered gravity simulator",
                 "p-mtab-3463",
+                "hybridization",
+                "labeling",
                 "sex",
-                "affymetrix:protocol:hybridization-unknown"
+                "temperature",
+                "time",
+                "treatment protocol"
             ],
             "landingPage": "https://data.nasa.gov/d/mazn-9rvz",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -1081131,9 +1081131,9 @@
             "identifier": "DASHLINK_681",
             "issued": "2013-03-29",
             "keyword": [
-                "ames",
                 "nasa",
-                "dashlink"
+                "dashlink",
+                "ames"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/681/",
             "modified": "2020-01-29",
@@ -1096356,38 +1096356,38 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-spec-v1.2_mq2e-8a34",
             "issued": "2021-05-21",
             "keyword": [
-                "atlas",
+                "dark sky",
+                "cassini-huygens",
+                "phoebe",
+                "titan",
+                "tethys",
+                "telesto",
+                "tarvos",
+                "sun",
+                "star",
+                "s rings",
+                "skoll",
+                "siarnaq",
                 "saturn",
                 "rhea",
                 "prometheus",
-                "phoebe",
+                "ymir",
                 "pandora",
                 "pan",
-                "helene",
-                "epimetheus",
-                "hyperion",
                 "paaliaq",
                 "mimas",
-                "iapetus",
+                "janus",
                 "ijiraq",
+                "iapetus",
+                "hyperion",
+                "helene",
+                "epimetheus",
                 "enceladus",
                 "dione",
-                "dark sky",
-                "albiorix",
-                "cassini-huygens",
                 "calypso",
                 "bestia",
-                "janus",
-                "ymir",
-                "titan",
-                "tethys",
-                "telesto",
-                "tarvos",
-                "sun",
-                "star",
-                "s rings",
-                "skoll",
-                "siarnaq"
+                "atlas",
+                "albiorix"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SPEC-V1.2",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -1099153,8 +1099153,8 @@
             "identifier": "DASHLINK_449",
             "issued": "2011-08-15",
             "keyword": [
-                "ames",
                 "dashlink",
+                "ames",
                 "nasa"
             ],
             "landingPage": "https://c3.nasa.gov/dashlink/resources/449/",
@@ -1099396,18 +1099396,18 @@
             "issue-identification": "GSSTF_NCEP_3",
             "issued": "2012-08-14",
             "keyword": [
+                "oceans",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric radiation",
                 "atmospheric temperature",
                 "atmospheric water vapor",
-                "ocean pressure",
-                "ocean heat budget",
-                "atmospheric pressure",
-                "ocean winds",
-                "atmosphere",
-                "ocean temperature",
                 "atmospheric winds",
                 "earth science",
-                "atmospheric radiation",
-                "oceans"
+                "ocean heat budget",
+                "ocean pressure",
+                "ocean winds",
+                "ocean temperature"
             ],
             "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA302",
             "language": [
@@ -1123394,9 +1123394,9 @@
             "identifier": "NASA-783",
             "issued": "2018-06-25",
             "keyword": [
-                "validation",
                 "tool",
-                "pds"
+                "pds",
+                "validation"
             ],
             "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
             "modified": "2020-01-29",
@@ -1138232,11 +1138232,11 @@
             "identifier": "C3363997464-LANCEMODIS",
             "issued": "2024-12-31",
             "keyword": [
+                "vegetation",
                 "earth science",
-                "land surface",
                 "biosphere",
                 "surface radiative properties",
-                "vegetation"
+                "land surface"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VNP13A4N.002",
             "language": [
@@ -1143122,9 +1143122,9 @@
             "identifier": "C2569836924-LARC_ASDC",
             "issued": "2022-09-12",
             "keyword": [
+                "atmosphere",
                 "aerosols",
-                "earth science",
-                "atmosphere"
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_AircraftRemoteSensing_DC8_HSRL_Data_1",
             "language": [
@@ -1146829,9 +1146829,9 @@
             "identifier": "https://data.nasa.gov/api/views/nk8v-ckry",
             "issued": "2023-02-16",
             "keyword": [
-                "degradation",
+                "phm",
                 "prognostics",
-                "phm"
+                "degradation"
             ],
             "landingPage": "https://data.nasa.gov/d/nk8v-ckry",
             "license": "https://www.usa.gov/government-works",
@@ -1160796,8 +1160796,8 @@
             "identifier": "C2799465538-POCLOUD",
             "issued": "2022-06-28",
             "keyword": [
-                "earth science",
                 "ocean waves",
+                "earth science",
                 "oceans",
                 "sea surface topography"
             ],
@@ -1177089,12 +1177089,12 @@
             "identifier": "C2789033440-ORNL_CLOUD",
             "issued": "2023-10-18",
             "keyword": [
+                "human dimensions",
+                "natural hazards",
+                "ecosystems",
                 "ecological dynamics",
                 "earth science",
-                "biosphere",
-                "ecosystems",
-                "natural hazards",
-                "human dimensions"
+                "biosphere"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/756",
             "language": [
@@ -1180474,10 +1180474,10 @@
             "identifier": "C2751949500-ORNL_CLOUD",
             "issued": "2023-08-20",
             "keyword": [
+                "biosphere",
                 "ecological dynamics",
                 "vegetation",
-                "earth science",
-                "biosphere"
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/653",
             "language": [
@@ -1203946,10 +1203946,10 @@
             "keyword": [
                 "terrestrial hydrosphere",
                 "national geospatial data asset",
-                "earth science",
+                "surface water",
                 "ngda",
                 "land surface",
-                "surface water",
+                "earth science",
                 "topography"
             ],
             "landingPage": "https://doi.org/10.5067/ASTER/ASTGTM_NC.003",
@@ -1210407,12 +1210407,12 @@
             "identifier": "C1220567908-USGS_LTA",
             "issued": "2019-09-20",
             "keyword": [
-                "surface radiative properties",
+                "topography",
+                "earth science",
                 "land surface",
                 "national geospatial data asset",
-                "earth science",
-                "topography",
-                "ngda"
+                "ngda",
+                "surface radiative properties"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567908-USGS_LTA.html",
             "language": [
@@ -1213092,17 +1213092,17 @@
             "identifier": "C2956539244-ORNL_CLOUD",
             "issued": "2024-04-26",
             "keyword": [
-                "vegetation",
+                "atmospheric chemistry",
+                "atmospheric radiation",
                 "biosphere",
-                "earth science",
+                "surface thermal properties",
                 "ecological dynamics",
                 "land surface",
-                "surface thermal properties",
                 "soils",
                 "surface radiative properties",
-                "atmospheric chemistry",
-                "atmosphere",
-                "atmospheric radiation"
+                "earth science",
+                "vegetation",
+                "atmosphere"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/807",
             "language": [
@@ -1213334,11 +1213334,11 @@
             "identifier": "C1237114212-GES_DISC",
             "issued": "2004-04-30",
             "keyword": [
-                "aerosols",
-                "earth science",
-                "atmospheric radiation",
+                "atmosphere",
                 "atmospheric chemistry",
-                "atmosphere"
+                "atmospheric radiation",
+                "earth science",
+                "aerosols"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114212-GES_DISC.html",
             "language": [
@@ -1217528,15 +1217528,15 @@
             "identifier": "C2777436413-ASF",
             "issued": "2021-01-01",
             "keyword": [
-                "glaciers/ice sheets",
                 "coastal processes",
+                "oceans",
                 "cryosphere",
-                "earth science",
-                "geomorphic landforms/processes",
                 "land surface",
-                "oceans",
-                "solid earth",
-                "tectonics"
+                "glaciers/ice sheets",
+                "geomorphic landforms/processes",
+                "earth science",
+                "tectonics",
+                "solid earth"
             ],
             "landingPage": "https://doi.org/10.5067/SNWG/OPERA_L2_RTC-S1_V1",
             "language": [
@@ -1217666,21 +1217666,21 @@
             "identifier": "C1220566586-USGS_LTA",
             "issued": "1992-04-01",
             "keyword": [
-                "earth science",
+                "human dimensions",
                 "visible wavelengths",
-                "vegetation",
                 "topography",
-                "terrestrial hydrosphere",
-                "terrestrial ecosystems",
-                "surface water",
-                "spectral/engineering",
+                "vegetation",
+                "environmental governance/management",
+                "ecological dynamics",
+                "earth science",
                 "land use/land cover",
+                "spectral/engineering",
+                "surface water",
                 "land surface",
-                "human dimensions",
-                "aquatic ecosystems",
-                "environmental governance/management",
                 "biosphere",
-                "ecological dynamics"
+                "aquatic ecosystems",
+                "terrestrial ecosystems",
+                "terrestrial hydrosphere"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566586-USGS_LTA.html",
             "language": [
@@ -1223130,9 +1223130,9 @@
             "identifier": "C2622842528-GES_DISC",
             "issued": "2021-07-19",
             "keyword": [
-                "microwave",
+                "spectral/engineering",
                 "earth science",
-                "spectral/engineering"
+                "microwave"
             ],
             "landingPage": "https://doi.org/10.5067/CBM5W8T7HHL6",
             "language": [
@@ -1226059,13 +1226059,13 @@
             "identifier": "C5862867-LARC_ASDC",
             "issued": "2007-09-06",
             "keyword": [
-                "spectral/engineering",
-                "atmosphere",
-                "aerosols",
-                "atmospheric radiation",
                 "infrared wavelengths",
                 "earth science",
-                "visible wavelengths"
+                "atmospheric radiation",
+                "atmosphere",
+                "visible wavelengths",
+                "aerosols",
+                "spectral/engineering"
             ],
             "landingPage": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_IIR-VALSTAGE1-V3-01_L1B-003.01",
             "language": [
@@ -1233189,8 +1233189,8 @@
             "issued": "2016-03-04",
             "keyword": [
                 "earth science",
-                "human dimensions",
-                "habitat conversion/fragmentation"
+                "habitat conversion/fragmentation",
+                "human dimensions"
             ],
             "landingPage": "https://doi.org/10.7927/H4Z899CG",
             "language": [
@@ -1245177,9 +1245177,9 @@
             "identifier": "https://data.nasa.gov/api/views/qghr-qkfw",
             "issued": "2022-10-20",
             "keyword": [
+                "batteries",
                 "degradation",
                 "phm",
-                "batteries",
                 "prognostics"
             ],
             "landingPage": "https://data.nasa.gov/d/qghr-qkfw",
@@ -1249805,11 +1249805,11 @@
             "issued": "2023-11-03",
             "keyword": [
                 "ecosystems",
-                "spectral/engineering",
-                "biosphere",
                 "earth science",
-                "lidar",
-                "vegetation"
+                "biosphere",
+                "spectral/engineering",
+                "vegetation",
+                "lidar"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/2056",
             "language": [
@@ -1252534,9 +1252534,9 @@
             "identifier": "C1339230298-GES_DISC",
             "issued": "2014-04-01",
             "keyword": [
+                "atmospheric chemistry",
                 "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
+                "earth science"
             ],
             "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1339230298-GES_DISC.html",
             "language": [
@@ -1259708,23 +1259708,23 @@
             "identifier": "nasa_genelab_GLDS-123_qr4c-tdt5",
             "issued": "2021-05-21",
             "keyword": [
-                "p-mtab-43160",
-                "data transformation",
-                "p-mtab-43159",
-                "p-mtab-43158",
-                "p-mtab-43157",
-                "p-mtab-43156",
-                "nucleic acid labeling protocol",
-                "nucleic acid hybridization",
                 "nucleic acid extraction protocol",
-                "normalization data transformation protocol",
-                "array scanning and feature extraction protocol",
-                "treatment protocol",
-                "hypergravity",
+                "nucleic acid hybridization",
+                "nucleic acid labeling protocol",
+                "p-mtab-43156",
+                "p-mtab-43157",
+                "p-mtab-43158",
+                "p-mtab-43159",
+                "p-mtab-43160",
+                "p-mtab-43161",
                 "genelab microarray data processing protocol",
-                "growth protocol",
+                "hypergravity",
+                "normalization data transformation protocol",
                 "p-mtab-43162",
-                "p-mtab-43161"
+                "treatment protocol",
+                "array scanning and feature extraction protocol",
+                "data transformation",
+                "growth protocol"
             ],
             "landingPage": "https://data.nasa.gov/d/qr4c-tdt5",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -1271128,16 +1271128,16 @@
             "identifier": "nasa-iss-data_2022-02-20_qw8y-5irh",
             "issued": "2022-02-20",
             "keyword": [
+                "international",
+                "coordinates",
+                "ephemeris",
+                "coords",
+                "station",
+                "space",
                 "trajectory",
-                "topo",
                 "location",
                 "iss",
-                "coordinates",
-                "space",
-                "station",
-                "international",
-                "ephemeris",
-                "coords"
+                "topo"
             ],
             "landingPage": "https://spotthestation.nasa.gov",
             "language": [
@@ -1284092,8 +1284092,8 @@
             "identifier": "https://data.nasa.gov/api/views/r588-f7pr",
             "issued": "2015-11-19",
             "keyword": [
-                "material science",
-                "outgassing"
+                "outgassing",
+                "material science"
             ],
             "landingPage": "https://outgassing.nasa.gov/",
             "modified": "2023-01-31",
@@ -1301641,15 +1301641,15 @@
             "identifier": "NASA-545",
             "issued": "2018-06-26",
             "keyword": [
-                "spice",
+                "mcs",
                 "marci",
                 "hirise",
-                "ctx",
-                "crism",
                 "pds",
+                "ctx",
                 "rss",
+                "crism",
                 "sharad",
-                "mcs"
+                "spice"
             ],
             "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
             "modified": "2020-01-29",
@@ -1302278,8 +1302278,8 @@
             "identifier": "C1392010615-LPDAAC_ECS",
             "issued": "2018-07-19",
             "keyword": [
-                "earth science",
                 "biosphere",
+                "earth science",
                 "vegetation"
             ],
             "landingPage": "https://doi.org/10.5067/VIIRS/VNP13A3.001",
@@ -1307574,15 +1307574,15 @@
             "identifier": "NASA-0000059",
             "issued": "2018-06-25",
             "keyword": [
-                "satellite imagery",
-                "landmark",
-                "nasa",
+                "imaging",
                 "landsat",
-                "elevation",
+                "nasa",
                 "wwhgd",
-                "geospatial",
                 "topography",
-                "imaging"
+                "geospatial",
+                "satellite imagery",
+                "landmark",
+                "elevation"
             ],
             "landingPage": "http://worldwind.arc.nasa.gov/java/",
             "modified": "2020-01-29",
@@ -1325806,10 +1325806,10 @@
             "identifier": "NASA-565",
             "issued": "2018-06-25",
             "keyword": [
-                "dictionary",
+                "data",
                 "pds",
                 "index",
-                "data"
+                "dictionary"
             ],
             "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
             "modified": "2020-01-29",
@@ -1334304,9 +1334304,9 @@
             "identifier": "C1427515664-SEDAC",
             "issued": "2017-10-13",
             "keyword": [
+                "population",
                 "earth science",
-                "human dimensions",
-                "population"
+                "human dimensions"
             ],
             "landingPage": "https://doi.org/10.7927/H47M05W2",
             "language": [
@@ -1351381,10 +1351381,10 @@
             "identifier": "https://data.nasa.gov/api/views/sb48-rsbc",
             "issued": "2022-10-20",
             "keyword": [
-                "degradation",
-                "phm",
                 "prognostics",
-                "batteries"
+                "batteries",
+                "degradation",
+                "phm"
             ],
             "landingPage": "https://data.nasa.gov/d/sb48-rsbc",
             "license": "https://www.usa.gov/government-works",
@@ -1367676,12 +1367676,12 @@
             "identifier": "NASA-341",
             "issued": "2018-06-25",
             "keyword": [
-                "spacesuit",
                 "emu",
-                "astronaut",
-                "3d model",
+                "spacesuit",
+                "spacewalk",
                 "suit",
-                "spacewalk"
+                "3d model",
+                "astronaut"
             ],
             "landingPage": "http://nasa3d.arc.nasa.gov/detail/aces",
             "modified": "2020-01-29",
@@ -1370336,10 +1370336,10 @@
             "identifier": "C2799465507-POCLOUD",
             "issued": "2022-07-21",
             "keyword": [
+                "oceans",
                 "ocean waves",
-                "sea surface topography",
                 "earth science",
-                "oceans"
+                "sea surface topography"
             ],
             "landingPage": "https://doi.org/10.5067/SWOT-SSH-2.0",
             "language": [
@@ -1370482,10 +1370482,10 @@
             "identifier": "NASA-0000032__1",
             "issued": "2018-06-25",
             "keyword": [
-                "optical",
                 "aerosol",
                 "depth",
-                "earth science"
+                "earth science",
+                "optical"
             ],
             "landingPage": "http://earthobservatory.nasa.gov/",
             "modified": "2020-01-29",
@@ -1372720,14 +1372720,14 @@
             "identifier": "C2762262185-ORNL_CLOUD",
             "issued": "2019-07-09",
             "keyword": [
+                "vegetation",
                 "atmosphere",
-                "earth science",
                 "atmospheric chemistry",
-                "land surface",
+                "atmospheric water vapor",
                 "biosphere",
-                "soils",
-                "vegetation",
-                "atmospheric water vapor"
+                "earth science",
+                "land surface",
+                "soils"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/899",
             "language": [
@@ -1373882,9 +1373882,9 @@
             "identifier": "C1419984463-SEDAC",
             "issued": "2017-06-28",
             "keyword": [
-                "human dimensions",
+                "earth science",
                 "environmental impacts",
-                "earth science"
+                "human dimensions"
             ],
             "landingPage": "https://doi.org/10.7927/H4FT8J0X",
             "language": [
@@ -1374987,12 +1374987,12 @@
             "identifier": "nasa_genelab_GLDS-5_ss5u-42b3",
             "issued": "2021-05-21",
             "keyword": [
-                "labeling protocol",
+                "data processing protocol",
                 "nucleic acid extraction protocol",
+                "scan protocol",
+                "labeling protocol",
                 "hybridization protocol",
-                "data processing protocol",
                 "sample collection protocol",
-                "scan protocol",
                 "simulated microgravity"
             ],
             "landingPage": "https://data.nasa.gov/d/ss5u-42b3",
@@ -1382402,9 +1382402,9 @@
             "identifier": "C3026778309-LARC_ASDC",
             "issued": "2024-04-24",
             "keyword": [
-                "atmosphere",
+                "clouds",
                 "earth science",
-                "clouds"
+                "atmosphere"
             ],
             "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/CLOUDHEIGHT_L2.001",
             "language": [
@@ -1386390,9 +1386390,9 @@
             "identifier": "C1993479681-GES_DISC",
             "issued": "2020-12-07",
             "keyword": [
+                "solar activity",
                 "sun-earth interactions",
-                "earth science",
-                "solar activity"
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/Y0HCCI3Z1JHD",
             "language": [
@@ -1411934,9 +1411934,9 @@
             "identifier": "NASA-EDI-1",
             "issued": "2015-07-08",
             "keyword": [
-                "edi",
                 "foia",
-                "ocio"
+                "ocio",
+                "edi"
             ],
             "landingPage": "https://data.nasa.gov/d/tey6-w6pm",
             "modified": "2024-05-22",
@@ -1413688,8 +1413688,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-5-ddr-ss-tec-ext1-v1.0",
             "issued": "2021-05-21",
             "keyword": [
-                "mars express",
-                "mars"
+                "mars",
+                "mars express"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-5-DDR-SS-TEC-EXT1-V1.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -1421801,9 +1421801,9 @@
             "identifier": "C2912123196-NSIDC_ECS",
             "issued": "2017-07-16",
             "keyword": [
-                "earth science",
                 "surface water",
-                "terrestrial hydrosphere"
+                "terrestrial hydrosphere",
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/WS83XMWHGEM9",
             "language": [
@@ -1426781,8 +1426781,8 @@
             "identifier": "C2927748781-ORNL_CLOUD",
             "issued": "2023-11-22",
             "keyword": [
-                "earth science",
                 "cryosphere",
+                "earth science",
                 "snow/ice"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/428",
@@ -1437856,9 +1437856,9 @@
             "issued": "2017-05-05",
             "keyword": [
                 "air quality",
-                "atmosphere",
-                "earth science",
                 "atmospheric chemistry",
+                "earth science",
+                "atmosphere",
                 "aerosols"
             ],
             "landingPage": "https://doi.org/10.5270/S5P-7g4iapn",
@@ -1440141,10 +1440141,10 @@
             "identifier": "C3155140117-SEDAC",
             "issued": "2024-07-10",
             "keyword": [
-                "population",
-                "earth science",
                 "human dimensions",
-                "human settlements"
+                "human settlements",
+                "population",
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.7927/brq1-xc29",
             "language": [
@@ -1444424,10 +1444424,10 @@
             "identifier": "NASA-316",
             "issued": "2018-06-25",
             "keyword": [
-                "international space station",
+                "astronaut",
                 "3d model",
                 "shuttle",
-                "astronaut"
+                "international space station"
             ],
             "landingPage": "http://nasa3d.arc.nasa.gov/detail/astronaut",
             "modified": "2020-01-29",
@@ -1451068,9 +1451068,9 @@
             "identifier": "C2210241616-SEDAC",
             "issued": "2011-09-26",
             "keyword": [
-                "population",
+                "human dimensions",
                 "earth science",
-                "human dimensions"
+                "population"
             ],
             "landingPage": "https://doi.org/10.7927/H4R20Z93",
             "language": [
@@ -1452476,8 +1452476,8 @@
             "identifier": "urn:nasa:pds:maven.rose.derived",
             "issued": "2021-05-21",
             "keyword": [
-                "mars",
-                "mars atmosphere and volatile evolution mission"
+                "mars atmosphere and volatile evolution mission",
+                "mars"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.rose.derived&version=1.10",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -1454549,15 +1454549,15 @@
             "identifier": "C1426999496-LANCEMODIS",
             "issued": "2017-10-11",
             "keyword": [
-                "atmospheric temperature",
-                "earth science",
-                "atmosphere",
+                "atmospheric phenomena",
                 "atmospheric chemistry",
+                "atmospheric temperature",
                 "atmospheric pressure",
-                "atmospheric water vapor",
                 "national geospatial data asset",
+                "earth science",
+                "atmospheric water vapor",
                 "ngda",
-                "atmospheric phenomena"
+                "atmosphere"
             ],
             "landingPage": "https://doi.org/10.5067/MODIS/MYD07_L2.NRT.061",
             "language": [
@@ -1467012,9 +1467012,9 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ds1-a-c-spice-6-v1.0_ugr4-gadp",
             "issued": "2018-06-26",
             "keyword": [
+                "19p/borrelly 1 (1904 y2)",
                 "deep space 1",
-                "9969 braille",
-                "19p/borrelly 1 (1904 y2)"
+                "9969 braille"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DS1-A%2FC-SPICE-6-V1.0",
             "modified": "2023-01-26",
@@ -1467229,10 +1467229,10 @@
             "identifier": "https://data.nasa.gov/api/views/ugxu-9kjx",
             "issued": "2022-10-20",
             "keyword": [
-                "batteries",
                 "degradation",
+                "prognostics",
                 "phm",
-                "prognostics"
+                "batteries"
             ],
             "landingPage": "https://data.nasa.gov/d/ugxu-9kjx",
             "license": "https://www.usa.gov/government-works",
@@ -1468585,11 +1468585,11 @@
             "identifier": "C1422086277-CDDIS",
             "issued": "1992-01-01",
             "keyword": [
-                "earth science",
                 "solid earth",
-                "geodetics",
                 "gravity/gravitational field",
-                "tectonics"
+                "earth science",
+                "tectonics",
+                "geodetics"
             ],
             "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_M_001",
             "language": [
@@ -1480788,8 +1480788,8 @@
             "issued": "2018-07-30",
             "keyword": [
                 "earth science",
-                "atmospheric water vapor",
-                "atmosphere"
+                "atmosphere",
+                "atmospheric water vapor"
             ],
             "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXIU.001",
             "language": [
@@ -1486676,8 +1486676,8 @@
             "issued": "2021-05-21",
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "zeta cas",
                 "vega",
+                "zeta cas",
                 "international rosetta mission"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67PCHURYUMOV-M26-V2.0",
@@ -1494567,20 +1494567,20 @@
             "identifier": "C1288937542-GES_DISC",
             "issued": "2020-01-30",
             "keyword": [
-                "atmospheric pressure",
-                "soils",
-                "surface thermal properties",
-                "surface water",
-                "terrestrial hydrosphere",
-                "atmosphere",
-                "land surface",
-                "precipitation",
-                "snow/ice",
                 "atmospheric radiation",
+                "atmosphere",
+                "atmospheric pressure",
                 "atmospheric temperature",
                 "atmospheric water vapor",
                 "atmospheric winds",
-                "earth science"
+                "earth science",
+                "land surface",
+                "precipitation",
+                "snow/ice",
+                "soils",
+                "surface thermal properties",
+                "surface water",
+                "terrestrial hydrosphere"
             ],
             "landingPage": "https://doi.org/10.5067/LWTYSMP3VM5Z",
             "language": [
@@ -1523382,9 +1523382,9 @@
             "issued": "2022-11-22",
             "keyword": [
                 "milling",
-                "degradation",
                 "phm",
-                "prognostics"
+                "prognostics",
+                "degradation"
             ],
             "landingPage": "https://data.nasa.gov/d/vjv9-9f3x",
             "license": "https://www.usa.gov/government-works",
@@ -1550836,10 +1550836,10 @@
             "identifier": "C3142513079-NSIDC_ECS",
             "issued": "2020-02-01",
             "keyword": [
+                "vegetation",
+                "topography",
                 "land surface",
                 "earth science",
-                "topography",
-                "vegetation",
                 "biosphere"
             ],
             "landingPage": "https://doi.org/10.5067/M9TPF6NWL53K",
@@ -1554360,8 +1554360,8 @@
             "issued": "2018-12-31",
             "keyword": [
                 "earth science",
-                "human dimensions",
-                "population"
+                "population",
+                "human dimensions"
             ],
             "landingPage": "https://doi.org/10.7927/H49C6VHW",
             "language": [
@@ -1564937,9 +1564937,9 @@
             "identifier": "C2884982401-ORNL_CLOUD",
             "issued": "2024-03-02",
             "keyword": [
-                "biosphere",
+                "vegetation",
                 "earth science",
-                "vegetation"
+                "biosphere"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/180",
             "language": [
@@ -1572340,15 +1572340,15 @@
             "identifier": "C2389101052-ORNL_CLOUD",
             "issued": "2019-12-17",
             "keyword": [
+                "geomorphic landforms/processes",
                 "ecosystems",
-                "biosphere",
-                "carbon flux",
+                "earth science",
                 "climate indicators",
-                "vegetation",
+                "carbon flux",
+                "biosphere",
                 "soils",
-                "land surface",
-                "earth science",
-                "geomorphic landforms/processes"
+                "vegetation",
+                "land surface"
             ],
             "landingPage": "https://doi.org/10.3334/ORNLDAAC/1650",
             "language": [
@@ -1582524,15 +1582524,15 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-nims-3-tube-v1.0_wmhi-adbr",
             "issued": "2021-05-21",
             "keyword": [
+                "ganymede",
+                "callisto",
                 "europa",
+                "sky",
+                "unknown",
+                "jupiter",
                 "j rings",
                 "io",
-                "callisto",
-                "unknown",
-                "galileo",
-                "ganymede",
-                "sky",
-                "jupiter"
+                "galileo"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-NIMS-3-TUBE-V1.0",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
@@ -1583484,19 +1583484,19 @@
             "issued": "2018-06-25",
             "keyword": [
                 "nrt",
-                "geospatial",
-                "power",
                 "climate",
-                "temperature",
                 "energy",
-                "time series",
+                "geospatial",
                 "google earth",
-                "renewable energy",
-                "near real time (nrt)",
-                "meteorology",
                 "irradiance",
-                "wind",
-                "solar"
+                "meteorology",
+                "near real time (nrt)",
+                "power",
+                "renewable energy",
+                "solar",
+                "temperature",
+                "time series",
+                "wind"
             ],
             "landingPage": "https://power.larc.nasa.gov/",
             "modified": "2024-02-02",
@@ -1590695,8 +1590695,8 @@
             "issued": "2003-01-07",
             "keyword": [
                 "aerosols",
-                "atmosphere",
                 "atmospheric water vapor",
+                "atmosphere",
                 "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/ASDC_DAAC/LASE/0003",
@@ -1594297,9 +1594297,9 @@
             "identifier": "C1684122432-GES_DISC",
             "issued": "2020-01-10",
             "keyword": [
-                "earth science",
+                "sun-earth interactions",
                 "solar activity",
-                "sun-earth interactions"
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/FDSY1RKARUSN",
             "language": [
@@ -1597968,13 +1597968,13 @@
             "identifier": "C2142771958-LPCLOUD",
             "issued": "2021-07-27",
             "keyword": [
-                "topography",
-                "biosphere",
-                "land surface",
                 "lidar",
+                "topography",
                 "vegetation",
                 "earth science",
-                "spectral/engineering"
+                "biosphere",
+                "spectral/engineering",
+                "land surface"
             ],
             "landingPage": "https://doi.org/10.5067/GEDI/GEDI02_A.002",
             "language": [
@@ -1610169,9 +1610169,9 @@
             "identifier": "C3280806477-GES_DISC",
             "issued": "2021-07-19",
             "keyword": [
-                "microwave",
+                "spectral/engineering",
                 "earth science",
-                "spectral/engineering"
+                "microwave"
             ],
             "landingPage": "https://doi.org/10.5067/57Q5OQ3VHUZ9",
             "language": [
@@ -1613546,9 +1613546,9 @@
             "identifier": "C3242613140-CDDIS",
             "issued": "1992-01-01",
             "keyword": [
-                "solid earth",
                 "earth science",
-                "tectonics"
+                "tectonics",
+                "solid earth"
             ],
             "landingPage": "https://doi.org/10.5067/GNSS/glonass_daily_g_001",
             "language": [
@@ -1622501,9 +1622501,9 @@
             "identifier": "DASHLINK_140",
             "issued": "2010-09-22",
             "keyword": [
-                "dashlink",
+                "ames",
                 "nasa",
-                "ames"
+                "dashlink"
             ],
             "landingPage": "http://www.grc.nasa.gov/WWW/cdtb/software/mapss.html",
             "modified": "2020-01-29",
@@ -1627643,14 +1627643,14 @@
             "identifier": "NASA-917",
             "issued": "2010-10-18",
             "keyword": [
-                "star catalog",
-                "gsfc",
                 "goddard space flight center",
-                "data visualization",
-                "smithsonian astrophysical observatory",
                 "hearsarc",
+                "astronomy",
+                "gsfc",
+                "star catalog",
                 "thermodynamics",
-                "astronomy"
+                "data visualization",
+                "smithsonian astrophysical observatory"
             ],
             "landingPage": "http://ds9.si.edu/site/Home.html",
             "modified": "2020-01-29",
@@ -1630888,13 +1630888,13 @@
             "identifier": "https://data.nasa.gov/api/views/xg3n-ngei",
             "issued": "2023-12-18",
             "keyword": [
-                "temperature",
                 "batteries",
-                "capacity",
                 "current",
                 "degradation",
                 "health management",
                 "prognostics",
+                "capacity",
+                "temperature",
                 "voltage"
             ],
             "landingPage": "https://data.nasa.gov/d/xg3n-ngei",
@@ -1674058,22 +1674058,22 @@
             "identifier": "C1692982090-GES_DISC",
             "issued": "2018-02-17",
             "keyword": [
-                "oceans",
-                "earth science",
-                "land surface",
-                "clouds",
-                "atmospheric water vapor",
                 "atmospheric temperature",
-                "surface radiative properties",
-                "surface thermal properties",
-                "ocean temperature",
                 "atmospheric radiation",
                 "atmospheric pressure",
                 "atmospheric chemistry",
-                "altitude",
+                "oceans",
+                "ocean temperature",
                 "atmosphere",
+                "altitude",
+                "surface thermal properties",
                 "air quality",
-                "precipitation"
+                "earth science",
+                "clouds",
+                "atmospheric water vapor",
+                "precipitation",
+                "surface radiative properties",
+                "land surface"
             ],
             "landingPage": "https://doi.org/10.5067/LESQUBLWS18H",
             "language": [
@@ -1677688,9 +1677688,9 @@
             "identifier": "urn:nasa:pds:ladee_ldex_yaxv-4vbx",
             "issued": "2018-06-26",
             "keyword": [
-                "ladee",
+                "dust",
                 "moon",
-                "dust"
+                "ladee"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aladee_ldex&version=1.2",
             "modified": "2023-01-26",
@@ -1678115,14 +1678115,14 @@
             "identifier": "NASA-0000054",
             "issued": "2018-06-25",
             "keyword": [
-                "galaxy",
-                "dem",
                 "planets",
                 "barycenters",
-                "space science",
-                "telnet",
+                "dem",
+                "exoplanet exploration",
+                "galaxy",
                 "nga",
-                "exoplanet exploration"
+                "space science",
+                "telnet"
             ],
             "landingPage": "https://data.nasa.gov/d/ybas-8ey9",
             "modified": "2020-01-29",
@@ -1685200,8 +1685200,8 @@
             "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcies-2-cr5-v1.0_yfd5-hjgb",
             "issued": "2018-06-26",
             "keyword": [
-                "international rosetta mission",
-                "solar wind"
+                "solar wind",
+                "international rosetta mission"
             ],
             "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCIES-2-CR5-V1.0",
             "modified": "2023-01-26",
@@ -1693442,8 +1693442,8 @@
             "identifier": "C2730520815-POCLOUD",
             "issued": "2022-04-21",
             "keyword": [
-                "oceans",
                 "ocean winds",
+                "oceans",
                 "earth science"
             ],
             "landingPage": "https://doi.org/10.5067/ESASA-L2W11",
@@ -1697459,15 +1697459,15 @@
             "identifier": "C2022275525-SEDAC",
             "issued": "2021-03-03",
             "keyword": [
+                "sustainability",
+                "socioeconomics",
                 "public health",
                 "land use/land cover",
                 "land surface",
-                "earth science",
                 "infrastructure",
-                "sustainability",
                 "human dimensions",
                 "economic resources",
-                "socioeconomics"
+                "earth science"
             ],
             "landingPage": "https://doi.org/10.7927/hn96-9703",
             "language": [
@@ -1710004,12 +1710004,12 @@
             "identifier": "https://data.nasa.gov/api/views/yvxp-ccvk",
             "issued": "2016-03-24",
             "keyword": [
-                "spaceapps",
-                "space apps",
-                "conference",
                 "sxsw",
                 "leads",
-                "company"
+                "company",
+                "spaceapps",
+                "space apps",
+                "conference"
             ],
             "landingPage": "https://data.nasa.gov/d/yvxp-ccvk",
             "language": [
```

